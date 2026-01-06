input_ppm = "graycode.ppm"
output_txt = "rafael_nadal.txt"
brightness_map = [
    (230, ' '),
    (210, '.'),
    (190, ':'),
    (170, '-'),
    (150, '='),
    (120, '+'),
    (90, '*'),
    (60, '#'),
    (30, '%'),
    (0, '@')
]

def brightness_to_char(value):
    for threshold, char in brightness_map:
        if value >= threshold:
            return char
    return '@'

with open(input_ppm, "r") as f:
    lines = f.readlines()
data = []
for line in lines:
    line = line.strip()
    if not line.startswith("#") and line:
        data.extend(line.split())

assert data[0] == "P3", "Not a P3 PPM file"

width = int(data[1])
height = int(data[2])
max_val = int(data[3])

pixel_data = data[4:]

ascii_lines = []
idx = 0
for _ in range(height):
    line_chars = []
    for _ in range(width):
        r = int(pixel_data[idx])
        g = int(pixel_data[idx + 1])
        b = int(pixel_data[idx + 2])
        idx += 3
        brightness = (r + g + b) // 3
        line_chars.append(brightness_to_char(brightness))
    ascii_lines.append("".join(line_chars))

with open(output_txt, "w") as f:
    f.write("\n".join(ascii_lines))

print(f"ASCII art decoded and written to {output_txt}")
