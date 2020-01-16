from libqtile.config import Screen
from libqtile import widget, bar
import subprocess
import os


def get_screens():
	# check screen numbers (either 1 or 2)
	ps = subprocess.Popen("xrandr -q | grep ' connected' | wc -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	nb_screens = int(ps.communicate()[0])

	if nb_screens == 1:
		screens = [
			Screen(
				top=bar.Bar(
					[
						widget.CurrentLayoutIcon(),
						widget.CurrentScreen(),
						widget.GroupBox(),
						widget.Prompt(),
						widget.TaskList(),
						# widget.WindowName(),
						widget.Systray(),
						widget.Wallpaper(wallpaper_command=["feh", "--bg-max"], directory=f"~/.config/qtile/wallpapers/", label="\N{ARTIST PALETTE}"),
						widget.ThermalSensor(),
						widget.Clock(format='%a %H:%M'),
						widget.BatteryIcon(),
						widget.CheckUpdates(distro="Debian"),   # added root cronjob for apt update -y
						widget.Notify(),
					],
					24,
				),
			),
		]

	else:
		screens = [
			Screen(
				top=bar.Bar(
					[
						widget.CurrentLayoutIcon(),
						widget.CurrentScreen(),
						widget.GroupBox(),
						widget.Prompt(),
						widget.TaskList(),
						# widget.WindowName(),
						widget.Systray(),
						widget.Wallpaper(wallpaper_command=["feh", "--bg-max"], directory=f"~/.config/qtile/wallpapers/", label="\N{ARTIST PALETTE}"),
						widget.ThermalSensor(),
						widget.Clock(format='%a %H:%M'),
						widget.BatteryIcon(),
						widget.CheckUpdates(distro="Debian"),   # added root cronjob for apt update -y
						widget.Notify(),
					],
					24,
				),
			),
			Screen(
				top=bar.Bar(
					[
						widget.CurrentLayoutIcon(),
						widget.CurrentScreen(),
						widget.GroupBox(),
						widget.TaskList(),
						# widget.WindowName(),
						widget.Battery(),
						widget.Clock(format='%a %H:%M'),
					],
					24,
				)
			)
		]

	return screens
