import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    with open(file_path,"rb") as file:
        return pickle.load(file)


if __name__ == "__main__":
    my_dict = {1:"a",2:"b",3:"c"}
    my_file="example_file.txt"

    save_dict(my_dict, my_file)

    actual_result = load_dict(my_file)

    print(actual_result)

    assert actual_result == my_dict

