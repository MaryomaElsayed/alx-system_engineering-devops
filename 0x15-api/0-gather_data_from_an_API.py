#!/usr/bin/python3ls

import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(employee_id))

    # Check if the request was successful
    if user_response.status_code != 200:
        print("Error: Unable to fetch employee information. Please check the employee ID.")
        sys.exit(1)

    user = user_response.json()

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params)

    # Check if the request was successful
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list for the employee. Please check the employee ID.")
        sys.exit(1)

    todos = todos_response.json()

    # Filter completed tasks and count them
    completed = [todo.get("title") for todo in todos if todo.get("completed")]

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with indentation
    [print("\t{}".format(task)) for task in completed]
