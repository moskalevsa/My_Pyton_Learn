# Импортируем библиотеку
from subprocess import run

# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
def git_config_list():
    # Удаляем заглушку, создаем переменную result:
    # Используем subprocess.run для выполнения команды в переменной result

    result = run('git config --global --list', shell = True, )
     # Выводим результат выполнения команды result.stdout
    return print (f'{result.stdout}')

# вызываем git_config_list()
print(git_config_list())
