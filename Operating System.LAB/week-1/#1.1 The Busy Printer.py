#1.1 The Busy Printer
def Claculate_Total_Time(arrival_time,pages):
    curren_ttime=0
    total_time=0
    for i in range(len(arrival_time)):
        current_time=pages[i]
        total_time+=current_time
    return total_time
arrival_time=list(map(int,input().split(',')))
pages=list(map(int,input().split(',')))
total_time=Claculate_Total_Time(arrival_time,pages)
print(total_time)

