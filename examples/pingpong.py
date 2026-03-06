# run_example.py
from xled_plus.samples.sample_setup import *
from xled_frame_animation.led_animation400 import prepare_frames, GradientSequence2

led_count = 400

#Example: Ping-pong animation from LED 1 to 400 and back to 1
frames = [[(i, (0, 255, 0))] for i in range(1, led_count + 1)] \
       + [[(i, (0, 255, 0))] for i in range(led_count - 1, 0, -1)]



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
