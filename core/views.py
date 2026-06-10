from django.shortcuts import render, get_object_or_404
from .models import Work, Character
from .models import Work, Character, Route


def home(request):
    return render(request, 'home/index.html')


def work_list(request):
    works = Work.objects.all()
    return render(request, 'works/list.html', {'works': works})


def work_detail(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    return render(request, 'works/detail.html', {'work': work})


def character_list(request):
    characters = Character.objects.all()
    return render(request, 'characters/list.html', {'characters': characters})


def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'characters/detail.html', {'character': character})


def character_search(request):
    keyword = request.GET.get('keyword')

    characters = Character.objects.all()

    if keyword:
        characters = characters.filter(name__icontains=keyword)

    return render(request,'characters/search.html',{'keyword': keyword,'characters': characters,})

def route_list(request):
    routes = Route.objects.all()
    return render(request, 'routes/list.html', {'routes': routes})


def route_detail(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    return render(request, 'routes/detail.html', {'route': route})

def diagnosis(request):

    if request.method == "POST":

        route_type = request.POST.get("route_type")

        if route_type == "classic":
            route = Route.objects.get(
                title="クラシック入門ルート"
            )

        elif route_type == "timeline":
            route = Route.objects.get(
                title="時系列ルート"
            )

        else:
            route = Route.objects.get(
                title="マンダロリアン入門ルート"
            )

        return render(
            request,
            "diagnosis/result.html",
            {"route": route}
        )

    return render(
        request,
        "diagnosis/form.html"
    )