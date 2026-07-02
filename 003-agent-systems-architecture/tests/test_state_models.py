from services.agent_control_plane.state_models import (
    INITIAL_WORKFLOW_STATE,
    create_initial_governed_agent_run,
)


def test_create_initial_governed_agent_run_has_required_identity_fields() -> None:
    governed_agent_run = create_initial_governed_agent_run(
        user_query="Review this case against policy criteria."
    )

    execution_envelope = governed_agent_run.execution_envelope

    assert execution_envelope.run_id.startswith("run_")
    assert execution_envelope.input_id.startswith("input_")
    assert execution_envelope.trace_id.startswith("trace_")
    assert execution_envelope.created_at_utc is not None


def test_create_initial_governed_agent_run_starts_at_start_state() -> None:
    governed_agent_run = create_initial_governed_agent_run(
        user_query="Review this case against policy criteria."
    )

    workflow_state_context = governed_agent_run.workflow_state_context

    assert workflow_state_context.current_workflow_state == INITIAL_WORKFLOW_STATE
    assert workflow_state_context.previous_workflow_state is None
    assert workflow_state_context.state_history == [INITIAL_WORKFLOW_STATE]


def test_create_initial_governed_agent_run_preserves_user_query() -> None:
    user_query = "Review this case against policy criteria."

    governed_agent_run = create_initial_governed_agent_run(user_query=user_query)

    assert governed_agent_run.agent_data_payload.user_query == user_query
    assert governed_agent_run.agent_data_payload.detected_intent is None
    assert governed_agent_run.agent_data_payload.selected_plan_steps == []
    assert governed_agent_run.agent_data_payload.error_messages == []


def test_create_initial_governed_agent_run_starts_with_empty_trace_events() -> None:
    governed_agent_run = create_initial_governed_agent_run(
        user_query="Review this case against policy criteria."
    )

    assert governed_agent_run.trace_events == []


def test_multiple_governed_agent_runs_do_not_share_mutable_state() -> None:
    first_run = create_initial_governed_agent_run(
        user_query="First workflow request."
    )
    second_run = create_initial_governed_agent_run(
        user_query="Second workflow request."
    )

    first_run.workflow_state_context.state_history.append("classify_request")
    first_run.agent_data_payload.error_messages.append("first run error")

    assert second_run.workflow_state_context.state_history == [INITIAL_WORKFLOW_STATE]
    assert second_run.agent_data_payload.error_messages == []
