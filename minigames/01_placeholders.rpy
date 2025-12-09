# Procedural placeholder graphics for Beacon Quest minigame
# These are fallback renderers when sprite assets are not available
# File: minigames/01_placeholders.rpy

init python:
    import pygame
    import math

    # ================================================================
    # PROCEDURAL TILE RENDERING
    # These functions draw tiles when tileset images are not loaded
    # ================================================================

    def draw_procedural_floor(surf, px, py, tile_size, x, y):
        """Draw a procedural floor tile."""
        # Checkerboard pattern
        color = (60, 50, 80) if (x + y) % 2 == 0 else (55, 45, 75)
        pygame.draw.rect(surf, color, (px, py, tile_size, tile_size))
        pygame.draw.rect(surf, (70, 60, 90), (px, py, tile_size, tile_size), 1)

    def draw_procedural_wall(surf, px, py, tile_size):
        """Draw a procedural wall tile."""
        # Main wall body
        pygame.draw.rect(surf, (80, 70, 100), (px, py, tile_size, tile_size))
        # Brick-like detail
        pygame.draw.rect(surf, (100, 90, 120), (px + 4, py + 4, tile_size - 8, tile_size - 16))
        # Border
        pygame.draw.rect(surf, (60, 50, 80), (px, py, tile_size, tile_size), 2)

    def draw_procedural_beacon(surf, px, py, tile_size, time_ms, is_active):
        """Draw a procedural beacon/goal tile."""
        # Floor underneath
        pygame.draw.rect(surf, (60, 50, 80), (px, py, tile_size, tile_size))

        # Glowing beacon effect
        glow = 0.5 + 0.3 * math.sin(time_ms * 0.003)
        glow_size = int(40 + 15 * glow)

        if is_active:
            glow_color = (255, 220, 100, int(150 * glow))
            beacon_color = (255, 240, 150)
        else:
            glow_color = (100, 80, 150, int(80 * glow))
            beacon_color = (150, 130, 180)

        glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, glow_color, (glow_size, glow_size), glow_size)
        surf.blit(glow_surf, (px + tile_size // 2 - glow_size, py + tile_size // 2 - glow_size))

        pygame.draw.circle(surf, beacon_color, (px + tile_size // 2, py + tile_size // 2), 15)

    def draw_procedural_door(surf, px, py, tile_size, direction, time_ms):
        """Draw a procedural door/portal tile."""
        # Floor underneath
        pygame.draw.rect(surf, (50, 40, 70), (px, py, tile_size, tile_size))

        # Glowing portal
        glow = 0.6 + 0.3 * math.sin(time_ms * 0.004)
        center_x = px + tile_size // 2
        center_y = py + tile_size // 2

        # Outer glow
        glow_surf = pygame.Surface((tile_size + 20, tile_size + 20), pygame.SRCALPHA)
        pygame.draw.ellipse(glow_surf, (100, 200, 255, int(60 * glow)),
                          (0, 0, tile_size + 20, tile_size + 20))
        surf.blit(glow_surf, (px - 10, py - 10))

        # Inner portal
        pygame.draw.ellipse(surf, (80, 150, 200), (px + 8, py + 8, tile_size - 16, tile_size - 16))
        pygame.draw.ellipse(surf, (150, 220, 255), (px + 14, py + 14, tile_size - 28, tile_size - 28))

        # Direction indicator (arrow)
        arrow_color = (200, 240, 255)
        if direction == 'N':
            pygame.draw.polygon(surf, arrow_color, [(center_x, py + 18), (center_x - 8, py + 30), (center_x + 8, py + 30)])
        elif direction == 'S':
            pygame.draw.polygon(surf, arrow_color, [(center_x, py + tile_size - 18), (center_x - 8, py + tile_size - 30), (center_x + 8, py + tile_size - 30)])
        elif direction == 'E':
            pygame.draw.polygon(surf, arrow_color, [(px + tile_size - 18, center_y), (px + tile_size - 30, center_y - 8), (px + tile_size - 30, center_y + 8)])
        elif direction == 'W':
            pygame.draw.polygon(surf, arrow_color, [(px + 18, center_y), (px + 30, center_y - 8), (px + 30, center_y + 8)])


    # ================================================================
    # PROCEDURAL ENEMY RENDERING
    # These functions draw enemies when sprite assets are not loaded
    # ================================================================

    def draw_procedural_slime(surf, screen_x, screen_y, width, height, anim_phase, is_dying, death_timer):
        """Draw a procedural slime enemy."""
        # Slime colors (green/teal)
        body_color = (50, 180, 80)
        highlight_color = (100, 220, 130)

        # Jiggly animation
        jiggle = math.sin(anim_phase * 3) * 3
        squash = 1 + math.sin(anim_phase * 2) * 0.1

        # Death fade
        alpha = 255
        if is_dying:
            alpha = max(0, 255 - int(death_timer * 0.5))

        # Shadow
        shadow_surf = pygame.Surface((width, 16), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (0, 0, 0, 50), shadow_surf.get_rect())
        surf.blit(shadow_surf, (screen_x, screen_y + height - 12))

        # Body - blobby ellipse with squash/stretch
        body_w = int(width * squash)
        body_h = int(height * 0.7 / squash)
        body_x = screen_x + (width - body_w) // 2
        body_y = screen_y + height - body_h - 5 + int(jiggle)

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
            pygame.draw.circle(surf, (20, 20, 20), (int(screen_x + width // 2 - eye_spacing), int(eye_y)), 5)
            pygame.draw.circle(surf, (255, 255, 255), (int(screen_x + width // 2 - eye_spacing - 1), int(eye_y - 1)), 2)
            # Right eye
            pygame.draw.circle(surf, (20, 20, 20), (int(screen_x + width // 2 + eye_spacing), int(eye_y)), 5)
            pygame.draw.circle(surf, (255, 255, 255), (int(screen_x + width // 2 + eye_spacing - 1), int(eye_y - 1)), 2)


    def draw_procedural_vampire(surf, screen_x, screen_y, width, height, anim_phase, facing, is_dying, death_timer):
        """Draw a procedural vampire enemy."""
        # Color scheme (dark purple/black with red accents)
        body_color = (40, 30, 50)
        cape_color = (120, 20, 30)

        # Floating/hovering animation
        hover = math.sin(anim_phase * 2) * 4
        cape_flow = math.sin(anim_phase * 3) * 5

        # Death fade
        alpha = 255
        if is_dying:
            alpha = max(0, 255 - int(death_timer * 0.3))

        # Shadow (smaller, vampire floats)
        shadow_surf = pygame.Surface((width - 20, 12), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (0, 0, 0, 40), shadow_surf.get_rect())
        surf.blit(shadow_surf, (screen_x + 10, screen_y + height - 8))

        # Cape (flowing behind)
        cape_points = [
            (screen_x + width // 2, int(screen_y + 15 + hover)),
            (int(screen_x + 8 + cape_flow), screen_y + height - 5),
            (screen_x + width // 2, screen_y + height - 15),
            (int(screen_x + width - 8 - cape_flow), screen_y + height - 5),
        ]
        cape_surf = pygame.Surface((width + 20, height + 10), pygame.SRCALPHA)
        adjusted_cape = [(int(p[0] - screen_x + 10), int(p[1] - screen_y + 5)) for p in cape_points]
        pygame.draw.polygon(cape_surf, (*cape_color[:3], alpha), adjusted_cape)
        surf.blit(cape_surf, (screen_x - 10, screen_y - 5))

        # Body (dark humanoid shape)
        body_surf = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.ellipse(body_surf, (*body_color[:3], alpha),
                          (15, 10, width - 30, height - 25))
        surf.blit(body_surf, (screen_x, screen_y + int(hover)))

        # Head
        head_y = screen_y + 5 + hover
        pygame.draw.circle(surf, (*body_color[:3], alpha) if alpha == 255 else body_color,
                         (int(screen_x + width // 2), int(head_y + 10)), 12)

        # Glowing red eyes
        if alpha > 100:
            eye_y = head_y + 8
            glow_size = 3 + int(math.sin(anim_phase * 4) * 1)
            pygame.draw.circle(surf, (255, 50, 50), (int(screen_x + width // 2 - 6), int(eye_y)), glow_size + 2)
            pygame.draw.circle(surf, (255, 150, 150), (int(screen_x + width // 2 - 6), int(eye_y)), glow_size)
            pygame.draw.circle(surf, (255, 50, 50), (int(screen_x + width // 2 + 6), int(eye_y)), glow_size + 2)
            pygame.draw.circle(surf, (255, 150, 150), (int(screen_x + width // 2 + 6), int(eye_y)), glow_size)

            # Fangs
            fang_y = int(head_y + 16)
            pygame.draw.polygon(surf, (255, 255, 255), [
                (screen_x + width // 2 - 4, fang_y),
                (screen_x + width // 2 - 2, fang_y + 5),
                (screen_x + width // 2 - 6, fang_y)
            ])
            pygame.draw.polygon(surf, (255, 255, 255), [
                (screen_x + width // 2 + 4, fang_y),
                (screen_x + width // 2 + 2, fang_y + 5),
                (screen_x + width // 2 + 6, fang_y)
            ])


    def draw_procedural_orc(surf, screen_x, screen_y, width, height, anim_phase, is_dying, death_timer):
        """Draw a procedural orc enemy."""
        # Color scheme (green/brown for orc)
        skin_color = (80, 120, 60)
        armor_color = (80, 60, 40)

        # Subtle breathing animation
        breathe = math.sin(anim_phase * 1.5) * 2

        # Death fade
        alpha = 255
        if is_dying:
            alpha = max(0, 255 - int(death_timer * 0.35))

        # Shadow (larger for bulky orc)
        shadow_surf = pygame.Surface((width, 18), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (0, 0, 0, 55), shadow_surf.get_rect())
        surf.blit(shadow_surf, (screen_x, screen_y + height - 12))

        # Body (bulky torso)
        body_surf = pygame.Surface((width, height), pygame.SRCALPHA)

        # Armor/chest plate
        pygame.draw.ellipse(body_surf, (*armor_color[:3], alpha), (12, int(18 + breathe), width - 24, 30))

        # Arms (thick)
        pygame.draw.ellipse(body_surf, (*skin_color[:3], alpha), (4, int(20 + breathe), 14, 28))
        pygame.draw.ellipse(body_surf, (*skin_color[:3], alpha), (width - 18, int(20 + breathe), 14, 28))

        # Legs
        pygame.draw.ellipse(body_surf, (*armor_color[:3], alpha), (15, 42, 12, 20))
        pygame.draw.ellipse(body_surf, (*armor_color[:3], alpha), (width - 27, 42, 12, 20))

        surf.blit(body_surf, (screen_x, screen_y))

        # Head (large and brutish)
        head_y = screen_y + 5 + breathe
        head_surf = pygame.Surface((36, 28), pygame.SRCALPHA)
        pygame.draw.ellipse(head_surf, (*skin_color[:3], alpha), (0, 0, 36, 28))
        surf.blit(head_surf, (screen_x + width // 2 - 18, int(head_y)))

        if alpha > 100:
            # Angry eyes
            eye_y = head_y + 10
            pygame.draw.ellipse(surf, (200, 50, 50), (screen_x + width // 2 - 10, int(eye_y), 6, 5))
            pygame.draw.ellipse(surf, (200, 50, 50), (screen_x + width // 2 + 4, int(eye_y), 6, 5))
            pygame.draw.circle(surf, (0, 0, 0), (int(screen_x + width // 2 - 7), int(eye_y + 2)), 2)
            pygame.draw.circle(surf, (0, 0, 0), (int(screen_x + width // 2 + 7), int(eye_y + 2)), 2)

            # Tusks
            tusk_y = int(head_y + 20)
            pygame.draw.polygon(surf, (230, 220, 200), [
                (screen_x + width // 2 - 12, tusk_y),
                (screen_x + width // 2 - 8, tusk_y + 8),
                (screen_x + width // 2 - 14, tusk_y + 3)
            ])
            pygame.draw.polygon(surf, (230, 220, 200), [
                (screen_x + width // 2 + 12, tusk_y),
                (screen_x + width // 2 + 8, tusk_y + 8),
                (screen_x + width // 2 + 14, tusk_y + 3)
            ])


    def draw_procedural_spider(surf, screen_x, screen_y, width, height, anim_phase, is_dying, death_timer):
        """Draw a procedural spider enemy."""
        # Color scheme (dark brown/black)
        body_color = (50, 35, 30)
        leg_color = (70, 50, 40)

        # Leg animation based on movement
        leg_phase = anim_phase * 8

        # Death fade
        alpha = 255
        if is_dying:
            alpha = max(0, 255 - int(death_timer * 0.6))

        # Shadow
        shadow_surf = pygame.Surface((width - 16, 10), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (0, 0, 0, 35), shadow_surf.get_rect())
        surf.blit(shadow_surf, (screen_x + 8, screen_y + height - 8))

        center_x = screen_x + width // 2
        center_y = screen_y + height // 2

        # Draw 8 legs (4 on each side)
        leg_length = 18
        leg_angles_left = [150, 170, 190, 210]
        leg_angles_right = [30, 10, -10, -30]

        for i, angle in enumerate(leg_angles_left):
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
        pygame.draw.ellipse(surf, body_color, (center_x - 14, center_y - 2, 28, 22))

        # Cephalothorax (front body - smaller)
        pygame.draw.ellipse(surf, body_color, (center_x - 10, center_y - 16, 20, 18))

        # Eyes (multiple small eyes in a cluster)
        if alpha > 100:
            eye_y = center_y - 12
            # Main eyes
            pygame.draw.circle(surf, (150, 20, 20), (int(center_x - 5), int(eye_y)), 3)
            pygame.draw.circle(surf, (150, 20, 20), (int(center_x + 5), int(eye_y)), 3)
            # Secondary eyes
            pygame.draw.circle(surf, (120, 20, 20), (int(center_x - 8), int(eye_y - 5)), 2)
            pygame.draw.circle(surf, (120, 20, 20), (int(center_x + 8), int(eye_y - 5)), 2)
            # Tiny eyes
            pygame.draw.circle(surf, (100, 15, 15), (int(center_x - 3), int(eye_y - 7)), 1)
            pygame.draw.circle(surf, (100, 15, 15), (int(center_x + 3), int(eye_y - 7)), 1)
            # Eye shine
            pygame.draw.circle(surf, (255, 200, 200), (int(center_x - 4), int(eye_y - 1)), 1)
            pygame.draw.circle(surf, (255, 200, 200), (int(center_x + 6), int(eye_y - 1)), 1)
            # Fangs
            pygame.draw.line(surf, (80, 60, 50), (center_x - 4, center_y - 6), (center_x - 6, center_y), 2)
            pygame.draw.line(surf, (80, 60, 50), (center_x + 4, center_y - 6), (center_x + 6, center_y), 2)


    # ================================================================
    # PROCEDURAL CHARACTER RENDERING (base Enemy class fallback)
    # ================================================================

    def draw_procedural_enemy(surf, screen_x, screen_y, width, height, anim_phase, hit_flash):
        """Draw a generic procedural enemy (shadowy blob)."""
        if hit_flash > 0:
            color = (255, 200, 200)
        else:
            color = (80, 50, 100)

        bob = math.sin(anim_phase) * 3

        # Shadow
        shadow_surf = pygame.Surface((width, 20), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (0, 0, 0, 60), shadow_surf.get_rect())
        surf.blit(shadow_surf, (screen_x, screen_y + height - 5))

        # Body (shadowy blob)
        body_surf = pygame.Surface((width + 10, height + 10), pygame.SRCALPHA)
        pygame.draw.ellipse(body_surf, (100, 50, 130, 100), (0, 0, width + 10, height + 10))
        pygame.draw.ellipse(body_surf, color, (5, 5, width, height - 5))
        surf.blit(body_surf, (screen_x - 5, screen_y + bob - 5))

        # Evil eyes
        eye_y = screen_y + height // 3 + bob
        pygame.draw.circle(surf, (255, 100, 100), (int(screen_x + 15), int(eye_y)), 6)
        pygame.draw.circle(surf, (255, 100, 100), (int(screen_x + width - 15), int(eye_y)), 6)
        pygame.draw.circle(surf, (255, 200, 200), (int(screen_x + 15), int(eye_y)), 3)
        pygame.draw.circle(surf, (255, 200, 200), (int(screen_x + width - 15), int(eye_y)), 3)
