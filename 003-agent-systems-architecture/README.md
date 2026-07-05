# Block 3 — Agent Systems Architecture

This module implements a reusable shared agent control plane and validates it through two workflow profiles:

1. AI Infrastructure Incident Response
2. Regulated Evidence Review

## Shared Control Plane Responsibilities

- Workflow profile registration
- Request routing
- State transition enforcement
- Planner-executor coordination
- Supervisor-worker coordination
- Bounded loops
- Policy and tool authorization
- Human approval
- Checkpoint recovery
- Trace logging
- Trajectory evaluation

## Development Commands

```bash
make install
make test
make type-check
make lint
make validate
