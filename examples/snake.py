# run_example.py
from xled_plus.samples.sample_setup import *
from xled_frame_animation.led_animation400 import prepare_frames, GradientSequence2

led_count = 400


#Example: Moving sanake
snake_pattern = [
    (0, (12, 12, 12)),
    (1, (128, 128, 128)),
    (2, (255, 255, 255)),
    (3, (255, 255, 255)),
    (4, (255, 255, 255)),
    (5, (128, 128, 128)),
    (6, (12, 12, 12))
]

frames = []

for pos in list(range(1, led_count - 6 + 1)) + list(range(led_count - 6, 0, -1)):
    frame = []
    for offset, color in snake_pattern:
        led_index = pos + offset
        frame.append((led_index, color))
    frames.append(frame)



# Setup controller
ctr = setup_control()
ctr.set_mode("off")
ctr.adjust_layout_aspect(led_count)

# Prepare frames for animation
frames_indices, frames_colors = prepare_frames(frames)

# Launch animation
GradientSequence2(
    ctr,
    frames_indices,
    frames_colors,
    led_count=led_count,
    speed=8 / len(frames),  # Adjust speed based on frame count
    folds=0.8,
    angle=1
).launch_movie()

# Speed reference:
# speed = 4     -> 2 frame animation
# speed = 1     -> 8 frame animation
# speed = 0.1   -> 80 frame animation
# speed = 0.01334 -> 600 frame animation
