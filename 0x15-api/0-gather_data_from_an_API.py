#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

def fetch_employee_todo_list(employee_id):
    """
    Fetches employee information and their corresponding TODO list from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee whose TODO list should be fetched.

    Returns:
        None

    Raises:
        requests.HTTPError: If there is an error while fetching data from the API.
    """
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get the employee information using the provided employee ID
    user_response = requests.get(url + "users/{}".format(employee_id))
    user_response.raise_for_status()  # Raise an exception for HTTP errors

    user = user_response.json()

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params)
    todos_response.raise_for_status()  # Raise an exception for HTTP errors

    todos = todos_response.json()

    # Filter completed tasks and count them
    completed = [todo.get("title") for todo in todos if todo.get("completed")]

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks ({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with indentation
    [print("\t{}".format(task)) for task in completed]

if __name__ == "__main__":
    fetch_employee_todo_list(int(sys.argv[1]))

