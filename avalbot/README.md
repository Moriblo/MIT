# AvalBot

> Multi-Persona AI Platform powered by Discord + Groq

---

## Current Release

| Attribute | Value |
|------------|---------|
| Release | R2V1 |
| Status | 🚧 In Development |
| Deployment Target | Azure Virtual Machine |
| Runtime | Python |
| AI Engine | Groq |
| Communication Channel | Discord |
| Repository | MIT / avalbot |

---

# Current Project Status

## Executive Dashboard

| Item | Status |
|--------|----------|
| AvalBot Project Created | ✅ Completed |
| GitHub Project (avalbot) Created | ✅ Completed |
| README.md Defined | ✅ Completed |
| Initial Architecture Defined | ✅ Completed |
| Business Rules Defined | ✅ Completed |
| R2V1 Scope Defined | ✅ Completed |
| personas.md | ⏳ Pending |
| personas.json | ⏳ Pending |
| Repository Structure | ⏳ Pending |
| Session Service | ⏳ Pending |
| Persona Service | ⏳ Pending |
| Discord Commands | ⏳ Pending |
| Groq Refactoring | ⏳ Pending |
| R2V1 Release | ⏳ Pending |
| Azure Deployment | ⏳ Pending |

---

# Initial Scope Definition (R2V1)

## Objective

Create the first production-ready release of AvalBot supporting:

- Multiple AI personas
- External persona configuration
- User session persistence
- Active profile management
- Discord integration
- Groq integration
- Role-based authorization foundation
- Azure deployment readiness

---

## Deliverables

### Functional

- Persona selection
- Persona switching
- User session persistence
- Persona-specific prompts
- Discord commands
- Groq integration

### Technical

- Modular architecture
- External configuration
- Service-oriented design
- Azure-ready deployment

### Governance

- Discord as identity provider
- Discord Roles as authorization mechanism
- No internal credential management

---

# Vision

AvalBot is a multi-persona conversational platform designed to explore Generative AI, AI Governance, Digital Specialists and Human-AI Interaction.

The platform enables a single Discord bot to dynamically assume multiple expert identities while maintaining a consistent user experience.

Users may:

- Interact with specialized AI experts
- Compare different viewpoints
- Explore governance and regulation topics
- Experiment with prompt engineering
- Validate multi-persona interaction models
- Build foundations for future AI specialist marketplaces

---

# Project Context

AvalBot is part of the practical activities associated with studies conducted within the MIT program.

The project serves as a laboratory for:

- Generative AI
- AI Governance
- Conversational Systems
- Prompt Engineering
- Human-AI Interaction
- Specialized AI Agents
- Multi-Persona Architectures

---

# High-Level Architecture

## Conceptual View

```text
                        ┌─────────────┐
                        │   Discord   │
                        └──────┬──────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │      AvalBot       │
                    │     (Python)       │
                    └─────────┬──────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼

 ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
 │ Persona Service│  │ Session Service│  │ Command Service│
 └───────┬────────┘  └───────┬────────┘  └────────────────┘
         │                   │
         ▼                   ▼

 ┌────────────────┐  ┌────────────────┐
 │ personas.json  │  │ sessions.json  │
 └────────────────┘  └────────────────┘

                              │
                              ▼

                     ┌────────────────┐
                     │  Groq Service  │
                     └───────┬────────┘
                             │
                             ▼

                        ┌────────┐
                        │  Groq  │
                        └────────┘
```

---

## Interaction Flow

```text
User
  │
  ▼

Discord Message

  │
  ▼

AvalBot

  │
  ├── Identify User
  │
  ├── Load Active Session
  │
  ├── Determine Persona
  │
  ├── Load Persona Prompt
  │
  ├── Send Request to Groq
  │
  └── Return Response

  ▼

Discord
```

---

# Dependency Chain

The implementation sequence for R2V1 follows the dependency chain below.

```text
README.md
    │
    ▼

personas.md
    │
    ▼

personas.json
    │
    ▼

Repository Structure
    │
    ▼

Session Service
    │
    ▼

Persona Service
    │
    ▼

Groq Refactoring
    │
    ▼

Discord Commands
    │
    ▼

R2V1 Release
    │
    ▼

Azure Deployment
```

This dependency model minimizes rework and ensures architectural consistency.

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

Architecture must support future evolution toward:

- Multi-agent ecosystems
- Specialist marketplaces
- Additional communication channels
- Enterprise governance models

---

# Initial Personas

## ✔️ Aval

### Purpose

General-purpose assistant.

