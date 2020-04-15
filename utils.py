import os
import subprocess as sub

def does_exist(filepath):
    filepath = os.path.expanduser(filepath)
    if not os.path.exists(filepath):
        return False
    return True

def is_installed(program_name):
    code = sub.call(f"which {program_name}".split(), stdout=sub.DEVNULL)
    if code != 0:
        return False
    return True

# TODO a program package should be a series of steps that you do before installing
# each step should have a skipper func, aka some kind of way to skip the step if 
# the requirements are already installed

