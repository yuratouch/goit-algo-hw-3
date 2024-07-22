import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії.')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist).')
    return parser.parse_args()

def copy_and_sort_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_extension = os.path.splitext(file)[1].lstrip('.').lower()
                if file_extension == '':
                    file_extension = 'no_extension'
                dest_sub_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(dest_sub_dir, exist_ok=True)
                shutil.copy(file_path, dest_sub_dir)
                print(f"Копіювання {file} до {dest_sub_dir}")
            except Exception as e:
                print(f"Помилка копіювання {file}: {e}")

def main():
    args = parse_arguments()
    src_dir = args.src_dir
    dest_dir = args.dest_dir

    if not os.path.isdir(src_dir):
        print(f"Помилка: {src_dir} не є директорією або не існує.")
        return

    os.makedirs(dest_dir, exist_ok=True)
    copy_and_sort_files(src_dir, dest_dir)
    print(f"Копіювання та сортування завершено. Всі файли скопійовані до {dest_dir}.")

if __name__ == '__main__':
    main()
