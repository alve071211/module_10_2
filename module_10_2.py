import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        day_counter = 0
        enemy_counter = 100
        print(f'{self.name}, на нас напали!')
        while enemy_counter > 0:
            enemy_counter -= self.power
            time.sleep(1)
            day_counter += 1
            if enemy_counter < 0:
                print(f'{self.name} сражается {day_counter} день(дня), осталось {enemy_counter} воинов')
            else:
                print(f'{self.name} сражается {day_counter} день(дня), осталось {enemy_counter} воинов')

        print(f"{self.name} одержал победу спустя {day_counter} дней(дня)!")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все сражения завершены!')