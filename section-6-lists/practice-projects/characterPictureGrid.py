grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


''' No. of rows is basically total items in the list. '''
numberOfRows = len(grid)


''' No. of columns, is number of items in the each row,
those are equal in all sublists. '''
numberOfColumns = len(grid[0])

''' For colum index 0(for first column), inner loop will print
all the characters in the row 1, and so on. '''
for col in range(numberOfColumns):
    for row in range(numberOfRows):
        print(grid[row][col], end=' ')

    # Print newline after each iteration
    print()
