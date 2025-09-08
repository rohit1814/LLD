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


# Concrete Command for Light
class LightCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# Concrete Command for Fan
class FanCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()


# Invoker: Remote Controller
class RemoteController:
    def __init__(self, num_buttons: int = 4):
        self.buttons = [None] * num_buttons
        self.button_pressed = [False] * num_buttons

    def set_command(self, idx: int, cmd: Command):
        if 0 <= idx < len(self.buttons):
            self.buttons[idx] = cmd
            self.button_pressed[idx] = False

    def press_button(self, idx: int):
        if 0 <= idx < len(self.buttons) and self.buttons[idx] is not None:
            if not self.button_pressed[idx]:
                self.buttons[idx].execute()
            else:
                self.buttons[idx].undo()
            self.button_pressed[idx] = not self.button_pressed[idx]
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
