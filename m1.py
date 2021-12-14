def convert_input_to_array(value, length):
    output = "{0:b}".format(value)
    output = "0" * (length-len(output)) + output
    output = list(map(int, output))
    return list(output)

def check_matrix(values, matrix_size):
    columns_with_ones = set()
    for value in values:
        converted_val = convert_input_to_array(value, matrix_size)
        if sum(converted_val) != 1:
            return False
        one_column_val = converted_val.index(1)
        if one_column_val in columns_with_ones:
            return False
        columns_with_ones.add(one_column_val)
    return True

def main():
    N = int(input())
    for test_case in range(N):
        M = int(input())
        matrix_rows = []
        for matrix_row in range(M):
            value = int(input())
            matrix_rows.append(value)
        if check_matrix(matrix_rows, M):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()
