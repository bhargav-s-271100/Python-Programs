t=int(input("enter the  time"))
def time(min):
    if(min>=60):
        t_hrs=int(min/60)
        t_min=min%60
    else:
        t_hrs=0
        t_min=min
    return t_hrs,t_min
print("time is : (hrs,min)")
print(time(t))

