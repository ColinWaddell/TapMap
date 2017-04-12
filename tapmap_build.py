from tapmap.map import CreateClothingMap, CreateWeatherMap
from subprocess import call
import sys

try:
    OUTDIR = sys.argv[1] + "/"
    print(OUTDIR)
except IndexError:
    OUTDIR = "./"

CreateClothingMap("/srv/www/taps-aff.co.uk/tapmap/taps_clothing.svg")
call(["convert", "-depth", "4", "/srv/www/taps-aff.co.uk/tapmap/taps_clothing.svg", OUTDIR+"taps_clothing.png"])

CreateWeatherMap("/srv/www/taps-aff.co.uk/tapmap/taps_weather.svg")
call(["convert", "-depth", "4", "/srv/www/taps-aff.co.uk/tapmap/taps_weather.svg", OUTDIR+"taps_weather.png"])
