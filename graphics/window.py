# Main game window
import arcade
from pyglet.event import EVENT_HANDLE_STATE
from torch.utils.benchmark import select_unit

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
        self.start_select = False

    def setup(self):
        unit = Unit(100, 100, 1, settings.UNIT_SPEED)
        unit1 = Unit(500, 100, 1, settings.UNIT_SPEED)
        self.world.add_unit(unit)
        self.world.add_unit(unit1)
        self.units_list = arcade.SpriteList(use_spatial_has=True)
        self.units_list.append(unit)
        self.units_list.append(unit1)

    def on_draw(self):
        self.clear()
        for unit in self.units_list:
            if unit in self.selected_units:
                arcade.draw_circle_outline(unit.center_x, unit.center_y, 100, arcade.color.RED, 10)
        if self.units_list:
            self.units_list.draw()

        if self.start_select and self.start_select_window and self.end_select_window:
            x1, y1 = self.start_select_window
            x2, y2 = self.end_select_window
            left = min(x1, x2)
            right = max(x1, x2)
            bottom = min(y1, y2)
            top = max(y1, y2)
            width = abs(x1 - x2)
            height = abs(y1 - y2)
            arcade.draw_lbwh_rectangle_outline(
                left, bottom, width, height,
                arcade.color.GREEN, 2
            )
            for unit in self.units_list:
                if left < unit.center_x < right and top > unit.center_y > bottom:
                    if unit not in self.selected_units:
                        self.selected_units.append(unit)


    def on_update(self, delta_time):
        self.world.update(delta_time)
        for unit in self.units_list:
            unit.update(delta_time)

    def on_mouse_press(self, x, y, button, modifiers):
        unit = self.world.get_unit_in_point(x, y)
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.start_select_window = (x, y)
            if unit in self.selected_units:
                self.selected_units.remove(unit)
            else:
                self.selected_units.append(unit)
        self.end_select_window = (x, y)
        if unit in self.selected_units:
            if button == arcade.MOUSE_BUTTON_RIGHT:
                if unit:
                    print(self.selected_units)
                    for really_unit in self.selected_units:
                        really_unit.set_target(x, y)
        if modifiers == arcade.key.MOD_SHIFT:
            if unit not in self.selected_units:
                self.selected_units.append(unit)
            self.start_select = True

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        self.end_select_window = (x, y)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.start_select = False