def fibo(n):
  if n == 0: print(n)
  elif n == 1: print(n)
  else:
    a = 0
    b = 1
    counter = 1
    while True:
      if counter < n:
        counter += 1
        c = a + b
        z = c
      else:
        break
      if counter < n:
        counter += 1
        a = b + c
        z = a
      else:
        break
      if counter < n:
        counter += 1
        b = c + a
        z = b
      else:
        break
    print("Your Fibonacci number is " + str(z))
  
