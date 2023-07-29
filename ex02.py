# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def get_award(name: list, salary: list, award: list) -> dict:
    return {name: salary / 100 * float(award) for name, salary, award in
            zip(name, salary, map(lambda x: x.replace('%', ''),
                                  award))}


print(get_award(name=["Иван", "Николай", "Петр"], salary=[125_000, 96_000, 109_000], award=['10.5%', '25.2%', '13%']))