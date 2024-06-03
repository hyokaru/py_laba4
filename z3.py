from datetime import datetime, timedelta


def date(days_until_exam, current_date):
    exam_date = current_date + timedelta(days=days_until_exam)
    return exam_date


def main():
    try:
        days_until_exam = int(input("Введите количество дней до экзамена: "))
        current_date_input = input("Введите текущую дату в формате ГГГГ-ММ-ДД: ")
        current_date = datetime.strptime(current_date_input, "%Y-%m-%d")

        exam_date = date(days_until_exam, current_date)

        print(f"Экзамен состоится {exam_date.strftime('%d-%m-%Y')}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    main()