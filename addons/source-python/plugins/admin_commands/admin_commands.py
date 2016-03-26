import importlib.machinery
import os

from glob import glob

from cvars.public import PublicConVar
from plugins.info import PluginInfo

from . import bans, commands
from .utils import utils


info = PluginInfo()
info.name = "Admin Commands"
info.author = "necavi"
info.version = "0.1"
info.basename = "admin_commands"
info.variable = info.basename + "_version"
info.convar = PublicConVar(info.variable, info.version, info.name + " Version")


cwd = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for module in glob("commands/*.py"):
    name = "admin_commands.commands." + os.path.splitext(os.path.basename(module))[0]
    loader = importlib.machinery.SourceFileLoader(name, module)
    loader.load_module(name)
os.chdir(cwd)


def unload():
    utils.unload()
