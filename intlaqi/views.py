from django.shortcuts import render

# Create your views here.
# pylint: disable=unused-variable
# pylint: enable=too-many-lines

def projects(request):
    return render(request, 'projects.html', {})

def intl_aqi(request):
    import json
    import requests

    api_req = requests.get("https://api.waqi.info/feed/makati/?token=7b8cc61eb74aee354c5818dfce380d7c9a3ca765")

    try:
        api = json.loads(api_req.content)
    except Exception as e:
        api = "Error: No data"

    return render(request, 'intl_aqi.html', {'api' : api })