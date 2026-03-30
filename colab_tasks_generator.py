import json
import random

def generate_colab_tasks(student_name, level=2):
    """Генерирует задания для Colab на уровне сложности"""
    
    tasks = {
        'name': student_name,
        'level': level,
        'tasks': []
    }
    
    if level == 1:
        tasks['tasks'] = [
            {'name': 'Загрузка данных', 'type': 'load_json', 'points': 10},
            {'name': 'Базовая статистика', 'type': 'statistics', 'points': 20},
            {'name': 'Простые графики', 'type': 'bar_chart', 'points': 20},
            {'name': 'Выводы', 'type': 'conclusions', 'points': 10},
        ]
    
    elif level == 2:
        tasks['tasks'] = [
            {'name': 'Визуализация маршрута', 'type': 'plot_route', 'points': 25},
            {'name': 'Анализ ошибок', 'type': 'error_analysis', 'points': 25},
            {'name': 'Расчёт оптимального пути', 'type': 'optimal_path', 'points': 25},
            {'name': 'Рекомендации', 'type': 'recommendations', 'points': 10},
        ]
    
    elif level == 3:
        tasks['tasks'] = [
            {'name': 'Тепловая карта', 'type': 'heatmap', 'points': 20},
            {'name': 'Поиск паттернов', 'type': 'pattern_detection', 'points': 25},
            {'name': 'Предсказание', 'type': 'prediction', 'points': 20},
            {'name': 'Сравнение студентов', 'type': 'comparison', 'points': 20},
            {'name': 'Отчёт', 'type': 'report', 'points': 15},
        ]
    
    elif level == 4:
        tasks['tasks'] = [
            {'name': 'Реализация A*', 'type': 'astar_algorithm', 'points': 30},
            {'name': 'Симуляция', 'type': 'simulation', 'points': 25},
            {'name': 'Кластеризация', 'type': 'clustering', 'points': 25},
            {'name': 'Интерактивный отчёт', 'type': 'interactive_report', 'points': 20},
        ]
    
    # Сохраняем
    filename = f'colab_tasks_{student_name}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Задания Level {level} сгенерированы: {filename}")
    return tasks

# Пример использования:
# generate_colab_tasks('irina', level=2)
