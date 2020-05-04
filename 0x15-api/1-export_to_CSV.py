#!/usr/bin/python3
"""
for each given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys
import csv


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId))
    users = user.json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId))
    todos = todo.json()
    with open("{}.csv".format(userId), 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([int(userId), users.get('username'),
                             task.get('completed'),
                             task.get('title')])
