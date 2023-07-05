 #функция принимает аргумент(список с элементами) возвращает список уникальных элементов
def unique_users(list_name):
    unique = set()
    for user_name in list_name:
        unique.add(user_name)
    return list(unique)


with open('records', 'r') as journal:
    user_actions_map = {}  # user -> [action1, action2, ...]
    lines = journal.readlines()
    users = []
    actions = []

    for line in lines:
        name_and_log = line.split('] ')
        num_of_first_space = name_and_log[1].find(' ')
        name = name_and_log[1][:num_of_first_space]
        users.append(name)
        act = name_and_log[1][num_of_first_space + 1:-2]
        actions.append(act)

    unique_users_name = unique_users(users)

    for name in user_actions_map:
        user_actions_map[name].append(act)
    else:
        user_actions_map[name] = [act]

for unique_user_name in unique_users_name:
    action_list = user_actions_map.get(unique_user_name, [])
    formatted_actions = ',\n '.join(action_list)
    print(f"{unique_user_name}: {formatted_actions}")