M, N = list(map(int, input("Введите M и N: ").split()))

zeros = []
for i in range(M):
    zeros.append([0] * N)

print(*zeros)

# for i in range(M):
#     for j in range(N):
#         zeros[i][j] = 1
#
# print(zeros)
