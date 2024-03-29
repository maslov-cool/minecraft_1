from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import keyboard

game = Ursina()

grass = load_texture('textures/grass.png')
land = load_texture('textures/land.jpg')
sky = load_texture('textures/sky.png')
books = load_texture('textures/books.jpg')
bricks = load_texture('textures/bricks.jpg')
sand = load_texture('textures/sand.jpg')
tree = load_texture('textures/tree.png')
grass_and_land = load_texture('textures/grass_and_land.jpg')

main_texture = land


def update():
    global main_texture

    if held_keys['0']:
        main_texture = grass
    if held_keys['1']:
        main_texture = land
    if held_keys['2']:
        main_texture = grass_and_land
    if held_keys['3']:
        main_texture = sand
    if held_keys['4']:
        main_texture = tree
    if held_keys['5']:
        main_texture = bricks
    if held_keys['6']:
        main_texture = books

    if held_keys['right mouse'] or held_keys['left mouse']:
        hand.active()
    else:
        hand.passive()


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            scale=(0.2, 0.3),
            color=color.rgb(255, 223, 196),
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.4)
        )

    def active(self):
        self.position = Vec2(0.1, -0.5)
        self.rotation = Vec3(90, -10, 0)

    def passive(self):
        self.rotation = Vec3(150, -10, 0)
        self.position = Vec2(0.4, -0.4)


class Management(Button):
    def __init__(self, position=(0, 0, 0), texture=grass):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=5,
            texture=texture,
            color=color.color(0, 0, 255),
            highlight_color=color.yellow
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Management(position=self.position + mouse.normal, texture=main_texture)
            if key == 'right mouse down':
                destroy(self)


for z in range(40):
    for x in range(40):
        for y in range(3):
            management = Management((x, y, z))


player = FirstPersonController()
sky = Sky(texture=sky)
hand = Hand()
game.run()

