import importlib
import math

game = importlib.import_module("game")

# ограничения
MIN_SIZE = 8
MIN_OBS = 10
MAX_SPEED = 10

def check():

    errors = []

    # 1. проверка скорости
    if abs(game.vx) > MAX_SPEED or abs(game.vy) > MAX_SPEED:
        errors.append("Speed too high")

    # 2. размеры (если добавлены)
    if hasattr(game, "hero_size"):
        if game.hero_size < MIN_SIZE:
            errors.append("Hero too small")

    if hasattr(game, "obstacle_size"):
        if game.obstacle_size < MIN_OBS:
            errors.append("Obstacle too small")

    # 3. лог движения
    if hasattr(game, "log"):
        if len(game.log) < 50:
            errors.append("Too short run")

    if errors:
        print("❌ FAIL")
        for e in errors:
            print("-", e)
    else:
        print("✅ PASS")

if _name_ == "_main_":
    check()
