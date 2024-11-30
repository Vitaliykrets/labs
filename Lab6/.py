class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def get_length(sequence):
        count = 0
        for a in sequence:
            count += 1
        return count

    @staticmethod
    def sort_row_descending(row):
        row_length = Matrix.get_length(row)
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

    @staticmethod
    def sorting_decorator(func):
        def wrapper(instance, *args, **kwargs):
            sorted_matrix = []
            for row in instance.matrix:
                sorted_row = Matrix.sort_row_descending(row)
                sorted_matrix.append(sorted_row)
            instance.matrix = sorted_matrix
            return func(instance, *args, **kwargs)
        return wrapper

    @sorting_decorator
    def sort_matrix(self):
        return self.matrix

    def calculate_fi(self):
        num_rows = self.get_length(self.matrix)
        num_cols = self.get_length(self.matrix[0])
        fi_values = []

        j = 0
        while j < num_cols:
            sum_elements = 0
            count = 0
            i = 0
            while i < j:
                sum_elements += self.matrix[i][j]
                count += 1
                i += 1
            if count > 0:
                fi_values.append(sum_elements / count)
            else:
                fi_values.append(0)
            j += 1

        return fi_values

    @staticmethod
    def calculate_F(fi_values):
        product = 1
        for fi in fi_values:
            product *= fi
        return product

    def __add__(self, other):
        result_matrix = []
        num_rows = self.get_length(self.matrix)
        num_cols = self.get_length(self.matrix[0])

        i = 0
        while i < num_rows:
            row_result = []
            j = 0
            while j < num_cols:
                row_result.append(self.matrix[i][j] + other.matrix[i][j])
                j += 1
            result_matrix.append(row_result)
            i += 1

        return Matrix(result_matrix)

    def __str__(self):
        result = []
        for row in self.matrix:
            row_str = ''
            for element in row:
                row_str += str(element) + ' '
            result.append(row_str.strip()) 
        return '\n'.join(result)


def main():
    matrix1 = Matrix([[1, 3, 4], 
                      [5, 6, 9], 
                      [2, 8, 7]])
    
    matrix2 = Matrix([[4, 2, 3],
                      [8, 5, 6],
                      [7, 7, 4]])

    print("Initial Matrix 1:")
    for row in matrix1.matrix:
        print(row)

    sorted_matrix = matrix1.sort_matrix()
    print("\nSorted Matrix 1:")
    for row in sorted_matrix:
        print(row)

    fi_values = matrix1.calculate_fi()
    print("\nfi(aij) values:")
    print(fi_values)

    F_value = Matrix.calculate_F(fi_values)
    print("\nF(fi(aij)) value:")
    print(F_value)

    sum_matrix = matrix1 + matrix2
    print("\nSum of Matrix 1 and Matrix 2:")
    print(sum_matrix)

if __name__ == "__main__":
    main()
