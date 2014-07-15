def maximum_prime(n):
    if n <= 1:
        print("Please, insert a number, which is more than 1")
    else:
        import math
        z = int(math.sqrt(n))
        checklist = list(range(2, z + 1))
        all_dividers = []# Container for storage of all dividers for x
        for i in checklist:# Using the trial division method
            if n % i == 0:
                all_dividers.append(i)
        comp_dividers = []# Container for storage of all composite dividers
                          # for x
        for w in all_dividers:
            for c in range(2,w):
                if w % c == 0 and w not in comp_dividers:
                    comp_dividers.append(w)
        final = list(set(all_dividers).difference(comp_dividers))
        # The last container with only prime dividers for x
        print("The maximun prime divider for your number is " + str(max(final)))
        
                     
    


            

