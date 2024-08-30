#2.1 Managing System and User Processes\
'''
from queue import Queue
q=Queue()
q.put(1)
q.put(2)
print(q.queue)
'''
from queue import Queue
def calculate_total_time(system_processes, user_processes):
    System_queue=Queue()
    User_queue=Queue()
    Total_time=0
    for i in system_processes.values():
        System_queue.put(i)
    for j in user_processes.values():
        User_queue.put(j)
    while not System_queue.empty():
        Total_time+=System_queue.get()
    while not User_queue.empty():
        Total_time+=User_queue.get()

    return Total_time

system_processes = {'Process A': 5,'Process B': 3,'Process C': 7,}
user_processes = {'Process D': 4, 'Process E': 2, 'Process F': 6,}
total_time = calculate_total_time (system_processes, user_processes)
print(f"The total time required to complete all processes is: {total_time} units")
