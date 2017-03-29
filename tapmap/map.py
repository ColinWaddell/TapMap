from .codetoicon import GetClothingIcon, GetWeatherIcon
from .weatherdata import GetWeatherData
from .locations import LOCATIONS
import svgwrite

C_WIDTH  = 1123
C_HEIGHT = 1484
I_WIDTH  = 75
I_HEIGHT = 75


def _BuildWeatherIcons(locations):
    icons = []
    for location in locations:
        try:
            weather = GetWeatherData(location["name"])
            clothing = GetWeatherIcon(weather["code"], weather["daytime"])
            icon = svgwrite.image.Image(
                        "tapmap/assets/symbols/weather/" + clothing + ".svg",
                        size=(I_WIDTH, I_HEIGHT),
                        insert=((location["x"]*C_WIDTH) - (I_WIDTH/2), 
                                (location["y"]*C_HEIGHT) - (I_HEIGHT/2))
                    )
            icons.append(icon)
        except KeyError:
            break

    return icons

def _BuildClothingIcons(locations):
    icons = []
    for location in locations:
        try:
            print(location["name"])
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
            break

    return icons



def BuildClothingMap(filename, locations=LOCATIONS):
    # Scotland
    dwg = svgwrite.Drawing(filename, size=(C_WIDTH, C_HEIGHT))
    scotland = svgwrite.image.Image("tapmap/assets/map/scotland.svg")
    dwg.add(scotland)
    overlay = _BuildClothingIcons(locations)
    [dwg.add(o) for o in overlay]
    return dwg

def BuildWeatherMap(filename, locations=LOCATIONS):
    # Scotland
    dwg = svgwrite.Drawing(filename, size=(C_WIDTH, C_HEIGHT))
    scotland = svgwrite.image.Image("tapmap/assets/map/scotland.svg")
    dwg.add(scotland)
    overlay = _BuildWeatherIcons(locations)
    [dwg.add(o) for o in overlay]
    return dwg
