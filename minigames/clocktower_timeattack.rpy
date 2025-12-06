# clocktower_timeattack.rpy - Clocktower Time Attack Minigame
# A fast-paced gear-clicking challenge against the clock

####################################################################################################################
# GEAR RUSH TIME ATTACK MINIGAME
####################################################################################################################

init python in gear_rush:
    import pygame
    import random
    import math
    from pygame.locals import *

    ####################################################################################################################
    # SPRITE CONFIGURATION - Set USE_SPRITES = True and provide sprite paths to use custom graphics
    ####################################################################################################################

    USE_SPRITES = False  # Set to True when sprites are ready

    # Gear sprites - one for each gear material type
    # Each gear should be a centered sprite with transparency
    GEAR_SPRITES = {
        "bronze": "images/minigames/gearrush/gears/gear_bronze.png",
        "silver": "images/minigames/gearrush/gears/gear_silver.png",
        "gold": "images/minigames/gearrush/gears/gear_gold.png",
        "copper": "images/minigames/gearrush/gears/gear_copper.png",
        "steel": "images/minigames/gearrush/gears/gear_steel.png",
    }

    # Gear glow sprites (rendered behind gear when highlighted)
    GEAR_GLOW_SPRITES = {
        "bronze": "images/minigames/gearrush/glows/glow_bronze.png",
        "silver": "images/minigames/gearrush/glows/glow_silver.png",
        "gold": "images/minigames/gearrush/glows/glow_gold.png",
        "copper": "images/minigames/gearrush/glows/glow_copper.png",
        "steel": "images/minigames/gearrush/glows/glow_steel.png",
    }

    # Target ring sprite (pulsing ring around next gear to click)
    TARGET_RING_SPRITE = "images/minigames/gearrush/effects/target_ring.png"

    # Wrong click flash sprite
    WRONG_CLICK_SPRITE = "images/minigames/gearrush/effects/wrong_flash.png"

    # Number sprites for gear order (0-9 plus "10")
    NUMBER_SPRITES = {
        1: "images/minigames/gearrush/numbers/num_1.png",
        2: "images/minigames/gearrush/numbers/num_2.png",
        3: "images/minigames/gearrush/numbers/num_3.png",
        4: "images/minigames/gearrush/numbers/num_4.png",
        5: "images/minigames/gearrush/numbers/num_5.png",
        6: "images/minigames/gearrush/numbers/num_6.png",
        7: "images/minigames/gearrush/numbers/num_7.png",
        8: "images/minigames/gearrush/numbers/num_8.png",
        9: "images/minigames/gearrush/numbers/num_9.png",
        10: "images/minigames/gearrush/numbers/num_10.png",
    }

    # Click effect particles
    CLICK_PARTICLE_SPRITES = {
        "success": "images/minigames/gearrush/particles/particle_success.png",
        "fail": "images/minigames/gearrush/particles/particle_fail.png",
        "spark_gold": "images/minigames/gearrush/particles/spark_gold.png",
        "spark_green": "images/minigames/gearrush/particles/spark_green.png",
        "spark_red": "images/minigames/gearrush/particles/spark_red.png",
    }

    # Background decorative gears (larger, slower, faded)
    BG_GEAR_SPRITES = {
        "small": "images/minigames/gearrush/background/bg_gear_small.png",
        "medium": "images/minigames/gearrush/background/bg_gear_medium.png",
        "large": "images/minigames/gearrush/background/bg_gear_large.png",
    }

    # UI element sprites
    UI_SPRITES = {
        "time_bar_bg": "images/minigames/gearrush/ui/time_bar_bg.png",
        "time_bar_fill_green": "images/minigames/gearrush/ui/time_bar_fill_green.png",
        "time_bar_fill_yellow": "images/minigames/gearrush/ui/time_bar_fill_yellow.png",
        "time_bar_fill_red": "images/minigames/gearrush/ui/time_bar_fill_red.png",
        "time_bar_frame": "images/minigames/gearrush/ui/time_bar_frame.png",
        "score_panel": "images/minigames/gearrush/ui/score_panel.png",
        "wave_panel": "images/minigames/gearrush/ui/wave_panel.png",
    }

    # Countdown sprites
    COUNTDOWN_SPRITES = {
        3: "images/minigames/gearrush/countdown/count_3.png",
        2: "images/minigames/gearrush/countdown/count_2.png",
        1: "images/minigames/gearrush/countdown/count_1.png",
        "go": "images/minigames/gearrush/countdown/count_go.png",
    }

    # End screen overlays
    OVERLAY_SPRITES = {
        "victory": "images/minigames/gearrush/overlays/victory_banner.png",
        "gameover": "images/minigames/gearrush/overlays/gameover_banner.png",
    }

    # Background image
    BACKGROUND_SPRITE = "images/minigames/gearrush/background.png"

    # Sprite cache
    _sprite_cache = {}

    def load_sprite(path, scale=None):
        """Load a sprite from path with optional scaling.

        Args:
            path: Path to the sprite image
            scale: Optional (width, height) tuple to scale to

        Returns:
            pygame.Surface or None if loading fails
        """
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

    def get_gear_sprite(gear_name, size=None):
        """Get sprite for a gear type.

        Args:
            gear_name: 'bronze', 'silver', 'gold', 'copper', or 'steel'
            size: Optional (width, height) tuple

        Returns:
            pygame.Surface or None
        """
        if not USE_SPRITES:
            return None
        path = GEAR_SPRITES.get(gear_name)
        if not path:
            return None
        return load_sprite(path, size)

    def get_gear_glow_sprite(gear_name, size=None):
        """Get glow sprite for a gear type."""
        if not USE_SPRITES:
            return None
        path = GEAR_GLOW_SPRITES.get(gear_name)
        if not path:
            return None
        return load_sprite(path, size)

    def get_number_sprite(number, size=None):
        """Get sprite for a number (1-10)."""
        if not USE_SPRITES:
            return None
        path = NUMBER_SPRITES.get(number)
        if not path:
            return None
        return load_sprite(path, size)

    def get_particle_sprite(particle_type, size=None):
        """Get a particle effect sprite."""
        if not USE_SPRITES:
            return None
        path = CLICK_PARTICLE_SPRITES.get(particle_type)
        if not path:
            return None
        return load_sprite(path, size)

    def get_bg_gear_sprite(gear_size, dimensions=None):
        """Get a background decorative gear sprite."""
        if not USE_SPRITES:
            return None
        path = BG_GEAR_SPRITES.get(gear_size)
        if not path:
            return None
        return load_sprite(path, dimensions)

    def get_ui_sprite(element, size=None):
        """Get a UI element sprite."""
        if not USE_SPRITES:
            return None
        path = UI_SPRITES.get(element)
        if not path:
            return None
        return load_sprite(path, size)

    def get_countdown_sprite(count, size=None):
        """Get a countdown number sprite."""
        if not USE_SPRITES:
            return None
        path = COUNTDOWN_SPRITES.get(count)
        if not path:
            return None
        return load_sprite(path, size)

    def clear_sprite_cache():
        """Clear the sprite cache to free memory."""
        _sprite_cache.clear()

    ####################################################################################################################
    # END SPRITE CONFIGURATION
    ####################################################################################################################

    ####################################################################################################################
    # AUDIO CONFIGURATION - Sound effects for Gear Rush
    ####################################################################################################################

    USE_AUDIO = True  # Set to False to disable all minigame audio

    AUDIO_PATHS = {
        "gear_click": "audio/sfx/minigames/gearrush/gear_click.ogg",
        "gear_correct": "audio/sfx/minigames/gearrush/gear_correct.ogg",
        "gear_wrong": "audio/sfx/minigames/gearrush/gear_wrong.ogg",
        "gear_spin": "audio/sfx/minigames/gearrush/gear_spin.ogg",
        "gear_chain": "audio/sfx/minigames/gearrush/gear_chain.ogg",
        "wave_complete": "audio/sfx/minigames/gearrush/wave_complete.ogg",
        "countdown_tick": "audio/sfx/minigames/gearrush/countdown_tick.ogg",
        "countdown_go": "audio/sfx/minigames/gearrush/countdown_go.ogg",
        "time_low": "audio/sfx/minigames/gearrush/time_low.ogg",
        "time_bonus": "audio/sfx/minigames/gearrush/time_bonus.ogg",
        "victory": "audio/sfx/minigames/common/victory.ogg",
        "defeat": "audio/sfx/minigames/common/defeat.ogg",
        "game_start": "audio/sfx/minigames/common/game_start.ogg",
    }

    # Background music - fast-paced, time pressure theme
    MUSIC_PATH = "audio/music/minigames/clocktower_gear_rush.ogg"

    _audio_cache = {}
    _audio_initialized = False
    _music_playing = False

    def init_audio():
        global _audio_initialized
        if not _audio_initialized:
            try:
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
                _audio_initialized = True
            except:
                pass

    def load_sound(sound_key):
        if not USE_AUDIO or not _audio_initialized:
            return None
        if sound_key in _audio_cache:
            return _audio_cache[sound_key]
        path = AUDIO_PATHS.get(sound_key)
        if path:
            try:
                sound = pygame.mixer.Sound(path)
                _audio_cache[sound_key] = sound
                return sound
            except:
                return None
        return None

    def play_sound(sound_key, volume=1.0):
        if not USE_AUDIO:
            return
        init_audio()
        sound = load_sound(sound_key)
        if sound:
            sound.set_volume(volume)
            sound.play()

    def start_music(volume=0.6):
        """Start playing the Gear Rush music."""
        global _music_playing
        if not USE_AUDIO:
            return
        init_audio()
        try:
            pygame.mixer.music.load(MUSIC_PATH)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)  # Loop indefinitely
            _music_playing = True
        except:
            pass

    def stop_music(fadeout_ms=500):
        """Stop the Gear Rush music with optional fadeout."""
        global _music_playing
        if not USE_AUDIO:
            return
        try:
            pygame.mixer.music.fadeout(fadeout_ms)
            _music_playing = False
        except:
            pass

    ####################################################################################################################
    # END AUDIO CONFIGURATION
    ####################################################################################################################

    # Game constants
    WIDTH, HEIGHT = 1920, 1080

    # Game states
    STATE_COUNTDOWN = "countdown"
    STATE_PLAYING = "playing"
    STATE_VICTORY = "victory"
    STATE_GAMEOVER = "gameover"

    # Gear colors
    GEAR_COLORS = [
        {"name": "bronze", "color": (180, 130, 70), "glow": (220, 170, 100)},
        {"name": "silver", "color": (180, 190, 200), "glow": (220, 230, 240)},
        {"name": "gold", "color": (220, 180, 50), "glow": (255, 220, 100)},
        {"name": "copper", "color": (180, 100, 80), "glow": (220, 140, 120)},
        {"name": "steel", "color": (140, 150, 170), "glow": (180, 190, 210)},
    ]

    class Gear:
        """A clickable gear target."""
        def __init__(self, x, y, size, order, color_idx):
            self.x = x
            self.y = y
            self.size = size
            self.order = order  # Which number this gear is in sequence
            self.color_idx = color_idx
            self.color_data = GEAR_COLORS[color_idx]

            self.rotation = random.random() * math.pi * 2
            self.rotation_speed = random.uniform(0.5, 2.0) * random.choice([-1, 1])
            self.teeth = random.randint(8, 14)

            self.clicked = False
            self.wrong_click = False
            self.wrong_timer = 0
            self.pulse_phase = random.random() * math.pi * 2
            self.spawn_anim = 0  # For spawn animation

            # Glow effect
            self.glow_intensity = 0

        def update(self, dt):
            self.rotation += self.rotation_speed * dt * 0.001
            self.pulse_phase += dt * 0.005
            self.spawn_anim = min(1.0, self.spawn_anim + dt * 0.004)

            if self.wrong_click:
                self.wrong_timer -= dt
                if self.wrong_timer <= 0:
                    self.wrong_click = False

            # Update glow for next target
            target_glow = 1.0 if self.order == 0 else 0.3
            self.glow_intensity += (target_glow - self.glow_intensity) * 0.1

        def contains_point(self, mx, my):
            """Check if point is within gear."""
            dist = math.hypot(mx - self.x, my - self.y)
            return dist <= self.size

        def draw(self, surf, show_order=True):
            if self.clicked:
                return

            color = self.color_data["color"]
            glow_color = self.color_data["glow"]

            # Apply spawn animation
            current_size = self.size * self.spawn_anim

            if current_size < 5:
                return

            # Create gear surface
            gear_size = int(current_size * 2.5)
            gear_surf = pygame.Surface((gear_size, gear_size), pygame.SRCALPHA)
            cx, cy = gear_size // 2, gear_size // 2

            # Glow effect (stronger for next target)
            if self.glow_intensity > 0.1:
                glow_radius = int(current_size * (1.2 + 0.2 * math.sin(self.pulse_phase)))
                glow_alpha = int(100 * self.glow_intensity)
                pygame.draw.circle(gear_surf, (*glow_color, glow_alpha), (cx, cy), glow_radius)

            # Wrong click flash
            if self.wrong_click:
                flash_alpha = int(150 * (self.wrong_timer / 300))
                pygame.draw.circle(gear_surf, (255, 50, 50, flash_alpha), (cx, cy), int(current_size * 1.3))

            # Draw gear teeth
            tooth_length = current_size * 0.25
            for i in range(self.teeth):
                angle = self.rotation + i * (2 * math.pi / self.teeth)
                inner_r = current_size - tooth_length
                outer_r = current_size
                tooth_width = math.pi / self.teeth * 0.6

                points = [
                    (cx + math.cos(angle - tooth_width) * inner_r,
                     cy + math.sin(angle - tooth_width) * inner_r),
                    (cx + math.cos(angle - tooth_width * 0.4) * outer_r,
                     cy + math.sin(angle - tooth_width * 0.4) * outer_r),
                    (cx + math.cos(angle + tooth_width * 0.4) * outer_r,
                     cy + math.sin(angle + tooth_width * 0.4) * outer_r),
                    (cx + math.cos(angle + tooth_width) * inner_r,
                     cy + math.sin(angle + tooth_width) * inner_r),
                ]
                pygame.draw.polygon(gear_surf, color, points)

            # Gear body
            pygame.draw.circle(gear_surf, color, (cx, cy), int(current_size - tooth_length))

            # Inner ring (highlight)
            highlight = tuple(min(255, c + 40) for c in color)
            pygame.draw.circle(gear_surf, highlight, (cx, cy), int(current_size * 0.7), 3)

            # Center hole
            pygame.draw.circle(gear_surf, (40, 30, 50), (cx, cy), int(current_size * 0.25))
            pygame.draw.circle(gear_surf, (60, 50, 70), (cx, cy), int(current_size * 0.15))

            surf.blit(gear_surf, (self.x - gear_size // 2, self.y - gear_size // 2))

            # Draw order number
            if show_order and self.order >= 0:
                font = pygame.font.Font(None, int(current_size * 0.8))
                # Highlight the next gear to click
                if self.order == 0:
                    num_color = (255, 255, 100)
                    # Pulsing ring around next target
                    pulse_size = current_size * (1.1 + 0.1 * math.sin(self.pulse_phase * 2))
                    ring_surf = pygame.Surface((int(pulse_size * 2.4), int(pulse_size * 2.4)), pygame.SRCALPHA)
                    ring_cx, ring_cy = int(pulse_size * 1.2), int(pulse_size * 1.2)
                    pygame.draw.circle(ring_surf, (255, 255, 100, 150), (ring_cx, ring_cy), int(pulse_size), 4)
                    surf.blit(ring_surf, (self.x - pulse_size * 1.2, self.y - pulse_size * 1.2))
                else:
                    num_color = (255, 255, 255)

                num_text = font.render(str(self.order + 1), True, num_color)
                surf.blit(num_text, (self.x - num_text.get_width() // 2,
                                    self.y - num_text.get_height() // 2))

    class ClickEffect:
        """Visual effect when gear is clicked."""
        def __init__(self, x, y, success):
            self.x = x
            self.y = y
            self.success = success
            self.lifetime = 400
            self.max_lifetime = 400
            self.particles = []

            # Create particles
            color = (100, 255, 150) if success else (255, 100, 100)
            for _ in range(12 if success else 6):
                angle = random.random() * math.pi * 2
                speed = random.uniform(3, 8)
                self.particles.append({
                    'x': x,
                    'y': y,
                    'vx': math.cos(angle) * speed,
                    'vy': math.sin(angle) * speed,
                    'size': random.uniform(4, 10),
                    'color': color
                })

        def update(self, dt):
            self.lifetime -= dt
            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['vy'] += 0.1
            return self.lifetime > 0

        def draw(self, surf):
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            for p in self.particles:
                size = p['size'] * (self.lifetime / self.max_lifetime)
                if size > 0:
                    particle_surf = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
                    pygame.draw.circle(particle_surf, (*p['color'], alpha),
                                     (int(size + 2), int(size + 2)), int(size))
                    surf.blit(particle_surf, (int(p['x'] - size), int(p['y'] - size)))

    class GearRushGame:
        """Main game controller for Gear Rush."""
        def __init__(self, target_waves=5, time_limit=60):
            self.state = STATE_COUNTDOWN
            self.countdown = 3
            self.countdown_timer = 0

            self.target_waves = target_waves
            self.time_limit = time_limit
            self.time_remaining = time_limit

            self.wave = 0
            self.score = 0
            self.gears_per_wave = 4  # Starting gears
            self.gears = []
            self.effects = []

            self.perfect_waves = 0
            self.total_clicks = 0
            self.wrong_clicks = 0

            # Background gears (decorative)
            self.bg_gears = []
            for _ in range(8):
                self.bg_gears.append({
                    'x': random.randint(100, WIDTH - 100),
                    'y': random.randint(100, HEIGHT - 100),
                    'size': random.randint(60, 150),
                    'rotation': random.random() * math.pi * 2,
                    'speed': random.uniform(0.2, 0.8) * random.choice([-1, 1]),
                    'teeth': random.randint(10, 16),
                    'alpha': random.randint(20, 50)
                })

        def start_wave(self):
            """Start a new wave of gears."""
            self.wave += 1
            self.gears = []

            # Calculate gears for this wave
            num_gears = min(self.gears_per_wave + (self.wave - 1), 10)

            # Generate non-overlapping positions
            positions = []
            margin = 150
            min_dist = 140

            for i in range(num_gears):
                attempts = 0
                while attempts < 100:
                    x = random.randint(margin, WIDTH - margin)
                    y = random.randint(margin + 100, HEIGHT - margin - 50)

                    # Check distance from other gears
                    valid = True
                    for px, py in positions:
                        if math.hypot(x - px, y - py) < min_dist:
                            valid = False
                            break

                    if valid:
                        positions.append((x, y))
                        break
                    attempts += 1

                if attempts >= 100 and len(positions) <= i:
                    # Fallback position
                    positions.append((margin + i * 150, HEIGHT // 2))

            # Create gears
            for i, (x, y) in enumerate(positions):
                size = random.randint(45, 65)
                color_idx = random.randint(0, len(GEAR_COLORS) - 1)
                gear = Gear(x, y, size, i, color_idx)
                self.gears.append(gear)

        def handle_click(self, mx, my):
            """Handle mouse click."""
            if self.state != STATE_PLAYING:
                return

            self.total_clicks += 1

            # Find clicked gear
            for gear in self.gears:
                if gear.clicked:
                    continue

                if gear.contains_point(mx, my):
                    if gear.order == 0:
                        # Correct click!
                        gear.clicked = True
                        self.score += 100 + int(self.time_remaining * 2)
                        self.effects.append(ClickEffect(gear.x, gear.y, True))

                        # Update remaining gear orders
                        for g in self.gears:
                            if not g.clicked:
                                g.order -= 1

                        # Check if wave complete
                        if all(g.clicked for g in self.gears):
                            self.complete_wave()
                    else:
                        # Wrong click!
                        gear.wrong_click = True
                        gear.wrong_timer = 300
                        self.wrong_clicks += 1
                        self.time_remaining = max(0, self.time_remaining - 2)  # Time penalty
                        self.effects.append(ClickEffect(mx, my, False))
                    return

            # Clicked nothing - small time penalty
            self.time_remaining = max(0, self.time_remaining - 0.5)

        def complete_wave(self):
            """Handle wave completion."""
            # Bonus for completing wave
            wave_bonus = 200 * self.wave

            # Perfect wave bonus (no wrong clicks this wave)
            wave_wrong = sum(1 for g in self.gears if g.wrong_click)
            if wave_wrong == 0:
                self.perfect_waves += 1
                wave_bonus += 300

            self.score += wave_bonus

            # Time bonus
            self.time_remaining = min(self.time_limit, self.time_remaining + 5)

            # Check victory
            if self.wave >= self.target_waves:
                self.state = STATE_VICTORY
            else:
                self.start_wave()

        def update(self, dt):
            # Update background gears
            for bg in self.bg_gears:
                bg['rotation'] += bg['speed'] * dt * 0.001

            # Update effects
            self.effects = [e for e in self.effects if e.update(dt)]

            if self.state == STATE_COUNTDOWN:
                self.countdown_timer += dt
                if self.countdown_timer >= 1000:
                    self.countdown_timer = 0
                    self.countdown -= 1
                    if self.countdown <= 0:
                        self.state = STATE_PLAYING
                        self.start_wave()
                return

            if self.state != STATE_PLAYING:
                return

            # Update timer
            self.time_remaining -= dt / 1000
            if self.time_remaining <= 0:
                self.time_remaining = 0
                self.state = STATE_GAMEOVER

            # Update gears
            for gear in self.gears:
                gear.update(dt)

        def draw(self, surf):
            # Draw background gears
            self.draw_background(surf)

            # Draw active gears
            for gear in self.gears:
                gear.draw(surf)

            # Draw effects
            for effect in self.effects:
                effect.draw(surf)

            # Draw UI
            self.draw_ui(surf)

            # Draw countdown
            if self.state == STATE_COUNTDOWN:
                self.draw_countdown(surf)

            # Draw end screen
            if self.state in (STATE_VICTORY, STATE_GAMEOVER):
                self.draw_end_screen(surf)

        def draw_background(self, surf):
            """Draw decorative background gears."""
            for bg in self.bg_gears:
                gear_surf = pygame.Surface((bg['size'] * 2 + 40, bg['size'] * 2 + 40), pygame.SRCALPHA)
                cx, cy = bg['size'] + 20, bg['size'] + 20

                # Draw teeth
                tooth_length = bg['size'] * 0.2
                for i in range(bg['teeth']):
                    angle = bg['rotation'] + i * (2 * math.pi / bg['teeth'])
                    inner_r = bg['size'] - tooth_length
                    outer_r = bg['size']
                    tooth_width = math.pi / bg['teeth'] * 0.6

                    points = [
                        (cx + math.cos(angle - tooth_width) * inner_r,
                         cy + math.sin(angle - tooth_width) * inner_r),
                        (cx + math.cos(angle - tooth_width * 0.4) * outer_r,
                         cy + math.sin(angle - tooth_width * 0.4) * outer_r),
                        (cx + math.cos(angle + tooth_width * 0.4) * outer_r,
                         cy + math.sin(angle + tooth_width * 0.4) * outer_r),
                        (cx + math.cos(angle + tooth_width) * inner_r,
                         cy + math.sin(angle + tooth_width) * inner_r),
                    ]
                    pygame.draw.polygon(gear_surf, (60, 50, 80, bg['alpha']), points)

                pygame.draw.circle(gear_surf, (50, 40, 70, bg['alpha']), (cx, cy), int(bg['size'] - tooth_length))
                pygame.draw.circle(gear_surf, (40, 30, 55, bg['alpha']), (cx, cy), int(bg['size'] * 0.3))

                surf.blit(gear_surf, (bg['x'] - bg['size'] - 20, bg['y'] - bg['size'] - 20))

        def draw_ui(self, surf):
            """Draw game UI."""
            font_large = pygame.font.Font(None, 64)
            font_medium = pygame.font.Font(None, 48)
            font_small = pygame.font.Font(None, 32)

            # Time bar (top)
            bar_width = 600
            bar_height = 30
            bar_x = WIDTH // 2 - bar_width // 2
            bar_y = 30

            # Background
            pygame.draw.rect(surf, (40, 30, 60), (bar_x - 5, bar_y - 5, bar_width + 10, bar_height + 10), border_radius=10)

            # Fill
            fill_ratio = self.time_remaining / self.time_limit
            fill_width = int(bar_width * fill_ratio)
            fill_color = (100, 200, 100) if fill_ratio > 0.3 else (255, 150, 50) if fill_ratio > 0.15 else (255, 80, 80)
            if fill_width > 0:
                pygame.draw.rect(surf, fill_color, (bar_x, bar_y, fill_width, bar_height), border_radius=8)

            # Border
            pygame.draw.rect(surf, (150, 130, 180), (bar_x - 5, bar_y - 5, bar_width + 10, bar_height + 10), width=3, border_radius=10)

            # Time text
            time_text = font_medium.render(f"{self.time_remaining:.1f}s", True, (255, 255, 255))
            surf.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, bar_y + bar_height + 10))

            # Score (top left)
            score_label = font_small.render("SCORE", True, (180, 160, 220))
            surf.blit(score_label, (50, 30))
            score_text = font_large.render(f"{self.score}", True, (255, 255, 255))
            surf.blit(score_text, (50, 55))

            # Wave (top right)
            wave_label = font_small.render("WAVE", True, (180, 160, 220))
            surf.blit(wave_label, (WIDTH - 150, 30))
            wave_text = font_large.render(f"{self.wave}/{self.target_waves}", True, (255, 220, 100))
            surf.blit(wave_text, (WIDTH - 150, 55))

            # Instructions (bottom)
            if self.state == STATE_PLAYING:
                inst_text = font_small.render("Click gears in order (1, 2, 3...)", True, (150, 140, 180))
                surf.blit(inst_text, (WIDTH // 2 - inst_text.get_width() // 2, HEIGHT - 50))

        def draw_countdown(self, surf):
            """Draw countdown before game starts."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            surf.blit(overlay, (0, 0))

            font = pygame.font.Font(None, 200)

            if self.countdown > 0:
                text = font.render(str(self.countdown), True, (255, 255, 255))
            else:
                text = font.render("GO!", True, (100, 255, 150))

            surf.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        def draw_end_screen(self, surf):
            """Draw end game screen."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            surf.blit(overlay, (0, 0))

            font_title = pygame.font.Font(None, 96)
            font_large = pygame.font.Font(None, 64)
            font_medium = pygame.font.Font(None, 48)

            # Title
            if self.state == STATE_VICTORY:
                title = font_title.render("GEARS ALIGNED!", True, (100, 255, 150))
            else:
                title = font_title.render("TIME'S UP!", True, (255, 100, 100))

            surf.blit(title, (WIDTH // 2 - title.get_width() // 2, 180))

            # Stats
            y = 300
            spacing = 60

            score_text = font_large.render(f"Score: {self.score}", True, (255, 255, 255))
            surf.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, y))
            y += spacing

            waves_text = font_medium.render(f"Waves Completed: {self.wave}/{self.target_waves}", True, (200, 180, 255))
            surf.blit(waves_text, (WIDTH // 2 - waves_text.get_width() // 2, y))
            y += spacing

            perfect_text = font_medium.render(f"Perfect Waves: {self.perfect_waves}", True, (255, 220, 100))
            surf.blit(perfect_text, (WIDTH // 2 - perfect_text.get_width() // 2, y))
            y += spacing

            accuracy = ((self.total_clicks - self.wrong_clicks) / self.total_clicks * 100) if self.total_clicks > 0 else 0
            acc_color = (100, 255, 150) if accuracy >= 90 else (255, 220, 100) if accuracy >= 70 else (255, 150, 100)
            acc_text = font_medium.render(f"Accuracy: {accuracy:.1f}%", True, acc_color)
            surf.blit(acc_text, (WIDTH // 2 - acc_text.get_width() // 2, y))

            # Continue prompt
            prompt = font_medium.render("Press ENTER to continue", True, (180, 160, 220))
            surf.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT - 120))


# Ren'Py Displayable wrapper
init python:
    class GearRushDisplayable(renpy.Displayable):
        """Ren'Py displayable wrapper for Gear Rush."""

        def __init__(self, target_waves=5, time_limit=60, **kwargs):
            super(GearRushDisplayable, self).__init__(**kwargs)
            self.target_waves = target_waves
            self.time_limit = time_limit
            self.game = None
            self.last_time = None

        def render(self, width, height, st, at):
            import pygame

            if self.game is None:
                self.game = gear_rush.GearRushGame(self.target_waves, self.time_limit)
                self.last_time = pygame.time.get_ticks()

            current_time = pygame.time.get_ticks()
            dt = current_time - self.last_time
            self.last_time = current_time

            self.game.update(dt)

            render = renpy.Render(gear_rush.WIDTH, gear_rush.HEIGHT)
            canvas = render.canvas()
            canvas.rect((30, 22, 50), (0, 0, gear_rush.WIDTH, gear_rush.HEIGHT))
            self.game.draw(canvas.get_surface())

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            import pygame

            if self.game is None:
                return None

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.game.handle_click(x, y)

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    return "quit"
                if ev.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    if self.game.state == gear_rush.STATE_VICTORY:
                        return "victory"
                    elif self.game.state == gear_rush.STATE_GAMEOVER:
                        return "retry"

            return None

        def visit(self):
            return []


# Screen
screen gear_rush_screen(target_waves=5, time_limit=60):
    default game_display = GearRushDisplayable(target_waves, time_limit)

    add Solid("#1e1632")
    add game_display

    key "K_ESCAPE" action Return("quit")


# Entry label
label gear_rush_start(target_waves=5, time_limit=60):
    $ quick_menu = False

    # Start minigame music
    $ gear_rush.start_music()

    call screen gear_rush_screen(target_waves, time_limit)

    # Stop minigame music
    $ gear_rush.stop_music()

    $ quick_menu = True
    $ result = _return

    if result == "victory":
        return True
    else:
        return False


# Test label
label test_gear_rush:
    "Starting Gear Rush!"
    "Click the gears in numerical order before time runs out!"

    call gear_rush_start(target_waves=5, time_limit=45)

    if _return:
        "The clockwork is perfectly synchronized!"
    else:
        "The gears need more tuning..."

    return
