#!/usr/bin/python3
"""Module that gathers data from a REST API for a given employee ID.

Exports the employee's TODO list data to a CSV file.
"""
import csv
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

    username = user.get("username")

    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
