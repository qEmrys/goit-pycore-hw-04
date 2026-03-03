from pathlib import Path
import sys
from colorama import init, Fore, Style

init(autoreset=True)


def get_directory_structure(directory: Path, indent=0):
    structure = []

    if indent == 0:
        structure.append(Fore.BLUE + directory.name + Style.RESET_ALL)
        indent += 1

    for item in directory.iterdir():
        prefix = '  ' * indent

        if item.is_dir():
            name = Fore.BLUE + item.name + Style.RESET_ALL
            structure.append(prefix + name)
            structure.extend(get_directory_structure(item, indent + 1))
        else:
            name = Fore.GREEN + item.name + Style.RESET_ALL
            structure.append(prefix + name)

    return structure


def main():
    if len(sys.argv) > 1:
        root = Path(sys.argv[1])

        if not root.exists() or not root.is_dir():
            print("Invalid directory path")
            return

        structure = get_directory_structure(root)
        
        for item in structure:
            print(item)


if __name__ == "__main__":
    main()