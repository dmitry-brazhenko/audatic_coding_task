def convert_input_to_array(value, length):
    output = "{0:b}".format(value)
    output = "0" * (length - len(output)) + output
    output = list(map(int, output))
    return list(output)


def convert_input_to_index(value, length):
    output = "{0:b}".format(value)[::-1]
    if output.count("1") != 1:
        return None
    return length - output.index("1") - 1


def check_matrix(values, matrix_size):
    columns_with_ones = [0] * matrix_size
    for value in values:
        converted_val = convert_input_to_index(value, matrix_size)
        if converted_val is None:
            return False
        if columns_with_ones[converted_val] == 1:
            return False
        columns_with_ones[converted_val] = 1
    return True


def main():
    N = int(input())
    for test_case in range(N):
        M = int(input())
        elems_product = None
        matrix_is_permutable = True
        seen_columns = set()
        for matrix_row in range(M):
            if matrix_is_permutable:
                value = int(input())
                col_index = convert_input_to_index(value, M)
            else:
                input()

            if col_index is None:
                matrix_is_permutable = False

            if matrix_is_permutable:
                if col_index not in seen_columns:
                    seen_columns.add(col_index)
                else:
                    matrix_is_permutable = False
            #     if elems_product is None:
            #         elems_product = col_index
            #     else:
            #         elems_product = elems_product ^ col_index
            #
            # if matrix_is_permutable and matrix_row > 2 and elems_product == 0:
            #     matrix_is_permutable = False

        if matrix_is_permutable:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    main()
