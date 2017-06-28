import folium #change python code to html javascript css
import pandas 
data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT']) ; lon = list(data['LON']); name = list(data['NAME']); elvation = list(data['ELEV'])
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38,-99],zoom_start=3,tiles='Mapbox Bright')
fg1 = folium.FeatureGroup(name='Volcanoes')
for lt, ln, n, e in zip(lat, lon, name, elvation):
    fg1.add_child(folium.CircleMarker(location=[lt, ln],popup=n + ' ' + str(e) + "m", fill_color=color_producer(e),color='gray',radius = 6))

fg2 = folium.FeatureGroup(name='Populations')
fg2.add_child(folium.GeoJson(data = open('world.json','r',encoding='utf-8-sig'), style_function = lambda x:{'fillColor': 
	'green' if x['properties']['POP2005'] < 10000000 
	else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
	else 'red'}))
    
map.add_child(fg1)
map.add_child(fg2)

map.add_child(folium.LayerControl())

map.save('Map.html')