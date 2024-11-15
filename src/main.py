import os
import shutil
from generatepage import generate_page_recursively


def main():
    if os.path.exists('public'):
        shutil.rmtree('public')
    os.mkdir('public')

    def copy_contents(src_dir, dest_dir):
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dest_path = os.path.join(dest_dir, item)

            if os.path.isdir(src_path):
                os.mkdir(dest_path)
                copy_contents(src_path, dest_path)
            else:
                shutil.copy(src_path, dest_path)

    copy_contents("static", "public")
    generate_page_recursively("content", "template.html", "public")


main()
