import concurrent.futures
import random
import numpy as np
from collections import Counter
import threading
import time
import random

"""
In this exercise I was cooperating with Jakub Guza
"""

def CalculateHistogram(count=100):

    coin_throws = np.zeros(count, dtype=int)

    for index in range(count):
        coin_throws[index] = random.randint(1, 2) + random.randint(1, 2)

    counts = Counter(coin_throws)
    print(counts['a'])

    histogram = {"heads": counts[2], "heads and tails": counts[3], "tails": counts[4]}

    return histogram

def main_histogram():

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread:
        th = thread.submit(CalculateHistogram, 200_000)

    histogram = th.result()
    print(f"{histogram}")


class Philosopher(threading.Thread):

    def __init__(self, philosopher, first, second, deadlock):
        super().__init__()
        self.philosopher = philosopher
        self.first_fork = first
        self.second_fork = second
        self.without_deadlock = deadlock

    def Eating(self):

            first_fork_num = self.philosopher
            second_fork_num = (self.philosopher + 1) % 5

            if self.without_deadlock:
                if self.philosopher % 2 == 0:
                    temp = self.first_fork
                    self.first_fork = self.second_fork
                    self.second_fork = temp
                    first_fork_num = (self.philosopher + 1) % 5
                    second_fork_num = self.philosopher

            time.sleep(random.randint(1, 5))
            self.first_fork.acquire()
            print(f"Philosopher {self.philosopher} acquired fork {first_fork_num} \n")

            time.sleep(random.randint(1, 5))
            self.second_fork.acquire()
            print(f"Philosopher {self.philosopher} acquired fork {second_fork_num} \n")

            time.sleep(2)
            print(f"Philosopher {self.philosopher} is eating...\n")

            self.first_fork.release()
            print(f"Philosopher {self.philosopher} released fork {first_fork_num} \n")
            self.second_fork.release()
            print(f"Philosopher {self.philosopher} released fork {second_fork_num} \n")


    def run(self):
        while True:
            print(f"Philosopher {self.philosopher} is thinking\n")
            time.sleep(random.randint(1, 5))
            self.Eating()


def main_philosophers():
    without_deadlock = True

    forks = [threading.Condition(threading.Lock()) for _ in range(5)]
    philosophers = [Philosopher(id, forks[id], forks[(id + 1) % 5], without_deadlock) for id in range(5)]

    for philo in philosophers:
        philo.start()


if __name__ == '__main__':
    main_histogram()
    #main_philosophers()

