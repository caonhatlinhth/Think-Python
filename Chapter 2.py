# import math

def exercise2a():
    r = 5
    volume_sphere = 4/3*math.pi*r**3
    print (volume_sphere)

def exercise2b(copy):
    cover_price = 24.95
    shipping_first = 3
    shipping_add = 0.75
    discount = 0.4
    wholesale = copy*cover_price*(1-discount) + shipping_first + shipping_add*(copy-1)
    print(wholesale)

#Exercise 2c

def hms_to_s(hour, minute, second):
    total_second = hour * 3600 + minute * 60 + second
    return total_second

def s_to_hms(total_second):
    hour = int(total_second/3600)
    minute = int((total_second -hour*3600)/60)
    second = total_second - hour*3600 - minute*60
    return hour, minute, second

def exercise2c():
    easy_pace = hms_to_s(0,8,15)
    tempo_pace = hms_to_s(0,7,12)
    leave_house_time = hms_to_s(6,52,0)

    final_time = leave_house_time + 2*easy_pace + 3*tempo_pace
    hour, minute, second = s_to_hms(final_time)

    print(f"Time I get home for breakfast is: {hour:02d}:{minute:02d}:{second:02d}")

def main():
    # exercise2a()
    # exercise2b(80)
    exercise2c()

    pass

if __name__ == "__main__":
    main()