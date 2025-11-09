import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occurred: {err}")

    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("Tell your pin (4 digits): ")),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, you cannot create your account")
        else:
            print("Account created successfully!")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please note down your bank number")

            Bank.data.append(info)
            Bank.update()

    def depositmoney(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin as well: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no data found")
        else:
            amount = int(input("How much do you want to deposit: "))
            if amount > 10000 or amount <= 0:
                print("Sorry, the amount must be between 1 and 10,000")
            else:
                userdata[0]['balance'] += amount
                Bank.update()
                print("Amount deposited successfully!")

    def withdrawtmoney(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin as well: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no data found")
        else:
            amount = int(input("How much do you want to withdraw: "))
            if userdata[0]['balance'] < amount:
                print("Sorry, you don't have sufficient balance.")
            else:
                userdata[0]['balance'] -= amount
                Bank.update()
                print("Amount withdrawn successfully!")

    def showdetails(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin as well: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no data found")
        else:
            print('Your information:')
            for i in userdata[0]:
                print(f"{i}: {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin as well: "))
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if not userdata:
            print("No user found")
        else:
            print("You cannot change age, account number, or balance.")
            print("Fill the details for change or leave empty.")

            newdata = {
                "name": input("Please tell your new name or press Enter to skip: "),
                "email": input("Please tell your new email or press Enter to skip: "),
                "pin": input("Enter new pin or press Enter to skip: ")
            }

            # Keep old values if left blank
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            else:
                newdata["pin"] = int(newdata["pin"])

            # Retain unchanged fields
            newdata['age'] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']

            # Update record
            for key in newdata:
                userdata[0][key] = newdata[key]

            Bank.update()
            print("Details updated successfully!")
    def deleteaccount(self):
        accnumber = input("Enter your account number to delete: ")
        pin = int(input("Enter your PIN: "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        Bank.data.remove(i)
        Bank.update()
        print("Account deleted successfully.")
        return
        print(" Account not found or PIN incorrect.")




user = Bank()

print("Press 1 for creating an account")
print("Press 2 for depositing money in the bank")
print("Press 3 for withdrawing money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting your account")

check = int(input("Tell your response: "))

if check == 1:
    user.Createaccount()
elif check == 2:
    user.depositmoney()
elif check == 3:
    user.withdrawtmoney()
elif check == 4:
    user.showdetails()
elif check == 5:
    user.updatedetails()
elif check==6:
    user.deleteaccount()


