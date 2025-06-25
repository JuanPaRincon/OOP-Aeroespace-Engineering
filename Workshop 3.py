#Workshop 3
#Santiago Flórez
#David Arévalo
#Juan Pablo Rincón
#Schneider Alejandro Torres
from abc import ABC, abstractmethod

class BaseSystem(ABC):
    @abstractmethod
    def update(self):
        pass

class AttitudeControlSystem(BaseSystem):
    def __init__(self):
        self._orientation = 0

    def update(self):
        self._orientation = (self._orientation + 1) % 360
        print(f"[Attitude] Orientation is now {self._orientation}°")

    def get_orientation(self):
        return self._orientation

    def set_orientation(self, value):
        self._orientation = value % 360


class PowerSystem(BaseSystem):
    def __init__(self):
        self._battery = 100
        self._solar_input = True

    def update(self):
        if self._solar_input:
            self._battery = min(100, self._battery + 5)
            print(f"[Power] Charging from solar. Battery: {self._battery}%")
        else:
            self._battery -= 10
            print(f"[Power] Discharging battery. Battery: {self._battery}%")

    def get_battery_level(self):
        return self._battery

    def set_battery_level(self, value):
        self._battery = max(0, min(100, value))

    def set_solar_input(self, value):
        self._solar_input = value

    def get_solar_input(self):
        return self._solar_input

    def is_low_battery(self):
        return self._battery < 20
    

class PayloadCamera(BaseSystem):
    def __init__(self):
        self._temperature = 20

    def update(self):
        self._temperature += 1
        print(f"[Payload] Capturing image at {self._temperature}°C")

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        self._temperature = value


class CommSystem(PowerSystem):
    def __init__(self):
        super().__init__()

    def update(self):
        if self.is_low_battery():
            print("[Comms] Cannot transmit. Battery too low.")
        else:
            print("[Comms] Transmitting data to Earth.")


class EventManager:
    def __init__(self):
        self._step = 0

    def handle_event(self, ship):
        if self._step == 3:
            print("[Event] Eclipse started! Solar input disabled.")
            ship.set_solar_input(False)
        elif self._step == 13:
            print("[Event] Eclipse ended! Solar input restored.")
            ship.set_solar_input(True)
        self._step += 1




class Ship(AttitudeControlSystem, CommSystem, PayloadCamera):
    def __init__(self):
        AttitudeControlSystem.__init__(self)
        CommSystem.__init__(self)  # This also sets up PowerSystem
        PayloadCamera.__init__(self)
        self._events = EventManager()

    def update(self):
        print("\n--- Time Step ---")
        self._events.handle_event(self)

        AttitudeControlSystem.update(self)
        PowerSystem.update(self)
        PayloadCamera.update(self)
        CommSystem.update(self)


def main():
    ship = Ship()
    for _ in range(20):
        ship.update()

main()