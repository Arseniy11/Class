my_book = open('Phonebook.txt', 'r')
my_dict = {}
for every_line in my_book:
    if every_line != "\n":
        # Because I used the mode 'a' in task № 3 to create and fill the
        # "Phonebook.txt" file. That means that the last line in the file will
        # be empty.
        separate = every_line.split(": ")
        first_word = separate[0]
        second_word = separate[1]
        second_word_pure = len(second_word) - 1
        # Because there is \n at the end of every line
        second_word = second_word[0: second_word_pure]
    else: pass
    my_dict[first_word] = second_word

def get_name(phone_number): # With usage of built-in get() method.
    phone_number = str(phone_number)
    return my_dict.get(phone_number, "Nothing found.")

def get_name_2(phone_number): # Without get() method.
    phone_number = str(phone_number)
    list(my_dict.keys())
    if phone_number in my_dict: return my_dict[phone_number]
    else: return "Nothing found."
        
