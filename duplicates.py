import os


def get_file_list(dir_path):
    all_files_info = []
    all_files_list = os.walk(dir_path)
    for all_files in all_files_list:
        for file in all_files[2]:
            file_info = dict(path=all_files[0], name=file, size=file.__sizeof__())
            all_files_info.append(file_info)
    return all_files_info


def find_duplicates(all_files_info):
    duplicates = []
    for file_1 in all_files_info:
        for file_2 in all_files_info:
            if file_1['name'] == file_2['name'] \
                    and file_1['size'] == file_2['size'] \
                    and file_1['path'] != file_2['path']:
                duplicates.append(file_2['path'] + '/' + file_2['name'])
                all_files_info.remove(file_2)
    return duplicates


def delete_duplicates(duplicates):
    files_removed = []
    for file in duplicates:
        os.remove(file)
        files_removed.append(file)
    return files_removed


if __name__ == '__main__':
    directory = input("Enter directory to clean --> ")
    files = get_file_list(directory)
    duplicated_files = find_duplicates(files)
    removed_files = delete_duplicates(duplicated_files)
    for removed_file in removed_files:
        print("File removed: ", removed_file)
