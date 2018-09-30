from django.shortcuts import render

# Create your views here.
from engine.model

def hello_world_name


class Engine(objects):
    pass


def engine_list(request):
    engine = Engine.objects.all()
    output = ""
    for engine in engine:
        output += f'(engine.id)  <a href="/engine/(engine.id">(engine.name)</a><hr>'
        return HttpResponse(output)

    def products_list(request):
        product = Engine.objects.all()
        return render(
            request = request
            context =('engine')
