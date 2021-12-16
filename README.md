![is_maintained](https://camo.githubusercontent.com/6e4da91cb02711349e6b9d0aba6a767362818c1d17891a02f06fded4415f6172/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d61696e7461696e65642533462d7965732d677265656e2e737667)
![pypi_version](https://img.shields.io/badge/pypi-v1.0.1-%233775A9)

# Chunky
A chunking system for game development


## Using the library

### Installation
run `pip install hamolicious-chunky`

### Implementing
```python

# import necessary modules from library
from chunky import World as BaseWorld, Chunk, Vec2d

# setup library
BaseWorld.render_dist.set(3, 3) # how many chunks to load
Chunk.size = Vec2d(300, 300) # size of chunks in pixels

# override the `generate_chunk()` method
class World(BaseWorld):
	def generate_chunk(self, pos:Vec2d) -> Chunk:
		chunk = Chunk(pos)
		chunk.objects.append() # add objects the chunk should hold
		return chunk # should always return chunk

# create player
player_pos = Vec2d(500, 500)

# instantiate class
world = World(player_pos)

while True: # main loop
	world.update(player_pos) # update to generate new chunks and update the loaded chunks

	chunks = world.get_loaded_chunks() # gets the chunks inside the render distance

```

