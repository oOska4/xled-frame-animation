# XLED Custom Animation Framework

Simple framework for running custom LED animations with the xled-plus library.

Works with Twinkly style LED controllers supported by xled-plus.

## Features

- Frame-based LED animation
- Works with any LED count
- Easy frame definition
- Fast playback
- Fully customizable LED mapping

## Important

Before using the animation you must manually map your LED layout.

Different LED strips / trees / installations have different physical LED orders.
Because of that you must create a mapping function that converts the logical LED
index to the physical LED index.

Example mapping function:

```python
def good_to_bad_led(index):
    if (1 <= index <= 197) or (198 <= index <= 200):
        return 202 - index
    if 201 <= index <= 398:
        return index + 1
    if index == 399:
        return 0
    if index == 400:
        return 1
    return -1
