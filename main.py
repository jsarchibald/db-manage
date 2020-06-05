import ctypes
from db import commands
from PIL import Image
import platform
import pystray
import subprocess
import sys


def set_admin(system):
    if system == "Windows":
        try:
            admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            admin = False
        
        if not admin:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit(0)


def start(icon, item):
    """Start a database service."""
    commandx = commands[system][item.text]["start"]
    for command in commandx:
        command = command.split(" ")
        subprocess.run(command, stdout=subprocess.DEVNULL)


def stop(icon, item):
    """Stop a database service."""
    commandx = commands[system][item.text]["stop"]
    for command in commandx:
        command = command.split(" ")
        subprocess.run(command, stdout=subprocess.DEVNULL)


def quit_program(icon, item):
    """Quits the program"""
    icon.stop()
    sys.exit(0)


def start_menu():
    menu = pystray.Menu(
        pystray.MenuItem(
            "MongoDB",
            start
        ),
        pystray.MenuItem(
            "MySQL",
            start
        ),
        pystray.MenuItem(
            "PostgreSQL",
            start
        )
    )
    return menu


def stop_menu():
    menu = pystray.Menu(
        pystray.MenuItem(
            "MongoDB",
            stop
        ),
        pystray.MenuItem(
            "MySQL",
            stop
        ),
        pystray.MenuItem(
            "PostgreSQL",
            stop
        )
    )
    return menu

def menu():
    menu = pystray.Menu(
        pystray.MenuItem(
            "Start",
            start_menu()
        ),
        pystray.MenuItem(
            "Stop",
            stop_menu()
        ),
        pystray.MenuItem(
            "Quit",
            quit_program
        )
    )
    return menu


def main():
    system = platform.system()
    set_admin(system)

    img = Image.open("database.png")
    icon = pystray.Icon("DB Manage", icon=img, menu=menu())
    icon.run()


if __name__ == "__main__":
    main()
