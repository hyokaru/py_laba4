import z7_module

def main():
    try:
        n = int(input("Введите количество чисел: "))
        nums = []
        for i in range(n):
            num = int(input(f"Введите число {i + 1}: "))
            nums.append(num)

        max_sum_number = z7_module.max_sum(nums)

        if max_sum_number is not None:
            print(f"Число с максимальной суммой цифр: {max_sum_number}")
        else:
            print("Список чисел пуст.")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()
