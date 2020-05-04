#!/usr/bin/python3
"""
for each given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys
import json


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId))
    users = user.json()
    username = users.get('username')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId))
    todos = todo.json()
    user_obj = {}
    task_list = []
    for task in todos:
        new_dict = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username}
        task_list.append(new_dict)
    user_obj[userId] = task_list
    with open('{}.json'.format(userId), mode='w') as f:
        json.dump(user_obj, f)
