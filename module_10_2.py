import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        day_counter = 1
        enemy_counter = 100 - self.power

        while enemy_counter > 1:
            print(f'{self.name} сражается {day_counter} день(дня), осталось {enemy_counter} воинов \n{self.name}'
                  f' одержал победу {day_counter} день(дня) спустя')
            day_counter += 1
            enemy_counter -= self.power
            time.sleep(1)
        if enemy_counter < 0:
            print(f'{self.name} сражается {day_counter} день(дня), осталось 0 воинов')
        else:
            print(f'{self.name} сражается {day_counter} день(дня), осталось {enemy_counter} воинов')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все сражения завершены!')