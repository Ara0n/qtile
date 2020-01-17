from libqtile import layout

config = {
	"margin": 15,
	"num_stacks": 2
}

def get_layouts():
	layouts = [
		layout.Max(),
		# layout.Stack(num_stacks=2),
		# layout.Bsp(),
		# layout.Columns(),
		# layout.Matrix(**config),
		layout.MonadTall(),
		# layout.MonadWide(),
		# layout.RatioTile(**config),
		# layout.Tile(),
		# layout.TreeTab(),
		# layout.VerticalTile(),
		# layout.Zoomy(),
		layout.Stack(**config),
	]

	return layouts
