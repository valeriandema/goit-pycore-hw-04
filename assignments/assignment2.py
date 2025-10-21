
def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Помилка: Неправильний формат рядка: {line}")
                    continue
                    
                cat_id, name, age = parts
                
                cat_info = {
                    'id': cat_id,
                    'name': name,
                    'age': age
                }
                cats_info.append(cat_info)
                
    except FileNotFoundError:
        print(f"Помилка: Файл {path} не знайдено")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []
    
    return cats_info

