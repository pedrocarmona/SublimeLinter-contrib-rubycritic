#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Pedro Carmona
# Copyright (c) 2015 Pedro Carmona
#
# License: MIT
#

"""This module exports the Rubycritic plugin class."""

from SublimeLinter.lint import Linter
import sublime


class Rubycritic(Linter):

    """Provides an interface to rubycritic."""

    def get_files():
        files = ""
        for window in sublime.windows():
            if window.extract_variables()['file_extension'] == "rb":
                files += str(window.extract_variables()['file'])
                files += " "
        return files

    syntax = ('ruby', 'ruby on rails', 'rspec')
    cmd = 'rubycritic * %s' % get_files()
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(:?(?P<warning>[RCW])|(?P<error>[EF])): '
        r'(?P<message>.+)'
    )
    defaults = {
        '--format=': 'emacs'
    }
    # comment_re = r'\s*#'
