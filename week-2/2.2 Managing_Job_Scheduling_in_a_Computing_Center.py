#2.2 Managing Job Scheduling in a Computing Center
from queue import Queue
def calculate_total_time(high_priority_jobs, low_priority_jobs):
    high_priority_queue=Queue()
    low_priority_queue=Queue()
    Total_time=0
    for i in high_priority_jobs.values():
        high_priority_queue.put(i)
    for j in low_priority_jobs.values():
        low_priority_queue.put(j)
    while not high_priority_queue.empty():
        Total_time+=high_priority_queue.get()
    while not low_priority_queue.empty():
        Total_time+=low_priority_queue.get()
    return Total_time
high_priority_jobs = {'Job A': 8, 'Job B': 5, 'Job C': 10,}
low_priority_jobs = {'Job D': 6, 'Job E': 3, 'Job F': 7,}
total_time = calculate_total_time(high_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")
