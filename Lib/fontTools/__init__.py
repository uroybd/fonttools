from __future__ import print_function, division, absolute_import
from fontTools.misc.py23 import *
import logging
from fontTools.misc.loggingTools import configLogger

log = logging.getLogger(__name__)

version = __version__ = "3.21.3.dev0"

__all__ = ["version", "log", "configLogger"]
