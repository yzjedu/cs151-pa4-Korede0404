def find_word(file_list, choice):
    count = 0
    for words in file_list:
        if words.find(choice.lower()) != -1:
            count += 1
    return count

def read_file_to_list(filename):
    try:
        input_file = open(filename, "r")
        data = input_file.readlines()
        input_file.close()
        for i in range(len(data)):
            data[i] = data[i].lower().strip("\n")
        return data
    except FileNotFoundError:
        print("Error Reading File")
        return []

print(read_file_to_list("2014.txt"))


file_name = input("W")
word_choice = input("re")
Variable = read_file_to_list(file_name)
print(find_word(Variable, word_choice))