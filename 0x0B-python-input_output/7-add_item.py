#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys
import os

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file
# word = sys.argv
# to_json = save_to_json_file(word[1:], 'add_item.json')
# from_json = load_from_json_file("add_item.json")


my_list = []
if os.path.exists("add_item.json"):
    my_list = load_file("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, "add_item.json")
