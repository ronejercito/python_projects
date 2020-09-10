from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects.html', {})

def intl_aqi(request):
    return render(request, 'intl_aqi.html', {})