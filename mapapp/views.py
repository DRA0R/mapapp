from .models import Search
from .forms import SearchForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
import folium
import geocoder

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()

    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your address input is invalid')

    #Create maps object
    m = folium.Map(location=[19,-12], zoom_start=2)

    ##point marker yourself
    # folium.Marker([5.594,-0.216],
    #  tooltip='Click for more', popup='Ghana').add_to(m)

    folium.Marker([lat,lng],
     tooltip='Click for more', popup=country).add_to(m)
    #get HTML representation of map 
    m = m._repr_html_()
    context = {
        'm':m,
        'form':form,
    }

    return render(request, 'index.html', context)