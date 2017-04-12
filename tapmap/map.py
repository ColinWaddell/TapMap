from .codetoicon import GetClothingIcon, GetWeatherIcon
from .weatherdata import GetWeatherData
from .locations import LOCATIONS
import xml.etree.ElementTree as ET
from clint.textui import puts, indent, colored, progress
import svgwrite
import datetime
import os

# The canvas we'll draw on and
# the size of the icons.
PATH = os.path.dirname(os.path.realpath(__file__))
SCOTLAND_SVG = PATH + "/assets/map/scotland.svg"
I_WIDTH  = 50
I_HEIGHT = 50
RETRIES  = 3

def _longestName(locations):
    return len(max([l["name"] for l in locations], key=len))

def _GetSVGSize(filename):
    svg = ET.parse(filename)
    tree = svg.getroot()
    s2i = lambda s: int(''.join(map(str, [int(i) for i in s if i.isdigit()])))
    width = s2i(tree.get("width"))
    height = s2i(tree.get("height"))
    return (width, height)

def _BuildWeatherIcons(locations):
    icons = []
    label_len = _longestName(locations)+1
    print("Building Weather Icons:")
    with progress.Bar(label=" "*label_len, expected_size=len(locations)) as bar:
        for index, location in enumerate(locations):
            retries = RETRIES
            bar.show(index+1)
            name = location["name"]
            bar.label = name + " "*(label_len - len(name))
            while retries:
                try:
                    weather = GetWeatherData(name)
                    forecast = GetWeatherIcon(weather["code"], weather["daytime"])
                    icon = svgwrite.image.Image(
                                PATH + "/assets/symbols/weather/" + forecast + ".svg",
                                size=(I_WIDTH, I_HEIGHT),
                                insert=(round((location["x"]*C_WIDTH) - (I_WIDTH/2)),
                                        round((location["y"]*C_HEIGHT) - (I_HEIGHT/2)))
                            )
                    icons.append(icon)
                    break # No need to retry

                except KeyError:
                    print("WEATHER: Error retrieving " + name + ". Retries remaining: " + str(retries))
                    retries = retries - 1

    return icons



def _BuildClothingIcons(locations):
    icons = []
    label_len = _longestName(locations)+1
    print("Building Clothing Icons:")
    with progress.Bar(label=" "*label_len, expected_size=len(locations)) as bar:
        for index, location in enumerate(locations):
            retries = RETRIES
            bar.show(index+1)
            name = location["name"]
            bar.label = name + " "*(label_len - len(name))
            while retries:
                try:
                    weather = GetWeatherData(name)
                    clothing = GetClothingIcon(weather["code"], weather["temp_c"])
                    icon = svgwrite.image.Image(
                                PATH + "/assets/symbols/clothing/" + clothing + ".svg",
                                size=(I_WIDTH, I_HEIGHT),
                                insert=(round((location["x"]*C_WIDTH) - (I_WIDTH/2)),
                                        round((location["y"]*C_HEIGHT) - (I_HEIGHT/2)))
                            )
                    icons.append(icon)
                    break # No need to retry

                except KeyError:
                    print("CLOTHING: Error retrieving " + name + ". Retries remaining: " + str(retries))
                    retries = retries - 1

    return icons


def _CreateBaseMap(filename):
    # Scotland
    dwg = svgwrite.Drawing(filename, size=(C_WIDTH, C_HEIGHT))
    scotland = svgwrite.image.Image(SCOTLAND_SVG, size=(C_WIDTH, C_HEIGHT), insert=(0, 0))
    # Build time
    dt = datetime.datetime.now().strftime("%d/%m/%y %I:%M %p").lstrip("0").replace(" 0", " ")
    message = svgwrite.text.Text(dt, insert=(10, C_HEIGHT-10), style="font-size:20px; color: #ccc; font-family: Arial")
    dwg.add(scotland)
    dwg.add(message)
    return dwg


def CreateClothingMap(filename, locations=LOCATIONS):
    dwg = _CreateBaseMap(filename)
    overlay = _BuildClothingIcons(locations)
    [dwg.add(o) for o in overlay]
    dwg.save()


def CreateWeatherMap(filename, locations=LOCATIONS):
    if not locations:
        return

    dwg = _CreateBaseMap(filename)
    overlay = _BuildWeatherIcons(locations)
    [dwg.add(o) for o in overlay]
    dwg.save()

# On load of this module find the
# size of the canvas for use later
(C_WIDTH, C_HEIGHT) = _GetSVGSize(SCOTLAND_SVG)
