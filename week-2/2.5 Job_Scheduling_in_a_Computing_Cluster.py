#2.5 Job Scheduling in a Computing Cluster
from queue import Queue
def calculate_total_time(high_priority_jobs, medium_priority_jobs, 
low_priority_jobs):
    high_priority_queue=Queue()
    medium_priority_queue=Queue()
    low_priority_queue=Queue()
    total_time=0
    for i in high_priority_jobs.values():
        high_priority_queue.put(i)
    for j in medium_priority_jobs.values():
        medium_priority_queue.put(j)
    for j in low_priority_jobs.values():
        low_priority_queue.put(j)
    while not high_priority_queue.empty():
        total_time+=high_priority_queue.get()
    while not medium_priority_queue.empty():
        total_time+=medium_priority_queue.get()
    while not low_priority_queue.empty():
        total_time+=low_priority_queue.get()
    return total_time
high_priority_jobs = {'Job A': 20, 'Job B': 15, 'Job C': 25,}
medium_priority_jobs = {'Job D': 10, 'Job E': 12, 'Job F': 8,}
low_priority_jobs = {'Job G': 5, 'Job H': 4, 'Job I': 6,}
total_time = calculate_total_time(high_priority_jobs, medium_priority_jobs, 
low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")
