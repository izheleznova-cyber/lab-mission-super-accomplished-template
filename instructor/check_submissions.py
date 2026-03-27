#!/usr/bin/env python3
"""
🔍 Скрипт проверки заданий для преподавателя

Использование:
    python instructor/check_submissions.py --student irina
    python instructor/check_submissions.py --all  # проверить всех
    python instructor/check_submissions.py --export results.csv
"""

import json
import os
import re
import argparse
from pathlib import Path
from datetime import datetime

class SubmissionChecker:
    def __init__(self, base_dir='.'):
        self.base_dir = Path(base_dir)
        self.results = []
    
    def check_student(self, name, verbose=True):
        """Проверяет одного студента"""
        
        # Загружаем задания
        tasks_file = self.base_dir / f'student_tasks_{name}.json'
        if not tasks_file.exists():
            print(f"❌ {name}: Нет файла заданий")
            return None
        
        with open(tasks_file, 'r', encoding='utf-8') as f:
            tasks_data = json.load(f)
        
        # Загружаем код
        game_file = self.base_dir / 'game.py'
        if not game_file.exists():
            print(f"❌ {name}: Нет файла game.py")
            return None
        
        with open(game_file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        if verbose:
            print(f"\n{'='*60}")
            print(f"📊 ПРОВЕРКА: {name.upper()}")
            print(f"{'='*60}")
        
        total_points = 0
        max_points = 0
        completed_tasks = []
        
        for level_key, level_data in tasks_data['levels'].items():
            level_num = level_key.replace('level_', '')
            
            for i, task in enumerate(level_data['tasks']):
                max_points += task['points']
                
                # Проверяем паттерн
                if re.search(task['code_pattern'], code, re.IGNORECASE | re.MULTILINE):
                    status = "✅"
                    total_points += task['points']
                    level_data['completed'][i] = True
                    completed_tasks.append(task['id'])
                else:
                    status = "❌"
                
                if verbose:
                    print(f"{status} [{task['id']}] {task['title']} ({task['points']} бал.)")
        
        # Сохраняем результаты
        result = {
            'name': name,
            'timestamp': datetime.now().isoformat(),
            'total_points': total_points,
            'max_points': max_points,
            'percentage': total_points/max_points*100 if max_points > 0 else 0,
            'completed_tasks': completed_tasks,
            'seed': tasks_data.get('seed', 'unknown')
        }
        
        self.results.append(result)
        
        # Обновляем файл заданий
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, indent=2, ensure_ascii=False)
        
        if verbose:
            print(f"{'='*60}")
            print(f"📊 БАЛЛЫ: {total_points}/{max_points} ({result['percentage']:.1f}%)")
            
            # Оценка
            if result['percentage'] >= 90:
                grade = "5 (Отлично) ⭐⭐⭐⭐⭐"
            elif result['percentage'] >= 60:
                grade = "4 (Хорошо) ⭐⭐⭐⭐"
            elif result['percentage'] >= 30:
                grade = "3 (Удовлетворительно) ⭐⭐⭐"
            else:
                grade = "2 (Неудовлетворительно) ⭐⭐"
            
            print(f"🎓 ОЦЕНКА: {grade}")
            print(f"{'='*60}\n")
        
        return result
    
    def check_all_students(self, student_list):
        """Проверяет всех студентов из списка"""
        print(f"\n🔍 ПРОВЕРКА ГРУППЫ ({len(student_list)} студентов)")
        print("="*60)
        
        for name in student_list:
            self.check_student(name, verbose=True)
        
        self.print_summary()
    
    def print_summary(self):
        """Выводит сводку по группе"""
        if not self.results:
            return
        
        print(f"\n{'='*60}")
        print("📈 СВОДКА ПО ГРУППЕ")
        print("="*60)
        print(f"{'Имя':<20} {'Баллы':<15} {'%':<10} {'Оценка'}")
        print("-"*60)
        
        total_percentage = 0
        
        for result in sorted(self.results, key=lambda x: x['percentage'], reverse=True):
            if result['percentage'] >= 90:
                grade = "5"
            elif result['percentage'] >= 60:
                grade = "4"
            elif result['percentage'] >= 30:
                grade = "3"
            else:
                grade = "2"
            
            print(f"{result['name']:<20} {result['total_points']}/{result['max_points']:<10} "
                  f"{result['percentage']:<10.1f} {grade}")
            
            total_percentage += result['percentage']
        
        avg_percentage = total_percentage / len(self.results)
        
        print("-"*60)
        print(f"{'Средний балл':<20} {'':<15} {avg_percentage:.1f}%")
        print("="*60)
    
    def export_to_csv(self, filename='results.csv'):
        """Экспортирует результаты в CSV"""
        if not self.results:
            print("❌ Нет результатов для экспорта")
            return
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Name,Total Points,Max Points,Percentage,Grade,Completed Tasks,Seed\n")
            
            for result in self.results:
                if result['percentage'] >= 90:
                    grade = "5"
                elif result['percentage'] >= 60:
                    grade = "4"
                elif result['percentage'] >= 30:
                    grade = "3"
                else:
                    grade = "2"
                
                tasks = ','.join(result['completed_tasks'])
                f.write(f"{result['name']},{result['total_points']},{result['max_points']},"
                       f"{result['percentage']:.1f},{grade},\"{tasks}\",{result['seed']}\n")
        
        print(f"✅ Результаты экспортированы в {filename}")

def main():
    parser = argparse.ArgumentParser(description='🔍 Проверка заданий студентов')
    parser.add_argument('--student', '-s', help='Имя студента для проверки')
    parser.add_argument('--all', '-a', action='store_true', help='Проверить всех студентов')
    parser.add_argument('--export', '-e', help='Экспортировать результаты в CSV файл')
    parser.add_argument('--students-list', help='Файл со списком имён студентов (по одному в строке)')
    
    args = parser.parse_args()
    
    checker = SubmissionChecker()
    
    if args.student:
        # Проверка одного студента
        checker.check_student(args.student)
    elif args.all or args.students_list:
        # Проверка всех
        if args.students_list:
            with open(args.students_list, 'r') as f:
                students = [line.strip() for line in f if line.strip()]
        else:
            # Автоматически ищем файлы student_tasks_*.json
            students = []
            for f in Path('.').glob('student_tasks_*.json'):
                name = f.stem.replace('student_tasks_', '')
                students.append(name)
        
        checker.check_all_students(students)
    
    # Экспорт
    if args.export:
        checker.export_to_csv(args.export)

if __name__ == "__main__":
    main()
