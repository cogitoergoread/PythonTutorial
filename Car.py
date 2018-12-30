""""
Tutorial: https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html
"""
class Car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("Sebességem {} km/h.".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time > 0:
            return self.odometer / self.time
        else:
            return 0


if __name__ == '__main__':
    my_car = Car()
    print ("Kész az autó!")
    while True:
        action = input("Mit tegyünk? [A]ccelerate, [B]rake, show [O]dometer, show average [S]peed?").upper()
        if action not in ('ABOS'):
            print("Nem sikerült... [ABOS]!")
            continue

        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'S':
            print ("Az átlagsebesség {} km/h.".format(my_car.average_speed()))
        elif action == 'O':
            print("A megtett út {} km.".format(my_car.odometer))

        my_car.step()
        my_car.say_state()