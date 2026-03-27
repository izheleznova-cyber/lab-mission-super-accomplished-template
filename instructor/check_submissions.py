
---

## 📋 **ШАГ 5: Скрипт проверки для преподавателя**

Создайте `check_submissions.py`:

```python
import json
import os
import subprocess

def check_student_submission(name):
    """Проверяет выполнение заданий студента"""
    
    # Загружаем задания
    tasks_file = f'student_tasks_{name}.json'
    if not os.path.exists(tasks_file):
        print(f"❌ {name}: Нет файла заданий")
        return
    
    with open(tasks_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Загружаем код студента
    game_file = f'game.py'
    if not os.path.exists(game_file):
        print(f"❌ {name}: Нет файла game.py")
        return
    
    with open(game_file, 'r', encoding='utf-8') as f:
        code = f.read()
    
    print(f"\n📊 ПРОВЕРКА: {name}")
    print("="*60)
    
    total_points = 0
    max_points = 0
    
    for level_key, level_data in data['levels'].items():
        for i, task in enumerate(level_data['tasks']):
            max_points += task['points']
            
            # Проверяем паттерн в коде
            import re
            if re.search(task['code_pattern'], code, re.IGNORECASE):
                print(f"✅ [{task['id']}] {task['title']} — ВЫПОЛНЕНО")
                total_points += task['points']
                level_data['completed'][i] = True
            else:
                print(f"❌ [{task['id']}] {task['title']} — НЕ ВЫПОЛНЕНО")
    
    # Обновляем файл с отметками
    with open(tasks_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("="*60)
    print(f"📊 БАЛЛЫ: {total_points}/{max_points}")
    print(f"📈 ПРОЦЕНТ: {total_points/max_points*100:.1f}%")
    
    # Оценка
    percentage = total_points/max_points*100
    if percentage >= 90:
        grade = "5 (Отлично)"
    elif percentage >= 60:
        grade = "4 (Хорошо)"
    elif percentage >= 30:
        grade = "3 (Удовлетворительно)"
    else:
        grade = "2 (Неудовлетворительно)"
    
    print(f"🎓 ОЦЕНКА: {grade}")

# Проверка всех студентов
if __name__ == "__main__":
    students = ['irina', 'alex', 'dmitry']  # Список имён
    
    for student in students:
        check_student_submission(student)
