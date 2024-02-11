# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class bankAccount:
    def __init__(self):
        self.name=input("enter your name ")
        self.__nationalid=input("enter your national id")
        self.__phonenumber=int(input("enter your phone number"))
        self.__password=int(input("entrer your password"))
        self._credit=0
    def __checkpasswordF(self):
        accountpass=int(input("enter your password"))
        if accountpass==self.__password:
            return True
        else:
            return False
    def deposit(self):
        amount=int(input("enter your deposit amount"))
        self._credit+=amount
        print("done, balance has been addded ")
    def withdraw(self):
        if self.__checkpasswordF():
            amount=int(input("enter your withdraw amount"))
            if amount<=self._credit:
                self._credit-=amount
                print("done,please take your money")
            else:
                print("you dont have enough money")
        else:
            print("wrong password")
    def checkcredit(self):
       if self.__checkpasswordF():
           print(self._credit)
       else:
           print("wrong password")
    def change_password(self):
       if self.__checkpasswordF():
            newpassword=int(input("enter your new password"))
            self.__password=newpassword
            print("password changed successfully")
       else:
            print("wrong password")
myacc=bankAccount()
myacc.deposit()
# myacc.checkcredit()
# myacc.withdraw()
# myacc.checkcredit()
# myacc.change_password()



class qatarBank(bankAccount):
    def __init__(self):
        print("hala hala")
        super().__init__()
        self.addwallet()

    def addwallet(self):
        self.__walletpassword=int(input("enter your wallet password"))
        self.__walletcredit=0
        print("your wallet has been created")
    def walletdeposit(self):
        amount=int(input("enter your deposit"))
        self.__walletcredit+=amount
        print(f"done you are add {self.__walletcredit}")
    def get_walletcredit(self):
        return self.__walletcredit
    def withdrawWallet(self):
        wpassword=int(input("enter your password"))
        if self.__walletpassword==wpassword:
            amount=int(input("enter your withdraw"))
            if amount<=self.__walletcredit:
                self.__walletcredit-=amount
                print("please take your money ")
            else:
                print("your are poor")
        else:
            print("wrong password")
    def changeWalletPasswprd(self):
        wPassword=int(input("enter your wallet password"))
        if self.__walletpassword==wPassword:
            newWalletPassword=int(input("enter new password"))
            self.__walletpassword=newWalletPassword
        else:
            print("wrong password")
    def tansferCredit2Wallet(self):
        amount=int(input("enter your transfer amount"))
        if amount<=self._credit:
            self.__walletcredit+=amount
            self._credit-=amount
        else:
            print("you dont have enough money in your account")
myacc=bankAccount()
myacc.deposit()
person1=qatarBank()
person1.walletdeposit()
person1.get_walletcredit()
person1.withdrawWallet()
person1.get_walletcredit()
person1.changeWalletPasswprd()
person1.tansferCredit2Wallet()
person1.get_walletcredit()

