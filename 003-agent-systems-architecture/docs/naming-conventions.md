# Naming Conventions

## General Rule

Names must describe system responsibility without requiring the reader to guess.

## Folder Names

Use responsibility-based names:

- `contracts`
- `runtime`
- `governance`
- `recovery`
- `observability`
- `evaluation`

Avoid vague names:

- `utils`
- `helpers`
- `misc`
- `common`
- `core`

## File Names

Use names such as:

- `workflow_profile_registry.py`
- `state_transition_engine.py`
- `tool_authorization_engine.py`
- `workflow_checkpoint_store.py`

Avoid:

- `manager.py`
- `handler.py`
- `processor.py`
- `service.py`

## Variable Names

Use:

- `requested_next_workflow_state`
- `authorized_tool_contract`
- `workflow_step_result`
- `checkpoint_verification_result`
- `maximum_loop_attempts`

Avoid:

- `data`
- `result`
- `obj`
- `temp`
- `info`

## Boolean Names

Boolean variables must read as questions:

- `is_transition_allowed`
- `requires_human_approval`
- `has_reached_loop_limit`
- `is_checkpoint_verified`

## Collection Names

Use plural names:

- `registered_workflow_profiles`
- `allowed_state_transitions`
- `worker_results`
- `trace_event_records`
