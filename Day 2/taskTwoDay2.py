class Career:
    def __init__(self):
        self.choice = []
        self.questionsList =  ['Mathematics','Biology','Geography','Physics','Computer Studies ','History ','English','Chemistry']
        self.careerList = ['Doctor','Software Developer','Mechanical Engineer','Civil Engineer','Archeology','Lawyer']
        self.answers = []
        self.questions()
        self.careerChoicce()

    def questions(self):
        for number,question in enumerate (self.questionsList) :
            answer = input('Are you good at ' + question + ' ?').lower()

            if answer == 'yes':
               self.answers.append(question)


    def careerChoicce(self):
        try:
            if 'Chemistry' in self.answers and 'Biology' in self.answers:
                self.choice.append(self.careerList[0])
            if 'Mathematics' in self.answers and 'Computer Studies' in self.answers:
                self.choice.append(self.careerList[1])
            if 'Mathematics' in self.answers and 'Physics' in self.answers:
                self.choice.append(self.careerList[2])
            if 'Mathematics' in self.answers and 'Geography' in self.answers:
                self.choice.append(self.careerList[3])
            if 'Geography' in self.answers and 'History' in self.answers:
                self.choice.append(self.careerList[4])
            if 'English' in self.answers and 'History' in self.answers:
                self.choice.append(self.careerList[5])
        except:
            raise Exception("Sorry, could go get a career?")
    def display(self):
        print('Your Preferred Careers are :')
        print(self.choice)




if __name__ == '__main__':
    mycareer = Career()
    mycareer.display()
        