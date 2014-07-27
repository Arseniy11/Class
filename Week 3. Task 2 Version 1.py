def sieve(n):
    if n == 0 or n == 1: print(n)
    else:
        divisor = 2
        all_numbers = list(range(2,n+1))
        while divisor <= n:
            for step in all_numbers:
                if step % divisor == 0 and step != divisor:
                    all_numbers.remove(step)
            divisor += 1 
        return all_numbers


        
    
