from players.helpers import userid_from_index, edict_from_userid
from commands import CommandReturn
from engines.server import engine_server
from ..utils.utils import target_filter, Command, message_client


@Command("sp_kick", permission="sp.punishment.kick")
def sp_kick(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_kick $c=(white)<name|#userid|@filter> [reason: \"\"]")
        return CommandReturn.BLOCK
    targets = target_filter(command[1], source.index)
    if len(targets) == 0:
        source.message("c=(white)[c=(purple)SPc=(white)] No Targets found.")
    else:
        for target in targets:
            reason = " ".join([command[x] for x in range(2, command.get_arg_count())])
            engine_server.server_command("kickid {} {}\n".format(userid_from_index(target), reason))
        source.message("c=(white)[c=(purple)SPc=(white)] Kicked " + str(len(targets)) + " players.")
    return CommandReturn.BLOCK


@Command("sp_ban", permission="sp.punishment.ban")
def sp_ban(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_ban $c=(white)<name|#userid|@filter> [minutes: 0] [reason: \"\"]")
        return CommandReturn.BLOCK
    targets = target_filter(command[1], source.index)
    time = command[2] if command.get_arg_count() > 2 else 0
    reason = " ".join([command[x] for x in range(3, command.get_arg_count())])
    if len(targets) == 0:
        source.message("c=(white)[c=(purple)SPc=(white)] No Targets found.")
    else:
        for target in targets:
            engine_server.server_command("banid {} {}\n".format(time, userid_from_index(target)))
            engine_server.server_command("kickid {} {}\n".format(userid_from_index(target), reason))
            engine_server.server_command("writeid")
        source.message("c=(white)[c=(purple)SPc=(white)] Banned " + str(len(targets)) + " players.")
    return CommandReturn.BLOCK


@Command("sp_unban", permission="sp.punishmnet.unban")
def sp_unban(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_unban $c=(white)<steamid>")
        return CommandReturn.BLOCK
    steamid = command[1]
    engine_server.server_command("removeid {}\n".format(steamid))
    return CommandReturn.BLOCK


@Command("sp_slay", permission="sp.punishment.slay")
def sp_slay(source, command):
    if command.get_arg_count() == 1:
        source.message("c=(white)[c=(purple)SPc=(white)] Usage: $c=(purple)sp_slay $c=(white)<name|#userid|@filter>")
        return CommandReturn.BLOCK
    targets = target_filter(command[1], source.index)
    if len(targets) == 0:
        source.message("c=(white)[c=(purple)SPc=(white)] No Targets found.")
    else:
        for target in targets:
            engine_server.client_command(edict_from_userid(userid_from_index(target)), "kill", True)
            message_client(target, "You have been slayed.")
        source.message("c=(white)[c=(purple)SPc=(white)] Slayed " + str(len(targets)) + " players.")
    return CommandReturn.BLOCK
