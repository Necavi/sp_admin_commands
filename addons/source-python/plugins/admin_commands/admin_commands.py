import importlib.machinery
import os

from . import utils
from glob import glob

from cvars.public import PublicConVar
from plugins.info import PluginInfo

info = PluginInfo()
info.name = "Admin Commands"
info.author = "necavi"
info.version = "0.1"
info.basename = "admin_commands"
info.variable = info.basename + "_version"
info.convar = PublicConVar(info.variable, info.version, 0, info.name + " Version")


cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for module in glob("commands/*.py"):
    name = "admin_commands." + os.path.splitext(os.path.basename(module))[0]
    loader = importlib.machinery.SourceFileLoader(name, module)
    loader.load_module(name)
os.chdir(cwd)


def unload():
    utils.unload()
    