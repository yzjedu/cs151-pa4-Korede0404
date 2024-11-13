def read_file_to_list(filename):
    data = []
    try:
        input_file = open(filename, "r")
        data = input_file.readlines()
    except FileNotFoundError:
        print("Error: File Does Not Exist")
    return data

print(read_file_to_list("2014.txt"))