water = 400
milk = 540
beans = 120
cups = 9
money = 550

def state(water, milk, beans, cups, money):
    print()
    print("The coffee machine has:")
    print(water,"of water")
    print(milk,"of milk")
    print(beans,"of coffee beans")
    print(cups,"of disposable cups")
    print(money,"of money")
    print()
    pass

def buy():
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    def coffee(water_out, milk_out, beans_out, cups_out, money_in):
        global water, milk, beans, money, cups

        if (water - water_out) > 0:
            water -= water_out
        else:
            return print("Sorry, not enough water")
        if (milk - milk_out) > 0:
            milk -= milk_out
        else:
            return ("Sorry, not enough milk")
        if (beans - beans_out) > 0:
            beans -= beans_out
        else:
            return print("Sorry, not enough coffee beans")

        if (cups - cups_out) > 0:
            cups -= cups_out
        else:
            return print("Sorry, not enough cups")

        money += money_in

        return print("I have enough resources, making you a coffee!")


    if coffee_type == "1":
        return coffee(250, 0, 16, 1, 4)
    elif coffee_type == "2":
        return coffee(350, 75, 20, 1, 7)
    elif coffee_type == "3":
        return coffee(200, 100, 12, 1, 6)
    elif coffee_type == "back":
        pass

def fill():
    global water, milk, beans, cups
    water_in = int(input("Write how many ml of water do you want to add:"))
    water += water_in

    milk_in = int(input("Write how many ml of milk do you want to add:"))
    milk += milk_in

    beans_in = int(input("Write how many grams of coffee beans do you want to add:"))
    beans += beans_in

    cups_in = int(input("Write how many disposable cups of coffee do you want to add:"))
    cups += cups_in

    pass


while True:
    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == "buy":
        print()
        buy()
        print()
    elif action == "fill":
        print()
        fill()
        print()
    elif action == "take":
        print()
        print("I gave you $", money)
        money = 0
        print()
    elif action == "remaining":
        state(water, milk, beans, cups, money)
    elif action == "exit":
        break


