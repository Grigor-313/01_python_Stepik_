'''
s = 'pithon'
type(s)
<class 'str'>
s.upper()
'PITHON'
s
'pithon'
res = s.upper()
res
'PITHON'
res.lower()
'pithon'
msg = 'abrakadabra'
msg.count('ra')
2
msg.count('ra', 4)
1
msg.count('ra', 4 ,10)
0
msg.count('ra', 4, 12)
1
msg.find('br')
1
msg.find('br', 2)
8
msg.find('brr', 2)
-1
msg
'abrakadabra'
msg.replace('a', 'o')
'obrokodobro'
msg.replace('ab', 'AB')
'ABrakadABra'
msg.replace('ab', '')
'rakadra'
msg.replace('a', 'o', 2)
'obrokadabra'
msg.isalpha()
True
'hello world'.isalpha()
False
'5.6'.isdigit()
False
'56'.isdigit()
True
'-56'.isdigit()
False
d = 'abc'
d.rjust(5)
'  abc'
d = '12'
d.rjust(4, '0')
'0012'
d.rjust(4, '00')
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
d.ljust(1, '0')
'12'
d.ljust(10, '*')
'12********'
'Иванов Иван Иванович'.split(' ')
['Иванов', 'Иван', 'Иванович']
digs = '1, 3,  8,   9,4, 5, 9'
digs.replace(' ', '').split(',')
['1', '3', '8', '9', '4', '5', '9']
d = digs.replace(' ', '').split(',')
d
['1', '3', '8', '9', '4', '5', '9']
', '.join(d)
'1, 3, 8, 9, 4, 5, 9'
fio = 'Иванов Иван Иванович'
', '.join(fio.split())
'Иванов, Иван, Иванович'
'    hello word,     \n'.strip()
'hello word,'
 hello word,     \n'.strip()
'hello word,'
'    hello word,     \n'.rstrip()
'    hello word,'
'    hello word,     \n'.lstrip()
'hello word,     \n'


'''
