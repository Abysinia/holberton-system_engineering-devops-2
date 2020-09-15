#!/usr/bin/python3
""" export data in the JSON format. """

import json
import requests
from sys import argv


def main():

    if len(argv) != 2:
        return

    call_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))

    employee = call_employee.json()

    call_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1]))
    todos = call_todos.json()

    list_tasks = []
    for task in todos:
        list_tasks.append(
            {"task": task["title"], "completed": task["completed"],
             "username": employee["username"]})

    name_file = "{}.json".format(argv[1])
    with open(name_file, 'w', newline='', encoding='utf-8') as f:
        json.dump({employee["id"]: list_tasks}, f)


if __name__ == "__main__":
    main()
