# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import multilogue as multi
import meeting.assemble as assemble


def main():
    assemble.gather()
    pass


if __name__ == "__main__":
    try:
        while True:
            # This code may be interrupted by ^C on the keyboard.
            main()
    except KeyboardInterrupt:
        # Clean shutdown
        print("    Keyboard Interrupt detected. Exiting...")
        # stop all the machines
        pass # TODO implement STOP MACHINES
        # quit
        exit(0)
