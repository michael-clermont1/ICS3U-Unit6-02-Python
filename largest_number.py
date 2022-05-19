#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is gets the largest numbr in an array

import random


def largest_number_array(array):
    # this function is gets the largest numbr in an array

    large_number = 0
    for counter in range(0, len(array)):
        maxi = array[counter]
        if large_number < maxi:
            large_number = maxi

    return large_number


def main():
    # this function uses a list

    random_numbers = []
    largest_number = 0

    # input
    print("The numbers are: ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 100)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    largest_number = largest_number_array(random_numbers)

    print("The largest number generated is: {0} ".format(largest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
