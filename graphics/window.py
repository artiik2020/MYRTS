# Main game window
import arcade
from utils import settings
from game_logic import world, Unit


class Window_draw(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.world = world.World()
        arcade.set_background_color(arcade.color.WHITE)

        self.selected_units = []
        self.start_select_window = None
        self.end_select_window = None

    def setup(self):
        unit = Unit(100, 100, 1, settings.UNIT_SPEED)
        self.world.add_unit(unit)
        self.units_list = arcade.SpriteList()
        self.units_list.append(unit)

    def on_draw(self):
        self.clear()
        if self.units_list:
            self.units_list.draw()


    def on_update(self, delta_time):
        self.world.update(delta_time)
        for unit in self.units_list:
            unit.update(delta_time)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.start_select_window = (x, y)
            self.end_select_window = (x + 100, y + 100)
        unit = self.world.get_unit_in_point(x, y)
        if unit:
            unit.set_target(x, y)
            if modifiers == arcade.key.MOD_SHIFT:
                if unit.name not in self.selected_units:
                    self.selected_units.append(unit.name)
