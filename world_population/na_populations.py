import pygal

wm = pygal.maps.world.World()
wm.title = 'Population of Countries in NA'

wm.add('North America', {'ca': 34126000, 'mx': 113423000, 'us': 309349000})

wm.render_to_file('na_populations.svg')
