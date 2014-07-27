def check(n):# Here I used a call for a function inside another function
    divisor = 2
    all_numbers = list(range(2,n+1))
    while divisor <= n:
        for step in all_numbers:
            if step % divisor == 0 and step != divisor:
                all_numbers.remove(step)
        divisor += 1
    return all_numbers
    
def sieve(n):
    if n == 0 or n == 1: print(n)
    else: return check(n)



        
    
