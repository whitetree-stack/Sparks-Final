# valley_minigames.rpy - Valley Region Minigames
# Contains: Tree Climb Scroller + Vine Blaster (Beacon Rescue)

####################################################################################################################
# SPRITE CONFIGURATION - Set USE_SPRITES = True and provide sprite paths to use custom graphics
# This configuration applies to both Vine Blaster and Valley Climb minigames
####################################################################################################################

init python:
    ################################################################################################
    # VALLEY MINIGAMES SPRITE CONFIGURATION
    ################################################################################################

    VALLEY_USE_SPRITES = False  # Set to True when sprites are ready

    # Character sprites (Tristan and Henry for both minigames)
    VALLEY_CHARACTER_SPRITES = {
        # Tristan (green/older brother)
        "tristan_idle": "images/minigames/valley/characters/tristan_idle.png",
        "tristan_walk_left": "images/minigames/valley/characters/tristan_walk_left.png",
        "tristan_walk_right": "images/minigames/valley/characters/tristan_walk_right.png",
        "tristan_jump": "images/minigames/valley/characters/tristan_jump.png",
        "tristan_climb_0": "images/minigames/valley/characters/tristan_climb_0.png",
        "tristan_climb_1": "images/minigames/valley/characters/tristan_climb_1.png",
        "tristan_aim": "images/minigames/valley/characters/tristan_aim.png",
        "tristan_hurt": "images/minigames/valley/characters/tristan_hurt.png",
        "tristan_glow": "images/minigames/valley/characters/tristan_glow.png",

        # Henry (blue/younger brother)
        "henry_idle": "images/minigames/valley/characters/henry_idle.png",
        "henry_walk_left": "images/minigames/valley/characters/henry_walk_left.png",
        "henry_walk_right": "images/minigames/valley/characters/henry_walk_right.png",
        "henry_jump": "images/minigames/valley/characters/henry_jump.png",
        "henry_climb_0": "images/minigames/valley/characters/henry_climb_0.png",
        "henry_climb_1": "images/minigames/valley/characters/henry_climb_1.png",
        "henry_aim": "images/minigames/valley/characters/henry_aim.png",
        "henry_hurt": "images/minigames/valley/characters/henry_hurt.png",
        "henry_glow": "images/minigames/valley/characters/henry_glow.png",
    }

    # Spider enemy sprites (used in both minigames)
    SPIDER_SPRITES = {
        # Walking animation frames (5 frames per direction)
        "walk_up_0": "images/minigames/valley/enemies/spider_walk_up_0.png",
        "walk_up_1": "images/minigames/valley/enemies/spider_walk_up_1.png",
        "walk_up_2": "images/minigames/valley/enemies/spider_walk_up_2.png",
        "walk_up_3": "images/minigames/valley/enemies/spider_walk_up_3.png",
        "walk_up_4": "images/minigames/valley/enemies/spider_walk_up_4.png",
        "walk_down_0": "images/minigames/valley/enemies/spider_walk_down_0.png",
        "walk_down_1": "images/minigames/valley/enemies/spider_walk_down_1.png",
        "walk_down_2": "images/minigames/valley/enemies/spider_walk_down_2.png",
        "walk_down_3": "images/minigames/valley/enemies/spider_walk_down_3.png",
        "walk_down_4": "images/minigames/valley/enemies/spider_walk_down_4.png",
        "walk_left_0": "images/minigames/valley/enemies/spider_walk_left_0.png",
        "walk_left_1": "images/minigames/valley/enemies/spider_walk_left_1.png",
        "walk_left_2": "images/minigames/valley/enemies/spider_walk_left_2.png",
        "walk_left_3": "images/minigames/valley/enemies/spider_walk_left_3.png",
        "walk_left_4": "images/minigames/valley/enemies/spider_walk_left_4.png",
        "walk_right_0": "images/minigames/valley/enemies/spider_walk_right_0.png",
        "walk_right_1": "images/minigames/valley/enemies/spider_walk_right_1.png",
        "walk_right_2": "images/minigames/valley/enemies/spider_walk_right_2.png",
        "walk_right_3": "images/minigames/valley/enemies/spider_walk_right_3.png",
        "walk_right_4": "images/minigames/valley/enemies/spider_walk_right_4.png",
        # Death animation (4 frames)
        "death_0": "images/minigames/valley/enemies/spider_death_0.png",
        "death_1": "images/minigames/valley/enemies/spider_death_1.png",
        "death_2": "images/minigames/valley/enemies/spider_death_2.png",
        "death_3": "images/minigames/valley/enemies/spider_death_3.png",
        # Hit flash
        "hit": "images/minigames/valley/enemies/spider_hit.png",
    }

    # Vine sprites for Vine Blaster
    VINE_SPRITES = {
        # Vine segment images (rotated to follow path)
        "segment_1": "images/minigames/valley/vines/segment_1.png",
        "segment_2": "images/minigames/valley/vines/segment_2.png",
        "segment_3": "images/minigames/valley/vines/segment_3.png",
        "segment_4": "images/minigames/valley/vines/segment_4.png",
        # Vine tip (animated, dangerous part)
        "tip": "images/minigames/valley/vines/tip.png",
        "tip_open": "images/minigames/valley/vines/tip_open.png",
        "tip_attack": "images/minigames/valley/vines/tip_attack.png",
        # Root/base where vine spawns
        "root": "images/minigames/valley/vines/root.png",
    }

    # Projectile/Fireball sprites
    PROJECTILE_SPRITES = {
        # Tristan's fireballs (orange/yellow)
        "fireball_orange_0": "images/minigames/valley/projectiles/fireball_orange_0.png",
        "fireball_orange_1": "images/minigames/valley/projectiles/fireball_orange_1.png",
        "fireball_orange_2": "images/minigames/valley/projectiles/fireball_orange_2.png",
        "fireball_orange_3": "images/minigames/valley/projectiles/fireball_orange_3.png",
        "fireball_orange_trail": "images/minigames/valley/projectiles/fireball_orange_trail.png",
        # Henry's fireballs (blue)
        "fireball_blue_0": "images/minigames/valley/projectiles/fireball_blue_0.png",
        "fireball_blue_1": "images/minigames/valley/projectiles/fireball_blue_1.png",
        "fireball_blue_2": "images/minigames/valley/projectiles/fireball_blue_2.png",
        "fireball_blue_3": "images/minigames/valley/projectiles/fireball_blue_3.png",
        "fireball_blue_trail": "images/minigames/valley/projectiles/fireball_blue_trail.png",
        # Impact effects
        "impact_orange": "images/minigames/valley/projectiles/impact_orange.png",
        "impact_blue": "images/minigames/valley/projectiles/impact_blue.png",
    }

    # Beacon sprites (central objective in Vine Blaster)
    BEACON_SPRITES = {
        "beacon_base": "images/minigames/valley/beacon/beacon_base.png",
        "beacon_light": "images/minigames/valley/beacon/beacon_light.png",
        "beacon_glow": "images/minigames/valley/beacon/beacon_glow.png",
        "beacon_danger": "images/minigames/valley/beacon/beacon_danger.png",
        "beacon_shield": "images/minigames/valley/beacon/beacon_shield.png",
    }

    # Tree/Platform sprites for Valley Climb
    PLATFORM_SPRITES = {
        "branch_left": "images/minigames/valley/platforms/branch_left.png",
        "branch_right": "images/minigames/valley/platforms/branch_right.png",
        "branch_middle": "images/minigames/valley/platforms/branch_middle.png",
        "platform_wood": "images/minigames/valley/platforms/platform_wood.png",
        "platform_moss": "images/minigames/valley/platforms/platform_moss.png",
        "vine_swing": "images/minigames/valley/platforms/vine_swing.png",
        "mushroom": "images/minigames/valley/platforms/mushroom.png",
    }

    # Tree trunk and background for Valley Climb
    TREE_SPRITES = {
        "trunk_segment": "images/minigames/valley/tree/trunk_segment.png",
        "trunk_knot": "images/minigames/valley/tree/trunk_knot.png",
        "trunk_hollow": "images/minigames/valley/tree/trunk_hollow.png",
        "bark_detail": "images/minigames/valley/tree/bark_detail.png",
        "leaves_bg": "images/minigames/valley/tree/leaves_bg.png",
        "canopy": "images/minigames/valley/tree/canopy.png",
    }

    # Collectible sprites for Valley Climb
    COLLECTIBLE_SPRITES = {
        "acorn": "images/minigames/valley/collectibles/acorn.png",
        "acorn_glow": "images/minigames/valley/collectibles/acorn_glow.png",
        "leaf_green": "images/minigames/valley/collectibles/leaf_green.png",
        "leaf_gold": "images/minigames/valley/collectibles/leaf_gold.png",
        "berry": "images/minigames/valley/collectibles/berry.png",
        "feather": "images/minigames/valley/collectibles/feather.png",
    }

    # Effect sprites
    VALLEY_EFFECT_SPRITES = {
        "hit_spark": "images/minigames/valley/effects/hit_spark.png",
        "death_puff": "images/minigames/valley/effects/death_puff.png",
        "collect_sparkle": "images/minigames/valley/effects/collect_sparkle.png",
        "dust_cloud": "images/minigames/valley/effects/dust_cloud.png",
        "leaf_particle": "images/minigames/valley/effects/leaf_particle.png",
        "second_wind_burst": "images/minigames/valley/effects/second_wind_burst.png",
    }

    # UI sprites
    VALLEY_UI_SPRITES = {
        "health_bar_bg": "images/minigames/valley/ui/health_bar_bg.png",
        "health_bar_fill": "images/minigames/valley/ui/health_bar_fill.png",
        "health_bar_danger": "images/minigames/valley/ui/health_bar_danger.png",
        "wave_indicator": "images/minigames/valley/ui/wave_indicator.png",
        "score_panel": "images/minigames/valley/ui/score_panel.png",
        "timer_panel": "images/minigames/valley/ui/timer_panel.png",
        "heart_icon": "images/minigames/valley/ui/heart_icon.png",
    }

    # Background sprites
    VALLEY_BACKGROUND_SPRITES = {
        "forest_bg": "images/minigames/valley/background/forest_bg.png",
        "sky_gradient": "images/minigames/valley/background/sky_gradient.png",
        "distant_trees": "images/minigames/valley/background/distant_trees.png",
        "mist_layer": "images/minigames/valley/background/mist_layer.png",
        "sunbeam": "images/minigames/valley/background/sunbeam.png",
    }

    # Overlay sprites
    VALLEY_OVERLAY_SPRITES = {
        "victory_banner": "images/minigames/valley/overlays/victory_banner.png",
        "gameover_banner": "images/minigames/valley/overlays/gameover_banner.png",
        "wave_complete": "images/minigames/valley/overlays/wave_complete.png",
        "second_wind_flash": "images/minigames/valley/overlays/second_wind_flash.png",
    }

    ################################################################################################
    # END SPRITE CONFIGURATION
    ################################################################################################

    ################################################################################################
    # AUDIO CONFIGURATION - Sound effects for Valley minigames
    ################################################################################################

    VALLEY_USE_AUDIO = True  # Set to False to disable all minigame audio

    VALLEY_AUDIO_PATHS = {
        # Vine Blaster sounds
        "fireball_shoot": "audio/sfx/minigames/valley/fireball_shoot.ogg",
        "fireball_hit": "audio/sfx/minigames/valley/fireball_hit.ogg",
        "vine_grow": "audio/sfx/minigames/valley/vine_grow.ogg",
        "vine_destroy": "audio/sfx/minigames/valley/vine_destroy.ogg",
        "spider_crawl": "audio/sfx/minigames/valley/spider_crawl.ogg",
        "spider_death": "audio/sfx/minigames/valley/spider_death.ogg",
        "beacon_danger": "audio/sfx/minigames/valley/beacon_danger.ogg",
        "second_wind": "audio/sfx/minigames/valley/second_wind.ogg",
        "wave_start": "audio/sfx/minigames/valley/wave_start.ogg",
        "wave_complete": "audio/sfx/minigames/valley/wave_complete.ogg",
        # Valley Climb sounds
        "jump": "audio/sfx/minigames/valley/jump.ogg",
        "land": "audio/sfx/minigames/valley/land.ogg",
        "climb": "audio/sfx/minigames/valley/climb.ogg",
        "acorn_collect": "audio/sfx/minigames/valley/acorn_collect.ogg",
        "branch_grab": "audio/sfx/minigames/valley/branch_grab.ogg",
        "fall": "audio/sfx/minigames/valley/fall.ogg",
        # Common
        "victory": "audio/sfx/minigames/common/victory.ogg",
        "defeat": "audio/sfx/minigames/common/defeat.ogg",
        "game_start": "audio/sfx/minigames/common/game_start.ogg",
    }

    # Music tracks for Valley minigames
    VALLEY_MUSIC_PATHS = {
        "vine_blaster": "audio/music/minigames/valley_vine_blaster.ogg",  # Action, intense defense
        "valley_climb": "audio/music/minigames/valley_climb.ogg",         # Upbeat, adventurous climbing
    }

    # Audio state
    _valley_audio_cache = {}
    _valley_audio_initialized = False
    _valley_music_playing = False

    def valley_init_audio():
        """Initialize pygame mixer for Valley minigames."""
        global _valley_audio_initialized
        if not _valley_audio_initialized:
            try:
                import pygame
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
                _valley_audio_initialized = True
            except:
                pass

    def valley_play_sound(sound_key, volume=1.0):
        """Play a sound effect for Valley minigames."""
        if not VALLEY_USE_AUDIO:
            return
        valley_init_audio()
        import pygame
        if sound_key in _valley_audio_cache:
            sound = _valley_audio_cache[sound_key]
        else:
            path = VALLEY_AUDIO_PATHS.get(sound_key)
            if path:
                try:
                    sound = pygame.mixer.Sound(path)
                    _valley_audio_cache[sound_key] = sound
                except:
                    return
            else:
                return
        sound.set_volume(volume)
        sound.play()

    def valley_start_music(game_type, volume=0.6):
        """Start playing music for a Valley minigame.

        Args:
            game_type: 'vine_blaster' or 'valley_climb'
            volume: Music volume (0.0 to 1.0)
        """
        global _valley_music_playing
        if not VALLEY_USE_AUDIO:
            return
        valley_init_audio()
        import pygame
        music_path = VALLEY_MUSIC_PATHS.get(game_type)
        if music_path:
            try:
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play(-1)  # Loop indefinitely
                _valley_music_playing = True
            except:
                pass

    def valley_stop_music(fadeout_ms=500):
        """Stop Valley minigame music with optional fadeout."""
        global _valley_music_playing
        if not VALLEY_USE_AUDIO:
            return
        try:
            import pygame
            pygame.mixer.music.fadeout(fadeout_ms)
            _valley_music_playing = False
        except:
            pass

    ################################################################################################
    # END AUDIO CONFIGURATION
    ################################################################################################

