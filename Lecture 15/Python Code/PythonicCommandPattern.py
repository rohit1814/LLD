# Using a dictionary for button slots instead of a fixed-size list (no arbitrary limit like 4).
# Keeping toggle state inside the command itself instead of remote controller.

from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Receivers
class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")


class Fan:
    def on(self):
        print("Fan is ON")

    def off(self):
        print("Fan is OFF")


# Base Toggle Command
class ToggleCommand(Command):
    def __init__(self):
        self.is_on = False

    def press(self):
        if not self.is_on:
            self.execute()
        else:
            self.undo()
        self.is_on = not self.is_on


# Concrete Command for Light
class LightCommand(ToggleCommand):
    def __init__(self, light: Light):
        super().__init__()
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# Concrete Command for Fan
class FanCommand(ToggleCommand):
    def __init__(self, fan: Fan):
        super().__init__()
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()


# Invoker: Remote Controller
class RemoteController:
    def __init__(self):
        self.buttons: dict[int, Command] = {}

    def set_command(self, idx: int, cmd: Command):
        self.buttons[idx] = cmd

    def press_button(self, idx: int):
        if idx in self.buttons:
            self.buttons[idx].press()
        else:
            print(f"No command assigned at button {idx}")


# Example usage
if __name__ == "__main__":
    living_room_light = Light()
    ceiling_fan = Fan()

    remote = RemoteController()

    remote.set_command(0, LightCommand(living_room_light))
    remote.set_command(1, FanCommand(ceiling_fan))

    print("--- Toggling Light Button 0 ---")
    remote.press_button(0)  # ON
    remote.press_button(0)  # OFF

    print("--- Toggling Fan Button 1 ---")
    remote.press_button(1)  # ON
    remote.press_button(1)  # OFF

    print("--- Pressing Unassigned Button 2 ---")
    remote.press_button(2)
