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
from urllib.parse import urljoin
from uuid import uuid4

class url_lib():
    library = {}
    def new_url(self, url):
        salt = uuid4().hex
        if '//' in url[:8]:
            if 'https' in url[:5]:
                abs_url = 'https://' + url[8:]
            elif 'http' in url[:4]:
                abs_url = 'http://' + url[7:]
            else:
                abs_url = urljoin('http://', url)
        else:
            abs_url = urljoin('http://', '//' + url)
        if abs_url in self.library.keys():
            return print(self.library[abs_url])
        else:
            self.library[abs_url] = hashlib.sha256(salt.encode() + abs_url.encode()).hexdigest()
            return print('added new url to the library')

    def __str__(self):
        return str(self.library)


le_url_library = url_lib()

le_url_library.new_url('http://www.encoder.net')
le_url_library.new_url('https://www.le_me_in_python.com/im_a_junior_dev.php')
print(le_url_library)
le_url_library.new_url('www.encoder.net')
le_url_library.new_url('//www.example.net')
print(le_url_library)

