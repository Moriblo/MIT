# AvalBot VM Operations

## Purpose

This document describes the controlled operational channel used to inspect the Azure VM and Docker runtime hosting AvalBot.

The operational workflow is implemented by:

`.github/workflows/avalbot-vm-ops.yml`

The initial implementation is intentionally **READ-ONLY**.

Its purpose is to provide controlled visibility into the production environment without modifying, restarting, rebuilding, stopping, or otherwise changing the running AvalBot service.

---

## Architecture

```text
Human authorization / HITL
        |
        v
GitHub Actions
.github/workflows/avalbot-vm-ops.yml
        |
        | OIDC authentication
        v
Microsoft Entra ID / Azure
        |
        | Azure RBAC
        v
Azure VM Run Command
        |
        v
vm-avalbot
        |
        v
Docker
        |
        v
avalbot
```

The workflow does not require an interactive SSH session.

No SSH private key is stored in GitHub for this operational channel.

No permanent operational script is initially installed on the Azure VM.

The operational commands are defined and version-controlled through the GitHub workflow.

---

## Authentication

GitHub Actions authenticates to Azure using OpenID Connect (OIDC).

The intended authentication model avoids storing long-lived Azure credentials or SSH private keys in the repository.

The GitHub workflow receives a temporary identity token, which Microsoft Entra ID validates before Azure RBAC determines whether the requested Azure operation is authorized.

Configuration identifiers such as the Azure Tenant ID, Subscription ID, and Client ID are not application credentials.

---

## Azure Command Execution Model

Version 1 uses **Azure Action Run Command** as the VM command execution mechanism.

Action Run Command was selected because the initial operational channel is intended for small, one-time diagnostic scripts and controlled READ-ONLY inspection of the running environment.

**Managed Run Command is deliberately not used in Version 1.** It is more appropriate when recurrent execution, multiple scripts, deployment-time execution, sequencing, long-running commands, or reusable published commands are required.

Action Run Command executes the diagnostic script through the Azure VM Agent. No permanent operational script is initially installed on the VM.

Action Run Command has an important output limitation: only the last **4,096 bytes** of command output are returned.

This limitation directly affects the `runtime-source` operation. The implementation MUST NOT assume that printing the runtime Python file through standard output guarantees retrieval of the complete source. A mechanism that preserves and verifies the complete runtime source must be defined before `runtime-source` can report a source file as complete.

The use of Action Run Command does not itself make an operation READ-ONLY. READ-ONLY behavior is enforced by the closed set of diagnostic operations defined by this contract and implemented by the workflow.

---

## Operational Principle

The workflow follows a **closed-command model**.

Users cannot submit arbitrary shell commands to the VM.

Only explicitly defined operations can be selected.

The initial operational scope is:

| Operation | Purpose |
|---|---|
| `status` | Inspect VM/container operational status |
| `container-inspect` | Inspect selected runtime metadata without exposing environment variables |
| `runtime-source` | Identify the Python program actually executed by the `avalbot` container and retrieve its complete source |
| `logs` | Retrieve a controlled portion of the AvalBot runtime logs |

---

## `runtime-source`

`runtime-source` must determine the source file from the actual running container rather than assuming that a particular repository version is deployed.

Conceptually:

```text
avalbot
   |
   v
running process
   |
   v
python -u <runtime-file>.py
             |
             v
identify actual file
             |
             v
retrieve complete runtime source
```

The complete Python source executed in production must be returned whenever technically possible.

The implementation must account for output-size limitations of the Azure command execution mechanism and must not silently present truncated source as complete source.

---

## READ-ONLY Boundary

Version 1 of `avalbot-vm-ops.yml` is strictly intended for diagnostic operations.

The workflow MUST NOT provide operations that:

- stop the `avalbot` container;
- start or restart the `avalbot` container;
- remove containers;
- build Docker images;
- remove Docker images;
- execute `git pull`;
- modify repository files;
- modify files inside the container;
- modify `.env`;
- display secrets or environment credentials;
- install or remove operating-system packages;
- reboot or shut down the VM;
- modify Azure resources;
- execute arbitrary commands supplied by a workflow user.

Any future operation capable of changing the production environment requires a new governance decision and an explicit HITL authorization before implementation.

---

## Secret Protection

Operational diagnostics must not expose:

- `GROQ_API_KEY`;
- Discord bot token;
- `.env` contents;
- SSH private keys;
- Azure credentials;
- other runtime secrets.

Commands such as unrestricted `docker inspect` must not be used when their output could expose container environment variables.

Only explicitly selected metadata should be returned.

---

## Human-in-the-Loop Governance

