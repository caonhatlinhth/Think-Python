import copy
from datetime import datetime


class Time(object):
    """Represents the time of day
    attributes: hour, minute, second
    """
time = Time()
time.hour = 11
time.minute = 50
time.second = 30

time1 = Time()
time1.hour = 10
time1.minute = 20
time1.second = 30
time2 = Time()
time2.hour = 11
time2.minute = 10
time2.second = 20

def print_time():
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

def compare_two_time():
    time1_format = "%.2d:%.2d:%.2d" % (time1.hour, time1.minute, time1.second)
    time2_format = "%.2d:%.2d:%.2d" % (time2.hour, time2.minute, time2.second)
    # print("%.2d:%.2d:%.2d" % (time1.hour, time1.minute, time1.second) > "%.2d:%.2d:%.2d" % (time2.hour, time2.minute, time2.second))
    print(time1_format > time2_format)


def correct_version_of_increasement(time, second):
    increase_second = time.second + second
    increase_minute = time.minute + increase_second/60
    time.hour += increase_minute/60
    time.minute = increase_minute%60
    time.second = increase_second%60
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

def pure_version_of_increasement(time, second):
    increase_time = copy.copy(time)
    correct_version_of_increasement(increase_time, second)
    return increase_time

def time_to_int(time):
    minute = time.hour*60 + time.minute
    second = minute*60 + time.second
    return second

def int_to_time(second):
    time = Time()
    minute, time.second = divmod(second, 60)
    time.hour, time.minute = divmod(minute, 60)
    print ("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

def rewrite_increment(time, increase_second):
    minute = time.hour*60 + time.minute
    old_second = minute*60 + time.second
    new_second = old_second + increase_second
    new_minute, time.second = divmod(new_second, 60)
    time.hour, time.minute = divmod(new_minute, 60)
    print ("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

def mul_time(time, number):
    minute = time.hour*60 + time.minute
    old_second = minute*60 + time.second
    new_second = old_second * number
    new_minute, time.second = divmod(new_second, 60)
    time.hour, time.minute = divmod(new_minute, 60)
    new_time = "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)
    return new_time

def time_and_distance_in_a_race(time, distance):
    time_per_distance = mul_time(time, 1/distance)
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

def today_vs_weekday():
    # now = datetime.datetime.now()
    # weekday = now.weekday()
    print(datetime.now().strftime("%A, %B %d %Y, %H:%M:%S"))
    # print(now,weekday)
    
def birthday_count():
    birthday = datetime(1998, 10, 16)
    today = datetime.now()
    age = today.year - 1998 - ((today.month, today.day) < (10, 16))
    my_birthday = birthday.replace(year = today.year)
    if my_birthday < today:
        my_birthday = birthday.replace(year = today.year + 1)
    time_to_birthday = abs(my_birthday - today)
    time_to_birthday.days
    print(age, time_to_birthday)
    
def find_double_day():
    start_date = datetime(1970,1,1)
    date_1 = datetime(1998, 1, 19) - start_date
    date_2 = datetime(1998,10,16) - start_date
    date_3 = 2*date_2 - date_1
    date_4 = start_date + date_3
    double_day = date_4.ctime()
    print(double_day)

def find_n_time_day(n):
    start_date = datetime(1970,1,1)
    birthday_1 = datetime(1998, 1, 19)
    birthday_2 = datetime(1998,10,16)
    date_1 = birthday_1 - start_date
    date_2 = birthday_2 - start_date
    date_3 = (n*date_2 - date_1)/(n-1)
    date_4 = start_date + date_3
    n_time_day = date_4.ctime()
    print(n_time_day)

def main():
    find_n_time_day(5)
    # birthday_count()
    # today_vs_weekday()      
    # print_time()
    # compare_two_time()
    # correct_version_of_increasement(time, 50)
    # print(pure_version_of_increasement(time, 50))
    # print(time_to_int(time))
    # int_to_time(50280)
    # rewrite_increment(time, 8400)
    # time_and_distance_in_a_race(time, 5)
    # time_and_distance_in_a_race(time, 5)
    pass

if __name__ == "__main__":
    main()