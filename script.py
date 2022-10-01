import os
import shutil as sh


class FileManager:
    def __init__(self):
        """Проверяет наличие папки пользователя, если ее нет, то создает новую с заданным именем"""

        user_name = input('Введите пользователя> ')
        if os.path.isdir(os.path.expanduser('~\\Desktop') + f'\\{user_name}'):
            self.loc = os.path.expanduser('~\\Desktop') + f'\\{user_name}'
        else:
            self.loc = os.path.expanduser('~\\Desktop')
            self.create_folder(user_name)
            self.loc += f'\\{user_name}'

        self.dir_kernel = user_name
        self.current_dir = user_name
        self.get_list()

    def create_file(self, name, data=None):
        """Создание файла"""

        with open(self.loc + f'\\{name}', 'w', encoding='utf-8') as f:
            if data:
                f.write(data)

    def get_data(self, name):
        """Получение данных из файла"""

        if os.access(self.loc + f'\\{name}', mode=2):
            with open(self.loc + f'\\{name}', 'r', encoding='utf-8') as f:
                print(' '.join([x.strip('\n') for x in f.readlines()]))
        else:
            print('Проверьте путь к файлу!')

    def create_folder(self, name):
        """Создает папку"""

        try:
            os.mkdir(self.loc + f'\\{name}')
        except FileExistsError as ex_:
            print(ex_)

    def get_list(self, folders_only=False, prnt=True):
        """Получение нумерованного словаря файлов или папок в текущей директории"""

        list_files = os.listdir(self.loc)
        if folders_only:
            list_files = [file for file in list_files if os.path.isdir(file)]
        dict_files = {i + 1: f for i, f in enumerate(list_files)}
        if prnt:
            print(self.current_dir, end='\n\n')
            for k, v in dict_files.items():
                print(f'{k} -> {v}')
        if not list_files:
            print('Пустая папка')
        return dict_files

    def delete(self, name: list):
        """Удаление файлов или папок"""

        for file in name:
            try:
                if os.path.isdir(self.loc + f'\\{file}'):
                    os.rmdir(self.loc + f'\\{file}')
                else:
                    os.remove(self.loc + f'\\{file}')
            except Exception as ex_:
                print(ex_)

    def rename(self, name, new_name):
        """Переименовывание файла или папки"""

        try:
            os.rename(self.loc + f'\\{name}', new_name)
        except Exception as ex_:
            print(ex_)

    def copy_file(self, name, new_folder, move_file=False):
        """Копирование или перемещение файла или папки(move_file=True)"""

        try:
            if os.path.isdir(self.loc + f'\\{name}'):
                sh.copytree(self.loc + f'\\{name}', new_folder)
            else:
                sh.copy(self.loc + f'\\{name}', new_folder)
        except Exception as ex_:
            print(ex_)
        if move_file:
            self.delete(name)

    def move_in_dir(self, move, files):
        """Переход между папками"""

        def check_int(num):
            try:
                int(num)
                return 1
            except ValueError:
                return None

        if check_int(move) is not None:
            try:
                self.loc += f'\\{files[int(move)]}'
                self.current_dir += f'\\{files[int(move)]}'
                self.get_list()
            except KeyError:
                print('Введен неверный номер папки')
        elif move == '<':
            if self.current_dir != self.dir_kernel:
                self.current_dir = '\\'.join(self.current_dir.split('\\')[:-1])
                self.loc = '\\'.join(self.loc.split('\\')[:-1])
                self.get_list()
            else:
                print('Вы не можете выйти из своей папки')
        else:
            print('Введен некорректный параметр')
