from .codetoicon import GetClothingIcon, GetWeatherIcon
from .weatherdata import GetWeatherData
from .locations import LOCATIONS
import xml.etree.ElementTree as ET
import svgwrite
import os

# The canvas we'll draw on and
# the size of the icons.
PATH = os.getcwd()
SCOTLAND_SVG = PATH + "/tapmap/assets/map/scotland.svg"
I_WIDTH  = 100
I_HEIGHT = 100

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
                        PATH + "/tapmap/assets/symbols/weather/" + forecast + ".svg",
                        size=(I_WIDTH, I_HEIGHT),
                        insert=((location["x"]*C_WIDTH)  - (I_WIDTH/2),
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
                        PATH + "/tapmap/assets/symbols/clothing/" + clothing + ".svg",
                        size=(I_WIDTH, I_HEIGHT),
                        insert=((location["x"]*C_WIDTH) - (I_WIDTH/2),
                                (location["y"]*C_HEIGHT) - (I_HEIGHT/2))
                    )
            icons.append(icon)
        except KeyError:
            pass

    return icons


def _CreateBaseMap(filename):
    # Scotland
    dwg = svgwrite.Drawing(filename, size=(C_WIDTH, C_HEIGHT))
    scotland = svgwrite.image.Image(SCOTLAND_SVG, size=(C_WIDTH, C_HEIGHT), insert=(0, 0))
    dwg.add(scotland)
    return dwg


def CreateClothingMap(filename, locations=LOCATIONS):
    dwg = _CreateBaseMap(filename)
    overlay = _BuildClothingIcons(locations)
    [dwg.add(o) for o in overlay]
    dwg.save()


def CreateWeatherMap(filename, locations=LOCATIONS):
    dwg = _CreateBaseMap(filename)
    overlay = _BuildWeatherIcons(locations)
    [dwg.add(o) for o in overlay]
    dwg.save()

# On load of this module find the
# size of the canvas for use later
(C_WIDTH, C_HEIGHT) = _GetSVGSize(SCOTLAND_SVG)
