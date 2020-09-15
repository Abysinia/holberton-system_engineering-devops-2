#!/usr/bin/python3
""" export data in the JSON format. """

import json
import requests
from sys import argv


def main():

    call_employees = requests.get(
        "https://jsonplaceholder.typicode.com/users")

    employees = call_employees.json()

    all = {}
    for employee in employees:
        call_todos = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".
            format(employee["id"]))
        todos = call_todos.json()

        list_tasks = []
        for task in todos:
            list_tasks.append(
                {"username": employee["username"],
                 "task": task["title"], "completed": task["completed"]
                 })

        all[employee["id"]] = list_tasks

    with open("todo_all_employees.json", 'w',
              newline='', encoding='utf-8') as f:
        json.dump(all, f)


if __name__ == "__main__":
    main()
