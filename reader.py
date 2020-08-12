# coding=utf-8
"""
reader module : reads file instruction
NB : several assumptions
    *x_max<10
    *y_max<10
    *instructions are represented by a single letter
"""

from typing import List, Dict


def reader(file_path) -> List[Dict]:
    """
    reader : increments a list of dict, each dict containing settings for a specific mower
    :param file_path:
    :return List[Dict]:
    """
    file_content = []

    lines = [line.rstrip('\n') for line in open(file_path)]
    lines = [line.replace(" ", "") for line in lines]

    x_max = int(lines[0][0])
    y_max = int(lines[0][1])
    nb_mower = int(len(lines[1:]) / 2)
    for m in range(nb_mower):
        current_mower = {}
        current_mower["name"] = "mower_" + str(m + 1)
        current_mower["x_max"] = x_max
        current_mower["y_max"] = y_max
        current_mower["x_ini"] = int(lines[1 + 2 * m][0])
        current_mower["y_ini"] = int(lines[1 + 2 * m][1])
        current_mower["orientation_ini"] = lines[1 + 2 * m][2]
        current_mower["instructions"] = lines[1 + 2 * m + 1]
        file_content.append(current_mower)

    return file_content
