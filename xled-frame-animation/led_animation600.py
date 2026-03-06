# led_animation.py
from xled_plus.samples.sample_setup import *

def good_to_bad_led(index):
    """Convert LED index from 'good' numbering to 'bad' numbering."""
    if index == 1:
        return 1
    elif index == 2:
        return 0
    elif 301 <= index <= 600:
        return index - 299
    elif 3 <= index <= 300:
        return 602 - index
    else:
        return -1


def bad_to_good_led(index):
    """Convert LED index from 'bad' numbering to 'good' numbering."""
    if index == 1:
        return 1
    elif index == 0:
        return 2
    elif 3 <= index <= 301:
        return index + 299
    elif 302 <= index <= 599:
        return 602 - index
    else:
        return -1


def prepare_frames(frames):
    """Convert a list of frames [(index, (r,g,b)), ...] into index and color arrays."""
    frames_indices = []
    frames_colors = []

    for frame in frames:
        frames_indices.append([good_to_bad_led(led[0]) for led in frame])
        frames_colors.append([led[1] for led in frame])

    return frames_indices, frames_colors


class GradientSequence2(Sequence):
    """Custom LED animation sequence."""
    def __init__(self, ctr, frames_indices, frames_colors, led_count=600, speed=1.0, folds=1.0, angle=0):
        self.frames_indices = frames_indices
        self.frames_colors = frames_colors
        self.led_count = led_count
        self.frame_counter = 0
        self.current_led = 1
        super(GradientSequence2, self).__init__(ctr, self.get_color, speed, folds, angle)

    def first_led_color_gradient(self, x):
        self.current_led += 1
        if self.current_led == self.led_count:
            self.current_led = 0
            self.frame_counter += 1
            print(self.frame_counter)

        frame_number = self.frame_counter - 1
        if 0 <= frame_number < len(self.frames_indices):
            if self.current_led in self.frames_indices[frame_number]:
                idx = self.frames_indices[frame_number].index(self.current_led)
                r, g, b = self.frames_colors[frame_number][idx]
                return rgb_color(r/255, g/255, b/255)

        return rgb_color(0, 0, 0)

    def get_color(self, x):
        return self.first_led_color_gradient(x)
