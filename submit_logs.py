#!/usr/bin/env python3
"""
Отправка логов в Git репозиторий
"""
import os
import subprocess
import glob
from datetime import datetime

def submit_logs():
    """Находит логи и отправляет их в Git"""
    
    # Найти все лог-файлы
    log_files = glob.glob("log_*.json")
    
    if not log_files:
        print("❌ Логи не найдены!")
        print("💡 Запустите игру сначала: python game.py")
        return False
    
    print(f"📁 Найдено логов: {len(log_files)}")
    for f in log_files:
        print(f"  - {f}")
    
    # Добавить в Git
    print("\n🔄 Добавление файлов в Git...")
    subprocess.run(["git", "add"] + log_files, check=True)
    
    # Сделать коммит
    print("💾 Создание коммита...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    subprocess.run(
        ["git", "commit", "-m", f"Add game logs - {timestamp}"],
        check=True
    )
    
    # Отправить в репозиторий
    print("📤 Отправка в GitHub...")
    subprocess.run(["git", "push", "origin", "main"], check=True)
    
    print("\n✅ Логи успешно отправлены в репозиторий!")
    return True

if __name__ == "__main__":
    submit_logs()
