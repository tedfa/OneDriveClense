import os

invalid_chars = ["*", ":", "<", ">", "?", "/", "\\", "|"]

path = input("Enter path to sanitize: ")


def replace_invalid(path, invalid_chars):
    path = r'{}'.format(path)

    for root, dirs, files in os.walk(path, topdown=True):

        # Sanitize subdirectory names
        for i, name in enumerate(dirs):
            new_name = name

            for char in invalid_chars:
                if char in name:
                    new_name = name.replace(char, '_')

                    print(f"Renaming subdir {repr(os.path.join(root, name))} to {repr(os.path.join(root, new_name))}")

            if new_name != name:
                os.rename(os.path.join(r'{}'.format(root), name), os.path.join(r'{}'.format(root), new_name))
                dirs[i] = new_name

        root = r'{}'.format(root)

        # Sanitize file names
        for name in files:
            new_name = name

            for char in invalid_chars:
                if char in name:
                    new_name = name.replace(char, '_')

                    print(f"Renaming file {repr(os.path.join(root, name))} to {repr(os.path.join(root, new_name))}")

            if new_name != name:
                os.rename(os.path.join(r'{}'.format(root), name), os.path.join(r'{}'.format(root), new_name))


replace_invalid(path, invalid_chars)