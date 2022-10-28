from art import logo

#create functions for each operator

def addition(n1, n2):
  return n1 + n2
  
def subtraction(n1, n2):
  return n1-n2

def multiplication(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2

  
#dictionary of operators
dict_operations = {
  "+" : addition,
  "-" : subtraction,
  "*" : multiplication,
  "/" : division
}
  

def calculator():
  print(logo)
  
  print("\nHello! Welcome to my Basic-Python-Calculator. Please enjoy! \n")
  
  first_number = float(input("Please enter a 1st number: "))

  for ops in dict_operations:
    print("\n"+ ops)

  should_continue = True

  while should_continue:
    operators = input("\nChoose an operator: ")
    
    second_number = float(input("\nPlease enter a 2nd number: "))
    
    calculation_function = dict_operations[operators]
    answer = calculation_function(first_number, second_number)
    
    print(f"\nCalculation is = {first_number} {operators} {second_number} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      first_number = answer
    else:
      should_continue = False
      calculator()

calculator()
