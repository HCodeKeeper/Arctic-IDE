def directory_to_string(directory):
    directory_listed = directory.split('/')
    new_directory = ""
    for i, path in enumerate(directory_listed):
        if ' ' in path:
            path=f"'{path}'"
        if i > 0:
            path = f'\{path}'
        new_directory += path

    return new_directory