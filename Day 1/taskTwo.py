class Charge:
    def __init__(self, wallSize, amtPerGallon):
        self.paintGallons = None
        self.labourHours = None
        self.costPaint = None
        self.labourCharge = None
        self.totalCost = None
        self.calculate(wallSize, amtPerGallon)

    def calculate(self, wallSize, amtPerGallon):
        self.paintGallons = ((wallSize * 1) / 115)
        self.labourHours = ((wallSize * 8) / 115)
        self.labourCharge = self.labourHours * 20
        self.costPaint = (self.paintGallons * amtPerGallon)
        self.totalCost = self.costPaint + self.labourCharge

    def display(self):
        print("Number of Gallons : " + str(self.paintGallons))
        print("Hours of Labour : " + str(self.labourHours))
        print("Cost of Paint : " + str(self.costPaint))
        print("Labour Charges : " + str(self.labourCharge))
        print("Total Cost : " + str(self.totalCost))


if __name__ == '__main__':
    wallSIze = int(input("Enter the wall size : "))
    amtPerGallon = int(input("Enter the amount of paint per Gallon: "))
    project1 = Charge(wallSIze, amtPerGallon)
    project1.display()
