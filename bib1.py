# 1
# a = int(input())
#
# n1 = a % 10
# n2 = a // 10 % 10
#
# n3 = a // 100 % 10
# n4 = a // 1000 % 10
#
# a1 = n3 * 10 + n4
# a2 = n2 * 10 + n1
#
# print(((a1+1) % (a2+1)) + 1)

# 2

a = int(input())
b = int(input())

u = a // b

c = (u - 1) // (u + 1) + 1

print(c * a + (1 - c) * b)