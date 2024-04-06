
import folium
import pandas as pd
import xlrd


# | Map Interface |
world_map = folium.Map(tiles="Cartodb dark_matter")


# | Creating the Features Layer |
volcanoes = folium.FeatureGroup(name="Volcanoes (US)")
population_map = folium.FeatureGroup(name="Population (GLOBE)")
cities = folium.FeatureGroup(name="Cities (TR)")
airports = folium.FeatureGroup(name="Airports (TR)")


# Data import
data_volcan = pd.read_excel("Volcanoes.xlsx")
data_city = pd.read_excel("TR-Cities.xlsx")
data_airports = pd.read_excel("Istanbul_Airports.xlsx")


# | Main Sets |

# Volcano
latitude1 = list(data_volcan["Latitude"])
longitude1 = list(data_volcan["Longitude"])
names1 = list(data_volcan["Names"])
volcan_types = list(data_volcan["Types"])


# City
latitude2 = list(data_city["Latitude"])
longitude2 = list(data_city["Longitude"])
names2 = list(data_city["Cities"])


# Airport

latitude3 = list(data_airports["Latitude"])
longitude3 = list(data_airports["Longitude"])
names3 = list(data_airports["Names"])


# | Layers |


# Volcano Layer

for lat1, long1, Name1, volcan_type in zip(latitude1, longitude1, names1, volcan_types):
    volcanoes.add_child(folium.Marker(location=(lat1, long1),
                                      icon=folium.Marker((lat1, long1)), popup=Name1 + volcan_type))


# City Layer

for lat2, long2, Name2 in zip(latitude2, longitude2, names2):
    cities.add_child(folium.Marker(location=(lat2, long2),
                                   icon=folium.Marker(location=(lat2, long2)), popup=Name2))


# Airport Layer

for lat3, long3, Name3 in zip(latitude3, longitude3, names3):
    airports.add_child(folium.Marker(location=(lat3, long3),
                                     icon=folium.Marker((lat3, long3)), popup=Name3))


population_map.add_child(folium.GeoJson(
                                data=(open("world.json", "r", encoding="utf-8-sig").read()),
                                style_function=lambda x: {'fillColor': 'white'
                                if x["properties"]["POP2005"] < 20000000 else 'green'
                                if 20000000 <= x["properties"]["POP2005"] <= 50000000 else 'orange'
                                if 50000000 <= x["properties"]["POP2005"] <= 100000000 else 'red'}))


# Adding Layers

world_map.add_child(volcanoes)
world_map.add_child(cities)
world_map.add_child(airports)
world_map.add_child(population_map)

world_map.add_child(folium.LayerControl())  # Layer Control

world_map.save("General_Map.html")  # End
