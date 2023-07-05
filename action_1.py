# функция принимает аргумент(список с элементами) возвращает список уникальных элементов
import time

def unique_users(list_name):
    unique = set()
    for user_name in list_name:
        unique.add(user_name)
    return list(unique)

start_time = time.time()

with open('pon.txt', 'r') as journal:
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

        if name in user_actions_map:
            user_actions_map[name].append(act)
        else:
            user_actions_map[name] = [act]

    unique_users_name = unique_users(users)

    for user_name in unique_users_name:
        action_list = user_actions_map.get(user_name, [])
        formatted_actions = ""
        for i, action in enumerate(action_list, start=1):
            if i == 1:
                formatted_actions += f" {i}. {action}\n"
            else:
                formatted_actions += f" {i}. {action}\n"
        print(f"{user_name}:\n{formatted_actions}")

end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")