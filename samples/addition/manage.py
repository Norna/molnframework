#!/usr/bin/evn python
""" 
Command-line utility for administrative task
"""

import os
import sys
sys.path.append('C:\\Users\\RHINO\\Studies\\Semester4\\framework\\framework')

from molnframework.core import serialisers

if __name__ == "__main__":

    """ Just Keep It """

    #execute_from_command_line(sys.argv)

    """ ----- """

    os.environ.setdefault("MOLNFRAMEWORK_SETTINGS_MODULE","settings")
    
    from molnframework.core.management import execute_command_line
    execute_command_line(sys.argv)

