# main.py

import z5_module


def main():
    print(z5_module.description())
    number = int(input("Введите число для проверки, является ли оно простым: "))

    if z5_module.num(number):
        print(f"{number} является простым числом.")
    else:
        print(f"{number} не является простым числом.")

if __name__ == "__main__":
    main()
