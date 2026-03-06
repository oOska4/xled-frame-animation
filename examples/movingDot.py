# run_example.py
from xled_plus.samples.sample_setup import *
from xled_frame_animation.led_animation600 import prepare_frames, GradientSequence2

led_count = 600

# Example: one frame for each LED with same color
frames = [[(i, (0, 255, 255))] for i in range(1, led_count + 1)]



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
