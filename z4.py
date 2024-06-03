from datetime import datetime, timedelta

def lucky_day(date):
    return date.day % 4 != 0 and date.weekday() != 0

def dates(start_date, n, count=3):
    lucky_dates = []
    current_date = start_date

    while len(lucky_dates) < count:
        current_date += timedelta(days=n)
        if lucky_day(current_date):
            lucky_dates.append(current_date)
    return lucky_dates

def main():
    try:
        start_date_input = input("Введите исходную дату в формате ГГГГ-ММ-ДД): ")
        n = int(input("Введите число n: "))
        start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
        lucky_dates = dates(start_date, n)

        for date in lucky_dates:
            print(f"Счастливая дата: {date.strftime('%d %B, %A')}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()