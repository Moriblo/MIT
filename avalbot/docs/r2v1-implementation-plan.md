# Initial Scope Definition (R2V1 Baseline)

## Purpose

This section defines the original approved scope for Release R2V1.

It represents the baseline against which future progress, scope changes and delivered functionality will be evaluated.

Operational tracking must occur exclusively through the GitHub Project **avalbot**.

This section is maintained to preserve the original planning history of the release.

---

## R2V1 Baseline Scope

### Phase F1 - Planning & Repository Setup

| ID | Description | Status |
|----|-------------|---------|
| AB-001 | Create GitHub Project "avalbot" | ✅ Completed |
| AB-002 | Create README.md | ✅ Completed |
| AB-003 | Create repository structure | 🟨 In Progress |

---

### Phase F2 - Persona Definition

| ID | Description | Status |
|----|-------------|---------|
| AB-004 | Create docs/personas.md | ⬜ Planned |

---

### Phase F3 - Configuration Structure

| ID | Description | Status |
|----|-------------|---------|
| AB-005 | Create personas.json | ⬜ Planned |
| AB-006 | Create sessions.json | ⬜ Planned |

---

### Phase F4 - Core Services

| ID | Description | Status |
|----|-------------|---------|
| AB-007 | Create persona_service.py | ⬜ Planned |
| AB-008 | Create session_service.py | ⬜ Planned |
| AB-009 | Create groq_service.py | ⬜ Planned |

---

### Phase F5 - Command Layer

| ID | Description | Status |
|----|-------------|---------|
| AB-010 | Create command_service.py | ⬜ Planned |
| AB-011 | Implement command $perfis | ⬜ Planned |
| AB-012 | Implement command $perfil | ⬜ Planned |
| AB-013 | Implement command $ajuda | ⬜ Planned |
| AB-014 | Implement command $whoami | ⬜ Planned |

---

### Phase F6 - Discord Integration

| ID | Description | Status |
|----|-------------|---------|
| AB-015 | Integrate services with Discord | ⬜ Planned |

---

### Phase F7 - Testing

| ID | Description | Status |
|----|-------------|---------|
| AB-016 | Execute functional tests | ⬜ Planned |

---

### Phase F8 - Release Packaging

| ID | Description | Status |
|----|-------------|---------|
| AB-017 | Publish Release R2V1 | ⬜ Planned |

---

### Phase F9 - Azure Deployment

| ID | Description | Status |
|----|-------------|---------|
| AB-018 | Prepare Azure environment | ⬜ Planned |
| AB-019 | Deploy AvalBot 24x7 on Azure | ⬜ Planned |

---

## Deliverables

At the conclusion of R2V1 the following artifacts must exist.

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

- Preserve planning history
- Provide traceability
- Enable planned-versus-delivered analysis
- Support future release retrospectives

---

## Success Criteria

Release R2V1 will be considered complete when:

- All baseline items are delivered
- All acceptance criteria are approved
- Functional tests are successful
- The bot is operational on Discord
- Personas are externally configurable
- User sessions are persisted
- The solution is running continuously on Azure

