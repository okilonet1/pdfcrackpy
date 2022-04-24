import pikepdf
import random
import itertools
import math

locked_file = input("Input the directory of the locked pdf file: ")
total_passwords = math.factorial(10)/(math.factorial(10-4))
choices = [''.join(x) for x in itertools.permutations('0123456789', 4)]

for index, choice in enumerate(choices):
    password = random.choice(choices)
    try:
        with pikepdf.open(locked_file, password=password) as pdf_file:
            print("\n+++++++++++++++++++SUCCESS+++++++++++++++")
            print("Success---------- File is Unlocked and the password is: ", password)
            pdf_file.save(f"{locked_file}_unlocked.pdf")
            print("Success---------- File is saved as: ", f"{locked_file}_unlocked.pdf")
            break
    except:
        print("\n=====================")
        print(f"Trying Password {password} --- Fail!!!!")
        scanning = (index / total_passwords) * 100
        print("Scanning passwords complete:", round(scanning, 2), "%")
        continue
