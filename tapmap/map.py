from .codetoicon import GetClothingIcon, GetWeatherIcon
from .weatherdata import GetWeatherData
from .locations import LOCATIONS
import xml.etree.ElementTree as ET
import svgwrite

SCOTLAND_SVG = "tapmap/assets/map/scotland.svg"
I_WIDTH  = 75
I_HEIGHT = 75

def _StringToInt(s):
    x = [int(i) for i in s if i.isdigit()]
    return int(''.join(map(str,x)))


def _GetSVGSize(filename):
    svg = ET.parse()
    tree = svg.getroot(SCOTLAND_SVG)
    width = _StringToInt(tree.get("width"))
    height = _StringToInt(tree.get("height"))
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
            clothing = GetClothingIcon(weather["code"], weather["temp_f"])
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

(C_WIDTH, C_HEIGHT) = _GetSVGSize(SCOTLAND_SVG)
