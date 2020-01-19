water = 400
milk = 540
beans = 120
cups = 9
money = 550

class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def state(self):
        print()
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print()


    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        if coffee_type == "1":
            if self.water > 250:
                if self.beans > 16:
                    if self.cups > 1:
                        self.water -= 250
                        self.beans -= 16
                        self.cups -= 1
                        self.money += 4
                        print("I have enough resources, making you a coffee!")
                    else:
                        print("Sorry, not enough cups")
                else:
                    print("Sorry, not enough coffee beans")
            else:
                print("Sorry, not enough water")

        elif coffee_type == "2":
            if self.water > 350:
                if self. milk > 75:
                    if self.beans > 20:
                        if self.cups > 1:
                            self.water -= 350
                            self.milk -= 75
                            self.beans -= 20
                            self.cups -= 1
                            self.money += 7
                            print("I have enough resources, making you a coffee!")
                        else:
                            print("Sorry, not enough cups")
                    else:
                        print("Sorry, not enough coffee beans")
                else:
                    print("Sorry, not enough milk")
            else:
                print("Sorry, not enough water")

        elif coffee_type == "3":
            if self.water > 200:
                if self. milk > 100:
                    if self.beans > 12:
                        if self.cups > 1:
                            self.water -= 200
                            self.milk -= 100
                            self.beans -= 12
                            self.cups -= 1
                            self.money += 6
                            print("I have enough resources, making you a coffee!")
                        else:
                            print("Sorry, not enough cups")
                    else:
                        print("Sorry, not enough coffee beans")
                else:
                    print("Sorry, not enough milk")
            else:
                print("Sorry, not enough water")

        elif coffee_type == "back":
            pass

    def fill(self):

        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print(f"I gave you $ {self.money}")
        self.money = 0


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == "buy":
        print()
        coffee_machine.buy()
        print()
    elif action == "fill":
        print()
        coffee_machine.fill()
        print()
    elif action == "take":
        print()
        coffee_machine.take()
        print()
    elif action == "remaining":
        coffee_machine.state()
    elif action == "exit":
        break


