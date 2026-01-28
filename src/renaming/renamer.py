import os
def rename():
    d = []
    for root, dirs, files in os.walk('.'):
        for name in files:
            full_path = os.path.join(root, name)
            d.append(full_path)
    for i, path in enumerate(d):
        print(f"{i}, {path}")

    try:
        index = int(input("Pick the index you want: "))
        new_name = input("Pick a new name for the file: ")

        old_path = d[index]

        directory = os.path.dirname(old_path)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
    except (ValueError, IndexError):
        print("Value or index error")
    except Exception:
        print("General Exception")

