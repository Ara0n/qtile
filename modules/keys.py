from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
import os

meta = "mod4"
alt = "mod1"
ctrl = "control"
shift = "shift"


def get_keys(groups=[]):
    newpath = os.getenv("PATH").replace("/home/thomas/local/qtile/venv/bin:", "")
    exitvenv = f"env -u VIRTUAL_ENV PATH='{newpath}'"   # to get out of the venv used to launch qtile


    keys = [
        # session management
        Key([meta, ctrl], "r", lazy.restart()),
        Key([meta, ctrl], "q", lazy.shutdown()),


        # screen management
        ## hide bar from the screen
        Key([meta], "F11", lazy.hide_show_bar("top")),

        ## lock screen
        Key([meta], "l", lazy.spawn(f"{exitvenv} xtrlock")),

        ## brightness control
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -10")),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl +10")),

        ## Toggle between different layouts as defined below
        Key([meta], "Tab", lazy.next_layout()),

        ## switch to screen
        Key([meta], "Up", lazy.to_screen(0)),
        Key([meta], "Down", lazy.to_screen(1)),

        ## Switch between windows in current stack pane
        Key([meta], "Left", lazy.layout.up()),
        Key([meta], "Right", lazy.layout.down()),

        ## Move windows up or down in current stack
        Key([meta, ctrl], "Left", lazy.layout.shuffle_up()),
        Key([meta, ctrl], "Right", lazy.layout.shuffle_down()),

        ## Switch window focus to other pane(s) of stack
        Key([meta], "space", lazy.layout.next()),

        ## Swap panes of split stack
        Key([meta, shift], "space", lazy.layout.rotate()),


        # window/tile management
        ## opacity control
        Key([meta], "XF86MonBrightnessDown", lazy.window.down_opacity()),
        Key([meta], "XF86MonBrightnessUp", lazy.window.up_opacity()),
        Key([meta, ctrl], "XF86MonBrightnessDown", lazy.window.opacity(0.1)),
        Key([meta, ctrl], "XF86MonBrightnessUp", lazy.window.opacity(1)),

        ## tile size change
        Key([meta], "KP_Add", lazy.layout.grow()),
        Key([meta], "KP_Subtract", lazy.layout.shrink()),
        Key([meta], "KP_Enter", lazy.layout.swap_main()),
        Key([meta], "KP_Multiply", lazy.layout.maximize()),
        Key([meta], "KP_Divide", lazy.layout.flip()),

        ## close current window
        Key([meta], "w", lazy.window.kill()),


        # softwares
        Key([meta], "r", lazy.spawncmd()),

        ## spawn terminal
        Key([meta], "Return", lazy.spawn(f"{exitvenv} kitty")),

        # custom lauch programs
        Key([meta], "f", lazy.spawn(f"{exitvenv} firefox-esr")),
        Key([meta], "d", lazy.spawn(f"{exitvenv} discord-ptb")),
        Key([meta], "c", lazy.spawn(f"{exitvenv} CALIBRE_USE_DARK_PALETTE=1 calibre")),
        Key([meta], "t", lazy.spawn(f"{exitvenv} telegram-desktop")),
        Key([meta], "e", lazy.spawn(f"{exitvenv} nautilus")),
        Key([meta], "m", lazy.spawn("kitty qshell")),

        ## IDE software
        Key([meta], "p", lazy.spawn(f"{exitvenv} pycharm")),
        Key([meta], "o", lazy.spawn(f"{exitvenv} clion")),
        Key([meta], "i", lazy.spawn(f"{exitvenv} idea")),
        Key([meta], "u", lazy.spawn(f"{exitvenv} phpstorm")),

        ## task manager
        Key([alt, ctrl], "Delete", lazy.spawn("kitty htop")),

        ## network manager
        Key([meta], "n", lazy.spawn("kitty nmtui")),

        ## GUI volume control
        Key([meta], "v", lazy.spawn(f"{exitvenv} pavucontrol")),


        # volume control
        Key([], "XF86AudioLowerVolume", lazy.spawn("pulseaudio-ctl down")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("pulseaudio-ctl up")),
        Key([], "XF86AudioMute", lazy.spawn("pulseaudio-ctl mute")),
    ]

    # setup group keybinds
    for i in groups:
        keys.extend([
            Key([meta], i.name, lazy.group[i.name].toscreen()),
            Key([meta, "control", shift], i.name, lazy.window.togroup(i.name, switch_group=True)),
            Key([meta, shift], i.name, lazy.window.togroup(i.name)),
        ])
    return keys


def get_mouse():
    # Drag floating layouts.
    mouse = [
        Drag([meta], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([meta], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Click([meta], "Button2", lazy.window.toggle_floating())
    ]

    return mouse
