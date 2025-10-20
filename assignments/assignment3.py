from pathlib import Path
import sys
from colorama import Fore, Style

def display_folder_structure(path, indent=0):
    """
    Рекурсивно відображає структуру папок з правильним відступом та кольоровим виведенням.
    
    Args:
        path: Шлях для відображення (файл або директорія)
        indent: Поточний рівень відступу для правильного форматування
    """
    path = Path(path)
    
    # Визначаємо кольори та формат імені
    if path.is_dir():
        color = Fore.BLUE
        name = f"{path.name}/"
    else:
        color = Fore.GREEN
        name = path.name
    
    # Виводимо поточний елемент з правильним відступом (4 пробіли на рівень)
    indent_str = "    " * indent
    print(f"{indent_str}{color}{name}{Style.RESET_ALL}")
    
    # Якщо це директорія, рекурсивно обробляємо її вміст
    if path.is_dir():
        try:
            # Отримуємо всі елементи в директорії, відсортовані для послідовного виводу
            items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
            for item in items:
                display_folder_structure(item, indent + 1)
        except PermissionError:
            error_indent = "    " * (indent + 1)
            print(f"{error_indent}{Fore.RED}[ERROR] Доступ заборонено{Style.RESET_ALL}")
        except Exception as e:
            error_indent = "    " * (indent + 1)
            print(f"{error_indent}{Fore.RED}[ERROR] {e}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python assignments/assignment3.py <directory_path>{Style.RESET_ALL}")
        return 1
    
    directory_path = sys.argv[1]
    path = Path(directory_path)
    
    # Перевіряємо, чи існує шлях
    if not path.exists():
        print(f"{Fore.RED}[ERROR] Шлях '{directory_path}' не існує{Style.RESET_ALL}")
        return 1
    
    # Перевіряємо, чи це директорія
    if not path.is_dir():
        print(f"{Fore.RED}[ERROR] '{directory_path}' не є директорією{Style.RESET_ALL}")
        return 1
    
    try:
        display_folder_structure(directory_path)
        return 0
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Критична помилка: {e}{Style.RESET_ALL}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
