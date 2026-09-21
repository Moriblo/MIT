# dbot Operation Catalog

**Catalog ID:** `dbot-operation-catalog`  
**Status:** ACTIVE  
**Owner Persona:** `dbot ChatGPT`  

---

## 1. Purpose

This document is the canonical registry of operational workflows exposed as capabilities through the `dbot ChatGPT` persona.

It functions as an operational allowlist.

A workflow existing under `.github/workflows/` is NOT automatically an authorized `dbot ChatGPT` capability.

---

## 2. Catalog Rules

Each registered capability MUST define:

- human alias;
- capability ID;
- workflow;
- canonical operational contract;
- lifecycle status;
- classification;
- available operations;
- trigger;
- target;
- HITL requirement.

Supported lifecycle states:

```text
ACTIVE
PLANNED
DISABLED
DEPRECATED
```

Definitions:

- `ACTIVE` — registered and available subject to its governance rules.
- `PLANNED` — registered for design purposes but NOT executable.
- `DISABLED` — previously registered but currently unavailable.
- `DEPRECATED` — retained for historical/reference purposes and not intended for new execution.

Registration does not override HITL.

---

## 3. Capability Selection

Human-friendly aliases MAY be used during conversation.

Example:

```text
A -> AvalBot VM Operations
B -> dbot Feature Update
```

Aliases are interaction shortcuts only.

The canonical identity of a capability is its `capability_id`.

Entering or mentioning an alias selects a capability context.

It does NOT constitute authorization to execute an operation.

---

## 4. Registered Capabilities

### A — AvalBot VM Operations

```text
capability_id: avalbot-vm-ops
status: ACTIVE
classification: READ-ONLY
workflow: .github/workflows/avalbot-vm-ops.yml
contract: dbot/AVALBOT_VM_OPERATIONS.md
trigger: workflow_dispatch
git_ref: main
environment: avalbot-vm-ops
target: Azure VM vm-avalbot
```

Approved conceptual operations:

```text
status
container-inspect
runtime-source
logs
```

Current executable implementation:

```text
runtime-source: ENABLED
status: NOT YET IMPLEMENTED
container-inspect: NOT YET IMPLEMENTED
logs: NOT YET IMPLEMENTED
```

Only `runtime-source` is currently exposed by the workflow choice input. Conceptual approval does not mean implementation or execution eligibility.

The workflow input MUST use a closed choice model. Its current implemented allowlist is:

```yaml
operation:
  type: choice
  required: true
  options:
    - runtime-source
```

Additional conceptual operations may be added only through a governed workflow change.

Arbitrary shell input is prohibited.

HITL:

```text
Human request
      |
      v
dbot ChatGPT presents operation and scope
      |
      v
Explicit human authorization
      |
      v
workflow_dispatch
```

Chat dispatch mapping for the implemented operation:

```text
capability_id: avalbot-vm-runtime-source
workflow: .github/workflows/avalbot-vm-ops.yml
ref: main
input: operation=runtime-source
ledger: .github/workflow-dispatch/commands.log
```

Expected production modification: `NONE`

The implementation MUST comply with `dbot/AVALBOT_VM_OPERATIONS.md`.

---

### B — dbot Feature Update

```text
capability_id: dbot-feature-update
status: PLANNED
classification: WRITE
workflow: .github/workflows/dbot_feature_update.yml
contract: NOT YET DEFINED
trigger: NOT YET APPROVED
environment: NOT YET APPROVED
target: NOT YET APPROVED
```

This capability is a placeholder for future governance and design.

It is NOT executable.

Its presence in this catalog MUST NOT be interpreted as authorization to create or execute the workflow.

Before this capability can transition from `PLANNED` to `ACTIVE`, a new explicit governance/HITL decision MUST define:

1. exact operations;
2. production impact;
3. permissions;
4. validation;
5. rollback;
6. failure handling;
7. secret protection;
8. Environment strategy;
9. reviewer requirements;
10. dispatch authorization model.

---

## 5. READ-ONLY vs WRITE

```text
READ-ONLY capability
       |
       +-- may use an explicitly approved READ-ONLY governance model

WRITE capability
       |
       +-- MUST receive its own explicit governance approval
           before becoming ACTIVE
```

READ-ONLY authorization MUST NOT propagate to WRITE capabilities.

---

## 6. Execution Eligibility

Before `dbot ChatGPT` dispatches any workflow, ALL of the following conditions MUST be true:

```text
Capability is registered
        AND
Capability status is ACTIVE
        AND
Requested operation is explicitly allowed
        AND
Applicable governance contract permits execution
        AND
Required HITL authorization has been obtained
```

Failure of any condition means the workflow MUST NOT be dispatched.

---

## 7. Catalog Integrity

Adding a capability to this document does not create execution authority.

Changing a capability from `PLANNED`, `DISABLED`, or `DEPRECATED` to `ACTIVE` is a governed change.

WRITE capabilities always require a new explicit governance decision before activation.
