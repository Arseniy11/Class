my_book = open('Phonebook.txt', 'r')
my_list = []
for every_line in my_book:
    if every_line != "\n":
        separate = every_line.split(": ")
        first_word = separate[0]
        second_word = separate[1]
        second_word_pure = len(second_word) - 1
        second_word = second_word[0: second_word_pure]
        my_tuple = (first_word, second_word)
        my_list.append(my_tuple)
    else: pass
my_list.sort()

def get_name(phone_number):
    # I couldn't come up with anything better so I have to repeat myself.
    phone_number = str(phone_number)
    for check_line in my_list:
        if check_line[0] == phone_number:
            return(check_line[1])
    else: return "Nothing found"
    
