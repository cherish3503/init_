import math

def eratosthenes(n):
  # n이하의 소수의 리스트를 리턴
  prime = [False,False] + [True]*(n-1)
  for i in range(2, math.floor(n ** 0.5)+1):
    if prime[i] == True:
      for j in range(2*i, n+1, i):
        prime[j] = False
  
  return [i for i in range(2,n+1) if prime[i] == True]
