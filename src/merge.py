from parse_inputs import parse_inputs
import multiprocessing

def merge(input_array): 

    processes = []

    for element in input_array:
        new_input = [None, element]
        parse_inputs(new_input)
        if 
