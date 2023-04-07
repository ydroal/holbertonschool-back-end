#!/usr/bin/python3
'''
Module for a given employee ID, returns information
about his/her todo list progress and exports data in CSV format.
'''
import requests
import sys
import csv

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
    total_tasks = len(res_todo_json)
    done_tasks = [task for task in res_todo_json if task['completed']]

    with open(f'{employee_id}.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in res_todo_json:
            writer.writerow(
                [employee_id, employee_name, str(task['completed']), task['title']]
                )
