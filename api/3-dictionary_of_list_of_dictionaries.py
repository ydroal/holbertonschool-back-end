#!/usr/bin/python3
'''
Module to export query data in the JSON format
'''
import json
import requests
import sys


if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users/'
    res = requests.get(url)
    res_json = res.json()

    dict_employee_name = {}
    for e in res_json:
        dict_employee_name[e['id']] = e['username']

    all_tasks = {}
    for key, value in dict_employee_name.items():
        url_todo = ('https://jsonplaceholder.typicode.com/'
                    f'users/{key}/todos')

        res_todo = requests.get(url_todo)
        res_todo_json = res_todo.json()

        task = []
        for t in res_todo_json:
            v = {
                'username': value,
                'task': t.get('title'),
                'completed': t.get('completed'),
                }
            task.append(v)

        all_tasks[key] = task

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_tasks, f)
