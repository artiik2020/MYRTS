# game_logic/__init__.py

# Импорт модулей
from . import unit
from . import world

# Импорт основных классов для удобства
from .unit import Unit
from .world import World

# Что будет доступно при from game_logic import *
__all__ = ['Unit', 'World', 'unit', 'world']

print(f"✅ game_logic загружен. Доступно: {__all__}")