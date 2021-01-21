# -*- coding: utf-8 -*-
import folium
import webbrowser
from geopy.geocoders import Nominatim

 
ville = "92400"
adresse = "12 Avenue Léonard de Vinci 92400"

geolocator = Nominatim()
coord_ville = geolocator.geocode(ville) #récupère les coordonnées latitude longitude de la ville
coord_adresse = geolocator.geocode(adresse) #récupère les coordonnées latitude longitude de l'adresse

carte= folium.Map(location=[coord_ville.latitude, coord_ville.longitude],zoom_start=15) #ouvre la carte directement sur la ville avec un zoom
folium.Marker([coord_adresse.latitude, coord_adresse.longitude],popup=adresse).add_to(carte) #place un point sur l'adresse

carte.save('Carte.html') #enregistre la carte
webbrowser.open('Carte.html') #ouvre la carte sur le navigateur 