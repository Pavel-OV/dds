from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    max_len = 25
    # pk_lst = Recipes.objects.exclude(image__exact='').values_list('id', flat=True)
    # if len(pk_lst) <= max_carussel_len:
    #     pk_rnd = pk_lst
    # else:
    #     pk_rnd = choices(pk_lst, k=5)
    # recipes_carussel = {}
    # for k, i in enumerate(pk_rnd):
    #     recipes_carussel[f'set{k}'] = Recipes.objects.filter(pk=i)
#     return HttpResponse("""Добавление, редактирование и удаление статусов, типов,
# категорий и подкатегорий, а также установление необходимых
# зависимостей.""")

    return render(request, "site_ddsapp/index.html", {'recipes_carussel': max_len})

def edit_page(request):
      max_len = 25
      return render(request, "site_ddsapp/index.html", {'recipes_carussel': max_len})

#      return HttpResponse("""Добавление, редактирование и удаление статусов, типов,
# категорий и подкатегорий, а также установление необходимых
# зависимостей.""")


def create_page(request):
     return HttpResponse("""Добавление, редактирование и удаление статусов, типов,
категорий и подкатегорий, а также установление необходимых
зависимостей.""")

def directory_management(request):
    return HttpResponse("""Добавление, редактирование и удаление статусов, типов,
категорий и подкатегорий, а также установление необходимых
зависимостей.""")

# def creat_edit_entry(request):
#     return HttpResponse("""■ Форма для ввода данных.
# ■ Поле выбора категорий, автоматически фильтрующее
# подкатегории на основе выбранной категории.""")