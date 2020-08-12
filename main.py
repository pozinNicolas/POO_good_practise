from state import State
from mower import Mower
from reader import reader

if __name__ == '__main__':

    settings = reader("setting_file.txt")

    initial_states = []
    mowers = []
    for s in settings:
        initial_state = State(x=s["x_ini"], y=s["y_ini"], orientation=s["orientation_ini"],
                              x_max=s["x_max"], y_max=s["y_max"])
        mowers.append(
            Mower(state=initial_state, instructions=s["instructions"], name=s["name"]))

    objective_states = ["13W", "25N"]
    for m, mower in enumerate(mowers):
        mower.sequence_move()
        assert str(
            mower.state) == objective_states[m], \
            "wrong state %r, should be %r" % mower.name % objective_states[m]

        print("passed test for", mower.name)
