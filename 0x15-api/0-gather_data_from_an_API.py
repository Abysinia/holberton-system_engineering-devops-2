#!/usr/bin/python3
""" using REST API, for a given employee ID,
returns information about his/her TODO list progress """

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

    completed = []
    for task in todos:
        if task["completed"] is True:
            completed.append(task)

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(employee["name"], len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    main()
