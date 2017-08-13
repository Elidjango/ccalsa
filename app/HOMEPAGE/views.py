from django.shortcuts import render_to_response

# Create your views here.

#ESTO ES LA PAGINA INICIAL Y NO LLEVA NINGUNA CONFIGURACION
#ASI QUE EN ESTA APP NO HARAS NADA SOLO MODIFICAR EL HTML, PARA INTRODUCIR INFORMACION ESTATICA

def index(request):
    return render_to_response('index.html')
