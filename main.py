import os

from src.functions import Trimmer


def main():
    files = os.listdir('source')
    trimmer = Trimmer()
    for file in files:
        full_path = os.path.join('source', file)
        trimmer.trim(full_path, 'result')


if __name__ == '__main__':
    main()
