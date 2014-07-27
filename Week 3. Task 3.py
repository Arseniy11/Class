import random, string
for check in range(100000):
    number = ''.join(random.sample(string.digits, 7))
    # I used the random.sample() method here, because we need 100000 unique numbers
    name_length = range(random.randint(4, 10))
    name = ''.join(random.choice(string.ascii_lowercase) for check_2 in name_length)
    # I used the random.choice() method here, because we can't build 100000 unique
    # names on the basis of English alphabet. So some names must repeat each other
    phonebook = open('Phonebook.txt', 'a')
    phonebook.write(number + ": " + name + "\n")
    phonebook.close()

    
