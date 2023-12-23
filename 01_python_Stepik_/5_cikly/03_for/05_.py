x = int(input())
y = []
for i in range(1, x + 1):
    if x % i == 0:
        y.append(i)
        if len(y) >= 2:
            if y[-1] != x:
                print('НЕТ')
                break

        if y[-1] == x:
            print('ДА')
            break

# print('ДА')
# print('НЕТ')

'''n = int(input())
m = 0
for i in range(1, n+1):
    if n % i == 0:
        m += i
if m == 1 + n:
    print("ДА")
else:
    print("НЕТ")  '''

'''n = int(input())
msg = 'ДА'

for i in range(2, n // 2 + 1):
    if n % i == 0:
        msg = 'НЕТ'
        break
        
print(msg)'''
