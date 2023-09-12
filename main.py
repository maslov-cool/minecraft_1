from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import keyboard

game = Ursina()

grass = load_texture('grass.png')
land = load_texture('land.jpg')
sky = load_texture('sky.png')
books = load_texture('books.jpg')
bricks = load_texture('bricks.jpg')
sand = load_texture('sand.jpg')
tree = load_texture('tree.png')
grass_and_land = load_texture('grass_and_land.jpg')

main_texture = land


def update():
    global main_texture

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


for z in range(50):
    for x in range(50):
        # for y in range(2):
        Management((x, 0, z))


class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.speed = 3

    def input(self, key):
        if keyboard.is_pressed(87):
            end_position = self.position + self.forward * self.speed
            self.animate('position', end_position, duration=0.1)
        if keyboard.is_pressed(83):
            end_position = self.position - self.forward * self.speed
            self.animate('position', end_position, duration=0.1)
        if keyboard.is_pressed(68):
            end_position = self.position + self.right * self.speed
            self.animate('position', end_position, duration=0.1)
        if keyboard.is_pressed(65):
            end_position = self.position - self.right * self.speed
            self.animate('position', end_position, duration=0.1)
        if keyboard.is_pressed('space'):
            end_position = self.position + self.up * 7
            self.animate('position', end_position, duration=1)


player = Player()
sky = Sky(texture=sky)
hand = Hand()
game.run()
