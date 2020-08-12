# coding=utf-8
"""
Mower module : manages mower motion
"""

from typing import Callable

from motion import MOTION_DICT
from state import State

Motion = Callable[[State], None]


class Mower:
    """
    Mower Class
    """

    def __init__(self,
                 state: State,
                 instructions: str,
                 name: str = None):
        self.state = state
        self.instructions = instructions
        self.name = name
        self.list_motions = [MOTION_DICT[instructions[i]] for i in range(len(instructions))]

    def __repr__(self):
        output = self.name + "\n"
        output += self.state.__repr__()
        return output

    def unit_move(self, motion: Motion):
        """
        mower move according to a motion instruction
        :param motion:
        :return:
        """
        x_ini = self.state.x
        y_ini = self.state.y
        motion(self.state)
        if not self.state.is_on_lawn():
            # back to previous state
            self.state.x = x_ini
            self.state.y = y_ini

    def sequence_move(self):
        """
        mower move according to a sequence of motion instructions
        :param:
        :return:
        """
        i = 0
        while self.instructions:
            self.unit_move(self.list_motions[i])
            self.instructions = self.instructions[1:]
            i += 1
        print(self)
