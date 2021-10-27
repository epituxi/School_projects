import datetime
import string
import itertools
from timeit import default_timer as timer
import time

#This program brute forces a password

def password():
    password = input("Set your password:\n")
    return password

def solver(password):
    global guess
    i = 0
    chars = string.printable
    answer = ''
    time_start = timer()
    sekuntikello = int(timer() - time_start)
    for j in range(1, 100000000):
        for guess in itertools.product(chars, repeat=j):
            i += 1
            guess = ''.join(guess)
            if sekuntikello < int(timer() - time_start):
                sekuntikello = int(timer() - time_start)
                print(guess, sekuntikello)
            if guess == password:
                time_end = timer()
                answer = password
                return answer, time_end, time_start


def main():
    salasana = password()
    answer, time_end, time_start = solver(salasana)
    time_elapsed = time_end - time_start
    print("The program found inputted password {} in {:.2f} seconds.".format(answer, time_elapsed))
main()