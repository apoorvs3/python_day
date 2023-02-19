import colorgram

colors = colorgram.extract('delorazepam.jpg', 100)


def extract_colors():
    ls = []
    for color in colors:
        rgb = color.rgb
        red = color.rgb.r
        blue = color.rgb.b
        green = color.rgb.b
        ls.append((red, green, blue))
    print(len(ls))
    return ls
