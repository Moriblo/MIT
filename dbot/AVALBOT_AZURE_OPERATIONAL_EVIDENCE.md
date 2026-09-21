# AvalBot Azure Operational Evidence

**Status:** ACTIVE  
**Scope:** Azure/GitHub operational configuration and implementation evidence since the previous canonical artifact reconciliation  
**Secret policy:** This artifact contains identifiers and configuration evidence only. It MUST NOT contain access tokens, client secrets, SSH private keys, Groq API keys, Discord tokens, or `.env` contents.

---

## 1. Azure Target

```text
Subscription: Azure subscription 1
Subscription ID: 1c122157-db37-42f0-8c57-9e2ce43ebd36
Tenant ID: 5fd31207-d439-4a64-96cb-1eb98204656b
Resource Group: rg-avalbot
VM: vm-avalbot
Region: East US
OS: Ubuntu 24.04
Docker container: avalbot
```

## 2. Microsoft Entra Application

```text
App Registration: github-avalbot-vm-ops
Application (Client) ID: b9524e82-0bcf-448c-ba4a-c916a9b58aeb
App Registration Object ID: f603c46d-6ca4-448c-bf0c-821561008c0f
Service Principal Object ID: 3c96ac6c-4de3-42d5-a4b2-0a5530915c67
Tenant ID: 5fd31207-d439-4a64-96cb-1eb98204656b
Account type: Single tenant
Client secret: NONE
Certificate: NONE
```

These object identifiers represent different Entra objects and MUST NOT be conflated.

## 3. GitHub Environment

Environment: `avalbot-vm-ops`.

Implemented protection state:

- selected branches/tags policy with branch `main`;
- Required Reviewers OFF;
- Wait timer OFF;
- no custom protection rule;
- Environment is the OIDC identity boundary for V1.

The Environment holds the configured Azure identity identifiers and target resource names used by the workflows. Secret values are not reproduced in this evidence artifact.

## 4. Federated Identity Credential

```text
Name: github-Moriblo-MIT-avalbot-vm-ops
Scenario: GitHub Actions deploying Azure resources
Issuer: https://token.actions.githubusercontent.com
Organization: Moriblo
Organization ID: 99156792
Repository: MIT
Repository ID: 1314016054
Entity type: Environment
GitHub Environment: avalbot-vm-ops
Subject: repo:Moriblo@99156792/MIT@1314016054:environment:avalbot-vm-ops
Audience: api://AzureADTokenExchange
```

Azure's immutable organization/repository ID subject superseded the earlier design-time legacy subject based only on names.

## 5. Custom Azure Role

```text
Role name: AvalBot VM Read-Only Operations
Role Definition ID: 3fa02a55-2352-461c-956b-cd9b2156b8c5
Assignable scope: /subscriptions/1c122157-db37-42f0-8c57-9e2ce43ebd36
Actions:
  Microsoft.Compute/virtualMachines/runCommand/action
  Microsoft.Compute/virtualMachines/read
NotActions: []
DataActions: []
NotDataActions: []
```

No wildcard, diagnostic Run Command, Managed Run Command `virtualMachines/runCommands/*`, VMSS permission, or speculative permission was added.

### Portal creation incident

During final role creation the Azure Portal displayed a generic red `Erro. Tente novamente.` message. The operation was NOT blindly retried.

The subscription Activity Log was checked first and showed the corresponding `Create or update` operation as successful. Subscription IAM then showed the custom role and its JSON confirmed persistence.

Operational lesson: a portal presentation error must not be treated as proof that the backend operation failed. Verify Activity Log/resource state before retrying an idempotency-sensitive configuration operation.

The exact pre-creation and persisted post-creation JSON are stored separately under `dbot/evidence/azure/`.

## 6. VM-Scoped Role Assignment

```text
Role Assignment ID: 13b8d8b8-cea6-480b-93dd-c807880b4aab
Display Name: github-avalbot-vm-ops
Object Type: ServicePrincipal
Object ID: 3c96ac6c-4de3-42d5-a4b2-0a5530915c67
Role: AvalBot VM Read-Only Operations
Role Definition ID: /subscriptions/1c122157-db37-42f0-8c57-9e2ce43ebd36/providers/Microsoft.Authorization/roleDefinitions/3fa02a55-2352-461c-956b-cd9b2156b8c5
Scope: /subscriptions/1c122157-db37-42f0-8c57-9e2ce43ebd36/resourceGroups/rg-avalbot/providers/Microsoft.Compute/virtualMachines/vm-avalbot
Condition: none
```

The exported assignment JSON is stored separately under `dbot/evidence/azure/`.

## 7. OIDC/RBAC Smoke Test

Workflow: `.github/workflows/avalbot-vm-oidc-rbac-smoke-test.yml`.

Closed VM payload:

```bash
printf 'AVALBOT_OIDC_RBAC_OK\n'
```

The test does not inspect Docker, source, logs, `.env`, or application secrets and does not restart or modify AvalBot.

