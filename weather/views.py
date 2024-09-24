from django.shortcuts import render, HttpResponse
import json
import requests # type: ignore


# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = ''
        list_of_data = requests.get(source.format(city)).json

        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate' : str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lan']),
            'temp': round((list_of_data['main']['temp']-32)*5.0/9.0,2),
            'humidity': str(list_of_data['main']['humidity'])                 
               }
    else:
        data ={}
    return render(request, 'home .html', data)