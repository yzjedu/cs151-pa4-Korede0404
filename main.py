def read_file_to_list(filename):
    with open(filename, "r") as input_file:
        data = input_file.readlines()
        return data

print(read_file_to_list("2014.txt"))