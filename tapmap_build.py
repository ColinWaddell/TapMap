from tapmap.map import CreateClothingMap, CreateWeatherMap
import cairosvg
import sys

try:
    OUTDIR = sys.argv[1] + "/"
    print(OUTDIR)
except IndexError:
    OUTDIR = "./"

CreateClothingMap(OUTDIR+"taps_clothing.svg")
cairosvg.svg2png(url=OUTDIR+"taps_clothing.svg", write_to=OUTDIR+"taps_clothing.png")

CreateWeatherMap(OUTDIR+"taps_weather.svg")
cairosvg.svg2png(url=OUTDIR+"taps_weather.svg", write_to=OUTDIR+"taps_weather.png")
