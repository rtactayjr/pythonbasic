from art import logo


print(logo)
print("\nHello! Welcome to my Basic-Python-Calculator. Please enjoy! \n")


#create functions for each operator

def addition(n1, n2):
  return n1 + n2

  
def subtraction(n1, n2):
  return n1-n2

  
def multiplication(n1, n2):
  return n1 * n2

  
def division(n1, n2):
  return n1 / n2


first_number = float(input("Please enter a 1st number: "))

dict_operations = {
  "+" : addition,
  "-" : subtraction,
  "*" : multiplication,
  "/" : division
}
for ops in dict_operations:
  print("\n"+ ops)
operators = input("\nChoose an operator: ")

second_number = float(input("\nPlease enter a 2nd number: "))

calculation_function = dict_operations[operators]
answer = calculation_function(first_number, second_number)

print(f"\nCalculation is = {first_number} {operators} {second_number} = {answer}")

