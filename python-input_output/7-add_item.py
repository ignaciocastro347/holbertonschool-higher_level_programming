#!/usr/bin/python3
""" add_item module """
if __name__ == '__main__':
    import sys
    save_to_file = __import__('5-save_to_json_file').save_to_json_file
    load_file = __import__('6-load_from_json_file').load_from_json_file
    argv = sys.argv

    try:
        list = load_file("add_item.json")
    except Exception:
        list = []
    list += argv[1:]
    save_to_file(list, "add_item.json")
