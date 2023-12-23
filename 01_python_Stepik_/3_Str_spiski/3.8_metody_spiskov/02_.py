a = list(input())
a.remove('+')
a[0] = '8'
a.remove('-')
a.remove('-')
print("".join(a))
