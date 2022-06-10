from django.shortcuts import render
import folium


def index(request):
    #Create maps object
    m = folium.Map(location=[19,-12], zoom_start=2)
    folium.Marker([5.594,-0.216], tooltip='Click for more',
    popup='SALVADOR MORENO \n Tel: 3144300548').add_to(m)
    #get HTML representation of map 
    m = m._repr_html_()
    context = {
        'm':m
    }

    return render(request, 'index.html', context)