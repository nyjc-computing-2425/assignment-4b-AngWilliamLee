standardform = input('Enter a number in scientific notation: ')
standardform = standardform.strip()

possible_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', 'x', '.', '-', '^']

if any(chr not in possible_characters for chr in standardform):
  print("Error converting to scientific E notation.")

elif standardform.count('.') > 1:
  print("Error converting to scientific E notation.")

elif standardform.count('^') > 1:
  print("Error converting to scientific E notation.")

elif standardform.count('x') > 1:
  print("Error converting to scientific E notation.")  


else:
  standardform_list = standardform.split('x10^')
  mantissa = standardform_list[0]
  exponent = standardform_list[1]

  if any(char == '.' for char in exponent):
    print("Error converting to scientific E notation.")

  else:

    result = mantissa + 'E' + exponent

    print(f'This number in E notation is {result}.')