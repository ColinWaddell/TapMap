from tapmap.codetoicon import GetClothingIcon, GetWeatherIcon
import svgwrite

WIDTH=1123
HEIGHT=1484

locations = [
    {
        "title": "Glasgow",
        "x": 0.1,
        "y": 0.1,
    },
]



dwg = svgwrite.Drawing('test.svg', size=(WIDTH, HEIGHT))
scotland = svgwrite.image.Image("assets/map/scotland.svg")
overlay = [
    svgwrite.image.Image("assets/symbols/clothing/hoodie.svg", insert=(100,100), size=(30, 40))
]

dwg.add(scotland)
dwg.add(overlay[0])


dwg.save()
