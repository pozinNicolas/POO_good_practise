# coding=utf-8
"""
Motion module : motion catalog for mower move
"""

from state import State


# Motion catalog
def motion_a(state: State):
    """
    a motion : gowing forward
    :param state:
    :return:
    """
    state.x += (state.orientation == "E") - (state.orientation == "W")
    state.y += (state.orientation == "N") - (state.orientation == "S")


orientations = ["N", "E", "S", "W"]


def motion_d(state: State):
    """
    d motion : turning right
    :param state:
    :return:
    """

    def cyclic_clockwise(orientation_ini):
        return orientations[(orientations.index(orientation_ini) + 1) % (len(orientations))]

    state.orientation = cyclic_clockwise(state.orientation)


def motion_g(state: State):
    """
    g motion : turning left
    :param state:
    :return:
    """

    def cyclic_counterclockwise(orientation_ini):
        return orientations[(orientations.index(orientation_ini) + len(orientations) - 1) % (len(orientations))]

    state.orientation = cyclic_counterclockwise(state.orientation)


MOTION_DICT = {
    "A": motion_a,
    "G": motion_g,
    "D": motion_d,
}
