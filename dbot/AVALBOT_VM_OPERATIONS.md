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

At this stage, the App Registration does **not yet have the GitHub federated identity credential defined by this design, and no Azure RBAC authorization for VM operations has yet been granted as part of this operational channel**.

The next governed step is to establish the GitHub Actions → Microsoft Entra ID OIDC trust. Azure RBAC authorization must be treated as a separate subsequent step.

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

**Phase:** Initial design  
**Operational mode:** READ-ONLY  
**Production modifications:** None  
**SSH dependency:** None  
**Permanent Azure-side operational script:** None initially  
**Authentication model:** GitHub Actions OIDC → Microsoft Entra ID → Azure RBAC  
**Target:** `vm-avalbot` / Docker container `avalbot`
