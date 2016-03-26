from engines.server import engine_server
from commands import CommandReturn
from listeners.tick.delays import tick_delays
from ..utils.utils import Command, change_map


@Command("sp_map", permission="sp.map.map")
def sp_map(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_map $c=(white)<map>")
        return CommandReturn.BLOCK
    level = command[1]
    if not engine_server.is_map_valid(level):
        source.message("c=(white)[c=(purple)SPc=(white)] Map not found")
        return CommandReturn.BLOCK
    tick_delays.delay(3.0, change_map, level)
    source.message("c=(white)[c=(purple)SPc=(white)] Changing map to {} in 3 seconds".format(level))
