# Main game runner file 
# run.py - ИСПРАВЛЕННЫЙ
from graphics.window import Window_draw
import arcade
from utils import settings


def main():
    print("Запуск RTS игры...")

    # Создаём окно (теперь без аргументов!)
    window = Window_draw(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, settings.GAME_TITLE)
    window.setup()

    # Запускаем игру
    print("Игра запущена!")
    arcade.run()


if __name__ == "__main__":
    main()