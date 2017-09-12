from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

while True:
    user_input = prompt('>',
                        history=FileHistory('history.txt'),
                       )
    print(user_input)
