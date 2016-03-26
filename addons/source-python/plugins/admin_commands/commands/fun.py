from players.entity import PlayerEntity
from commands import CommandReturn
from ..utils.utils import target_filter, Command, message_client

from entities.constants import MoveType
from listeners.tick.delays import tick_delays


@Command("sp_ignite", permission="sp.fun.ignite")
def sp_ignite(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: c=(purple)sp_ignite $c=(white)<name|#userid|@filter> [time: 0]")
        return CommandReturn.BLOCK
    targets = target_filter(command[1], source.index)
    time = int(command[2]) if command.get_arg_count() > 2 else 0
    if len(targets) == 0:
        source.message("c=(white)[c=(purple)SPc=(white)] No Targets found.")
    else:
        for target in targets:
            player = PlayerEntity(target)
            player.ignite_lifetime(time) if time > 0 else player.ignite()
            message_client(player.index, "You have been set on fire for " + str(time) + " seconds.")
        source.message("c=(white)[c=(purple)SPc=(white)] Set " + str(len(targets)) + " players on fire.")
    return CommandReturn.BLOCK


def unfreeze(player):
    player.move_type = MoveType.WALK
    message_client(player.index, "You have been unfrozen.")


@Command("sp_freeze", permission="sp.fun.freeze")
def sp_ignite(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_freeze $c=(white)<name|#userid|@filter> [time: 0]")
        return CommandReturn.BLOCK
    targets = target_filter(command[1], source.index)
    time = int(command[2]) if command.get_arg_count() > 2 else 0
    if len(targets) == 0:
        source.message("c=(white)[c=(purple)SPc=(white)] No Targets found.")
    else:
        for target in targets:
            player = PlayerEntity(target)
            player.move_type = MoveType.NONE
            if time != 0:
                tick_delays.delay(time, unfreeze, player)
                message_client(player.index, "You have been frozen for " + str(time) + " seconds.")
            message_client(player.index, "You have been frozen.")
        source.message("c=(white)[c=(purple)SPc=(white)] Froze " + str(len(targets)) + " players.")
    return CommandReturn.BLOCK


@Command("sp_unfreeze", permission="sp.fun.unfreeze")
def sp_ignite(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_unfreeze $c=(white)<name|#userid|@filter>")
        return CommandReturn.BLOCK
    targets = target_filter(command[1], source.index)
    if len(targets) == 0:
        source.message("c=(white)[c=(purple)SPc=(white)] No Targets found.")
    else:
        for target in targets:
            player = PlayerEntity(target)
            if player.move_type == MoveType.NONE:
                player.move_type = MoveType.WALK
                message_client(player.index, "You have been unfrozen.")
        source.message("c=(white)[c=(purple)SPc=(white)] Froze " + str(len(targets)) + " players.")
    return CommandReturn.BLOCK