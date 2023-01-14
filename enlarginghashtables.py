def fn(n):
  f = 1
  for i in range(2, int(n**.5)+1):
    if n % i == 0:
      f = 0
      break
  return f
n = int(input())
while n!= 0:
  s = n*2
  while 1:
    if fn(s):
      break
    s += 1
  if fn(n):
    print(s)
  else:
    print(s,  f"({n} is not prime)")
  n = int(input())