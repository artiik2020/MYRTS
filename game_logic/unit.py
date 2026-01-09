# Unit class 
import arcade

class Unit(arcade.Sprite):
    def __init__(self, x: float, y: float, player_id: int = 0, speed: int = 100, name='Боец'):
        super().__init__(x, y, player_id, speed)
        self.texture = arcade.load_texture('sprites/unit.png')

        # ✅ Устанавливаем правильные координаты
        self.center_x = x
        self.center_y = y

        # ✅ Правильные target координаты
        self.target_x = x
        self.target_y = y

        # ✅ Правильная скорость
        self.speed = speed
        self.change_x = 0
        self.change_y = 0

        self.rotation = 0.0
        self.health = 100
        self.armor = 0
        self.change = False
        self.name = name

        # ✅ Правильный масштаб
        self.scale = 0.5  # вместо 0.1

        print(f"✅ Создан юнит '{name}' в ({x}, {y})")

    def update(self, delta_time: float = 1 / 60):
        """Обновление с учетом времени"""
        # Если есть target, двигаемся к нему
        if self.change_x != 0 or self.change_y != 0:
            self.center_x += self.change_x * delta_time
            self.center_y += self.change_y * delta_time

        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y
        distance = max((dx ** 2 + dy ** 2) ** 0.5, 1)  # избегаем деления на 0
        if distance <= 50:
            self.change_x = 0
            self.change_y = 0
        else:
            self.change_x = (dx / distance) * self.speed
            self.change_y = (dy / distance) * self.speed


    def set_target(self, x, y):
        """Установить цель и рассчитать направление движения"""
        self.target_x = x
        self.target_y = y

        # Рассчитываем вектор направления
        dx = x - self.center_x
        dy = y - self.center_y
        distance = max((dx ** 2 + dy ** 2) ** 0.5, 1)  # избегаем деления на 0

        # Нормализуем вектор и умножаем на скорость
        print(distance)
        if distance <= 50:
            self.change_x = 0
            self.change_y = 0
        else:
            self.change_x = (dx / distance) * self.speed
            self.change_y = (dy / distance) * self.speed

        print(f"🔄 {self.name} движется к ({x}, {y})")