# skybridge_adventure.rpy - Zelda-Style Dungeon Adventure
# A Link's Awakening inspired top-down action adventure

####################################################################################################################
# BEACON QUEST - ZELDA-STYLE DUNGEON CRAWLER
####################################################################################################################

init python in beacon_quest:
    import pygame
    import random
    import math
    from pygame.locals import *

    # Game constants
    WIDTH, HEIGHT = 1920, 1080
    TILE_SIZE = 64

    # Room dimensions (tiles)
    ROOM_WIDTH = 16
    ROOM_HEIGHT = 10

    # Calculate offsets to center the room
    ROOM_OFFSET_X = (WIDTH - ROOM_WIDTH * TILE_SIZE) // 2
    ROOM_OFFSET_Y = (HEIGHT - ROOM_HEIGHT * TILE_SIZE) // 2 + 30

    # Tile types
    TILE_FLOOR = 0
    TILE_WALL = 1
    TILE_DOOR_N = 2
    TILE_DOOR_S = 3
    TILE_DOOR_E = 4
    TILE_DOOR_W = 5
    TILE_LOCKED_N = 6
    TILE_LOCKED_S = 7
    TILE_LOCKED_E = 8
    TILE_LOCKED_W = 9
    TILE_CRACKED = 10  # Bombable wall
    TILE_SWITCH = 11
    TILE_SWITCH_ON = 12
    TILE_BLOCK = 13    # Pushable block
    TILE_PIT = 14
    TILE_CHEST = 15
    TILE_CHEST_OPEN = 16
    TILE_STAIRS = 17

    # Item types
    ITEM_KEY = "key"
    ITEM_BOMB = "bomb"
    ITEM_HEART = "heart"
    ITEM_HEART_CONTAINER = "heart_container"
    ITEM_MAP = "map"
    ITEM_COMPASS = "compass"

    # Direction helpers
    DIR_UP = (0, -1)
    DIR_DOWN = (0, 1)
    DIR_LEFT = (-1, 0)
    DIR_RIGHT = (1, 0)
    DIRECTIONS = {'up': DIR_UP, 'down': DIR_DOWN, 'left': DIR_LEFT, 'right': DIR_RIGHT}

    # Game states
    STATE_PLAYING = "playing"
    STATE_TRANSITION = "transition"
    STATE_VICTORY = "victory"
    STATE_GAMEOVER = "gameover"
    STATE_PAUSED = "paused"
    STATE_BOSS_INTRO = "boss_intro"

    ####################################################################################################################
    # ROOM CLASS
    ####################################################################################################################

    class Room:
        """A single room in the dungeon."""
        def __init__(self, room_id, room_type="normal"):
            self.room_id = room_id
            self.room_type = room_type  # normal, entrance, key_room, puzzle, boss, treasure
            self.tiles = [[TILE_FLOOR for _ in range(ROOM_WIDTH)] for _ in range(ROOM_HEIGHT)]
            self.enemies = []
            self.items = []
            self.projectiles = []
            self.switches = []
            self.blocks = []
            self.chest = None
            self.chest_contents = None
            self.cleared = False
            self.visited = False

            # Connections to other rooms (room_id or None)
            self.connections = {'north': None, 'south': None, 'east': None, 'west': None}
            # Door states (open, locked, cracked, none)
            self.doors = {'north': 'none', 'south': 'none', 'east': 'none', 'west': 'none'}

            # Build walls
            self._build_walls()

        def _build_walls(self):
            """Create the room's wall structure."""
            for x in range(ROOM_WIDTH):
                self.tiles[0][x] = TILE_WALL
                self.tiles[ROOM_HEIGHT-1][x] = TILE_WALL
            for y in range(ROOM_HEIGHT):
                self.tiles[y][0] = TILE_WALL
                self.tiles[y][ROOM_WIDTH-1] = TILE_WALL

        def set_door(self, direction, door_type):
            """Set a door in the given direction."""
            self.doors[direction] = door_type

            # Place door tiles
            if direction == 'north':
                cx = ROOM_WIDTH // 2
                if door_type == 'open':
                    self.tiles[0][cx-1] = TILE_DOOR_N
                    self.tiles[0][cx] = TILE_DOOR_N
                elif door_type == 'locked':
                    self.tiles[0][cx-1] = TILE_LOCKED_N
                    self.tiles[0][cx] = TILE_LOCKED_N
                elif door_type == 'cracked':
                    self.tiles[0][cx-1] = TILE_CRACKED
                    self.tiles[0][cx] = TILE_CRACKED

            elif direction == 'south':
                cx = ROOM_WIDTH // 2
                if door_type == 'open':
                    self.tiles[ROOM_HEIGHT-1][cx-1] = TILE_DOOR_S
                    self.tiles[ROOM_HEIGHT-1][cx] = TILE_DOOR_S
                elif door_type == 'locked':
                    self.tiles[ROOM_HEIGHT-1][cx-1] = TILE_LOCKED_S
                    self.tiles[ROOM_HEIGHT-1][cx] = TILE_LOCKED_S
                elif door_type == 'cracked':
                    self.tiles[ROOM_HEIGHT-1][cx-1] = TILE_CRACKED
                    self.tiles[ROOM_HEIGHT-1][cx] = TILE_CRACKED

            elif direction == 'east':
                cy = ROOM_HEIGHT // 2
                if door_type == 'open':
                    self.tiles[cy-1][ROOM_WIDTH-1] = TILE_DOOR_E
                    self.tiles[cy][ROOM_WIDTH-1] = TILE_DOOR_E
                elif door_type == 'locked':
                    self.tiles[cy-1][ROOM_WIDTH-1] = TILE_LOCKED_E
                    self.tiles[cy][ROOM_WIDTH-1] = TILE_LOCKED_E
                elif door_type == 'cracked':
                    self.tiles[cy-1][ROOM_WIDTH-1] = TILE_CRACKED
                    self.tiles[cy][ROOM_WIDTH-1] = TILE_CRACKED

            elif direction == 'west':
                cy = ROOM_HEIGHT // 2
                if door_type == 'open':
                    self.tiles[cy-1][0] = TILE_DOOR_W
                    self.tiles[cy][0] = TILE_DOOR_W
                elif door_type == 'locked':
                    self.tiles[cy-1][0] = TILE_LOCKED_W
                    self.tiles[cy][0] = TILE_LOCKED_W
                elif door_type == 'cracked':
                    self.tiles[cy-1][0] = TILE_CRACKED
                    self.tiles[cy][0] = TILE_CRACKED

        def unlock_door(self, direction):
            """Unlock a locked door."""
            if self.doors[direction] == 'locked':
                self.doors[direction] = 'open'
                cx = ROOM_WIDTH // 2
                cy = ROOM_HEIGHT // 2

                if direction == 'north':
                    self.tiles[0][cx-1] = TILE_DOOR_N
                    self.tiles[0][cx] = TILE_DOOR_N
                elif direction == 'south':
                    self.tiles[ROOM_HEIGHT-1][cx-1] = TILE_DOOR_S
                    self.tiles[ROOM_HEIGHT-1][cx] = TILE_DOOR_S
                elif direction == 'east':
                    self.tiles[cy-1][ROOM_WIDTH-1] = TILE_DOOR_E
                    self.tiles[cy][ROOM_WIDTH-1] = TILE_DOOR_E
                elif direction == 'west':
                    self.tiles[cy-1][0] = TILE_DOOR_W
                    self.tiles[cy][0] = TILE_DOOR_W
                return True
            return False

        def destroy_wall(self, direction):
            """Destroy a cracked wall with a bomb."""
            if self.doors[direction] == 'cracked':
                self.doors[direction] = 'open'
                cx = ROOM_WIDTH // 2
                cy = ROOM_HEIGHT // 2

                if direction == 'north':
                    self.tiles[0][cx-1] = TILE_DOOR_N
                    self.tiles[0][cx] = TILE_DOOR_N
                elif direction == 'south':
                    self.tiles[ROOM_HEIGHT-1][cx-1] = TILE_DOOR_S
                    self.tiles[ROOM_HEIGHT-1][cx] = TILE_DOOR_S
                elif direction == 'east':
                    self.tiles[cy-1][ROOM_WIDTH-1] = TILE_DOOR_E
                    self.tiles[cy][ROOM_WIDTH-1] = TILE_DOOR_E
                elif direction == 'west':
                    self.tiles[cy-1][0] = TILE_DOOR_W
                    self.tiles[cy][0] = TILE_DOOR_W
                return True
            return False

        def add_obstacle(self, x, y, tile_type):
            """Add an obstacle tile."""
            if 1 <= x < ROOM_WIDTH-1 and 1 <= y < ROOM_HEIGHT-1:
                self.tiles[y][x] = tile_type

        def add_pushable_block(self, x, y, target_x=None, target_y=None):
            """Add a pushable block with optional target position."""
            self.blocks.append({
                'x': x, 'y': y,
                'target_x': target_x, 'target_y': target_y,
                'on_target': False
            })
            self.tiles[y][x] = TILE_BLOCK

        def add_switch(self, x, y, linked_door=None):
            """Add a floor switch."""
            self.switches.append({
                'x': x, 'y': y,
                'activated': False,
                'linked_door': linked_door
            })
            self.tiles[y][x] = TILE_SWITCH

        def add_chest(self, x, y, contents):
            """Add a treasure chest."""
            self.chest = {'x': x, 'y': y, 'opened': False}
            self.chest_contents = contents
            self.tiles[y][x] = TILE_CHEST

        def is_walkable(self, x, y):
            """Check if a tile is walkable."""
            if x < 0 or x >= ROOM_WIDTH or y < 0 or y >= ROOM_HEIGHT:
                return False
            tile = self.tiles[y][x]
            walkable_tiles = [
                TILE_FLOOR, TILE_DOOR_N, TILE_DOOR_S, TILE_DOOR_E, TILE_DOOR_W,
                TILE_SWITCH, TILE_SWITCH_ON, TILE_STAIRS
            ]
            return tile in walkable_tiles

        def is_door_tile(self, x, y):
            """Check if tile is a door."""
            if x < 0 or x >= ROOM_WIDTH or y < 0 or y >= ROOM_HEIGHT:
                return False
            return self.tiles[y][x] in [TILE_DOOR_N, TILE_DOOR_S, TILE_DOOR_E, TILE_DOOR_W]

        def is_locked_tile(self, x, y):
            """Check if tile is a locked door."""
            if x < 0 or x >= ROOM_WIDTH or y < 0 or y >= ROOM_HEIGHT:
                return False
            return self.tiles[y][x] in [TILE_LOCKED_N, TILE_LOCKED_S, TILE_LOCKED_E, TILE_LOCKED_W]

        def get_door_direction(self, x, y):
            """Get which direction a door leads."""
            tile = self.tiles[y][x]
            if tile in [TILE_DOOR_N, TILE_LOCKED_N]:
                return 'north'
            elif tile in [TILE_DOOR_S, TILE_LOCKED_S]:
                return 'south'
            elif tile in [TILE_DOOR_E, TILE_LOCKED_E]:
                return 'east'
            elif tile in [TILE_DOOR_W, TILE_LOCKED_W]:
                return 'west'
            return None


    ####################################################################################################################
    # COLLECTIBLE ITEM CLASS
    ####################################################################################################################

    class CollectibleItem:
        """A collectible item in the world."""
        def __init__(self, x, y, item_type):
            self.x = x
            self.y = y
            self.item_type = item_type
            self.collected = False
            self.anim_phase = random.random() * math.pi * 2

        def update(self, dt):
            self.anim_phase += dt * 0.004

        def get_rect(self):
            px = self.x * TILE_SIZE + ROOM_OFFSET_X
            py = self.y * TILE_SIZE + ROOM_OFFSET_Y
            return pygame.Rect(px + 16, py + 16, 32, 32)

        def draw(self, surf, time_ms):
            if self.collected:
                return

            px = self.x * TILE_SIZE + ROOM_OFFSET_X + TILE_SIZE // 2
            py = self.y * TILE_SIZE + ROOM_OFFSET_Y + TILE_SIZE // 2
            bob = math.sin(self.anim_phase) * 4

            if self.item_type == ITEM_KEY:
                # Draw key
                key_color = (255, 220, 50)
                pygame.draw.circle(surf, key_color, (int(px), int(py + bob - 8)), 8)
                pygame.draw.circle(surf, (200, 170, 30), (int(px), int(py + bob - 8)), 5)
                pygame.draw.rect(surf, key_color, (px - 3, py + bob - 4, 6, 16))
                pygame.draw.rect(surf, key_color, (px - 6, py + bob + 8, 5, 4))
                pygame.draw.rect(surf, key_color, (px + 1, py + bob + 4, 5, 4))

            elif self.item_type == ITEM_BOMB:
                # Draw bomb
                pygame.draw.circle(surf, (40, 40, 50), (int(px), int(py + bob)), 14)
                pygame.draw.circle(surf, (60, 60, 70), (int(px - 3), int(py + bob - 3)), 5)
                # Fuse
                pygame.draw.line(surf, (139, 90, 43), (px, py + bob - 14), (px + 5, py + bob - 20), 3)
                # Spark
                spark_size = 3 + int(2 * math.sin(time_ms * 0.01))
                pygame.draw.circle(surf, (255, 200, 50), (int(px + 5), int(py + bob - 20)), spark_size)

            elif self.item_type == ITEM_HEART:
                # Draw heart
                color = (255, 80, 80)
                pygame.draw.circle(surf, color, (int(px - 6), int(py + bob - 4)), 8)
                pygame.draw.circle(surf, color, (int(px + 6), int(py + bob - 4)), 8)
                pygame.draw.polygon(surf, color, [
                    (px - 14, py + bob), (px + 14, py + bob), (px, py + bob + 14)
                ])
                # Shine
                pygame.draw.circle(surf, (255, 200, 200), (int(px - 4), int(py + bob - 6)), 3)

            elif self.item_type == ITEM_HEART_CONTAINER:
                # Draw heart container (larger, golden outline)
                color = (255, 80, 80)
                outline = (255, 220, 50)
                pygame.draw.circle(surf, outline, (int(px - 8), int(py + bob - 5)), 12)
                pygame.draw.circle(surf, outline, (int(px + 8), int(py + bob - 5)), 12)
                pygame.draw.polygon(surf, outline, [
                    (px - 20, py + bob + 2), (px + 20, py + bob + 2), (px, py + bob + 22)
                ])
                pygame.draw.circle(surf, color, (int(px - 8), int(py + bob - 5)), 9)
                pygame.draw.circle(surf, color, (int(px + 8), int(py + bob - 5)), 9)
                pygame.draw.polygon(surf, color, [
                    (px - 17, py + bob + 2), (px + 17, py + bob + 2), (px, py + bob + 18)
                ])


    ####################################################################################################################
    # PROJECTILE CLASS
    ####################################################################################################################

    class Projectile:
        """A projectile (arrow, magic, etc)."""
        def __init__(self, x, y, dx, dy, proj_type="arrow", damage=1, from_player=False):
            self.x = x
            self.y = y
            self.dx = dx
            self.dy = dy
            self.proj_type = proj_type
            self.damage = damage
            self.from_player = from_player
            self.speed = 6 if proj_type == "arrow" else 4
            self.alive = True
            self.lifetime = 3000

        def update(self, dt, room):
            self.lifetime -= dt
            if self.lifetime <= 0:
                self.alive = False
                return

            self.x += self.dx * self.speed
            self.y += self.dy * self.speed

            # Check wall collision
            tile_x = int((self.x - ROOM_OFFSET_X) // TILE_SIZE)
            tile_y = int((self.y - ROOM_OFFSET_Y) // TILE_SIZE)

            if tile_x < 1 or tile_x >= ROOM_WIDTH - 1 or tile_y < 1 or tile_y >= ROOM_HEIGHT - 1:
                self.alive = False
            elif room.tiles[tile_y][tile_x] == TILE_WALL:
                self.alive = False

        def get_rect(self):
            return pygame.Rect(self.x - 8, self.y - 8, 16, 16)

        def draw(self, surf):
            if not self.alive:
                return

            if self.proj_type == "arrow":
                # Draw arrow
                angle = math.atan2(self.dy, self.dx)
                end_x = self.x + math.cos(angle) * 15
                end_y = self.y + math.sin(angle) * 15
                pygame.draw.line(surf, (139, 90, 43), (self.x, self.y), (end_x, end_y), 3)
                # Arrowhead
                pygame.draw.circle(surf, (100, 100, 110), (int(end_x), int(end_y)), 4)

            elif self.proj_type == "magic":
                # Draw magic orb
                pygame.draw.circle(surf, (150, 50, 200), (int(self.x), int(self.y)), 10)
                pygame.draw.circle(surf, (200, 100, 255), (int(self.x), int(self.y)), 6)
                pygame.draw.circle(surf, (255, 200, 255), (int(self.x - 2), int(self.y - 2)), 3)

            elif self.proj_type == "fireball":
                # Draw fireball
                pygame.draw.circle(surf, (255, 100, 0), (int(self.x), int(self.y)), 12)
                pygame.draw.circle(surf, (255, 200, 50), (int(self.x), int(self.y)), 8)
                pygame.draw.circle(surf, (255, 255, 200), (int(self.x - 2), int(self.y - 2)), 4)


    ####################################################################################################################
    # BOMB CLASS
    ####################################################################################################################

    class Bomb:
        """A placed bomb that explodes after a timer."""
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.timer = 2000  # 2 seconds
            self.exploding = False
            self.explosion_timer = 300
            self.explosion_radius = TILE_SIZE * 1.5

        def update(self, dt):
            if self.exploding:
                self.explosion_timer -= dt
                return self.explosion_timer > 0
            else:
                self.timer -= dt
                if self.timer <= 0:
                    self.exploding = True
                return True

        def get_explosion_rect(self):
            return pygame.Rect(
                self.x - self.explosion_radius,
                self.y - self.explosion_radius,
                self.explosion_radius * 2,
                self.explosion_radius * 2
            )

        def draw(self, surf, time_ms):
            if self.exploding:
                # Draw explosion
                progress = 1 - (self.explosion_timer / 300)
                radius = int(self.explosion_radius * (0.5 + progress * 0.5))
                alpha = int(255 * (1 - progress))

                exp_surf = pygame.Surface((radius * 2 + 20, radius * 2 + 20), pygame.SRCALPHA)
                pygame.draw.circle(exp_surf, (255, 200, 50, alpha), (radius + 10, radius + 10), radius)
                pygame.draw.circle(exp_surf, (255, 100, 0, alpha), (radius + 10, radius + 10), int(radius * 0.7))
                pygame.draw.circle(exp_surf, (255, 255, 200, alpha), (radius + 10, radius + 10), int(radius * 0.3))
                surf.blit(exp_surf, (self.x - radius - 10, self.y - radius - 10))
            else:
                # Draw bomb
                flash = (self.timer < 500 and (time_ms // 100) % 2 == 0)
                color = (255, 100, 100) if flash else (40, 40, 50)

                pygame.draw.circle(surf, color, (int(self.x), int(self.y)), 16)
                pygame.draw.circle(surf, (70, 70, 80), (int(self.x - 4), int(self.y - 4)), 5)

                # Fuse
                fuse_progress = self.timer / 2000
                fuse_length = int(15 * fuse_progress)
                pygame.draw.line(surf, (139, 90, 43),
                               (self.x, self.y - 16),
                               (self.x + 5, self.y - 16 - fuse_length), 3)

                # Spark
                spark_size = 4 + int(2 * math.sin(time_ms * 0.02))
                pygame.draw.circle(surf, (255, 220, 50),
                                 (int(self.x + 5), int(self.y - 16 - fuse_length)), spark_size)


    ####################################################################################################################
    # PARTICLE EFFECT CLASS
    ####################################################################################################################

    class ParticleEffect:
        """Visual particle effect."""
        def __init__(self, x, y, effect_type="death"):
            self.x = x
            self.y = y
            self.effect_type = effect_type
            self.particles = []
            self.lifetime = 500

            if effect_type == "death":
                for _ in range(12):
                    angle = random.random() * math.pi * 2
                    speed = random.uniform(2, 5)
                    self.particles.append({
                        'x': x, 'y': y,
                        'vx': math.cos(angle) * speed,
                        'vy': math.sin(angle) * speed - 2,
                        'size': random.uniform(4, 10),
                        'color': random.choice([(100, 50, 130), (150, 80, 180), (200, 100, 150)])
                    })
            elif effect_type == "collect":
                for _ in range(8):
                    angle = random.random() * math.pi * 2
                    speed = random.uniform(1, 3)
                    self.particles.append({
                        'x': x, 'y': y,
                        'vx': math.cos(angle) * speed,
                        'vy': math.sin(angle) * speed - 3,
                        'size': random.uniform(3, 7),
                        'color': (255, 255, 100)
                    })
            elif effect_type == "hit":
                for _ in range(6):
                    angle = random.random() * math.pi * 2
                    speed = random.uniform(2, 4)
                    self.particles.append({
                        'x': x, 'y': y,
                        'vx': math.cos(angle) * speed,
                        'vy': math.sin(angle) * speed,
                        'size': random.uniform(3, 6),
                        'color': (255, 255, 255)
                    })

        def update(self, dt):
            self.lifetime -= dt
            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['vy'] += 0.15
            return self.lifetime > 0

        def draw(self, surf):
            alpha = int(255 * (self.lifetime / 500))
            for p in self.particles:
                size = p['size'] * (self.lifetime / 500)
                if size > 0:
                    ps = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
                    color = p['color']
                    if len(color) == 3:
                        color = (*color, alpha)
                    pygame.draw.circle(ps, color, (int(size + 2), int(size + 2)), int(size))
                    surf.blit(ps, (int(p['x'] - size), int(p['y'] - size)))


    ####################################################################################################################
    # PLAYER CLASS
    ####################################################################################################################

    class Player:
        """The player character with sword combat and inventory."""
        def __init__(self, x, y):
            self.tile_x = x
            self.tile_y = y
            self.x = x * TILE_SIZE + ROOM_OFFSET_X + TILE_SIZE // 2
            self.y = y * TILE_SIZE + ROOM_OFFSET_Y + TILE_SIZE // 2
            self.width = 40
            self.height = 40
            self.speed = 4

            # Health
            self.health = 3
            self.max_health = 3

            # Inventory
            self.keys = 0
            self.bombs = 3
            self.has_map = False
            self.has_compass = False

            # Combat
            self.facing = 'down'
            self.attacking = False
            self.attack_timer = 0
            self.attack_duration = 250
            self.attack_cooldown = 0
            self.invulnerable = 0

            # Animation
            self.anim_frame = 0
            self.anim_timer = 0
            self.moving = False

            # Bomb placement
            self.placing_bomb = False

        def update(self, dt, keys, room):
            # Update attack state
            if self.attacking:
                self.attack_timer += dt
                if self.attack_timer >= self.attack_duration:
                    self.attacking = False
                    self.attack_timer = 0

            if self.attack_cooldown > 0:
                self.attack_cooldown -= dt

            if self.invulnerable > 0:
                self.invulnerable -= dt

            # Movement (only if not attacking)
            if not self.attacking:
                dx, dy = 0, 0
                if keys[K_UP] or keys[K_w]:
                    dy = -self.speed
                    self.facing = 'up'
                elif keys[K_DOWN] or keys[K_s]:
                    dy = self.speed
                    self.facing = 'down'
                if keys[K_LEFT] or keys[K_a]:
                    dx = -self.speed
                    self.facing = 'left'
                elif keys[K_RIGHT] or keys[K_d]:
                    dx = self.speed
                    self.facing = 'right'

                self.moving = dx != 0 or dy != 0

                # Try horizontal movement
                if dx != 0:
                    new_x = self.x + dx
                    if self.can_move_to(new_x, self.y, room):
                        self.x = new_x

                # Try vertical movement
                if dy != 0:
                    new_y = self.y + dy
                    if self.can_move_to(self.x, new_y, room):
                        self.y = new_y

                # Update tile position
                self.tile_x = int((self.x - ROOM_OFFSET_X) // TILE_SIZE)
                self.tile_y = int((self.y - ROOM_OFFSET_Y) // TILE_SIZE)

            # Animation
            if self.moving:
                self.anim_timer += dt
                if self.anim_timer >= 150:
                    self.anim_timer = 0
                    self.anim_frame = (self.anim_frame + 1) % 4
            else:
                self.anim_frame = 0

        def can_move_to(self, new_x, new_y, room):
            """Check if player can move to pixel position."""
            # Check hitbox corners
            half_w = self.width // 2 - 4
            half_h = self.height // 2 - 4

            corners = [
                (new_x - half_w, new_y - half_h),
                (new_x + half_w, new_y - half_h),
                (new_x - half_w, new_y + half_h),
                (new_x + half_w, new_y + half_h),
            ]

            for cx, cy in corners:
                tile_x = int((cx - ROOM_OFFSET_X) // TILE_SIZE)
                tile_y = int((cy - ROOM_OFFSET_Y) // TILE_SIZE)

                if not room.is_walkable(tile_x, tile_y):
                    return False

            return True

        def attack(self):
            """Start sword attack."""
            if not self.attacking and self.attack_cooldown <= 0:
                self.attacking = True
                self.attack_timer = 0
                self.attack_cooldown = 150
                return True
            return False

        def place_bomb(self):
            """Place a bomb at current position."""
            if self.bombs > 0 and not self.placing_bomb:
                self.bombs -= 1
                self.placing_bomb = True
                return Bomb(self.x, self.y)
            return None

        def get_attack_rect(self):
            """Get the sword attack hitbox."""
            attack_range = 45
            attack_width = 50

            if self.facing == 'up':
                return pygame.Rect(self.x - attack_width // 2, self.y - attack_range - 10, attack_width, attack_range)
            elif self.facing == 'down':
                return pygame.Rect(self.x - attack_width // 2, self.y + 10, attack_width, attack_range)
            elif self.facing == 'left':
                return pygame.Rect(self.x - attack_range - 10, self.y - attack_width // 2, attack_range, attack_width)
            else:  # right
                return pygame.Rect(self.x + 10, self.y - attack_width // 2, attack_range, attack_width)

        def get_rect(self):
            """Get player collision rect."""
            return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

        def take_damage(self, amount=1):
            """Take damage if not invulnerable."""
            if self.invulnerable <= 0:
                self.health -= amount
                self.invulnerable = 1500  # 1.5 seconds of invulnerability
                return True
            return False

        def heal(self, amount=1):
            """Heal the player."""
            self.health = min(self.max_health, self.health + amount)

        def add_heart_container(self):
            """Add a heart container (increase max health)."""
            self.max_health += 1
            self.health = self.max_health

        def collect_item(self, item_type):
            """Collect an item."""
            if item_type == ITEM_KEY:
                self.keys += 1
            elif item_type == ITEM_BOMB:
                self.bombs += 3
            elif item_type == ITEM_HEART:
                self.heal(1)
            elif item_type == ITEM_HEART_CONTAINER:
                self.add_heart_container()
            elif item_type == ITEM_MAP:
                self.has_map = True
            elif item_type == ITEM_COMPASS:
                self.has_compass = True

        def use_key(self):
            """Use a key."""
            if self.keys > 0:
                self.keys -= 1
                return True
            return False

        def get_facing_tile(self):
            """Get the tile position the player is facing."""
            dx, dy = DIRECTIONS[self.facing]
            return (self.tile_x + dx, self.tile_y + dy)

        def check_room_exit(self, room):
            """Check if player is exiting the room through a door."""
            # Check each edge
            if self.y < ROOM_OFFSET_Y + TILE_SIZE and room.doors['north'] == 'open':
                return 'north'
            elif self.y > ROOM_OFFSET_Y + (ROOM_HEIGHT - 1) * TILE_SIZE - TILE_SIZE // 2 and room.doors['south'] == 'open':
                return 'south'
            elif self.x > ROOM_OFFSET_X + (ROOM_WIDTH - 1) * TILE_SIZE - TILE_SIZE // 2 and room.doors['east'] == 'open':
                return 'east'
            elif self.x < ROOM_OFFSET_X + TILE_SIZE and room.doors['west'] == 'open':
                return 'west'
            return None

        def enter_room_from(self, direction):
            """Position player entering from a direction."""
            if direction == 'north':
                self.x = ROOM_OFFSET_X + ROOM_WIDTH * TILE_SIZE // 2
                self.y = ROOM_OFFSET_Y + (ROOM_HEIGHT - 2) * TILE_SIZE
                self.facing = 'up'
            elif direction == 'south':
                self.x = ROOM_OFFSET_X + ROOM_WIDTH * TILE_SIZE // 2
                self.y = ROOM_OFFSET_Y + TILE_SIZE * 2
                self.facing = 'down'
            elif direction == 'east':
                self.x = ROOM_OFFSET_X + TILE_SIZE * 2
                self.y = ROOM_OFFSET_Y + ROOM_HEIGHT * TILE_SIZE // 2
                self.facing = 'right'
            elif direction == 'west':
                self.x = ROOM_OFFSET_X + (ROOM_WIDTH - 2) * TILE_SIZE
                self.y = ROOM_OFFSET_Y + ROOM_HEIGHT * TILE_SIZE // 2
                self.facing = 'left'

            self.tile_x = int((self.x - ROOM_OFFSET_X) // TILE_SIZE)
            self.tile_y = int((self.y - ROOM_OFFSET_Y) // TILE_SIZE)

        def draw(self, surf, time_ms):
            # Flash when invulnerable
            if self.invulnerable > 0 and (time_ms // 100) % 2 == 0:
                return

            # Player colors (green tunic like Link)
            tunic_color = (80, 160, 80)
            tunic_dark = (60, 120, 60)
            skin_color = (255, 210, 170)
            hair_color = (200, 150, 80)

            # Draw shadow
            shadow_surf = pygame.Surface((self.width + 10, 16), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 60), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x - self.width // 2 - 5, self.y + self.height // 2 - 8))

            # Body bob
            bob = 0
            if self.moving:
                bob = math.sin(time_ms * 0.015) * 2

            # Draw body
            body_y = self.y + bob

            # Tunic body
            pygame.draw.ellipse(surf, tunic_dark,
                              (self.x - 16, body_y - 8, 32, 28))
            pygame.draw.ellipse(surf, tunic_color,
                              (self.x - 14, body_y - 6, 28, 24))

            # Head
            pygame.draw.circle(surf, skin_color, (int(self.x), int(body_y - 18)), 14)

            # Hair (direction dependent)
            if self.facing == 'up':
                pygame.draw.ellipse(surf, hair_color, (self.x - 12, body_y - 32, 24, 16))
            elif self.facing == 'down':
                pygame.draw.ellipse(surf, hair_color, (self.x - 10, body_y - 30, 20, 12))
                # Eyes
                pygame.draw.circle(surf, (40, 40, 40), (int(self.x - 5), int(body_y - 18)), 3)
                pygame.draw.circle(surf, (40, 40, 40), (int(self.x + 5), int(body_y - 18)), 3)
            elif self.facing == 'left':
                pygame.draw.ellipse(surf, hair_color, (self.x - 14, body_y - 30, 18, 14))
                pygame.draw.circle(surf, (40, 40, 40), (int(self.x - 6), int(body_y - 18)), 3)
            else:  # right
                pygame.draw.ellipse(surf, hair_color, (self.x - 4, body_y - 30, 18, 14))
                pygame.draw.circle(surf, (40, 40, 40), (int(self.x + 6), int(body_y - 18)), 3)

            # Draw sword attack
            if self.attacking:
                self.draw_attack(surf, time_ms)

        def draw_attack(self, surf, time_ms):
            """Draw sword swing effect."""
            progress = self.attack_timer / self.attack_duration
            swing_length = 40

            # Sword colors
            blade_color = (200, 210, 220)
            hilt_color = (139, 90, 43)

            if self.facing == 'up':
                # Swing from right to left above player
                angle = math.radians(180 + (1 - progress) * 180)
                sx = self.x + math.cos(angle) * swing_length
                sy = self.y - 20 + math.sin(angle) * swing_length * 0.5
            elif self.facing == 'down':
                # Swing from left to right below player
                angle = math.radians((1 - progress) * 180)
                sx = self.x + math.cos(angle) * swing_length
                sy = self.y + 10 + math.sin(angle) * swing_length * 0.5
            elif self.facing == 'left':
                # Swing from top to bottom on left
                angle = math.radians(90 + (1 - progress) * 180)
                sx = self.x - 20 + math.cos(angle) * swing_length * 0.5
                sy = self.y + math.sin(angle) * swing_length
            else:  # right
                angle = math.radians(-90 + (1 - progress) * 180)
                sx = self.x + 20 + math.cos(angle) * swing_length * 0.5
                sy = self.y + math.sin(angle) * swing_length

            # Draw sword
            pygame.draw.line(surf, hilt_color, (self.x, self.y), (self.x + (sx - self.x) * 0.3, self.y + (sy - self.y) * 0.3), 6)
            pygame.draw.line(surf, blade_color, (self.x + (sx - self.x) * 0.3, self.y + (sy - self.y) * 0.3), (sx, sy), 4)

            # Sparkle at tip
            if progress > 0.3 and progress < 0.7:
                spark_size = 5
                pygame.draw.circle(surf, (255, 255, 200), (int(sx), int(sy)), spark_size)


    ####################################################################################################################
    # ENEMY BASE CLASS
    ####################################################################################################################

    class Enemy:
        """Base class for all enemies."""
        def __init__(self, x, y):
            self.tile_x = x
            self.tile_y = y
            self.x = x * TILE_SIZE + ROOM_OFFSET_X + TILE_SIZE // 2
            self.y = y * TILE_SIZE + ROOM_OFFSET_Y + TILE_SIZE // 2
            self.width = 40
            self.height = 40
            self.speed = 1.5
            self.health = 2
            self.damage = 1
            self.alive = True
            self.hit_flash = 0
            self.anim_phase = random.random() * math.pi * 2
            self.direction = random.choice(['up', 'down', 'left', 'right'])
            self.move_timer = 0
            self.move_duration = random.randint(500, 1500)

        def update(self, dt, room, player):
            if not self.alive:
                return

            self.anim_phase += dt * 0.005
            if self.hit_flash > 0:
                self.hit_flash -= dt

            self.move_timer += dt
            if self.move_timer >= self.move_duration:
                self.move_timer = 0
                self.move_duration = random.randint(500, 1500)
                self.direction = random.choice(['up', 'down', 'left', 'right'])

        def can_move_to(self, new_x, new_y, room):
            """Check if enemy can move to pixel position."""
            half_w = self.width // 2 - 4
            half_h = self.height // 2 - 4

            corners = [
                (new_x - half_w, new_y - half_h),
                (new_x + half_w, new_y - half_h),
                (new_x - half_w, new_y + half_h),
                (new_x + half_w, new_y + half_h),
            ]

            for cx, cy in corners:
                tile_x = int((cx - ROOM_OFFSET_X) // TILE_SIZE)
                tile_y = int((cy - ROOM_OFFSET_Y) // TILE_SIZE)

                if tile_x < 1 or tile_x >= ROOM_WIDTH - 1 or tile_y < 1 or tile_y >= ROOM_HEIGHT - 1:
                    return False
                if room.tiles[tile_y][tile_x] in [TILE_WALL, TILE_PIT, TILE_BLOCK]:
                    return False

            return True

        def get_rect(self):
            return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

        def take_damage(self, amount=1):
            self.health -= amount
            self.hit_flash = 150
            if self.health <= 0:
                self.alive = False
                return True
            return False

        def draw(self, surf, time_ms):
            pass


    ####################################################################################################################
    # SLIME ENEMY
    ####################################################################################################################

    class Slime(Enemy):
        """A bouncing slime enemy."""
        def __init__(self, x, y):
            super().__init__(x, y)
            self.health = 1
            self.speed = 1.0
            self.color = random.choice([(50, 180, 50), (50, 50, 180), (180, 50, 50)])

        def update(self, dt, room, player):
            super().update(dt, room, player)
            if not self.alive:
                return

            # Simple random movement
            dx, dy = DIRECTIONS[self.direction]
            new_x = self.x + dx * self.speed
            new_y = self.y + dy * self.speed

            if self.can_move_to(new_x, new_y, room):
                self.x = new_x
                self.y = new_y
            else:
                self.direction = random.choice(['up', 'down', 'left', 'right'])

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            # Flash when hit
            if self.hit_flash > 0:
                color = (255, 255, 255)
            else:
                color = self.color

            # Bouncing animation
            bounce = abs(math.sin(self.anim_phase * 2)) * 8
            squash = 1 + math.sin(self.anim_phase * 2) * 0.2

            # Shadow
            shadow_surf = pygame.Surface((self.width, 12), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x - self.width // 2, self.y + self.height // 2 - 6))

            # Body
            body_width = int(self.width * squash)
            body_height = int(self.height / squash)
            pygame.draw.ellipse(surf, color,
                              (self.x - body_width // 2, self.y - body_height // 2 - bounce,
                               body_width, body_height))

            # Darker outline
            dark_color = (color[0] * 0.6, color[1] * 0.6, color[2] * 0.6)
            pygame.draw.ellipse(surf, dark_color,
                              (self.x - body_width // 2, self.y - body_height // 2 - bounce,
                               body_width, body_height), 2)

            # Eyes
            eye_y = self.y - bounce - 5
            pygame.draw.circle(surf, (255, 255, 255), (int(self.x - 8), int(eye_y)), 6)
            pygame.draw.circle(surf, (255, 255, 255), (int(self.x + 8), int(eye_y)), 6)
            pygame.draw.circle(surf, (0, 0, 0), (int(self.x - 8), int(eye_y + 2)), 3)
            pygame.draw.circle(surf, (0, 0, 0), (int(self.x + 8), int(eye_y + 2)), 3)


    ####################################################################################################################
    # BAT ENEMY
    ####################################################################################################################

    class Bat(Enemy):
        """A flying bat that moves erratically."""
        def __init__(self, x, y):
            super().__init__(x, y)
            self.health = 1
            self.speed = 2.5
            self.wing_phase = random.random() * math.pi * 2
            self.target_x = self.x
            self.target_y = self.y

        def update(self, dt, room, player):
            super().update(dt, room, player)
            if not self.alive:
                return

            self.wing_phase += dt * 0.02

            # Occasionally target player
            if random.random() < 0.02:
                self.target_x = player.x + random.randint(-100, 100)
                self.target_y = player.y + random.randint(-100, 100)

            # Move toward target
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            dist = math.sqrt(dx * dx + dy * dy)

            if dist > 10:
                move_x = (dx / dist) * self.speed
                move_y = (dy / dist) * self.speed

                new_x = self.x + move_x
                new_y = self.y + move_y

                if self.can_move_to(new_x, new_y, room):
                    self.x = new_x
                    self.y = new_y
                else:
                    self.target_x = self.x + random.randint(-100, 100)
                    self.target_y = self.y + random.randint(-100, 100)
            else:
                # Pick new target
                self.target_x = self.x + random.randint(-150, 150)
                self.target_y = self.y + random.randint(-150, 150)

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            if self.hit_flash > 0:
                color = (255, 255, 255)
            else:
                color = (80, 60, 100)

            # Wing flap
            wing_angle = math.sin(self.wing_phase) * 0.5

            # Body
            pygame.draw.ellipse(surf, color, (self.x - 12, self.y - 8, 24, 16))

            # Wings
            wing_y = self.y + math.sin(self.wing_phase) * 8
            # Left wing
            pygame.draw.ellipse(surf, color, (self.x - 28, wing_y - 6, 20, 12))
            # Right wing
            pygame.draw.ellipse(surf, color, (self.x + 8, wing_y - 6, 20, 12))

            # Eyes (red)
            pygame.draw.circle(surf, (255, 50, 50), (int(self.x - 5), int(self.y - 2)), 4)
            pygame.draw.circle(surf, (255, 50, 50), (int(self.x + 5), int(self.y - 2)), 4)
            pygame.draw.circle(surf, (255, 200, 200), (int(self.x - 5), int(self.y - 3)), 2)
            pygame.draw.circle(surf, (255, 200, 200), (int(self.x + 5), int(self.y - 3)), 2)


    ####################################################################################################################
    # SKELETON ENEMY
    ####################################################################################################################

    class Skeleton(Enemy):
        """A skeleton that patrols and chases the player."""
        def __init__(self, x, y):
            super().__init__(x, y)
            self.health = 3
            self.speed = 1.2
            self.chase_range = 200
            self.chasing = False

        def update(self, dt, room, player):
            super().update(dt, room, player)
            if not self.alive:
                return

            # Check if player in range
            dx = player.x - self.x
            dy = player.y - self.y
            dist = math.sqrt(dx * dx + dy * dy)

            if dist < self.chase_range:
                self.chasing = True
                # Move toward player
                if dist > 0:
                    move_x = (dx / dist) * self.speed
                    move_y = (dy / dist) * self.speed

                    new_x = self.x + move_x
                    new_y = self.y + move_y

                    if self.can_move_to(new_x, new_y, room):
                        self.x = new_x
                        self.y = new_y
            else:
                self.chasing = False
                # Patrol
                dir_dx, dir_dy = DIRECTIONS[self.direction]
                new_x = self.x + dir_dx * self.speed * 0.5
                new_y = self.y + dir_dy * self.speed * 0.5

                if self.can_move_to(new_x, new_y, room):
                    self.x = new_x
                    self.y = new_y
                else:
                    self.direction = random.choice(['up', 'down', 'left', 'right'])

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            if self.hit_flash > 0:
                color = (255, 255, 255)
            else:
                color = (220, 220, 200)

            dark_color = (180, 180, 160)

            # Walk animation
            walk_offset = math.sin(self.anim_phase * 3) * 3 if self.chasing else 0

            # Shadow
            shadow_surf = pygame.Surface((self.width, 12), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x - self.width // 2, self.y + self.height // 2 - 6))

            # Legs
            leg_spread = 8 + abs(walk_offset)
            pygame.draw.line(surf, dark_color, (self.x - 5, self.y + 5), (self.x - leg_spread, self.y + 20), 4)
            pygame.draw.line(surf, dark_color, (self.x + 5, self.y + 5), (self.x + leg_spread, self.y + 20), 4)

            # Ribcage/body
            pygame.draw.ellipse(surf, color, (self.x - 14, self.y - 10, 28, 20))
            for i in range(3):
                rib_y = self.y - 5 + i * 6
                pygame.draw.line(surf, dark_color, (self.x - 10, rib_y), (self.x + 10, rib_y), 2)

            # Arms
            arm_swing = walk_offset * 0.5
            pygame.draw.line(surf, dark_color, (self.x - 14, self.y - 5), (self.x - 25, self.y + 5 + arm_swing), 3)
            pygame.draw.line(surf, dark_color, (self.x + 14, self.y - 5), (self.x + 25, self.y + 5 - arm_swing), 3)

            # Skull
            pygame.draw.circle(surf, color, (int(self.x), int(self.y - 20)), 14)

            # Eye sockets
            pygame.draw.circle(surf, (40, 40, 40), (int(self.x - 5), int(self.y - 22)), 5)
            pygame.draw.circle(surf, (40, 40, 40), (int(self.x + 5), int(self.y - 22)), 5)

            # Glowing eyes when chasing
            if self.chasing:
                pygame.draw.circle(surf, (255, 50, 50), (int(self.x - 5), int(self.y - 22)), 3)
                pygame.draw.circle(surf, (255, 50, 50), (int(self.x + 5), int(self.y - 22)), 3)

            # Jaw
            pygame.draw.ellipse(surf, color, (self.x - 8, self.y - 14, 16, 8))


    ####################################################################################################################
    # ARCHER ENEMY
    ####################################################################################################################

    class Archer(Enemy):
        """A skeleton archer that shoots arrows."""
        def __init__(self, x, y):
            super().__init__(x, y)
            self.health = 2
            self.speed = 0.8
            self.shoot_range = 300
            self.shoot_cooldown = 0
            self.shoot_delay = 2000

        def update(self, dt, room, player):
            super().update(dt, room, player)
            if not self.alive:
                return

            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= dt

            # Check if player in range
            dx = player.x - self.x
            dy = player.y - self.y
            dist = math.sqrt(dx * dx + dy * dy)

            if dist < self.shoot_range and self.shoot_cooldown <= 0:
                # Shoot at player
                if dist > 0:
                    proj_dx = dx / dist
                    proj_dy = dy / dist
                    proj = Projectile(self.x, self.y, proj_dx, proj_dy, "arrow", 1, False)
                    room.projectiles.append(proj)
                    self.shoot_cooldown = self.shoot_delay

                    # Face player
                    if abs(dx) > abs(dy):
                        self.direction = 'right' if dx > 0 else 'left'
                    else:
                        self.direction = 'down' if dy > 0 else 'up'
            else:
                # Keep distance from player
                if dist < 150:
                    # Move away
                    if dist > 0:
                        move_x = -(dx / dist) * self.speed
                        move_y = -(dy / dist) * self.speed
                        new_x = self.x + move_x
                        new_y = self.y + move_y

                        if self.can_move_to(new_x, new_y, room):
                            self.x = new_x
                            self.y = new_y

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            if self.hit_flash > 0:
                color = (255, 255, 255)
            else:
                color = (200, 200, 180)

            dark_color = (160, 160, 140)

            # Shadow
            shadow_surf = pygame.Surface((self.width, 12), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x - self.width // 2, self.y + self.height // 2 - 6))

            # Legs
            pygame.draw.line(surf, dark_color, (self.x - 5, self.y + 5), (self.x - 8, self.y + 20), 3)
            pygame.draw.line(surf, dark_color, (self.x + 5, self.y + 5), (self.x + 8, self.y + 20), 3)

            # Body
            pygame.draw.ellipse(surf, color, (self.x - 12, self.y - 8, 24, 18))

            # Hood/cloak
            pygame.draw.ellipse(surf, (80, 60, 50), (self.x - 16, self.y - 25, 32, 25))

            # Skull face in hood
            pygame.draw.circle(surf, color, (int(self.x), int(self.y - 18)), 10)
            pygame.draw.circle(surf, (40, 40, 40), (int(self.x - 4), int(self.y - 19)), 3)
            pygame.draw.circle(surf, (40, 40, 40), (int(self.x + 4), int(self.y - 19)), 3)

            # Bow
            bow_color = (139, 90, 43)
            # Draw bow as arc using lines
            bow_points = []
            for i in range(10):
                angle = -math.pi/2 + (i / 9) * math.pi
                bx = self.x + 20 + math.cos(angle) * 5
                by = self.y - 5 + math.sin(angle) * 20
                bow_points.append((bx, by))
            if len(bow_points) >= 2:
                for i in range(len(bow_points) - 1):
                    pygame.draw.line(surf, bow_color, bow_points[i], bow_points[i + 1], 3)

            # Bowstring
            pygame.draw.line(surf, (200, 200, 200), bow_points[0], bow_points[-1], 1)


    ####################################################################################################################
    # BOSS CLASS
    ####################################################################################################################

    class Boss(Enemy):
        """The dungeon boss with multiple attack phases."""
        def __init__(self, x, y):
            super().__init__(x, y)
            self.health = 15
            self.max_health = 15
            self.width = 80
            self.height = 80
            self.speed = 1.5
            self.damage = 2

            # Boss phases
            self.phase = 1  # 1, 2, 3
            self.phase_health_thresholds = [10, 5]  # Phase 2 at 10hp, Phase 3 at 5hp

            # Attack patterns
            self.attack_state = "idle"  # idle, charging, attacking, recovering
            self.attack_timer = 0
            self.attack_cooldown = 2000
            self.current_cooldown = 2000

            # Charge attack
            self.charge_target_x = 0
            self.charge_target_y = 0
            self.charge_speed = 8

            # Projectile attack
            self.projectile_count = 4

            # Summon attack
            self.can_summon = False
            self.summon_cooldown = 0

            self.invulnerable_timer = 0
            self.intro_complete = False

        def update(self, dt, room, player):
            if not self.alive:
                return

            self.anim_phase += dt * 0.003
            if self.hit_flash > 0:
                self.hit_flash -= dt

            if self.invulnerable_timer > 0:
                self.invulnerable_timer -= dt

            # Update phase based on health
            if self.health <= self.phase_health_thresholds[1] and self.phase < 3:
                self.phase = 3
                self.can_summon = True
                self.invulnerable_timer = 1000  # Brief invulnerability on phase change
            elif self.health <= self.phase_health_thresholds[0] and self.phase < 2:
                self.phase = 2
                self.projectile_count = 6
                self.invulnerable_timer = 1000

            # Attack state machine
            if self.attack_state == "idle":
                self.attack_timer += dt
                if self.attack_timer >= self.current_cooldown:
                    self.start_attack(player, room)

            elif self.attack_state == "charging":
                self.attack_timer += dt
                if self.attack_timer >= 500:
                    self.attack_state = "attacking"
                    self.attack_timer = 0

            elif self.attack_state == "attacking":
                self.execute_attack(dt, player, room)

            elif self.attack_state == "recovering":
                self.attack_timer += dt
                if self.attack_timer >= 1000:
                    self.attack_state = "idle"
                    self.attack_timer = 0
                    self.current_cooldown = max(1000, self.attack_cooldown - self.phase * 300)

            # Summon cooldown
            if self.summon_cooldown > 0:
                self.summon_cooldown -= dt

        def start_attack(self, player, room):
            """Choose and start an attack."""
            self.attack_timer = 0

            # Choose attack based on phase
            if self.phase == 1:
                attack = random.choice(["charge", "projectile"])
            elif self.phase == 2:
                attack = random.choice(["charge", "projectile", "projectile"])
            else:
                attack = random.choice(["charge", "projectile", "summon"])

            if attack == "charge":
                self.attack_type = "charge"
                self.charge_target_x = player.x
                self.charge_target_y = player.y
                self.attack_state = "charging"

            elif attack == "projectile":
                self.attack_type = "projectile"
                self.attack_state = "charging"

            elif attack == "summon" and self.can_summon and self.summon_cooldown <= 0:
                self.attack_type = "summon"
                self.attack_state = "charging"
            else:
                # Default to projectile if summon on cooldown
                self.attack_type = "projectile"
                self.attack_state = "charging"

        def execute_attack(self, dt, player, room):
            """Execute the current attack."""
            if self.attack_type == "charge":
                # Charge toward target
                dx = self.charge_target_x - self.x
                dy = self.charge_target_y - self.y
                dist = math.sqrt(dx * dx + dy * dy)

                if dist > 20:
                    self.x += (dx / dist) * self.charge_speed
                    self.y += (dy / dist) * self.charge_speed
                else:
                    self.attack_state = "recovering"
                    self.attack_timer = 0

            elif self.attack_type == "projectile":
                # Fire projectiles in a circle
                for i in range(self.projectile_count):
                    angle = (i / self.projectile_count) * math.pi * 2
                    proj_dx = math.cos(angle)
                    proj_dy = math.sin(angle)
                    proj = Projectile(self.x, self.y, proj_dx, proj_dy, "fireball", 1, False)
                    proj.speed = 3
                    room.projectiles.append(proj)

                self.attack_state = "recovering"
                self.attack_timer = 0

            elif self.attack_type == "summon":
                # Summon minions
                for _ in range(2):
                    spawn_x = random.randint(3, ROOM_WIDTH - 4)
                    spawn_y = random.randint(3, ROOM_HEIGHT - 4)
                    if random.random() < 0.5:
                        room.enemies.append(Slime(spawn_x, spawn_y))
                    else:
                        room.enemies.append(Bat(spawn_x, spawn_y))

                self.summon_cooldown = 8000
                self.attack_state = "recovering"
                self.attack_timer = 0

        def take_damage(self, amount=1):
            if self.invulnerable_timer > 0:
                return False

            self.health -= amount
            self.hit_flash = 200

            if self.health <= 0:
                self.alive = False
                return True
            return False

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            # Flash when hit
            if self.hit_flash > 0:
                body_color = (255, 255, 255)
                eye_color = (255, 255, 255)
            else:
                # Color based on phase
                if self.phase == 1:
                    body_color = (60, 40, 80)
                    eye_color = (200, 50, 50)
                elif self.phase == 2:
                    body_color = (80, 40, 60)
                    eye_color = (255, 100, 50)
                else:
                    body_color = (100, 30, 30)
                    eye_color = (255, 200, 50)

            # Shadow
            shadow_surf = pygame.Surface((self.width + 20, 20), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 80), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x - self.width // 2 - 10, self.y + self.height // 2))

            # Aura when charging
            if self.attack_state == "charging":
                aura_size = 60 + int(math.sin(time_ms * 0.02) * 10)
                aura_surf = pygame.Surface((aura_size * 2, aura_size * 2), pygame.SRCALPHA)
                pygame.draw.circle(aura_surf, (*eye_color, 50), (aura_size, aura_size), aura_size)
                surf.blit(aura_surf, (self.x - aura_size, self.y - aura_size))

            # Body - large shadowy mass
            bob = math.sin(self.anim_phase) * 5

            # Main body
            pygame.draw.ellipse(surf, body_color,
                              (self.x - self.width // 2, self.y - self.height // 2 + bob,
                               self.width, self.height))

            # Darker inner
            inner_color = (body_color[0] * 0.6, body_color[1] * 0.6, body_color[2] * 0.6)
            pygame.draw.ellipse(surf, inner_color,
                              (self.x - self.width // 2 + 10, self.y - self.height // 2 + bob + 10,
                               self.width - 20, self.height - 20))

            # Spiky protrusions
            num_spikes = 6 + self.phase * 2
            for i in range(num_spikes):
                angle = (i / num_spikes) * math.pi * 2 + self.anim_phase * 0.5
                spike_len = 20 + math.sin(angle * 3 + time_ms * 0.005) * 8
                sx = self.x + math.cos(angle) * (self.width // 2)
                sy = self.y + bob + math.sin(angle) * (self.height // 2)
                ex = self.x + math.cos(angle) * (self.width // 2 + spike_len)
                ey = self.y + bob + math.sin(angle) * (self.height // 2 + spike_len)
                pygame.draw.line(surf, body_color, (sx, sy), (ex, ey), 6)

            # Eyes
            eye_size = 12 + self.phase * 2
            # Main eye
            pygame.draw.circle(surf, eye_color, (int(self.x), int(self.y + bob - 10)), eye_size)
            pygame.draw.circle(surf, (255, 255, 200), (int(self.x), int(self.y + bob - 10)), eye_size // 2)

            # Additional eyes in later phases
            if self.phase >= 2:
                pygame.draw.circle(surf, eye_color, (int(self.x - 25), int(self.y + bob)), 8)
                pygame.draw.circle(surf, eye_color, (int(self.x + 25), int(self.y + bob)), 8)

            if self.phase >= 3:
                pygame.draw.circle(surf, eye_color, (int(self.x - 15), int(self.y + bob + 15)), 6)
                pygame.draw.circle(surf, eye_color, (int(self.x + 15), int(self.y + bob + 15)), 6)

            # Health bar
            bar_width = 100
            bar_height = 8
            bar_x = self.x - bar_width // 2
            bar_y = self.y - self.height // 2 - 20

            pygame.draw.rect(surf, (40, 40, 40), (bar_x - 2, bar_y - 2, bar_width + 4, bar_height + 4))
            pygame.draw.rect(surf, (80, 20, 20), (bar_x, bar_y, bar_width, bar_height))

            health_width = int((self.health / self.max_health) * bar_width)
            pygame.draw.rect(surf, (200, 50, 50), (bar_x, bar_y, health_width, bar_height))


    ####################################################################################################################
    # DUNGEON GENERATOR
    ####################################################################################################################

    class DungeonGenerator:
        """Generates the dungeon layout with rooms."""

        @staticmethod
        def create_dungeon():
            """Create a dungeon with connected rooms."""
            rooms = {}

            # Create a 3x3 grid of rooms + boss room
            # Layout:
            #   [0,0] - [1,0] - [2,0]
            #     |       |       |
            #   [0,1] - [1,1] - [2,1]
            #     |       |       |
            #   [0,2] - [1,2] - [2,2]
            #             |
            #          [BOSS]

            # Room types
            room_layout = {
                (1, 2): "entrance",     # Start room (bottom center)
                (0, 2): "normal",       # Has slimes
                (2, 2): "key_room",     # Has key
                (0, 1): "puzzle",       # Block puzzle
                (1, 1): "normal",       # Central room
                (2, 1): "treasure",     # Bombs chest
                (0, 0): "normal",       # Has archers
                (1, 0): "key_room",     # Boss key
                (2, 0): "normal",       # Has skeletons
                (1, -1): "boss",        # Boss room (north of center top)
            }

            for pos, room_type in room_layout.items():
                room_id = f"{pos[0]}_{pos[1]}"
                room = Room(room_id, room_type)

                # Set up connections and doors
                x, y = pos

                # North connection
                if (x, y - 1) in room_layout:
                    room.connections['north'] = f"{x}_{y-1}"
                    # Boss room requires boss key
                    if room_layout[(x, y - 1)] == "boss":
                        room.set_door('north', 'locked')
                    else:
                        room.set_door('north', 'open')

                # South connection
                if (x, y + 1) in room_layout:
                    room.connections['south'] = f"{x}_{y+1}"
                    room.set_door('south', 'open')

                # East connection
                if (x + 1, y) in room_layout:
                    room.connections['east'] = f"{x+1}_{y}"
                    # Key room (2,2) has locked door from (1,2)
                    if pos == (1, 2) and room_layout.get((x + 1, y)) == "key_room":
                        room.set_door('east', 'locked')
                    else:
                        room.set_door('east', 'open')

                # West connection
                if (x - 1, y) in room_layout:
                    room.connections['west'] = f"{x-1}_{y}"
                    room.set_door('west', 'open')

                # Add room-specific content
                DungeonGenerator._populate_room(room, room_type)

                rooms[room_id] = room

            return rooms

        @staticmethod
        def _populate_room(room, room_type):
            """Add enemies, items, and obstacles to a room."""

            if room_type == "entrance":
                # Starting room - just a few weak enemies
                room.enemies = [
                    Slime(4, 4),
                    Slime(11, 4),
                ]
                # Add some inner walls for cover
                room.add_obstacle(6, 3, TILE_WALL)
                room.add_obstacle(9, 3, TILE_WALL)

            elif room_type == "normal":
                # Random enemies based on room position
                room_id = room.room_id
                if room_id == "0_2":
                    room.enemies = [
                        Slime(3, 3), Slime(5, 5), Slime(10, 3),
                    ]
                elif room_id == "1_1":
                    room.enemies = [
                        Skeleton(4, 4), Bat(10, 3), Slime(7, 6),
                    ]
                    room.add_obstacle(7, 4, TILE_WALL)
                    room.add_obstacle(8, 4, TILE_WALL)
                elif room_id == "0_0":
                    room.enemies = [
                        Archer(3, 3), Archer(12, 3),
                    ]
                    # Cover walls
                    room.add_obstacle(5, 5, TILE_WALL)
                    room.add_obstacle(10, 5, TILE_WALL)
                elif room_id == "2_0":
                    room.enemies = [
                        Skeleton(4, 4), Skeleton(11, 4), Bat(7, 3),
                    ]

            elif room_type == "key_room":
                room_id = room.room_id
                if room_id == "2_2":
                    # First key room - guarded by enemies
                    room.enemies = [
                        Skeleton(4, 4), Slime(10, 5),
                    ]
                    room.items = [CollectibleItem(7, 5, ITEM_KEY)]
                elif room_id == "1_0":
                    # Boss key room - harder enemies
                    room.enemies = [
                        Archer(3, 3), Skeleton(11, 4), Bat(7, 2),
                    ]
                    room.items = [CollectibleItem(7, 5, ITEM_KEY)]
                    room.add_obstacle(6, 4, TILE_WALL)
                    room.add_obstacle(8, 4, TILE_WALL)

            elif room_type == "puzzle":
                # Block puzzle room
                room.add_switch(7, 7, 'north')  # Switch opens north door
                room.add_pushable_block(7, 4, 7, 7)  # Block needs to go on switch
                room.doors['north'] = 'locked'  # Door starts locked
                # Enemies appear after puzzle
                room.enemies = [Bat(3, 3), Bat(12, 3)]

            elif room_type == "treasure":
                # Treasure room with chest
                room.add_chest(7, 5, ITEM_BOMB)
                room.enemies = [
                    Slime(3, 4), Slime(11, 4),
                ]
                room.add_obstacle(5, 3, TILE_WALL)
                room.add_obstacle(6, 3, TILE_WALL)
                room.add_obstacle(8, 3, TILE_WALL)
                room.add_obstacle(9, 3, TILE_WALL)

            elif room_type == "boss":
                # Boss room
                room.enemies = [Boss(7, 4)]
                room.items = [CollectibleItem(7, 7, ITEM_HEART_CONTAINER)]
                # Clear floor for boss fight
                pass


    ####################################################################################################################
    # MAIN GAME CONTROLLER
    ####################################################################################################################

    class BeaconQuestGame:
        """Main game controller for Zelda-style dungeon adventure."""

        def __init__(self):
            self.state = STATE_PLAYING

            # Create dungeon
            self.rooms = DungeonGenerator.create_dungeon()
            self.current_room_id = "1_2"  # Start in entrance

            # Create player
            self.player = Player(7, 7)

            # Effects and objects
            self.effects = []
            self.bombs = []

            # Room transition
            self.transition_direction = None
            self.transition_progress = 0
            self.transition_speed = 0.003

            # Camera shake
            self.shake_amount = 0
            self.shake_timer = 0

            # Boss defeated flag
            self.boss_defeated = False

            # Mark starting room as visited
            self.current_room.visited = True

        @property
        def current_room(self):
            return self.rooms[self.current_room_id]

        def trigger_shake(self, amount=5):
            self.shake_amount = amount
            self.shake_timer = 200

        def update(self, dt):
            if self.state == STATE_TRANSITION:
                self._update_transition(dt)
                return

            if self.state != STATE_PLAYING:
                return

            time_ms = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()
            room = self.current_room

            # Update player
            self.player.update(dt, keys, room)
            self.player.placing_bomb = False

            # Check for room exit
            exit_dir = self.player.check_room_exit(room)
            if exit_dir and room.connections[exit_dir]:
                self._start_transition(exit_dir)
                return

            # Update enemies
            for enemy in room.enemies:
                enemy.update(dt, room, self.player)

            # Check player attack vs enemies
            if self.player.attacking:
                attack_rect = self.player.get_attack_rect()
                for enemy in room.enemies:
                    if enemy.alive and attack_rect.colliderect(enemy.get_rect()):
                        if enemy.take_damage():
                            # Enemy died
                            self.effects.append(ParticleEffect(enemy.x, enemy.y, "death"))
                            self.trigger_shake(8)
                            # Drop item chance
                            if random.random() < 0.3 and not isinstance(enemy, Boss):
                                drop = random.choice([ITEM_HEART, ITEM_BOMB, None, None])
                                if drop:
                                    item = CollectibleItem(
                                        int((enemy.x - ROOM_OFFSET_X) // TILE_SIZE),
                                        int((enemy.y - ROOM_OFFSET_Y) // TILE_SIZE),
                                        drop
                                    )
                                    room.items.append(item)

                            # Boss defeated
                            if isinstance(enemy, Boss):
                                self.boss_defeated = True

            # Check enemy vs player collision
            player_rect = self.player.get_rect()
            for enemy in room.enemies:
                if enemy.alive and player_rect.colliderect(enemy.get_rect()):
                    if self.player.take_damage(enemy.damage):
                        self.trigger_shake(10)
                        self.effects.append(ParticleEffect(self.player.x, self.player.y, "hit"))

            # Update projectiles
            for proj in room.projectiles:
                proj.update(dt, room)

                # Check projectile vs player
                if not proj.from_player and proj.alive:
                    if player_rect.colliderect(proj.get_rect()):
                        if self.player.take_damage(proj.damage):
                            self.trigger_shake(6)
                            self.effects.append(ParticleEffect(self.player.x, self.player.y, "hit"))
                        proj.alive = False

            room.projectiles = [p for p in room.projectiles if p.alive]

            # Update items
            for item in room.items:
                item.update(dt)
                if not item.collected and player_rect.colliderect(item.get_rect()):
                    item.collected = True
                    self.player.collect_item(item.item_type)
                    self.effects.append(ParticleEffect(item.x * TILE_SIZE + ROOM_OFFSET_X + 32,
                                                       item.y * TILE_SIZE + ROOM_OFFSET_Y + 32, "collect"))

            # Update bombs
            for bomb in self.bombs:
                if not bomb.update(dt):
                    # Bomb exploded - check damage
                    exp_rect = bomb.get_explosion_rect()

                    # Damage enemies
                    for enemy in room.enemies:
                        if enemy.alive and exp_rect.colliderect(enemy.get_rect()):
                            enemy.take_damage(3)
                            if not enemy.alive:
                                self.effects.append(ParticleEffect(enemy.x, enemy.y, "death"))

                    # Damage player
                    if exp_rect.colliderect(player_rect):
                        self.player.take_damage(1)
                        self.trigger_shake(8)

                    # Check for cracked walls
                    for direction in ['north', 'south', 'east', 'west']:
                        if room.doors[direction] == 'cracked':
                            room.destroy_wall(direction)
                            self.trigger_shake(10)

                    self.bombs.remove(bomb)

            # Update block pushing
            self._update_blocks(room)

            # Update switches
            self._update_switches(room)

            # Check chest interaction
            if room.chest and not room.chest['opened']:
                chest_rect = pygame.Rect(
                    room.chest['x'] * TILE_SIZE + ROOM_OFFSET_X,
                    room.chest['y'] * TILE_SIZE + ROOM_OFFSET_Y,
                    TILE_SIZE, TILE_SIZE
                )
                if player_rect.colliderect(chest_rect):
                    room.chest['opened'] = True
                    room.tiles[room.chest['y']][room.chest['x']] = TILE_CHEST_OPEN
                    self.player.collect_item(room.chest_contents)
                    self.effects.append(ParticleEffect(
                        room.chest['x'] * TILE_SIZE + ROOM_OFFSET_X + 32,
                        room.chest['y'] * TILE_SIZE + ROOM_OFFSET_Y + 32, "collect"))

            # Update effects
            self.effects = [e for e in self.effects if e.update(dt)]

            # Update shake
            if self.shake_timer > 0:
                self.shake_timer -= dt
                self.shake_amount *= 0.9
            else:
                self.shake_amount = 0

            # Check win/lose
            if self.boss_defeated and not any(e.alive for e in room.enemies):
                self.state = STATE_VICTORY
            elif self.player.health <= 0:
                self.state = STATE_GAMEOVER

        def _update_blocks(self, room):
            """Update pushable block logic."""
            if not room.blocks:
                return

            facing_x, facing_y = self.player.get_facing_tile()

            for block in room.blocks:
                if block['x'] == facing_x and block['y'] == facing_y:
                    # Player facing block - check if pushing
                    dx, dy = DIRECTIONS[self.player.facing]
                    new_x = block['x'] + dx
                    new_y = block['y'] + dy

                    # Can push if target is walkable
                    if room.is_walkable(new_x, new_y) or room.tiles[new_y][new_x] == TILE_SWITCH:
                        # Move block
                        room.tiles[block['y']][block['x']] = TILE_FLOOR
                        block['x'] = new_x
                        block['y'] = new_y
                        room.tiles[new_y][new_x] = TILE_BLOCK

                        # Check if on target
                        if block['target_x'] == new_x and block['target_y'] == new_y:
                            block['on_target'] = True

        def _update_switches(self, room):
            """Update floor switch logic."""
            for switch in room.switches:
                # Check if block or player on switch
                on_switch = False

                # Check blocks
                for block in room.blocks:
                    if block['x'] == switch['x'] and block['y'] == switch['y']:
                        on_switch = True
                        break

                # Check player
                if self.player.tile_x == switch['x'] and self.player.tile_y == switch['y']:
                    on_switch = True

                if on_switch and not switch['activated']:
                    switch['activated'] = True
                    room.tiles[switch['y']][switch['x']] = TILE_SWITCH_ON

                    # Unlock linked door
                    if switch['linked_door']:
                        room.unlock_door(switch['linked_door'])

        def _start_transition(self, direction):
            """Start room transition."""
            self.transition_direction = direction
            self.transition_progress = 0
            self.state = STATE_TRANSITION

        def _update_transition(self, dt):
            """Update room transition animation."""
            self.transition_progress += dt * self.transition_speed

            if self.transition_progress >= 1.0:
                # Complete transition
                next_room_id = self.current_room.connections[self.transition_direction]
                self.current_room_id = next_room_id
                self.current_room.visited = True

                # Position player at opposite door
                opposite = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
                self.player.enter_room_from(opposite[self.transition_direction])

                self.transition_direction = None
                self.transition_progress = 0
                self.state = STATE_PLAYING

                # Clear bombs when changing rooms
                self.bombs = []

        def handle_key_down(self, key):
            """Handle key press."""
            if self.state != STATE_PLAYING:
                return

            room = self.current_room

            # Attack
            if key in (K_SPACE, K_j):
                self.player.attack()

            # Place bomb
            if key in (K_b, K_k):
                bomb = self.player.place_bomb()
                if bomb:
                    self.bombs.append(bomb)

            # Use key on locked door
            if key in (K_e, K_l):
                facing_x, facing_y = self.player.get_facing_tile()
                if room.is_locked_tile(facing_x, facing_y):
                    door_dir = room.get_door_direction(facing_x, facing_y)
                    if door_dir and self.player.use_key():
                        room.unlock_door(door_dir)
                        # Also unlock in connected room
                        connected_id = room.connections[door_dir]
                        if connected_id:
                            opposite = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
                            self.rooms[connected_id].unlock_door(opposite[door_dir])

        def draw(self, surf):
            """Draw the game."""
            time_ms = pygame.time.get_ticks()

            # Calculate shake
            shake_x, shake_y = 0, 0
            if self.shake_amount > 0.5:
                shake_x = random.uniform(-self.shake_amount, self.shake_amount)
                shake_y = random.uniform(-self.shake_amount, self.shake_amount)

            # Create game surface
            game_surf = pygame.Surface((WIDTH, HEIGHT))
            game_surf.fill((20, 15, 30))

            # Draw room
            if self.state == STATE_TRANSITION:
                self._draw_transition(game_surf, time_ms)
            else:
                self._draw_room(game_surf, self.current_room, time_ms, 0, 0)

            # Blit with shake
            surf.blit(game_surf, (shake_x, shake_y))

            # Draw UI (no shake)
            self._draw_ui(surf, time_ms)

            # Draw overlays
            if self.state == STATE_VICTORY:
                self._draw_overlay(surf, "DUNGEON CLEARED!", (100, 255, 150), "The beacon's light is restored!")
            elif self.state == STATE_GAMEOVER:
                self._draw_overlay(surf, "GAME OVER", (255, 100, 100), "The darkness claims another hero...")

        def _draw_transition(self, surf, time_ms):
            """Draw room transition."""
            progress = self.transition_progress
            room = self.current_room
            next_room_id = room.connections[self.transition_direction]
            next_room = self.rooms[next_room_id]

            if self.transition_direction == 'north':
                offset = int(ROOM_HEIGHT * TILE_SIZE * progress)
                self._draw_room(surf, room, time_ms, 0, offset)
                self._draw_room(surf, next_room, time_ms, 0, offset - ROOM_HEIGHT * TILE_SIZE)
            elif self.transition_direction == 'south':
                offset = int(ROOM_HEIGHT * TILE_SIZE * progress)
                self._draw_room(surf, room, time_ms, 0, -offset)
                self._draw_room(surf, next_room, time_ms, 0, ROOM_HEIGHT * TILE_SIZE - offset)
            elif self.transition_direction == 'east':
                offset = int(ROOM_WIDTH * TILE_SIZE * progress)
                self._draw_room(surf, room, time_ms, -offset, 0)
                self._draw_room(surf, next_room, time_ms, ROOM_WIDTH * TILE_SIZE - offset, 0)
            elif self.transition_direction == 'west':
                offset = int(ROOM_WIDTH * TILE_SIZE * progress)
                self._draw_room(surf, room, time_ms, offset, 0)
                self._draw_room(surf, next_room, time_ms, offset - ROOM_WIDTH * TILE_SIZE, 0)

        def _draw_room(self, surf, room, time_ms, offset_x=0, offset_y=0):
            """Draw a room and its contents."""
            # Draw tiles
            for y in range(ROOM_HEIGHT):
                for x in range(ROOM_WIDTH):
                    tile = room.tiles[y][x]
                    px = x * TILE_SIZE + ROOM_OFFSET_X + offset_x
                    py = y * TILE_SIZE + ROOM_OFFSET_Y + offset_y

                    self._draw_tile(surf, tile, px, py, x, y, time_ms)

            # Draw items
            for item in room.items:
                if not item.collected:
                    # Adjust position for transition
                    orig_x, orig_y = item.x, item.y
                    item.draw(surf, time_ms)

            # Draw bombs
            for bomb in self.bombs:
                bomb.draw(surf, time_ms)

            # Draw enemies
            for enemy in room.enemies:
                if enemy.alive:
                    # Store original position
                    orig_x, orig_y = enemy.x, enemy.y
                    enemy.x += offset_x
                    enemy.y += offset_y
                    enemy.draw(surf, time_ms)
                    enemy.x, enemy.y = orig_x, orig_y

            # Draw projectiles
            for proj in room.projectiles:
                if proj.alive:
                    orig_x, orig_y = proj.x, proj.y
                    proj.x += offset_x
                    proj.y += offset_y
                    proj.draw(surf)
                    proj.x, proj.y = orig_x, orig_y

            # Draw player (only in current room during transition)
            if room == self.current_room or self.state != STATE_TRANSITION:
                orig_x, orig_y = self.player.x, self.player.y
                self.player.x += offset_x
                self.player.y += offset_y
                self.player.draw(surf, time_ms)
                self.player.x, self.player.y = orig_x, orig_y

            # Draw effects
            for effect in self.effects:
                effect.draw(surf)

        def _draw_tile(self, surf, tile, px, py, tx, ty, time_ms):
            """Draw a single tile."""
            # Floor
            if tile == TILE_FLOOR:
                color = (50, 45, 60) if (tx + ty) % 2 == 0 else (45, 40, 55)
                pygame.draw.rect(surf, color, (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (60, 55, 70), (px, py, TILE_SIZE, TILE_SIZE), 1)

            # Wall
            elif tile == TILE_WALL:
                pygame.draw.rect(surf, (70, 60, 85), (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (90, 80, 105), (px + 4, py + 4, TILE_SIZE - 8, TILE_SIZE - 12))
                pygame.draw.rect(surf, (50, 45, 65), (px, py, TILE_SIZE, TILE_SIZE), 2)

            # Doors
            elif tile in [TILE_DOOR_N, TILE_DOOR_S, TILE_DOOR_E, TILE_DOOR_W]:
                pygame.draw.rect(surf, (40, 35, 50), (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (80, 70, 60), (px + 8, py + 8, TILE_SIZE - 16, TILE_SIZE - 16))

            # Locked doors
            elif tile in [TILE_LOCKED_N, TILE_LOCKED_S, TILE_LOCKED_E, TILE_LOCKED_W]:
                pygame.draw.rect(surf, (40, 35, 50), (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (60, 50, 40), (px + 8, py + 8, TILE_SIZE - 16, TILE_SIZE - 16))
                # Lock icon
                lock_x = px + TILE_SIZE // 2
                lock_y = py + TILE_SIZE // 2
                pygame.draw.rect(surf, (200, 180, 50), (lock_x - 8, lock_y - 4, 16, 12))
                pygame.draw.circle(surf, (200, 180, 50), (lock_x, lock_y - 8), 8)
                pygame.draw.circle(surf, (60, 50, 40), (lock_x, lock_y - 8), 5)

            # Cracked wall
            elif tile == TILE_CRACKED:
                pygame.draw.rect(surf, (70, 60, 85), (px, py, TILE_SIZE, TILE_SIZE))
                # Crack lines
                pygame.draw.line(surf, (40, 35, 50), (px + 10, py + 5), (px + 30, py + 25), 2)
                pygame.draw.line(surf, (40, 35, 50), (px + 35, py + 10), (px + 20, py + 35), 2)
                pygame.draw.line(surf, (40, 35, 50), (px + 5, py + 30), (px + 25, py + 50), 2)

            # Switch
            elif tile == TILE_SWITCH:
                pygame.draw.rect(surf, (50, 45, 60), (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (80, 70, 90), (px + 12, py + 12, TILE_SIZE - 24, TILE_SIZE - 24))
                pygame.draw.rect(surf, (60, 55, 70), (px + 12, py + 12, TILE_SIZE - 24, TILE_SIZE - 24), 2)

            # Switch (activated)
            elif tile == TILE_SWITCH_ON:
                pygame.draw.rect(surf, (50, 45, 60), (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (100, 150, 100), (px + 12, py + 12, TILE_SIZE - 24, TILE_SIZE - 24))
                pygame.draw.rect(surf, (60, 55, 70), (px + 12, py + 12, TILE_SIZE - 24, TILE_SIZE - 24), 2)

            # Block
            elif tile == TILE_BLOCK:
                pygame.draw.rect(surf, (50, 45, 60), (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (100, 90, 80), (px + 6, py + 6, TILE_SIZE - 12, TILE_SIZE - 12))
                pygame.draw.rect(surf, (80, 70, 60), (px + 6, py + 6, TILE_SIZE - 12, TILE_SIZE - 12), 2)
                # Cross pattern
                pygame.draw.line(surf, (80, 70, 60), (px + 16, py + 16), (px + TILE_SIZE - 16, py + TILE_SIZE - 16), 2)
                pygame.draw.line(surf, (80, 70, 60), (px + TILE_SIZE - 16, py + 16), (px + 16, py + TILE_SIZE - 16), 2)

            # Chest
            elif tile == TILE_CHEST:
                pygame.draw.rect(surf, (50, 45, 60), (px, py, TILE_SIZE, TILE_SIZE))
                # Chest body
                pygame.draw.rect(surf, (139, 90, 43), (px + 8, py + 20, TILE_SIZE - 16, TILE_SIZE - 28))
                # Chest lid
                pygame.draw.rect(surf, (160, 110, 60), (px + 6, py + 12, TILE_SIZE - 12, 12))
                # Lock
                pygame.draw.circle(surf, (200, 180, 50), (px + TILE_SIZE // 2, py + 26), 5)

            # Chest (opened)
            elif tile == TILE_CHEST_OPEN:
                pygame.draw.rect(surf, (50, 45, 60), (px, py, TILE_SIZE, TILE_SIZE))
                # Chest body
                pygame.draw.rect(surf, (139, 90, 43), (px + 8, py + 20, TILE_SIZE - 16, TILE_SIZE - 28))
                # Open lid (tilted back)
                pygame.draw.rect(surf, (160, 110, 60), (px + 6, py + 4, TILE_SIZE - 12, 12))

            # Pit
            elif tile == TILE_PIT:
                pygame.draw.rect(surf, (15, 10, 20), (px, py, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(surf, (30, 25, 40), (px, py, TILE_SIZE, TILE_SIZE), 2)

        def _draw_ui(self, surf, time_ms):
            """Draw game UI."""
            font = pygame.font.Font(None, 32)

            # Health hearts (top left)
            for i in range(self.player.max_health):
                x = 30 + i * 36
                y = 30
                if i < self.player.health:
                    color = (255, 80, 80)
                else:
                    color = (60, 50, 70)

                # Heart shape
                pygame.draw.circle(surf, color, (x - 5, y), 9)
                pygame.draw.circle(surf, color, (x + 5, y), 9)
                pygame.draw.polygon(surf, color, [(x - 14, y + 2), (x + 14, y + 2), (x, y + 16)])

            # Keys (top left, below hearts)
            key_text = font.render(f"Keys: {self.player.keys}", True, (255, 220, 50))
            surf.blit(key_text, (30, 60))

            # Bombs (below keys)
            bomb_text = font.render(f"Bombs: {self.player.bombs}", True, (200, 200, 200))
            surf.blit(bomb_text, (30, 90))

            # Minimap (top right)
            self._draw_minimap(surf)

            # Controls hint (bottom)
            controls = font.render("Arrow/WASD: Move | SPACE/J: Attack | B/K: Bomb | E/L: Use Key", True, (120, 110, 140))
            surf.blit(controls, (WIDTH // 2 - controls.get_width() // 2, HEIGHT - 35))

            # Room name
            room = self.current_room
            room_names = {
                "entrance": "Entrance Hall",
                "normal": "Dungeon Chamber",
                "key_room": "Key Chamber",
                "puzzle": "Puzzle Room",
                "treasure": "Treasure Vault",
                "boss": "Shadow Sanctum"
            }
            room_name = room_names.get(room.room_type, "Unknown")
            name_text = font.render(room_name, True, (180, 170, 200))
            surf.blit(name_text, (WIDTH // 2 - name_text.get_width() // 2, 20))

        def _draw_minimap(self, surf):
            """Draw the dungeon minimap."""
            map_x = WIDTH - 160
            map_y = 20
            cell_size = 20
            padding = 2

            # Background
            pygame.draw.rect(surf, (30, 25, 40), (map_x - 5, map_y - 5, 145, 105))
            pygame.draw.rect(surf, (60, 55, 70), (map_x - 5, map_y - 5, 145, 105), 2)

            # Room positions in grid
            room_positions = {
                "0_0": (0, 0), "1_0": (1, 0), "2_0": (2, 0),
                "0_1": (0, 1), "1_1": (1, 1), "2_1": (2, 1),
                "0_2": (0, 2), "1_2": (1, 2), "2_2": (2, 2),
                "1_-1": (1, -1),  # Boss room
            }

            for room_id, (gx, gy) in room_positions.items():
                room = self.rooms.get(room_id)
                if not room:
                    continue

                # Adjust y for boss room (shift down)
                draw_y = gy + 1  # Offset so boss room fits

                rx = map_x + gx * (cell_size + padding) + 40
                ry = map_y + draw_y * (cell_size + padding)

                if room.visited:
                    # Visited room
                    if room.room_type == "boss":
                        color = (150, 50, 50)
                    elif room.room_type == "entrance":
                        color = (50, 150, 50)
                    else:
                        color = (80, 75, 100)

                    pygame.draw.rect(surf, color, (rx, ry, cell_size, cell_size))

                    # Current room indicator
                    if room_id == self.current_room_id:
                        pygame.draw.rect(surf, (255, 255, 100), (rx, ry, cell_size, cell_size), 2)
                else:
                    # Unvisited room (show if player has map)
                    if self.player.has_map:
                        pygame.draw.rect(surf, (40, 35, 50), (rx, ry, cell_size, cell_size))
                        pygame.draw.rect(surf, (60, 55, 70), (rx, ry, cell_size, cell_size), 1)

        def _draw_overlay(self, surf, title, color, subtitle):
            """Draw end game overlay."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            surf.blit(overlay, (0, 0))

            font_title = pygame.font.Font(None, 96)
            font_sub = pygame.font.Font(None, 48)

            title_text = font_title.render(title, True, color)
            surf.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 80))

            sub_text = font_sub.render(subtitle, True, (255, 255, 255))
            surf.blit(sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2))

            prompt = font_sub.render("Press ENTER to continue", True, (180, 160, 220))
            surf.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 + 80))


####################################################################################################################
# REN'PY DISPLAYABLE WRAPPER
####################################################################################################################

init python:
    class BeaconQuestDisplayable(renpy.Displayable):
        """Ren'Py displayable wrapper for Beacon Quest Zelda-style adventure."""

        def __init__(self, **kwargs):
            super(BeaconQuestDisplayable, self).__init__(**kwargs)
            self.game = None
            self.last_time = None

        def render(self, width, height, st, at):
            import pygame

            if self.game is None:
                self.game = beacon_quest.BeaconQuestGame()
                self.last_time = pygame.time.get_ticks()

            current_time = pygame.time.get_ticks()
            dt = current_time - self.last_time
            self.last_time = current_time

            # Cap dt to prevent huge jumps
            dt = min(dt, 50)

            self.game.update(dt)

            render = renpy.Render(beacon_quest.WIDTH, beacon_quest.HEIGHT)
            canvas = render.canvas()
            self.game.draw(canvas.get_surface())

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            import pygame

            if self.game is None:
                return None

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return "quit"
                if ev.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if self.game.state == beacon_quest.STATE_VICTORY:
                        return "victory"
                    elif self.game.state == beacon_quest.STATE_GAMEOVER:
                        return "retry"
                else:
                    self.game.handle_key_down(ev.key)

            return None

        def visit(self):
            return []


####################################################################################################################
# REN'PY SCREEN
####################################################################################################################

screen beacon_quest_screen():
    default game_display = BeaconQuestDisplayable()

    add Solid("#1a1525")
    add game_display

    key "K_ESCAPE" action Return("quit")


####################################################################################################################
# ENTRY LABELS
####################################################################################################################

label beacon_quest_start():
    $ quick_menu = False

    call screen beacon_quest_screen()

    $ quick_menu = True
    $ result = _return

    if result == "victory":
        return True
    else:
        return False


# Test label for standalone testing
label test_beacon_quest:
    "Welcome to Beacon Quest!"
    "Navigate the dungeon, find keys, solve puzzles, and defeat the boss!"
    "Controls: Arrow Keys/WASD to move, SPACE/J to attack, B/K for bombs, E/L to use keys."

    call beacon_quest_start()

    if _return:
        "You cleared the dungeon and restored the beacon's light!"
    else:
        "The darkness proved too strong... but you can try again."

    return
