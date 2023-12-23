lst = list(map(int, input().split()))
b = lst.pop() % 2 == 1
lst.append(b)
print(*lst)
