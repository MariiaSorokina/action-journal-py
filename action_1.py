# функция принимает аргумент(список с элементами) возвращает список уникальных элементов
import time

start_time = time.time()

with open('pon.txt', 'r') as journal:
    user_actions_map = {}  # user -> [action1, action2, ...]
    lines = journal.readlines()

    for line in lines:
        name_start = line.find('] ') + 2
        name_end = line.find(' ', name_start)
        name = line[name_start:name_end]
        action = line[name_end + 1:-2]

        if name in user_actions_map:
            user_actions_map[name].append(action)
        else:
            user_actions_map[name] = [action]

    for name, actions in user_actions_map.items():
        print(f'{name}:')
        for i, action in enumerate(actions, 1):
            print(f' {i}. {action}')

end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")