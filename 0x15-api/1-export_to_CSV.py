#!/usr/bin/python3
""" using REST API, for a given employee ID,
returns information about his/her TODO list progress """

import csv
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

    name_file = "{}.csv".format(argv[1])
    with open(name_file, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_write.writerow(
                [argv[1], employee['username'],
                 task["completed"], task["title"]])


if __name__ == "__main__":
    main()
