from collections import OrderedDict
from pprint import pprint
all_f = {}
file_list = ['1.txt', '2.txt', '3.txt']

def read_data(file_list):
    for f in file_list:
        with open (f, encoding='utf-8') as file:
            data = file.readlines()
            numb_lines_f=len(data)
            name = f
            f_dict = {name:[str(numb_lines_f), data]}
            all_f.update(f_dict)

read_data(file_list)

def write_sort_files(all_f):
    sorted_tuples = sorted(all_f.items(), key=lambda item: item[1])

    sorted_dict = OrderedDict()
    for k, v in sorted_tuples:
        sorted_dict[k] = v

    with open('all_f.txt', 'w', encoding='utf-8') as f:
        for key, val in sorted_dict.items():
            f.write(f'{key}\n')
            for el in val:
                for elem in el:
                    f.write(f'{elem.rstrip()}\n')

write_sort_files(all_f)