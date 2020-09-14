from django.shortcuts import render

# Create your views here.
# pylint: disable=unused-variable
# pylint: enable=too-many-lines

def projects(request):
    return render(request, 'projects.html', {})

def intl_aqi(request):
    import json
    import requests
    import re
    from urllib.request import urlopen

    if request.method == "POST":
        city = request.POST['city']

    else:     
        url = "http://ipinfo.io/json"
        resp = urlopen(url)
        jsondata = json.load(resp)
        city = jsondata['city']

    api_req = requests.get("https://api.waqi.info/feed/" + city + "/?token=7b8cc61eb74aee354c5818dfce380d7c9a3ca765")

    try:
        api = json.loads(api_req.content)

        if api['status'] == 'error':
            api = "Error: No data on city"

    except Exception as e:
        api = "Error: No data on city"

    return render(request, 'intl_aqi.html', {'api' : api })