####################################################################################################################
# VINE BLASTER - Beacon Rescue Minigame
####################################################################################################################

init python in vine_blaster:
    import pygame
    import random
    import math
    from pygame.locals import *

    WIDTH, HEIGHT = 1920, 1080
    
    def img(path):
        return renpy.display.im.Image(path).load()
    
    # Load spider sprites (same as valley_climb uses)
    SPIDER_SCALE = 1.5  # Slightly smaller for vine blaster
    spider_walk_up = []
    spider_walk_down = []
    spider_walk_left = []
    spider_walk_right = []
    spider_death = []
    try:
        spider_walk_up = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
            (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
            int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(1, 6)]
        spider_walk_down = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
            (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
            int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(21, 26)]
        spider_walk_left = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
            (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
            int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(7, 12)]
        spider_walk_right = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
            (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
            int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(27, 32)]
        spider_death = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
            (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
            int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(41, 45)]
    except:
        pass  # Will use procedural fallback
    
    # Try to load vine segment images (fallback to procedural if not found)
    VINE_SEGMENTS = []
    VINE_TIP = None
    try:
        # Load vine segment images - expects images/enemies/vines/segment_1.png, etc.
        for i in range(1, 5):
            seg = img(f"images/enemies/vines/segment_{i}.png")
            VINE_SEGMENTS.append(pygame.transform.smoothscale(seg, (60, 60)))
        # Load vine tip image
        tip = img("images/enemies/vines/tip.png")
        VINE_TIP = pygame.transform.smoothscale(tip, (50, 50))
    except:
        VINE_SEGMENTS = []  # Will use procedural drawing
        VINE_TIP = None
    
    # Try to load fireball animation frames
    FIREBALL_FRAMES_TRISTAN = []
    FIREBALL_FRAMES_HENRY = []
    try:
        # Tristan's fireball (orange/yellow) - expects images/effects/fireball_orange/1.png, etc.
        for i in range(1, 5):
            frame = img(f"images/effects/fireball_orange/{i}.png")
            FIREBALL_FRAMES_TRISTAN.append(pygame.transform.smoothscale(frame, (48, 48)))
    except:
        FIREBALL_FRAMES_TRISTAN = []  # Will use circle fallback
    
    try:
        # Henry's fireball (blue) - expects images/effects/fireball_blue/1.png, etc.
        for i in range(1, 5):
            frame = img(f"images/effects/fireball_blue/{i}.png")
            FIREBALL_FRAMES_HENRY.append(pygame.transform.smoothscale(frame, (48, 48)))
    except:
        FIREBALL_FRAMES_HENRY = []  # Will use circle fallback
    
    BEACON_CENTER = (WIDTH // 2, HEIGHT // 2)
    BEACON_RADIUS = 80
    WAVE_COUNT = 3
    WAVE_DURATION = [30000, 45000, 60000]
    WAVE_SPAWN_RATE = [2000, 1500, 1000]
    MAX_ENCROACHMENT = 100
    ENCROACHMENT_RATE = 0.5
    SECOND_WIND_THRESHOLD = 100
    SECOND_WIND_RESET = 75
    MAX_SECOND_WINDS = 2
    
    class Projectile:
        def __init__(self, x, y, target_x, target_y, owner="tristan"):
            self.x, self.y = x, y
            self.owner = owner
            dx, dy = target_x - x, target_y - y
            dist = math.hypot(dx, dy)
            if dist > 0:
                self.vx = (dx / dist) * 20
                self.vy = (dy / dist) * 20
                self.angle = math.degrees(math.atan2(-dy, dx))  # For rotation
            else:
                self.vx, self.vy = 0, -20
                self.angle = 90
            self.alive = True
            self.radius = 12
            self.color = (255, 220, 100) if owner == "tristan" else (100, 200, 255)
            # Animation
            self.anim_frame = 0
            self.anim_timer = 0
            self.anim_speed = 50  # ms per frame
            # Trail effect
            self.trail = []
            self.max_trail = 5
        
        def update(self, dt):
            # Store trail position
            self.trail.append((self.x, self.y))
            if len(self.trail) > self.max_trail:
                self.trail.pop(0)
            
            self.x += self.vx
            self.y += self.vy
            if self.x < -50 or self.x > WIDTH + 50 or self.y < -50 or self.y > HEIGHT + 50:
                self.alive = False
            # Update animation
            self.anim_timer += dt
            if self.anim_timer >= self.anim_speed:
                self.anim_timer = 0
                frames = FIREBALL_FRAMES_TRISTAN if self.owner == "tristan" else FIREBALL_FRAMES_HENRY
                if frames:
                    self.anim_frame = (self.anim_frame + 1) % len(frames)
        
        def draw(self, surf):
            # Draw trail
            for i, (tx, ty) in enumerate(self.trail):
                alpha = int(100 * (i + 1) / len(self.trail))
                trail_radius = int(self.radius * (i + 1) / len(self.trail) * 0.7)
                trail_surf = pygame.Surface((trail_radius * 2 + 4, trail_radius * 2 + 4), pygame.SRCALPHA)
                trail_color = (*self.color[:3], alpha)
                pygame.draw.circle(trail_surf, trail_color, (trail_radius + 2, trail_radius + 2), trail_radius)
                surf.blit(trail_surf, (int(tx) - trail_radius - 2, int(ty) - trail_radius - 2))
            
            # Try to use animated sprite
            frames = FIREBALL_FRAMES_TRISTAN if self.owner == "tristan" else FIREBALL_FRAMES_HENRY
            if frames:
                frame = frames[self.anim_frame % len(frames)]
                # Rotate to face movement direction
                rotated = pygame.transform.rotate(frame, self.angle)
                rect = rotated.get_rect(center=(int(self.x), int(self.y)))
                surf.blit(rotated, rect)
            else:
                # Fallback to glowing circles
                # Outer glow
                glow_surf = pygame.Surface((self.radius * 4, self.radius * 4), pygame.SRCALPHA)
                pygame.draw.circle(glow_surf, (*self.color[:3], 80), (self.radius * 2, self.radius * 2), self.radius * 2)
                surf.blit(glow_surf, (int(self.x) - self.radius * 2, int(self.y) - self.radius * 2))
                # Core
                pygame.draw.circle(surf, (255, 255, 255), (int(self.x), int(self.y)), self.radius + 4)
                pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.radius)
        
        def rect(self):
            return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
    
    class VineSegment:
        def __init__(self, edge="top"):
            self.edge = edge
            self.hp = 3
            self.max_hp = 3
            self.alive = True
            self.width = 40
            self.growth = 0
            self.growth_speed = 0.02
            
            if edge == "top":
                self.x = random.randint(200, WIDTH - 200)
                self.y = 0
                self.target_x = BEACON_CENTER[0] + random.randint(-100, 100)
                self.target_y = BEACON_CENTER[1]
            elif edge == "bottom":
                self.x = random.randint(200, WIDTH - 200)
                self.y = HEIGHT
                self.target_x = BEACON_CENTER[0] + random.randint(-100, 100)
                self.target_y = BEACON_CENTER[1]
            elif edge == "left":
                self.x = 0
                self.y = random.randint(200, HEIGHT - 200)
                self.target_x = BEACON_CENTER[0]
                self.target_y = BEACON_CENTER[1] + random.randint(-100, 100)
            else:
                self.x = WIDTH
                self.y = random.randint(200, HEIGHT - 200)
                self.target_x = BEACON_CENTER[0]
                self.target_y = BEACON_CENTER[1] + random.randint(-100, 100)
            
            self.wiggle_offset = random.random() * math.pi * 2
            self.wiggle_speed = 2 + random.random()
            
            # Hit flash effect
            self.hit_flash_timer = 0
            self.hit_flash_duration = 100
        
        def update(self, dt):
            if not self.alive:
                return
            self.growth += self.growth_speed * (dt / 1000)
            self.growth = min(1.0, self.growth)
            # Update hit flash
            if self.hit_flash_timer > 0:
                self.hit_flash_timer = max(0, self.hit_flash_timer - dt)
        
        def get_tip_position(self):
            tip_x = self.x + (self.target_x - self.x) * self.growth
            tip_y = self.y + (self.target_y - self.y) * self.growth
            return (tip_x, tip_y)
        
        def take_damage(self, amount=1):
            self.hp -= amount
            self.hit_flash_timer = self.hit_flash_duration
            if self.hp <= 0:
                self.alive = False
                return True
            return False
        
        def draw(self, surf, time_ms):
            if not self.alive:
                return
            tip_x, tip_y = self.get_tip_position()
            num_segments = max(2, int(self.growth * 20))
            points = []
            for i in range(num_segments + 1):
                t = i / num_segments
                px = self.x + (tip_x - self.x) * t
                py = self.y + (tip_y - self.y) * t
                wiggle = math.sin(time_ms * 0.003 * self.wiggle_speed + t * 10 + self.wiggle_offset) * 15 * t
                dx, dy = tip_x - self.x, tip_y - self.y
                length = math.hypot(dx, dy)
                if length > 0:
                    px += (-dy / length) * wiggle
                    py += (dx / length) * wiggle
                points.append((int(px), int(py)))
            
            if len(points) >= 2:
                # Check if we have vine segment images
                if VINE_SEGMENTS:
                    # Draw vine using images along the path
                    for i in range(len(points) - 1):
                        p1 = points[i]
                        p2 = points[i + 1]
                        # Calculate angle between points
                        angle = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]))
                        # Select segment image based on position (cycle through)
                        seg_img = VINE_SEGMENTS[i % len(VINE_SEGMENTS)].copy()
                        
                        # Hit flash effect
                        if self.hit_flash_timer > 0:
                            flash_surf = pygame.Surface(seg_img.get_size(), pygame.SRCALPHA)
                            flash_surf.fill((255, 255, 255, 150))
                            seg_img.blit(flash_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
                        
                        # Tint based on health
                        health_ratio = self.hp / self.max_hp
                        if health_ratio < 1.0:
                            dark_overlay = pygame.Surface(seg_img.get_size(), pygame.SRCALPHA)
                            dark_overlay.fill((0, 0, 0, int(100 * (1 - health_ratio))))
                            seg_img.blit(dark_overlay, (0, 0))
                        
                        # Rotate to face direction
                        rotated = pygame.transform.rotate(seg_img, -angle)
                        # Position at midpoint between p1 and p2
                        mid_x = (p1[0] + p2[0]) // 2
                        mid_y = (p1[1] + p2[1]) // 2
                        rect = rotated.get_rect(center=(mid_x, mid_y))
                        surf.blit(rotated, rect)
                    
                    # Draw tip
                    if VINE_TIP:
                        tip_angle = math.degrees(math.atan2(
                            points[-1][1] - points[-2][1],
                            points[-1][0] - points[-2][0]
                        ))
                        tip_img = VINE_TIP.copy()
                        if self.hit_flash_timer > 0:
                            flash_surf = pygame.Surface(tip_img.get_size(), pygame.SRCALPHA)
                            flash_surf.fill((255, 255, 255, 150))
                            tip_img.blit(flash_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
                        rotated_tip = pygame.transform.rotate(tip_img, -tip_angle)
                        tip_rect = rotated_tip.get_rect(center=points[-1])
                        surf.blit(rotated_tip, tip_rect)
                    else:
                        # Fallback tip
                        tip_color = (255, 200, 200) if self.hit_flash_timer > 0 else (255, 100, 100)
                        pygame.draw.circle(surf, tip_color, (int(tip_x), int(tip_y)), 15, 2)
                else:
                    # Fallback to procedural drawing with improved visuals
                    # Outer dark edge
                    pygame.draw.lines(surf, (20, 60, 20), False, points, self.width + 6)
                    
                    # Main vine body - color based on health
                    health_ratio = self.hp / self.max_hp
                    if self.hit_flash_timer > 0:
                        green = 200  # Flash brighter
                        red = 150
                    else:
                        green = int(100 + 80 * health_ratio)
                        red = int(60 - 20 * health_ratio)
                    pygame.draw.lines(surf, (red, green, 30), False, points, self.width)
                    
                    # Inner highlight
                    pygame.draw.lines(surf, (60, int(120 + 40 * health_ratio), 40), False, points, self.width // 2)
                    
                    # Tip with pulsing effect
                    tip_pulse = math.sin(time_ms * 0.01) * 3
                    tip_color = (255, 200, 200) if self.hit_flash_timer > 0 else (255, 100, 100)
                    pygame.draw.circle(surf, tip_color, (int(tip_x), int(tip_y)), int(15 + tip_pulse))
                    pygame.draw.circle(surf, (255, 150, 150), (int(tip_x), int(tip_y)), int(10 + tip_pulse))
        
        def rect(self):
            tip_x, tip_y = self.get_tip_position()
            return pygame.Rect(tip_x - 25, tip_y - 25, 50, 50)
    
    class VineSpider:
        def __init__(self, vine):
            self.vine = vine
            self.progress = 0
            self.speed = 0.1
            self.hp = 1
            self.alive = True
            self.size = 30
            self.anim_timer = 0
            self.anim_frame = 0
            self.leg_offset = random.random() * math.pi * 2
            # Track position for facing direction
            self.prev_x = vine.x
            self.prev_y = vine.y
            self.facing = 3  # 0=left, 1=right, 2=up, 3=down
            # Hit flash effect
            self.hit_flash_timer = 0
            self.hit_flash_duration = 150
        
        def update(self, dt):
            if not self.alive or not self.vine.alive:
                self.alive = False
                return
            # Store previous position for facing
            old_x, old_y = self.get_position()
            
            self.progress += self.speed * (dt / 1000)
            self.progress = min(1.0, self.progress)
            self.anim_timer += dt
            
            # Update hit flash
            if self.hit_flash_timer > 0:
                self.hit_flash_timer = max(0, self.hit_flash_timer - dt)
            
            # Update animation frame
            if self.anim_timer > 100:
                self.anim_frame = (self.anim_frame + 1) % 5
                self.anim_timer = 0
            
            # Calculate facing based on movement direction
            new_x, new_y = self.get_position()
            dx = new_x - old_x
            dy = new_y - old_y
            if abs(dx) > 0.1 or abs(dy) > 0.1:
                if abs(dx) > abs(dy):
                    self.facing = 0 if dx < 0 else 1  # left or right
                else:
                    self.facing = 2 if dy < 0 else 3  # up or down
        
        def get_position(self):
            tip_x, tip_y = self.vine.get_tip_position()
            x = self.vine.x + (tip_x - self.vine.x) * self.progress
            y = self.vine.y + (tip_y - self.vine.y) * self.progress
            return (x, y)
        
        def reached_beacon(self):
            return self.progress >= 0.95
        
        def take_damage(self, amount=1):
            self.hp -= amount
            self.hit_flash_timer = self.hit_flash_duration
            if self.hp <= 0:
                self.alive = False
                return True
            return False
        
        def draw(self, surf):
            if not self.alive:
                return
            x, y = self.get_position()
            
            # Try to use sprite animation
            sprite_sets = [spider_walk_left, spider_walk_right, spider_walk_up, spider_walk_down]
            if sprite_sets[self.facing]:
                sprites = sprite_sets[self.facing]
                frame = self.anim_frame % len(sprites)
                sprite = sprites[frame]
                
                # Apply hit flash effect
                if self.hit_flash_timer > 0:
                    sprite = sprite.copy()
                    white_surface = pygame.Surface(sprite.get_size(), pygame.SRCALPHA)
                    white_surface.fill((255, 255, 255, 180))
                    sprite.blit(white_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
                
                # Center sprite on position
                draw_x = int(x - sprite.get_width() // 2)
                draw_y = int(y - sprite.get_height() // 2)
                surf.blit(sprite, (draw_x, draw_y))
            else:
                # Fallback to procedural drawing
                leg_phase = self.anim_timer * 0.01 + self.leg_offset
                # Body
                body_color = (255, 200, 200) if self.hit_flash_timer > 0 else (60, 40, 80)
                inner_color = (255, 220, 220) if self.hit_flash_timer > 0 else (80, 60, 100)
                pygame.draw.circle(surf, body_color, (int(x), int(y)), self.size)
                pygame.draw.circle(surf, inner_color, (int(x), int(y)), self.size - 5)
                # Eyes
                pygame.draw.circle(surf, (200, 50, 50), (int(x - 8), int(y - 5)), 6)
                pygame.draw.circle(surf, (200, 50, 50), (int(x + 8), int(y - 5)), 6)
                pygame.draw.circle(surf, (255, 255, 255), (int(x - 8), int(y - 5)), 3)
                pygame.draw.circle(surf, (255, 255, 255), (int(x + 8), int(y - 5)), 3)
                # Animated legs
                for i, angle in enumerate(range(0, 360, 45)):
                    rad = math.radians(angle)
                    leg_anim = math.sin(leg_phase + i * 0.5) * 5
                    leg_x = x + math.cos(rad) * (self.size + 10 + leg_anim)
                    leg_y = y + math.sin(rad) * (self.size + 10 + leg_anim)
                    leg_color = (255, 180, 180) if self.hit_flash_timer > 0 else (40, 30, 50)
                    pygame.draw.line(surf, leg_color, (int(x), int(y)), (int(leg_x), int(leg_y)), 3)
        
        def rect(self):
            x, y = self.get_position()
            return pygame.Rect(x - self.size, y - self.size, self.size * 2, self.size * 2)
    
    class PlayerCursor:
        def __init__(self, player_id="tristan"):
            self.player_id = player_id
            self.speed = 12
            if player_id == "tristan":
                self.home_x = WIDTH // 2 - 200
                self.home_y = HEIGHT - 150
                self.color = (255, 200, 100)
            else:
                self.home_x = WIDTH // 2 + 200
                self.home_y = HEIGHT - 150
                self.color = (100, 180, 255)
            self.x = self.home_x
            self.y = self.home_y
            self.fire_cooldown = 0
            self.fire_rate = 300
            self.charge_timer = 0  # For charged shots (future feature)
        
        def update(self, keys, dt):
            if self.player_id == "tristan":
                if keys[K_LEFT]: self.x -= self.speed
                if keys[K_RIGHT]: self.x += self.speed
                if keys[K_UP]: self.y -= self.speed
                if keys[K_DOWN]: self.y += self.speed
            else:
                if keys[K_a]: self.x -= self.speed
                if keys[K_d]: self.x += self.speed
                if keys[K_w]: self.y -= self.speed
                if keys[K_s]: self.y += self.speed
            self.x = max(50, min(WIDTH - 50, self.x))
            self.y = max(50, min(HEIGHT - 50, self.y))
            self.fire_cooldown = max(0, self.fire_cooldown - dt)
        
        def can_fire(self):
            return self.fire_cooldown <= 0
        
        def fire(self, target_x, target_y):
            if self.can_fire():
                self.fire_cooldown = self.fire_rate
                return Projectile(self.home_x, self.home_y, target_x, target_y, self.player_id)
            return None
        
        def draw(self, surf):
            # Targeting reticle with animation
            pulse = math.sin(pygame.time.get_ticks() * 0.005) * 3
            # Outer circle
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), int(20 + pulse), 3)
            # Crosshairs
            pygame.draw.line(surf, self.color, (self.x - 30, self.y), (self.x - 10, self.y), 2)
            pygame.draw.line(surf, self.color, (self.x + 10, self.y), (self.x + 30, self.y), 2)
            pygame.draw.line(surf, self.color, (self.x, self.y - 30), (self.x, self.y - 10), 2)
            pygame.draw.line(surf, self.color, (self.x, self.y + 10), (self.x, self.y + 30), 2)
            # Center dot
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), 4)
            # Home base with glow
            glow_surf = pygame.Surface((70, 70), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*self.color[:3], 50), (35, 35), 35)
            surf.blit(glow_surf, (int(self.home_x) - 35, int(self.home_y) - 35))
            pygame.draw.circle(surf, self.color, (int(self.home_x), int(self.home_y)), 25)
            pygame.draw.circle(surf, (255, 255, 255), (int(self.home_x), int(self.home_y)), 18)

    class ImpactParticle:
        """Simple particle for hit effects in Vine Blaster."""
        def __init__(self, x, y, color):
            self.x, self.y = x, y
            angle = random.random() * math.pi * 2
            speed = random.uniform(2, 6)
            self.vx = math.cos(angle) * speed
            self.vy = math.sin(angle) * speed
            self.color = color
            self.size = random.uniform(3, 8)
            self.lifetime = random.randint(200, 400)
            self.max_lifetime = self.lifetime
            self.alive = True
        
        def update(self, dt):
            self.x += self.vx
            self.y += self.vy
            self.vy += 0.1  # Gravity
            self.lifetime -= dt
            if self.lifetime <= 0:
                self.alive = False
        
        def draw(self, surf):
            if not self.alive:
                return
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            size = self.size * (self.lifetime / self.max_lifetime)
            if size < 1:
                return
            particle_surf = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
            color_with_alpha = (*self.color[:3], alpha)
            pygame.draw.circle(particle_surf, color_with_alpha, 
                             (int(size + 2), int(size + 2)), int(size))
            surf.blit(particle_surf, (int(self.x - size - 2), int(self.y - size - 2)))

    def spawn_impact(x, y, color, count=8):
        """Spawn impact particles."""
        return [ImpactParticle(x, y, color) for _ in range(count)]


####################################################################################################################
# Valley Climbing Minigame
####################################################################################################################

init python in valley_climb:
    import pygame
    import random
    import math
    from pygame.locals import *

    WIDTH, HEIGHT = 1920, 1080

    def img(path):
        return renpy.display.im.Image(path).load()

    bg_raw = img("images/bg/metaltreebark.png")
    TARGET_BG_WIDTH = WIDTH - 400
    scale = TARGET_BG_WIDTH / bg_raw.get_width()
    TARGET_BG_HEIGHT = int(bg_raw.get_height() * scale)
    bg = pygame.transform.smoothscale(bg_raw, (TARGET_BG_WIDTH, TARGET_BG_HEIGHT))

    bg2_raw = img("images/bg/bg_forest_parallax.png")
    scale2 = 1920 / bg2_raw.get_width()
    TARGET_BG_HEIGHT_2 = int(bg2_raw.get_height() * scale2)
    bg2 = pygame.transform.smoothscale(bg2_raw, (1920, TARGET_BG_HEIGHT_2))

    t_climb_up_down = [
        pygame.transform.smoothscale(
            img(f"images/characters/Tristan/rmbg/climbing/vertical/{i}.png"),
            (img(f"images/characters/Tristan/rmbg/climbing/vertical/{i}.png").get_width() // 4,
            img(f"images/characters/Tristan/rmbg/climbing/vertical/{i}.png").get_height() // 4)
        ) for i in range(1, 16)
    ] + [
        pygame.transform.smoothscale(
            img(f"images/characters/Tristan/rmbg/climbing/vertical/{i}.png"),
            (img(f"images/characters/Tristan/rmbg/climbing/vertical/{i}.png").get_width() // 4,
            img(f"images/characters/Tristan/rmbg/climbing/vertical/{i}.png").get_height() // 4)
        ) for i in range(15, 0, -1)
    ]

    t_climb_side = [
        pygame.transform.smoothscale(
            img(f"images/characters/Tristan/rmbg/climbing/horizontal/{i}.png"),
            (img(f"images/characters/Tristan/rmbg/climbing/horizontal/{i}.png").get_width() // 5,
            img(f"images/characters/Tristan/rmbg/climbing/horizontal/{i}.png").get_height() // 5)
        ) for i in range(1, 31)
    ]

    # Tristan attack animation (8 frames, 180 degree swing)
    t_attack = [
        pygame.transform.smoothscale(
            img(f"images/characters/Tristan/rmbg/climbing/attack/{i}.png"),
            (img(f"images/characters/Tristan/rmbg/climbing/attack/{i}.png").get_width() // 2,
            img(f"images/characters/Tristan/rmbg/climbing/attack/{i}.png").get_height() // 2)
        ) for i in range(1, 9)
    ]

    player_fall = img("images/characters/Tristan/rmbg/climbing/vertical/1.png")

    try:
        h_climb_up_down = [
            pygame.transform.smoothscale(
                img(f"images/characters/Henry/rmbg/climbing/vertical/{i}.png"),
                (img(f"images/characters/Henry/rmbg/climbing/vertical/{i}.png").get_width() // 4,
                img(f"images/characters/Henry/rmbg/climbing/vertical/{i}.png").get_height() // 4)
            ) for i in range(1, 16)
        ] + [
            pygame.transform.smoothscale(
                img(f"images/characters/Henry/rmbg/climbing/vertical/{i}.png"),
                (img(f"images/characters/Henry/rmbg/climbing/vertical/{i}.png").get_width() // 4,
                img(f"images/characters/Henry/rmbg/climbing/vertical/{i}.png").get_height() // 4)
            ) for i in range(15, 0, -1)
        ]
        h_climb_side = [
            pygame.transform.smoothscale(
                img(f"images/characters/Henry/rmbg/climbing/horizontal/{i}.png"),
                (img(f"images/characters/Henry/rmbg/climbing/horizontal/{i}.png").get_width() // 5,
                img(f"images/characters/Henry/rmbg/climbing/horizontal/{i}.png").get_height() // 5)
            ) for i in range(1, 31)
        ]
    except:
        h_climb_up_down = t_climb_up_down
        h_climb_side = t_climb_side

    HEART_SIZE = 48
    def load_heart_image(path, fallback_color):
        try:
            raw = img(path)
            return pygame.transform.smoothscale(raw, (HEART_SIZE, HEART_SIZE))
        except:
            surf = pygame.Surface((HEART_SIZE, HEART_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(surf, fallback_color, (HEART_SIZE//3, HEART_SIZE//3), HEART_SIZE//4)
            pygame.draw.circle(surf, fallback_color, (2*HEART_SIZE//3, HEART_SIZE//3), HEART_SIZE//4)
            pygame.draw.polygon(surf, fallback_color, [(HEART_SIZE//8, HEART_SIZE//3), (HEART_SIZE//2, HEART_SIZE - 4), (7*HEART_SIZE//8, HEART_SIZE//3)])
            return surf
    
    heart_full = load_heart_image("images/ui/heart_full.png", (255, 60, 90))
    heart_half = load_heart_image("images/ui/heart_half.png", (255, 150, 170))
    heart_empty = load_heart_image("images/ui/heart_empty.png", (80, 80, 80))
    
    try:
        pickup_heart_img = pygame.transform.smoothscale(img("images/ui/heart_pickup.png"), (40, 40))
    except:
        pickup_heart_img = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(pickup_heart_img, (255, 100, 150), (20, 20), 18)

    SPIDER_SCALE = 2
    spider_walk_up = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(1, 6)]
    spider_walk_down = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(21, 26)]
    spider_walk_left = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(7, 12)]
    spider_walk_right = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(27, 32)]
    spider_attack_left = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(17, 20)]
    spider_attack_up = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(13, 16)]
    spider_attack_down = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(33, 36)]
    spider_attack_right = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(37, 40)]
    spider_death_animation = [pygame.transform.smoothscale(img(f"images/enemies/spiders/images/{i}.png"),
        (int(img(f"images/enemies/spiders/images/{i}.png").get_width() * SPIDER_SCALE),
        int(img(f"images/enemies/spiders/images/{i}.png").get_height() * SPIDER_SCALE))) for i in range(41, 45)]
    
    
    class HealthPickup:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.collected = False
            self.bob_offset = 0
            self.bob_timer = 0
            self.glow_timer = 0
        def update(self):
            self.bob_timer += 1
            self.bob_offset = math.sin(self.bob_timer * 0.1) * 5
            self.glow_timer += 1
        def draw(self, surf, camera_y):
            if not self.collected:
                screen_y = self.y + camera_y + self.bob_offset
                # Glow effect
                glow_alpha = int(80 + math.sin(self.glow_timer * 0.1) * 40)
                glow_surf = pygame.Surface((60, 60), pygame.SRCALPHA)
                pygame.draw.circle(glow_surf, (255, 100, 150, glow_alpha), (30, 30), 25)
                surf.blit(glow_surf, (int(self.x) - 10, int(screen_y) - 10))
                surf.blit(pickup_heart_img, (int(self.x), int(screen_y)))
        def rect(self):
            return pygame.Rect(self.x, self.y, 40, 40)

    class Particle:
        """Visual particle for effects like hits, deaths, pickups."""
        def __init__(self, x, y, vx, vy, color, size=5, lifetime=500, gravity=0, shrink=True):
            self.x, self.y = x, y
            self.vx, self.vy = vx, vy
            self.color = color
            self.size = size
            self.max_size = size
            self.lifetime = lifetime
            self.max_lifetime = lifetime
            self.gravity = gravity
            self.shrink = shrink
            self.alive = True
        
        def update(self, dt):
            self.x += self.vx * (dt / 16)
            self.y += self.vy * (dt / 16)
            self.vy += self.gravity * (dt / 16)
            self.lifetime -= dt
            if self.lifetime <= 0:
                self.alive = False
            if self.shrink:
                self.size = self.max_size * (self.lifetime / self.max_lifetime)
        
        def draw(self, surf):
            if not self.alive or self.size < 1:
                return
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            particle_surf = pygame.Surface((int(self.size * 2 + 4), int(self.size * 2 + 4)), pygame.SRCALPHA)
            color_with_alpha = (*self.color[:3], alpha)
            pygame.draw.circle(particle_surf, color_with_alpha, 
                             (int(self.size + 2), int(self.size + 2)), int(self.size))
            surf.blit(particle_surf, (int(self.x - self.size - 2), int(self.y - self.size - 2)))

    def spawn_hit_particles(x, y, color=(255, 200, 100), count=8):
        """Create particles radiating from a hit point."""
        particles = []
        for _ in range(count):
            angle = random.random() * math.pi * 2
            speed = random.uniform(2, 6)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            size = random.uniform(3, 8)
            lifetime = random.randint(200, 400)
            particles.append(Particle(x, y, vx, vy, color, size, lifetime, gravity=0.1))
        return particles

    def spawn_death_particles(x, y, count=15):
        """Create particles for enemy death."""
        particles = []
        for _ in range(count):
            angle = random.random() * math.pi * 2
            speed = random.uniform(3, 8)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed - 2  # Slight upward bias
            # Mix of purple and green for spider death
            color = random.choice([(100, 60, 120), (60, 100, 80), (80, 50, 100)])
            size = random.uniform(4, 10)
            lifetime = random.randint(300, 600)
            particles.append(Particle(x, y, vx, vy, color, size, lifetime, gravity=0.15))
        return particles

    def spawn_heal_particles(x, y, count=10):
        """Create particles for healing effect."""
        particles = []
        for _ in range(count):
            angle = random.random() * math.pi * 2
            speed = random.uniform(1, 3)
            vx = math.cos(angle) * speed
            vy = -random.uniform(1, 4)  # Float upward
            color = random.choice([(255, 150, 180), (255, 200, 220), (255, 100, 150)])
            size = random.uniform(3, 6)
            lifetime = random.randint(400, 700)
            particles.append(Particle(x, y, vx, vy, color, size, lifetime, gravity=-0.05, shrink=True))
        return particles

    class ScreenShake:
        """Screen shake effect for impacts."""
        def __init__(self):
            self.shake_amount = 0
            self.shake_timer = 0
            self.decay = 0.9
        
        def trigger(self, amount=10, duration=200):
            self.shake_amount = max(self.shake_amount, amount)
            self.shake_timer = duration
        
        def update(self, dt):
            if self.shake_timer > 0:
                self.shake_timer -= dt
                if self.shake_timer <= 0:
                    self.shake_amount = 0
                else:
                    self.shake_amount *= self.decay
        
        def get_offset(self):
            if self.shake_amount < 0.5:
                return (0, 0)
            return (
                random.uniform(-self.shake_amount, self.shake_amount),
                random.uniform(-self.shake_amount, self.shake_amount)
            )

    class ComboTracker:
        """Track kill combos for bonus points."""
        def __init__(self):
            self.combo = 0
            self.combo_timer = 0
            self.combo_timeout = 2000  # ms to keep combo alive
            self.max_combo = 0
            self.display_combo = 0  # For display animation
            self.display_timer = 0
        
        def add_kill(self):
            self.combo += 1
            self.combo_timer = self.combo_timeout
            self.display_combo = self.combo
            self.display_timer = 1000
            self.max_combo = max(self.max_combo, self.combo)
            return self.get_multiplier()
        
        def update(self, dt):
            if self.combo_timer > 0:
                self.combo_timer -= dt
                if self.combo_timer <= 0:
                    self.combo = 0
            if self.display_timer > 0:
                self.display_timer -= dt
        
        def get_multiplier(self):
            if self.combo >= 10:
                return 3.0
            elif self.combo >= 5:
                return 2.0
            elif self.combo >= 3:
                return 1.5
            return 1.0
        
        def draw(self, surf, x, y):
            if self.display_timer > 0 and self.display_combo >= 2:
                alpha = min(255, int(255 * (self.display_timer / 500)))
                scale = 1.0 + (self.display_timer / 1000) * 0.3
                
                # Combo text
                combo_text = f"{self.display_combo}x COMBO!"
                if self.display_combo >= 10:
                    color = (255, 215, 0)  # Gold
                    combo_text = f"{self.display_combo}x ULTRA COMBO!"
                elif self.display_combo >= 5:
                    color = (255, 100, 100)  # Red
                    combo_text = f"{self.display_combo}x SUPER COMBO!"
                else:
                    color = (255, 200, 100)  # Orange
                
                # Create text surface (using pygame primitives since we can't use fonts easily)
                # Just draw colored rectangles as placeholder for combo indicator
                combo_surf = pygame.Surface((200, 40), pygame.SRCALPHA)
                combo_surf.fill((*color[:3], int(alpha * 0.7)))
                pygame.draw.rect(combo_surf, (*color[:3], alpha), (0, 0, 200, 40), 3)
                surf.blit(combo_surf, (x - 100, y - 20))

    class Player:
        def __init__(self):
            self.reset()
        def reset(self):
            self.x, self.y = WIDTH // 2, HEIGHT - 400
            self.falling = False
            self.run_count = 0
            self.facing_left = False
            self.speed = 6
            self.max_hp = 10
            self.hp = self.max_hp
            self.invincible = False
            self.invincible_timer = 0
            self.invincible_duration = 1500
            self.flash_timer = 0
            self.visible = True
            self.attacking = False
            self.attack_timer = 0
            self.attack_duration = 350
            self.attack_cooldown = 0
            self.attack_cooldown_max = 600
            self.attack_radius = 180
            self.attack_damage = 1
            self.attack_angle = 0
            self.attack_facing_left = False
        def take_damage(self, amount):
            if self.invincible or self.falling:
                return False
            self.hp -= amount
            if self.hp <= 0:
                self.hp = 0
                self.falling = True
            else:
                self.invincible = True
                self.invincible_timer = 0
            return True
        def heal(self, amount):
            self.hp = min(self.max_hp, self.hp + amount)
        def update_invincibility(self, dt):
            if self.invincible:
                self.invincible_timer += dt
                self.flash_timer += dt
                if self.flash_timer >= 100:
                    self.visible = not self.visible
                    self.flash_timer = 0
                if self.invincible_timer >= self.invincible_duration:
                    self.invincible = False
                    self.visible = True
            else:
                self.visible = True
        def start_attack(self, spiders, camera_y=0):
            if self.attack_cooldown <= 0 and not self.attacking and not self.falling:
                self.attacking = True
                self.attack_timer = 0
                self.attack_angle = 0
                attack_cx = self.x + 112
                attack_cy = (self.y - camera_y) + 130
                closest_spider = None
                closest_dist = float('inf')
                for spider in spiders:
                    if spider.dead:
                        continue
                    spider_screen_y = spider.y + camera_y
                    dist = math.hypot(spider.x - attack_cx, spider_screen_y - attack_cy)
                    if dist < closest_dist:
                        closest_dist = dist
                        closest_spider = spider
                if closest_spider:
                    self.attack_facing_left = closest_spider.x < attack_cx
                else:
                    self.attack_facing_left = not self.facing_left
                return True
            return False
        def update_attack(self, dt):
            if self.attack_cooldown > 0:
                self.attack_cooldown -= dt
            if self.attacking:
                self.attack_timer += dt
                self.attack_angle = (self.attack_timer / self.attack_duration) * 180
                if self.attack_timer >= self.attack_duration:
                    self.attacking = False
                    self.attack_cooldown = self.attack_cooldown_max
        def get_attack_center(self):
            return (self.x + 112, self.y + 130)
        def is_in_attack_range(self, target_x, target_y):
            if not self.attacking:
                return False
            cx, cy = self.get_attack_center()
            dist = math.hypot(target_x - cx, target_y - cy)
            if dist > self.attack_radius:
                return False
            if self.attack_facing_left:
                return target_x <= cx + 30
            else:
                return target_x >= cx - 30
        def get_attack_frame(self):
            if not self.attacking:
                return 0
            progress = self.attack_timer / self.attack_duration
            frame = int(progress * len(t_attack))
            return min(frame, len(t_attack) - 1)
        def update(self, keys):
            if self.falling:
                return
            moving = False
            if keys[K_LEFT]:
                self.x -= self.speed
                self.facing_left = False
                moving = True
            if keys[K_RIGHT]:
                self.x += self.speed
                self.facing_left = True
                moving = True
            if keys[K_UP]:
                self.y -= self.speed
                moving = True
            if keys[K_DOWN]:
                self.y += self.speed
                moving = True
            self.run_count = self.run_count + 1 if moving else 0
            self.x = max(225, min(self.x, 1695 - self.rect().width))
            self.y = max(-20000, min(self.y, 200000))
        def draw(self, surf, camera_y):
            if not self.visible:
                return
            keys = pygame.key.get_pressed()
            if self.attacking:
                frame = self.get_attack_frame()
                image = t_attack[frame]
                if self.attack_facing_left:
                    image = pygame.transform.flip(image, True, False)
                offset_x = -200
                offset_y = -180
                if self.attack_facing_left:
                    offset_x = -150
                surf.blit(image, (int(self.x + offset_x), int(self.y - camera_y + offset_y)))
            elif self.falling:
                image = player_fall
                surf.blit(image, (int(self.x), int(self.y - camera_y)))
            else:
                frame = self.run_count
                if keys[K_LEFT] or keys[K_RIGHT]:
                    image = t_climb_side[frame % len(t_climb_side)]
                else:
                    image = t_climb_up_down[frame % len(t_climb_up_down)]
                if self.facing_left:
                    image = pygame.transform.flip(image, True, False)
                surf.blit(image, (int(self.x), int(self.y - camera_y)))
        def rect(self):
            return pygame.Rect(self.x + 70, self.y + 50, 85, 190)

    class Henry:
        def __init__(self):
            self.reset()
        def reset(self):
            self.x, self.y = WIDTH // 2 - 80, HEIGHT - 350
            self.run_count = 0
            self.facing_left = False
            self.speed = 5.5
            self.follow_delay_positions = []
            self.max_stored_positions = 15
            self.attacking = False
            self.attack_timer = 0
            self.attack_duration = 350
            self.attack_cooldown = 0
            self.attack_cooldown_max = 1000
            self.attack_radius = 150
            self.attack_damage = 1
            self.attack_angle = 0
            self.attack_facing_left = False
            self.min_distance = 80
        def update(self, player, spiders, dt, camera_y=0):
            self.follow_delay_positions.append((player.x - 160, player.y + 130))
            if len(self.follow_delay_positions) > self.max_stored_positions:
                self.follow_delay_positions.pop(0)
            if self.follow_delay_positions:
                target_x, target_y = self.follow_delay_positions[0]
                dx, dy = target_x - self.x, target_y - self.y
                dist = math.hypot(dx, dy)
                if dist > 150:
                    self.x += (dx / dist) * self.speed
                    self.y += (dy / dist) * self.speed
                    self.run_count += 1
                    self.facing_left = dx > 0
                else:
                    self.run_count = 0
            player_dx = self.x - player.x
            player_dy = self.y - player.y
            player_dist = math.hypot(player_dx, player_dy)
            if player_dist < self.min_distance:
                if player_dist > 0:
                    self.x = player.x + (player_dx / player_dist) * self.min_distance
                    self.y = player.y + (player_dy / player_dist) * self.min_distance
                else:
                    self.x = player.x - self.min_distance
            self.attack_cooldown = max(0, self.attack_cooldown - dt)
            if not self.attacking and self.attack_cooldown <= 0:
                henry_attack_cx = self.x + 112
                henry_attack_cy = (self.y - camera_y) + 130
                closest_dist = self.attack_radius + 50
                closest_spider = None
                for spider in spiders:
                    if spider.dead:
                        continue
                    spider_screen_y = spider.y + camera_y
                    dist = math.hypot(spider.x - henry_attack_cx, spider_screen_y - henry_attack_cy)
                    if dist < closest_dist:
                        closest_dist = dist
                        closest_spider = spider
                if closest_spider and closest_dist <= self.attack_radius + 30:
                    self.attacking = True
                    self.attack_timer = 0
                    self.attack_angle = 0
                    self.attack_facing_left = closest_spider.x < self.x
            if self.attacking:
                self.attack_timer += dt
                self.attack_angle = (self.attack_timer / self.attack_duration) * 180
                if self.attack_timer >= self.attack_duration:
                    self.attacking = False
                    self.attack_cooldown = self.attack_cooldown_max
        def get_attack_center(self):
            return (self.x + 112, self.y + 130)
        def is_in_attack_range(self, target_x, target_y):
            if not self.attacking:
                return False
            cx, cy = self.get_attack_center()
            dist = math.hypot(target_x - cx, target_y - cy)
            if dist > self.attack_radius:
                return False
            if self.attack_facing_left:
                return target_x <= cx + 30
            else:
                return target_x >= cx - 30
        def get_attack_frame(self):
            if not self.attacking:
                return 0
            progress = self.attack_timer / self.attack_duration
            frame = int(progress * len(t_attack))
            return min(frame, len(t_attack) - 1)
        def draw(self, surf, camera_y):
            frame = self.run_count
            if self.attacking:
                attack_frame = self.get_attack_frame()
                image = t_attack[attack_frame]
                offset_x = -200
                offset_y = -180
                if self.attack_facing_left:
                    image = pygame.transform.flip(image, True, False)
                    offset_x = -150
                surf.blit(image, (int(self.x + offset_x), int(self.y - camera_y + offset_y)))
            else:
                image = h_climb_up_down[frame % len(h_climb_up_down)]
                if self.facing_left:
                    image = pygame.transform.flip(image, True, False)
                surf.blit(image, (int(self.x), int(self.y - camera_y)))

    SPIDER_IDLE, SPIDER_WANDER, SPIDER_PURSUE, SPIDER_DEAD, SPIDER_ATTACK = 0, 1, 2, 3, 4
    
    class Spider:
        def __init__(self, x, y, detection_radius=200):
            self.x, self.y = x, y
            self.detection_radius = detection_radius
            self.speed = 7
            self.wander_speed = 1
            self.state = SPIDER_IDLE
            self.state_timer = 0
            self.wander_target_x, self.wander_target_y = x, y
            self.wander_pause_time = random.randint(1000, 3000)
            self.wander_move_time = random.randint(500, 2000)
            self.is_paused = True
            self.anim_frame = 0
            self.anim_timer = 0
            self.facing = 3
            self.idle_frame = 0
            self.facing_cooldown = 300
            self.damage = 2
            self.hp = 2
            self.dead = False
            self.death_timer = 0
            self.death_frame = 0
            self.hit_cooldown = 0
            self.hit_this_attack = False
            self.hit_by_henry = False
            self.attack_timer = 0
            self.attack_frame = 0
            self.hit_flash_timer = 0
            self.hit_flash_duration = 150
            self.fall_velocity = 0
            self.fall_acceleration = 0.5
        def update(self, player=None, dt=16, camera_y=0):
            if self.hit_flash_timer > 0:
                self.hit_flash_timer = max(0, self.hit_flash_timer - dt)
            if self.dead:
                self.death_timer += dt
                self.anim_timer += dt
                if self.anim_timer > 150:
                    self.death_frame = min(self.death_frame + 1, len(spider_death_animation) - 1)
                    self.anim_timer = 0
                self.fall_velocity += self.fall_acceleration
                self.y += self.fall_velocity
                return
            self.state_timer += dt
            self.hit_cooldown = max(0, self.hit_cooldown - dt)
            self._camera_y = camera_y
            if player and not player.falling:
                spider_screen_y = self.y + camera_y
                player_hitbox_x = player.x + 112
                player_hitbox_screen_y = (player.y - camera_y) + 145
                dist = math.hypot(self.x - player_hitbox_x, spider_screen_y - player_hitbox_screen_y)
                if dist < self.detection_radius:
                    self.state = SPIDER_PURSUE
                elif self.state == SPIDER_PURSUE and dist > self.detection_radius * 1.5:
                    self.state = SPIDER_WANDER
                    self.is_paused = True
                    self.state_timer = 0
            if self.state == SPIDER_IDLE:
                if self.state_timer > 2000:
                    self.state = SPIDER_WANDER
                    self.state_timer = 0
                    self._pick_wander_target()
            elif self.state == SPIDER_WANDER:
                self._do_wander(dt)
            elif self.state == SPIDER_PURSUE:
                self._do_pursue(player, dt)
            is_moving = (self.state == SPIDER_PURSUE or (self.state == SPIDER_WANDER and not self.is_paused))
            if is_moving:
                self.anim_timer += dt
                if self.anim_timer > 80:
                    self.anim_frame = (self.anim_frame + 1) % 5
                    self.anim_timer = 0
        def _pick_wander_target(self):
            self.wander_target_x = max(250, min(1650, self.x + random.randint(-150, 150)))
            self.wander_target_y = self.y + random.randint(-150, 150)
            self.is_paused = False
            self.wander_move_time = random.randint(500, 2000)
            self.state_timer = 0
        def _do_wander(self, dt):
            if self.is_paused:
                if self.state_timer > self.wander_pause_time:
                    self._pick_wander_target()
            else:
                dx, dy = self.wander_target_x - self.x, self.wander_target_y - self.y
                dist = math.hypot(dx, dy)
                if dist > 1:
                    self.x += (dx / dist) * self.wander_speed
                    self.y += (dy / dist) * self.wander_speed
                    self._update_facing(dx, dy)
                if self.state_timer > self.wander_move_time or dist <= 5:
                    self.is_paused = True
                    self.wander_pause_time = random.randint(1000, 3000)
                    self.state_timer = 0
        def _do_pursue(self, player, dt):
            if not player:
                return
            target_x = player.x + 112
            dx = target_x - self.x
            camera_y = getattr(self, '_camera_y', 0)
            target_y = player.y - 2 * camera_y + 145
            dy = target_y - self.y
            dist = math.hypot(dx, dy)
            if dist > 10:
                self.x += (dx / dist) * self.speed
                self.y += (dy / dist) * self.speed
                self._update_facing(dx, dy)
        def _update_facing(self, dx, dy):
            abs_dx, abs_dy = abs(dx), abs(dy)
            if abs_dx < 1.0 and abs_dy < 1.0:
                return
            self.facing_cooldown = max(0, self.facing_cooldown - 16)
            if self.facing_cooldown > 0:
                return
            new_facing = None
            if abs_dx > abs_dy * 4:
                new_facing = 0 if dx < 0 else 1
            elif abs_dy > abs_dx * 4:
                new_facing = 2 if dy < 0 else 3
            if new_facing is not None and new_facing != self.facing:
                self.facing = new_facing
                self.facing_cooldown = 400
        def take_damage(self, amount=1):
            self.hp -= amount
            self.hit_flash_timer = self.hit_flash_duration
            if self.hp <= 0:
                self.dead = True
                self.state = SPIDER_DEAD
                self.death_frame = 0
                self.anim_timer = 0
                self.fall_velocity = 2
                return True
            return False
        def can_hit_player(self):
            return self.hit_cooldown <= 0 and not self.dead
        def did_hit_player(self):
            self.hit_cooldown = 1000
        def draw(self, surf, camera_y):
            screen_y = self.y + camera_y
            if self.dead:
                if self.death_timer > 1500:
                    return
                sprite = spider_death_animation[min(self.death_frame, len(spider_death_animation) - 1)]
                sprite = sprite.copy()
                alpha = max(0, 255 - int((self.death_timer / 1500) * 255))
                sprite.set_alpha(alpha)
                surf.blit(sprite, (int(self.x - sprite.get_width() // 2), int(screen_y - sprite.get_height() // 2)))
                return
            sprites = [spider_walk_left, spider_walk_right, spider_walk_up, spider_walk_down][min(self.facing, 3)]
            frame = self.anim_frame % len(sprites)
            sprite = sprites[frame]
            if self.hit_flash_timer > 0:
                sprite = sprite.copy()
                white_surface = pygame.Surface(sprite.get_size(), pygame.SRCALPHA)
                white_surface.fill((255, 255, 255, 200))
                sprite.blit(white_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
                draw_x = int(self.x - sprite.get_width() // 2)
                draw_y = int(screen_y - sprite.get_height() // 2)
                glow_surf = pygame.Surface((sprite.get_width() + 8, sprite.get_height() + 8), pygame.SRCALPHA)
                glow_surf.fill((255, 100, 100, 150))
                surf.blit(glow_surf, (draw_x - 4, draw_y - 4))
                surf.blit(sprite, (draw_x, draw_y))
            else:
                surf.blit(sprite, (int(self.x - sprite.get_width() // 2), int(screen_y - sprite.get_height() // 2)))
        def rect(self):
            return pygame.Rect(self.x - 30, self.y - 30, 60, 60)
        def is_dead_and_gone(self):
            return self.dead and self.death_timer > 1500

    # Ambush Vine state constants
    VINE_HIDDEN, VINE_WARNING, VINE_ATTACKING, VINE_RETRACTING, VINE_COOLDOWN = 0, 1, 2, 3, 4
    
    class AmbushVine:
        """Hidden plant enemy that lunges at player when they get close."""
        def __init__(self, x, y, direction="left"):
            self.x, self.y = x, y
            self.direction = direction
            self.state = VINE_HIDDEN
            self.state_timer = 0
            self.detection_radius = 180
            self.attack_range = 250
            self.current_extension = 0
            self.attack_speed = 18
            self.retract_speed = 10
            self.warning_duration = 400
            self.hold_duration = 200
            self.cooldown_duration = 2500
            self.damage = 1
            self.hp = 2
            self.dead = False
            self.hit_player = False
            self.anim_timer = 0
            self.wiggle_offset = random.random() * math.pi * 2
            self.base_color = (60, 100, 40)
            self.attack_color = (100, 160, 60)
            self.hit_flash_timer = 0
            self.hit_flash_duration = 150
        
        def update(self, player, dt, camera_y=0):
            if self.dead:
                return
            self.state_timer += dt
            self.anim_timer += dt
            if self.hit_flash_timer > 0:
                self.hit_flash_timer = max(0, self.hit_flash_timer - dt)
            vine_screen_y = self.y + camera_y
            player_screen_y = player.y - camera_y
            player_center_x = player.x + 112
            player_center_y = player_screen_y + 145
            dist_to_player = math.hypot(self.x - player_center_x, vine_screen_y - player_center_y)
            if self.state == VINE_HIDDEN:
                if dist_to_player < self.detection_radius and not player.falling:
                    self.state = VINE_WARNING
                    self.state_timer = 0
            elif self.state == VINE_WARNING:
                if self.state_timer >= self.warning_duration:
                    self.state = VINE_ATTACKING
                    self.state_timer = 0
                    self.hit_player = False
            elif self.state == VINE_ATTACKING:
                self.current_extension += self.attack_speed
                if self.current_extension >= self.attack_range:
                    self.current_extension = self.attack_range
                    if self.state_timer >= self.hold_duration:
                        self.state = VINE_RETRACTING
                        self.state_timer = 0
            elif self.state == VINE_RETRACTING:
                self.current_extension -= self.retract_speed
                if self.current_extension <= 0:
                    self.current_extension = 0
                    self.state = VINE_COOLDOWN
                    self.state_timer = 0
            elif self.state == VINE_COOLDOWN:
                if self.state_timer >= self.cooldown_duration:
                    self.state = VINE_HIDDEN
                    self.state_timer = 0
        
        def get_tip_position(self, camera_y):
            screen_y = self.y + camera_y
            if self.direction == "left":
                tip_x = self.x + self.current_extension
            else:
                tip_x = self.x - self.current_extension
            return (tip_x, screen_y)
        
        def check_collision(self, player, camera_y):
            if self.dead or self.state != VINE_ATTACKING or self.hit_player:
                return False
            tip_x, tip_y = self.get_tip_position(camera_y)
            player_screen_y = player.y - camera_y
            tip_rect = pygame.Rect(tip_x - 25, tip_y - 25, 50, 50)
            player_rect = pygame.Rect(player.x + 70, player_screen_y + 50, 85, 190)
            if tip_rect.colliderect(player_rect):
                self.hit_player = True
                return True
            return False
        
        def take_damage(self, amount=1):
            self.hp -= amount
            self.hit_flash_timer = self.hit_flash_duration
            if self.hp <= 0:
                self.dead = True
                return True
            return False
        
        def draw(self, surf, camera_y, time_ms):
            if self.dead:
                return
            screen_y = self.y + camera_y
            if screen_y < -100 or screen_y > 1180:
                return
            alpha = 255
            if self.state == VINE_HIDDEN:
                alpha = 50
            elif self.state == VINE_WARNING:
                alpha = 100 + int(math.sin(time_ms * 0.02) * 50)
            elif self.state == VINE_COOLDOWN:
                alpha = 120
            num_points = max(3, int(self.current_extension / 25) + 2)
            points = [(self.x, screen_y)]
            for i in range(1, num_points):
                t = i / (num_points - 1) if num_points > 1 else 1
                if self.direction == "left":
                    px = self.x + self.current_extension * t
                else:
                    px = self.x - self.current_extension * t
                wiggle_amount = 12 if self.state == VINE_ATTACKING else 6
                wiggle = math.sin(time_ms * 0.015 + t * 6 + self.wiggle_offset) * wiggle_amount * (1 - t * 0.3)
                py = screen_y + wiggle
                points.append((int(px), int(py)))
            if len(points) >= 2 and (self.current_extension > 5 or self.state in [VINE_HIDDEN, VINE_WARNING, VINE_COOLDOWN]):
                if self.hit_flash_timer > 0:
                    color = (255, 200, 200)
                elif self.state == VINE_ATTACKING:
                    color = self.attack_color
                else:
                    color = self.base_color
                if self.current_extension > 5:
                    for i in range(len(points) - 1):
                        p1 = points[i]
                        p2 = points[i + 1]
                        thickness = max(4, int(14 - i * 1.5))
                        line_color = (*color, alpha)
                        line_surf = pygame.Surface((abs(p2[0] - p1[0]) + thickness * 2 + 20, abs(p2[1] - p1[1]) + thickness * 2 + 20), pygame.SRCALPHA)
                        offset_x = min(p1[0], p2[0]) - thickness - 10
                        offset_y = min(p1[1], p2[1]) - thickness - 10
                        pygame.draw.line(line_surf, line_color, 
                                        (p1[0] - offset_x, p1[1] - offset_y),
                                        (p2[0] - offset_x, p2[1] - offset_y), thickness)
                        surf.blit(line_surf, (offset_x, offset_y))
                    tip_x, tip_y = points[-1]
                    tip_size = 18 if self.state == VINE_ATTACKING else 12
                    tip_surf = pygame.Surface((tip_size * 2 + 10, tip_size * 2 + 10), pygame.SRCALPHA)
                    if self.hit_flash_timer > 0:
                        tip_color = (255, 150, 150, alpha)
                    elif self.state == VINE_ATTACKING:
                        tip_color = (220, 80, 80, alpha)
                    else:
                        tip_color = (180, 100, 80, alpha)
                    pygame.draw.circle(tip_surf, tip_color, (tip_size + 5, tip_size + 5), tip_size)
                    inner_color = (255, 120, 120, alpha)
                    pygame.draw.circle(tip_surf, inner_color, (tip_size + 5, tip_size + 5), tip_size - 5)
                    surf.blit(tip_surf, (tip_x - tip_size - 5, tip_y - tip_size - 5))
            base_size = 25
            base_surf = pygame.Surface((base_size * 2 + 10, base_size * 2 + 10), pygame.SRCALPHA)
            base_alpha = max(alpha, 80)
            base_color = (50, 90, 40, base_alpha)
            pygame.draw.circle(base_surf, base_color, (base_size + 5, base_size + 5), base_size)
            pygame.draw.circle(base_surf, (70, 110, 50, base_alpha), (base_size + 5, base_size + 5), base_size - 8)
            surf.blit(base_surf, (self.x - base_size - 5, screen_y - base_size - 5))
        
        def is_on_screen(self, camera_y, height):
            screen_y = self.y + camera_y
            return -150 < screen_y < height + 150


############################################################################
# Ren'Py Displayables
############################################################################

init python:
    class ValleyClimbDisplayable(renpy.Displayable):
        def __init__(self):
            super().__init__()
            import pygame
            self.__dict__["surface"] = pygame.Surface((1920,1080), pygame.SRCALPHA)
            self.clock = pygame.time.Clock()
            self.player = valley_climb.Player()
            self.henry = valley_climb.Henry()
            self.spiders = []
            self.ambush_vines = []
            self.health_pickups = []
            self.particles = []  # Visual particle effects
            self.pickup_spawn_timer = 0
            self.spider_spawn_timer = 0
            self.vine_spawn_timer = 0
            self.score = 0
            self.speed = 30
            self.speed_timer = 0
            self.done = False
            self.should_end = False
            self.camera_y = 0
            self.prev_camera_y = 0
            self.bg_y = self.bg_y2 = self.bg2_y = self.bg2_y2 = 0
            self.debug_mode = False
            self.time_ms = 0
            # New systems
            self.screen_shake = valley_climb.ScreenShake()
            self.combo_tracker = valley_climb.ComboTracker()

        def render(self, width, height, st, at):
            import pygame
            import math
            if self.done:
                return renpy.Render(1920, 1080)
            dt = self.clock.tick(60)
            self.time_ms += dt
            self.surface.fill((0, 0, 0, 0))

            self.speed_timer += dt
            if self.speed_timer > 500:
                self.speed += 0.5
                self.speed_timer = 0

            self.spider_spawn_timer += dt
            if self.spider_spawn_timer > 3000:
                spawn_y = -self.camera_y - random.randint(100, 400)
                self.spiders.append(valley_climb.Spider(
                    random.randint(300, 1600),
                    spawn_y,
                    detection_radius=random.randint(180, 250)))
                self.spider_spawn_timer = 0

            self.vine_spawn_timer += dt
            if self.vine_spawn_timer > 8000 and len(self.ambush_vines) < 5:
                spawn_y = -self.camera_y - random.randint(200, 600)
                if random.random() < 0.5:
                    vine_x = 260
                    direction = "left"
                else:
                    vine_x = 1660
                    direction = "right"
                self.ambush_vines.append(valley_climb.AmbushVine(vine_x, spawn_y, direction))
                self.vine_spawn_timer = 0

            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.player.update_invincibility(dt)
            self.player.update_attack(dt)

            self.prev_camera_y = self.camera_y

            player_screen_y = self.player.y - self.camera_y
            if player_screen_y < 400 and keys[pygame.K_UP]:
                self.camera_y += 6
            self.camera_y = max(0, self.camera_y)
            
            camera_scroll = self.camera_y - self.prev_camera_y
            
            player_screen_y = self.player.y - self.camera_y
            if player_screen_y < 400:
                self.player.y = self.camera_y + 400
            if player_screen_y > height - 100:
                self.player.y = self.camera_y + height - 100

            self.henry.update(self.player, self.spiders, dt, self.camera_y)

            for spider in self.spiders[:]:
                spider.update(player=self.player, dt=dt, camera_y=self.camera_y)
                
                if spider.is_dead_and_gone():
                    self.spiders.remove(spider)
                    self.score += 50
                    continue
                screen_y = spider.y + self.camera_y
                if screen_y > height + 300:
                    self.spiders.remove(spider)
                    continue
                if screen_y < -300:
                    self.spiders.remove(spider)
                    continue
                    
                if not spider.dead and self.player.attacking:
                    spider_screen_y = spider.y + self.camera_y
                    player_screen_y = self.player.y - self.camera_y
                    cx = self.player.x + 112
                    cy = player_screen_y + 130
                    dist = math.hypot(spider.x - cx, spider_screen_y - cy)
                    in_range = dist <= self.player.attack_radius
                    if self.player.attack_facing_left:
                        in_range = in_range and spider.x <= cx + 30
                    else:
                        in_range = in_range and spider.x >= cx - 30
                    if in_range and not spider.hit_this_attack:
                        was_alive = not spider.dead
                        spider.take_damage(self.player.attack_damage)
                        spider.hit_this_attack = True
                        # Spawn hit particles
                        self.particles.extend(valley_climb.spawn_hit_particles(
                            spider.x, spider_screen_y, (255, 200, 100)))
                        # Check if killed
                        if spider.dead and was_alive:
                            multiplier = self.combo_tracker.add_kill()
                            self.score += int(50 * multiplier)
                            self.particles.extend(valley_climb.spawn_death_particles(
                                spider.x, spider_screen_y))
                            self.screen_shake.trigger(8, 150)
                if not spider.dead and self.henry.attacking:
                    spider_screen_y = spider.y + self.camera_y
                    henry_screen_y = self.henry.y - self.camera_y
                    cx = self.henry.x + 112
                    cy = henry_screen_y + 130
                    dist = math.hypot(spider.x - cx, spider_screen_y - cy)
                    in_range = dist <= self.henry.attack_radius
                    if self.henry.attack_facing_left:
                        in_range = in_range and spider.x <= cx + 30
                    else:
                        in_range = in_range and spider.x >= cx - 30
                    if in_range and not spider.hit_by_henry:
                        was_alive = not spider.dead
                        spider.take_damage(self.henry.attack_damage)
                        spider.hit_by_henry = True
                        # Spawn hit particles
                        self.particles.extend(valley_climb.spawn_hit_particles(
                            spider.x, spider_screen_y, (100, 200, 255)))
                        # Check if killed
                        if spider.dead and was_alive:
                            multiplier = self.combo_tracker.add_kill()
                            self.score += int(50 * multiplier)
                            self.particles.extend(valley_climb.spawn_death_particles(
                                spider.x, spider_screen_y))
                            self.screen_shake.trigger(6, 120)
                if not self.player.attacking:
                    spider.hit_this_attack = False
                if not self.henry.attacking:
                    spider.hit_by_henry = False
                if not spider.dead and spider.can_hit_player():
                    spider_screen_y = spider.y + self.camera_y
                    player_screen_y = self.player.y - self.camera_y
                    spider_screen_rect = pygame.Rect(spider.x - 30, spider_screen_y - 30, 60, 60)
                    player_screen_rect = pygame.Rect(self.player.x + 70, player_screen_y + 50, 85, 190)
                    if spider_screen_rect.colliderect(player_screen_rect):
                        if self.player.take_damage(spider.damage):
                            spider.did_hit_player()
                            self.screen_shake.trigger(12, 200)  # Bigger shake when player hit

            for vine in self.ambush_vines[:]:
                vine.update(self.player, dt, self.camera_y)
                
                if vine.dead:
                    self.ambush_vines.remove(vine)
                    self.score += 30
                    continue
                if not vine.is_on_screen(self.camera_y, height):
                    vine_screen_y = vine.y + self.camera_y
                    if vine_screen_y > height + 200:
                        self.ambush_vines.remove(vine)
                        continue
                
                if vine.check_collision(self.player, self.camera_y):
                    self.player.take_damage(vine.damage)
                    self.screen_shake.trigger(10, 180)
                
                if self.player.attacking and not vine.dead:
                    tip_x, tip_y = vine.get_tip_position(self.camera_y)
                    player_screen_y = self.player.y - self.camera_y
                    cx = self.player.x + 112
                    cy = player_screen_y + 130
                    dist = math.hypot(tip_x - cx, tip_y - cy)
                    in_range = dist <= self.player.attack_radius
                    if self.player.attack_facing_left:
                        in_range = in_range and tip_x <= cx + 30
                    else:
                        in_range = in_range and tip_x >= cx - 30
                    if in_range:
                        was_alive = not vine.dead
                        vine.take_damage(self.player.attack_damage)
                        # Spawn green particles for vine hit
                        self.particles.extend(valley_climb.spawn_hit_particles(
                            tip_x, tip_y, (80, 180, 60), count=6))
                        if vine.dead and was_alive:
                            self.score += 30
                            self.screen_shake.trigger(5, 100)

            self.pickup_spawn_timer += dt
            if self.pickup_spawn_timer > 25000 and self.player.hp < self.player.max_hp and random.random() < 0.3:
                spawn_y = -self.camera_y - random.randint(100, 300)
                self.health_pickups.append(valley_climb.HealthPickup(
                    random.randint(300, 1600), 
                    spawn_y))
                self.pickup_spawn_timer = 0
            for pickup in self.health_pickups[:]:
                pickup.update()
                screen_y = pickup.y + self.camera_y
                if screen_y > height + 100:
                    self.health_pickups.remove(pickup)
                elif not pickup.collected:
                    player_screen_y = self.player.y - self.camera_y
                    pickup_rect = pygame.Rect(pickup.x, screen_y, 40, 40)
                    player_rect = pygame.Rect(self.player.x + 70, player_screen_y + 50, 85, 190)
                    if pickup_rect.colliderect(player_rect):
                        pickup.collected = True
                        self.player.heal(2)
                        # Spawn heal particles
                        self.particles.extend(valley_climb.spawn_heal_particles(
                            pickup.x + 20, screen_y + 20))
                        self.health_pickups.remove(pickup)

            # Update particle system
            for particle in self.particles[:]:
                particle.update(dt)
                if not particle.alive:
                    self.particles.remove(particle)
            
            # Update screen shake
            self.screen_shake.update(dt)
            shake_x, shake_y = self.screen_shake.get_offset()
            
            # Update combo tracker
            self.combo_tracker.update(dt)

            bg, bg2 = valley_climb.bg, valley_climb.bg2
            self.bg_y = self.camera_y % bg.get_height()
            self.bg_y2 = self.bg_y - bg.get_height()
            self.bg2_y = (self.camera_y * 0.05 + height - bg2.get_height()) % bg2.get_height()
            self.bg2_y2 = self.bg2_y - bg2.get_height()

            bg2_x = (width - bg2.get_width()) // 2
            self.surface.blit(bg2, (bg2_x + int(shake_x), int(self.bg2_y + shake_y)))
            self.surface.blit(bg2, (bg2_x + int(shake_x), int(self.bg2_y2 + shake_y)))
            bg_x = (width - bg.get_width()) // 2
            self.surface.blit(bg, (bg_x + int(shake_x), int(self.bg_y + shake_y)))
            self.surface.blit(bg, (bg_x + int(shake_x), int(self.bg_y2 + shake_y)))

            for vine in self.ambush_vines:
                vine.draw(self.surface, self.camera_y, self.time_ms)

            self.henry.draw(self.surface, self.camera_y)
            self.player.draw(self.surface, self.camera_y)
            for spider in self.spiders:
                spider.draw(self.surface, self.camera_y)
            for pickup in self.health_pickups:
                pickup.draw(self.surface, self.camera_y)
            
            # Draw particles on top
            for particle in self.particles:
                particle.draw(self.surface)
            
            # Draw combo indicator
            self.combo_tracker.draw(self.surface, width // 2, 100)

            if self.debug_mode:
                player_screen_y = self.player.y - self.camera_y
                henry_screen_y = self.henry.y - self.camera_y
                player_rect = pygame.Rect(self.player.x + 70, player_screen_y + 50, 85, 190)
                pygame.draw.rect(self.surface, (0, 255, 0), player_rect, 2)
                henry_rect = pygame.Rect(self.henry.x + 70, henry_screen_y + 50, 85, 190)
                pygame.draw.rect(self.surface, (0, 150, 255), henry_rect, 2)
                player_center_x = self.player.x + 112
                player_center_y = player_screen_y + 130
                pygame.draw.circle(self.surface, (0, 255, 255), 
                    (int(player_center_x), int(player_center_y)), 
                    self.henry.min_distance, 1)
                attack_cx = self.player.x + 112
                attack_cy = player_screen_y + 130
                pygame.draw.circle(self.surface, (255, 255, 0), 
                    (int(attack_cx), int(attack_cy)), 
                    self.player.attack_radius, 1)
                pygame.draw.circle(self.surface, (255, 255, 0), 
                    (int(attack_cx), int(attack_cy)), 5)
                if self.player.attacking:
                    r = self.player.attack_radius
                    if self.player.attack_facing_left:
                        for i in range(12):
                            angle1 = math.radians(90 + i * 15)
                            angle2 = math.radians(90 + (i + 1) * 15)
                            x1 = attack_cx + math.cos(angle1) * r
                            y1 = attack_cy + math.sin(angle1) * r
                            x2 = attack_cx + math.cos(angle2) * r
                            y2 = attack_cy + math.sin(angle2) * r
                            pygame.draw.line(self.surface, (255, 150, 0), (int(x1), int(y1)), (int(x2), int(y2)), 3)
                    else:
                        for i in range(12):
                            angle1 = math.radians(-90 + i * 15)
                            angle2 = math.radians(-90 + (i + 1) * 15)
                            x1 = attack_cx + math.cos(angle1) * r
                            y1 = attack_cy + math.sin(angle1) * r
                            x2 = attack_cx + math.cos(angle2) * r
                            y2 = attack_cy + math.sin(angle2) * r
                            pygame.draw.line(self.surface, (255, 150, 0), (int(x1), int(y1)), (int(x2), int(y2)), 3)
                henry_attack_cx = self.henry.x + 112
                henry_attack_cy = henry_screen_y + 130
                pygame.draw.circle(self.surface, (100, 200, 255), (int(henry_attack_cx), int(henry_attack_cy)), self.henry.attack_radius, 1)
                pygame.draw.circle(self.surface, (100, 200, 255), (int(henry_attack_cx), int(henry_attack_cy)), 5)
                if self.henry.attacking:
                    r = self.henry.attack_radius
                    if self.henry.attack_facing_left:
                        for i in range(12):
                            angle1 = math.radians(90 + i * 15)
                            angle2 = math.radians(90 + (i + 1) * 15)
                            x1 = henry_attack_cx + math.cos(angle1) * r
                            y1 = henry_attack_cy + math.sin(angle1) * r
                            x2 = henry_attack_cx + math.cos(angle2) * r
                            y2 = henry_attack_cy + math.sin(angle2) * r
                            pygame.draw.line(self.surface, (150, 200, 255), (int(x1), int(y1)), (int(x2), int(y2)), 3)
                    else:
                        for i in range(12):
                            angle1 = math.radians(-90 + i * 15)
                            angle2 = math.radians(-90 + (i + 1) * 15)
                            x1 = henry_attack_cx + math.cos(angle1) * r
                            y1 = henry_attack_cy + math.sin(angle1) * r
                            x2 = henry_attack_cx + math.cos(angle2) * r
                            y2 = henry_attack_cy + math.sin(angle2) * r
                            pygame.draw.line(self.surface, (150, 200, 255), (int(x1), int(y1)), (int(x2), int(y2)), 3)
                for spider in self.spiders:
                    if not spider.dead:
                        spider_screen_y = spider.y + self.camera_y
                        spider_rect = pygame.Rect(spider.x - 30, spider_screen_y - 30, 60, 60)
                        pygame.draw.rect(self.surface, (255, 0, 0), spider_rect, 2)
                for vine in self.ambush_vines:
                    if not vine.dead:
                        vine_screen_y = vine.y + self.camera_y
                        pygame.draw.circle(self.surface, (100, 255, 100), 
                            (int(vine.x), int(vine_screen_y)), vine.detection_radius, 1)
                        tip_x, tip_y = vine.get_tip_position(self.camera_y)
                        pygame.draw.rect(self.surface, (255, 100, 255), 
                            pygame.Rect(tip_x - 25, tip_y - 25, 50, 50), 2)

            self.score = max(0, int(self.speed // 10 - 3))
            hp = self.player.hp
            for i in range(5):
                heart_x = 20 + i * 52
                heart_value = hp - i * 2
                if heart_value >= 2:
                    self.surface.blit(valley_climb.heart_full, (heart_x, 20))
                elif heart_value == 1:
                    self.surface.blit(valley_climb.heart_half, (heart_x, 20))
                else:
                    self.surface.blit(valley_climb.heart_empty, (heart_x, 20))

            if self.player.falling:
                self.done = True
                if not hasattr(self, "fall_timer"):
                    self.fall_timer = 0
                self.fall_timer += dt
                if self.fall_timer >= 1200:
                    self.should_end = True
            if self.should_end:
                renpy.end_interaction(self.score)
                return renpy.Render(1920, 1080)

            r = renpy.Render(1920, 1080)
            r.blit(self.surface, (0, 0))
            renpy.redraw(self, 0)
            return r

        def __getstate__(self):
            return None

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.done = True
                    renpy.end_interaction(self.score)
                    return
                if ev.key == pygame.K_SPACE:
                    self.player.start_attack(self.spiders, self.camera_y)
                    return
            raise renpy.IgnoreEvent()


    class VineBlasterDisplayable(renpy.Displayable):
        def __init__(self):
            super().__init__()
            import pygame
            self.__dict__["surface"] = pygame.Surface((1920, 1080), pygame.SRCALPHA)
            self.clock = pygame.time.Clock()
            self.reset_game()
        
        def reset_game(self):
            self.tristan = vine_blaster.PlayerCursor("tristan")
            self.henry = vine_blaster.PlayerCursor("henry")
            self.projectiles = []
            self.vines = []
            self.spiders = []
            self.particles = []  # Impact particles
            self.wave = 1
            self.wave_timer = 0
            self.spawn_timer = 0
            self.encroachment = 0
            self.second_winds_used = 0
            self.game_over = False
            self.victory = False
            self.done = False
            self.score = 0
            self.time_ms = 0
        
        def render(self, width, height, st, at):
            import pygame
            if self.done:
                return renpy.Render(1920, 1080)
            dt = self.clock.tick(60)
            self.time_ms += dt
            self.surface.fill((20, 30, 40))
            keys = pygame.key.get_pressed()

            self.tristan.update(keys, dt)
            self.henry.update(keys, dt)

            self.wave_timer += dt
            wave_dur = vine_blaster.WAVE_DURATION[min(self.wave - 1, 2)]
            if self.wave_timer >= wave_dur and self.wave < vine_blaster.WAVE_COUNT:
                self.wave += 1
                self.wave_timer = 0
            if self.wave >= vine_blaster.WAVE_COUNT and self.wave_timer >= wave_dur:
                self.victory = True
                self.done = True

            self.spawn_timer += dt
            spawn_rate = vine_blaster.WAVE_SPAWN_RATE[min(self.wave - 1, 2)]
            if self.spawn_timer >= spawn_rate:
                self.vines.append(vine_blaster.VineSegment(random.choice(["top", "bottom", "left", "right"])))
                self.spawn_timer = 0
                good_vines = [v for v in self.vines if v.alive and v.growth > 0.3]
                if good_vines and random.random() < 0.3:
                    self.spiders.append(vine_blaster.VineSpider(random.choice(good_vines)))

            for vine in self.vines[:]:
                vine.update(dt)
                if not vine.alive:
                    self.vines.remove(vine)
                    self.score += 100

            for spider in self.spiders[:]:
                spider.update(dt)
                if not spider.alive or not spider.vine.alive:
                    if not spider.alive:
                        self.score += 50
                    self.spiders.remove(spider)
                elif spider.reached_beacon():
                    self.encroachment += 5
                    self.spiders.remove(spider)

            for proj in self.projectiles[:]:
                proj.update(dt)
                if not proj.alive:
                    self.projectiles.remove(proj)
                    continue
                for vine in self.vines:
                    if vine.alive and proj.rect().colliderect(vine.rect()):
                        vine.take_damage(1)
                        # Spawn green particles for vine hit
                        tip_x, tip_y = vine.get_tip_position()
                        self.particles.extend(vine_blaster.spawn_impact(
                            tip_x, tip_y, (80, 180, 60)))
                        proj.alive = False
                        break
                for spider in self.spiders:
                    if spider.alive and proj.rect().colliderect(spider.rect()):
                        spider.take_damage(1)
                        # Spawn purple particles for spider hit
                        sx, sy = spider.get_position()
                        self.particles.extend(vine_blaster.spawn_impact(
                            sx, sy, (150, 80, 180)))
                        proj.alive = False
                        break

            # Update particles
            for particle in self.particles[:]:
                particle.update(dt)
                if not particle.alive:
                    self.particles.remove(particle)

            for vine in self.vines:
                if vine.alive and vine.growth >= 0.95:
                    self.encroachment += vine_blaster.ENCROACHMENT_RATE * (dt / 1000)

            if self.encroachment >= vine_blaster.SECOND_WIND_THRESHOLD:
                if self.second_winds_used < vine_blaster.MAX_SECOND_WINDS:
                    self.encroachment = vine_blaster.SECOND_WIND_RESET
                    self.second_winds_used += 1
                else:
                    self.game_over = True
                    self.done = True

            for y_pos in range(0, height, 20):
                shade = int(20 + (y_pos / height) * 15)
                pygame.draw.rect(self.surface, (shade, shade + 10, shade + 20), (0, y_pos, width, 20))

            bx, by = vine_blaster.BEACON_CENTER
            pulse = math.sin(self.time_ms * 0.005) * 20 + 60
            for r in range(3):
                glow_alpha = 30 - r * 10
                glow_size = vine_blaster.BEACON_RADIUS + 40 + r * 20
                glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
                pygame.draw.circle(glow_surf, (255, 200, 100, glow_alpha), (glow_size, glow_size), glow_size)
                self.surface.blit(glow_surf, (bx - glow_size, by - glow_size))
            pygame.draw.circle(self.surface, (255, 200, 100), (bx, by), vine_blaster.BEACON_RADIUS + 20)
            pygame.draw.circle(self.surface, (255, 220, 150), (bx, by), vine_blaster.BEACON_RADIUS)
            pygame.draw.circle(self.surface, (255, 255, 200), (bx, by), int(pulse))
            pygame.draw.circle(self.surface, (255, 255, 255), (bx, by), int(pulse * 0.5))

            for vine in self.vines:
                vine.draw(self.surface, self.time_ms)
            for spider in self.spiders:
                spider.draw(self.surface)
            for proj in self.projectiles:
                proj.draw(self.surface)
            # Draw particles on top
            for particle in self.particles:
                particle.draw(self.surface)
            self.tristan.draw(self.surface)
            self.henry.draw(self.surface)

            meter_x = (width - 300) // 2
            meter_y = 30
            draw_rounded_rect(self.surface, (30, 30, 40), (meter_x - 2, meter_y - 2, 304, 34), radius=5)
            draw_rounded_rect(self.surface, (50, 50, 60), (meter_x, meter_y, 300, 30), radius=4)
            fill = int((self.encroachment / 100) * 300)
            if self.encroachment > 75:
                color = (255, 80, 80)
            elif self.encroachment > 50:
                color = (255, 180, 80)
            else:
                color = (100, 255, 150)
            if fill > 0:
                draw_rounded_rect(self.surface, color, (meter_x, meter_y, fill, 30), radius=4)
            draw_rounded_rect(self.surface, (200, 200, 220), (meter_x, meter_y, 300, 30), radius=4, width=2)
            
            for i in range(vine_blaster.MAX_SECOND_WINDS):
                sw_x = meter_x + 310 + i * 25
                if i < self.second_winds_used:
                    pygame.draw.circle(self.surface, (100, 100, 100), (sw_x, meter_y + 15), 10)
                else:
                    pygame.draw.circle(self.surface, (100, 255, 200), (sw_x, meter_y + 15), 10)
                    pygame.draw.circle(self.surface, (150, 255, 220), (sw_x, meter_y + 15), 6)

            r = renpy.Render(1920, 1080)
            r.blit(self.surface, (0, 0))
            renpy.redraw(self, 0)
            return r
        
        def __getstate__(self):
            return None
        
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.done = True
                    renpy.end_interaction(self.score)
                    return
                if ev.key == pygame.K_SPACE:
                    proj = self.tristan.fire(self.tristan.x, self.tristan.y)
                    if proj:
                        self.projectiles.append(proj)
                if ev.key in (pygame.K_e, pygame.K_RETURN):
                    proj = self.henry.fire(self.henry.x, self.henry.y)
                    if proj:
                        self.projectiles.append(proj)
            if ev.type == pygame.MOUSEBUTTONDOWN:
                proj = self.tristan.fire(x, y)
                if proj:
                    self.projectiles.append(proj)
            raise renpy.IgnoreEvent()


############################################################################
# Screens
############################################################################

screen valley_climb_screen():
    modal True
    zorder 100
    $ game_display = ValleyClimbDisplayable()
    add game_display xalign 0.5 yalign 0.0
    frame:
        background Solid("#000000ba")
        xpos 1700 ypos 20 xanchor 1.0
        text "Score: [game_display.score]" size 40 color "#FFFFFF" outlines [(2, "#000000")]

screen vine_blaster_screen():
    modal True
    zorder 100
    $ game_display = VineBlasterDisplayable()
    add game_display xalign 0.5 yalign 0.0
    frame:
        background Solid("#000000ba")
        xpos 1700 ypos 20 xanchor 1.0
        text "Wave [game_display.wave] | Score: [game_display.score]" size 32 color "#FFFFFF"


############################################################################
# Labels
############################################################################

label play_valley_climb:
    # Start minigame music
    $ valley_start_music("valley_climb")

    show screen valley_climb_screen
    "Arrow Keys to climb! SPACE to attack! ESC to exit."
    $ score = ui.interact()
    hide screen valley_climb_screen

    # Stop minigame music
    $ valley_stop_music()

    "You finished climbing with a score of [score]!"
    menu:
        "Continue":
            return
        "Try again":
            jump play_valley_climb
    return

label play_vine_blaster:
    # Start minigame music
    $ valley_start_music("vine_blaster")

    show screen vine_blaster_screen
    "Tristan: Arrow Keys + SPACE | Henry: WASD + E | Destroy the vines!"
    $ score = ui.interact()
    hide screen vine_blaster_screen

    # Stop minigame music
    $ valley_stop_music()

    $ game_display = VineBlasterDisplayable()
    if game_display.victory:
        "The beacon is saved! Score: [score]"
    else:
        "The vines overwhelmed the beacon... Score: [score]"
    menu:
        "Continue":
            return
        "Try again":
            jump play_vine_blaster
    return
