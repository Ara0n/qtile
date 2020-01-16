from libqtile import layout

def get_layouts():
	layouts = [
		layout.Max(),
		# layout.Stack(num_stacks=2),
		# layout.Bsp(),
		# layout.Columns(),
		# layout.Matrix(),
		layout.MonadTall(),
		# layout.MonadWide(),
		# layout.RatioTile(),
		# layout.Tile(),
		# layout.TreeTab(),
		# layout.VerticalTile(),
		# layout.Zoomy(),
	]

	return layouts
