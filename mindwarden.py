#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# List
# - use colored ouput
# - use animated output
# - no library module for now
# - v2: use sqlite module for table
# - v2: table keeps balance weights
# - v2: table keeps stats
# - enable as global script via scriptrunner
# Created by: Sarif Industries


#======================================#
#=            MIND WARDEN             =#
#======================================#

"""
    
"""


import random
import time
from functools import reduce


# Color codes
RESET =   "\033[0m"
BOLD =    "\033[1m"
GREEN =   "\033[32m"
LGREEN =  "\033[92m"
LMAG =    "\033[96m"

DEEDS = [
#   Deed                     Weight
    ("The Last Spell",          5),
    ("The Book of Hours",       5),
    ("The Longing",             2),
]


"""
    Выбор элемента в соответствии с его весом.
"""
def weighted_choice(settings: list):
    total_weight = reduce(lambda a, b: a + b, [w for (s, w) in settings])
    r = random.random() * total_weight
    # Секции делят интервал (от 0 до Суммы весов) на отрезки для каждого элемента.
    # Проверяем в какую секцию попало случайное число r.
    choice = None
    section = 0
    for (s, w) in settings:
        section += w
        if r < section:
            # Попали в секцию для этого элемента.
            choice = s
            break
    return choice


# Unit test
def test_weighted_choice():
    stats = { deed[0]:0 for deed in DEEDS }
    test_range = 10_000
    for _ in range(test_range):
        choice = weighted_choice(DEEDS)
        stats[choice] += 1
    percented_stats = { key: f"{int(stats[key] / test_range * 100)}%" for key in stats.keys() }
    print(f"Probability distribution test results:\n{percented_stats}")


#===================== MAIN =====================

def main():
	# TODO: color
    print("[ " ,LGREEN, "Station argus report", RESET, " ]", sep="")
    time.sleep(0.6)
    print("[ ", LGREEN, "Current date: ", RESET, "10.10.2078 ]", sep="")
    time.sleep(0.6)
    print("[ ", BOLD, LMAG, "Mindwarden", RESET, " launch ]", sep="")
    deed = weighted_choice(DEEDS)
    print("Deed: ", BOLD, deed, RESET, sep="")

#================================================


if __name__ == "__main__":
    main()

