'''lst = ['Москва', 'Уфа,' 'Тверь', 'Казань']
lst[1,3]
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
lst[1:3]
['Уфа,Тверь', 'Казань']
lst = ['Москва', 'Уфа', 'Тверь', 'Казань']
lst
['Москва', 'Уфа', 'Тверь', 'Казань']
lst[1:3]
['Уфа', 'Тверь']
a = lst[1:3]
a[0] = 'Воронеж'
a
['Воронеж', 'Тверь']
lst
['Москва', 'Уфа', 'Тверь', 'Казань']
lst[2:]
['Тверь', 'Казань']
lst[:3]
['Москва', 'Уфа', 'Тверь']
citis = lst[:]
citis
['Москва', 'Уфа', 'Тверь', 'Казань']
id(lst)
1859040081216
id(citis)
1859039694848
d = lst
id(lst)
1859040081216
id(d)
1859040081216
marks = [2, 3, 4, 5, 3]
marks = [2:-1]
Traceback (most recent call last):
  File "C:\Users\Григорий\AppData\Local\Programs\Python\Python311\Lib\code.py", line 63, in runsource
    code = self.compile(source, filename, symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Григорий\AppData\Local\Programs\Python\Python311\Lib\codeop.py", line 153, in __call__
    return _maybe_compile(self.compiler, source, filename, symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Григорий\AppData\Local\Programs\Python\Python311\Lib\codeop.py", line 73, in _maybe_compile
    return compiler(source, filename, symbol)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Григорий\AppData\Local\Programs\Python\Python311\Lib\codeop.py", line 118, in __call__
    codeob = compile(source, filename, symbol, self.flags, True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<input>", line 1
    marks = [2:-1]
              ^
SyntaxError: invalid syntax
marks[2:-1]
[4, 5]
marks = [2, 3, 4, 3, 5, 3]
marks[1:5:2]
[3, 3]
marks[:5:2]
[2, 4, 5]
marks[1::2]
[3, 3, 3]
marks[::2]
[2, 4, 5]
marks[::-1]
[3, 5, 3, 4, 3, 2]
marks
[2, 3, 4, 3, 5, 3]
marks[::-2]
[3, 3, 3]
marks
[2, 3, 4, 3, 5, 3]
marks[2:4] = ['хорошо', 'удовлетворительно']
marks
[2, 3, 'хорошо', 'удовлетворительно', 5, 3]
marks[::2] [0, 0, 0]
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
marks
[2, 3, 'хорошо', 'удовлетворительно', 5, 3]
marks[::2] = [0, 0, 0]
marks
[0, 3, 0, 'удовлетворительно', 0, 3]
marks[2:4] = 10, 20
marks
[0, 3, 10, 20, 0, 3]
[1, 2, 3] == [1, 2, 3]
True
[1, 2, 3] != [1, 2, 3]
False
[1, 2, 3] > [1, 2, 3]
False
[10, 2, 3] != [1, 2, 3]
True
[1, 2, 3] >= [1, 2, 3]
True
[1, 2, 3] > [1, 2, 3, 4]
False
[10, 2, 'abc'] > [1, 2, 'abc']
True
[1, 2, 'abc'] > [1, 2, 'abc']
False
[1, 2, 'abc'] > [1, 2, 3]
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'''
