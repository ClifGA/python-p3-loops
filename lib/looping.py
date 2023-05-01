#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i > 0):
        print(i)
        i -= 1
        if i == 0:
            print("Happy New Year!")

def square_integers(int_list):
    new_number = [intnum * intnum for intnum in int_list]
    return new_number

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        else:
            print(i)
            continue
