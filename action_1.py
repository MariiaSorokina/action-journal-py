with open('records', 'r') as journal:
    user_actions_map = {}  # user -> [action1, action2, ...]
    lines = journal.readlines()
    users = []
    actions = []


    # функция принимает аргумент(список с элементами) возвращает список уникальных элементов
    def unique_users(list_name):  # TODO: use hashset (set)
        unique = []
        for user_name in list_name:
            if user_name in unique:
                continue
            else:
                unique.append(user_name)
        return unique

    for line in lines:
        name_and_log = line.split('] ')[1]  # Eve deleted the folder "Important Documents."
        num_of_first_space = name_and_log.find(" ")
        name = name_and_log[0:num_of_first_space]
        users.append(name)

        # TODO вынести на верхний уровень, отрефакторить названия переменных/аргументов
        unique_users_name = unique_users(users)
        actions = name_and_log[num_of_first_space:-2]

        if name in user_actions_map:
            user_actions_map[name].append(actions)
        else:
            user_actions_map[name] = [actions]

    for unique_users_name, action_list in user_actions_map.items():
        formatted_actions = ',\n '.join(action_list)
        print(f"{unique_users_name}: {formatted_actions}")
