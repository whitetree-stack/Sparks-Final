# skybridge_adventure.rpy - Skybridge Zelda-Style Adventure Minigame
# A top-down action adventure game

####################################################################################################################
# BEACON QUEST ADVENTURE MINIGAME
####################################################################################################################

init python in beacon_quest:
    import pygame
    import random
    import math
    from pygame.locals import *

    ####################################################################################################################
    # SPRITE CONFIGURATION - Set USE_SPRITES = True and provide sprite paths to use custom graphics
    ####################################################################################################################

    USE_SPRITES = False  # Set to True when sprites are ready

    # Player character sprites
    # Each direction has idle + 4 walking frames, plus attack animation
    PLAYER_SPRITES = {
        # Idle sprites (one per direction)
        "idle_up": "images/minigames/beaconquest/player/idle_up.png",
        "idle_down": "images/minigames/beaconquest/player/idle_down.png",
        "idle_left": "images/minigames/beaconquest/player/idle_left.png",
        "idle_right": "images/minigames/beaconquest/player/idle_right.png",

        # Walking animation frames (4 frames per direction)
        "walk_up_0": "images/minigames/beaconquest/player/walk_up_0.png",
        "walk_up_1": "images/minigames/beaconquest/player/walk_up_1.png",
        "walk_up_2": "images/minigames/beaconquest/player/walk_up_2.png",
        "walk_up_3": "images/minigames/beaconquest/player/walk_up_3.png",
        "walk_down_0": "images/minigames/beaconquest/player/walk_down_0.png",
        "walk_down_1": "images/minigames/beaconquest/player/walk_down_1.png",
        "walk_down_2": "images/minigames/beaconquest/player/walk_down_2.png",
        "walk_down_3": "images/minigames/beaconquest/player/walk_down_3.png",
        "walk_left_0": "images/minigames/beaconquest/player/walk_left_0.png",
        "walk_left_1": "images/minigames/beaconquest/player/walk_left_1.png",
        "walk_left_2": "images/minigames/beaconquest/player/walk_left_2.png",
        "walk_left_3": "images/minigames/beaconquest/player/walk_left_3.png",
        "walk_right_0": "images/minigames/beaconquest/player/walk_right_0.png",
        "walk_right_1": "images/minigames/beaconquest/player/walk_right_1.png",
        "walk_right_2": "images/minigames/beaconquest/player/walk_right_2.png",
        "walk_right_3": "images/minigames/beaconquest/player/walk_right_3.png",

        # Attack animation (3 frames per direction showing sword swing)
        "attack_up_0": "images/minigames/beaconquest/player/attack_up_0.png",
        "attack_up_1": "images/minigames/beaconquest/player/attack_up_1.png",
        "attack_up_2": "images/minigames/beaconquest/player/attack_up_2.png",
        "attack_down_0": "images/minigames/beaconquest/player/attack_down_0.png",
        "attack_down_1": "images/minigames/beaconquest/player/attack_down_1.png",
        "attack_down_2": "images/minigames/beaconquest/player/attack_down_2.png",
        "attack_left_0": "images/minigames/beaconquest/player/attack_left_0.png",
        "attack_left_1": "images/minigames/beaconquest/player/attack_left_1.png",
        "attack_left_2": "images/minigames/beaconquest/player/attack_left_2.png",
        "attack_right_0": "images/minigames/beaconquest/player/attack_right_0.png",
        "attack_right_1": "images/minigames/beaconquest/player/attack_right_1.png",
        "attack_right_2": "images/minigames/beaconquest/player/attack_right_2.png",

        # Shadow (drawn beneath player)
        "shadow": "images/minigames/beaconquest/player/shadow.png",
    }

    # Alternative: Player spritesheet (single image with all frames)
    PLAYER_SPRITESHEET = "images/minigames/beaconquest/player/player_spritesheet.png"
    # Format: 4 rows (down, up, left, right), 8 cols (idle, walk x4, attack x3)

    # Enemy sprites - shadow creature
    ENEMY_SPRITES = {
        "shadow_idle": "images/minigames/beaconquest/enemies/shadow_idle.png",
        "shadow_move_0": "images/minigames/beaconquest/enemies/shadow_move_0.png",
        "shadow_move_1": "images/minigames/beaconquest/enemies/shadow_move_1.png",
        "shadow_hit": "images/minigames/beaconquest/enemies/shadow_hit.png",
        "shadow_glow": "images/minigames/beaconquest/enemies/shadow_glow.png",
        "shadow_eyes": "images/minigames/beaconquest/enemies/shadow_eyes.png",
    }

    # Additional enemy types (for future expansion)
    ENEMY_TYPE_SPRITES = {
        "shadow": ENEMY_SPRITES,
        "wraith": {
            "idle": "images/minigames/beaconquest/enemies/wraith_idle.png",
            "move_0": "images/minigames/beaconquest/enemies/wraith_move_0.png",
            "move_1": "images/minigames/beaconquest/enemies/wraith_move_1.png",
            "hit": "images/minigames/beaconquest/enemies/wraith_hit.png",
        },
        "phantom": {
            "idle": "images/minigames/beaconquest/enemies/phantom_idle.png",
            "move_0": "images/minigames/beaconquest/enemies/phantom_move_0.png",
            "move_1": "images/minigames/beaconquest/enemies/phantom_move_1.png",
            "hit": "images/minigames/beaconquest/enemies/phantom_hit.png",
        },
    }

    # Tile sprites for the game map
    TILE_SPRITES = {
        "floor_light": "images/minigames/beaconquest/tiles/floor_light.png",
        "floor_dark": "images/minigames/beaconquest/tiles/floor_dark.png",
        "floor_pattern": "images/minigames/beaconquest/tiles/floor_pattern.png",
        "wall": "images/minigames/beaconquest/tiles/wall.png",
        "wall_top": "images/minigames/beaconquest/tiles/wall_top.png",
        "wall_corner_tl": "images/minigames/beaconquest/tiles/wall_corner_tl.png",
        "wall_corner_tr": "images/minigames/beaconquest/tiles/wall_corner_tr.png",
        "wall_corner_bl": "images/minigames/beaconquest/tiles/wall_corner_bl.png",
        "wall_corner_br": "images/minigames/beaconquest/tiles/wall_corner_br.png",
        "beacon_base": "images/minigames/beaconquest/tiles/beacon_base.png",
        "beacon_active": "images/minigames/beaconquest/tiles/beacon_active.png",
        "beacon_inactive": "images/minigames/beaconquest/tiles/beacon_inactive.png",
        "beacon_glow": "images/minigames/beaconquest/tiles/beacon_glow.png",
        "bridge": "images/minigames/beaconquest/tiles/bridge.png",
        "door_closed": "images/minigames/beaconquest/tiles/door_closed.png",
        "door_open": "images/minigames/beaconquest/tiles/door_open.png",
        "chest_closed": "images/minigames/beaconquest/tiles/chest_closed.png",
        "chest_open": "images/minigames/beaconquest/tiles/chest_open.png",
    }

    # Collectible shard sprites
    SHARD_SPRITES = {
        "shard": "images/minigames/beaconquest/items/shard.png",
        "shard_glow": "images/minigames/beaconquest/items/shard_glow.png",
        "shard_sparkle": "images/minigames/beaconquest/items/shard_sparkle.png",
    }

    # Other collectible items (for future expansion)
    ITEM_SPRITES = {
        "health_potion": "images/minigames/beaconquest/items/health_potion.png",
        "key": "images/minigames/beaconquest/items/key.png",
        "coin": "images/minigames/beaconquest/items/coin.png",
        "powerup_speed": "images/minigames/beaconquest/items/powerup_speed.png",
        "powerup_attack": "images/minigames/beaconquest/items/powerup_attack.png",
    }

    # Weapon/attack effect sprites
    WEAPON_SPRITES = {
        "sword": "images/minigames/beaconquest/weapons/sword.png",
        "sword_swing": "images/minigames/beaconquest/weapons/sword_swing.png",
        "sword_sparkle": "images/minigames/beaconquest/weapons/sword_sparkle.png",
        "slash_effect_0": "images/minigames/beaconquest/weapons/slash_effect_0.png",
        "slash_effect_1": "images/minigames/beaconquest/weapons/slash_effect_1.png",
        "slash_effect_2": "images/minigames/beaconquest/weapons/slash_effect_2.png",
    }

    # Projectile sprites (for ranged attacks/enemies)
    PROJECTILE_SPRITES = {
        "arrow": "images/minigames/beaconquest/projectiles/arrow.png",
        "magic_bolt": "images/minigames/beaconquest/projectiles/magic_bolt.png",
        "shadow_ball": "images/minigames/beaconquest/projectiles/shadow_ball.png",
        "light_beam": "images/minigames/beaconquest/projectiles/light_beam.png",
    }

    # Effect/particle sprites
    EFFECT_SPRITES = {
        "death_particle_purple": "images/minigames/beaconquest/effects/death_particle_purple.png",
        "death_particle_dark": "images/minigames/beaconquest/effects/death_particle_dark.png",
        "hit_spark": "images/minigames/beaconquest/effects/hit_spark.png",
        "collect_sparkle": "images/minigames/beaconquest/effects/collect_sparkle.png",
        "dust_cloud": "images/minigames/beaconquest/effects/dust_cloud.png",
        "magic_circle": "images/minigames/beaconquest/effects/magic_circle.png",
    }

    # UI element sprites
    UI_SPRITES = {
        "heart_full": "images/minigames/beaconquest/ui/heart_full.png",
        "heart_empty": "images/minigames/beaconquest/ui/heart_empty.png",
        "heart_half": "images/minigames/beaconquest/ui/heart_half.png",
        "shard_icon": "images/minigames/beaconquest/ui/shard_icon.png",
        "shard_icon_empty": "images/minigames/beaconquest/ui/shard_icon_empty.png",
        "panel_bg": "images/minigames/beaconquest/ui/panel_bg.png",
        "objective_panel": "images/minigames/beaconquest/ui/objective_panel.png",
    }

    # Background elements
    BACKGROUND_SPRITES = {
        "sky": "images/minigames/beaconquest/background/sky.png",
        "star_small": "images/minigames/beaconquest/background/star_small.png",
        "star_large": "images/minigames/beaconquest/background/star_large.png",
        "cloud": "images/minigames/beaconquest/background/cloud.png",
        "distant_island": "images/minigames/beaconquest/background/distant_island.png",
    }

    # Overlay sprites for end screens
    OVERLAY_SPRITES = {
        "victory_banner": "images/minigames/beaconquest/overlays/victory_banner.png",
        "gameover_banner": "images/minigames/beaconquest/overlays/gameover_banner.png",
        "vignette": "images/minigames/beaconquest/overlays/vignette.png",
    }

    # Tileset (alternative: single image containing all tiles)
    TILESET_SPRITE = "images/minigames/beaconquest/tiles/tileset.png"
    # Tileset layout: 8 tiles per row, includes all floor/wall variations

    # Sprite cache
    _sprite_cache = {}

    def load_sprite(path, scale=None):
        """Load a sprite from path with optional scaling."""
        cache_key = (path, scale)
        if cache_key in _sprite_cache:
            return _sprite_cache[cache_key]

        try:
            sprite = pygame.image.load(path).convert_alpha()
            if scale:
                sprite = pygame.transform.scale(sprite, scale)
            _sprite_cache[cache_key] = sprite
            return sprite
        except (pygame.error, FileNotFoundError):
            return None

    def get_player_sprite(state, direction, frame=0):
        """Get player sprite for current state.

        Args:
            state: 'idle', 'walk', or 'attack'
            direction: 'up', 'down', 'left', or 'right'
            frame: Animation frame number (0-3 for walk, 0-2 for attack)

        Returns:
            pygame.Surface or None
        """
        if not USE_SPRITES:
            return None

        if state == 'idle':
            key = f"idle_{direction}"
        elif state == 'walk':
            key = f"walk_{direction}_{frame % 4}"
        elif state == 'attack':
            key = f"attack_{direction}_{frame % 3}"
        else:
            return None

        path = PLAYER_SPRITES.get(key)
        if not path:
            return None
        return load_sprite(path)

    def get_enemy_sprite(enemy_type, state, frame=0):
        """Get enemy sprite for current state."""
        if not USE_SPRITES:
            return None

        sprites = ENEMY_TYPE_SPRITES.get(enemy_type, ENEMY_SPRITES)
        if state == 'idle':
            path = sprites.get('idle') or sprites.get('shadow_idle')
        elif state == 'move':
            key = f"move_{frame % 2}" if f"move_{frame % 2}" in sprites else f"shadow_move_{frame % 2}"
            path = sprites.get(key)
        elif state == 'hit':
            path = sprites.get('hit') or sprites.get('shadow_hit')
        else:
            return None

        if not path:
            return None
        return load_sprite(path)

    def get_tile_sprite(tile_type, variant=None):
        """Get tile sprite for map rendering."""
        if not USE_SPRITES:
            return None

        key = tile_type if variant is None else f"{tile_type}_{variant}"
        path = TILE_SPRITES.get(key)
        if not path:
            return None
        return load_sprite(path)

    def get_shard_sprite(state="shard"):
        """Get shard collectible sprite."""
        if not USE_SPRITES:
            return None
        path = SHARD_SPRITES.get(state)
        if not path:
            return None
        return load_sprite(path)

    def get_weapon_sprite(weapon, state="sword"):
        """Get weapon or attack effect sprite."""
        if not USE_SPRITES:
            return None
        path = WEAPON_SPRITES.get(state)
        if not path:
            return None
        return load_sprite(path)

    def get_effect_sprite(effect_type, size=None):
        """Get particle/effect sprite."""
        if not USE_SPRITES:
            return None
        path = EFFECT_SPRITES.get(effect_type)
        if not path:
            return None
        return load_sprite(path, size)

    def get_ui_sprite(element, size=None):
        """Get UI element sprite."""
        if not USE_SPRITES:
            return None
        path = UI_SPRITES.get(element)
        if not path:
            return None
        return load_sprite(path, size)

    def get_projectile_sprite(projectile_type, size=None):
        """Get projectile sprite for ranged attacks."""
        if not USE_SPRITES:
            return None
        path = PROJECTILE_SPRITES.get(projectile_type)
        if not path:
            return None
        return load_sprite(path, size)

    def clear_sprite_cache():
        """Clear the sprite cache to free memory."""
        _sprite_cache.clear()

    ####################################################################################################################
    # END SPRITE CONFIGURATION
    ####################################################################################################################

    # Game constants
    WIDTH, HEIGHT = 1920, 1080
    TILE_SIZE = 64

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
    TILE_DOOR = 4
    TILE_VOID = 5
    TILE_BRIDGE = 6

    # Game states
    STATE_PLAYING = "playing"
    STATE_VICTORY = "victory"
    STATE_GAMEOVER = "gameover"

    # Direction vectors
    DIRECTIONS = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)
    }

    class Player:
        """The player character."""
        def __init__(self, x, y):
            self.x = x * TILE_SIZE + MAP_OFFSET_X
            self.y = y * TILE_SIZE + MAP_OFFSET_Y
            self.tile_x = x
            self.tile_y = y
            self.width = 48
            self.height = 48
            self.speed = 5

            self.health = 5
            self.max_health = 5
            self.shards_collected = 0
            self.target_shards = 3

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

        def update(self, dt, keys, game_map, enemies):
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

            # Animation
            if self.moving:
                self.anim_timer += dt
                if self.anim_timer >= 150:
                    self.anim_timer = 0
                    self.anim_frame = (self.anim_frame + 1) % 4
            else:
                self.anim_frame = 0

        def can_move_to(self, new_x, new_y, game_map):
            """Check if player can move to position."""
            # Check corners of player hitbox
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

        def attack(self):
            """Start attack animation."""
            if not self.attacking and self.attack_cooldown <= 0:
                self.attacking = True
                self.attack_timer = 0
                self.attack_cooldown = 300

        def get_attack_rect(self):
            """Get the attack hitbox based on facing direction."""
            attack_range = 50
            attack_width = 60

            cx = self.x + self.width // 2
            cy = self.y + self.height // 2

            if self.facing == 'up':
                return pygame.Rect(cx - attack_width // 2, cy - attack_range - 10, attack_width, attack_range)
            elif self.facing == 'down':
                return pygame.Rect(cx - attack_width // 2, cy + 10, attack_width, attack_range)
            elif self.facing == 'left':
                return pygame.Rect(cx - attack_range - 10, cy - attack_width // 2, attack_range, attack_width)
            else:  # right
                return pygame.Rect(cx + 10, cy - attack_width // 2, attack_range, attack_width)

        def take_damage(self, amount=1):
            """Take damage if not invulnerable."""
            if self.invulnerable <= 0:
                self.health -= amount
                self.invulnerable = 1000  # 1 second of invulnerability
                return True
            return False

        def draw(self, surf, time_ms):
            # Flash when invulnerable
            if self.invulnerable > 0 and (time_ms // 100) % 2 == 0:
                return

            # Determine color based on player (green for player)
            color = (100, 200, 100)
            outline = (60, 150, 60)

            # Draw shadow
            shadow_surf = pygame.Surface((self.width, 20), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
            surf.blit(shadow_surf, (self.x, self.y + self.height - 10))

            # Draw body
            body_offset = 0
            if self.moving:
                body_offset = math.sin(time_ms * 0.015) * 3

            pygame.draw.rect(surf, outline, (self.x + 4, self.y + body_offset + 4, self.width - 8, self.height - 8), border_radius=8)
            pygame.draw.rect(surf, color, (self.x + 6, self.y + body_offset + 6, self.width - 12, self.height - 12), border_radius=6)

            # Draw face based on direction
            face_x = self.x + self.width // 2
            face_y = self.y + self.height // 2 + body_offset - 5

            # Eyes
            eye_offset = {'up': (0, -8), 'down': (0, 8), 'left': (-8, 0), 'right': (8, 0)}
            ex, ey = eye_offset[self.facing]

            pygame.draw.circle(surf, (255, 255, 255), (face_x - 8, face_y), 6)
            pygame.draw.circle(surf, (255, 255, 255), (face_x + 8, face_y), 6)
            pygame.draw.circle(surf, (40, 40, 40), (face_x - 8 + ex // 2, face_y + ey // 2), 3)
            pygame.draw.circle(surf, (40, 40, 40), (face_x + 8 + ex // 2, face_y + ey // 2), 3)

            # Draw attack effect
            if self.attacking:
                self.draw_attack(surf, time_ms)

        def draw_attack(self, surf, time_ms):
            """Draw sword swing effect."""
            attack_rect = self.get_attack_rect()
            progress = self.attack_timer / self.attack_duration

            # Sword swing arc
            cx = self.x + self.width // 2
            cy = self.y + self.height // 2

            swing_length = 45
            swing_width = 4

            if self.facing == 'up':
                base_angle = -90
                swing_range = 90
            elif self.facing == 'down':
                base_angle = 90
                swing_range = 90
            elif self.facing == 'left':
                base_angle = 180
                swing_range = 90
            else:
                base_angle = 0
                swing_range = 90

            # Calculate swing angle
            swing_angle = base_angle + (progress - 0.5) * swing_range
            rad = math.radians(swing_angle)

            end_x = cx + math.cos(rad) * swing_length
            end_y = cy + math.sin(rad) * swing_length

            # Draw sword
            pygame.draw.line(surf, (200, 200, 220), (cx, cy), (end_x, end_y), swing_width + 2)
            pygame.draw.line(surf, (255, 255, 255), (cx, cy), (end_x, end_y), swing_width)

            # Sparkle at tip
            sparkle_size = 4 + int(3 * math.sin(progress * math.pi))
            pygame.draw.circle(surf, (255, 255, 200), (int(end_x), int(end_y)), sparkle_size)

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

    class BeaconQuestGame:
        """Main game controller for Beacon Quest."""
        def __init__(self):
            self.state = STATE_PLAYING

            # Create map
            self.game_map = self.create_map()

            # Create player
            self.player = Player(10, 11)  # Start near bottom center

            # Create enemies
            self.enemies = [
                Enemy(5, 3),
                Enemy(14, 3),
                Enemy(3, 7),
                Enemy(16, 7),
                Enemy(10, 5),
            ]

            # Create shards
            self.shards = [
                Shard(3, 2),
                Shard(16, 2),
                Shard(10, 1),
            ]

            self.effects = []

            # Camera shake
            self.shake_amount = 0
            self.shake_timer = 0

        def create_map(self):
            """Create the game map."""
            # 0=floor, 1=wall, 2=beacon, 5=void, 6=bridge
            game_map = [[TILE_VOID for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

            # Main platform (center area)
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

            # Inner walls/obstacles
            game_map[4][5] = TILE_WALL
            game_map[4][6] = TILE_WALL
            game_map[4][13] = TILE_WALL
            game_map[4][14] = TILE_WALL
            game_map[7][5] = TILE_WALL
            game_map[7][6] = TILE_WALL
            game_map[7][13] = TILE_WALL
            game_map[7][14] = TILE_WALL

            # Central beacon area
            game_map[1][9] = TILE_BEACON
            game_map[1][10] = TILE_BEACON

            return game_map

        def trigger_shake(self, amount=5):
            self.shake_amount = amount
            self.shake_timer = 200

        def update(self, dt):
            if self.state != STATE_PLAYING:
                return

            time_ms = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()

            # Update player
            self.player.update(dt, keys, self.game_map, self.enemies)

            # Check attack collision with enemies
            if self.player.attacking:
                attack_rect = self.player.get_attack_rect()
                for enemy in self.enemies:
                    if enemy.alive and attack_rect.colliderect(enemy.get_rect()):
                        if enemy.take_damage():
                            # Enemy died
                            self.effects.append(DeathEffect(enemy.x + enemy.width // 2,
                                                           enemy.y + enemy.height // 2))
                            self.trigger_shake(8)

            # Update enemies
            for enemy in self.enemies:
                enemy.update(dt, self.game_map, self.player)

                # Check collision with player
                if enemy.alive:
                    player_rect = pygame.Rect(self.player.x, self.player.y,
                                             self.player.width, self.player.height)
                    if player_rect.colliderect(enemy.get_rect()):
                        if self.player.take_damage():
                            self.trigger_shake(10)

            # Update shards
            for shard in self.shards:
                shard.update(dt)
                if not shard.collected:
                    player_rect = pygame.Rect(self.player.x, self.player.y,
                                             self.player.width, self.player.height)
                    if player_rect.colliderect(shard.get_rect()):
                        shard.collected = True
                        self.player.shards_collected += 1

            # Update effects
            self.effects = [e for e in self.effects if e.update(dt)]

            # Update shake
            if self.shake_timer > 0:
                self.shake_timer -= dt
                self.shake_amount *= 0.9
            else:
                self.shake_amount = 0

            # Check win/lose conditions
            if self.player.shards_collected >= self.player.target_shards:
                self.state = STATE_VICTORY
            elif self.player.health <= 0:
                self.state = STATE_GAMEOVER

        def handle_key_down(self, key):
            if self.state != STATE_PLAYING:
                return

            if key == K_SPACE or key == K_j:
                self.player.attack()

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
            for shard in self.shards:
                shard.draw(game_surf, time_ms)

            # Draw enemies
            for enemy in self.enemies:
                enemy.draw(game_surf, time_ms)

            # Draw player
            self.player.draw(game_surf, time_ms)

            # Draw effects
            for effect in self.effects:
                effect.draw(game_surf)

            # Blit with shake
            surf.blit(game_surf, (shake_x, shake_y))

            # Draw UI (no shake)
            self.draw_ui(surf)

            # Draw end screens
            if self.state == STATE_VICTORY:
                self.draw_overlay(surf, "BEACON RESTORED!", (100, 255, 150), "The light shines again!")
            elif self.state == STATE_GAMEOVER:
                self.draw_overlay(surf, "DEFEATED", (255, 100, 100), "The shadows overwhelmed you...")

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
            """Draw the game map."""
            for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    tile = self.game_map[y][x]
                    px = x * TILE_SIZE + MAP_OFFSET_X
                    py = y * TILE_SIZE + MAP_OFFSET_Y

                    if tile == TILE_FLOOR:
                        # Stone floor with pattern
                        color = (60, 50, 80) if (x + y) % 2 == 0 else (55, 45, 75)
                        pygame.draw.rect(surf, color, (px, py, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(surf, (70, 60, 90), (px, py, TILE_SIZE, TILE_SIZE), 1)

                    elif tile == TILE_WALL:
                        # Stone wall
                        pygame.draw.rect(surf, (80, 70, 100), (px, py, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(surf, (100, 90, 120), (px + 4, py + 4, TILE_SIZE - 8, TILE_SIZE - 16))
                        pygame.draw.rect(surf, (60, 50, 80), (px, py, TILE_SIZE, TILE_SIZE), 2)

                    elif tile == TILE_BEACON:
                        # Beacon pedestal
                        pygame.draw.rect(surf, (60, 50, 80), (px, py, TILE_SIZE, TILE_SIZE))

                        # Glowing beacon
                        glow = 0.5 + 0.3 * math.sin(time_ms * 0.003)
                        glow_size = int(40 + 15 * glow)

                        # Check if all shards collected
                        if self.player.shards_collected >= self.player.target_shards:
                            glow_color = (255, 220, 100, int(150 * glow))
                            beacon_color = (255, 240, 150)
                        else:
                            glow_color = (100, 80, 150, int(80 * glow))
                            beacon_color = (150, 130, 180)

                        glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
                        pygame.draw.circle(glow_surf, glow_color, (glow_size, glow_size), glow_size)
                        surf.blit(glow_surf, (px + TILE_SIZE // 2 - glow_size, py + TILE_SIZE // 2 - glow_size))

                        pygame.draw.circle(surf, beacon_color, (px + TILE_SIZE // 2, py + TILE_SIZE // 2), 15)

                    elif tile == TILE_VOID:
                        # Nothing - void/sky
                        pass

        def draw_ui(self, surf):
            """Draw game UI."""
            font_medium = pygame.font.Font(None, 36)
            font_small = pygame.font.Font(None, 28)

            # Health (top left)
            for i in range(self.player.max_health):
                x = 30 + i * 40
                y = 30
                if i < self.player.health:
                    color = (255, 100, 100)
                else:
                    color = (60, 50, 80)

                # Heart shape
                pygame.draw.circle(surf, color, (x, y), 12)
                pygame.draw.circle(surf, color, (x + 12, y), 12)
                pygame.draw.polygon(surf, color, [(x - 12, y + 2), (x + 24, y + 2), (x + 6, y + 22)])

            # Shards (top right)
            shard_text = font_medium.render(f"Shards: {self.player.shards_collected}/{self.player.target_shards}",
                                           True, (255, 220, 100))
            surf.blit(shard_text, (WIDTH - 200, 30))

            # Controls hint (bottom)
            controls = font_small.render("Arrow Keys/WASD: Move | SPACE/J: Attack", True, (150, 140, 180))
            surf.blit(controls, (WIDTH // 2 - controls.get_width() // 2, HEIGHT - 40))

            # Objective
            if self.player.shards_collected < self.player.target_shards:
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

    call screen beacon_quest_screen()

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
