from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ai_orchestrator_route() -> None:
    response = client.post(
        '/api/v1/ai/orchestrate',
        json={
            'workflow': 'appointment',
            'payload': {'branch': 'Downtown', 'slot': '09:00'},
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body['agent'] == 'Appointment Agent'
    assert 'Downtown' in body['result']


def test_ai_workflows_route() -> None:
    response = client.get('/api/v1/ai/workflows')

    assert response.status_code == 200
    body = response.json()
    assert 'appointment' in body['workflows']
    assert 'queue' in body['workflows']
