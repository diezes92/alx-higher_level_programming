#!/usr/bin/python3
if __name__ == "__main__":
    def print_matrix_integer(matrix=[[]]):
        for i in range(len(matrix)):
            print("")

            for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end=' ')

        print("")
