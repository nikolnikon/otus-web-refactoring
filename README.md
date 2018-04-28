# dclnt lib

dclnt это библиотека, которая позволяет собирать статистику по использованию слов в названиях функций, содержащихся в
модулях того или иного проекта. С ее помощью можно определить самые встречающиеся слова и глаголы в названиях функций,
а также самые встречающиеся имена функций.

## Пример использования

Код:
```python
projects = [('jobReqSync', '/home/nikonov/dev/jobReqSync'), ('jobLauncher', '/home/nikonov/dev/jobLauncher')]
    for project in projects:
        stats = get_top_verbs_in_path(project[1], 5)
        print('Project "{}" top verbs'.format(project[0]))
        for verb in stats:
            print('\t{verb}: {occurence}'.format(verb=verb[0], occurence=verb[1]))
```
Вывод:
```
Project "jobReqSync" top verbs
	get: 6
	run: 1
Project "jobLauncher" top verbs
	get: 5
	run: 1
	add: 1
```

## Установка

С использованием pip:
```bash
$ pip install dclnt
```

С использованием git и установкой зависимостей из requirements.txt:
```bash
$ git clone https://github.com/nikolnikon/otus-web-refactoring.git ./dclnt
$ cd dclnt
$ pip install -r requirements.txt
$ python
>>> import nltk
>>> nltk.download('averaged_perceptron_tagger')
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /home/nikonov/nltk_data...
[nltk_data]   Unzipping taggers/averaged_perceptron_tagger.zip.
True
```

## Документация


## Участие в проекте


## Тестирование


## Версионирование
Используется подход [semantic versioning](https://github.com/dbrock/semver-howto/blob/master/README.md).

## Лицензия
Проект распространяентся под лицензией MIT. Подробная информация в файле
[LICENSE](https://github.com/nikolnikon/otus-web-refactoring/blob/master/LICENSE)
