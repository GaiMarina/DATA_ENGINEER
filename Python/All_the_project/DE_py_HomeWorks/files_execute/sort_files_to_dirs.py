"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""
"""
import os
from pathlib import Path
import shutil

VIDEO_FOLDER_NAME = 'video'
TEXT_FOLDER_NAME = 'txt'


def sort_files(path):
    p = Path(path)
    for el in p.iterdir():
        suffix = Path(el).suffix[1:]
        if el.is_file() and suffix in ['mp4', 'txt']:
            if suffix == 'mp4':
                os.replace(Path(el), os.path.join(path, VIDEO_FOLDER_NAME, Path(el).name))
            else:
                os.replace(Path(el), os.path.join(path, TEXT_FOLDER_NAME, Path(el).name))


print()
sort_files(Path.cwd() / 'L7_S7')
"""

# ---------------------------------------------
import os
import shutil


def sort_files_by_extension(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)  # создали папку

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_extention = os.path.splitext(file)[1]

            if file_extention.lower() in ('.jpg', 'jpeg', '.png', '.gif'):
                # в папку с изображениями
                image_folder = os.path.join(destination_folder, 'Изображения')
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                shutil.move(file_path, os.path.join(image_folder, file))

            elif file_extention.lower() in ('.txt', 'doc', 'pdf'):
                # в папку с тестовыми документами
                text_folder = os.path.join(destination_folder, 'Текст')
                if not os.path.exists(text_folder):
                    os.makedirs(text_folder)
                shutil.move(file_path, os.path.join(text_folder, file))

            elif file_extention.lower() in ('.mp4', '.avi', '.mkv'):
                # в папку с видео
                video_folder = os.path.join(destination_folder, 'Видео')
                if not os.path.exists(video_folder):
                    os.makedirs(video_folder)
                shutil.move(file_path, os.path.join(video_folder, file))
