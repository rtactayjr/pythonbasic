number = int(input("Please enter any number: "))


def num_checker(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


print(num_checker(number))
