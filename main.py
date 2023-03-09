import random


ALPH = "QWERTYUIOPASDFGHJKLZXCVBNM" + "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
LEN = 8
AMOUNT = 50


def gen(l: int) -> str:
    res = ""
    for _ in range(l):
        res += ALPH[random.randint(0, len(ALPH) - 1)]

    return res

passwords = []

for _ in range(AMOUNT):
    passwords.append(gen(LEN)) 

with open("./password.txt", "w") as file:
    for pwd in passwords:
        file.write(pwd + "\n")