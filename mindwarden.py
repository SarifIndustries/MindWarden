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
import os
import sys

WARDEN_FILE = os.path.join(os.path.expanduser("~"), ".warden/warden.conf")

# Color codes
RESET =   "\033[0m"
BOLD =    "\033[1m"
GREEN =   "\033[32m"
LGREEN =  "\033[92m"
LMAG =    "\033[96m"

DEEDS = [
#   Deed                     Weight
    ("The Last Spell",          6),
    #("The Book of Hours",       7), Until Last Spell finish
    #("The Longing",             3), Until This War Of Mine finish
    ("This War of Mine",        3),
    ("Gods Will Be Watching",   4),
    ("The Work",                2),
    ("The Station Deeds",       2),
    ("The Knowledge",           4),
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


def record(deed):
    with open(WARDEN_FILE, 'w') as f:
        f.write(deed)


def show_last_deed():
    with open(WARDEN_FILE, 'r') as f:
        last_deed = f.read()
        print(last_deed)


#===================== MAIN =====================

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--last":
            show_last_deed()
        elif arg == "--run":
            print("[ " ,LGREEN, "Station argus report", RESET, " ]", sep="")
            time.sleep(0.6)
            print("[ ", LGREEN, "Current date: ", RESET, "10.10.2078 ]", sep="")
            time.sleep(0.6)
            print("[ ", BOLD, LMAG, "Mindwarden", RESET, " launch ]", sep="")
            deed = weighted_choice(DEEDS)
            record(deed)
            print("Deed: ", BOLD, deed, RESET, sep="")
    else:
        print("--run for run, --last for last")

#================================================


if __name__ == "__main__":
    main()

