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
