from django.shortcuts import render

# Create your views here.
def App2(request):
    return render (request,'templatesProductos/certamen.html')

def chile(request):
    data={
        "titulo":"Chile",
        "imagen":"imagenes/chileicon.png",
        "url":"http://127.0.0.1:8000/App1/",
        "dato1":"El idioma oficial es el castellano, existiendo además lenguas de los pueblos originarios que hoy aun se utilizan, entre ellas se encuentra el mapudungún (mapuche), el quechua, y el Rapa Nui.",
        "dato2":"Las ciudades más importantes, además de Santiago, la capital, con 5.257.937 habitantes, son: Antofagasta (225.316 habitantes), Concepción (800.000), Temuco (210.587), Valparaíso / Viña del Mar (566.992) principal puerto del país, localizado a 120 kms. al oeste de Santiago, y Puerto Montt (110.139)",
        "dato3":"El territorio chileno se encuentra al suroeste de América del Sur, entre los meridianos 17°30' y los 90° de latitud Sur.",
        "dato4":"Chile limita al norte con el Perú, al este con Bolivia y Argentina, al Oeste con el océano Pacifico y al sur con el Polo Sur.",
    }
    return render (request,'templatesProductos/certamen.html',data)

def argentina(request):
    data={
        "titulo":"Argentina",
        "url":"http://127.0.0.1:8000/App1/",
        "imagen":"imagenes/arg.png",
        "dato1":"La Argentina está organizada como un Estado federal descentralizado.",
        "dato2":"Es el único país latinoamericano que tiene un centro de investigación y enseñanza científica entre los diez mejores del mundo.",
        "dato3":"Su territorio reúne una gran diversidad de climas, causada por una amplitud latitudinal que supera los 30°",
        "dato4":"Su territorio continental americano, que abarca gran parte del Cono Sur, limita al norte con Bolivia y Paraguay, al nordeste con Brasil, al este con Uruguay y el océano Atlántico, al oeste con Chile y, siempre en su sector americano, al sur con Chile y las aguas atlánticas del pasaje de Drake.",
    }
    return render (request,'templatesProductos/certamen.html',data)

def brasil(request):
    data={
        "titulo":"Brasil",
        "url":"http://127.0.0.1:8000/App1/",
        "imagen":"imagenes/br.png",
        "dato1":"La región del actual Brasil, hasta entonces habitada por pueblos indígenas, tuvo su primer contacto con los europeos en el año 1500 d. C.",
        "dato2":"La economía brasileña es la mayor de América del Sur, América Latina y del hemisferio sur, la undécima mayor del mundo por PIB nominal y la octava mayor por paridad del poder adquisitivo (PPC).",
        "dato3":"El país es miembro fundador de la Organización de las Naciones Unidas (ONU), G20, Comunidad de Países de Lengua Portuguesa (CPLP), Unión Latina, Organización de los Estados Americanos (OEA), Organización de los Estados iberoamericanos (OEI), Mercado Común del Sur (Mercosur) y de la Unión de Naciones Sudamericanas (Unasur), además de ser uno de los países BRICS.",
        "dato4":"En las cartas náuticas medievales, aparece a menudo una «isla Brasil» en el océano Atlántico. El caso más antiguo es el mapa de Angelino Dulcert de 1325.",
    }
    return render (request,'templatesProductos/certamen.html',data)