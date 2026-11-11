"""Hardware-facing lock drivers."""

class SimulatedLockGateway:
    def __init__(self):
        self.unlocked: set[str] = set()
    def unlock(self, bike_id: str) -> bool:
        self.unlocked.add(bike_id)
        return True
    def lock(self, bike_id: str) -> bool:
        self.unlocked.discard(bike_id)
        return True

class DockController:
    """Low-level station controller with command and device response semantics."""
    def __init__(self):
        self.last_command: tuple[str, str] | None = None
    def send_command(self, station_port: str, operation: str) -> dict:
        self.last_command = (station_port, operation)
        return {"ack": "ACK", "port": station_port}

class StationLockAdapter:
    """Wraps the station command interface for the application."""
    def __init__(self, controller: DockController, bike_ports: dict[str, str]):
        self.controller = controller
        self.bike_ports = bike_ports
    def unlock(self, bike_id: str) -> bool:
        return self.controller.send_command(self.bike_ports[bike_id], "UNLOCK")["ack"] == "ACK"
    def lock(self, bike_id: str) -> bool:
        return self.controller.send_command(self.bike_ports[bike_id], "LOCK")["ack"] == "ACK"
