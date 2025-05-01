def number_pyramid(rows):

  for i in range(1, rows + 1):
    # spaces
    print(' ' * (rows - i), end='')
    # numbers in ascending order
    for j in range(1, i + 1):
      print(j, end=' ')
    print()
number_pyramid(5)