The existence of an automation mechanism does not constitute authorization to modify production.

Human authorization MUST NOT be inferred.

The initial workflow is limited to diagnostic operations.

Future production-changing capabilities, if implemented, must introduce explicit HITL checkpoints separating at least:

```text
DIAGNOSE
   |
   | READ-ONLY
   v
PREPARE
   |
   | HITL approval required
   v
CHANGE
   |
   v
VALIDATE
   |
   +----> ROLLBACK, when required
```

No future extension of this workflow should bypass the applicable HITL checkpoint.

---

## Source of Truth

Three different sources provide different types of evidence:

### GitHub

Represents the version-controlled application and operational definitions.

### Azure / deployment documentation

Represents infrastructure configuration and deployment history.

### Running VM/container

Represents the actual production runtime.

When determining what AvalBot is currently executing, the **running container is the runtime source of truth**.

Repository content must not be assumed to represent the currently deployed runtime without verification.

---

## Version 1 Scope

The first version of the operational channel will contain only:

```text
status
container-inspect
runtime-source
logs
```

No production-changing capability is part of Version 1.

---

## Azure Target Configuration

The Version 1 operational channel targets the following Azure resources, confirmed directly in the Azure Portal:

```text
AZURE_TENANT_ID       = 5fd31207-d439-4a64-96cb-1eb98204656b
AZURE_SUBSCRIPTION_ID = 1c122157-db37-42f0-8c57-9e2ce43ebd36
AZURE_RESOURCE_GROUP  = rg-avalbot
AZURE_VM_NAME         = vm-avalbot
```

These values are resource and directory identifiers, not authentication credentials.

No Azure access token, client secret, SSH private key, Groq API key, Discord token, or other secret may be stored in this document.

---

## Microsoft Entra Workload Identity

A dedicated Microsoft Entra ID App Registration has been created for the AvalBot GitHub-to-Azure operational channel.

```text
AZURE_APP_REGISTRATION = github-avalbot-vm-ops
AZURE_CLIENT_ID        = b9524e82-0bcf-448c-ba4a-c916a9b58aeb
AZURE_OBJECT_ID        = f603c46d-6ca4-448c-bf0c-821561008c0f
AZURE_TENANT_ID        = 5fd31207-d439-4a64-96cb-1eb98204656b
ACCOUNT_TYPE           = Single tenant
CLIENT_SECRET          = NONE
```

The application is enabled and no client secret or certificate was created.

The App Registration now has the approved GitHub Federated Identity Credential and the VM-scoped custom Azure RBAC assignment. Their persisted identifiers and evidence are recorded below and in the Azure evidence artifacts.

---

## Approved GitHub-to-Azure OIDC Architecture

The Version 1 GitHub-to-Azure operational authentication and authorization path is approved as follows:

```text
workflow_dispatch
       |
       v
GitHub Environment: avalbot-vm-ops
       |
       v
GitHub OIDC
       |
       v
Federated Identity Credential
       |
       v
Microsoft Entra App Registration:
github-avalbot-vm-ops
       |
       v
Minimum required Azure RBAC
       |
       v
vm-avalbot
```

The intended federated identity subject for the GitHub Environment context is:

```text
repo:Moriblo@99156792/MIT@1314016054:environment:avalbot-vm-ops
```

### Governance Boundaries

- `workflow_dispatch` is the human-trigger mechanism for Version 1. The operational workflow must not be automatically triggered by `push`, `pull_request`, scheduled execution, or other automatic repository events.
- The GitHub Environment defines the GitHub/OIDC execution context. It does not itself grant Azure authorization.
- The Federated Identity Credential establishes trust between the approved GitHub identity context and the Microsoft Entra App Registration. It does not itself define the operations permitted against the VM.
- Azure RBAC is a separate authorization layer and must grant only the minimum permissions required for the approved READ-ONLY operational scope.
- Creation of the GitHub Environment, creation of the Federated Identity Credential, and assignment of Azure RBAC permissions remain separate implementation steps subject to their applicable HITL checkpoints.

---

## Human Dispatch and V1 Authorization Model

Version 1 uses `workflow_dispatch` as its explicit human-trigger mechanism.

The human authorization may be materialized through the GitHub UI or through an approved conversational interface capable of dispatching the registered workflow.

```text
Human authorization
        |
        +---- GitHub UI --------+
        |                       |
        +---- Chat interface ---+
                                |
                                v
                         workflow_dispatch
                                |
                                v
                       avalbot-vm-ops.yml
```

When the Chat interface is used, the intended interaction is:

