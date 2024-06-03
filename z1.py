import random
import string


def generate(n, l):
    a = string.ascii_letters + string.digits
    passwords = set()

    while len(passwords) < n:
        password = ''.join(random.choice(a) for _ in range(l))
        passwords.add(password)

    return passwords


def main():
    n = int(input("Введите количество паролей: "))
    length = int(input("Введите длину пароля: "))

    passwords = generate(n, length)

    print("Сгенерированные пароли:")
    for i, password in enumerate(passwords, 1):
        print(f"Пароль {i}: {password}")


if __name__ == "__main__":
    main()