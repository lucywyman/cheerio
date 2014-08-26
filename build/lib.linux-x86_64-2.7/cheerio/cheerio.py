#!usr/bin/env python
from goodbye import *
import random

def cheerio():
    a = random.randint(0, len(goodbyes)-1)
    color = random.randint(0, len(colors)-1)
    print colors[color]+goodbyes[a]+'\033[0m'

if __name__ == "__main__":
    cheerio()    


