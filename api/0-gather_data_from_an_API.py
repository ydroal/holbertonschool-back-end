#!/usr/bin/python3
'''
Module for a given employee ID, returns information
about his/her todo list progress.
'''
import requests
import sys

if __name__ == '__main__':
    args = sys.argv
    if args[1]:
        employee_id = int(sys.argv[1])

    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')

    users_data = users_response.json()
    todos_data = todos_response.json()

    employee_name = None
    for user in users_data:
        if user['id'] == employee_id:
            employee_name = user['name']
            break

    total_tasks = 0
    done_tasks = []
    for task in todos_data:
        if task['userId'] == employee_id:
            total_tasks += 1
            if task['completed']:
                done_tasks.append(task)

    print(f'Employee {employee_name} is done with tasks'
          f'({len(done_tasks)}/{total_tasks}):')

    for task in done_tasks:
        task_title = task.get('title')
        print(f'\t {task_title}')
