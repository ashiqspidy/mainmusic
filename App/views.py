# Create your views here.
from base64 import b64encode
from django.shortcuts import render,redirect
# imported our models
from django.core.paginator import Paginator
from . models import Song

def gautam(request):

    return render(request,'gautam.html')

def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

def contact(request):

    return render(request,'contact.html')

def signout(request):

    return render(request,'signout.html')




# the code for spotify tracks 


import requests
from django.http import JsonResponse

from django.shortcuts import render
from django.shortcuts import render
import requests
from base64 import b64encode
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt

def spotify_search(request):
    if request.method == 'POST':
        # Get the search query from the POST parameters
        search_query = request.POST.get('search_query', '')

        # Check if the search query is empty
        if not search_query:
            return render(request, 'spotify_search.html', {'error_message': 'Please enter a search query'})

        # Paste your Spotify client ID and client secret here
        client_id ='c9309412267f4e1684d286cdfa689253'
        client_secret = '38a4becf7d994bd49b62353f10030854'

        # Obtain an access token from the Spotify API
        token_url = 'https://accounts.spotify.com/api/token'
        headers = {'Authorization': 'Basic ' + b64encode(f"{client_id}:{client_secret}".encode()).decode()}
        data = {'grant_type': 'client_credentials'}
        token_response = requests.post(token_url, headers=headers, data=data)

        if token_response.status_code == 200:
            access_token = token_response.json().get('access_token')

            # Make a request to the Spotify API to search for tracks
            api_url = 'https://api.spotify.com/v1/search'
            headers = {'Authorization': 'Bearer ' + access_token}
            params = {'q': search_query, 'type': 'track'}
            response = requests.get(api_url, headers=headers, params=params)

            if response.status_code == 200:
                # If the request is successful, parse the response and extract relevant information
                data = response.json()
                tracks = data.get('tracks', {}).get('items', [])
                
                # Render the template with the retrieved tracks
                return render(request, 'spotify_tracks.html', {'tracks': tracks, 'search_query': search_query})
            else:
                # If the request fails, return an error message
                return render(request, 'spotify_search.html', {'error_message': 'Failed to fetch tracks from Spotify API'})

        else:
            # If unable to obtain access token, return an error message
            return render(request, 'spotify_search.html', {'error_message': 'Failed to obtain access token from Spotify API'})

    elif request.method == 'GET':
        # Render the search page template for GET requests
        return render(request, 'spotify_search.html')

    else:
        # Return a method not allowed error for other request methods
        return JsonResponse({'error': 'Method not allowed'}, status=405)



#the code end here for spotify
#now new codes

def login(request):

    return render(request,'login.html')

def homepage(request):

    return render(request,'homepage.html')

def anciya(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"anciya.html",context)