### Characteristics

- Neutral
- Helpful
- Balanced
- Generalist
- Didactic

### Default Profile

Assigned automatically to all new users.

---

## 🏛️ Governança IA

### Purpose

AI Governance Specialist.

### Expertise

- Responsible AI
- Trustworthy AI
- ISO 42001
- NIST AI RMF
- LGPD
- AI Regulation
- Ethics
- Compliance

### Communication Style

- Strategic
- Executive
- Structured
- Consultative

---

## 🏴‍☠️ Pirate

### Purpose

Creative conversational persona.

### Characteristics

- Informal
- Humorous
- Character-driven
- High engagement

### Communication Style

- Pirate-themed language
- Relaxed interaction
- Entertainment-oriented

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
    │   ├── personas.md
    │   ├── architecture.md
    │   ├── business-rules.md
    │   └── roadmap.md
    │
    └── releases/
        ├── r2v1/
        ├── r2v2/
        ├── r2v3/
        ├── r2v4/
        └── r3v0/
```

---

# Personas Configuration

All personas are externally configured.

```text
personas.json
```

Example:

```json
{
  "default": {
    "name": "Aval",
    "emoji": "🧭",
    "description": "General Assistant",
    "prompt": "..."
  },

  "governanca": {
    "name": "Governança IA",
    "emoji": "🏛️",
    "description": "AI Governance Specialist",
    "prompt": "..."
  },

  "pirate": {
    "name": "Pirate",
    "emoji": "🏴",
    "description": "Creative Pirate Persona",
    "prompt": "..."
  }
}
```

---

# User Sessions

User state persistence.

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

| ID | Rule |
|------|------|
| RB001 | Every user has exactly one active profile |
| RB002 | New users receive Aval as default profile |
| RB003 | Messages without commands use active profile |
| RB004 | `$perfil <profile>` changes active profile |
| RB005 | `$perfil <profile> <question>` performs one-time execution |
| RB006 | Future `$compare` never changes active profile |
| RB007 | Discord is the only identity provider |
| RB008 | No user credentials are stored |
| RB009 | Authorization uses Discord Roles |
| RB010 | No hardcoded user lists |
| RB011 | All personas are externally configured |

---

# Commands

## Available Profiles

```text
$perfis
```

## General Help

```text
$ajuda
```

## Persona Help

```text
$ajuda governanca
```

## Change Active Profile

```text
$perfil governanca
```

## One-Time Question

```text
$perfil governanca What do you think about AI governance?
```

## Active Profile Question

```text
What do you think about AI governance?
```

## User Information

```text
$whoami
```

Displays:

- Discord username
- Active profile
- Discord roles
- Authorized personas

---

# Hosting Strategy

## Development

Local workstation.

---

## Validation

Discord Test Server.

---

## Production

Microsoft Azure Virtual Machine.

### Target Environment

- Ubuntu Linux
- Python Runtime
- Discord Bot
- Groq Integration
- Systemd Service

### Objective

Provide:

- 24x7 operation
- Continuous availability
- Centralized deployment
- Stable execution environment

---

# Release Roadmap

| Release | Objective | Status |
|----------|------------|----------|
| R2V1 | Multi-Persona Foundation | 🚧 In Development |
| R2V2 | Governance & Authorization | Planned |
| R2V3 | Comparative Intelligence | Planned |
| R2V4 | Observability & Metrics | Planned |
| R3V0 | Specialist Marketplace | Future |

---

# GitHub Project

Project:

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

| ID | Description | Status |
|------|-------------|----------|
| AB-001 | Create personas.md | ⏳ |
| AB-002 | Create personas.json | ⏳ |
| AB-003 | Create repository structure | ⏳ |
| AB-004 | Create session service | ⏳ |
| AB-005 | Create persona service | ⏳ |
| AB-006 | Refactor Groq integration | ⏳ |
| AB-007 | Implement $perfis | ⏳ |
| AB-008 | Implement $perfil | ⏳ |
| AB-009 | Implement $ajuda | ⏳ |
| AB-010 | Implement $whoami | ⏳ |
| AB-011 | Persist sessions | ⏳ |
| AB-012 | Publish R2V1 | ⏳ |
| AB-013 | Deploy on Azure VM | ⏳ |

---

# Author

**Moacyr Ribeiro Blondet**

Developed as part of ongoing studies involving:

- Artificial Intelligence
- AI Governance
- Conversational Systems
- Prompt Engineering
- Specialized Digital Agents
- Multi-Persona Architectures
