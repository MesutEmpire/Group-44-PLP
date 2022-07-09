class Points:
    def __init__(self,booksBought):
        self.awardedPoints = None
        self.books = booksBought
        self.calculatePoints()

    def calculatePoints(self):
        if self.books == 0:
            self.awardedPoints = 0
        elif self.books == 1:
            self.awardedPoints = 6
        elif self.books == 2:
            self.awardedPoints = 16
        elif self.books == 3:
            self.awardedPoints = 32
        elif self.books >= 4:
            self.awardedPoints = 60
        else:
            print("Please Input the correct number of Books")

    def display(self):
        print("You are awarded : "+str(self.awardedPoints) + " points")


if __name__== "__main__":
    booksBought = int(input("Enter the number of Books this Month :"))
    mypoints = Points(booksBought)
    mypoints.display()
