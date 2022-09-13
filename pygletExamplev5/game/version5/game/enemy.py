import pyglet, math
from pyglet.window import key
from . import bullet, physicalobject, resources

class Enemy(physicalobject.PhysicalObject):
    """ Represents an enemy in Asteroids"""

    def __init__(self, player, *args, **kwargs):
        super(Enemy, self).__init__(img=resources.enemy_image, *args, **kwargs)

        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False

        self.player = player

        self.thrust = 150.0
        self.rotate_speed = 100.0
        self.bullet_speed = 700.0

        self.reacts_to_bullets = False

        def update(self, dt):
            super(Enemy, self).update(dt)

            dx = self.x - self.player.x
            dy = self.y - self.player.y

            angle = atan(dy/dx)
            if angle > self.rotation:
                self.rotation += self.rotate_speed * dt
            else:
                self.rotation -= self.rotate_speed * dt




        def delete(self):
            # We have a child sprite which must be deleted when this object
            # is deleted from batches, etc.
            self.engine_sprite.delete()
            super(Player, self).delete()
