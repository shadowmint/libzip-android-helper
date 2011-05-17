from optparse import OptionParser
import os
import sys

__ROOT = False
__EXT = False

def __getParams():
  """ Get the build target from the command line. """
  global __ROOT, __EXT
  parser = OptionParser()
  parser.add_option("-x", "--ext", dest="ext", help="build extension", metavar="EXT")
  parser.add_option("-p", "--path", dest="path", help="build root", metavar="PATH")
  (options, args) = parser.parse_args()
  if (not options.__dict__['path'] is None):
    __ROOT = options.__dict__["path"]
  if (not options.__dict__['ext'] is None):
    __EXT = options.__dict__["ext"]

def __findSources(path, ext):
  """ Returns an array of files from target. """
  rtn = []
  if os.path.exists(path) and os.path.isdir(path):
    d = os.listdir(path)
    for name in d:
      if name.endswith("."+ext):
        rtn.append(name)
  return rtn

__getParams()
if __ROOT and __EXT:
  set = __findSources(__ROOT, __EXT)
  for i in set:
    sys.stdout.write(i + " ")
