from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

logo = """
(
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
     \""--..__                              __..--""/
       '._     ""______"" ------_.'......__^^^
          `""--..,,_____            _____,,..--""`
                        `""_____""`.."""

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    print(logo)
    options = menu.get_items()
    print("type 'off' to exit the program or type 'report' to show remaining resources.")
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
