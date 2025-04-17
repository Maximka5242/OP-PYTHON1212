from random import *


class Student:

    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -=5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):

        if self.progress< -0.5:
            print("Cast out...")
            self.alive = False

        elif self.gladness < 0:
            print("Depression...")
            self.alive = False

        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self,day):

        print("/n")
        print()
        print("-" * 20)
        print(f"Num of day: {day}")
        print(f"Num of day : {self.progress}")
        print(f"Progress: {self.gladness}")
        print("-" * 20)
        print()

    def live(self,day):

        live_cube = randint(1, 3)

        if live_cube ==1:
            self.to_study()

        elif live_cube ==2:
            self.to_sleep()


        elif live_cube ==3:
            self.to_chill()

        self.end_of_day(day)
        self.is_alive()







student_Nazar = Student("Nazar ")

for day in range(1,365):

    if student_Nazar == False:
        break

    student_Nazar.live(day)

