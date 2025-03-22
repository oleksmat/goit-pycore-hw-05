from .add import add
from .close import close
from .delete import delete
from .hello import hello
from .list import list
from .update import update
from .view import view


# every command is exported as a tuple:
# (
#   list_of_names>: list[str],
#   number_of_parameters: int,
#   description: str,
#   command_routine: CommandRoutine
# )
#
# where:
# CommandRoutine = (contacts: dict[str,str], *args: [str]) -> str
# contacts - mutable list of contacts
# args - arguments passed by user
# :return - text to render to the user

# we combine all commans into a single list
commands = [add, close, delete, hello, list, update, view]
