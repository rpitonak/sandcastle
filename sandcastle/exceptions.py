# MIT License
#
# Copyright (c) 2018-2019 Red Hat, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class SandcastleException(Exception):
    """ Something went wrong. """


class SandcastleExecutionError(SandcastleException):
    """ There was an issue during sandbox execution. """


class SandcastleCommandFailed(SandcastleException):
    """ The command executed in sandbox failed. """

    def __init__(self, output: str, reason: str, rc: int):
        """
        :param output: output of the command
        :param reason: reason the command failed
        :param rc: return code
        """
        self.output: str = output
        self.reason: str = reason
        self.rc: int = rc

    def __repr__(self):
        return f"SandcastleCommandFailed(reason={self.reason}, rc={self.rc})\n{self.output}"

    def __str__(self):
        return f"Command failed (rc={self.rc}, reason={self.reason})\n{self.output}"
