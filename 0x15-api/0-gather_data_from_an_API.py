#!/usr/bin/python3
"""
for each given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId))
    users = user.json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId))
    todos = todo.json()
    tasks_completed = []
    for task in todos:
        if task.get('completed') is True:
            tasks_completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(users.get('name'), len(tasks_completed), len(todos)))
    print("\n".join("\t {}".format(task) for task in tasks_completed))
