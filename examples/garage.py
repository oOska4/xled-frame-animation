# run_example.py
from xled_plus.samples.sample_setup import *
from xled_frame_animation.led_animation400led_animation400 import prepare_frames, GradientSequence2

led_count = 400


frames = []

start = 10
end = 61
center = (start + end) // 2
max_dist = max(center - start, end - center)
steps = max_dist  # steps from center to edges

# Forward animation: fill from center to edges
for step in range(steps + 1):
    frame = []
    green_blue = int(255 * (1 - step / steps))
    green_blue = max(0, green_blue)
    left = center - step
    right = center + step
    for led in range(start, end + 1):
        if left <= led <= right:
            frame.append((led, (255, green_blue, green_blue)))
    frames.append(frame)

# Backward animation: empty from edges to center
for step in range(steps - 1, -1, -1):
    frame = []
    green_blue = int(255 * (1 - step / steps))
    green_blue = max(0, green_blue)
    left = center - step
    right = center + step
    for led in range(start, end + 1):
        if left <= led <= right:
            frame.append((led, (255, green_blue, green_blue)))
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
