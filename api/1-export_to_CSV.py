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

    res = requests.get(
        'https://jsonplaceholder.typicode.com/users',
        params={'id': employee_id}
        )
    res_json = res.json()
    employee_name = res_json[0].get('username')

    res_todo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        )
    res_todo_json = res_todo.json()
    total_tasks = len(res_todo_json)
    done_tasks = [task for task in res_todo_json if task['completed']]

    # Export data to CSV
    with open(f'{employee_id}.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in res_todo_json:
            writer.writerow(
                [employee_id, employee_name, task['completed'], task['title']]
                )
