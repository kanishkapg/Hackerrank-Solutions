n, m = map(int, input().split(' '))

result1 = [('.|.' * (2*i-1)).center(m, '-') for i in range(1, (n+1)//2)]
result2 = 'WELCOME'.center(m, '-')
result3 = [('.|.' * (2*i-1)).center(m, '-') for i in range((n//2), 0, -1)]

print('\n'.join([j for j in result1]))
print(result2)
print('\n'.join([r for r in result3]))
