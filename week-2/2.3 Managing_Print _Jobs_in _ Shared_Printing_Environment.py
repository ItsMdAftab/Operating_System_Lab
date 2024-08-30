#2.3 Managing Print Jobs in a Shared Printing Environment
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
# Driver Code
high_priority_jobs = {'Job A': 15, 'Job B': 10, 'Job C': 20,}
low_priority_jobs = {'Job D': 5, 'Job E': 8, 'Job F': 3,}
total_time = calculate_total_time(high_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all print jobs is: {total_time} units")
