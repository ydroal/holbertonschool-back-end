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

    res = requests.get(
        'https://jsonplaceholder.typicode.com/users',
        params={'id': employee_id}
        )
    res_json = res.json()
    employee_name = res_json[0].get('name')

    res_todo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        )
    res_todo_json = res_todo.json()
    total_tasks = len(res_todo_json)
    done_tasks = [task for task in res_todo_json if task['completed']]

    print(f'Employee {employee_name} is done with tasks'
          f'({len(done_tasks)}/{total_tasks})')

    for task in done_tasks:
        task_title = task.get('title')
        print(f'\t {task_title}')