```text
Human
  |
  | requests an operation
  v
dbot ChatGPT
  |
  | presents operation and scope
  v
Human
  |
  | explicit authorization
  v
GitHub workflow_dispatch
  |
  | operation=<approved closed choice>
  | ref=main
  v
avalbot-vm-ops.yml
```

Human authorization MUST NOT be inferred from the request to investigate, discuss, prepare, or explain an operation.

### V1 Operational Chain

```text
Human
  |
  v
workflow_dispatch
[explicit HITL]
  |
  v
avalbot-vm-ops.yml
[V1: closed READ-ONLY operations]
  |
  v
branch: main
  |
  v
Environment: avalbot-vm-ops
[identity boundary]
  |
  v
GitHub OIDC
  |
  v
Federated Identity Credential
  |
  v
github-avalbot-vm-ops
  |
  v
Minimum required Azure RBAC
  |
  v
Azure Action Run Command
  |
  v
vm-avalbot
```

The READ-ONLY classification belongs to the operational contract implemented by `avalbot-vm-ops.yml`.

The GitHub Environment, OIDC, Federated Identity Credential, Azure RBAC, and Azure Action Run Command are NOT inherently READ-ONLY.

### GitHub Environment Role

For Version 1, the `avalbot-vm-ops` GitHub Environment is an identity boundary for the OIDC trust.

`workflow_dispatch` provides the explicit human trigger for the approved READ-ONLY operations.

Version 1 does not require a second approval through Environment Required Reviewers.

The Environment restricts eligible deployment branches/tags to the approved V1 branch policy: branch `main`.

### WRITE Evolution Rule

Any future WRITE operation requires a new explicit governance/HITL decision before it can be introduced as an executable capability.

That decision MUST separately evaluate stronger protection mechanisms, including:

- mandatory Environment reviewers;
- segregation of duties;
- a dedicated production-change GitHub Environment;
- minimum required permissions;
- validation;
- rollback;
- failure handling;
- secret protection.

Authorization of the V1 READ-ONLY workflow MUST NOT be interpreted as authorization for any future WRITE operation.

---

## Implemented Configuration and Validation State

The V1 operational chain is now implemented and empirically validated.

### GitHub Environment

`avalbot-vm-ops` is configured with:

- selected branch policy: `main`;
- Required Reviewers: OFF for V1;
- Wait timer: OFF;
- custom protection rules: none;
- Environment used as the OIDC identity boundary.

Environment configuration supplies the Azure identity identifiers and target resource names required by the workflows. No client secret is used.

### Federated Identity Credential

The App Registration `github-avalbot-vm-ops` uses the immutable GitHub organization/repository ID subject generated by Azure:

```text
name: github-Moriblo-MIT-avalbot-vm-ops
issuer: https://token.actions.githubusercontent.com
subject: repo:Moriblo@99156792/MIT@1314016054:environment:avalbot-vm-ops
audience: api://AzureADTokenExchange
```

The earlier design-time legacy subject `repo:Moriblo/MIT:environment:avalbot-vm-ops` is superseded by this persisted immutable-ID subject.

### Azure RBAC

Custom role:

```text
Role name: AvalBot VM Read-Only Operations
Role Definition ID: 3fa02a55-2352-461c-956b-cd9b2156b8c5
Actions:
  Microsoft.Compute/virtualMachines/runCommand/action
  Microsoft.Compute/virtualMachines/read
```

The role is assigned only at the `vm-avalbot` VM scope to the Service Principal for `github-avalbot-vm-ops`.

```text
Service Principal Object ID: 3c96ac6c-4de3-42d5-a4b2-0a5530915c67
Role Assignment ID: 13b8d8b8-cea6-480b-93dd-c807880b4aab
Scope: /subscriptions/1c122157-db37-42f0-8c57-9e2ce43ebd36/resourceGroups/rg-avalbot/providers/Microsoft.Compute/virtualMachines/vm-avalbot
```

The successful smoke test empirically demonstrated that these two role actions are sufficient for the approved Action Run Command invocation. Permissions were not expanded speculatively.

### Smoke Test

`.github/workflows/avalbot-vm-oidc-rbac-smoke-test.yml` validates the complete authentication/authorization path with a closed non-application-mutating marker command.

Validated chain:

```text
workflow_dispatch
  -> Environment avalbot-vm-ops
  -> GitHub OIDC
  -> Entra FIC
  -> Service Principal
  -> custom Azure RBAC
  -> Azure Action Run Command
  -> vm-avalbot
```

Successful target run: `35565609963`.

### Chat-to-Workflow Dispatcher

The implemented conversational dispatch path uses:

