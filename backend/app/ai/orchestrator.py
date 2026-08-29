from app.ai.agents import (
    AnalyticsAgent,
    AppointmentAgent,
    CustomerServiceAgent,
    NotificationAgent,
    QueueOptimizationAgent,
)


class AgentOrchestrator:
    def __init__(self) -> None:
        self.appointment = AppointmentAgent()
        self.queue = QueueOptimizationAgent()
        self.customer = CustomerServiceAgent()
        self.analytics = AnalyticsAgent()
        self.notifications = NotificationAgent()

    def run(self, workflow: str, payload: dict) -> dict:
        if workflow == "appointment":
            return {"agent": self.appointment.config.name, "result": self.appointment.suggest(payload)}
        if workflow == "queue":
            return {"agent": self.queue.config.name, "result": self.queue.optimize(payload)}
        if workflow == "support":
            return {"agent": self.customer.config.name, "result": self.customer.handle(payload)}
        if workflow == "analytics":
            return {"agent": self.analytics.config.name, "result": self.analytics.analyze(payload)}
        if workflow == "notification":
            return {"agent": self.notifications.config.name, "result": self.notifications.notify(payload)}
        return {"agent": "Orchestrator", "result": "No workflow found"}
