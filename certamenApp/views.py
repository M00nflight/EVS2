from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'templatesProductos/certamen.html')
def chile(request):
    data={
        "titulo":"Chile",
        "imagen1":"imagenes/chileicon.png",
        "url":"",
        
    }
    return render (request,'/certamen.html',data)

def argentina(request):
    data={
        "titulo":"Argentina",

    }
    return render (request,'/certamen.html',data)

def brasil(request):
    data={
        "titulo":"Brasil",

    }
    return render (request,'/certamen.html',data)