from agent_control_plane.contracts.common_contract_types import (
    PayloadTrustLevel,
)
from agent_control_plane.contracts.execution_envelope_models import (
    ExecutionEnvelope,
)
from agent_control_plane.contracts.workflow_state_models import (
    AgentDataPayload,
    GovernedAgentEnvelope,
    UntrustedPayloadItem,
    WorkflowStateContext,
)


def create_sample_governed_envelope() -> GovernedAgentEnvelope:
    execution_envelope = ExecutionEnvelope(
        run_id="run_demo_001",
        trace_id="trace_demo_001",
        input_case_id="incident_case_001",
        workflow_profile_name="ai_infrastructure_incident_response",
        workflow_profile_version="0.1.0",
    )

    workflow_state_context = WorkflowStateContext(
        current_workflow_state="START",
        state_transition_history=["START"],
    )

    agent_data_payload = AgentDataPayload(
        user_request=UntrustedPayloadItem(
            source_identifier="user_request",
            trust_level=PayloadTrustLevel.UNTRUSTED_USER_INPUT,
            raw_content="Investigate elevated inference latency.",
        )
    )

    return GovernedAgentEnvelope(
        execution_envelope=execution_envelope,
        workflow_state_context=workflow_state_context,
        agent_data_payload=agent_data_payload,
    )


if __name__ == "__main__":
    governed_agent_envelope = create_sample_governed_envelope()
    print(governed_agent_envelope.model_dump_json(indent=2))
