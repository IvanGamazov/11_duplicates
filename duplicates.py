import os


def get_file_list(dir_path):
    all_files_info = []
    all_files_list = os.walk(dir_path)
    for all_files in all_files_list:
        for name_of_file in all_files[2]:
            file_info = dict(path=all_files[0], name=name_of_file, size=get_file_size(name_of_file))
            all_files_info.append(file_info)
    return all_files_info


def get_file_size(filename):
    if os.path.exists(filename):
        return os.path.getsize(filename)
    else:
        return None


def find_duplicates(all_files_info):
    duplicates = []
    for file_1 in all_files_info:
        for file_2 in all_files_info:
            if check_if_files_are_duplicates(file_1, file_2):
                duplicates.append('Файл ' + file_2['path'] + '/' + file_2['name']
                                  + ' - дубликат файла ' + file_1['path'] + '/' + file_1['name'])
                all_files_info.remove(file_2)
    return duplicates


def check_if_files_are_duplicates(file_1, file_2):
    if file_1['name'] == file_2['name'] \
            and file_1['size'] == file_2['size'] \
            and file_1['path'] != file_2['path']:
        return True
    else:
        return False


if __name__ == '__main__':
    directory = input("Укажите директорию для проверки --> ")
    files = get_file_list(directory)
    duplicated_files = find_duplicates(files)
    for duplicate in duplicated_files:
        print(duplicate)
