from commands import CommandReturn
from .sp_utils.utils import Command, target_filter


@Command("sp_rename", permission="sp.player.rename")
def sp_rename(source, command):
    if command.get_arg_count() < 3:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_rename$c=(white)<name|#userid> <name>")
        return CommandReturn.BLOCK
    target = target_filter(command[1], source.index, False)
    if target is None:
        source.message("c=(white)[c=(purple)SPc=(white)] Target not found.")
        return CommandReturn.BLOCK
    name = command[2]
    source.message("c=(white)[c=(purple)SPc=(white)] Rename is not implemented for this game.")