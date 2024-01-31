import json


def jsonize(diff_tree):
    return json.dumps(diff_tree, indent=4)
