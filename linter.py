"""This module exports the Bashate plugin class."""

from cuda_lint import Linter, util
import os

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
    
    def tmpfile(self, cmd, code, suffix=''):
        """
        Run an external executable using a temp file to pass code and return its output.
        We override this to have the tmpfile extension match what is being
        linted so E005 is valid.
        """

        filename, extension = os.path.splitext(self.filename)
        extension = '.missingextension' if not extension else extension
        return super().tmpfile(cmd, code, extension)
    
