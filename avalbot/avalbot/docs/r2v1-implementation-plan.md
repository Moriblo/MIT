---

# Initial Scope Definition (R2V1 Baseline)

## Purpose

This section defines the original approved scope for Release R2V1.

It represents the baseline against which future progress, scope changes and delivered functionality will be evaluated.

Operational tracking must occur exclusively through the GitHub Project **avalbot**.

This section is maintained to preserve the original planning history of the release.

---

## R2V1 Baseline Scope

| ID | Description | Status |
|----|-------------|---------|
| AB-001 | Create repository structure | ⬜ Planned |
| AB-002 | Create personas.json | ⬜ Planned |
| AB-003 | Create sessions.json | ⬜ Planned |
| AB-004 | Create persona_service.py | ⬜ Planned |
| AB-005 | Create session_service.py | ⬜ Planned |
| AB-006 | Create groq_service.py | ⬜ Planned |
| AB-007 | Create command_service.py | ⬜ Planned |
| AB-008 | Implement command $perfis | ⬜ Planned |
| AB-009 | Implement command $perfil | ⬜ Planned |
| AB-010 | Implement command $ajuda | ⬜ Planned |
| AB-011 | Implement command $whoami | ⬜ Planned |
| AB-012 | Integrate services with Discord | ⬜ Planned |
| AB-013 | Execute functional tests | ⬜ Planned |
| AB-014 | Publish Release R2V1 | ⬜ Planned |
| AB-015 | Prepare Azure environment | ⬜ Planned |
| AB-016 | Deploy AvalBot 24x7 on Azure | ⬜ Planned |

---

## Deliverables

At the conclusion of R2V1 the following artifacts must exist:

### Documentation

- README.md
- docs/personas.md
- docs/r2v1-implementation-plan.md

### Configuration

- personas.json
- sessions.json

### Source Code

```text
src/
├── main.py
├── command_service.py
├── discord_service.py
├── groq_service.py
├── persona_service.py
└── session_service.py
```

### Release Package

```text
releases/
└── r2v1/
```

### Infrastructure

- Azure VM provisioned
- Python runtime installed
- Environment variables configured
- Systemd service configured
- Automatic restart enabled

---

## Scope Governance

The Initial Scope Definition represents the official baseline of Release R2V1.

Changes introduced during development must be managed through the GitHub Project and should not retroactively modify this baseline.

Objectives:

- Preserve planning history.
- Provide traceability.
- Enable planned-versus-delivered analysis.
- Support future release retrospectives.

---

## Success Criteria

Release R2V1 will be considered complete when:

- All baseline items are delivered.
- All acceptance criteria are approved.
- Functional tests are successful.
- The bot is operational on Discord.
- Personas are externally configurable.
- User sessions are persisted.
- The solution is running continuously on Azure.

---
