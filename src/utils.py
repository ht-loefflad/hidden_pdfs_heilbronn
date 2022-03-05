import os


def make_sure_dir_exists(dirname: str):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print(f"Created directory '{dirname}'")
