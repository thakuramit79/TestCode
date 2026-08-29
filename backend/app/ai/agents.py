from dataclasses import dataclass


@dataclass
class AgentConfig:
    name: str
    purpose: str


class AppointmentAgent:
    def __init__(self) -> None:
        self.config = AgentConfig("Appointment Agent", "Suggest and optimize appointment booking decisions")

    def suggest(self, payload: dict) -> str:
        return f"Appointment suggestion for {payload.get('branch', 'branch')}: prioritize available slots with minimum wait time."


class QueueOptimizationAgent:
    def __init__(self) -> None:
        self.config = AgentConfig("Queue Optimization Agent", "Reduce waiting time and optimize queue flow")

    def optimize(self, payload: dict) -> str:
        return f"Queue optimization recommendation: balance workload across {payload.get('agents', 2)} agents and prioritize VIP cases."


class CustomerServiceAgent:
    def __init__(self) -> None:
        self.config = AgentConfig("Customer Service Agent", "Respond to customer support and queue inquiries")

    def handle(self, payload: dict) -> str:
        return f"Customer support response: estimated wait time is {payload.get('eta_minutes', 12)} minutes."


class AnalyticsAgent:
    def __init__(self) -> None:
        self.config = AgentConfig("Analytics Agent", "Provide insights and trend analysis")

    def analyze(self, payload: dict) -> str:
        return f"Analytics summary: SLA compliance is {payload.get('sla_compliance', 96)}% with lower than norm queue load."


class NotificationAgent:
    def __init__(self) -> None:
        self.config = AgentConfig("Notification Agent", "Trigger proactive notification and reminder messages")

    def notify(self, payload: dict) -> str:
        return f"Notification generated for {payload.get('customer', 'customer')} via {payload.get('channel', 'email')}."
