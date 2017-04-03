from tapmap.map import CreateClothingMap, CreateWeatherMap
import cairosvg

CreateClothingMap("taps_clothing.svg")
cairosvg.svg2png(url="taps_clothing.svg", write_to="taps_clothing.png")

CreateWeatherMap("taps_weather.svg")
cairosvg.svg2png(url="taps_weather.svg", write_to="taps_weather.png")
