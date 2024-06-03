import z6_module

def main():
    try:
        n = int(input("Введите количество элементов в списке: "))
        lst = []

        for i in range(n):
            num = int(input(f"Введите элемент {i + 1}: "))
            lst.append(num)

        k = int(input("Введите значение K (элементы, которые останутся неизменными): "))
        m = int(input("Введите значение M (на которое будут заменены все остальные элементы): "))

        mod_list = z6_module.replace(lst, k, m)
        print("Измененный список:", mod_list)

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()
