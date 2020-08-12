import math
from collections import Counter


def is_prime(number: int) -> bool:
    """
    Method check if number is prime number.
    Example of prime number 2, 3, 7, 67
    :param number: int
    :return: bool
    """
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        divisor_number = 2
        while divisor_number <= math.sqrt(number):
            if number % divisor_number == 0:
                return False
            divisor_number += 1
    return True


def reduce_elements(sequence_a: list, sequence_b: list) -> list:
    """
    Reduce elements from the sequence_a. If number exists in the sequence_b p times and p is prime number remove
    all repetition of a number in sequence_a.
    :param sequence_a: list
    :param sequence_b: list
    :return: list
    """
    #  # calculate the occurrence of numbers in the sequence_a and sequence_b - fast solution
    occurrence_counter_seq_a = Counter(sequence_a)
    occurrence_counter_seq_b = Counter(sequence_b)
    # Iterate through occurrence counter eg. {2: 2, 3: 2, 21: 2} - (number: occurrence of number)
    for number, occurrence in occurrence_counter_seq_b.items():
        if number in sequence_a and is_prime(occurrence):
            for i in range(occurrence_counter_seq_a[number]):  # remove all repetition of a number from sequence_a
                sequence_a.remove(number)
    return sequence_a
