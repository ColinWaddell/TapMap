from tapmap.map import CreateClothingMap, CreateWeatherMap
import cairosvg

OUTDIR = "/srv/www/taps-aff.co.uk/public_html/public/maps/"

CreateClothingMap("taps_clothing.svg")
cairosvg.svg2png(url="taps_clothing.svg", write_to=OUTDIR+"taps_clothing.png")

CreateWeatherMap("taps_weather.svg")
cairosvg.svg2png(url="taps_weather.svg", write_to=OUTDIR+"taps_weather.png")
