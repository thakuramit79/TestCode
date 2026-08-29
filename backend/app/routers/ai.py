from typing import Any

from fastapi import APIRouter

from app.ai.orchestrator import AgentOrchestrator

router = APIRouter(prefix="/ai", tags=["ai"])
orchestrator = AgentOrchestrator()


@router.get("/workflows")
def list_workflows() -> dict[str, list[str]]:
    return {
        "workflows": [
            "appointment",
            "queue",
            "support",
            "analytics",
            "notification",
        ]
    }


@router.post("/orchestrate")
def orchestrate(workflow_payload: dict[str, Any]) -> dict[str, str]:
    workflow = str(workflow_payload.get("workflow", "")).strip()
    payload = workflow_payload.get("payload", {})
    if not isinstance(payload, dict):
        payload = {}
    return orchestrator.run(workflow, payload)
