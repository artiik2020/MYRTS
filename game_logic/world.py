"""
Игровой мир - содержит всё, что происходит в игре.
"""
class World:
    """Игровой мир"""

    def __init__(self):
        # Все объекты в мире
        self.units = []
        self.structure = []

        # Время игры
        self.time_from_start = 0.0

    def add_unit(self, unit):
        """Добавить юнита в мир"""
        self.units.append(unit)
        print(f"В мир добавлен {unit.name}")

    def update(self, delta_time):
        """Обновить состояние мира"""
        # Увеличиваем время
        self.time_from_start += delta_time

        # Обновляем всех юнитов
        for unit in self.units:
            unit.update(delta_time)

        # Можно добавить:
        # - Обновление зданий
        # - Проверку столкновений
        # - И т.д.

    def get_unit_in_point(self, x, y, radius=150):
        """Найти юнита в указанной точке"""
        for unit in self.units:
            # Простая проверка расстояния
            range = ((unit.center_x - x) ** 2 + (unit.center_y - y) ** 2) ** 0.5
            if range <= radius:
                return unit
        return None