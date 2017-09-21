import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")
lat=data["LAT"]
lon=data["LON"]
el=data["ELEV"]
map=folium.Map(location=[39,-111])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<elevation<3000:
        return 'orange'
    else:
        return 'red'
fg=folium.FeatureGroup("Hi Map")
for i, j, z in zip(lat,lon,el):
    fg.add_child(folium.CircleMarker(location=[i,j], radius=6, popup=str(z)+" Elevation in Meters",
    fill_color=color_producer(z),color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 1000000 }))

map.add_child(fg)
map.save("Map1.html")
