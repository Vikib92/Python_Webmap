import folium
import pandas as pd

df1 = pd.read_csv("Volcanoes_USA.txt")
#from geopy.geocoders import Nominatim
#gv3 = Nominatim(user_agent="my-application", scheme = "https")
#df1['Coordinates'] = df1.Lat + df1.Lon
#df['Pos'] = df1.Coordinates.apply(gv3.geocode)

lat = list(df1.LAT)
lon = list(df1.LON)
elev = list(df1.ELEV)
nme = list(df1.NAME)

def det_cr(elev):
    if elev in range(0,1000):
        return 'green'
    elif elev in range(1000,3000):
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -90.09], tiles='Mapbox Bright', zoom_start=12)
fg = folium.FeatureGroup(name="Volcanoes")

for i,j,k,l in zip(lat,lon,nme,elev):
    fg.add_child(folium.CircleMarker(location=[i,j], radius=6, popup=folium.Popup(k, parse_html=True), 
                                     fill_color=det_cr(l), color='grey', fill_opacity=0.7))
#    fg.add_child(folium.CircleMarker(location=[i,j], popup=folium.Popup(k, parse_html=True), tooltip=folium.Icon(color=det_cr(l))))

fp = folium.FeatureGroup(name="Population")
    
fp.add_child(folium.GeoJson(data=open('world.json','r', encoding = 'utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    
map.add_child(fg)
map.add_child(fp)
map.add_child(folium.LayerControl())
map.save("webmap.html")