#2.4 Task Scheduling in a Multi-User System
from queue import Queue
def calculate_total_time(high_priority_tasks, low_priority_tasks):
    high_priority_queue=Queue()
    low_priority_queue=Queue()
    total_time=0
    for i in high_priority_tasks.values():
        high_priority_queue.put(i)
    for j in low_priority_tasks.values():
        low_priority_queue.put(j)
    while not high_priority_queue.empty():
        total_time+=high_priority_queue.get()
    while not low_priority_queue.empty():
        total_time+=low_priority_queue.get()
    return total_time
high_priority_tasks = {'Task A': 12, 'Task B': 8, 'Task C': 15,}
low_priority_tasks = {'Task D': 6, 'Task E': 4, 'Task F': 10, }
total_time = calculate_total_time(high_priority_tasks, low_priority_tasks)
print(f"The total time required to complete all tasks is: {total_time} units")