Execution history:

- `REQ-000001`: dispatcher failed before target dispatch because the inline Bash regex parsed the semicolon as shell syntax.
- Regex corrected to a variable-based pattern. A malformed intermediate repository write was caught by immediate post-write verification and corrected before any dispatcher execution.
- `REQ-000002`: dispatcher run `35565602785` SUCCESS; target smoke-test run `35565609963` SUCCESS.
- Target log returned `AVALBOT_OIDC_RBAC_OK`.

This empirically validated the complete GitHub OIDC/FIC/RBAC/Action Run Command chain and demonstrated that the custom role's two actions were sufficient for this invocation.

## 8. Dispatcher Implementation

Ledger: `.github/workflow-dispatch/commands.log`.

Dispatcher: `.github/workflows/dbot-workflow-dispatcher.yml`.

Record format:

```text
<request-id>;<capability-id>
```

Governance controls:

- one explicit human-authorized request line;
- append-only ledger semantics;
- unique request ID;
- strict syntax validation;
- capability allowlist;
- fixed workflow, ref, and inputs;
- no arbitrary shell command;
- no arbitrary workflow filename;
- no arbitrary ref;
- no token or secret in the request;
- no arbitrary operational parameter.

Current mappings:

```text
avalbot-oidc-rbac-smoke-test
  -> avalbot-vm-oidc-rbac-smoke-test.yml
  -> ref main
  -> no inputs

avalbot-vm-runtime-source
  -> avalbot-vm-ops.yml
  -> ref main
  -> operation=runtime-source
```

## 9. runtime-source Implementation and Troubleshooting

Workflow: `.github/workflows/avalbot-vm-ops.yml`.

### REQ-000003

Target run `35566619714` failed at runtime discovery with `Invalid source byte count.`

Root cause: host-shell redirection attempted to open a container-local path before `docker exec`.

Correction: execute `wc -c "$CONTAINER_FILE"` inside the container and parse its first field.

### REQ-000004

Dispatcher run `35567041184` succeeded. Target run `35567046939` advanced through discovery but failed source reconstruction with `base64: invalid input`.

Evidence obtained before failure:

```text
Runtime source: /app/mybot_v3.py
Expected bytes: 5538
Expected SHA-256: 7bc83690a8748f7cb21b7d503c7ff5c1bfd6841b6ff9d493612bcd712e025725
```

Root cause: Azure Run Command framing text was being concatenated with the Base64 payload.

Correction: explicit `AVALBOT_CHUNK_BEGIN` / `AVALBOT_CHUNK_END` envelope, exactly-one marker checks, extraction only between markers, CR/LF removal, non-empty payload check, and per-chunk Base64 validation.

### REQ-000005

Dispatcher and target run completed successfully. Complete source reconstruction and SHA-256 validation succeeded, and the effective literal model was `openai/gpt-oss-20b`.

A cleanliness defect remained in the summary step: Markdown backticks inside double-quoted Bash `echo` strings were interpreted as command substitutions. This did not invalidate the reconstructed source, hash, or model evidence, but produced dirty summary-step log messages.

Correction: summary generation changed to `printf` with single-quoted Markdown format strings and runtime-derived values supplied only as `%s` arguments.

### REQ-000006 — final clean validation

Ledger request:

```text
REQ-000006;avalbot-vm-runtime-source
```

Dispatcher run `35568866562`: SUCCESS.

Target run `35568872518`: SUCCESS.

All steps completed successfully, including the corrected summary step.

Final verified runtime evidence:

```text
Container: avalbot
Running: true
Runtime command: ["python","-u","mybot_v3.py"]
Runtime source: /app/mybot_v3.py
Source bytes: 5538
Source SHA-256: 7bc83690a8748f7cb21b7d503c7ff5c1bfd6841b6ff9d493612bcd712e025725
Complete source reconstructed and SHA-256 verified: YES
Effective configured GROQ_MODEL: openai/gpt-oss-20b
```

Final log review found none of the previously observed error signatures:

```text
##[error]
command not found
No such file or directory
base64: invalid input
```

## 10. Runtime / Repository Drift

The verified production container executes `mybot_v3.py`.

The repository Dockerfile still references `mybot_v2.py`.

This is a documented state divergence. The evidence reconciliation does NOT authorize or perform a Dockerfile, image, container, or production change.

## 11. Security Outcome

Throughout the implemented workflow:

- no client secret was created for the Entra App Registration;
- no SSH private key is required by the GitHub operational channel;
- no unrestricted `docker inspect` is used;
- container environment variables are not intentionally read;
- `.env` is not intentionally read;
- complete runtime source is reconstructed only ephemerally on the GitHub runner and is not printed or uploaded as an artifact;
- no production restart, stop, rebuild, file modification, package installation, or Azure resource mutation is part of the V1 runtime-source operation.

The technical capability of Azure Action Run Command to mutate the VM remains distinct from the READ-ONLY operational contract enforced by the closed workflow.
