import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Clubs:
    def __init__(self):
        self.list = []

    def addClub(self, name: str, city: str, titles: int, age: float) -> None:
        self.list.append([name, city, titles, round(age, 2)])

    def sortClub(self, attr: int) -> bool:
        if attr >= 0 and attr <= len(self.list):
            self.list.sort(key=lambda x: x[attr - 1])
            return True
        return False

    def removeClub(self, n: int) -> None:
        if num > len(clubs.list) or num < 0:
            print("Введено неверное число")
        else:
            self.list.pop(n - 1)

    def printClubs(self, titles=0) -> None:
        maxlen = [0, 0, 0]
        for club in self.list:
            if club[2] >= titles:
                for i in range(len(club) - 1):
                    maxlen[i] = max(maxlen[i], len(str(club[i])))
        for club in self.list:
            if club[2] >= titles:
                for i in range(len(club) - 1):
                    print(
                        str(club[i]) + " " * (maxlen[i] - len(str(club[i])) + 3),
                        end="",
                        sep="",
                    )
                print(club[3])


clubs = Clubs()
clubs.addClub("Бокс", "Москва", 4, 15.2)
clubs.addClub("Самбо", "Новосибирск", 15, 24.6)
clubs.addClub("Каратэ", "Санкт-Петербург", 5, 14.2)
clubs.addClub("Футбол", "Екатеринбург", 7, 11.0)


while True:
    print(
        """1. Вывести все спортивные клубы.
2. Выход из программы.
3. Добавление нового клуба.
4. Удаление клуба.
5. Сортировка клубов по выбранному свойству.
6. Вывести все клубы, завоевавшие титулов в количестве не менее указанного значения
7. Вывести средний возраст по всем клубам в месяцах"""
    )
    n = input("Выберите вариант: ")
    try:
        clear()
        n = int(n)
        match n:
            case 1:
                clubs.printClubs()
            case 2:
                break
            case 3:
                if len(clubs.list) >= 12:
                    print("Возможно записать не более 12 клубов.")
                else:
                    name = input("Введите имя: ")
                    city = input("Введите город: ")
                    titles = int(input("Введите количество завоёванных титулов: "))
                    age = float(input("Введите средний возраст игроков в годах: "))
                    clubs.addClub(name, city, titles, age)
                    clear()
                    print("Клуб добавлен.")
            case 4:
                num = int(input("Введите номер клуба для удаления: "))
                clubs.removeClub(num)
            case 5:
                print(
                    """1. Название клуба
2. Город, где базируется клуб
3. Количество завоеванных титулов
4. Средний возраст игроков в годах"""
                )
                attr = int(input("Выберите свойство: "))
                clear()
                if clubs.sortClub(attr):
                    print("Клубы отсортированы.")
                else:
                    print("Введено неверное число.")
            case 6:
                num = int(input("Введите значение: "))
                clear()
                clubs.printClubs(num)
            case 7:
                for i in clubs.list:
                    print(i[0], ": ", int(i[3] * 12), " мес.", sep="")
    except ValueError:
        clear()
        print("Введено неправильное значение.")
