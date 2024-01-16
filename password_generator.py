import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Prosze dalej liczbe znakow do Twojego hasla: "))

safe_password = ""

for i in range(password_length):
    safe_password += random.choice(characters)

print(safe_password)
