
# print 2D matrix 
def print_matrix(mat):
    for row in mat:
        print(row)

# Convert row string to 2D matrix
def parse_matrix(text):
    mat = []
    # string_rows = text.split('\n')
    for string_row in text:
        int_row = list(map(int, string_row.split()))
        mat.append(int_row)
    return mat

# Read command line input and convert to a 2D matrix
def read_matrix(number_of_rows):
    text = []
    for i in range(number_of_rows):
        row_input = input()
        text.append(row_input)
    return parse_matrix(text)

# Matrix addition
def matrix_add(mat1, mat2):
    mat = []
    no_of_rows = len(mat1)
    no_of_cols = len(mat1[0])
    for r in range(no_of_rows):
        row = []
        for c in range(no_of_cols):
            row.append(mat1[r][c] + mat2[r][c])
        mat.append(row)
    return mat

# Matrix multiplication
def matrix_add(mat1, mat2):
    mat = []
    return mat


mat1 = read_matrix(3)
mat2 = read_matrix(3)

mat_sum = matrix_add(mat1, mat2)
print_matrix(mat_sum)

"""
1 2 3
4 5 6
7 8 9

-2 2 3
4 5 -5
7 0 9
"""