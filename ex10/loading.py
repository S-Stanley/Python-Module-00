#!/usr/bin/python3

from tqdm import tqdm
from time import sleep

def ft_progress(lst):
    for i in tqdm(lst): sleep(0.002)
lst = range(1000)

ft_progress(lst)