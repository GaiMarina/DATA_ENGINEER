"""Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
"""

from module_func_game import more_less_game
from riddles_6_sem_modules import puzzle_riddles, dictionary_output


__all__ = ['more_less_game', 'puzzle_riddles', 'dictionary_output']

# Теперь импортировать можно не отдельно из каждого файла, а из общей папки любую указанную функцию: import DE_py_seminars
# Если, при импорте не находит, перед названием модуля в импорте - добавить точку. from .module_func_game