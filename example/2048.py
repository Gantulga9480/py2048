import os
import sys
sys.path.append(os.getcwd())
from py2048 import Py2048  # noqa


g = Py2048()
g.loop_forever()
