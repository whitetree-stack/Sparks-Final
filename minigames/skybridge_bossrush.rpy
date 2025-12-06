# skybridge_bossrush.rpy - Skybridge Boss Rush Minigame
# Epic finale boss battle against the Shadow King

####################################################################################################################
# SHADOW KING BOSS RUSH MINIGAME
####################################################################################################################

init python in boss_rush:
    import pygame
    import random
    import math
    from pygame.locals import *

    ####################################################################################################################
    # SPRITE CONFIGURATION - Set USE_SPRITES = True and provide sprite paths to use custom graphics
    ####################################################################################################################

    USE_SPRITES = False  # Set to True when sprites are ready

    # Hero twin sprites (Tristan and Henry)
    HERO_SPRITES = {
        # Tristan (green hero) - Arrow key controls
        "tristan_idle": "images/minigames/bossrush/heroes/tristan_idle.png",
        "tristan_move_left": "images/minigames/bossrush/heroes/tristan_move_left.png",
        "tristan_move_right": "images/minigames/bossrush/heroes/tristan_move_right.png",
        "tristan_shoot": "images/minigames/bossrush/heroes/tristan_shoot.png",
        "tristan_hit": "images/minigames/bossrush/heroes/tristan_hit.png",
        "tristan_glow": "images/minigames/bossrush/heroes/tristan_glow.png",

        # Henry (blue hero) - WASD controls
        "henry_idle": "images/minigames/bossrush/heroes/henry_idle.png",
        "henry_move_left": "images/minigames/bossrush/heroes/henry_move_left.png",
        "henry_move_right": "images/minigames/bossrush/heroes/henry_move_right.png",
        "henry_shoot": "images/minigames/bossrush/heroes/henry_shoot.png",
        "henry_hit": "images/minigames/bossrush/heroes/henry_hit.png",
        "henry_glow": "images/minigames/bossrush/heroes/henry_glow.png",
    }

    # Hero projectile sprites (light orbs fired by heroes)
    HERO_PROJECTILE_SPRITES = {
        "orb_green": "images/minigames/bossrush/projectiles/orb_green.png",
        "orb_green_glow": "images/minigames/bossrush/projectiles/orb_green_glow.png",
        "orb_green_trail": "images/minigames/bossrush/projectiles/orb_green_trail.png",
        "orb_blue": "images/minigames/bossrush/projectiles/orb_blue.png",
        "orb_blue_glow": "images/minigames/bossrush/projectiles/orb_blue_glow.png",
        "orb_blue_trail": "images/minigames/bossrush/projectiles/orb_blue_trail.png",
    }

    # Shadow King boss sprites (multi-phase)
    BOSS_SPRITES = {
        # Phase 1 (full health)
        "phase1_idle": "images/minigames/bossrush/boss/phase1_idle.png",
        "phase1_attack": "images/minigames/bossrush/boss/phase1_attack.png",
        "phase1_hit": "images/minigames/bossrush/boss/phase1_hit.png",
        "phase1_aura": "images/minigames/bossrush/boss/phase1_aura.png",

        # Phase 2 (below 66% health)
        "phase2_idle": "images/minigames/bossrush/boss/phase2_idle.png",
        "phase2_attack": "images/minigames/bossrush/boss/phase2_attack.png",
        "phase2_hit": "images/minigames/bossrush/boss/phase2_hit.png",
        "phase2_aura": "images/minigames/bossrush/boss/phase2_aura.png",

        # Phase 3 (below 33% health - enraged)
        "phase3_idle": "images/minigames/bossrush/boss/phase3_idle.png",
        "phase3_attack": "images/minigames/bossrush/boss/phase3_attack.png",
        "phase3_hit": "images/minigames/bossrush/boss/phase3_hit.png",
        "phase3_aura": "images/minigames/bossrush/boss/phase3_aura.png",

        # Common elements
        "crown": "images/minigames/bossrush/boss/crown.png",
        "crown_glow": "images/minigames/bossrush/boss/crown_glow.png",
        "eyes": "images/minigames/bossrush/boss/eyes.png",
        "eyes_glow": "images/minigames/bossrush/boss/eyes_glow.png",
        "shadow": "images/minigames/bossrush/boss/shadow.png",
        "death_anim_0": "images/minigames/bossrush/boss/death_anim_0.png",
        "death_anim_1": "images/minigames/bossrush/boss/death_anim_1.png",
        "death_anim_2": "images/minigames/bossrush/boss/death_anim_2.png",
    }

    # Boss projectile sprites (dark orbs and spikes)
    BOSS_PROJECTILE_SPRITES = {
        "orb_dark": "images/minigames/bossrush/projectiles/orb_dark.png",
        "orb_dark_glow": "images/minigames/bossrush/projectiles/orb_dark_glow.png",
        "spike": "images/minigames/bossrush/projectiles/spike.png",
        "spike_glow": "images/minigames/bossrush/projectiles/spike_glow.png",
        "shadow_bolt": "images/minigames/bossrush/projectiles/shadow_bolt.png",
        "void_sphere": "images/minigames/bossrush/projectiles/void_sphere.png",
    }

    # Attack effect sprites (special attack visuals)
    ATTACK_EFFECT_SPRITES = {
        "spread_warning": "images/minigames/bossrush/effects/spread_warning.png",
        "rain_warning": "images/minigames/bossrush/effects/rain_warning.png",
        "spiral_charge": "images/minigames/bossrush/effects/spiral_charge.png",
        "targeted_lock": "images/minigames/bossrush/effects/targeted_lock.png",
    }

    # Hit/particle effect sprites
    HIT_EFFECT_SPRITES = {
        "spark_green": "images/minigames/bossrush/effects/spark_green.png",
        "spark_blue": "images/minigames/bossrush/effects/spark_blue.png",
        "spark_purple": "images/minigames/bossrush/effects/spark_purple.png",
        "spark_red": "images/minigames/bossrush/effects/spark_red.png",
        "explosion_small": "images/minigames/bossrush/effects/explosion_small.png",
        "explosion_large": "images/minigames/bossrush/effects/explosion_large.png",
        "hit_flash": "images/minigames/bossrush/effects/hit_flash.png",
    }

    # Background sprites
    BACKGROUND_SPRITES = {
        "sky_gradient": "images/minigames/bossrush/background/sky_gradient.png",
        "floating_particle": "images/minigames/bossrush/background/floating_particle.png",
        "lightning_flash": "images/minigames/bossrush/background/lightning_flash.png",
        "arena_floor": "images/minigames/bossrush/background/arena_floor.png",
        "arena_edge": "images/minigames/bossrush/background/arena_edge.png",
    }

    # UI element sprites
    UI_SPRITES = {
        "heart_full": "images/minigames/bossrush/ui/heart_full.png",
        "heart_empty": "images/minigames/bossrush/ui/heart_empty.png",
        "boss_health_bar_bg": "images/minigames/bossrush/ui/boss_health_bar_bg.png",
        "boss_health_bar_fill": "images/minigames/bossrush/ui/boss_health_bar_fill.png",
        "boss_health_bar_frame": "images/minigames/bossrush/ui/boss_health_bar_frame.png",
        "phase_indicator": "images/minigames/bossrush/ui/phase_indicator.png",
        "controls_panel": "images/minigames/bossrush/ui/controls_panel.png",
    }

    # Overlay sprites for intro/end screens
    OVERLAY_SPRITES = {
        "intro_title": "images/minigames/bossrush/overlays/intro_title.png",
        "intro_subtitle": "images/minigames/bossrush/overlays/intro_subtitle.png",
        "victory_banner": "images/minigames/bossrush/overlays/victory_banner.png",
        "defeat_banner": "images/minigames/bossrush/overlays/defeat_banner.png",
        "vignette": "images/minigames/bossrush/overlays/vignette.png",
    }

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

    def get_hero_sprite(hero_name, state):
        """Get hero sprite for current state.

        Args:
            hero_name: 'tristan' or 'henry'
            state: 'idle', 'move_left', 'move_right', 'shoot', 'hit', or 'glow'

        Returns:
            pygame.Surface or None
        """
        if not USE_SPRITES:
            return None

        key = f"{hero_name.lower()}_{state}"
        path = HERO_SPRITES.get(key)
        if not path:
            return None
        return load_sprite(path)

    def get_hero_projectile_sprite(color, state="orb"):
        """Get hero projectile sprite.

        Args:
            color: 'green' (Tristan) or 'blue' (Henry)
            state: 'orb', 'glow', or 'trail'
        """
        if not USE_SPRITES:
            return None

        key = f"orb_{color}" if state == "orb" else f"orb_{color}_{state}"
        path = HERO_PROJECTILE_SPRITES.get(key)
        if not path:
            return None
        return load_sprite(path)

    def get_boss_sprite(phase, state):
        """Get boss sprite for current phase and state.

        Args:
            phase: 1, 2, or 3
            state: 'idle', 'attack', 'hit', 'aura', 'crown', 'eyes', etc.
        """
        if not USE_SPRITES:
            return None

        # Handle common elements that don't change by phase
        if state in ('crown', 'crown_glow', 'eyes', 'eyes_glow', 'shadow'):
            path = BOSS_SPRITES.get(state)
        elif state.startswith('death_anim'):
            path = BOSS_SPRITES.get(state)
        else:
            key = f"phase{phase}_{state}"
            path = BOSS_SPRITES.get(key)

        if not path:
            return None
        return load_sprite(path)

    def get_boss_projectile_sprite(proj_type, state="normal"):
        """Get boss projectile sprite.

        Args:
            proj_type: 'orb', 'spike', 'shadow_bolt', 'void_sphere'
            state: 'normal' or 'glow'
        """
        if not USE_SPRITES:
            return None

        if proj_type == "orb":
            key = "orb_dark" if state == "normal" else "orb_dark_glow"
        elif proj_type == "spike":
            key = "spike" if state == "normal" else "spike_glow"
        else:
            key = proj_type

        path = BOSS_PROJECTILE_SPRITES.get(key)
        if not path:
            return None
        return load_sprite(path)

    def get_hit_effect_sprite(effect_type, size=None):
        """Get hit/particle effect sprite."""
        if not USE_SPRITES:
            return None
        path = HIT_EFFECT_SPRITES.get(effect_type)
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

    def get_background_sprite(element, size=None):
        """Get background element sprite."""
        if not USE_SPRITES:
            return None
        path = BACKGROUND_SPRITES.get(element)
        if not path:
            return None
        return load_sprite(path, size)

    def get_attack_effect_sprite(attack_type, size=None):
        """Get attack warning/effect sprite."""
        if not USE_SPRITES:
            return None
        path = ATTACK_EFFECT_SPRITES.get(attack_type)
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
    # AUDIO CONFIGURATION - Sound effects for Boss Rush
    ####################################################################################################################

    USE_AUDIO = True  # Set to False to disable all minigame audio

    AUDIO_PATHS = {
        "boss_roar": "audio/sfx/minigames/bossrush/boss_roar.ogg",
        "boss_attack": "audio/sfx/minigames/bossrush/boss_attack.ogg",
        "boss_hit": "audio/sfx/minigames/bossrush/boss_hit.ogg",
        "phase_change": "audio/sfx/minigames/bossrush/phase_change.ogg",
        "boss_death": "audio/sfx/minigames/bossrush/boss_death.ogg",
        "hero_shoot": "audio/sfx/minigames/bossrush/hero_shoot.ogg",
        "hero_hit": "audio/sfx/minigames/bossrush/hero_hit.ogg",
        "projectile_fire": "audio/sfx/minigames/bossrush/projectile_fire.ogg",
        "projectile_hit": "audio/sfx/minigames/bossrush/projectile_hit.ogg",
        "spread_attack": "audio/sfx/minigames/bossrush/spread_attack.ogg",
        "rain_attack": "audio/sfx/minigames/bossrush/rain_attack.ogg",
        "spiral_attack": "audio/sfx/minigames/bossrush/spiral_attack.ogg",
        "victory": "audio/sfx/minigames/common/victory.ogg",
        "defeat": "audio/sfx/minigames/common/defeat.ogg",
        "game_start": "audio/sfx/minigames/common/game_start.ogg",
    }

    # Boss battle music by phase
    BOSS_MUSIC = {
        1: "audio/music/regions/boss_battle_intense.ogg",
        2: "audio/music/regions/boss_battle_phase2.ogg",
        3: "audio/music/regions/boss_battle_finale.ogg",
    }

    _audio_cache = {}
    _audio_initialized = False

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

    ####################################################################################################################
    # END AUDIO CONFIGURATION
    ####################################################################################################################

    # Game constants
    WIDTH, HEIGHT = 1920, 1080
    ARENA_MARGIN = 100

    # Game states
    STATE_INTRO = "intro"
    STATE_PLAYING = "playing"
    STATE_PHASE_TRANSITION = "phase_transition"
    STATE_VICTORY = "victory"
    STATE_GAMEOVER = "gameover"

    class HeroTwin:
        """One of the hero twins (Tristan or Henry)."""
        def __init__(self, name, x, color, keys):
            self.name = name
            self.x = x
            self.y = HEIGHT - 200
            self.width = 60
            self.height = 60
            self.color = color
            self.keys = keys  # {'left': key, 'right': key, 'shoot': key}

            self.health = 5
            self.max_health = 5
            self.speed = 8
            self.alive = True

            self.shoot_cooldown = 0
            self.shoot_delay = 300
            self.invulnerable = 0

            self.anim_phase = random.random() * math.pi * 2

        def update(self, dt, keys):
            if not self.alive:
                return []

            self.anim_phase += dt * 0.01

            if self.invulnerable > 0:
                self.invulnerable -= dt

            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= dt

            # Movement
            if keys[self.keys['left']]:
                self.x = max(ARENA_MARGIN, self.x - self.speed)
            if keys[self.keys['right']]:
                self.x = min(WIDTH - ARENA_MARGIN - self.width, self.x + self.speed)

            # Shooting
            projectiles = []
            if keys[self.keys['shoot']] and self.shoot_cooldown <= 0:
                self.shoot_cooldown = self.shoot_delay
                projectiles.append(HeroProjectile(
                    self.x + self.width // 2,
                    self.y,
                    self.color
                ))

            return projectiles

        def take_damage(self):
            if self.invulnerable <= 0 and self.alive:
                self.health -= 1
                self.invulnerable = 1500
                if self.health <= 0:
                    self.alive = False
                return True
            return False

        def get_rect(self):
            return pygame.Rect(self.x + 10, self.y + 10, self.width - 20, self.height - 20)

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            # Flash when invulnerable
            if self.invulnerable > 0 and (time_ms // 100) % 2 == 0:
                alpha = 100
            else:
                alpha = 255

            cx = self.x + self.width // 2
            cy = self.y + self.height // 2
            bob = math.sin(self.anim_phase) * 3

            # Glow
            glow_surf = pygame.Surface((self.width + 40, self.height + 40), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*self.color, 50), (self.width // 2 + 20, self.height // 2 + 20), 40)
            surf.blit(glow_surf, (self.x - 20, self.y + bob - 20))

            # Body
            body_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.circle(body_surf, (*self.color, alpha), (self.width // 2, self.height // 2), 25)

            # Helmet/visor
            pygame.draw.arc(body_surf, (255, 255, 255, alpha), (10, 15, 40, 30), 0.5, 2.6, 4)

            surf.blit(body_surf, (self.x, self.y + bob))

            # Name label
            font = pygame.font.Font(None, 24)
            name_text = font.render(self.name, True, self.color)
            surf.blit(name_text, (cx - name_text.get_width() // 2, self.y + self.height + 10))

    class HeroProjectile:
        """Projectile fired by heroes."""
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.speed = 15
            self.color = color
            self.radius = 10
            self.alive = True
            self.anim_phase = 0

        def update(self, dt):
            self.y -= self.speed
            self.anim_phase += dt * 0.02
            if self.y < 0:
                self.alive = False

        def get_rect(self):
            return pygame.Rect(self.x - self.radius, self.y - self.radius,
                             self.radius * 2, self.radius * 2)

        def draw(self, surf):
            if not self.alive:
                return

            # Trail
            for i in range(5):
                trail_y = self.y + i * 8
                trail_alpha = int(150 - i * 30)
                trail_size = self.radius - i
                if trail_size > 0:
                    trail_surf = pygame.Surface((trail_size * 2 + 4, trail_size * 2 + 4), pygame.SRCALPHA)
                    pygame.draw.circle(trail_surf, (*self.color, trail_alpha),
                                     (trail_size + 2, trail_size + 2), trail_size)
                    surf.blit(trail_surf, (self.x - trail_size - 2, trail_y - trail_size - 2))

            # Main projectile
            pygame.draw.circle(surf, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.radius - 3)

    class BossProjectile:
        """Projectile fired by the boss."""
        def __init__(self, x, y, angle, speed=6, proj_type="orb"):
            self.x = x
            self.y = y
            self.angle = angle
            self.speed = speed
            self.proj_type = proj_type
            self.alive = True
            self.radius = 15 if proj_type == "orb" else 10
            self.anim_phase = random.random() * math.pi * 2

        def update(self, dt):
            self.x += math.cos(self.angle) * self.speed
            self.y += math.sin(self.angle) * self.speed
            self.anim_phase += dt * 0.01

            # Check bounds
            if self.x < -50 or self.x > WIDTH + 50 or self.y < -50 or self.y > HEIGHT + 50:
                self.alive = False

        def get_rect(self):
            return pygame.Rect(self.x - self.radius + 5, self.y - self.radius + 5,
                             self.radius * 2 - 10, self.radius * 2 - 10)

        def draw(self, surf):
            if not self.alive:
                return

            pulse = 0.8 + 0.2 * math.sin(self.anim_phase)

            if self.proj_type == "orb":
                color = (150, 50, 200)
                glow_color = (180, 80, 220, 100)
            else:
                color = (200, 50, 100)
                glow_color = (220, 80, 120, 100)

            # Glow
            glow_size = int(self.radius * 1.5 * pulse)
            glow_surf = pygame.Surface((glow_size * 2 + 10, glow_size * 2 + 10), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, glow_color, (glow_size + 5, glow_size + 5), glow_size)
            surf.blit(glow_surf, (self.x - glow_size - 5, self.y - glow_size - 5))

            # Core
            pygame.draw.circle(surf, color, (int(self.x), int(self.y)), int(self.radius * pulse))
            pygame.draw.circle(surf, (255, 200, 255), (int(self.x), int(self.y)), int(self.radius * 0.4 * pulse))

    class ShadowKing:
        """The final boss - The Shadow King."""
        def __init__(self):
            self.x = WIDTH // 2
            self.y = 200
            self.width = 200
            self.height = 200

            self.max_health = 100
            self.health = self.max_health
            self.phase = 1  # 1, 2, or 3

            self.alive = True
            self.vulnerable = True
            self.hit_flash = 0

            # Movement
            self.base_y = 200
            self.move_phase = 0
            self.move_pattern = "hover"  # hover, sweep, charge

            # Attack patterns
            self.attack_timer = 0
            self.attack_cooldown = 2000
            self.current_attack = None
            self.attack_phase = 0

            # Visual
            self.anim_phase = 0
            self.eye_glow = 0
            self.crown_rotation = 0

            # Projectiles spawned by boss
            self.pending_projectiles = []

        def update(self, dt, heroes):
            if not self.alive:
                return []

            self.anim_phase += dt * 0.003
            self.crown_rotation += dt * 0.001
            self.move_phase += dt * 0.002

            if self.hit_flash > 0:
                self.hit_flash -= dt

            # Update phase based on health
            health_percent = self.health / self.max_health
            if health_percent <= 0.33:
                self.phase = 3
            elif health_percent <= 0.66:
                self.phase = 2
            else:
                self.phase = 1

            # Movement
            self.update_movement(dt)

            # Attack patterns
            self.attack_timer += dt
            attack_interval = 2500 - (self.phase - 1) * 500  # Faster attacks in later phases

            if self.attack_timer >= attack_interval:
                self.attack_timer = 0
                self.spawn_attack(heroes)

            # Return pending projectiles
            projectiles = self.pending_projectiles
            self.pending_projectiles = []
            return projectiles

        def update_movement(self, dt):
            # Hover movement
            self.y = self.base_y + math.sin(self.move_phase) * 30

            # Horizontal sweep in later phases
            if self.phase >= 2:
                sweep_range = 200 if self.phase == 2 else 300
                self.x = WIDTH // 2 + math.sin(self.move_phase * 0.7) * sweep_range

        def spawn_attack(self, heroes):
            """Spawn an attack pattern."""
            attack_type = random.choice(self.get_available_attacks())

            if attack_type == "spread":
                self.attack_spread()
            elif attack_type == "rain":
                self.attack_rain()
            elif attack_type == "spiral":
                self.attack_spiral()
            elif attack_type == "targeted":
                self.attack_targeted(heroes)

        def get_available_attacks(self):
            """Get attacks available for current phase."""
            attacks = ["spread", "targeted"]
            if self.phase >= 2:
                attacks.extend(["rain", "spread"])
            if self.phase >= 3:
                attacks.extend(["spiral", "rain"])
            return attacks

        def attack_spread(self):
            """Fire projectiles in a spread pattern."""
            num_projectiles = 5 + self.phase * 2
            spread_angle = math.pi * 0.6

            for i in range(num_projectiles):
                angle = math.pi / 2 + spread_angle * (i / (num_projectiles - 1) - 0.5)
                self.pending_projectiles.append(BossProjectile(
                    self.x, self.y + self.height // 2,
                    angle, speed=5 + self.phase
                ))

        def attack_rain(self):
            """Rain projectiles from above."""
            for _ in range(8 + self.phase * 3):
                x = random.randint(ARENA_MARGIN, WIDTH - ARENA_MARGIN)
                self.pending_projectiles.append(BossProjectile(
                    x, -20,
                    math.pi / 2,  # Straight down
                    speed=4 + self.phase,
                    proj_type="spike"
                ))

        def attack_spiral(self):
            """Fire projectiles in a spiral pattern."""
            num_arms = 3 + self.phase
            projectiles_per_arm = 4

            for arm in range(num_arms):
                base_angle = arm * (2 * math.pi / num_arms) + self.anim_phase
                for i in range(projectiles_per_arm):
                    angle = base_angle + i * 0.2
                    delay_offset = i * 0.1  # Stagger the projectiles
                    self.pending_projectiles.append(BossProjectile(
                        self.x, self.y + self.height // 2,
                        angle,
                        speed=4
                    ))

        def attack_targeted(self, heroes):
            """Fire projectiles at hero positions."""
            for hero in heroes:
                if hero.alive:
                    dx = hero.x + hero.width // 2 - self.x
                    dy = hero.y + hero.height // 2 - (self.y + self.height // 2)
                    angle = math.atan2(dy, dx)

                    # Fire multiple projectiles with slight spread
                    for offset in [-0.2, 0, 0.2]:
                        self.pending_projectiles.append(BossProjectile(
                            self.x, self.y + self.height // 2,
                            angle + offset,
                            speed=6
                        ))

        def take_damage(self, amount=1):
            if self.vulnerable:
                self.health -= amount
                self.hit_flash = 100
                if self.health <= 0:
                    self.alive = False
                    return True
            return False

        def get_rect(self):
            return pygame.Rect(self.x - self.width // 2 + 30, self.y + 30,
                             self.width - 60, self.height - 60)

        def draw(self, surf, time_ms):
            if not self.alive:
                return

            cx = self.x
            cy = self.y + self.height // 2

            # Shadow underneath
            shadow_surf = pygame.Surface((self.width + 40, 40), pygame.SRCALPHA)
            pygame.draw.ellipse(shadow_surf, (0, 0, 0, 80), shadow_surf.get_rect())
            surf.blit(shadow_surf, (cx - self.width // 2 - 20, HEIGHT - 300))

            # Determine colors based on phase
            if self.phase == 1:
                body_color = (80, 40, 120)
                glow_color = (120, 60, 180)
            elif self.phase == 2:
                body_color = (100, 30, 100)
                glow_color = (150, 50, 150)
            else:
                body_color = (120, 20, 80)
                glow_color = (180, 40, 120)

            # Hit flash
            if self.hit_flash > 0:
                body_color = (255, 200, 200)

            # Aura
            aura_pulse = 0.7 + 0.3 * math.sin(self.anim_phase)
            aura_size = int((self.width // 2 + 50) * aura_pulse)
            aura_surf = pygame.Surface((aura_size * 2 + 20, aura_size * 2 + 20), pygame.SRCALPHA)
            pygame.draw.circle(aura_surf, (*glow_color, 50), (aura_size + 10, aura_size + 10), aura_size)
            surf.blit(aura_surf, (cx - aura_size - 10, cy - aura_size - 10))

            # Main body (cloaked figure)
            body_points = [
                (cx, cy - 80),  # Top
                (cx - 70, cy + 60),  # Bottom left
                (cx, cy + 40),  # Bottom middle
                (cx + 70, cy + 60),  # Bottom right
            ]
            pygame.draw.polygon(surf, body_color, body_points)

            # Inner robe detail
            inner_points = [
                (cx, cy - 60),
                (cx - 40, cy + 30),
                (cx, cy + 20),
                (cx + 40, cy + 30),
            ]
            pygame.draw.polygon(surf, tuple(max(0, c - 30) for c in body_color), inner_points)

            # Crown
            crown_y = cy - 70
            crown_points = []
            for i in range(5):
                angle = -math.pi / 2 + i * math.pi / 4 - math.pi / 2 + self.crown_rotation * 0.5
                spike_len = 30 if i % 2 == 0 else 20
                crown_points.append((cx + math.cos(angle) * spike_len, crown_y + math.sin(angle) * spike_len - 10))

            pygame.draw.polygon(surf, (180, 150, 50), crown_points)
            pygame.draw.polygon(surf, (220, 200, 100), crown_points, 2)

            # Eyes
            eye_glow = int(150 + 100 * math.sin(self.anim_phase * 2))
            eye_color = (255, eye_glow, eye_glow)

            pygame.draw.circle(surf, eye_color, (int(cx - 20), int(cy - 20)), 12)
            pygame.draw.circle(surf, eye_color, (int(cx + 20), int(cy - 20)), 12)
            pygame.draw.circle(surf, (255, 255, 200), (int(cx - 20), int(cy - 20)), 5)
            pygame.draw.circle(surf, (255, 255, 200), (int(cx + 20), int(cy - 20)), 5)

            # Health bar
            bar_width = 400
            bar_height = 25
            bar_x = WIDTH // 2 - bar_width // 2
            bar_y = 50

            # Background
            pygame.draw.rect(surf, (40, 20, 60), (bar_x - 3, bar_y - 3, bar_width + 6, bar_height + 6), border_radius=5)

            # Fill
            fill_width = int(bar_width * (self.health / self.max_health))
            health_color = (100, 200, 100) if self.health > self.max_health * 0.5 else \
                          (255, 200, 50) if self.health > self.max_health * 0.25 else (255, 80, 80)

            if fill_width > 0:
                pygame.draw.rect(surf, health_color, (bar_x, bar_y, fill_width, bar_height), border_radius=3)

            # Border
            pygame.draw.rect(surf, (150, 100, 180), (bar_x - 3, bar_y - 3, bar_width + 6, bar_height + 6),
                           width=2, border_radius=5)

            # Phase indicator
            font = pygame.font.Font(None, 36)
            phase_text = font.render(f"SHADOW KING - Phase {self.phase}", True, (200, 180, 255))
            surf.blit(phase_text, (WIDTH // 2 - phase_text.get_width() // 2, 85))

    class HitEffect:
        """Effect when something is hit."""
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color
            self.lifetime = 300
            self.max_lifetime = 300
            self.particles = []

            for _ in range(8):
                angle = random.random() * math.pi * 2
                speed = random.uniform(2, 6)
                self.particles.append({
                    'x': x, 'y': y,
                    'vx': math.cos(angle) * speed,
                    'vy': math.sin(angle) * speed,
                    'size': random.uniform(3, 8)
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
                    ps = pygame.Surface((int(size * 2 + 4), int(size * 2 + 4)), pygame.SRCALPHA)
                    pygame.draw.circle(ps, (*self.color, alpha), (int(size + 2), int(size + 2)), int(size))
                    surf.blit(ps, (int(p['x'] - size), int(p['y'] - size)))

    class BossRushGame:
        """Main game controller for Boss Rush."""
        def __init__(self):
            self.state = STATE_INTRO
            self.intro_timer = 0

            # Heroes
            self.tristan = HeroTwin("Tristan", WIDTH // 2 - 150, (100, 200, 100),
                                   {'left': K_LEFT, 'right': K_RIGHT, 'shoot': K_UP})
            self.henry = HeroTwin("Henry", WIDTH // 2 + 90, (100, 150, 255),
                                 {'left': K_a, 'right': K_d, 'shoot': K_w})
            self.heroes = [self.tristan, self.henry]

            # Boss
            self.boss = ShadowKing()

            # Projectiles
            self.hero_projectiles = []
            self.boss_projectiles = []

            # Effects
            self.effects = []

            # Screen shake
            self.shake_amount = 0
            self.shake_timer = 0

        def trigger_shake(self, amount=5):
            self.shake_amount = max(self.shake_amount, amount)
            self.shake_timer = 200

        def update(self, dt):
            # Update shake
            if self.shake_timer > 0:
                self.shake_timer -= dt
                self.shake_amount *= 0.9
            else:
                self.shake_amount = 0

            # Update effects
            self.effects = [e for e in self.effects if e.update(dt)]

            if self.state == STATE_INTRO:
                self.intro_timer += dt
                if self.intro_timer >= 3000:
                    self.state = STATE_PLAYING
                return

            if self.state != STATE_PLAYING:
                return

            keys = pygame.key.get_pressed()

            # Update heroes
            for hero in self.heroes:
                new_projectiles = hero.update(dt, keys)
                self.hero_projectiles.extend(new_projectiles)

            # Update boss
            boss_projectiles = self.boss.update(dt, self.heroes)
            self.boss_projectiles.extend(boss_projectiles)

            # Update hero projectiles
            for proj in self.hero_projectiles:
                proj.update(dt)

                # Check collision with boss
                if proj.alive and self.boss.alive:
                    if proj.get_rect().colliderect(self.boss.get_rect()):
                        proj.alive = False
                        self.boss.take_damage(1)
                        self.effects.append(HitEffect(proj.x, proj.y, proj.color))
                        self.trigger_shake(3)

            self.hero_projectiles = [p for p in self.hero_projectiles if p.alive]

            # Update boss projectiles
            for proj in self.boss_projectiles:
                proj.update(dt)

                # Check collision with heroes
                if proj.alive:
                    for hero in self.heroes:
                        if hero.alive and proj.get_rect().colliderect(hero.get_rect()):
                            if hero.take_damage():
                                proj.alive = False
                                self.effects.append(HitEffect(hero.x + hero.width // 2,
                                                             hero.y + hero.height // 2, (255, 100, 100)))
                                self.trigger_shake(8)

            self.boss_projectiles = [p for p in self.boss_projectiles if p.alive]

            # Check win/lose
            if not self.boss.alive:
                self.state = STATE_VICTORY
            elif not any(h.alive for h in self.heroes):
                self.state = STATE_GAMEOVER

        def draw(self, surf):
            time_ms = pygame.time.get_ticks()

            # Calculate shake
            shake_x, shake_y = 0, 0
            if self.shake_amount > 0.5:
                shake_x = random.uniform(-self.shake_amount, self.shake_amount)
                shake_y = random.uniform(-self.shake_amount, self.shake_amount)

            # Create game surface
            game_surf = pygame.Surface((WIDTH, HEIGHT))

            # Background (dark sky with particles)
            self.draw_background(game_surf, time_ms)

            # Draw arena floor
            floor_y = HEIGHT - 150
            pygame.draw.rect(game_surf, (50, 40, 70), (0, floor_y, WIDTH, 150))
            pygame.draw.line(game_surf, (80, 60, 100), (0, floor_y), (WIDTH, floor_y), 3)

            # Draw boss
            self.boss.draw(game_surf, time_ms)

            # Draw boss projectiles
            for proj in self.boss_projectiles:
                proj.draw(game_surf)

            # Draw hero projectiles
            for proj in self.hero_projectiles:
                proj.draw(game_surf)

            # Draw heroes
            for hero in self.heroes:
                hero.draw(game_surf, time_ms)

            # Draw effects
            for effect in self.effects:
                effect.draw(game_surf)

            # Blit with shake
            surf.blit(game_surf, (shake_x, shake_y))

            # Draw UI (no shake)
            self.draw_ui(surf)

            # Draw intro
            if self.state == STATE_INTRO:
                self.draw_intro(surf)

            # Draw end screens
            if self.state == STATE_VICTORY:
                self.draw_victory(surf)
            elif self.state == STATE_GAMEOVER:
                self.draw_gameover(surf)

        def draw_background(self, surf, time_ms):
            """Draw dramatic background."""
            # Gradient sky
            for y in range(HEIGHT - 150):
                ratio = y / (HEIGHT - 150)
                r = int(20 + ratio * 20)
                g = int(10 + ratio * 15)
                b = int(40 + ratio * 20)
                pygame.draw.line(surf, (r, g, b), (0, y), (WIDTH, y))

            # Lightning flashes during later phases
            if self.boss.phase >= 2 and random.random() < 0.01:
                flash_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                flash_surf.fill((255, 255, 255, 30))
                surf.blit(flash_surf, (0, 0))

            # Floating particles
            random.seed(42)
            for _ in range(50):
                x = random.randint(0, WIDTH)
                base_y = random.randint(0, HEIGHT - 200)
                y = base_y + math.sin(time_ms * 0.001 + x * 0.01) * 20
                size = random.randint(1, 3)
                alpha = random.randint(50, 150)

                particle_surf = pygame.Surface((size * 2 + 2, size * 2 + 2), pygame.SRCALPHA)
                pygame.draw.circle(particle_surf, (150, 100, 200, alpha), (size + 1, size + 1), size)
                surf.blit(particle_surf, (x, y))
            random.seed()

        def draw_ui(self, surf):
            """Draw game UI."""
            font = pygame.font.Font(None, 32)

            # Hero health displays
            for i, hero in enumerate(self.heroes):
                x_offset = 50 if i == 0 else WIDTH - 250

                # Name
                name_text = font.render(hero.name, True, hero.color)
                surf.blit(name_text, (x_offset, HEIGHT - 90))

                # Hearts
                for h in range(hero.max_health):
                    heart_x = x_offset + h * 35
                    heart_y = HEIGHT - 60
                    color = (255, 100, 100) if h < hero.health else (60, 50, 80)

                    pygame.draw.circle(surf, color, (heart_x, heart_y), 10)
                    pygame.draw.circle(surf, color, (heart_x + 10, heart_y), 10)
                    pygame.draw.polygon(surf, color, [
                        (heart_x - 10, heart_y + 2),
                        (heart_x + 20, heart_y + 2),
                        (heart_x + 5, heart_y + 18)
                    ])

            # Controls hint
            controls = font.render("Tristan: Arrow Keys | Henry: WASD", True, (150, 140, 180))
            surf.blit(controls, (WIDTH // 2 - controls.get_width() // 2, HEIGHT - 40))

        def draw_intro(self, surf):
            """Draw boss intro."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

            # Fade based on timer
            alpha = max(0, 255 - int(self.intro_timer / 3000 * 255))
            overlay.fill((0, 0, 0, alpha))
            surf.blit(overlay, (0, 0))

            # Text
            if self.intro_timer < 2000:
                font_title = pygame.font.Font(None, 96)
                font_sub = pygame.font.Font(None, 48)

                title = font_title.render("THE SHADOW KING", True, (200, 100, 255))
                surf.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 50))

                if self.intro_timer > 1000:
                    sub = font_sub.render("Defeat the darkness!", True, (255, 255, 255))
                    surf.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 30))

        def draw_victory(self, surf):
            """Draw victory screen."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            surf.blit(overlay, (0, 0))

            font_title = pygame.font.Font(None, 96)
            font_sub = pygame.font.Font(None, 48)

            title = font_title.render("VICTORY!", True, (100, 255, 150))
            surf.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 100))

            sub1 = font_sub.render("The Shadow King is defeated!", True, (255, 255, 255))
            surf.blit(sub1, (WIDTH // 2 - sub1.get_width() // 2, HEIGHT // 2 - 20))

            sub2 = font_sub.render("Light returns to the realm!", True, (255, 220, 100))
            surf.blit(sub2, (WIDTH // 2 - sub2.get_width() // 2, HEIGHT // 2 + 30))

            prompt = font_sub.render("Press ENTER to continue", True, (180, 160, 220))
            surf.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 + 120))

        def draw_gameover(self, surf):
            """Draw game over screen."""
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 200))
            surf.blit(overlay, (0, 0))

            font_title = pygame.font.Font(None, 96)
            font_sub = pygame.font.Font(None, 48)

            title = font_title.render("DEFEATED", True, (255, 100, 100))
            surf.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 80))

            sub = font_sub.render("The shadows grow stronger...", True, (200, 150, 180))
            surf.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2))

            prompt = font_sub.render("Press ENTER to try again", True, (180, 160, 220))
            surf.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 + 80))


# Ren'Py Displayable wrapper
init python:
    class BossRushDisplayable(renpy.Displayable):
        """Ren'Py displayable wrapper for Boss Rush."""

        def __init__(self, **kwargs):
            super(BossRushDisplayable, self).__init__(**kwargs)
            self.game = None
            self.last_time = None

        def render(self, width, height, st, at):
            import pygame

            if self.game is None:
                self.game = boss_rush.BossRushGame()
                self.last_time = pygame.time.get_ticks()

            current_time = pygame.time.get_ticks()
            dt = current_time - self.last_time
            self.last_time = current_time

            self.game.update(dt)

            render = renpy.Render(boss_rush.WIDTH, boss_rush.HEIGHT)
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
                    if self.game.state == boss_rush.STATE_VICTORY:
                        return "victory"
                    elif self.game.state == boss_rush.STATE_GAMEOVER:
                        return "retry"

            return None

        def visit(self):
            return []


# Screen
screen boss_rush_screen():
    default game_display = BossRushDisplayable()

    add Solid("#140a28")
    add game_display

    key "K_ESCAPE" action Return("quit")


# Entry label
label boss_rush_start():
    $ quick_menu = False

    call screen boss_rush_screen()

    $ quick_menu = True
    $ result = _return

    if result == "victory":
        return True
    else:
        return False


# Test label
label test_boss_rush:
    "The final battle awaits..."
    "Tristan and Henry must work together to defeat the Shadow King!"

    call boss_rush_start()

    if _return:
        "The Shadow King has been vanquished!"
        "Light returns to the realm!"
    else:
        "The heroes will return stronger..."

    return
