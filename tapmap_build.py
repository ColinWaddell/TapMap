from tapmap.map import CreateClothingMap, CreateWeatherMap
from subprocess import call
import sys

try:
    OUTDIR = sys.argv[1] + "/"
    print(OUTDIR)
except IndexError:
    OUTDIR = "./"

CreateClothingMap("/srv/www/taps-aff.co.uk/tapmap/taps_clothing.svg")
CreateWeatherMap("/srv/www/taps-aff.co.uk/tapmap/taps_weather.svg")
