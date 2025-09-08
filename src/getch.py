"""
Get character function.

full disclosure this code was taken from the internet.
source: https://code.activestate.com/recipes/134892/
"""


class _Getch:
    """
    Gets a single character from standard input.

    Does not echo to the screen.
    """

    def __init__(self):
        """Initialize the class."""
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        """Initialize the class."""
        import termios
        dir(termios)

    def __call__(self):
        """Call unix getch."""
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        """Initialize the class."""
        import msvcrt
        dir(msvcrt)

    def __call__(self):
        """Call windows getch."""
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
