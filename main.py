from script import FileManager


fm = FileManager()
while True:
    cmd = input('Введите команду(help - для помощи)> ')
    if cmd == 'get_list':
        fold = input('Показать только папки(Enter, если нужны все файлы)> ')
        if fold == '':
            fm.get_list()
        else:
            fm.get_list(folders_only=True)
        print()
    elif cmd == 'create_file':
        name = input('Введите имя файла> ')
        data = input('Введите данные(Enter,чтобы оставить файл пустым)> ')
        if data == '':
            fm.create_file(name)
        else:
            fm.create_file(name, data)
        print()
    elif cmd == 'get_data':
        name = input('Введите имя файла> ')
        fm.get_data(name)
        print()
    elif cmd == 'create_folder':
        name = input('Введите имя папки> ')
        fm.create_folder(name)
        print()
    elif cmd == 'delete':
        name = input('Введите имена файлов или папок для удаления> ').split(',')
        name = [n.strip() for n in name]
        fm.delete(name)
        print()
    elif cmd == 'rename':
        name = input('Введите имя файла> ')
        new_name = input('Введите новое имя файла> ')
        fm.rename(name, new_name)
        print()
    elif cmd == 'copy_file':
        name = input('Введите имя файла или папки> ')
        new_folder = input('Введите новый путь> ')
        move = input('Переместить файл?(Enter, чтобы копировать)> ')
        if move == '':
            fm.copy_file(name, new_folder)
        else:
            fm.copy_file(name, new_folder, move_file=True)
        print()
    elif cmd == 'move_in_dir':
        move = input('Введите номер папки(<,чтобы вернуться назад)> ')
        fm.move_in_dir(move, fm.get_list(prnt=False))
        print()
    elif cmd == 'help':
        print(f'{fm.get_list.__name__} -> {fm.get_list.__doc__}')
        print(f'{fm.create_file.__name__} -> {fm.create_file.__doc__}')
        print(f'{fm.create_folder.__name__} -> {fm.create_folder.__doc__}')
        print(f'{fm.delete.__name__} -> {fm.delete.__doc__}')
        print(f'{fm.rename.__name__} -> {fm.rename.__doc__}')
        print(f'{fm.get_data.__name__} -> {fm.get_data.__doc__}')
        print(f'{fm.copy_file.__name__} -> {fm.copy_file.__doc__}')
        print(f'{fm.move_in_dir.__name__} -> {fm.move_in_dir.__doc__}')
        print('exit -> Закончить работу')
        print()
    elif cmd == 'exit':
        break
    else:
        print('Некорректная команда')
