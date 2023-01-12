# #Exercise 4 without function
# s_km = 10
# t_min = 43
# t_sec = 30

# s_mile = s_km/1.61
# t_hour = t_min/60 + t_sec/3600

# def main():
#     average_time = t_hour/s_mile
#     print(average_time)

#     average_speed = s_mile/t_hour
# if __name__ == "__main__":
#     print(average_speed)
#     pass

#     main()

#Exercise 4 with function

def average_time(t_hour, s_mile):
    hour_per_mile = t_hour/s_mile
    return hour_per_mile

def average_speed(t_hour, s_mile):
    speed_per_hour = s_mile/t_hour
    return speed_per_hour

def exercise4():
    s_km = 10
    t_min = 43
    t_sec = 30

    s_mile = s_km/1.61
    t_hour = t_min/60 + t_sec/3600

    print(average_time(t_hour, s_mile))
    print(average_speed(t_hour, s_mile))

    time = average_time(t_hour, s_mile)
    hour, minute, second = hour_to_hms(time)
    # print(hour_to_hms(time))
    print(f"average time per mile is: {hour:02d}:{minute:02d}:{second:.2f}")

def hour_to_hms(time):
    hour = int(time)
    minute = int((time - hour)*60)
    second = time*3600 - hour*3600 - minute*60
    return hour, minute, second
    
    # print(f"average time per mile is: {hour:02d}:{minute:02d}:{second:02d}")

def main():
    exercise4()
    pass

if __name__ == "__main__":
    main()