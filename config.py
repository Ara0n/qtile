from libqtile import layout, hook
from libqtile.config import Group

from modules.keys import get_keys, get_mouse
from modules.layouts import get_layouts
from modules.screens import get_screens

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = get_screens()

meta = "mod4"

groups = [Group(name=i[0], label=i[1]) for i in [("F1", "work"), ("F2", "calibre"), ("F3", "internet"), ("F4", "discord"), ("F5", "etc")]]

keys = get_keys(groups)

layouts = get_layouts()


# Drag floating layouts.
mouse = get_mouse()

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
    qtile.cmd_restart()


@hook.subscribe.client_new
def func(c):
    if c.name in ["Discord", "Activité - Discord", "Discord Updater", "Telegram"]:
        c.togroup("F4")
    elif c.name in ["Mozilla Firefox"]:
        c.togroup("F3")
    elif c.name in ["calibre", "V calibre"]:
        c.togroup("F2")
    elif c.name in ["PyCharm", "IntelliJ IDEA", "Clion", "win0"]:
        c.togroup("F1")
