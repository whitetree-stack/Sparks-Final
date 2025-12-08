# skybridge_adventure.rpy - Skybridge Zelda-Style Adventure Minigame
# A top-down action adventure game with two playable characters

####################################################################################################################
# BEACON QUEST ADVENTURE MINIGAME
####################################################################################################################

init python in beacon_quest:
    import pygame
    import random
    import math
    from pygame.locals import *

    # Game constants
    WIDTH, HEIGHT = 1920, 1080
    TILE_SIZE = 64

    # ----------------------------------------------------------------
    # TILESET LOADING
    # ----------------------------------------------------------------
    # Helper to load images through Ren'Py
    def load_image(path):
        """Load an image through Ren'Py's image system."""
        try:
            return renpy.display.im.Image(path).load()
        except:
            return None

    # Tileset configuration - tile regions on the spritesheet
    # Format: (x, y, width, height) - coordinates on dungeon_tileset.png
    TILESET_PATH = "images/dungeon_tileset.png"
    TILESET_LOADED = False
    TILE_SPRITES = {}

    # Floor tiles are in a 6x6 grid at bottom right of spritesheet
    # Each floor tile is approximately 48x48 pixels
    FLOOR_TILE_SIZE = 48
    FLOOR_GRID_START_X = 736
    FLOOR_GRID_START_Y = 256

    # Wall/decoration tile regions (approximate positions)
    TILE_REGIONS = {
        # Floor variations (will be randomly selected)
        'floor_1': (736, 256, 48, 48),
        'floor_2': (784, 256, 48, 48),
        'floor_3': (832, 256, 48, 48),
        'floor_4': (880, 256, 48, 48),
        'floor_5': (928, 256, 48, 48),
        'floor_6': (976, 256, 48, 48),
        'floor_7': (736, 304, 48, 48),
        'floor_8': (784, 304, 48, 48),
        'floor_9': (832, 304, 48, 48),
        'floor_10': (880, 304, 48, 48),
        'floor_11': (928, 304, 48, 48),
        'floor_12': (976, 304, 48, 48),
        # More floor variations from lower rows
        'floor_13': (736, 352, 48, 48),
        'floor_14': (784, 352, 48, 48),
        'floor_15': (832, 352, 48, 48),
        'floor_16': (880, 352, 48, 48),

        # Wall pieces
        'wall_top': (0, 192, 96, 48),      # Top wall section
        'wall_shelf': (0, 64, 96, 64),     # Wall with shelf

        # Doorway/arch (open archway)
        'arch_open': (320, 0, 96, 128),

        # Gate/bars doorway
        'gate': (416, 0, 96, 128),

        # Dark doorway/entrance
        'door_dark': (576, 160, 64, 80),

        # Stairs
        'stairs': (672, 0, 64, 96),

        # Bookshelf
        'bookshelf': (736, 0, 64, 128),

        # Fountain/pedestal
        'fountain': (512, 224, 64, 64),

        # Pillars
        'pillar': (608, 80, 32, 80),
    }

    def load_tileset():
        """Load and extract tiles from the dungeon tileset."""
        global TILESET_LOADED, TILE_SPRITES

        if TILESET_LOADED:
            return True

        try:
            tileset = load_image(TILESET_PATH)
            if tileset is None:
                print("Failed to load tileset")
                return False

            # Extract each tile region
            for name, region in TILE_REGIONS.items():
                x, y, w, h = region
                # Create a surface for this tile
                tile_surf = pygame.Surface((w, h), pygame.SRCALPHA)
                tile_surf.blit(tileset, (0, 0), (x, y, w, h))

                # Scale to game tile size (64x64) for floor tiles
                if name.startswith('floor_'):
                    tile_surf = pygame.transform.scale(tile_surf, (TILE_SIZE, TILE_SIZE))

                TILE_SPRITES[name] = tile_surf

            TILESET_LOADED = True
            print(f"Loaded {len(TILE_SPRITES)} tiles from tileset")
            return True
        except Exception as e:
            print(f"Error loading tileset: {e}")
            return False

    def get_floor_tile(x, y):
        """Get a floor tile sprite based on position (for consistent variation)."""
        if not TILE_SPRITES:
            return None
        # Use position to deterministically select a tile variation
        floor_keys = [k for k in TILE_SPRITES.keys() if k.startswith('floor_')]
        if not floor_keys:
            return None
        # Create a pattern that looks natural
        index = (x * 7 + y * 13 + (x * y) % 5) % len(floor_keys)
        return TILE_SPRITES.get(floor_keys[index])

    # Map dimensions
    MAP_WIDTH = 20
    MAP_HEIGHT = 13

    # Calculate offsets to center the map
    MAP_OFFSET_X = (WIDTH - MAP_WIDTH * TILE_SIZE) // 2
    MAP_OFFSET_Y = (HEIGHT - MAP_HEIGHT * TILE_SIZE) // 2

    # Tile types
    TILE_FLOOR = 0
    TILE_WALL = 1
    TILE_BEACON = 2
    TILE_CHEST = 3
    TILE_VOID = 5
    TILE_BRIDGE = 6
    # Directional doors
    TILE_DOOR_N = 10  # Door leading north
    TILE_DOOR_S = 11  # Door leading south
    TILE_DOOR_E = 12  # Door leading east
    TILE_DOOR_W = 13  # Door leading west

    # Game states
    STATE_PLAYING = "playing"
    STATE_VICTORY = "victory"
    STATE_GAMEOVER = "gameover"
    STATE_TRANSITIONING = "transitioning"

    # Direction vectors
    DIRECTIONS = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)
    }

    # Door direction mapping (which direction player moves through)
    DOOR_DIRECTIONS = {
        TILE_DOOR_N: 'up',
        TILE_DOOR_S: 'down',
        TILE_DOOR_E: 'right',
        TILE_DOOR_W: 'left'
    }

    # Opposite spawn positions when entering a room
    OPPOSITE_DIRECTION = {
        'up': 'down',
        'down': 'up',
        'left': 'right',
        'right': 'left'
    }

    class Projectile:
        """A projectile fired by Tristan."""
        def __init__(self, x, y, direction, owner="tristan"):
            self.x = x
            self.y = y
            self.owner = owner
            self.direction = direction
            self.speed = 12
            self.alive = True
            self.radius = 10

            # Set velocity based on direction
            dir_vec = DIRECTIONS[direction]
            self.vx = dir_vec[0] * self.speed
            self.vy = dir_vec[1] * self.speed

            # Calculate angle for rotation
            self.angle = {'up': 90, 'down': -90, 'left': 180, 'right': 0}[direction]

            # Trail effect
            self.trail = []
            self.max_trail = 6

            # Animation
            self.anim_timer = 0
            self.pulse = 0

            # Color based on owner
            if owner == "tristan":
                self.color = (255, 200, 100)  # Orange/gold
                self.glow_color = (255, 150, 50)
            else:
                self.color = (100, 180, 255)  # Blue
                self.glow_color = (50, 130, 255)

        def update(self, dt, game_map):
            # Store trail position
            self.trail.append((self.x, self.y))
            if len(self.trail) > self.max_trail:
                self.trail.pop(0)

            # Move
            self.x += self.vx
            self.y += self.vy

            # Animation pulse
            self.anim_timer += dt
            self.pulse = math.sin(self.anim_timer * 0.02) * 0.3 + 0.7

            # Check wall collision
            tile_x = int((self.x - MAP_OFFSET_X) // TILE_SIZE)
            tile_y = int((self.y - MAP_OFFSET_Y) // TILE_SIZE)

            if tile_x < 0 or tile_x >= MAP_WIDTH or tile_y < 0 or tile_y >= MAP_HEIGHT:
                self.alive = False
                return

            tile = game_map[tile_y][tile_x]
            if tile in (TILE_WALL, TILE_VOID):
                self.alive = False

        def get_rect(self):
            return pygame.Rect(self.x - self.radius, self.y - self.radius,
                             self.radius * 2, self.radius * 2)

        def draw(self, surf):
            # Draw trail with decreasing opacity
            for i, (tx, ty) in enumerate(self.trail):
                alpha = int(120 * (i + 1) / len(self.trail) * self.pulse)
                trail_radius = int(self.radius * (i + 1) / len(self.trail) * 0.6)
                if trail_radius > 0:
                    trail_surf = pygame.Surface((trail_radius * 2 + 4, trail_radius * 2 + 4), pygame.SRCALPHA)
                    trail_color = (*self.glow_color[:3], alpha)
                    pygame.draw.circle(trail_surf, trail_color, (trail_radius + 2, trail_radius + 2), trail_radius)
                    surf.blit(trail_surf, (int(tx) - trail_radius - 2, int(ty) - trail_radius - 2))

            # Draw glow
            glow_size = int(self.radius * 2.5 * self.pulse)
            glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*self.glow_color, 60), (glow_size, glow_size), glow_size)
            surf.blit(glow_surf, (int(self.x) - glow_size, int(self.y) - glow_size))

            # Draw core
            pygame.draw.circle(surf, (255, 255, 255), (int(self.x), int(self.y)), int(self.radius * 0.7))
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.radius)


    class Character:
        """Base class for playable characters."""
        def __init__(self, x, y, char_type="tristan"):
            self.x = x * TILE_SIZE + MAP_OFFSET_X
            self.y = y * TILE_SIZE + MAP_OFFSET_Y
            self.tile_x = x
            self.tile_y = y
            self.width = 48
            self.height = 48
            self.speed = 5
            self.char_type = char_type

            self.health = 5
            self.max_health = 5

            self.facing = 'down'
            self.attacking = False
            self.attack_timer = 0
            self.attack_duration = 200
            self.attack_cooldown = 0
            self.invulnerable = 0

            # Animation
            self.anim_frame = 0
            self.anim_timer = 0
            self.moving = False

            # Character-specific colors
            if char_type == "tristan":
                self.color = (100, 200, 100)      # Green
                self.outline = (60, 150, 60)
            else:  # henry
                self.color = (100, 150, 220)      # Blue
                self.outline = (60, 100, 180)

        def set_position(self, x, y):
            """Set position in tile coordinates."""
            self.x = x * TILE_SIZE + MAP_OFFSET_X
            self.y = y * TILE_SIZE + MAP_OFFSET_Y
            self.tile_x = x
            self.tile_y = y

        def set_pixel_position(self, px, py):
            """Set position in pixel coordinates."""
            self.x = px
            self.y = py
            self.tile_x = int((self.x - MAP_OFFSET_X + self.width // 2) // TILE_SIZE)
            self.tile_y = int((self.y - MAP_OFFSET_Y + self.height // 2) // TILE_SIZE)

        def update(self, dt, keys, game_map, is_active=True):
            """Update character state. is_active determines if player-controlled."""
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

            # Only process input if active player
            if is_active:
                self.process_movement(dt, keys, game_map)

            # Animation
            if self.moving:
                self.anim_timer += dt
                if self.anim_timer >= 150:
                    self.anim_timer = 0
                    self.anim_frame = (self.anim_frame + 1) % 4
            else:
                self.anim_frame = 0

        def process_movement(self, dt, keys, game_map):
            """Process keyboard movement input."""
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
                if self.can_move_to(new_x, self.y, game_map):
                    self.x = new_x

            # Try vertical movement
            if dy != 0:
                new_y = self.y + dy
                if self.can_move_to(self.x, new_y, game_map):
                    self.y = new_y

            # Update tile position
            self.tile_x = int((self.x - MAP_OFFSET_X + self.width // 2) // TILE_SIZE)
            self.tile_y = int((self.y - MAP_OFFSET_Y + self.height // 2) // TILE_SIZE)

        def can_move_to(self, new_x, new_y, game_map):
            """Check if character can move to position."""
            corners = [
                (new_x + 8, new_y + 8),
                (new_x + self.width - 8, new_y + 8),
                (new_x + 8, new_y + self.height - 8),
                (new_x + self.width - 8, new_y + self.height - 8),
            ]

            for cx, cy in corners:
                tile_x = int((cx - MAP_OFFSET_X) // TILE_SIZE)
                tile_y = int((cy - MAP_OFFSET_Y) // TILE_SIZE)

                if tile_x < 0 or tile_x >= MAP_WIDTH or tile_y < 0 or tile_y >= MAP_HEIGHT:
                    return False

                tile = game_map[tile_y][tile_x]
                if tile in (TILE_WALL, TILE_VOID):
                    return False

            return True

        def take_damage(self, amount=1):
            """Take damage if not invulnerable."""
            if self.invulnerable <= 0:
                self.health -= amount
                self.invulnerable = 1000
                return True
            return False

        def get_rect(self):
            return pygame.Rect(self.x, self.y, self.width, self.height)

        def get_center(self):
            return (self.x + self.width // 2, self.y + self.height // 2)

        def draw(self, surf, time_ms, is_active=True):
            """Draw the character."""
            # Flash when invulnerable
            if self.invulnerable > 0 and (time_ms // 100) % 2 == 0:
                return

            # Draw shadow
            shadow_surf = pygame.Surface((self.width, 20), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x, self.y + self.height - 10))

            # Draw body with bobbing
            body_offset = 0
            if self.moving:
                body_offset = math.sin(time_ms * 0.015) * 3

            pygame.draw.rect(surf, self.outline, (self.x + 4, self.y + body_offset + 4, self.width - 8, self.height - 8))
            pygame.draw.rect(surf, self.color, (self.x + 6, self.y + body_offset + 6, self.width - 12, self.height - 12))

            # Draw active indicator (glowing ring around active character)
            if is_active:
                indicator_surf = pygame.Surface((self.width + 16, self.height + 16), pygame.SRCALPHA)
                pulse = 0.5 + 0.3 * math.sin(time_ms * 0.008)
                pygame.draw.rect(indicator_surf, (255, 255, 100, int(80 * pulse)),
                               (0, 0, self.width + 16, self.height + 16), 3)
                surf.blit(indicator_surf, (self.x - 8, self.y + body_offset - 8))

            # Draw face based on direction
            face_x = self.x + self.width // 2
            face_y = self.y + self.height // 2 + body_offset - 5

            eye_offset = {'up': (0, -8), 'down': (0, 8), 'left': (-8, 0), 'right': (8, 0)}
            ex, ey = eye_offset[self.facing]

            pygame.draw.circle(surf, (255, 255, 255), (face_x - 8, face_y), 6)
            pygame.draw.circle(surf, (255, 255, 255), (face_x + 8, face_y), 6)
            pygame.draw.circle(surf, (40, 40, 40), (face_x - 8 + ex // 2, face_y + ey // 2), 3)
            pygame.draw.circle(surf, (40, 40, 40), (face_x + 8 + ex // 2, face_y + ey // 2), 3)

            # Draw attack effect if attacking
            if self.attacking:
                self.draw_attack(surf, time_ms)

        def draw_attack(self, surf, time_ms):
            """Override in subclass for different attack visuals."""
            pass

        def attack(self):
            """Override in subclass."""
            pass


    class Tristan(Character):
        """Tristan - ranged projectile specialist."""
        def __init__(self, x, y):
            super().__init__(x, y, "tristan")
            self.attack_cooldown_max = 350  # Slightly slower than Henry
            self.projectile_queue = []      # Projectiles to spawn

        def attack(self):
            """Fire a projectile."""
            if not self.attacking and self.attack_cooldown <= 0:
                self.attacking = True
                self.attack_timer = 0
                self.attack_cooldown = self.attack_cooldown_max
                # Queue projectile spawn
                cx, cy = self.get_center()
                self.projectile_queue.append(Projectile(cx, cy, self.facing, "tristan"))
                return True
            return False

        def get_queued_projectiles(self):
            """Get and clear queued projectiles."""
            projectiles = self.projectile_queue[:]
            self.projectile_queue = []
            return projectiles

        def draw_attack(self, surf, time_ms):
            """Draw projectile firing effect."""
            if not self.attacking:
                return

            progress = self.attack_timer / self.attack_duration
            cx, cy = self.get_center()

            # Flash effect when firing
            if progress < 0.3:
                flash_size = int(30 * (1 - progress / 0.3))
                flash_surf = pygame.Surface((flash_size * 2, flash_size * 2), pygame.SRCALPHA)
                pygame.draw.circle(flash_surf, (255, 200, 100, int(150 * (1 - progress / 0.3))),
                                 (flash_size, flash_size), flash_size)
                surf.blit(flash_surf, (cx - flash_size, cy - flash_size))


    class Henry(Character):
        """Henry - melee sword specialist."""
        def __init__(self, x, y):
            super().__init__(x, y, "henry")
            self.attack_cooldown_max = 280  # Faster melee attacks
            self.attack_duration = 220

        def attack(self):
            """Sword swing attack."""
            if not self.attacking and self.attack_cooldown <= 0:
                self.attacking = True
                self.attack_timer = 0
                self.attack_cooldown = self.attack_cooldown_max
                return True
            return False

        def get_attack_rect(self):
            """Get the sword attack hitbox."""
            attack_range = 55
            attack_width = 65

            cx = self.x + self.width // 2
            cy = self.y + self.height // 2

            if self.facing == 'up':
                return pygame.Rect(cx - attack_width // 2, cy - attack_range - 10, attack_width, attack_range)
            elif self.facing == 'down':
                return pygame.Rect(cx - attack_width // 2, cy + 10, attack_width, attack_range)
            elif self.facing == 'left':
                return pygame.Rect(cx - attack_range - 10, cy - attack_width // 2, attack_range, attack_width)
            else:
                return pygame.Rect(cx + 10, cy - attack_width // 2, attack_range, attack_width)

        def draw_attack(self, surf, time_ms):
            """Draw sword swing effect."""
            if not self.attacking:
                return

            progress = self.attack_timer / self.attack_duration
            cx = self.x + self.width // 2
            cy = self.y + self.height // 2

            swing_length = 50
            swing_width = 5

            base_angles = {'up': -90, 'down': 90, 'left': 180, 'right': 0}
            base_angle = base_angles[self.facing]
            swing_range = 100

            swing_angle = base_angle + (progress - 0.5) * swing_range
            rad = math.radians(swing_angle)

            end_x = cx + math.cos(rad) * swing_length
            end_y = cy + math.sin(rad) * swing_length

            # Sword blade (blue tint for Henry)
            pygame.draw.line(surf, (180, 200, 230), (cx, cy), (end_x, end_y), swing_width + 3)
            pygame.draw.line(surf, (220, 240, 255), (cx, cy), (end_x, end_y), swing_width)

            # Sparkle at tip
            sparkle_size = 5 + int(4 * math.sin(progress * math.pi))
            pygame.draw.circle(surf, (200, 220, 255), (int(end_x), int(end_y)), sparkle_size)


    class CompanionAI:
        """AI controller for the non-active character."""
        def __init__(self):
            self.follow_distance = 80      # Desired distance from leader
            self.min_distance = 50         # Don't get closer than this
            self.attack_range = 150        # Range to auto-attack enemies
            self.attack_check_timer = 0
            self.move_timer = 0

        def update(self, follower, leader, dt, game_map, enemies):
            """Update the follower AI."""
            self.move_timer += dt
            self.attack_check_timer += dt

            # Calculate distance to leader
            dx = leader.x - follower.x
            dy = leader.y - follower.y
            dist = math.hypot(dx, dy)

            # Follow behavior
            follower.moving = False

            if dist > self.follow_distance:
                # Move toward leader
                if dist > 0:
                    move_x = (dx / dist) * follower.speed * 0.9  # Slightly slower than player
                    move_y = (dy / dist) * follower.speed * 0.9

                    # Update facing
                    if abs(dx) > abs(dy):
                        follower.facing = 'right' if dx > 0 else 'left'
                    else:
                        follower.facing = 'down' if dy > 0 else 'up'

                    # Try to move
                    new_x = follower.x + move_x
                    new_y = follower.y + move_y

                    if follower.can_move_to(new_x, follower.y, game_map):
                        follower.x = new_x
                        follower.moving = True
                    if follower.can_move_to(follower.x, new_y, game_map):
                        follower.y = new_y
                        follower.moving = True

                    # Update tile position
                    follower.tile_x = int((follower.x - MAP_OFFSET_X + follower.width // 2) // TILE_SIZE)
                    follower.tile_y = int((follower.y - MAP_OFFSET_Y + follower.height // 2) // TILE_SIZE)

            # Auto-attack nearby enemies
            if self.attack_check_timer >= 500:  # Check every 500ms
                self.attack_check_timer = 0
                self.try_auto_attack(follower, enemies)

        def try_auto_attack(self, character, enemies):
            """Attempt to attack nearby enemies."""
            cx, cy = character.get_center()

            for enemy in enemies:
                if not enemy.alive:
                    continue

                ex = enemy.x + enemy.width // 2
                ey = enemy.y + enemy.height // 2
                dist = math.hypot(ex - cx, ey - cy)

                if dist < self.attack_range:
                    # Face the enemy
                    dx = ex - cx
                    dy = ey - cy
                    if abs(dx) > abs(dy):
                        character.facing = 'right' if dx > 0 else 'left'
                    else:
                        character.facing = 'down' if dy > 0 else 'up'

                    # Attack!
                    character.attack()
                    return

    class Enemy:
        """A shadow enemy."""
        def __init__(self, x, y, enemy_type="shadow"):
            self.x = x * TILE_SIZE + MAP_OFFSET_X
            self.y = y * TILE_SIZE + MAP_OFFSET_Y
            self.width = 50
            self.height = 50
            self.speed = 2
            self.enemy_type = enemy_type

            self.health = 2
            self.alive = True
            self.hit_flash = 0

            self.direction = random.choice(['up', 'down', 'left', 'right'])
            self.move_timer = 0
            self.move_duration = random.randint(500, 1500)
            self.pause_timer = 0

            self.anim_phase = random.random() * math.pi * 2

        def update(self, dt, game_map, player):
            if not self.alive:
                return

            self.anim_phase += dt * 0.005

            if self.hit_flash > 0:
                self.hit_flash -= dt

            # Simple AI: move in current direction, occasionally change
            self.move_timer += dt
            if self.move_timer >= self.move_duration:
                self.move_timer = 0
                self.move_duration = random.randint(500, 1500)
                self.direction = random.choice(['up', 'down', 'left', 'right'])

            # Move towards player occasionally
            if random.random() < 0.02:
                dx = player.x - self.x
                dy = player.y - self.y
                if abs(dx) > abs(dy):
                    self.direction = 'right' if dx > 0 else 'left'
                else:
                    self.direction = 'down' if dy > 0 else 'up'

            # Move
            dx, dy = DIRECTIONS[self.direction]
            new_x = self.x + dx * self.speed
            new_y = self.y + dy * self.speed

            if self.can_move_to(new_x, new_y, game_map):
                self.x = new_x
                self.y = new_y
            else:
                # Change direction on collision
                self.direction = random.choice(['up', 'down', 'left', 'right'])

        def can_move_to(self, new_x, new_y, game_map):
            """Check if enemy can move to position."""
            corners = [
                (new_x + 8, new_y + 8),
                (new_x + self.width - 8, new_y + 8),
                (new_x + 8, new_y + self.height - 8),
                (new_x + self.width - 8, new_y + self.height - 8),
            ]

            for cx, cy in corners:
                tile_x = int((cx - MAP_OFFSET_X) // TILE_SIZE)
                tile_y = int((cy - MAP_OFFSET_Y) // TILE_SIZE)

                if tile_x < 0 or tile_x >= MAP_WIDTH or tile_y < 0 or tile_y >= MAP_HEIGHT:
                    return False

                tile = game_map[tile_y][tile_x]
                if tile in (TILE_WALL, TILE_VOID):
                    return False

            return True

        def get_rect(self):
            return pygame.Rect(self.x, self.y, self.width, self.height)

        def take_damage(self, amount=1):
            self.health -= amount
            self.hit_flash = 150
            if self.health <= 0:
                self.alive = False
                return True
            return False

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            # Flash when hit
            if self.hit_flash > 0:
                color = (255, 200, 200)
            else:
                color = (80, 50, 100)

            # Bobbing animation
            bob = math.sin(self.anim_phase) * 3

            # Shadow
            shadow_surf = pygame.Surface((self.width, 20), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 60), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x, self.y + self.height - 5))

            # Body (shadowy blob)
            body_surf = pygame.Surface((self.width + 10, self.height + 10), pygame.SRCALPHA)

            # Outer glow
            pygame.draw.ellipse(body_surf, (100, 50, 130, 100),
                              (0, 0, self.width + 10, self.height + 10))

            # Main body
            pygame.draw.ellipse(body_surf, color,
                              (5, 5, self.width, self.height - 5))

            surf.blit(body_surf, (self.x - 5, self.y + bob - 5))

            # Evil eyes
            eye_y = self.y + self.height // 3 + bob
            pygame.draw.circle(surf, (255, 100, 100), (int(self.x + 15), int(eye_y)), 6)
            pygame.draw.circle(surf, (255, 100, 100), (int(self.x + self.width - 15), int(eye_y)), 6)
            pygame.draw.circle(surf, (255, 200, 200), (int(self.x + 15), int(eye_y)), 3)
            pygame.draw.circle(surf, (255, 200, 200), (int(self.x + self.width - 15), int(eye_y)), 3)

    class Shard:
        """A collectible beacon shard."""
        def __init__(self, x, y):
            self.x = x * TILE_SIZE + MAP_OFFSET_X + TILE_SIZE // 2
            self.y = y * TILE_SIZE + MAP_OFFSET_Y + TILE_SIZE // 2
            self.collected = False
            self.anim_phase = random.random() * math.pi * 2

        def update(self, dt):
            self.anim_phase += dt * 0.004

        def get_rect(self):
            return pygame.Rect(self.x - 20, self.y - 20, 40, 40)

        def draw(self, surf, time_ms):
            if self.collected:
                return

            bob = math.sin(self.anim_phase) * 5
            glow = 0.5 + 0.3 * math.sin(self.anim_phase * 1.5)

            # Glow
            glow_size = int(35 + 10 * glow)
            glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
            glow_alpha = int(100 * glow)
            pygame.draw.circle(glow_surf, (255, 220, 100, glow_alpha), (glow_size, glow_size), glow_size)
            surf.blit(glow_surf, (self.x - glow_size, self.y + bob - glow_size))

            # Crystal shape
            points = []
            for i in range(6):
                angle = i * math.pi / 3 - math.pi / 2
                r = 18 if i % 2 == 0 else 10
                points.append((self.x + math.cos(angle) * r, self.y + bob + math.sin(angle) * r))

            pygame.draw.polygon(surf, (255, 240, 150), points)
            pygame.draw.polygon(surf, (255, 200, 50), points, 2)

            # Inner sparkle
            pygame.draw.circle(surf, (255, 255, 255), (int(self.x - 3), int(self.y + bob - 5)), 4)

    class DeathEffect:
        """Effect when enemy dies."""
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.particles = []
            self.lifetime = 500

            for _ in range(15):
                angle = random.random() * math.pi * 2
                speed = random.uniform(2, 5)
                self.particles.append({
                    'x': x, 'y': y,
                    'vx': math.cos(angle) * speed,
                    'vy': math.sin(angle) * speed - 2,
                    'size': random.uniform(4, 10),
                    'color': random.choice([(100, 50, 130), (150, 80, 180), (80, 40, 100)])
                })

        def update(self, dt):
            self.lifetime -= dt
            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['vy'] += 0.1
            return self.lifetime > 0

        def draw(self, surf):
            alpha = int(255 * (self.lifetime / 500))
            for p in self.particles:
                size = p['size'] * (self.lifetime / 500)
                if size > 0:
                    ps = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
                    pygame.draw.circle(ps, (*p['color'], alpha), (int(size + 2), int(size + 2)), int(size))
                    surf.blit(ps, (int(p['x'] - size), int(p['y'] - size)))

    class Room:
        """A single room in the dungeon."""
        def __init__(self, room_id, game_map, enemies, shards, doors):
            self.room_id = room_id
            self.game_map = game_map
            self.enemies = enemies
            self.shards = shards
            self.doors = doors  # Dict: {door_tile: (target_room_id, spawn_direction)}

        def reset_enemies(self):
            """Reset enemies when re-entering room."""
            for enemy in self.enemies:
                if not enemy.alive:
                    enemy.alive = True
                    enemy.health = 2


    class BeaconQuestGame:
        """Main game controller for Beacon Quest with multi-room support."""
        def __init__(self):
            self.state = STATE_PLAYING

            # Load tileset sprites
            load_tileset()

            # Create all rooms
            self.rooms = self.create_all_rooms()
            self.current_room_id = "start"
            self.current_room = self.rooms[self.current_room_id]
            self.game_map = self.current_room.game_map

            # Create both characters
            self.tristan = Tristan(10, 10)  # Start near bottom center
            self.henry = Henry(9, 10)       # Henry starts next to Tristan

            # Active character tracking
            self.active_character = "tristan"  # "tristan" or "henry"
            self.companion_ai = CompanionAI()

            # Shared game state
            self.shards_collected = 0
            self.target_shards = 5  # More shards across multiple rooms

            # Projectiles
            self.projectiles = []

            # Effects
            self.effects = []

            # Camera shake
            self.shake_amount = 0
            self.shake_timer = 0

            # Room transition
            self.transition_timer = 0
            self.transition_duration = 300
            self.transition_alpha = 0
            self.pending_room = None
            self.pending_spawn_dir = None

            # Character switch cooldown
            self.switch_cooldown = 0

        def get_active_player(self):
            """Get the currently controlled character."""
            return self.tristan if self.active_character == "tristan" else self.henry

        def get_companion(self):
            """Get the AI-controlled character."""
            return self.henry if self.active_character == "tristan" else self.tristan

        def switch_character(self):
            """Switch which character the player controls."""
            if self.switch_cooldown <= 0:
                self.active_character = "henry" if self.active_character == "tristan" else "tristan"
                self.switch_cooldown = 300  # 300ms cooldown

        def create_all_rooms(self):
            """Create all rooms in the dungeon."""
            rooms = {}

            # Starting room (center hub)
            rooms["start"] = self.create_start_room()

            # North room (beacon room)
            rooms["north"] = self.create_north_room()

            # East room
            rooms["east"] = self.create_east_room()

            # West room
            rooms["west"] = self.create_west_room()

            return rooms

        def create_start_room(self):
            """Create the starting hub room with doors to other areas."""
            game_map = [[TILE_VOID for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

            # Main platform
            for y in range(1, 12):
                for x in range(2, 18):
                    game_map[y][x] = TILE_FLOOR

            # Walls around edges
            for x in range(2, 18):
                game_map[0][x] = TILE_WALL
                game_map[12][x] = TILE_WALL
            for y in range(1, 12):
                game_map[y][1] = TILE_WALL
                game_map[y][18] = TILE_WALL

            # North door (to beacon room)
            game_map[0][9] = TILE_DOOR_N
            game_map[0][10] = TILE_DOOR_N

            # East door
            game_map[6][18] = TILE_DOOR_E

            # West door
            game_map[6][1] = TILE_DOOR_W

            # Some obstacles
            game_map[5][7] = TILE_WALL
            game_map[5][12] = TILE_WALL

            enemies = [
                Enemy(5, 4),
                Enemy(14, 4),
                Enemy(10, 7),
            ]

            shards = [
                Shard(4, 3),
            ]

            doors = {
                (9, 0): ("north", "up"),
                (10, 0): ("north", "up"),
                (18, 6): ("east", "right"),
                (1, 6): ("west", "left"),
            }

            return Room("start", game_map, enemies, shards, doors)

        def create_north_room(self):
            """Create the north room with the beacon."""
            game_map = [[TILE_VOID for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

            # Main platform
            for y in range(1, 12):
                for x in range(2, 18):
                    game_map[y][x] = TILE_FLOOR

            # Walls
            for x in range(2, 18):
                game_map[0][x] = TILE_WALL
                game_map[12][x] = TILE_WALL
            for y in range(1, 12):
                game_map[y][1] = TILE_WALL
                game_map[y][18] = TILE_WALL

            # South door (back to start)
            game_map[12][9] = TILE_DOOR_S
            game_map[12][10] = TILE_DOOR_S

            # Central beacon
            game_map[3][9] = TILE_BEACON
            game_map[3][10] = TILE_BEACON

            # Protective walls around beacon
            game_map[2][7] = TILE_WALL
            game_map[2][8] = TILE_WALL
            game_map[2][11] = TILE_WALL
            game_map[2][12] = TILE_WALL
            game_map[4][7] = TILE_WALL
            game_map[4][12] = TILE_WALL

            enemies = [
                Enemy(4, 6),
                Enemy(15, 6),
                Enemy(10, 9),
                Enemy(6, 3),
                Enemy(13, 3),
            ]

            shards = [
                Shard(3, 2),
                Shard(16, 2),
            ]

            doors = {
                (9, 12): ("start", "down"),
                (10, 12): ("start", "down"),
            }

            return Room("north", game_map, enemies, shards, doors)

        def create_east_room(self):
            """Create the east room - enemy gauntlet."""
            game_map = [[TILE_VOID for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

            # Main platform
            for y in range(1, 12):
                for x in range(2, 18):
                    game_map[y][x] = TILE_FLOOR

            # Walls
            for x in range(2, 18):
                game_map[0][x] = TILE_WALL
                game_map[12][x] = TILE_WALL
            for y in range(1, 12):
                game_map[y][1] = TILE_WALL
                game_map[y][18] = TILE_WALL

            # West door (back to start)
            game_map[6][1] = TILE_DOOR_W

            # Obstacle maze
            for y in range(3, 10):
                if y != 6:
                    game_map[y][6] = TILE_WALL
                    game_map[y][13] = TILE_WALL

            enemies = [
                Enemy(4, 3),
                Enemy(4, 9),
                Enemy(9, 5),
                Enemy(9, 8),
                Enemy(15, 4),
                Enemy(15, 8),
            ]

            shards = [
                Shard(16, 6),
            ]

            doors = {
                (1, 6): ("start", "left"),
            }

            return Room("east", game_map, enemies, shards, doors)

        def create_west_room(self):
            """Create the west room - treasure room."""
            game_map = [[TILE_VOID for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

            # Main platform
            for y in range(1, 12):
                for x in range(2, 18):
                    game_map[y][x] = TILE_FLOOR

            # Walls
            for x in range(2, 18):
                game_map[0][x] = TILE_WALL
                game_map[12][x] = TILE_WALL
            for y in range(1, 12):
                game_map[y][1] = TILE_WALL
                game_map[y][18] = TILE_WALL

            # East door (back to start)
            game_map[6][18] = TILE_DOOR_E

            # Pillars
            game_map[3][5] = TILE_WALL
            game_map[3][14] = TILE_WALL
            game_map[9][5] = TILE_WALL
            game_map[9][14] = TILE_WALL
            game_map[6][9] = TILE_WALL
            game_map[6][10] = TILE_WALL

            enemies = [
                Enemy(7, 3),
                Enemy(12, 3),
                Enemy(7, 9),
                Enemy(12, 9),
            ]

            shards = [
                Shard(3, 6),
            ]

            doors = {
                (18, 6): ("start", "right"),
            }

            return Room("west", game_map, enemies, shards, doors)

        def change_room(self, new_room_id, entry_direction):
            """Change to a new room with transition effect."""
            self.pending_room = new_room_id
            self.pending_spawn_dir = entry_direction
            self.state = STATE_TRANSITIONING
            self.transition_timer = 0
            self.transition_alpha = 0

        def complete_room_transition(self):
            """Complete the room transition after fade."""
            self.current_room_id = self.pending_room
            self.current_room = self.rooms[self.current_room_id]
            self.game_map = self.current_room.game_map

            # Calculate spawn position based on entry direction
            spawn_x, spawn_y = self.get_spawn_position(self.pending_spawn_dir)

            # Move both characters to spawn
            self.tristan.set_position(spawn_x, spawn_y)
            self.henry.set_position(spawn_x - 1 if spawn_x > 2 else spawn_x + 1, spawn_y)

            # Update facing direction
            opposite = OPPOSITE_DIRECTION[self.pending_spawn_dir]
            dir_to_facing = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
            self.tristan.facing = dir_to_facing[self.pending_spawn_dir]
            self.henry.facing = dir_to_facing[self.pending_spawn_dir]

            # Clear projectiles
            self.projectiles = []

            self.pending_room = None
            self.pending_spawn_dir = None

        def get_spawn_position(self, entry_direction):
            """Get spawn position when entering from a direction."""
            # Entry direction is the direction player was moving when they hit the door
            # So if they went through a north door (moving up), they appear at bottom of new room
            if entry_direction == 'up':
                # Came from south, spawn at bottom
                return (10, 10)
            elif entry_direction == 'down':
                # Came from north, spawn at top
                return (10, 2)
            elif entry_direction == 'left':
                # Came from east, spawn at right
                return (16, 6)
            elif entry_direction == 'right':
                # Came from west, spawn at left
                return (3, 6)
            return (10, 6)

        def check_door_collision(self, character):
            """Check if character is standing on a door tile."""
            tile_x = character.tile_x
            tile_y = character.tile_y

            if (tile_x, tile_y) in self.current_room.doors:
                target_room, entry_dir = self.current_room.doors[(tile_x, tile_y)]
                self.change_room(target_room, entry_dir)
                return True
            return False

        def trigger_shake(self, amount=5):
            self.shake_amount = amount
            self.shake_timer = 200

        def update(self, dt):
            # Handle transition state
            if self.state == STATE_TRANSITIONING:
                self.transition_timer += dt
                # Fade out then fade in
                if self.transition_timer < self.transition_duration / 2:
                    self.transition_alpha = int(255 * (self.transition_timer / (self.transition_duration / 2)))
                else:
                    if self.pending_room:
                        self.complete_room_transition()
                    self.transition_alpha = int(255 * (1 - (self.transition_timer - self.transition_duration / 2) / (self.transition_duration / 2)))

                if self.transition_timer >= self.transition_duration:
                    self.state = STATE_PLAYING
                    self.transition_alpha = 0
                return

            if self.state != STATE_PLAYING:
                return

            time_ms = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()

            # Update switch cooldown
            if self.switch_cooldown > 0:
                self.switch_cooldown -= dt

            # Get active and companion characters
            active = self.get_active_player()
            companion = self.get_companion()

            # Update active character with player input
            active.update(dt, keys, self.game_map, is_active=True)

            # Update companion with AI
            companion.update(dt, keys, self.game_map, is_active=False)
            self.companion_ai.update(companion, active, dt, self.game_map, self.current_room.enemies)

            # Get projectiles from Tristan (whether active or AI)
            for proj in self.tristan.get_queued_projectiles():
                self.projectiles.append(proj)

            # Update projectiles
            for proj in self.projectiles[:]:
                proj.update(dt, self.game_map)
                if not proj.alive:
                    self.projectiles.remove(proj)
                    continue

                # Check collision with enemies
                for enemy in self.current_room.enemies:
                    if enemy.alive and proj.get_rect().colliderect(enemy.get_rect()):
                        if enemy.take_damage():
                            self.effects.append(DeathEffect(enemy.x + enemy.width // 2,
                                                           enemy.y + enemy.height // 2))
                            self.trigger_shake(6)
                        proj.alive = False
                        break

            # Check Henry's melee attacks
            if self.henry.attacking:
                attack_rect = self.henry.get_attack_rect()
                for enemy in self.current_room.enemies:
                    if enemy.alive and attack_rect.colliderect(enemy.get_rect()):
                        if enemy.take_damage():
                            self.effects.append(DeathEffect(enemy.x + enemy.width // 2,
                                                           enemy.y + enemy.height // 2))
                            self.trigger_shake(8)

            # Update enemies
            for enemy in self.current_room.enemies:
                enemy.update(dt, self.game_map, active)

                # Check collision with both characters
                if enemy.alive:
                    for char in [self.tristan, self.henry]:
                        if char.get_rect().colliderect(enemy.get_rect()):
                            if char.take_damage():
                                self.trigger_shake(10)

            # Update shards
            for shard in self.current_room.shards:
                shard.update(dt)
                if not shard.collected:
                    for char in [self.tristan, self.henry]:
                        if char.get_rect().colliderect(shard.get_rect()):
                            shard.collected = True
                            self.shards_collected += 1
                            break

            # Check door collision for active character
            self.check_door_collision(active)

            # Update effects
            self.effects = [e for e in self.effects if e.update(dt)]

            # Update shake
            if self.shake_timer > 0:
                self.shake_timer -= dt
                self.shake_amount *= 0.9
            else:
                self.shake_amount = 0

            # Check win/lose conditions
            if self.shards_collected >= self.target_shards:
                self.state = STATE_VICTORY
            elif self.tristan.health <= 0 and self.henry.health <= 0:
                self.state = STATE_GAMEOVER

        def handle_key_down(self, key):
            if self.state != STATE_PLAYING:
                return

            # Attack
            if key == K_SPACE or key == K_j:
                self.get_active_player().attack()

            # Switch character
            if key == K_TAB or key == K_q:
                self.switch_character()

        def draw(self, surf):
            time_ms = pygame.time.get_ticks()

            # Calculate shake offset
            shake_x, shake_y = 0, 0
            if self.shake_amount > 0.5:
                shake_x = random.uniform(-self.shake_amount, self.shake_amount)
                shake_y = random.uniform(-self.shake_amount, self.shake_amount)

            # Create game surface
            game_surf = pygame.Surface((WIDTH, HEIGHT))
            game_surf.fill((30, 20, 50))

            # Draw starry background
            self.draw_background(game_surf, time_ms)

            # Draw map
            self.draw_map(game_surf, time_ms)

            # Draw shards
            for shard in self.current_room.shards:
                shard.draw(game_surf, time_ms)

            # Draw projectiles
            for proj in self.projectiles:
                proj.draw(game_surf)

            # Draw enemies
            for enemy in self.current_room.enemies:
                enemy.draw(game_surf, time_ms)

            # Draw both characters (companion first so active is on top)
            companion = self.get_companion()
            active = self.get_active_player()
            companion.draw(game_surf, time_ms, is_active=False)
            active.draw(game_surf, time_ms, is_active=True)

            # Draw effects
            for effect in self.effects:
                effect.draw(game_surf)

            # Blit with shake
            surf.blit(game_surf, (shake_x, shake_y))

            # Draw UI (no shake)
            self.draw_ui(surf)

            # Draw room transition overlay
            if self.state == STATE_TRANSITIONING and self.transition_alpha > 0:
                trans_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                trans_surf.fill((0, 0, 0, min(255, self.transition_alpha)))
                surf.blit(trans_surf, (0, 0))

            # Draw end screens
            if self.state == STATE_VICTORY:
                self.draw_overlay(surf, "BEACON RESTORED!", (100, 255, 150), "The brothers saved the light!")
            elif self.state == STATE_GAMEOVER:
                self.draw_overlay(surf, "DEFEATED", (255, 100, 100), "The shadows overwhelmed them...")

        def draw_background(self, surf, time_ms):
            """Draw starry sky background."""
            # Static stars (using time as seed for consistency)
            random.seed(42)
            for _ in range(100):
                x = random.randint(0, WIDTH)
                y = random.randint(0, HEIGHT)
                brightness = random.randint(100, 255)
                twinkle = math.sin(time_ms * 0.002 + x * 0.01) * 50
                color = int(max(50, min(255, brightness + twinkle)))
                size = 1 if random.random() > 0.1 else 2
                pygame.draw.circle(surf, (color, color, color), (x, y), size)
            random.seed()  # Reset seed

        def draw_map(self, surf, time_ms):
            """Draw the game map using tileset sprites."""
            for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    tile = self.game_map[y][x]
                    px = x * TILE_SIZE + MAP_OFFSET_X
                    py = y * TILE_SIZE + MAP_OFFSET_Y

                    if tile == TILE_FLOOR:
                        # Try to use tileset sprite
                        floor_sprite = get_floor_tile(x, y)
                        if floor_sprite:
                            surf.blit(floor_sprite, (px, py))
                        else:
                            # Fallback to procedural
                            color = (60, 50, 80) if (x + y) % 2 == 0 else (55, 45, 75)
                            pygame.draw.rect(surf, color, (px, py, TILE_SIZE, TILE_SIZE))
                            pygame.draw.rect(surf, (70, 60, 90), (px, py, TILE_SIZE, TILE_SIZE), 1)

                    elif tile == TILE_WALL:
                        # Draw floor underneath first (walls are on top of floor)
                        floor_sprite = get_floor_tile(x, y)
                        if floor_sprite:
                            surf.blit(floor_sprite, (px, py))

                        # Draw wall on top - use sprite if available
                        wall_sprite = TILE_SPRITES.get('wall_top')
                        if wall_sprite:
                            # Scale wall sprite to fit tile
                            scaled_wall = pygame.transform.scale(wall_sprite, (TILE_SIZE, TILE_SIZE))
                            surf.blit(scaled_wall, (px, py))
                        else:
                            # Fallback to procedural wall
                            pygame.draw.rect(surf, (80, 70, 100), (px, py, TILE_SIZE, TILE_SIZE))
                            pygame.draw.rect(surf, (100, 90, 120), (px + 4, py + 4, TILE_SIZE - 8, TILE_SIZE - 16))
                            pygame.draw.rect(surf, (60, 50, 80), (px, py, TILE_SIZE, TILE_SIZE), 2)

                    elif tile == TILE_BEACON:
                        # Draw floor first
                        floor_sprite = get_floor_tile(x, y)
                        if floor_sprite:
                            surf.blit(floor_sprite, (px, py))
                        else:
                            pygame.draw.rect(surf, (60, 50, 80), (px, py, TILE_SIZE, TILE_SIZE))

                        # Draw beacon pedestal/fountain sprite if available
                        fountain_sprite = TILE_SPRITES.get('fountain')
                        if fountain_sprite:
                            scaled_fountain = pygame.transform.scale(fountain_sprite, (TILE_SIZE, TILE_SIZE))
                            surf.blit(scaled_fountain, (px, py))

                        # Glowing beacon effect
                        glow = 0.5 + 0.3 * math.sin(time_ms * 0.003)
                        glow_size = int(40 + 15 * glow)

                        # Check if all shards collected
                        if self.shards_collected >= self.target_shards:
                            glow_color = (255, 220, 100, int(150 * glow))
                            beacon_color = (255, 240, 150)
                        else:
                            glow_color = (100, 80, 150, int(80 * glow))
                            beacon_color = (150, 130, 180)

                        glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
                        pygame.draw.circle(glow_surf, glow_color, (glow_size, glow_size), glow_size)
                        surf.blit(glow_surf, (px + TILE_SIZE // 2 - glow_size, py + TILE_SIZE // 2 - glow_size))

                        pygame.draw.circle(surf, beacon_color, (px + TILE_SIZE // 2, py + TILE_SIZE // 2), 15)

                    elif tile in (TILE_DOOR_N, TILE_DOOR_S, TILE_DOOR_E, TILE_DOOR_W):
                        # Draw floor first
                        floor_sprite = get_floor_tile(x, y)
                        if floor_sprite:
                            surf.blit(floor_sprite, (px, py))
                        else:
                            pygame.draw.rect(surf, (50, 40, 70), (px, py, TILE_SIZE, TILE_SIZE))

                        # Glowing portal
                        glow = 0.6 + 0.3 * math.sin(time_ms * 0.004)
                        center_x = px + TILE_SIZE // 2
                        center_y = py + TILE_SIZE // 2

                        # Outer glow
                        glow_surf = pygame.Surface((TILE_SIZE + 20, TILE_SIZE + 20), pygame.SRCALPHA)
                        pygame.draw.ellipse(glow_surf, (100, 200, 255, int(60 * glow)),
                                          (0, 0, TILE_SIZE + 20, TILE_SIZE + 20))
                        surf.blit(glow_surf, (px - 10, py - 10))

                        # Inner portal
                        pygame.draw.ellipse(surf, (80, 150, 200), (px + 8, py + 8, TILE_SIZE - 16, TILE_SIZE - 16))
                        pygame.draw.ellipse(surf, (150, 220, 255), (px + 14, py + 14, TILE_SIZE - 28, TILE_SIZE - 28))

                        # Direction indicator (arrow)
                        arrow_color = (200, 240, 255)
                        if tile == TILE_DOOR_N:
                            pygame.draw.polygon(surf, arrow_color, [(center_x, py + 18), (center_x - 8, py + 30), (center_x + 8, py + 30)])
                        elif tile == TILE_DOOR_S:
                            pygame.draw.polygon(surf, arrow_color, [(center_x, py + TILE_SIZE - 18), (center_x - 8, py + TILE_SIZE - 30), (center_x + 8, py + TILE_SIZE - 30)])
                        elif tile == TILE_DOOR_E:
                            pygame.draw.polygon(surf, arrow_color, [(px + TILE_SIZE - 18, center_y), (px + TILE_SIZE - 30, center_y - 8), (px + TILE_SIZE - 30, center_y + 8)])
                        elif tile == TILE_DOOR_W:
                            pygame.draw.polygon(surf, arrow_color, [(px + 18, center_y), (px + 30, center_y - 8), (px + 30, center_y + 8)])

                    elif tile == TILE_VOID:
                        # Nothing - void/sky
                        pass

        def draw_ui(self, surf):
            """Draw game UI."""
            font_medium = pygame.font.Font(None, 36)
            font_small = pygame.font.Font(None, 28)
            font_tiny = pygame.font.Font(None, 24)

            # Tristan health (top left) - Green
            tristan_label = font_small.render("TRISTAN", True, (100, 200, 100))
            surf.blit(tristan_label, (30, 15))

            for i in range(self.tristan.max_health):
                x = 30 + i * 35
                y = 45
                if i < self.tristan.health:
                    color = (100, 200, 100)  # Green for Tristan
                else:
                    color = (60, 50, 80)
                # Heart shape
                pygame.draw.circle(surf, color, (x, y), 10)
                pygame.draw.circle(surf, color, (x + 10, y), 10)
                pygame.draw.polygon(surf, color, [(x - 10, y + 2), (x + 20, y + 2), (x + 5, y + 18)])

            # Active indicator for Tristan
            if self.active_character == "tristan":
                pygame.draw.rect(surf, (255, 255, 100), (25, 10, 150, 55), 2)

            # Henry health (below Tristan) - Blue
            henry_label = font_small.render("HENRY", True, (100, 150, 220))
            surf.blit(henry_label, (30, 75))

            for i in range(self.henry.max_health):
                x = 30 + i * 35
                y = 105
                if i < self.henry.health:
                    color = (100, 150, 220)  # Blue for Henry
                else:
                    color = (60, 50, 80)
                # Heart shape
                pygame.draw.circle(surf, color, (x, y), 10)
                pygame.draw.circle(surf, color, (x + 10, y), 10)
                pygame.draw.polygon(surf, color, [(x - 10, y + 2), (x + 20, y + 2), (x + 5, y + 18)])

            # Active indicator for Henry
            if self.active_character == "henry":
                pygame.draw.rect(surf, (255, 255, 100), (25, 70, 150, 55), 2)

            # Ability indicators
            tristan_ability = font_tiny.render("Projectile", True, (180, 180, 150))
            surf.blit(tristan_ability, (180, 40))
            henry_ability = font_tiny.render("Sword", True, (180, 180, 150))
            surf.blit(henry_ability, (180, 100))

            # Shards (top right)
            shard_text = font_medium.render(f"Shards: {self.shards_collected}/{self.target_shards}",
                                           True, (255, 220, 100))
            surf.blit(shard_text, (WIDTH - 200, 30))

            # Room indicator
            room_names = {"start": "Hub", "north": "Beacon Chamber", "east": "Gauntlet", "west": "Treasury"}
            room_text = font_small.render(f"Room: {room_names.get(self.current_room_id, self.current_room_id)}",
                                         True, (150, 140, 180))
            surf.blit(room_text, (WIDTH - 200, 60))

            # Controls hint (bottom)
            controls = font_small.render("WASD: Move | SPACE: Attack | TAB/Q: Switch Character", True, (150, 140, 180))
            surf.blit(controls, (WIDTH // 2 - controls.get_width() // 2, HEIGHT - 40))

            # Objective
            if self.shards_collected < self.target_shards:
                obj_text = font_small.render("Collect all beacon shards!", True, (200, 180, 255))
            else:
                obj_text = font_small.render("Return to the beacon!", True, (100, 255, 150))
            surf.blit(obj_text, (WIDTH // 2 - obj_text.get_width() // 2, 30))

        def draw_overlay(self, surf, title, color, subtitle):
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


# Ren'Py Displayable wrapper
init python:
    class BeaconQuestDisplayable(renpy.Displayable):
        """Ren'Py displayable wrapper for Beacon Quest."""

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


# Screen
screen beacon_quest_screen():
    default game_display = BeaconQuestDisplayable()

    add Solid("#1e1432")
    add game_display

    key "K_ESCAPE" action Return("quit")


# Entry label
label beacon_quest_start():
    $ quick_menu = False
    $ disable_minigame_conflicts()

    call screen beacon_quest_screen()

    $ restore_minigame_conflicts()
    $ quick_menu = True
    $ result = _return

    if result == "victory":
        return True
    else:
        return False


# Test label
label test_beacon_quest:
    "Starting Beacon Quest!"
    "Collect the beacon shards and defeat the shadow creatures!"

    call beacon_quest_start()

    if _return:
        "The beacon shines with renewed power!"
    else:
        "The shadows have won... for now."

    return
