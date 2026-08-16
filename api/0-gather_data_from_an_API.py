#!/usr/bin/python3
"""Module that gathers data from a REST API for a given employee ID.

Displays the TODO list progress of an employee.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
