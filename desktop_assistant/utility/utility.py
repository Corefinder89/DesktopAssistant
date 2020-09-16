# -*- coding: utf-8 -*-
import getpass
import os
from configparser import SafeConfigParser


class Utility:
    # This method would get the required path for the directory or a file.
    # This would generate the absolute path to the required directory and the file
    def get_path(self, path_param):
        try:
            required_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_param)
            return required_path
        except IOError as e:
            print("Required Directory / File not found")

    def parse_config(self):
        parser = SafeConfigParser()
        parser.read(self.get_path('../configurations/config.ini'))
        return parser

    def get_current_user(self):
        sysuser = getpass.getuser()
        return sysuser
