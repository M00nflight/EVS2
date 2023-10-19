from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'templatesProductos/index.html')
def electronica(request):
    data={
        "titulo":"Electrónica",
        'producto1':"MAC",
        'producto2':"Celular",
        'producto3':"Playstation",
        'imagen1':'imagenes/MAC1.jpg',
        'imagen2':'imagenes/celular.jpg',
        'imagen3':'imagenes/ps4.jpg',
        'url':'https://portales.inacap.cl',
        'next1':"/ropa/",        
    }
    return render (request,'templatesProductos/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        'producto1':"Polera",
        'producto2':"Chaqueta",
        'producto3':"Zapatillas",
        'imagen1':'imagenes/jojopolera.webp',
        'imagen2':'imagenes/chaqueta.jpg',
        'imagen3':'imagenes/zapatillas.jpg',        
        'url':'https://portales.inacap.cl',
        'next2':"/juguetes/",   
    }
    return render (request,'templatesProductos/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        'producto1':"Pelota",
        'producto2':"Figura de Acción",
        'producto3':"Peluches",
        'imagen1':'imagenes/sl.webp',
        'imagen2':'imagenes/jojofigura.jpg',
        'imagen3':'imagenes/peluches.jpg',             
        'url':'https://portales.inacap.cl',
        'next3':"/electronica/",   
    }
    return render (request,'templatesProductos/productos.html',data)