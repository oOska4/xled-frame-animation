import time
import math
from xled_frame_animation.led_animation400 import prepare_frames, GradientSequence2
from xled_plus.samples.sample_setup import rgb_color

# ANSI escape codes for colors in console
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m█\033[0m"


def preview_animation(frames, led_count=400, delay=0.02, row_length=50):
    """
    Console preview of LED frames with colored blocks, wrapped into multiple rows.
    """
    frames_indices, frames_colors = prepare_frames(frames)
    
    for frame_number in range(len(frames_indices)):
        line = ""
        for led_idx in range(led_count):
            if led_idx in frames_indices[frame_number]:
                idx = frames_indices[frame_number].index(led_idx)
                r, g, b = frames_colors[frame_number][idx]
                line += rgb_to_ansi(r, g, b)
            else:
                line += " "
            # wrap line
            if (led_idx + 1) % row_length == 0:
                line += "\n"
        print(line)
        time.sleep(delay)
        print("\033[F" * math.ceil(led_count / row_length), end="")  # move cursor up

# Example usage
if __name__ == "__main__":
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


preview_animation(frames, led_count=led_count, delay=0.05)
