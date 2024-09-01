#1.2 The Software Developer's Tasks
def calculate_total_time(execution_times):
    total_time=0
    for i in execution_times:
        total_time+=i
    return total_time
execution_times = [3, 5, 7, 4] 
total_time = calculate_total_time(execution_times)
 
print(f"The total time required to complete all tasks is: {total_time} hours") 
