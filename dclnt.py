import ast
import os
import collections
import itertools
from nltk import pos_tag


def get_top_words_in_path(path, top_size=10):
    """
    Получает список слов, входящих в имена всех функций из всех .py файлов по указанному пути, и возвращает top_size самых
    повторяемых глаголов
    :param path:        Путь к директории с исходным кодом, который необходимо анализировать
    :param top_size:    Количество глаголов, для которых надо выводить статистику (величина топа)
    :return:            Список длиной top_size с наиболее встречающимися глаголами в названиях функций
    """
    trees = [t for t in _get_trees(path) if t]
    funcs = _flat([_get_all_functions_names(t) for t in trees])
    words = _flat([_get_words_from_function_name(function_name) for function_name in funcs])
    return collections.Counter(words).most_common(top_size)


def get_top_verbs_in_path(path, top_size=10):
    """
    Получает список глаголов, входящих в имена всех функций из всех .py файлов по указанному пути, и возвращает top_size
    самых повторяемых глаголов
    :param path:        Путь к директории с исходным кодом, который необходимо анализировать
    :param top_size:    Количество глаголов, для которых надо выводить статистику (величина топа)
    :return:            Список длиной top_size с наиболее встречающимися глаголами в названиях функций
    """
    trees = [t for t in _get_trees(path) if t]
    funcs = _flat([_get_all_functions_names(t) for t in trees])
    verbs = _flat([_get_verbs_from_function_name(function_name) for function_name in funcs])
    return collections.Counter(verbs).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    """
    Получает список имен всех функций из всех .py файлов по указанному пути и возвращает top_size самых повторяемых
    :param path:        Путь к директории с исходным кодом, который необходимо анализировать
    :param top_size:    Количество функций, для которых надо выводить статистику (величина топа)
    :return:            Список длиной top_size с наиболее встречающимися именами функций
    """
    trees = _get_trees(path)
    funcs = _flat([_get_all_functions_names(t) for t in trees])
    return collections.Counter(funcs).most_common(top_size)


def _flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return [itertools.chain.from_iterable(_list)]
    # return sum([list(item) for item in _list], [])


def _is_verb(word):
    """
    Проверяет, является ли слово глаголом
    :param word:    Слово
    :return:        True, если слово является глаголом, False, если нет
    """
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def _get_trees(path):
    """
    Находит файлы с расширением .py (максимум 100 файлов) и строит из их содержимого деревья с помощью ast
    :param path:                Путь к дирктории, внутри которой искать файлы
    :param with_filenames:      Признак, указывающий, записывать ли имена анализируемых файлов
    :param with_file_content:   Признак, указывающий, записывать ли содержимое анализируемых файлов
    :return:                    Список деревьев, постороенных из файлов. Элемент списка - кортеж
    """
    py_filenames = []
    trees = []
    for dirname, dirs, files in os.walk(path, topdown=True):
        _get_py_files_names(py_filenames, dirname, files)

    for filename in py_filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
            try:
                tree = ast.parse(main_file_content)
            except SyntaxError as e:
                tree = None

        trees.append(tree)

    return trees


def _get_py_files_names(py_filenames, dirname, files, limit=100):
    for file in files:
        if file.endswith('.py'):
            py_filenames.append(os.path.join(dirname, file))
            if len(py_filenames) == limit:
                break


def _get_all_functions_names(tree):
    """
    Возвращает список имен всех функций в дереве (файле), за исключением системных
    :param tree:    Дерево, построенное по файлу .py
    :return:        Список имен всех функций в дереве, за исключением системных
    """

    all_funcs = [node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    return [f for f in all_funcs if not (f.startswith('__') and f.endswith('__'))]


# def _get_all_names(tree):
#     """
#     Возвращает список всех имен из дерева (файла)
#     :param tree:    Дерево, построенное по файлу .py
#     :return:        Список всех имен в дереве
#     """
#     return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def _get_verbs_from_function_name(function_name):
    """
    Возвращает список глаголов, входящих в название функции
    :param function_name:   Название функции
    :return:                Список глаголов, входящих в название функции
    """
    return [word for word in function_name.split('_') if _is_verb(word)]


def _get_words_from_function_name(function_name):
    """
    Возвращает список слов, входящих в название функции
    :param function_name:   Название функции
    :return:                Список слов, входящих в название функции
    """
    return [word for word in function_name.split('_')]


if __name__ == 'main':
    projects = [('jobReqSync', '/home/nikonov/dev/jobReqSync'), ]
    for project in projects:
        stats = get_top_verbs_in_path(project[1], 5)
        print('Project {} top verbs\n'.format(project[0]))
        print(stats)
