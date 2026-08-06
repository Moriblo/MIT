````markdown
# AvalBot

> Multi-Persona AI Platform powered by Discord + Groq

![Status](https://img.shields.io/badge/status-R2V1%20Design-blue)
![Platform](https://img.shields.io/badge/platform-Discord-5865F2)
![LLM](https://img.shields.io/badge/LLM-Groq-orange)
![Hosting](https://img.shields.io/badge/Hosting-Azure-0078D4)

---

# Vision

AvalBot is a multi-persona conversational platform designed to explore Generative AI, AI Governance, Digital Specialists and Human-AI Interaction.

The platform allows a single Discord bot to dynamically assume different expert personas, each with its own identity, expertise, communication style and knowledge domain.

Users can:

- Interact with specialized digital experts.
- Compare perspectives from different personas.
- Explore AI Governance concepts.
- Experiment with prompt engineering techniques.
- Evaluate multi-agent conversational patterns.
- Build a foundation for future AI specialist marketplaces.

---

# Project Context

AvalBot is being developed as part of the practical activities associated with studies conducted in the MIT program.

The project serves as a laboratory for:

- Generative AI
- AI Governance
- Conversational Systems
- Prompt Engineering
- Human-AI Interaction
- Specialized AI Agents

---

# Core Principles

## Simplicity

One bot.

One server.

One primary channel.

Multiple personas.

---

## Extensibility

New personas must be created without modifying application code.

---

## Governance

Identity and authorization must be delegated to Discord.

No internal credential management.

---

## Scalability

The architecture must support future migration toward:

- Multi-agent systems
- Marketplace of specialists
- Additional communication channels
- Enterprise governance

---

# Initial Personas

## 🧭 Aval

### Purpose

General-purpose assistant.

### Characteristics

- Neutral
- Helpful
- Balanced
- Didactic
- Generalist

### Default Profile

All new users receive this profile automatically.

---

## 🏛️ Governança IA

### Purpose

AI Governance Specialist.

### Expertise

- Responsible AI
- Trustworthy AI
- AI Risk Management
- Compliance
- LGPD
- ISO 42001
- NIST AI RMF
- AI Regulation
- Ethics

### Communication Style

- Executive
- Strategic
- Structured
- Consultative

---

# Architecture

```text
Discord
   │
   ▼
AvalBot
   │
   ├── Command Service
   │
   ├── Persona Service
   │
   ├── Session Service
   │
   └── Groq Service
            │
            ▼
          Groq
```

---

# Repository Structure

```text
MIT/
│
└── avalbot/
    │
    ├── README.md
    ├── personas.json
    ├── sessions.json
    │
    ├── src/
    │   ├── main.py
    │   ├── command_service.py
    │   ├── discord_service.py
    │   ├── groq_service.py
    │   ├── persona_service.py
    │   └── session_service.py
    │
    ├── docs/
    │   ├── architecture.md
    │   ├── roadmap.md
    │   ├── personas.md
    │   └── business-rules.md
    │
    └── releases/
        ├── r2v1/
        ├── r2v2/
        ├── r2v3/
        └── r3v0/
```

---

# Personas Configuration

Personas are stored externally.

File:

```text
personas.json
```

Example:

```json
{
  "default": {
    "name": "Aval",
    "emoji": "🧭",
    "description": "General assistant",
    "prompt": "..."
  },

  "governanca": {
    "name": "Governança IA",
    "emoji": "🏛️",
    "description": "AI Governance Specialist",
    "prompt": "..."
  }
}
```

---

# User Sessions

User preferences are persisted locally.

File:

```text
sessions.json
```

Example:

```json
{
  "123456789": {
    "active_profile": "default"
  },

  "987654321": {
    "active_profile": "governanca"
  }
}
```

---

# Business Rules

## RB001

Every user has exactly one active profile.

---

## RB002

New users receive:

🧭 Aval

as their default profile.

---

## RB003

Questions without commands use the active profile.

---

## RB004

Command:

```text
$perfil <profile>
```

changes the active profile.

---

## RB005

Command:

```text
$perfil <profile> <question>
```

uses the specified profile without changing the active profile.

---

## RB006

Command:

```text
$compare
```

never changes the active profile.

---

## RB007

Discord is the only identity provider.

---

## RB008

No user credentials are stored by AvalBot.

---

## RB009

Authorization is based on Discord Roles.

---

## RB010

No hardcoded user lists are allowed.

---

## RB011

All personas must be externally configured.

---

# Commands

## List Available Profiles

```text
$perfis
```

---

## General Help

```text
$ajuda
```

---

## Persona Help

```text
$ajuda governanca
```

---

## Change Active Profile

```text
$perfil governanca
```

---

## One-Time Question

```text
$perfil governanca What do you think about AI governance?
```

---

## Active Profile Question

```text
What do you think about AI governance?
```

---

## User Information

```text
$whoami
```

Displays:

- Discord username
- Active profile
- Discord roles
- Available personas

---

# Hosting Strategy

## Development

Local machine.

---

## Validation

Discord Test Server.

---

## Production

Microsoft Azure Virtual Machine.

### Objective

Provide:

- 24x7 availability
- Continuous operation
- Centralized deployment
- Single execution environment

### Initial Deployment Target

Azure VM

Ubuntu Linux

Python Runtime

Systemd Service

---

# Observability Roadmap

Future releases will support:

- Usage statistics
- Persona metrics
- Token consumption
- User activity
- Audit logs

---

# Release Roadmap

## R2V1

### Foundation

Features:

- External personas
- User sessions
- Active profile
- $perfil
- $perfis
- $ajuda
- $whoami

Status:

🚧 In Design

---

## R2V2

### Governance

Features:

- Discord Roles
- Authorization
- Structured logs
- Audit support

Status:

Planned

---

## R2V3

### Comparative Intelligence

Features:

- $compare
- Multi-persona answers
- Comparative analysis

Status:

Planned

---

## R2V4

### Observability

Features:

- Metrics
- Dashboards
- Monitoring
- Telemetry

Status:

Planned

---

## R3V0

### Specialist Marketplace

Features:

- Plug-in personas
- Persona catalog
- Dynamic installation
- Agent framework

Status:

Future

---

# GitHub Project

Project Name:

```text
avalbot
```

Workflow:

```text
Backlog
Ready
In Progress
Testing
Done
```

---

# Initial Backlog

| ID | Description |
|------|------|
| AB-001 | Create personas.json |
| AB-002 | Create session service |
| AB-003 | Implement $perfis |
| AB-004 | Implement $perfil |
| AB-005 | Implement $ajuda |
| AB-006 | Persist sessions |
| AB-007 | Refactor Groq integration |
| AB-008 | Create handbook |
| AB-009 | Architecture documentation |
| AB-010 | Publish R2V1 |
| AB-011 | Create dynamic persona framework |

---

# Author

Moacyr Ribeiro Blondet

Developed as part of ongoing studies involving Artificial Intelligence, AI Governance, Conversational Systems and Specialized Digital Agents.

---
````
