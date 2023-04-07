#!/usr/bin/python3
'''
Module to export query data in the JSON format
'''
import json
import requests
import sys


if __name__ == '__main__':
    args = sys.argv
    if args[1]:
        employee_id = int(sys.argv[1])
    else:
        employee_id = None
        exit()

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    res = requests.get(url)
    res_json = res.json()
    employee_name = res_json.get('username')

    url_todo = ('https://jsonplaceholder.typicode.com/'
                f'users/{employee_id}/todos')

    res_todo = requests.get(url_todo)
    res_todo_json = res_todo.json()

    task = []
    for t in res_todo_json:
        v = {
            'task': t.get('title'),
            'completed': t.get('completed'),
            'username': employee_name,
            }
        task.append(v)

    formatted_data = {str(employee_id): task}

    with open(f'{employee_id}.json', mode='w') as f:
        json.dump(formatted_data, f)
