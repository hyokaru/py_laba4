import random

def exam(exams, subjects):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    times = ["8:30", "9.00", "10:05", "11:45"]
    ticket_numbers = list(range(1, 30))

    random.shuffle(subjects)
    if len(times) < exams:
        raise ValueError("Количество экзаменов превышает количество доступных временных интервалов.")

    schedule = []
    for i in range(exams):
        subject = subjects[i]
        day = random.choice(days_of_week)
        time = times.pop()
        ticket_number = random.choice(ticket_numbers)
        schedule.append((subject, day, time, ticket_number))

    return schedule

def main():
    try:
        exams = int(input("Введите количество экзаменов: "))
        subjects_input = input("Введите наименования дисциплин через запятую и пробел: ")
        subjects = [subject.strip() for subject in subjects_input.split(",")]

        if exams > len(subjects):
            raise ValueError("Количество экзаменов превышает количество уникальных дисциплин.")

        schedule = exam(exams, subjects)

        for subject, day, time, ticket_number in schedule:
            print(f"Экзамен по дисциплине {subject} состоится в день недели {day} в {time}. Ваш счастливый билет - {ticket_number}.")

    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
