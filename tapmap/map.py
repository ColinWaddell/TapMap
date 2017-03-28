from .codetoicon import GetClothingIcon, GetWeatherIcon
from .weatherdata import GetWeatherData
from .locations import LOCATIONS
import xml.etree.ElementTree as ET
import svgwrite

# The canvas we'll draw on and
# the size of the icons.
SCOTLAND_SVG = "tapmap/assets/map/scotland.svg"
I_WIDTH  = 75
I_HEIGHT = 75

def _GetSVGSize(filename):
    svg = ET.parse(filename)
    tree = svg.getroot()
    s2i = lambda s: int(''.join(map(str, [int(i) for i in s if i.isdigit()])))
    width = s2i(tree.get("width"))
    height = s2i(tree.get("height"))
    return (width, height)

def _BuildWeatherIcons(locations):
    icons = []
    for location in locations:
        try:
            weather = GetWeatherData(location["name"])
            forecast = GetWeatherIcon(weather["code"], weather["daytime"])
            icon = svgwrite.image.Image(
                        "tapmap/assets/symbols/weather/" + forecast + ".svg",
                        size=(I_WIDTH, I_HEIGHT),
                        insert=((location["x"]*C_WIDTH) - (I_WIDTH/2),
                                (location["y"]*C_HEIGHT) - (I_HEIGHT/2))
                    )
            icons.append(icon)
        except KeyError:
            pass

    return icons

def _BuildClothingIcons(locations):
    icons = []
    for location in locations:
        try:
            weather = GetWeatherData(location["name"])
            clothing = GetClothingIcon(weather["code"], weather["temp_c"])
            icon = svgwrite.image.Image(
                        "tapmap/assets/symbols/clothing/" + clothing + ".svg",
                        size=(I_WIDTH, I_HEIGHT),
                        insert=((location["x"]*C_WIDTH) - (I_WIDTH/2),
                                (location["y"]*C_HEIGHT) - (I_HEIGHT/2))
                    )
            icons.append(icon)
        except KeyError:
            pass

    return icons

def CreateClothingMap(filename, locations=LOCATIONS):
    # Scotland
    dwg = svgwrite.Drawing(filename, size=(C_WIDTH, C_HEIGHT))
    scotland = svgwrite.image.Image(SCOTLAND_SVG)
    dwg.add(scotland)
    overlay = _BuildClothingIcons(locations)
    [dwg.add(o) for o in overlay]
    dwg.save()


def CreateWeatherMap(filename, locations=LOCATIONS):
    # Scotland
    dwg = svgwrite.Drawing(filename, size=(C_WIDTH, C_HEIGHT))
    scotland = svgwrite.image.Image(SCOTLAND_SVG)
    dwg.add(scotland)
    overlay = _BuildWeatherIcons(locations)
    [dwg.add(o) for o in overlay]
    dwg.save()

# On load of this module find the
# size of the canvas for use later
(C_WIDTH, C_HEIGHT) = _GetSVGSize(SCOTLAND_SVG)
