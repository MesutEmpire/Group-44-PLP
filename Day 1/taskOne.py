from datetime import date, datetime


class Fare:
    def __init__(self):
        self.day = None
        self.date = None
        self.fare = None
        self.dateName = None
        self.getdate()
        self.getfare()

    def getdate(self):
        today = date.today()
        name = datetime.today()
        self.dateName = name.strftime('%a')
        self.date = date.isoformat(today)
        self.day = date.isoweekday(today)

    def getfare(self):
        if 1 <= self.day <= 5:
            self.fare = 100
        elif self.day == 6:
            self.fare = 60
        elif self.day == 7:
            self.fare = 80
        else:
            print("Error")

    def display(self):
        print("Date : " + str(self.date))
        print("Day : " + str(self.dateName))
        print("Fare : " + str(self.fare))


if __name__ == '__main__':
    cost = Fare()
    cost.display()
