"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""


import hashlib
from urllib.parse import urlparse
from uuid import uuid4

class url_lib():
    library = {}
    def new_url(self, url):
        salt = uuid4().hex
        parsed_url = urlparse(url)
        if parsed_url.netloc in self.library.keys():
            return print('this url is already in a url library!')
        else:
            self.library[parsed_url.netloc] = hashlib.sha256(salt.encode() + parsed_url.netloc.encode()).hexdigest()
            return print('added new url to the library')

    def __str__(self):
        return str(self.library)


le_url_library = url_lib()

le_url_library.new_url('http://www.encoder.net')
le_url_library.new_url('https://www.le_me_in_python.com/im_a_junior_dev.php')
print(le_url_library)
le_url_library.new_url('https://www.encoder.net')
print(le_url_library)

