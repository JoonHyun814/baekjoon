# 에라토스 테네스의 체
# import math

# n = 1000000

# is_prime = [False,False] + [True for _ in range(n-1)]

# for i in range(2,n):
#     if is_prime[i]:
#         k = 2
#         not_prime = i*k
#         while not_prime <= n:
#             is_prime[not_prime] = False
#             k += 1
#             not_prime = i*k

# prime_list = []
# for i in range(int(math.sqrt(n))):
#     if is_prime[i]:
#         prime_list.append(i)


# N = int(input())
# answer = 0
# for n in range(1,N+1):
#     div_primes = {}
#     while n != 1:
#         for prime in prime_list:
#             if prime > n:
#                 break
#             if n%prime == 0:
#                 if prime in div_primes:
#                     div_primes[prime] += 1
#                 else:
#                     div_primes[prime] = 1
#                 n //= prime
#                 break

#     sum_divs = 1
#     for k,v in div_primes.items():
#         s = 0
#         for i in range(v+1):
#             s += k**i
#         sum_divs *= s
    
#     answer += sum_divs

n = int(input())

sum = 0
for i in range(1,n+1):
    a = n//i
    sum += a*i

print(sum)