- ledger: `.github/workflow-dispatch/commands.log`;
- dispatcher: `.github/workflows/dbot-workflow-dispatcher.yml`;
- strict record format: `<request-id>;<capability-id>`;
- append-only human-authorized requests;
- fixed capability-to-workflow mappings;
- no arbitrary shell command, workflow filename, ref, token, secret, or free-form parameter from the ledger.

Current mappings include the smoke test and `avalbot-vm-runtime-source`.

### Implemented runtime-source Operation

Although four operations were conceptually approved for V1, only `runtime-source` is currently executable in `avalbot-vm-ops.yml`.

The operation:

1. authenticates with OIDC;
2. validates tenant/subscription context;
3. confirms the fixed `avalbot` container is running;
4. reads only `.State.Running` and `.Config.Cmd` from Docker metadata;
5. derives the actual Python runtime file from the running container;
6. obtains VM-side byte count and SHA-256;
7. retrieves source in 1,800-byte Base64 chunks wrapped in explicit begin/end markers;
8. validates each chunk before reconstruction;
9. reconstructs the complete source only on the ephemeral GitHub runner;
10. requires reconstructed byte count and SHA-256 to match the container values;
11. extracts only a supported literal `GROQ_MODEL` assignment;
12. does not print or persist the complete runtime source.

### Verified Production Runtime

Final clean validation request: `REQ-000006;avalbot-vm-runtime-source`.

Dispatcher run: `35568866562` — SUCCESS.

Target AvalBot VM Operations run: `35568872518` — SUCCESS.

Verified evidence:

```text
Container: avalbot
Runtime command: ["python","-u","mybot_v3.py"]
Runtime source: /app/mybot_v3.py
Source bytes: 5538
Source SHA-256: 7bc83690a8748f7cb21b7d503c7ff5c1bfd6841b6ff9d493612bcd712e025725
Complete reconstruction integrity: VERIFIED
Effective configured GROQ_MODEL: openai/gpt-oss-20b
```

No container environment variables or `.env` files were intentionally read.

This runtime evidence also establishes repository/runtime drift: the repository Dockerfile still references `mybot_v2.py`, while the verified production container executes `mybot_v3.py`. This fact is documented; no Dockerfile or production change is authorized by this reconciliation.

### Troubleshooting History

The implementation produced several controlled failures that materially improved the final contract:

1. **Dispatcher regex parsing** — an inline Bash regex containing a semicolon caused a parser failure. The regex was moved to a variable before evaluation. A first corrective repository write was detected as malformed during post-write verification and was immediately restored/corrected without triggering execution.
2. **Container-local byte count** — host-shell redirection attempted to resolve the container path on the VM host. The byte count was changed to execute `wc -c` inside the container.
3. **Azure output framing** — Azure Run Command framing text contaminated the Base64 stream. Explicit `AVALBOT_CHUNK_BEGIN/END` envelopes, marker-count checks, payload extraction, and per-chunk Base64 validation were introduced.
4. **Step Summary shell substitution** — Markdown backticks inside double-quoted Bash `echo` strings caused command substitution attempts. The summary was changed to `printf` with single-quoted format strings and runtime values passed as arguments.
5. **Final clean run** — REQ-000006 completed with no `command not found`, `No such file or directory`, `base64: invalid input`, or GitHub error markers.

Detailed Azure evidence and persisted JSON are maintained in `dbot/AVALBOT_AZURE_OPERATIONAL_EVIDENCE.md` and `dbot/evidence/azure/`.

---

## Change Governance

Changes to the operational scope must be documented before implementation.

Any proposal to introduce write operations must clearly identify:

1. the new operation;
2. its production impact;
3. required Azure permissions;
4. failure modes;
5. rollback procedure;
6. secret-exposure risks;
7. required HITL checkpoint.

The operational workflow must remain auditable through GitHub version history.

---

## Current Status

**Phase:** V1 implemented and end-to-end validated  
**Operational mode:** READ-ONLY  
**Human trigger:** `workflow_dispatch`  
**GitHub Environment:** `avalbot-vm-ops` — configured; selected branch `main`; Required Reviewers OFF; Wait timer OFF  
**Operation catalog:** `dbot/DBOT_OPERATION_CATALOG.md`  
**Operational persona:** `dbot/PERSONA_dbot_ChatGPT_v1.0.md`  
**Production modifications:** None  
**SSH dependency:** None  
**Permanent Azure-side operational script:** None initially  
**Authentication model:** GitHub Actions OIDC → Microsoft Entra ID → Azure RBAC  
**Target:** `vm-avalbot` / Docker container `avalbot`  
**Currently enabled operation:** `runtime-source`  
**Final validation:** `REQ-000006` / target run `35568872518` — SUCCESS
