#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	for key, v in sorted(a_dictionary):
		print("{}: {}".format(key, v))
