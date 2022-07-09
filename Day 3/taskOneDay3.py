from datetime import  datetime

class Door:
    def __init__(self,newPassword):
        self.password =newPassword
        self.opened = None
        self.closed = None
        self.lastOpened = None

    def loginUser(self):
        password = input('Enter your Password to LogIn : ')

        if self.password == password:
            print('Logged in Successfully')
            self.commands()
        else:
            print('Wrong Password ')
            self.loginUser()


    def commands(self):
        command = input('Enter Command : ')
        if command.lower() == 'open' and not self.opened == True:
            print('Door Last open  at '+str(self.lastOpened))
            self.opened = True
            self.closed = False
            print('The door is now open')
            self.lastOpened = datetime.today()
            self.commands()
        elif command.lower() == 'open' and self.opened == True:
            print('Door Last open  at ' + str(self.lastOpened))
            print('The door is already open')
            self.commands()
        elif command.lower() == 'close' and not self.closed == True:
            print('Door Last open  at '  +str(self.lastOpened))
            self.closed = True
            self.opened = False
            print('The door is now locked')
            self.commands()
        elif command.lower() == 'close' and self.closed == True:
            print('Door Last open  at ' +str(self.lastOpened))
            print('The door is already locked')
            self.commands()
        elif command.lower() == 'quit':
            return 0
            print('Process Terminated')
        else:
            print('Invalid input')
            self.commands()

if __name__=='__main__':
    newPassword = input('Create New Password :')
    print(newPassword)
    mydoor = Door(newPassword)
    mydoor.loginUser()
