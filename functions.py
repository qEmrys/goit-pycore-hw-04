def total_salary(path:str) -> tuple:
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
    except FileNotFoundError:
        print("File not found")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

    total_salary = 0

    for line in lines:
        line = line.strip()
        total_salary += int(line.split(',')[1])

    average = total_salary//len(lines)

    return (total_salary, average)


def get_cats_info(path:str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    cats_info = []
    try:
        for line in lines:
            line = line.strip()
            if line:
                cat_id, name, age = line.split(',')
                cats_info.append({"id": cat_id, "name": name, "age": int(age)})
    except Exception as e:
        print(f"An error occurred while processing cat information: {e}")
        return []

    return cats_info
