"""This module exports the Mypy plugin class."""

from cuda_lint import Linter, util


class Bashate(Linter):

    """Provides an interface to bashate"""
    cmd = 'bashate'
    executable = 'bashate'
    multiline = True
    syntax = ('Bash script')
    regex = (
        r'^.+:(?P<line>\d+):1: (?:(?P<error>E)|(?P<warning>W))\d{3} (?P<message>.+)'
    )
    base_cmd = (
    ''
    )
    tempfile_suffix = 'sh'


    def split_match(self, match):
   
        """Return the components of the error."""
        split_match = super(Bashate, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
    
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd
        return result
