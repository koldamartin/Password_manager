#Password Generator Project

from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_list = [choice(letters) for letter in range(randint(4, 5))]
symbols_list = [choice(symbols) for symbol in range(randint(2, 3))]
numbers_list = [choice(numbers) for number in range(randint(2, 3))]
password_list = letters_list + symbols_list + numbers_list
shuffle(password_list)
password = "".join(password_list)



