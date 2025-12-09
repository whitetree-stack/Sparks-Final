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
    TILE_SIZE = 80  # Increased from 64 for better visibility

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

    # ----------------------------------------------------------------
    # TILESET LOADING (Individual tile files)
    # ----------------------------------------------------------------
    # Floor tiles: images/tileset/floor/[1,2,3]/[1-5].png
    # Wall chunks: images/tileset/chunks/*.png

    TILESET_LOADED = False
    TILE_SPRITES = {}
    FLOOR_TILES = []  # List of floor tile surfaces
    WALL_CHUNKS = {}  # Named wall/decoration pieces

    # Floor tile configuration
    FLOOR_TILE_PATH = "images/tileset/floor/"
    FLOOR_COLOR_VARIANT = 1  # Which color folder to use (1, 2, or 3)
    FLOOR_TILE_COUNT = 5     # Number of tiles per folder

    # Wall chunk configuration
    WALL_CHUNK_PATH = "images/tileset/chunks/"

    def load_tileset():
        """Load tiles from individual image files."""
        global TILESET_LOADED, TILE_SPRITES, FLOOR_TILES, WALL_CHUNKS

        if TILESET_LOADED:
            return True

        loaded_count = 0

        # Load floor tiles from the selected color variant folder
        floor_folder = f"{FLOOR_TILE_PATH}{FLOOR_COLOR_VARIANT}/"
        for i in range(1, FLOOR_TILE_COUNT + 1):
            filepath = f"{floor_folder}{i}.png"
            tile = load_image(filepath)
            if tile:
                # Scale from 64x64 to TILE_SIZE
                scaled = pygame.transform.scale(tile, (TILE_SIZE, TILE_SIZE))
                FLOOR_TILES.append(scaled)
                TILE_SPRITES[f'floor_{i}'] = scaled
                loaded_count += 1
            else:
                print(f"Failed to load floor tile: {filepath}")

        # Load wall chunks
        wall_chunk_files = {
            'wall_top_1': 'tan_wall_top1.png',
            'wall_top_2': 'tan_wall_top2.png',
            'wall_top_3': 'tan_wall_top_3.png',
            'wall_bottom': 'top_of_wall_for_bottom_edge.png',
            'wall_left': 'wall_left.png',
            'wall_right': 'wall_right.png',
            'doorway_top': 'doorway_top.png',
            'doorway_stairs': 'doorway_stairs_top.png',
            'pillar_1': 'pillar1.png',
            'pillar_2': 'pillar2.png',
            'pillar_3': 'pillar3.png',
            'pillar_4': 'pillar4.png',
            'pillars_window': 'pillars_window_seethrough.png',
            'sewer_grate': 'sewer_grate.png',
            'stairs_left': 'stairs_floor_left.png',
            'stairs_right': 'stairs_floor_right.png',
        }

        for name, filename in wall_chunk_files.items():
            filepath = f"{WALL_CHUNK_PATH}{filename}"
            chunk = load_image(filepath)
            if chunk:
                WALL_CHUNKS[name] = chunk
                TILE_SPRITES[name] = chunk
                loaded_count += 1
            else:
                print(f"Failed to load wall chunk: {filepath}")

        if loaded_count > 0:
            TILESET_LOADED = True
            print(f"Loaded {loaded_count} tiles ({len(FLOOR_TILES)} floor, {len(WALL_CHUNKS)} chunks)")
            return True
        else:
            print("No tiles loaded - using procedural rendering")
            return False

    def get_floor_tile(x, y):
        """Get a floor tile sprite based on position (for consistent variation)."""
        if not FLOOR_TILES:
            return None
        # Use position to deterministically select a tile variation
        index = (x * 7 + y * 13 + (x * y) % 5) % len(FLOOR_TILES)
        return FLOOR_TILES[index]

    def get_wall_chunk(name):
        """Get a wall chunk sprite by name."""
        return WALL_CHUNKS.get(name)

    # ----------------------------------------------------------------
    # SLIME ENEMY SPRITES
    # ----------------------------------------------------------------
    SLIME_SPRITESHEET_PATH = "images/enemies/slime/green_slime.png"
    SLIME_FRAME_SIZE = 48
    SLIME_COLS = 10
    SLIME_ROWS = 9
    SLIME_SPRITES_LOADED = False
    SLIME_FRAMES = {}

    # Animation definitions: (row, start_col, num_frames)
    SLIME_ANIMATIONS = {
        'idle': (0, 0, 4),       # Row 0, frames 0-3: idle bounce
        'move': (1, 0, 4),       # Row 1, frames 0-3: movement
        'attack': (4, 0, 3),     # Row 4, frames 0-2: attack (star form)
        'hurt': (6, 0, 2),       # Row 6, frames 0-1: hurt (with hearts)
        'death': (2, 6, 3),      # Row 2, frames 6-8: smaller/death
    }

    def load_slime_sprites():
        """Load slime enemy sprites from spritesheet."""
        global SLIME_SPRITES_LOADED, SLIME_FRAMES

        if SLIME_SPRITES_LOADED:
            return True

        try:
            spritesheet = load_image(SLIME_SPRITESHEET_PATH)
            if spritesheet is None:
                print("Failed to load slime spritesheet")
                return False

            # Extract animation frames
            for anim_name, (row, start_col, num_frames) in SLIME_ANIMATIONS.items():
                SLIME_FRAMES[anim_name] = []
                for i in range(num_frames):
                    col = start_col + i
                    x = col * SLIME_FRAME_SIZE
                    y = row * SLIME_FRAME_SIZE

                    # Create frame surface
                    frame = pygame.Surface((SLIME_FRAME_SIZE, SLIME_FRAME_SIZE), pygame.SRCALPHA)
                    frame.blit(spritesheet, (0, 0), (x, y, SLIME_FRAME_SIZE, SLIME_FRAME_SIZE))

                    # Scale up to match game size (48 -> 64)
                    scaled_frame = pygame.transform.scale(frame, (TILE_SIZE, TILE_SIZE))
                    SLIME_FRAMES[anim_name].append(scaled_frame)

            SLIME_SPRITES_LOADED = True
            print(f"Loaded slime sprites: {list(SLIME_FRAMES.keys())}")
            return True
        except Exception as e:
            print(f"Error loading slime sprites: {e}")
            return False

    def get_slime_frame(anim_name, frame_index):
        """Get a specific slime animation frame."""
        if anim_name not in SLIME_FRAMES:
            return None
        frames = SLIME_FRAMES[anim_name]
        if not frames:
            return None
        return frames[frame_index % len(frames)]

    # ----------------------------------------------------------------
    # VAMPIRE ENEMY SPRITES
    # ----------------------------------------------------------------
    VAMPIRE_SPRITE_PATH = "images/enemies/vampires/"
    VAMPIRE_FRAME_SIZE = 64
    VAMPIRE_SPRITES_LOADED = False
    VAMPIRE_FRAMES = {}  # Organized as: VAMPIRE_FRAMES[anim_name][direction] = [frames]

    # Spritesheet definitions: filename -> (cols, rows)
    VAMPIRE_SPRITESHEETS = {
        'idle': ('vampire_idle.png', 4, 4),
        'walk': ('vampire_walk.png', 6, 4),
        'run': ('vampire_run.png', 8, 4),
        'attack': ('vampire_attack.png', 10, 4),
        'hurt': ('vampire_hurt.png', 4, 4),
        'death': ('vampire_death.png', 10, 4),
    }

    # Direction row mapping (row index -> direction name)
    VAMPIRE_DIRECTIONS = {
        0: 'down',
        1: 'up',
        2: 'left',
        3: 'right'
    }

    def load_vampire_sprites():
        """Load vampire enemy sprites from multiple spritesheets."""
        global VAMPIRE_SPRITES_LOADED, VAMPIRE_FRAMES

        if VAMPIRE_SPRITES_LOADED:
            return True

        try:
            for anim_name, (filename, cols, rows) in VAMPIRE_SPRITESHEETS.items():
                filepath = VAMPIRE_SPRITE_PATH + filename
                spritesheet = load_image(filepath)

                if spritesheet is None:
                    print(f"Failed to load vampire spritesheet: {filepath}")
                    continue

                VAMPIRE_FRAMES[anim_name] = {}

                # Extract frames for each direction
                for row in range(min(rows, 4)):  # 4 directions
                    direction = VAMPIRE_DIRECTIONS.get(row, 'down')
                    VAMPIRE_FRAMES[anim_name][direction] = []

                    for col in range(cols):
                        x = col * VAMPIRE_FRAME_SIZE
                        y = row * VAMPIRE_FRAME_SIZE

                        # Create frame surface
                        frame = pygame.Surface((VAMPIRE_FRAME_SIZE, VAMPIRE_FRAME_SIZE), pygame.SRCALPHA)
                        frame.blit(spritesheet, (0, 0), (x, y, VAMPIRE_FRAME_SIZE, VAMPIRE_FRAME_SIZE))

                        VAMPIRE_FRAMES[anim_name][direction].append(frame)

            VAMPIRE_SPRITES_LOADED = True
            print(f"Loaded vampire sprites: {list(VAMPIRE_FRAMES.keys())}")
            return True
        except Exception as e:
            print(f"Error loading vampire sprites: {e}")
            return False

    def get_vampire_frame(anim_name, direction, frame_index):
        """Get a specific vampire animation frame for a direction."""
        if anim_name not in VAMPIRE_FRAMES:
            return None
        if direction not in VAMPIRE_FRAMES[anim_name]:
            direction = 'down'  # Fallback
        frames = VAMPIRE_FRAMES[anim_name].get(direction, [])
        if not frames:
            return None
        return frames[frame_index % len(frames)]

    # ----------------------------------------------------------------
    # ORC ENEMY SPRITES
    # ----------------------------------------------------------------
    ORC_SPRITE_PATH = "images/enemies/orcs/"
    ORC_FRAME_SIZE = 64
    ORC_SPRITES_LOADED = False
    ORC_FRAMES = {}  # Organized as: ORC_FRAMES[anim_name][direction] = [frames]

    # Spritesheet definitions: filename -> (cols, rows)
    ORC_SPRITESHEETS = {
        'idle': ('orc_idle.png', 4, 4),
        'walk': ('orc_walk.png', 6, 4),
        'run': ('orc_run.png', 8, 4),
        'attack': ('orc_attack.png', 8, 4),
        'hurt': ('orc_hurt.png', 6, 4),
        'death': ('orc_death.png', 8, 4),
    }

    # Direction row mapping (same as vampire)
    ORC_DIRECTIONS = {
        0: 'down',
        1: 'up',
        2: 'left',
        3: 'right'
    }

    def load_orc_sprites():
        """Load orc enemy sprites from multiple spritesheets."""
        global ORC_SPRITES_LOADED, ORC_FRAMES

        if ORC_SPRITES_LOADED:
            return True

        try:
            for anim_name, (filename, cols, rows) in ORC_SPRITESHEETS.items():
                filepath = ORC_SPRITE_PATH + filename
                spritesheet = load_image(filepath)

                if spritesheet is None:
                    print(f"Failed to load orc spritesheet: {filepath}")
                    continue

                ORC_FRAMES[anim_name] = {}

                # Extract frames for each direction
                for row in range(min(rows, 4)):  # 4 directions
                    direction = ORC_DIRECTIONS.get(row, 'down')
                    ORC_FRAMES[anim_name][direction] = []

                    for col in range(cols):
                        x = col * ORC_FRAME_SIZE
                        y = row * ORC_FRAME_SIZE

                        # Create frame surface
                        frame = pygame.Surface((ORC_FRAME_SIZE, ORC_FRAME_SIZE), pygame.SRCALPHA)
                        frame.blit(spritesheet, (0, 0), (x, y, ORC_FRAME_SIZE, ORC_FRAME_SIZE))

                        ORC_FRAMES[anim_name][direction].append(frame)

            ORC_SPRITES_LOADED = True
            print(f"Loaded orc sprites: {list(ORC_FRAMES.keys())}")
            return True
        except Exception as e:
            print(f"Error loading orc sprites: {e}")
            return False

    def get_orc_frame(anim_name, direction, frame_index):
        """Get a specific orc animation frame for a direction."""
        if anim_name not in ORC_FRAMES:
            return None
        if direction not in ORC_FRAMES[anim_name]:
            direction = 'down'  # Fallback
        frames = ORC_FRAMES[anim_name].get(direction, [])
        if not frames:
            return None
        return frames[frame_index % len(frames)]

    # ----------------------------------------------------------------
    # SPIDER ENEMY SPRITES (from valley climb)
    # ----------------------------------------------------------------
    SPIDER_SPRITE_PATH = "images/enemies/spiders/images/"
    SPIDER_SPRITES_LOADED = False
    SPIDER_FRAMES = {}  # Organized as: SPIDER_FRAMES[direction] = [frames]

    # Spider frame mappings (individual files, not spritesheet)
    SPIDER_FRAME_RANGES = {
        'up': range(1, 6),       # 1.png to 5.png
        'left': range(7, 12),    # 7.png to 11.png
        'down': range(21, 26),   # 21.png to 25.png
        'right': range(27, 32),  # 27.png to 31.png
        'death': range(41, 45),  # 41.png to 44.png
    }

    def load_spider_sprites():
        """Load spider enemy sprites from individual files."""
        global SPIDER_SPRITES_LOADED, SPIDER_FRAMES

        if SPIDER_SPRITES_LOADED:
            return True

        try:
            for direction, frame_range in SPIDER_FRAME_RANGES.items():
                SPIDER_FRAMES[direction] = []
                for i in frame_range:
                    filepath = f"{SPIDER_SPRITE_PATH}{i}.png"
                    frame = load_image(filepath)

                    if frame is None:
                        print(f"Failed to load spider frame: {filepath}")
                        continue

                    # Scale to game tile size
                    scaled = pygame.transform.smoothscale(frame, (TILE_SIZE, TILE_SIZE))
                    SPIDER_FRAMES[direction].append(scaled)

            SPIDER_SPRITES_LOADED = True
            print(f"Loaded spider sprites: {list(SPIDER_FRAMES.keys())}")
            return True
        except Exception as e:
            print(f"Error loading spider sprites: {e}")
            return False

    def get_spider_frame(direction, frame_index):
        """Get a specific spider animation frame for a direction."""
        if direction not in SPIDER_FRAMES:
            direction = 'down'
        frames = SPIDER_FRAMES.get(direction, [])
        if not frames:
            return None
        return frames[frame_index % len(frames)]

    # Default map dimensions (rooms can override)
    DEFAULT_MAP_WIDTH = 20
    DEFAULT_MAP_HEIGHT = 13

    # Legacy constants for backwards compatibility
    MAP_WIDTH = DEFAULT_MAP_WIDTH
    MAP_HEIGHT = DEFAULT_MAP_HEIGHT

    # Viewport dimensions (what the camera shows)
    VIEWPORT_WIDTH = WIDTH
    VIEWPORT_HEIGHT = HEIGHT
    VIEWPORT_TILES_X = VIEWPORT_WIDTH // TILE_SIZE + 2  # Extra tiles for smooth scrolling
    VIEWPORT_TILES_Y = VIEWPORT_HEIGHT // TILE_SIZE + 2

    # Camera settings
    CAMERA_FOLLOW_SPEED = 0.08  # Lerp factor (0-1, higher = snappier)
    CAMERA_DEADZONE_X = 100  # Pixels player can move before camera follows (horizontal)
    CAMERA_DEADZONE_Y = 60   # Pixels player can move before camera follows (vertical)

    # Legacy offsets (will be replaced by camera system)
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

            # Check wall collision (world coordinates)
            tile_x = int(self.x // TILE_SIZE)
            tile_y = int(self.y // TILE_SIZE)

            map_height = len(game_map)
            map_width = len(game_map[0]) if game_map else 0

            if tile_x < 0 or tile_x >= map_width or tile_y < 0 or tile_y >= map_height:
                self.alive = False
                return

            tile = game_map[tile_y][tile_x]
            if tile in (TILE_WALL, TILE_VOID):
                self.alive = False

        def get_rect(self):
            return pygame.Rect(self.x - self.radius, self.y - self.radius,
                             self.radius * 2, self.radius * 2)

        def draw(self, surf, cam_x=0, cam_y=0):
            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -50 or screen_x > WIDTH + 50 or screen_y < -50 or screen_y > HEIGHT + 50:
                return

            # Draw trail with decreasing opacity
            for i, (tx, ty) in enumerate(self.trail):
                trail_screen_x = tx - cam_x
                trail_screen_y = ty - cam_y
                alpha = int(120 * (i + 1) / len(self.trail) * self.pulse)
                trail_radius = int(self.radius * (i + 1) / len(self.trail) * 0.6)
                if trail_radius > 0:
                    trail_surf = pygame.Surface((trail_radius * 2 + 4, trail_radius * 2 + 4), pygame.SRCALPHA)
                    trail_color = (*self.glow_color[:3], alpha)
                    pygame.draw.circle(trail_surf, trail_color, (trail_radius + 2, trail_radius + 2), trail_radius)
                    surf.blit(trail_surf, (int(trail_screen_x) - trail_radius - 2, int(trail_screen_y) - trail_radius - 2))

            # Draw glow
            glow_size = int(self.radius * 2.5 * self.pulse)
            glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*self.glow_color, 60), (glow_size, glow_size), glow_size)
            surf.blit(glow_surf, (int(screen_x) - glow_size, int(screen_y) - glow_size))

            # Draw core
            pygame.draw.circle(surf, (255, 255, 255), (int(screen_x), int(screen_y)), int(self.radius * 0.7))
            pygame.draw.circle(surf, self.color, (int(screen_x), int(screen_y)), self.radius)


    class Character:
        """Base class for playable characters."""
        def __init__(self, x, y, char_type="tristan"):
            # World coordinates (no MAP_OFFSET)
            self.x = x * TILE_SIZE
            self.y = y * TILE_SIZE
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
            self.x = x * TILE_SIZE
            self.y = y * TILE_SIZE
            self.tile_x = x
            self.tile_y = y

        def set_pixel_position(self, px, py):
            """Set position in pixel coordinates (world coords)."""
            self.x = px
            self.y = py
            self.tile_x = int((self.x + self.width // 2) // TILE_SIZE)
            self.tile_y = int((self.y + self.height // 2) // TILE_SIZE)

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

            # Update tile position (world coordinates)
            self.tile_x = int((self.x + self.width // 2) // TILE_SIZE)
            self.tile_y = int((self.y + self.height // 2) // TILE_SIZE)

        def can_move_to(self, new_x, new_y, game_map):
            """Check if character can move to position (world coordinates)."""
            # Get room dimensions from map
            map_height = len(game_map)
            map_width = len(game_map[0]) if game_map else 0

            corners = [
                (new_x + 8, new_y + 8),
                (new_x + self.width - 8, new_y + 8),
                (new_x + 8, new_y + self.height - 8),
                (new_x + self.width - 8, new_y + self.height - 8),
            ]

            for cx, cy in corners:
                tile_x = int(cx // TILE_SIZE)
                tile_y = int(cy // TILE_SIZE)

                if tile_x < 0 or tile_x >= map_width or tile_y < 0 or tile_y >= map_height:
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

        def draw(self, surf, time_ms, is_active=True, cam_x=0, cam_y=0):
            """Draw the character."""
            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -100 or screen_x > WIDTH + 100 or screen_y < -100 or screen_y > HEIGHT + 100:
                return

            # Flash when invulnerable
            if self.invulnerable > 0 and (time_ms // 100) % 2 == 0:
                return

            # Draw shadow
            shadow_surf = pygame.Surface((self.width, 20), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
            surf.blit(shadow_surf, (screen_x, screen_y + self.height - 10))

            # Draw body with bobbing
            body_offset = 0
            if self.moving:
                body_offset = math.sin(time_ms * 0.015) * 3

            pygame.draw.rect(surf, self.outline, (screen_x + 4, screen_y + body_offset + 4, self.width - 8, self.height - 8))
            pygame.draw.rect(surf, self.color, (screen_x + 6, screen_y + body_offset + 6, self.width - 12, self.height - 12))

            # Draw active indicator (glowing ring around active character)
            if is_active:
                indicator_surf = pygame.Surface((self.width + 16, self.height + 16), pygame.SRCALPHA)
                pulse = 0.5 + 0.3 * math.sin(time_ms * 0.008)
                pygame.draw.rect(indicator_surf, (255, 255, 100, int(80 * pulse)),
                               (0, 0, self.width + 16, self.height + 16), 3)
                surf.blit(indicator_surf, (screen_x - 8, screen_y + body_offset - 8))

            # Draw face based on direction
            face_x = screen_x + self.width // 2
            face_y = screen_y + self.height // 2 + body_offset - 5

            eye_offset = {'up': (0, -8), 'down': (0, 8), 'left': (-8, 0), 'right': (8, 0)}
            ex, ey = eye_offset[self.facing]

            pygame.draw.circle(surf, (255, 255, 255), (int(face_x - 8), int(face_y)), 6)
            pygame.draw.circle(surf, (255, 255, 255), (int(face_x + 8), int(face_y)), 6)
            pygame.draw.circle(surf, (40, 40, 40), (int(face_x - 8 + ex // 2), int(face_y + ey // 2)), 3)
            pygame.draw.circle(surf, (40, 40, 40), (int(face_x + 8 + ex // 2), int(face_y + ey // 2)), 3)

            # Draw attack effect if attacking
            if self.attacking:
                self.draw_attack(surf, time_ms, cam_x, cam_y)

        def draw_attack(self, surf, time_ms, cam_x=0, cam_y=0):
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

        def draw_attack(self, surf, time_ms, cam_x=0, cam_y=0):
            """Draw projectile firing effect."""
            if not self.attacking:
                return

            progress = self.attack_timer / self.attack_duration
            cx, cy = self.get_center()
            # Apply camera offset
            cx -= cam_x
            cy -= cam_y

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

        def draw_attack(self, surf, time_ms, cam_x=0, cam_y=0):
            """Draw sword swing effect."""
            if not self.attacking:
                return

            progress = self.attack_timer / self.attack_duration
            # Apply camera offset
            cx = self.x + self.width // 2 - cam_x
            cy = self.y + self.height // 2 - cam_y

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
            pygame.draw.line(surf, (180, 200, 230), (int(cx), int(cy)), (int(end_x), int(end_y)), swing_width + 3)
            pygame.draw.line(surf, (220, 240, 255), (int(cx), int(cy)), (int(end_x), int(end_y)), swing_width)

            # Sparkle at tip
            sparkle_size = 5 + int(4 * math.sin(progress * math.pi))
            pygame.draw.circle(surf, (200, 220, 255), (int(end_x), int(end_y)), sparkle_size)


    class CompanionAI:
        """AI controller for the non-active character with A* pathfinding."""
        def __init__(self):
            self.follow_distance = 80      # Desired distance from leader
            self.min_distance = 50         # Don't get closer than this
            self.attack_range = 150        # Range to auto-attack enemies
            self.attack_check_timer = 0
            self.move_timer = 0

            # Pathfinding
            self.current_path = []
            self.path_update_timer = 0
            self.path_update_interval = 150  # Recalculate path more frequently
            self.stuck_timer = 0
            self.last_distance_to_leader = 0  # Track progress by distance, not position
            self.no_progress_timer = 0        # Time spent not getting closer

        def find_path(self, start_tile, end_tile, game_map):
            """A* pathfinding from start to end tile."""
            import heapq

            map_height = len(game_map)
            map_width = len(game_map[0]) if game_map else 0

            def heuristic(a, b):
                return abs(a[0] - b[0]) + abs(a[1] - b[1])

            def is_walkable(x, y):
                if x < 0 or x >= map_width or y < 0 or y >= map_height:
                    return False
                tile = game_map[y][x]
                return tile not in (TILE_WALL, TILE_VOID)

            start = (int(start_tile[0]), int(start_tile[1]))
            end = (int(end_tile[0]), int(end_tile[1]))

            if not is_walkable(end[0], end[1]):
                # Find nearest walkable tile to target
                for radius in range(1, 5):
                    for dx in range(-radius, radius + 1):
                        for dy in range(-radius, radius + 1):
                            test = (end[0] + dx, end[1] + dy)
                            if is_walkable(test[0], test[1]):
                                end = test
                                break
                    else:
                        continue
                    break

            # A* algorithm
            open_set = []
            heapq.heappush(open_set, (0, start))
            came_from = {}
            g_score = {start: 0}
            f_score = {start: heuristic(start, end)}

            iterations = 0
            max_iterations = 500  # Prevent infinite loops

            while open_set and iterations < max_iterations:
                iterations += 1
                current = heapq.heappop(open_set)[1]

                if current == end:
                    # Reconstruct path
                    path = []
                    while current in came_from:
                        path.append(current)
                        current = came_from[current]
                    path.reverse()
                    return path

                # Check neighbors (4-directional)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    neighbor = (current[0] + dx, current[1] + dy)

                    if not is_walkable(neighbor[0], neighbor[1]):
                        continue

                    tentative_g = g_score[current] + 1

                    if neighbor not in g_score or tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

            return []  # No path found

        def update(self, follower, leader, dt, game_map, enemies):
            """Update the follower AI with pathfinding."""
            self.move_timer += dt
            self.attack_check_timer += dt
            self.path_update_timer += dt

            # Calculate distance to leader
            dx = leader.x - follower.x
            dy = leader.y - follower.y
            dist = math.hypot(dx, dy)

            # Follow behavior
            follower.moving = False

            if dist > self.follow_distance:
                # Track progress - are we getting closer to the leader?
                progress_threshold = 2.0  # Minimum pixels closer per update to count as progress
                if self.last_distance_to_leader > 0:
                    progress = self.last_distance_to_leader - dist
                    if progress < progress_threshold:
                        self.no_progress_timer += dt
                    else:
                        self.no_progress_timer = 0
                        # Making good progress - can clear path and use direct movement
                        if progress > 5:
                            self.current_path = []
                self.last_distance_to_leader = dist

                # Decide: use pathfinding or direct movement
                use_pathfinding = (
                    self.no_progress_timer > 100 or  # Not making progress for 100ms
                    len(self.current_path) > 0       # Already have an active path
                )

                if use_pathfinding:
                    # Update path periodically
                    if self.path_update_timer >= self.path_update_interval or not self.current_path:
                        self.path_update_timer = 0

                        # Get tile positions
                        follower_tile = (
                            int((follower.x + follower.width // 2) // TILE_SIZE),
                            int((follower.y + follower.height // 2) // TILE_SIZE)
                        )
                        leader_tile = (
                            int((leader.x + leader.width // 2) // TILE_SIZE),
                            int((leader.y + leader.height // 2) // TILE_SIZE)
                        )

                        new_path = self.find_path(follower_tile, leader_tile, game_map)
                        if new_path:
                            self.current_path = new_path

                    # Follow the path
                    if self.current_path:
                        next_tile = self.current_path[0]
                        target_x = next_tile[0] * TILE_SIZE + TILE_SIZE // 2 - follower.width // 2
                        target_y = next_tile[1] * TILE_SIZE + TILE_SIZE // 2 - follower.height // 2

                        path_dx = target_x - follower.x
                        path_dy = target_y - follower.y
                        path_dist = math.hypot(path_dx, path_dy)

                        if path_dist < 8:  # Reached waypoint
                            self.current_path.pop(0)
                            self.no_progress_timer = 0  # Reset on waypoint reach
                        elif path_dist > 0:
                            move_x = (path_dx / path_dist) * follower.speed * 0.95
                            move_y = (path_dy / path_dist) * follower.speed * 0.95

                            # Try to move toward the waypoint
                            new_x = follower.x + move_x
                            new_y = follower.y + move_y

                            moved = False
                            if follower.can_move_to(new_x, new_y, game_map):
                                follower.x = new_x
                                follower.y = new_y
                                moved = True
                            else:
                                # Try axis-separated movement
                                if follower.can_move_to(new_x, follower.y, game_map):
                                    follower.x = new_x
                                    moved = True
                                if follower.can_move_to(follower.x, new_y, game_map):
                                    follower.y = new_y
                                    moved = True

                            if moved:
                                follower.moving = True

                else:
                    # Direct movement toward leader (no obstacles expected)
                    if dist > 0:
                        move_x = (dx / dist) * follower.speed * 0.95
                        move_y = (dy / dist) * follower.speed * 0.95

                        new_x = follower.x + move_x
                        new_y = follower.y + move_y

                        if follower.can_move_to(new_x, new_y, game_map):
                            follower.x = new_x
                            follower.y = new_y
                            follower.moving = True
                        else:
                            # Hit obstacle - switch to pathfinding next frame
                            self.no_progress_timer = 200

                # Update facing based on movement direction
                if follower.moving:
                    if abs(dx) > abs(dy):
                        follower.facing = 'right' if dx > 0 else 'left'
                    else:
                        follower.facing = 'down' if dy > 0 else 'up'

                # Update tile position (world coordinates)
                follower.tile_x = int((follower.x + follower.width // 2) // TILE_SIZE)
                follower.tile_y = int((follower.y + follower.height // 2) // TILE_SIZE)

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


    def validate_spawn_position(x, y, game_map):
        """Check if a tile position is valid for spawning (not in a wall)."""
        map_height = len(game_map)
        map_width = len(game_map[0]) if game_map else 0

        if x < 0 or x >= map_width or y < 0 or y >= map_height:
            return False

        tile = game_map[y][x]
        return tile not in (TILE_WALL, TILE_VOID)


    def find_nearest_valid_spawn(x, y, game_map, max_radius=5):
        """Find the nearest valid spawn position to the given coordinates."""
        if validate_spawn_position(x, y, game_map):
            return (x, y)

        # Search in expanding squares
        for radius in range(1, max_radius + 1):
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if abs(dx) == radius or abs(dy) == radius:  # Only check border
                        test_x, test_y = x + dx, y + dy
                        if validate_spawn_position(test_x, test_y, game_map):
                            return (test_x, test_y)

        # No valid position found, return original (will likely cause issues)
        print(f"Warning: No valid spawn found near ({x}, {y})")
        return (x, y)


    class Enemy:
        """A shadow enemy."""
        def __init__(self, x, y, enemy_type="shadow"):
            # World coordinates (no MAP_OFFSET)
            self.x = x * TILE_SIZE
            self.y = y * TILE_SIZE
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
            """Check if enemy can move to position (world coordinates)."""
            # Get map dimensions
            map_height = len(game_map)
            map_width = len(game_map[0]) if game_map else 0

            corners = [
                (new_x + 8, new_y + 8),
                (new_x + self.width - 8, new_y + 8),
                (new_x + 8, new_y + self.height - 8),
                (new_x + self.width - 8, new_y + self.height - 8),
            ]

            for cx, cy in corners:
                tile_x = int(cx // TILE_SIZE)
                tile_y = int(cy // TILE_SIZE)

                if tile_x < 0 or tile_x >= map_width or tile_y < 0 or tile_y >= map_height:
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

        def draw(self, surf, time_ms, cam_x=0, cam_y=0):
            if not self.alive:
                return

            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -100 or screen_x > WIDTH + 100 or screen_y < -100 or screen_y > HEIGHT + 100:
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
            surf.blit(shadow_surf, (screen_x, screen_y + self.height - 5))

            # Body (shadowy blob)
            body_surf = pygame.Surface((self.width + 10, self.height + 10), pygame.SRCALPHA)

            # Outer glow
            pygame.draw.ellipse(body_surf, (100, 50, 130, 100),
                              (0, 0, self.width + 10, self.height + 10))

            # Main body
            pygame.draw.ellipse(body_surf, color,
                              (5, 5, self.width, self.height - 5))

            surf.blit(body_surf, (screen_x - 5, screen_y + bob - 5))

            # Evil eyes
            eye_y = screen_y + self.height // 3 + bob
            pygame.draw.circle(surf, (255, 100, 100), (int(screen_x + 15), int(eye_y)), 6)
            pygame.draw.circle(surf, (255, 100, 100), (int(screen_x + self.width - 15), int(eye_y)), 6)
            pygame.draw.circle(surf, (255, 200, 200), (int(screen_x + 15), int(eye_y)), 3)
            pygame.draw.circle(surf, (255, 200, 200), (int(screen_x + self.width - 15), int(eye_y)), 3)


    class SlimeEnemy(Enemy):
        """A slime enemy with sprite-based animations."""
        def __init__(self, x, y):
            super().__init__(x, y, enemy_type="slime")
            self.width = TILE_SIZE
            self.height = TILE_SIZE
            self.speed = 1.5  # Slimes are slower

            # Animation state
            self.current_anim = 'idle'
            self.anim_frame = 0
            self.anim_timer = 0
            self.anim_speed = 150  # ms per frame

            # Slime-specific properties
            self.is_attacking = False
            self.attack_timer = 0
            self.death_timer = 0
            self.is_dying = False
            self.pause_timer = 0

        def update(self, dt, game_map, player):
            if self.is_dying:
                self.death_timer += dt
                self.anim_timer += dt
                # Get death animation frame count
                death_frames = len(SLIME_FRAMES.get('death', [None, None, None]))
                # Only advance frame if not at last frame
                if self.anim_timer >= self.anim_speed and self.anim_frame < death_frames - 1:
                    self.anim_timer = 0
                    self.anim_frame += 1
                # Freeze on final frame - never set alive = False
                return

            if not self.alive:
                return

            # Update animation
            self.anim_timer += dt
            if self.anim_timer >= self.anim_speed:
                self.anim_timer = 0
                self.anim_frame += 1

            # Handle attack animation
            if self.is_attacking:
                self.attack_timer += dt
                self.current_anim = 'attack'
                if self.attack_timer >= 400:
                    self.is_attacking = False
                    self.attack_timer = 0
                return

            # Hit flash timer - use hurt animation
            if self.hit_flash > 0:
                self.hit_flash -= dt
                self.current_anim = 'hurt'
                return

            # Pause behavior while wandering
            if self.pause_timer > 0:
                self.pause_timer -= dt
                self.current_anim = 'idle'
                return

            # Parent movement logic
            self.move_timer += dt
            if self.move_timer >= self.move_duration:
                self.move_timer = 0
                self.move_duration = random.randint(800, 2000)
                self.direction = random.choice(['up', 'down', 'left', 'right'])
                # Random chance to pause
                if random.random() < 0.4:
                    self.pause_timer = random.randint(300, 800)
                    return

            # Move towards player occasionally (less aggressive than shadow)
            if random.random() < 0.01:
                dx = player.x - self.x
                dy = player.y - self.y
                if abs(dx) > abs(dy):
                    self.direction = 'right' if dx > 0 else 'left'
                else:
                    self.direction = 'down' if dy > 0 else 'up'

                # Chance to attack if close
                dist = math.sqrt(dx*dx + dy*dy)
                if dist < TILE_SIZE * 2 and random.random() < 0.3:
                    self.is_attacking = True
                    self.anim_frame = 0

            # Move
            dir_vec = DIRECTIONS[self.direction]
            new_x = self.x + dir_vec[0] * self.speed
            new_y = self.y + dir_vec[1] * self.speed

            if self.can_move_to(new_x, new_y, game_map):
                self.x = new_x
                self.y = new_y
                self.current_anim = 'move'
            else:
                self.direction = random.choice(['up', 'down', 'left', 'right'])
                self.current_anim = 'idle'

        def take_damage(self, amount=1):
            self.health -= amount
            self.hit_flash = 200
            self.anim_frame = 0
            if self.health <= 0:
                self.is_dying = True
                self.current_anim = 'death'
                self.anim_frame = 0
                return True
            return False

        def draw(self, surf, time_ms, cam_x=0, cam_y=0):
            if not self.alive and not self.is_dying:
                return

            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -100 or screen_x > WIDTH + 100 or screen_y < -100 or screen_y > HEIGHT + 100:
                return

            # Get the appropriate animation frame
            frame = get_slime_frame(self.current_anim, self.anim_frame)

            if frame:
                # Only apply red tint if hurt animation doesn't exist
                if self.hit_flash > 0 and self.current_anim != 'hurt':
                    # Create a red-tinted version
                    tinted = frame.copy()
                    tint_surf = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
                    tint_surf.fill((255, 100, 100, 100))
                    tinted.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
                    frame = tinted

                # No death fade - enemy freezes on final frame

                # Draw shadow
                shadow_surf = pygame.Surface((self.width, 20), pygame.SRCALPHA)
                pygame.draw.ellipse(shadow_surf, (0, 0, 0, 40), shadow_surf.get_rect())
                surf.blit(shadow_surf, (screen_x, screen_y + self.height - 15))

                # Draw sprite
                surf.blit(frame, (screen_x, screen_y))
            else:
                # Unique procedural slime rendering
                self.draw_procedural_slime(surf, screen_x, screen_y, time_ms)

        def draw_procedural_slime(self, surf, screen_x, screen_y, time_ms):
            """Draw a unique slime creature without sprites."""
            # Slime colors (green/teal)
            if self.hit_flash > 0:
                body_color = (255, 150, 150)
                highlight_color = (255, 200, 200)
            else:
                body_color = (50, 180, 80)
                highlight_color = (100, 220, 130)

            # Jiggly animation
            jiggle = math.sin(self.anim_phase * 3) * 3
            squash = 1 + math.sin(self.anim_phase * 2) * 0.1

            # Death fade
            alpha = 255
            if self.is_dying:
                alpha = max(0, 255 - int(self.death_timer * 0.5))

            # Shadow
            shadow_surf = pygame.Surface((self.width, 16), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
            surf.blit(shadow_surf, (screen_x, screen_y + self.height - 12))

            # Body - blobby ellipse with squash/stretch
            body_w = int(self.width * squash)
            body_h = int(self.height * 0.7 / squash)
            body_x = screen_x + (self.width - body_w) // 2
            body_y = screen_y + self.height - body_h - 5 + int(jiggle)

            # Create slime surface
            slime_surf = pygame.Surface((body_w + 10, body_h + 10), pygame.SRCALPHA)

            # Outer glow
            pygame.draw.ellipse(slime_surf, (*body_color[:3], int(80 * alpha / 255)),
                              (0, 0, body_w + 10, body_h + 10))

            # Main body
            pygame.draw.ellipse(slime_surf, (*body_color[:3], alpha),
                              (5, 5, body_w, body_h))

            # Highlight
            pygame.draw.ellipse(slime_surf, (*highlight_color[:3], int(alpha * 0.8)),
                              (8, 8, body_w - 15, body_h // 2))

            surf.blit(slime_surf, (body_x - 5, body_y - 5))

            # Eyes (cute dot eyes)
            if alpha > 100:
                eye_y = body_y + body_h // 3
                eye_spacing = 10
                # Left eye
                pygame.draw.circle(surf, (20, 20, 20), (int(screen_x + self.width // 2 - eye_spacing), int(eye_y)), 5)
                pygame.draw.circle(surf, (255, 255, 255), (int(screen_x + self.width // 2 - eye_spacing - 1), int(eye_y - 1)), 2)
                # Right eye
                pygame.draw.circle(surf, (20, 20, 20), (int(screen_x + self.width // 2 + eye_spacing), int(eye_y)), 5)
                pygame.draw.circle(surf, (255, 255, 255), (int(screen_x + self.width // 2 + eye_spacing - 1), int(eye_y - 1)), 2)


    class VampireEnemy(Enemy):
        """A vampire enemy with directional sprite-based animations."""
        def __init__(self, x, y):
            super().__init__(x, y, enemy_type="vampire")
            self.width = TILE_SIZE
            self.height = TILE_SIZE
            self.speed = 2.5  # Vampires are faster
            self.health = 3   # More health than basic enemies

            # Animation state
            self.current_anim = 'idle'
            self.anim_frame = 0
            self.anim_timer = 0
            self.anim_speed = 120  # ms per frame

            # Directional facing (matches sprite rows)
            self.facing = 'down'  # 'down', 'up', 'left', 'right'

            # Vampire-specific properties
            self.is_attacking = False
            self.attack_timer = 0
            self.attack_cooldown = 0
            self.death_timer = 0
            self.is_dying = False
            self.is_running = False
            self.pause_timer = 0

            # AI behavior
            self.aggro_range = TILE_SIZE * 5
            self.attack_range = TILE_SIZE * 1.5

        def update(self, dt, game_map, player):
            if self.is_dying:
                self.death_timer += dt
                self.anim_timer += dt
                self.current_anim = 'death'
                # Get death animation frame count
                death_frames = 10  # Vampire death has 10 frames
                if self.anim_timer >= self.anim_speed and self.anim_frame < death_frames - 1:
                    self.anim_timer = 0
                    self.anim_frame += 1
                # Freeze on final frame
                return

            if not self.alive:
                return

            # Update animation timer
            self.anim_timer += dt
            if self.anim_timer >= self.anim_speed:
                self.anim_timer = 0
                self.anim_frame += 1

            # Cooldowns
            if self.attack_cooldown > 0:
                self.attack_cooldown -= dt

            # Handle attack animation
            if self.is_attacking:
                self.attack_timer += dt
                self.current_anim = 'attack'
                if self.attack_timer >= 600:
                    self.is_attacking = False
                    self.attack_timer = 0
                    self.attack_cooldown = 1000
                return

            # Hit flash
            if self.hit_flash > 0:
                self.hit_flash -= dt
                self.current_anim = 'hurt'
                return

            # Calculate distance to player
            dx = player.x - self.x
            dy = player.y - self.y
            dist = math.sqrt(dx*dx + dy*dy)

            # Update facing direction based on movement intent
            if abs(dx) > abs(dy):
                self.facing = 'right' if dx > 0 else 'left'
            else:
                self.facing = 'down' if dy > 0 else 'up'

            # AI behavior based on distance
            if dist < self.attack_range and self.attack_cooldown <= 0:
                # Attack!
                self.is_attacking = True
                self.anim_frame = 0
                self.current_anim = 'attack'
            elif dist < self.aggro_range:
                # Chase player - run if far, walk if close
                self.is_running = dist > TILE_SIZE * 3
                speed = self.speed * (1.5 if self.is_running else 1.0)
                self.current_anim = 'run' if self.is_running else 'walk'

                # Move towards player
                if dist > 0:
                    move_x = (dx / dist) * speed
                    move_y = (dy / dist) * speed

                    new_x = self.x + move_x
                    new_y = self.y + move_y

                    if self.can_move_to(new_x, self.y, game_map):
                        self.x = new_x
                    if self.can_move_to(self.x, new_y, game_map):
                        self.y = new_y
            else:
                # Idle or patrol
                self.is_running = False

                # Pause behavior
                if self.pause_timer > 0:
                    self.pause_timer -= dt
                    self.current_anim = 'idle'
                    return

                # Random movement occasionally
                self.move_timer += dt
                if self.move_timer >= self.move_duration:
                    self.move_timer = 0
                    self.move_duration = random.randint(1000, 2500)
                    self.direction = random.choice(['up', 'down', 'left', 'right'])
                    self.facing = self.direction
                    # Random chance to pause
                    if random.random() < 0.4:
                        self.pause_timer = random.randint(400, 1000)
                        self.current_anim = 'idle'
                        return

                # Slow patrol movement
                dir_vec = DIRECTIONS[self.direction]
                new_x = self.x + dir_vec[0] * self.speed * 0.3
                new_y = self.y + dir_vec[1] * self.speed * 0.3

                if self.can_move_to(new_x, new_y, game_map):
                    self.x = new_x
                    self.y = new_y
                    self.current_anim = 'walk'
                else:
                    self.current_anim = 'idle'

        def take_damage(self, amount=1):
            self.health -= amount
            self.hit_flash = 250
            self.anim_frame = 0
            if self.health <= 0:
                self.is_dying = True
                self.current_anim = 'death'
                self.anim_frame = 0
                return True
            return False

        def draw(self, surf, time_ms, cam_x=0, cam_y=0):
            if not self.alive and not self.is_dying:
                return

            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -100 or screen_x > WIDTH + 100 or screen_y < -100 or screen_y > HEIGHT + 100:
                return

            # Get the appropriate animation frame with direction
            frame = get_vampire_frame(self.current_anim, self.facing, self.anim_frame)

            if frame:
                draw_frame = frame

                # Only apply red tint if not using hurt animation
                if self.hit_flash > 0 and self.current_anim != 'hurt':
                    tinted = frame.copy()
                    tint_surf = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
                    tint_surf.fill((255, 50, 50, 120))
                    tinted.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
                    draw_frame = tinted

                # No death fade - freeze on final frame

                # Draw shadow
                shadow_surf = pygame.Surface((self.width - 10, 16), pygame.SRCALPHA)
                pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
                surf.blit(shadow_surf, (screen_x + 5, screen_y + self.height - 12))

                # Draw sprite
                surf.blit(draw_frame, (screen_x, screen_y))
            else:
                # Unique procedural vampire rendering
                self.draw_procedural_vampire(surf, screen_x, screen_y, time_ms)

        def draw_procedural_vampire(self, surf, screen_x, screen_y, time_ms):
            """Draw a unique vampire creature without sprites."""
            # Color scheme (dark purple/black with red accents)
            if self.hit_flash > 0:
                body_color = (255, 150, 150)
                cape_color = (255, 100, 100)
            else:
                body_color = (40, 30, 50)
                cape_color = (120, 20, 30)

            # Floating/hovering animation
            hover = math.sin(self.anim_phase * 2) * 4
            cape_flow = math.sin(self.anim_phase * 3) * 5

            # Death fade
            alpha = 255
            if self.is_dying:
                alpha = max(0, 255 - int(self.death_timer * 0.3))

            # Shadow (smaller, vampire floats)
            shadow_surf = pygame.Surface((self.width - 20, 12), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 40), shadow_surf.get_rect())
            surf.blit(shadow_surf, (screen_x + 10, screen_y + self.height - 8))

            # Cape (flowing behind)
            cape_points = [
                (screen_x + self.width // 2, int(screen_y + 15 + hover)),  # Top center
                (int(screen_x + 8 + cape_flow), screen_y + self.height - 5),  # Bottom left
                (screen_x + self.width // 2, screen_y + self.height - 15),  # Bottom middle
                (int(screen_x + self.width - 8 - cape_flow), screen_y + self.height - 5),  # Bottom right
            ]
            cape_surf = pygame.Surface((self.width + 20, self.height + 10), pygame.SRCALPHA)
            adjusted_cape = [(int(p[0] - screen_x + 10), int(p[1] - screen_y + 5)) for p in cape_points]
            pygame.draw.polygon(cape_surf, (*cape_color[:3], alpha), adjusted_cape)
            surf.blit(cape_surf, (screen_x - 10, screen_y - 5))

            # Body (dark humanoid shape)
            body_rect = (screen_x + 15, screen_y + 10 + hover, self.width - 30, self.height - 25)
            body_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.ellipse(body_surf, (*body_color[:3], alpha),
                              (15, 10, self.width - 30, self.height - 25))
            surf.blit(body_surf, (screen_x, screen_y + int(hover)))

            # Head
            head_y = screen_y + 5 + hover
            pygame.draw.circle(surf, (*body_color[:3], alpha) if alpha == 255 else body_color,
                             (int(screen_x + self.width // 2), int(head_y + 10)), 12)

            # Glowing red eyes
            if alpha > 100:
                eye_y = head_y + 8
                glow_size = 3 + int(math.sin(self.anim_phase * 4) * 1)
                # Left eye
                pygame.draw.circle(surf, (255, 50, 50), (int(screen_x + self.width // 2 - 6), int(eye_y)), glow_size + 2)
                pygame.draw.circle(surf, (255, 150, 150), (int(screen_x + self.width // 2 - 6), int(eye_y)), glow_size)
                # Right eye
                pygame.draw.circle(surf, (255, 50, 50), (int(screen_x + self.width // 2 + 6), int(eye_y)), glow_size + 2)
                pygame.draw.circle(surf, (255, 150, 150), (int(screen_x + self.width // 2 + 6), int(eye_y)), glow_size)

                # Fangs (small white triangles)
                fang_y = int(head_y + 16)
                pygame.draw.polygon(surf, (255, 255, 255), [
                    (screen_x + self.width // 2 - 4, fang_y),
                    (screen_x + self.width // 2 - 2, fang_y + 5),
                    (screen_x + self.width // 2 - 6, fang_y)
                ])
                pygame.draw.polygon(surf, (255, 255, 255), [
                    (screen_x + self.width // 2 + 4, fang_y),
                    (screen_x + self.width // 2 + 2, fang_y + 5),
                    (screen_x + self.width // 2 + 6, fang_y)
                ])


    class OrcEnemy(Enemy):
        """An orc enemy with directional sprite-based animations - slow but tanky."""
        def __init__(self, x, y):
            super().__init__(x, y, enemy_type="orc")
            self.width = TILE_SIZE
            self.height = TILE_SIZE
            self.speed = 1.8  # Orcs are slower
            self.health = 4   # But very tanky

            # Animation state
            self.current_anim = 'idle'
            self.anim_frame = 0
            self.anim_timer = 0
            self.anim_speed = 100  # ms per frame

            # Directional facing
            self.facing = 'down'

            # Orc-specific properties
            self.is_attacking = False
            self.attack_timer = 0
            self.attack_cooldown = 0
            self.death_timer = 0
            self.is_dying = False
            self.pause_timer = 0

            # AI behavior - orcs are more aggressive but slower
            self.aggro_range = TILE_SIZE * 6
            self.attack_range = TILE_SIZE * 1.2
            self.charge_speed = 3.0  # Speed when charging

        def update(self, dt, game_map, player):
            if self.is_dying:
                self.death_timer += dt
                self.anim_timer += dt
                self.current_anim = 'death'
                # Get death animation frame count
                death_frames = 10  # Orc death has 10 frames
                if self.anim_timer >= self.anim_speed and self.anim_frame < death_frames - 1:
                    self.anim_timer = 0
                    self.anim_frame += 1
                # Freeze on final frame
                return

            if not self.alive:
                return

            # Update animation timer
            self.anim_timer += dt
            if self.anim_timer >= self.anim_speed:
                self.anim_timer = 0
                self.anim_frame += 1

            # Cooldowns
            if self.attack_cooldown > 0:
                self.attack_cooldown -= dt

            # Handle attack animation
            if self.is_attacking:
                self.attack_timer += dt
                self.current_anim = 'attack'
                if self.attack_timer >= 700:
                    self.is_attacking = False
                    self.attack_timer = 0
                    self.attack_cooldown = 1500  # Longer cooldown than vampire
                return

            # Hit flash
            if self.hit_flash > 0:
                self.hit_flash -= dt
                self.current_anim = 'hurt'
                return

            # Calculate distance to player
            dx = player.x - self.x
            dy = player.y - self.y
            dist = math.sqrt(dx*dx + dy*dy)

            # Update facing direction
            if abs(dx) > abs(dy):
                self.facing = 'right' if dx > 0 else 'left'
            else:
                self.facing = 'down' if dy > 0 else 'up'

            # AI behavior - orcs are aggressive chargers
            if dist < self.attack_range and self.attack_cooldown <= 0:
                # Attack!
                self.is_attacking = True
                self.anim_frame = 0
                self.current_anim = 'attack'
            elif dist < self.aggro_range:
                # Charge at player! Orcs run when they see you
                speed = self.charge_speed if dist > TILE_SIZE * 2 else self.speed
                self.current_anim = 'run' if dist > TILE_SIZE * 2 else 'walk'

                # Move towards player
                if dist > 0:
                    move_x = (dx / dist) * speed
                    move_y = (dy / dist) * speed

                    new_x = self.x + move_x
                    new_y = self.y + move_y

                    if self.can_move_to(new_x, self.y, game_map):
                        self.x = new_x
                    if self.can_move_to(self.x, new_y, game_map):
                        self.y = new_y
            else:
                # Idle patrol

                # Pause behavior
                if self.pause_timer > 0:
                    self.pause_timer -= dt
                    self.current_anim = 'idle'
                    return

                self.move_timer += dt
                if self.move_timer >= self.move_duration:
                    self.move_timer = 0
                    self.move_duration = random.randint(1500, 3000)
                    self.direction = random.choice(['up', 'down', 'left', 'right'])
                    self.facing = self.direction
                    # Random chance to pause
                    if random.random() < 0.4:
                        self.pause_timer = random.randint(500, 1200)
                        self.current_anim = 'idle'
                        return

                # Slow patrol
                dir_vec = DIRECTIONS[self.direction]
                new_x = self.x + dir_vec[0] * self.speed * 0.4
                new_y = self.y + dir_vec[1] * self.speed * 0.4

                if self.can_move_to(new_x, new_y, game_map):
                    self.x = new_x
                    self.y = new_y
                    self.current_anim = 'walk'
                else:
                    self.current_anim = 'idle'

        def take_damage(self, amount=1):
            self.health -= amount
            self.hit_flash = 300
            self.anim_frame = 0
            if self.health <= 0:
                self.is_dying = True
                self.current_anim = 'death'
                self.anim_frame = 0
                return True
            return False

        def draw(self, surf, time_ms, cam_x=0, cam_y=0):
            if not self.alive and not self.is_dying:
                return

            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -100 or screen_x > WIDTH + 100 or screen_y < -100 or screen_y > HEIGHT + 100:
                return

            # Get the appropriate animation frame with direction
            frame = get_orc_frame(self.current_anim, self.facing, self.anim_frame)

            if frame:
                draw_frame = frame

                # Only apply red tint if not using hurt animation
                if self.hit_flash > 0 and self.current_anim != 'hurt':
                    tinted = frame.copy()
                    tint_surf = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
                    tint_surf.fill((255, 50, 50, 150))
                    tinted.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
                    draw_frame = tinted

                # No death fade - freeze on final frame

                # Draw shadow
                shadow_surf = pygame.Surface((self.width - 8, 18), pygame.SRCALPHA)
                pygame.draw.ellipse(shadow_surf, (0, 0, 0, 55), shadow_surf.get_rect())
                surf.blit(shadow_surf, (screen_x + 4, screen_y + self.height - 14))

                # Draw sprite
                surf.blit(draw_frame, (screen_x, screen_y))
            else:
                # Unique procedural orc rendering
                self.draw_procedural_orc(surf, screen_x, screen_y, time_ms)

        def draw_procedural_orc(self, surf, screen_x, screen_y, time_ms):
            """Draw a unique orc creature without sprites."""
            # Color scheme (green/brown for orc)
            if self.hit_flash > 0:
                skin_color = (255, 150, 150)
                armor_color = (200, 150, 150)
            else:
                skin_color = (80, 120, 60)
                armor_color = (80, 60, 40)

            # Subtle breathing animation
            breathe = math.sin(self.anim_phase * 1.5) * 2

            # Death fade
            alpha = 255
            if self.is_dying:
                alpha = max(0, 255 - int(self.death_timer * 0.35))

            # Shadow (larger for bulky orc)
            shadow_surf = pygame.Surface((self.width, 18), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 55), shadow_surf.get_rect())
            surf.blit(shadow_surf, (screen_x, screen_y + self.height - 12))

            # Body (bulky torso)
            body_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

            # Armor/chest plate (use ellipse for rounded look since pygame_sdl2 doesn't support border_radius)
            pygame.draw.ellipse(body_surf, (*armor_color[:3], alpha), (12, int(18 + breathe), self.width - 24, 30))

            # Arms (thick)
            # Left arm
            pygame.draw.ellipse(body_surf, (*skin_color[:3], alpha), (4, int(20 + breathe), 14, 28))
            # Right arm
            pygame.draw.ellipse(body_surf, (*skin_color[:3], alpha), (self.width - 18, int(20 + breathe), 14, 28))

            # Legs
            pygame.draw.ellipse(body_surf, (*armor_color[:3], alpha), (15, 42, 12, 20))
            pygame.draw.ellipse(body_surf, (*armor_color[:3], alpha), (self.width - 27, 42, 12, 20))

            surf.blit(body_surf, (screen_x, screen_y))

            # Head (large and brutish)
            head_y = screen_y + 5 + breathe
            head_surf = pygame.Surface((36, 28), pygame.SRCALPHA)
            pygame.draw.ellipse(head_surf, (*skin_color[:3], alpha), (0, 0, 36, 28))
            surf.blit(head_surf, (screen_x + self.width // 2 - 18, int(head_y)))

            if alpha > 100:
                # Angry eyes
                eye_y = head_y + 10
                pygame.draw.ellipse(surf, (200, 50, 50), (screen_x + self.width // 2 - 10, int(eye_y), 6, 5))
                pygame.draw.ellipse(surf, (200, 50, 50), (screen_x + self.width // 2 + 4, int(eye_y), 6, 5))
                pygame.draw.circle(surf, (0, 0, 0), (int(screen_x + self.width // 2 - 7), int(eye_y + 2)), 2)
                pygame.draw.circle(surf, (0, 0, 0), (int(screen_x + self.width // 2 + 7), int(eye_y + 2)), 2)

                # Tusks
                tusk_y = int(head_y + 20)
                pygame.draw.polygon(surf, (230, 220, 200), [
                    (screen_x + self.width // 2 - 12, tusk_y),
                    (screen_x + self.width // 2 - 8, tusk_y + 8),
                    (screen_x + self.width // 2 - 14, tusk_y + 3)
                ])
                pygame.draw.polygon(surf, (230, 220, 200), [
                    (screen_x + self.width // 2 + 12, tusk_y),
                    (screen_x + self.width // 2 + 8, tusk_y + 8),
                    (screen_x + self.width // 2 + 14, tusk_y + 3)
                ])

                # Brow ridge (angry expression)
                pygame.draw.line(surf, (60, 90, 45),
                               (screen_x + self.width // 2 - 12, int(eye_y - 3)),
                               (screen_x + self.width // 2 - 4, int(eye_y - 1)), 2)
                pygame.draw.line(surf, (60, 90, 45),
                               (screen_x + self.width // 2 + 12, int(eye_y - 3)),
                               (screen_x + self.width // 2 + 4, int(eye_y - 1)), 2)


    class SpiderEnemy(Enemy):
        """A spider enemy - fast and erratic movement."""
        def __init__(self, x, y):
            super().__init__(x, y, enemy_type="spider")
            self.width = TILE_SIZE
            self.height = TILE_SIZE
            self.speed = 3.0  # Spiders are fast!
            self.health = 2   # But fragile

            # Animation state
            self.anim_frame = 0
            self.anim_timer = 0
            self.anim_speed = 80  # Fast animation

            # Directional facing
            self.facing = 'down'

            # Spider-specific properties
            self.death_timer = 0
            self.is_dying = False
            self.pause_timer = 0

            # Erratic movement
            self.direction_change_timer = 0
            self.direction_change_interval = random.randint(300, 800)
            self.is_fleeing = False
            self.flee_timer = 0

        def update(self, dt, game_map, player):
            if self.is_dying:
                self.death_timer += dt
                self.anim_timer += dt
                # Get death animation frame count
                death_frames = len(SPIDER_FRAMES.get('death', [None, None, None, None]))
                # Only advance frame if not at last frame
                if self.anim_timer >= self.anim_speed and self.anim_frame < death_frames - 1:
                    self.anim_timer = 0
                    self.anim_frame += 1
                # Freeze on final frame - don't set alive = False
                return

            if not self.alive:
                return

            # Update animation timer
            self.anim_timer += dt
            if self.anim_timer >= self.anim_speed:
                self.anim_timer = 0
                self.anim_frame += 1

            # Hit flash
            if self.hit_flash > 0:
                self.hit_flash -= dt

            # Calculate distance to player
            dx = player.x - self.x
            dy = player.y - self.y
            dist = math.sqrt(dx*dx + dy*dy)

            # Flee behavior when hit
            if self.flee_timer > 0:
                self.flee_timer -= dt
                # Run away from player
                if dist > 0:
                    flee_x = -dx / dist * self.speed * 1.5
                    flee_y = -dy / dist * self.speed * 1.5
                    new_x = self.x + flee_x
                    new_y = self.y + flee_y
                    if self.can_move_to(new_x, self.y, game_map):
                        self.x = new_x
                    if self.can_move_to(self.x, new_y, game_map):
                        self.y = new_y
                    # Update facing (away from player)
                    if abs(flee_x) > abs(flee_y):
                        self.facing = 'right' if flee_x > 0 else 'left'
                    else:
                        self.facing = 'down' if flee_y > 0 else 'up'
                return

            # Pause behavior (spiders pause briefly)
            if self.pause_timer > 0:
                self.pause_timer -= dt
                return

            # Erratic direction changes
            self.direction_change_timer += dt
            if self.direction_change_timer >= self.direction_change_interval:
                self.direction_change_timer = 0
                self.direction_change_interval = random.randint(300, 800)

                # Sometimes chase, sometimes random
                if dist < TILE_SIZE * 4 and random.random() < 0.6:
                    # Chase player
                    if abs(dx) > abs(dy):
                        self.direction = 'right' if dx > 0 else 'left'
                    else:
                        self.direction = 'down' if dy > 0 else 'up'
                else:
                    # Random direction
                    self.direction = random.choice(['up', 'down', 'left', 'right'])
                    # Random short pause
                    if random.random() < 0.25:
                        self.pause_timer = random.randint(150, 400)

                self.facing = self.direction

            # Move in current direction
            dir_vec = DIRECTIONS[self.direction]
            new_x = self.x + dir_vec[0] * self.speed
            new_y = self.y + dir_vec[1] * self.speed

            if self.can_move_to(new_x, new_y, game_map):
                self.x = new_x
                self.y = new_y
            else:
                # Hit wall - change direction immediately
                self.direction = random.choice(['up', 'down', 'left', 'right'])
                self.facing = self.direction

        def take_damage(self, amount=1):
            self.health -= amount
            self.hit_flash = 150
            self.flee_timer = 500  # Flee when hit!
            self.anim_frame = 0
            if self.health <= 0:
                self.is_dying = True
                self.anim_frame = 0
                return True
            return False

        def draw(self, surf, time_ms, cam_x=0, cam_y=0):
            if not self.alive and not self.is_dying:
                return

            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -100 or screen_x > WIDTH + 100 or screen_y < -100 or screen_y > HEIGHT + 100:
                return

            # Get the appropriate animation frame
            if self.is_dying:
                frame = get_spider_frame('death', self.anim_frame)
            else:
                frame = get_spider_frame(self.facing, self.anim_frame)

            if frame:
                draw_frame = frame

                # Apply hit flash tint if damaged (spiders don't have hurt anim, so always use tint)
                if self.hit_flash > 0:
                    tinted = frame.copy()
                    tint_surf = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
                    tint_surf.fill((255, 100, 100, 120))
                    tinted.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
                    draw_frame = tinted

                # No death fade - freeze on final frame

                # Draw shadow (smaller for spider)
                shadow_surf = pygame.Surface((self.width - 20, 12), pygame.SRCALPHA)
                pygame.draw.ellipse(shadow_surf, (0, 0, 0, 35), shadow_surf.get_rect())
                surf.blit(shadow_surf, (screen_x + 10, screen_y + self.height - 10))

                # Draw sprite
                surf.blit(draw_frame, (screen_x, screen_y))
            else:
                # Unique procedural spider rendering
                self.draw_procedural_spider(surf, screen_x, screen_y, time_ms)

        def draw_procedural_spider(self, surf, screen_x, screen_y, time_ms):
            """Draw a unique spider creature without sprites."""
            # Color scheme (dark brown/black)
            if self.hit_flash > 0:
                body_color = (255, 150, 150)
                leg_color = (200, 120, 120)
            else:
                body_color = (50, 35, 30)
                leg_color = (70, 50, 40)

            # Leg animation based on movement
            leg_phase = self.anim_phase * 8  # Fast leg movement

            # Death fade
            alpha = 255
            if self.is_dying:
                alpha = max(0, 255 - int(self.death_timer * 0.6))

            # Shadow
            shadow_surf = pygame.Surface((self.width - 16, 10), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 35), shadow_surf.get_rect())
            surf.blit(shadow_surf, (screen_x + 8, screen_y + self.height - 8))

            center_x = screen_x + self.width // 2
            center_y = screen_y + self.height // 2

            # Draw 8 legs (4 on each side)
            leg_length = 18
            leg_angles_left = [150, 170, 190, 210]
            leg_angles_right = [30, 10, -10, -30]

            for i, angle in enumerate(leg_angles_left):
                # Animate legs alternately
                leg_offset = math.sin(leg_phase + i * 1.5) * 4
                rad = math.radians(angle)
                end_x = center_x - 8 + math.cos(rad) * (leg_length + leg_offset)
                end_y = center_y + math.sin(rad) * (leg_length + leg_offset)
                pygame.draw.line(surf, leg_color, (center_x - 8, center_y), (int(end_x), int(end_y)), 2)

            for i, angle in enumerate(leg_angles_right):
                leg_offset = math.sin(leg_phase + i * 1.5 + math.pi) * 4
                rad = math.radians(angle)
                end_x = center_x + 8 + math.cos(rad) * (leg_length + leg_offset)
                end_y = center_y + math.sin(rad) * (leg_length + leg_offset)
                pygame.draw.line(surf, leg_color, (center_x + 8, center_y), (int(end_x), int(end_y)), 2)

            # Abdomen (back body - larger)
            pygame.draw.ellipse(surf, body_color,
                              (center_x - 14, center_y - 2, 28, 22))

            # Cephalothorax (front body - smaller)
            pygame.draw.ellipse(surf, body_color,
                              (center_x - 10, center_y - 16, 20, 18))

            # Eyes (multiple small eyes in a cluster)
            if alpha > 100:
                eye_y = center_y - 12
                # Main eyes (larger)
                pygame.draw.circle(surf, (150, 20, 20), (int(center_x - 5), int(eye_y)), 3)
                pygame.draw.circle(surf, (150, 20, 20), (int(center_x + 5), int(eye_y)), 3)
                # Secondary eyes (smaller, above)
                pygame.draw.circle(surf, (120, 20, 20), (int(center_x - 8), int(eye_y - 5)), 2)
                pygame.draw.circle(surf, (120, 20, 20), (int(center_x + 8), int(eye_y - 5)), 2)
                # Tiny eyes
                pygame.draw.circle(surf, (100, 15, 15), (int(center_x - 3), int(eye_y - 7)), 1)
                pygame.draw.circle(surf, (100, 15, 15), (int(center_x + 3), int(eye_y - 7)), 1)

                # Eye shine
                pygame.draw.circle(surf, (255, 200, 200), (int(center_x - 4), int(eye_y - 1)), 1)
                pygame.draw.circle(surf, (255, 200, 200), (int(center_x + 6), int(eye_y - 1)), 1)

                # Fangs (pedipalps)
                pygame.draw.line(surf, (80, 60, 50), (center_x - 4, center_y - 6), (center_x - 6, center_y), 2)
                pygame.draw.line(surf, (80, 60, 50), (center_x + 4, center_y - 6), (center_x + 6, center_y), 2)


    class Shard:
        """A collectible beacon shard."""
        def __init__(self, x, y):
            # Store in world coordinates (tile-based)
            self.x = x * TILE_SIZE + TILE_SIZE // 2
            self.y = y * TILE_SIZE + TILE_SIZE // 2
            self.collected = False
            self.anim_phase = random.random() * math.pi * 2

        def update(self, dt):
            self.anim_phase += dt * 0.004

        def get_rect(self):
            return pygame.Rect(self.x - 20, self.y - 20, 40, 40)

        def draw(self, surf, time_ms, cam_x=0, cam_y=0):
            if self.collected:
                return

            # Calculate screen position
            screen_x = self.x - cam_x
            screen_y = self.y - cam_y

            # Skip if off-screen
            if screen_x < -50 or screen_x > WIDTH + 50 or screen_y < -50 or screen_y > HEIGHT + 50:
                return

            bob = math.sin(self.anim_phase) * 5
            glow = 0.5 + 0.3 * math.sin(self.anim_phase * 1.5)

            # Glow
            glow_size = int(35 + 10 * glow)
            glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
            glow_alpha = int(100 * glow)
            pygame.draw.circle(glow_surf, (255, 220, 100, glow_alpha), (glow_size, glow_size), glow_size)
            surf.blit(glow_surf, (screen_x - glow_size, screen_y + bob - glow_size))

            # Crystal shape
            points = []
            for i in range(6):
                angle = i * math.pi / 3 - math.pi / 2
                r = 18 if i % 2 == 0 else 10
                points.append((screen_x + math.cos(angle) * r, screen_y + bob + math.sin(angle) * r))

            pygame.draw.polygon(surf, (255, 240, 150), points)
            pygame.draw.polygon(surf, (255, 200, 50), points, 2)

            # Inner sparkle
            pygame.draw.circle(surf, (255, 255, 255), (int(screen_x - 3), int(screen_y + bob - 5)), 4)

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

        def draw(self, surf, cam_x=0, cam_y=0):
            alpha = int(255 * (self.lifetime / 500))
            for p in self.particles:
                size = p['size'] * (self.lifetime / 500)
                if size > 0:
                    screen_x = p['x'] - cam_x
                    screen_y = p['y'] - cam_y
                    # Skip if off-screen
                    if screen_x < -50 or screen_x > WIDTH + 50 or screen_y < -50 or screen_y > HEIGHT + 50:
                        continue
                    ps = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
                    pygame.draw.circle(ps, (*p['color'], alpha), (int(size + 2), int(size + 2)), int(size))
                    surf.blit(ps, (int(screen_x - size), int(screen_y - size)))

    class Room:
        """A single room in the dungeon."""
        def __init__(self, room_id, game_map, enemies, shards, doors, width=None, height=None):
            self.room_id = room_id
            self.game_map = game_map
            self.shards = shards
            self.doors = doors  # Dict: {door_tile: (target_room_id, spawn_direction)}
            # Room dimensions (infer from map if not specified)
            self.width = width if width is not None else len(game_map[0]) if game_map else DEFAULT_MAP_WIDTH
            self.height = height if height is not None else len(game_map) if game_map else DEFAULT_MAP_HEIGHT
            # Room pixel dimensions
            self.pixel_width = self.width * TILE_SIZE
            self.pixel_height = self.height * TILE_SIZE

            # Validate and fix enemy spawn positions
            self.enemies = []
            for enemy in enemies:
                # Get enemy's tile position
                tile_x = int(enemy.x // TILE_SIZE)
                tile_y = int(enemy.y // TILE_SIZE)

                # Check if spawn is valid
                if not validate_spawn_position(tile_x, tile_y, game_map):
                    # Find nearest valid position
                    new_x, new_y = find_nearest_valid_spawn(tile_x, tile_y, game_map)
                    if (new_x, new_y) != (tile_x, tile_y):
                        print(f"Relocated {enemy.enemy_type} from ({tile_x}, {tile_y}) to ({new_x}, {new_y}) in room '{room_id}'")
                        enemy.x = new_x * TILE_SIZE
                        enemy.y = new_y * TILE_SIZE

                self.enemies.append(enemy)

        def reset_enemies(self):
            """Reset enemies when re-entering room."""
            for enemy in self.enemies:
                if not enemy.alive:
                    enemy.alive = True
                    enemy.health = 2

        def get_tile(self, x, y):
            """Safely get tile at position, returns TILE_VOID if out of bounds."""
            if 0 <= y < self.height and 0 <= x < self.width:
                return self.game_map[y][x]
            return TILE_VOID


    class BeaconQuestGame:
        """Main game controller for Beacon Quest with multi-room support."""
        def __init__(self):
            self.state = STATE_PLAYING

            # Load tileset sprites
            load_tileset()

            # Load enemy sprites
            load_slime_sprites()
            load_vampire_sprites()
            load_orc_sprites()
            load_spider_sprites()

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
            self.target_shards = 6  # Shards across all rooms (including large east room)

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

            # Camera system
            self.camera_x = 0.0  # Camera position (top-left corner of viewport)
            self.camera_y = 0.0
            self.camera_target_x = 0.0
            self.camera_target_y = 0.0
            # Initialize camera to center on starting position
            self.snap_camera_to_player()

        def snap_camera_to_player(self):
            """Instantly center camera on active player."""
            player = self.get_active_player()
            # Center camera on player
            target_x = player.x + player.width / 2 - VIEWPORT_WIDTH / 2
            target_y = player.y + player.height / 2 - VIEWPORT_HEIGHT / 2
            # Clamp to room bounds
            self.camera_x = self.clamp_camera_x(target_x)
            self.camera_y = self.clamp_camera_y(target_y)
            self.camera_target_x = self.camera_x
            self.camera_target_y = self.camera_y

        def clamp_camera_x(self, x):
            """Clamp camera X to room bounds."""
            room = self.current_room
            max_x = room.pixel_width - VIEWPORT_WIDTH
            if max_x <= 0:
                # Room fits in viewport, center it
                return (room.pixel_width - VIEWPORT_WIDTH) / 2
            return max(0, min(x, max_x))

        def clamp_camera_y(self, y):
            """Clamp camera Y to room bounds."""
            room = self.current_room
            max_y = room.pixel_height - VIEWPORT_HEIGHT
            if max_y <= 0:
                # Room fits in viewport, center it
                return (room.pixel_height - VIEWPORT_HEIGHT) / 2
            return max(0, min(y, max_y))

        def update_camera(self, dt):
            """Smoothly follow the active player with deadzone."""
            player = self.get_active_player()

            # Calculate player center in world coordinates
            player_center_x = player.x + player.width / 2
            player_center_y = player.y + player.height / 2

            # Calculate where player is relative to camera center
            camera_center_x = self.camera_x + VIEWPORT_WIDTH / 2
            camera_center_y = self.camera_y + VIEWPORT_HEIGHT / 2

            # Calculate offset from center
            offset_x = player_center_x - camera_center_x
            offset_y = player_center_y - camera_center_y

            # Only update target if player moves outside deadzone
            if abs(offset_x) > CAMERA_DEADZONE_X:
                if offset_x > 0:
                    self.camera_target_x = player_center_x - VIEWPORT_WIDTH / 2 - CAMERA_DEADZONE_X
                else:
                    self.camera_target_x = player_center_x - VIEWPORT_WIDTH / 2 + CAMERA_DEADZONE_X

            if abs(offset_y) > CAMERA_DEADZONE_Y:
                if offset_y > 0:
                    self.camera_target_y = player_center_y - VIEWPORT_HEIGHT / 2 - CAMERA_DEADZONE_Y
                else:
                    self.camera_target_y = player_center_y - VIEWPORT_HEIGHT / 2 + CAMERA_DEADZONE_Y

            # Clamp targets to room bounds
            self.camera_target_x = self.clamp_camera_x(self.camera_target_x)
            self.camera_target_y = self.clamp_camera_y(self.camera_target_y)

            # Smooth lerp towards target
            lerp_factor = 1.0 - math.pow(1.0 - CAMERA_FOLLOW_SPEED, dt / 16.67)
            self.camera_x += (self.camera_target_x - self.camera_x) * lerp_factor
            self.camera_y += (self.camera_target_y - self.camera_y) * lerp_factor

        def world_to_screen(self, world_x, world_y):
            """Convert world coordinates to screen coordinates."""
            return (world_x - self.camera_x, world_y - self.camera_y)

        def screen_to_world(self, screen_x, screen_y):
            """Convert screen coordinates to world coordinates."""
            return (screen_x + self.camera_x, screen_y + self.camera_y)

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
                SlimeEnemy(5, 4),   # Slime in start room
                SlimeEnemy(14, 4),  # Slime in start room
                OrcEnemy(10, 7),    # Orc patrolling center
                SpiderEnemy(8, 5),  # Spider - fast and erratic
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
                SlimeEnemy(4, 6),    # Slime guardian
                SlimeEnemy(15, 6),   # Slime guardian
                VampireEnemy(10, 5), # Vampire guarding beacon!
                SlimeEnemy(6, 8),    # Slime patrol
                SlimeEnemy(13, 8),   # Slime patrol
                SpiderEnemy(5, 10),  # Spider skittering around
                SpiderEnemy(14, 10), # Spider skittering around
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
            """Create the east room - LARGE enemy gauntlet to test camera."""
            # Much larger room: 45 wide x 28 tall (bigger than viewport!)
            room_width = 45
            room_height = 28
            game_map = [[TILE_VOID for _ in range(room_width)] for _ in range(room_height)]

            # Create the main walkable area
            for y in range(1, room_height - 1):
                for x in range(2, room_width - 2):
                    game_map[y][x] = TILE_FLOOR

            # Perimeter walls
            for x in range(2, room_width - 1):
                game_map[0][x] = TILE_WALL
                game_map[room_height - 1][x] = TILE_WALL
            for y in range(1, room_height - 1):
                game_map[y][1] = TILE_WALL
                game_map[y][room_width - 2] = TILE_WALL

            # West door (entrance from start room)
            game_map[6][1] = TILE_DOOR_W

            # Create interesting wall patterns throughout the large room
            # Section 1: Maze entrance (left side)
            for y in range(3, 12):
                if y != 6:  # Leave door path open
                    game_map[y][8] = TILE_WALL

            # Section 2: Middle pillars
            for pillar_x in [15, 22, 29]:
                for y in range(4, 8):
                    game_map[y][pillar_x] = TILE_WALL
                for y in range(16, 22):
                    game_map[y][pillar_x] = TILE_WALL

            # Section 3: Horizontal barriers
            for x in range(10, 18):
                game_map[13][x] = TILE_WALL
            for x in range(26, 36):
                game_map[13][x] = TILE_WALL
            for x in range(18, 28):
                game_map[20][x] = TILE_WALL

            # Section 4: L-shaped obstacles
            for x in range(35, 40):
                game_map[5][x] = TILE_WALL
            for y in range(5, 10):
                game_map[y][40] = TILE_WALL

            # Create some "rooms" with openings
            for y in range(16, 25):
                game_map[y][10] = TILE_WALL
            game_map[20][10] = TILE_FLOOR  # Opening

            # Place enemies throughout the large room
            enemies = [
                # Near entrance
                OrcEnemy(4, 5),
                SlimeEnemy(4, 9),

                # First section
                VampireEnemy(12, 6),
                SpiderEnemy(10, 3),
                SpiderEnemy(10, 10),

                # Middle section
                OrcEnemy(18, 8),
                SlimeEnemy(20, 10),
                VampireEnemy(25, 6),
                SpiderEnemy(22, 15),

                # Far section
                OrcEnemy(32, 5),
                VampireEnemy(35, 10),
                SlimeEnemy(38, 8),
                SpiderEnemy(40, 3),

                # Bottom section
                SlimeEnemy(15, 18),
                OrcEnemy(22, 22),
                VampireEnemy(30, 20),
                SpiderEnemy(35, 24),

                # Patrol in open area
                VampireEnemy(20, 15),
                SpiderEnemy(28, 18),
            ]

            # Multiple shards spread across the large room
            shards = [
                Shard(38, 6),    # Far right
                Shard(22, 24),   # Bottom middle
            ]

            doors = {
                (1, 6): ("start", "left"),
            }

            return Room("east", game_map, enemies, shards, doors, room_width, room_height)

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
                OrcEnemy(7, 4),      # Orc guard
                VampireEnemy(10, 6), # Vampire guarding treasure
                SlimeEnemy(7, 9),    # Slime patrol
                OrcEnemy(12, 8),     # Orc guard
                SpiderEnemy(4, 6),   # Spider near treasure
                SpiderEnemy(15, 4),  # Spider by pillar
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

            # Snap camera to new position
            self.snap_camera_to_player()

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

            # Update camera to follow active player
            self.update_camera(dt)

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

            # Get camera offset for rendering
            cam_x = int(self.camera_x)
            cam_y = int(self.camera_y)

            # Draw map (already handles camera internally)
            self.draw_map(game_surf, time_ms)

            # Draw shards (with camera offset)
            for shard in self.current_room.shards:
                shard.draw(game_surf, time_ms, cam_x, cam_y)

            # Draw projectiles (with camera offset)
            for proj in self.projectiles:
                proj.draw(game_surf, cam_x, cam_y)

            # Draw enemies (with camera offset)
            for enemy in self.current_room.enemies:
                enemy.draw(game_surf, time_ms, cam_x, cam_y)

            # Draw both characters (companion first so active is on top)
            companion = self.get_companion()
            active = self.get_active_player()
            companion.draw(game_surf, time_ms, is_active=False, cam_x=cam_x, cam_y=cam_y)
            active.draw(game_surf, time_ms, is_active=True, cam_x=cam_x, cam_y=cam_y)

            # Draw effects (with camera offset)
            for effect in self.effects:
                effect.draw(game_surf, cam_x, cam_y)

            # Blit with shake
            surf.blit(game_surf, (shake_x, shake_y))

            # Draw UI (no shake, always screen-space)
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
            """Draw the game map using tileset sprites with camera offset."""
            room = self.current_room

            # Calculate visible tile range based on camera position
            start_x = max(0, int(self.camera_x // TILE_SIZE) - 1)
            start_y = max(0, int(self.camera_y // TILE_SIZE) - 1)
            end_x = min(room.width, int((self.camera_x + VIEWPORT_WIDTH) // TILE_SIZE) + 2)
            end_y = min(room.height, int((self.camera_y + VIEWPORT_HEIGHT) // TILE_SIZE) + 2)

            # Use floored camera position to prevent tile gaps
            cam_x_floor = int(self.camera_x)
            cam_y_floor = int(self.camera_y)

            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    tile = room.get_tile(x, y)
                    # World position
                    world_x = x * TILE_SIZE
                    world_y = y * TILE_SIZE
                    # Screen position (apply floored camera offset for consistent gaps)
                    px = world_x - cam_x_floor
                    py = world_y - cam_y_floor

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
