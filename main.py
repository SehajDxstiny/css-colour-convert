import re
with open('testfiles/advanced.css') as f:
    css_file = f.read()

hex_match = re.compile(r'(?<=\#)([0-9a-fA-F]{3,8})(?=[;|\s])')
matches = hex_match.findall(css_file)

def hex_to_rgb(hex_color):
    hex_color = ''.join(c * 2 for c in hex_color) if len(hex_color) in (3, 4) else hex_color
    vals = [int(hex_color[i:i+2], 16) for i in range(0, len(hex_color), 2)]
    return f'rgb({vals[0]}, {vals[1]}, {vals[2]})' if len(vals) == 3 else f'rgba({vals[0]}, {vals[1]}, {vals[2]}, {round(vals[3]/255, 2)})'
   
for hex_color in matches:
    rgb_value = hex_to_rgb(hex_color)
    css_file = css_file.replace(f'#{hex_color};', f'{rgb_value};')

print(css_file)


