m = ['', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = (map(int, input().split()))
m[a] = '#до' if a == 1 else m[a]
m[a] = '#фа' if a == 4 else m[a]
m[b] = '#до' if b == 1 else m[b]
m[b] = '#фа' if b == 4 else m[b]
m[c] = '#до' if c == 1 else m[c]
m[c] = '#фа' if c == 4 else m[c]
print(m[a], m[b], m[c])
