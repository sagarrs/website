from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("<h1>This is the music app</h1>")

def detail(request, album_id):
	return HttpResponse("<h2> Details for album - " + str(album_id) + "</h2>")

