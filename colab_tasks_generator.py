#!/usr/bin/env python3
"""
🎓 Генератор заданий для студентов Colab (дистанционное обучение)
Запустите для каждого студента, который не был в классе
"""

import json
import random
import sys

def generate_colab_tasks(student_name, level=2):
    """
    Генерирует задания для Colab на уровне сложности
    
    Args:
        student_name (str): Имя студента
        level (int): Уровень сложности (1-4)
    
    Returns:
        dict: Словарь с заданиями
    """
    
    tasks = {
        'name': student_name,
        'level': level,
        'description': f'Задания для Colab - Уровень {level}',
        'tasks': []
    }
    
    if level == 1:
        tasks['tasks'] = [
            {
                'name': 'Загрузка данных',
                'type': 'load_json',
                'description': 'Загрузите log_{имя}.json и student_tasks_{имя}.json',
                'points': 10
            },
            {
                'name': 'Базовая статистика',
                'type': 'statistics',
                'description': 'Выведите: количество шагов, штрафов, итоговый счёт',
                'points': 20
            },
            {
                'name': 'Простые графики',
                'type': 'bar_chart',
                'description': 'Постройте столбчатую диаграмму событий',
                'points': 20
            },
            {
                'name': 'Выводы',
                'type': 'conclusions',
                'description': 'Напишите 2-3 вывода о вашей игре',
                'points': 10
            },
        ]
        tasks['max_score'] = 60
    
    elif level == 2:
        tasks['tasks'] = [
            {
                'name': 'Визуализация маршрута',
                'type': 'plot_route',
                'description': 'Постройте маршрут от A до B с отметками',
                'points': 25
            },
            {
                'name': 'Анализ ошибок',
                'type': 'error_analysis',
                'description': 'Найдите места штрафов и объясните причины',
                'points': 25
            },
            {
                'name': 'Расчёт оптимального пути',
                'type': 'optimal_path',
                'description': 'Рассчитайте минимальное расстояние A→B',
                'points': 25
            },
            {
                'name': 'Рекомендации',
                'type': 'recommendations',
                'description': 'Предложите как улучшить маршрут',
                'points': 10
            },
        ]
        tasks['max_score'] = 85
    
    elif level == 3:
        tasks['tasks'] = [
            {
                'name': 'Тепловая карта',
                'type': 'heatmap',
                'description': 'Создайте тепловую карту посещений клеток',
                'points': 20
            },
            {
                'name': 'Поиск паттернов',
                'type': 'pattern_detection',
                'description': 'Найдите повторяющиеся последовательности движений',
                'points': 25
            },
            {
                'name': 'Предсказание',
                'type': 'prediction',
                'description': 'Предскажите результат по первым 50% маршрута',
                'points': 20
            },
            {
                'name': 'Сравнение студентов',
                'type': 'comparison',
                'description': 'Сравните свой маршрут с 2 другими студентами',
                'points': 20
            },
            {
                'name': 'Отчёт',
                'type': 'report',
                'description': 'Создайте подробный отчёт с графиками',
                'points': 15
            },
        ]
        tasks['max_score'] = 100
    
    elif level == 4:
        tasks['tasks'] = [
            {
                'name': 'Реализация A*',
                'type': 'astar_algorithm',
                'description': 'Реализуйте алгоритм A* для поиска оптимального пути',
                'points': 30
            },
            {
                'name': 'Симуляция',
                'type': 'simulation',
                'description': 'Запустите 100 симуляций с разными стратегиями',
                'points': 25
            },
            {
                'name': 'Кластеризация',
                'type': 'clustering',
                'description': 'Примените k-means для кластеризации стилей игры',
                'points': 25
            },
            {
                'name': 'Интерактивный отчёт',
                'type': 'interactive_report',
                'description': 'Создайте HTML отчёт с интерактивными графиками',
                'points': 20
            },
        ]
        tasks['max_score'] = 100
    
    # Сохраняем
    filename = f'colab_tasks_{student_name}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Задания Level {level} сгенерированы: {filename}")
    print(f"📊 Максимальный балл: {tasks['max_score']}")
    print(f"📝 Заданий: {len(tasks['tasks'])}")
    
    return tasks

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование:")
        print("  python colab_tasks_generator.py <имя_студента> [уровень]")
        print("\nПримеры:")
        print("  python colab_tasks_generator.py irina 1  # Level 1")
        print("  python colab_tasks_generator.py vitaliy 2  # Level 2")
        print("\nУровни:")
        print("  1 - Базовый (60 баллов)")
        print("  2 - Средний (85 баллов)")
        print("  3 - Продвинутый (100 баллов)")
        print("  4 - Эксперт (100 баллов)")
        sys.exit(1)
    
    student_name = sys.argv[1]
    level = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    
    generate_colab_tasks(student_name, level)
