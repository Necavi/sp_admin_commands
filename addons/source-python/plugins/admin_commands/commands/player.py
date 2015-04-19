from commands import CommandReturn
from .utils import Command, target_filter


@Command("sp_rename", permission="sp.player.rename")
def sp_rename(source, command):
    if command.get_arg_count() < 3:
        source.message("Usage: ${purple}sp_rename${white}<name|#userid> <name>")
        return CommandReturn.BLOCK
    target = target_filter(command[1], source.index, False)
    if target is None:
        source.message("Target not found.")
        return CommandReturn.BLOCK
    name = command[2]
    source.message("Rename is not implemented for this game.")