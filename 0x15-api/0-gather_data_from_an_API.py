#!/usr/bin/python3
"""
Queries information from the JSON placeholder API.
Returns the information about an employee's TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + "users/{}".format(sys.argv[1])
    todo_url = url + "todos"
    params = {"userId": sys.argv[1]}
    user = requests.get(url=user_url).json()
    todos = requests.get(url=todo_url, params=params).json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
