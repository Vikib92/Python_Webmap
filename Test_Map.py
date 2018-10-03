import folium
import pandas as pd

df1 = pd.read_csv("supermarkets.csv")
df1 = df1.set_index("ID")

from geopy.geocoders import Nominatim
gv3 = Nominatim(user_agent="my-application", scheme = "https")
#cas = gv3.geocode("332 Hill St, San Francisco, California 94114, USA")
df1['Address'] = df1.Address + ', ' + df1.City + ', ' + df1.State + ', ' + df1.Country
df1['Coordinates'] = df1.Address.apply(gv3.geocode)
#df1.Coordinates[1].latitude
#df1['Latitute'] = df1.Coordinates.latitude
df1['Latitude'] = df1.Coordinates.apply(lambda x: x.latitude if x != None else None)
df1['Longitude'] = df1.Coordinates.apply(lambda x: x.longitude if x != None else None)

map = folium.Map(location=[38.58, -90.09], tiles='Stamen Terrain', zoom_start=6)
fg = folium.FeatureGroup(name="My Map")

for a,b,c in zip(df1.Latitude, df1.Longitude, df1.City):
    if (str(a) != "nan") and (str(b) != "nan"):
        fg.add_child(folium.Marker([a, b], popup=folium.Popup(c, parse_html=True), icon=folium.Icon(color='red')))        

#folium.Marker([48.58, -90.09], popup='Test_Lcc', icon=folium.Icon(color='blue')).add_to(fg)

map.add_child(fg)
map.save("testmap.html")

