
def total_salary(path):
    try:
        salaries = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:  # Пропускаємо порожні рядки
                    continue
                    
                try:
                    parts = line.split(',')
                    if len(parts) != 2:
                        print(f"Помилка: Неправильний формат рядка: {line}")
                        continue
                    
                    _, salary_str = parts
                    salary = int(salary_str.strip())
                    salaries.append(salary)
                    
                except ValueError as e:
                    if "invalid literal for int()" in str(e):
                        print(f"Помилка: Неправильне значення зарплати: {line}")
                    else:
                        print(f"Помилка: {e}")
                    continue
        
        if not salaries:
            print("Помилка: Файл порожній або не містить валідних даних")
            return (0, 0)
            
        total = sum(salaries)
        average = total // len(salaries) 
        
        return total, average
        
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено: {path}")
        return (0, 0)
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return (0, 0)
    