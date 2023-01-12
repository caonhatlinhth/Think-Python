
#exercise 1
class Time(object):
    def time_to_int(time):
        minute = time.hour*60 + time.minute
        second = minute*60 + time.second
        return second
    def print_time(time):
        print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))
    
time = Time()
time.hour = 11
time.minute = 50
time.second = 30

#exercise 2
class Point(object):
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        return'(%g, %g)' % (self.x, self.y)

    # def __add__(self, increase):
    #     increase_point = Point()
    #     increase_point.x += self.x + increase.x
    #     increase_point.y += self.y + increase.y
    #     return increase_point.print_point()

    def __add__(self, increase):
        increase_point = Point()
        if isinstance(increase, Time):
            increase_point.x += self.x + increase.x
            increase_point.y += self.y + increase.y
        elif type(increase) == tuple:
            increase_point.x += self.x + increase[0]
            increase_point.y += self.y + increase[1]
        return increase_point.print_point()

    def __radd__(self, increase):
        return self.__add__(increase)

point = Point(9,10)
increase = (2,3)

class Kangaroo(object):
    def __init__(self):
        self.pouch_content = []
    
    def put_in_pouch(self, thing):
        self.pouch_content.append(thing)
    def __str__(self):
        return "I have {} in my pouch".format(self.pouch_contents)

def main():
    
    # print(time.time_to_int())
    # time.print_time()
    # point.print_point()
    # print(point)
    # print(time.time_to_int())
    pass

if __name__ == '__main__':
    main()