def name_list():
    user_input = input("Type \"quit\" to leave. Enter a name: ")
    dict_of_names = {}
    while user_input != "quit":
        if len(user_input) not in dict_of_names.keys():
            dict_of_names[len(user_input)] = []
            dict_of_names[len(user_input)].append(user_input)
        else:
            dict_of_names[len(user_input)].append(user_input)
        user_input = input("Type \"quit\" to leave. Enter a name: ")
    return sorted(dict_of_names.items())