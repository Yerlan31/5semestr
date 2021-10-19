from operator import itemgetter

class myFile:
    def __init__(self, Id, Name, Size, IdDir):
        self.id = Id
        self.name = Name
        self.size = Size #количественный признак
        self.idd = IdDir

class myDirectory:
    def __init__(self, Id, Name):
        self.id = Id
        self.name = Name

class FileOfDir:
    def __init__(self, IdF, IdD):
        self.idf = IdF
        self.idd = IdD

files = [
    myFile (1, 'Dz', 200, 1),
    myFile (2, 'Elteh', 700, 2),
    myFile (3, 'Proga', 500, 3),
    myFile(4, 'Lab1', 400, 3),
    myFile(5, 'Config', 300, 3),
]

directoties = [
    myDirectory(1, 'Labs'),
    myDirectory(2, 'dir'),
    myDirectory(3, 'Univer'),
    myDirectory(11, 'Work'),
    myDirectory(22, 'Fun'),
    myDirectory(33, 'Secret'),
]

fildir = [
    FileOfDir(1,1),
    FileOfDir(2, 2),
    FileOfDir(3, 3),
    FileOfDir(3, 4),
    FileOfDir(3, 5),

    FileOfDir(11, 1),
    FileOfDir(22, 2),
    FileOfDir(33, 3),
    FileOfDir(33, 4),
    FileOfDir(33, 5),
]

def main():
    # Соединение данных один-ко-многим
    one_to_many = [(e.name, e.size, d.name)
                   for d in directoties
                   for e in files
                   if e.idd == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.idd, ed.idf)
                         for d in directoties
                         for ed in fildir
                         if d.id == ed.idd]

    many_to_many = [(e.name, e.size, dir_name)
                    for dir_name, idd, idf in many_to_many_temp
                    for e in files if e.id==idf]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in directoties:
        # Список сотрудников отдела
        d_files = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если отдел не пустой
        if len(d_files) > 0:
            # Зарплаты сотрудников отдела
            d_sizes = [sal for _, sal, _ in d_files]
            # Суммарная зарплата сотрудников отдела
            d_sizes_sum = sum(d_sizes)
            res_12_unsorted.append((d.name, d_sizes_sum))

    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for d in directoties:
        if 'dir' in d.name:
            # Список сотрудников отдела
            d_files = list(filter(lambda i: i[2] == d.name, many_to_many))
            # Только ФИО сотрудников
            d_files_names = [x for x, _, _ in d_files]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_files_names

    print(res_13)


if __name__ == '__main__':
    main()