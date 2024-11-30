def get_length(sequence):
    count = 0
    for a in sequence:
        count += 1
    return count

def sort_row_descending(row):
    row_length = get_length(row)
    i = 1
    while i < row_length:
        key = row[i]
        j = i - 1
        while j >= 0 and row[j] < key:
            row[j + 1] = row[j]
            j -= 1
        row[j + 1] = key
        i += 1
    return row

def calculate_fi(matrix):
    num_rows = get_length(matrix)
    num_cols = get_length(matrix[0])
    fi_values = []

    j = 0
    while j < num_cols:
        sum_elements = 0
        count = 0
        i = 0
        while i < j:
            sum_elements += matrix[i][j]
            count += 1
            i += 1
        if count > 0:
            fi_values.append(sum_elements / count)
        else:
            fi_values.append(0)
        j += 1

    return fi_values

def calculate_F(fi_values):
    product = 1
    for fi in fi_values:
        product *= fi
    return product

def main():
    matrix = [
        [12, 46, -23, 72, -5],
        [59, 7, -8, 0, 67],
        [7, -8, -4, -97, -55],
        [77, -1, -5, 34, -8],
        [0, 22, 27, 24, 24]
    ]

    sorted_matrix = []
    for row in matrix:
        sorted_matrix.append(sort_row_descending(row))

    fi_values = calculate_fi(sorted_matrix)
    F_value = calculate_F(fi_values)

    print("Sorted Matrix:")
    for row in sorted_matrix:
        print(row)

    print("\nfi(aij) values:")
    print(fi_values)

    print("\nF(fi(aij)) value:")
    print(F_value)

main()
