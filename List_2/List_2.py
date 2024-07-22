n = int(input())
a = list(map(int, input().split()))
a.insert(0, a.pop(-1))
print(a)