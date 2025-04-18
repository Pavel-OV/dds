 
from django.shortcuts import render, redirect
from .forms import Status
from .models import Status, Type, Category

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

# def edit_page(request):
#       max_len = 25
#       return render(request, "site_ddsapp/index.html", {'recipes_carussel': max_len})

#      return HttpResponse("""Добавление, редактирование и удаление статусов, типов,
# категорий и подкатегорий, а также установление необходимых
# зависимостей.""")
def create_status(request):
    if request.method == 'POST':
        status = Status.objects.all()
        name = request.POST['name']
        new_status = Status.objects.create(name=name)
        message = ' - статус добавлен'
        return render(request,'site_ddsapp/list_status.html', {'items':status, 'imtes': Status.objects.all(),' message': message})  # перенаправление на страницу со списком
    else:
        return render(request, 'site_ddsapp/create_status.html')
    
def create_type(request):
    if request.method == 'POST':
        status = Type.objects.all()
        name = request.POST['name']
        new_type = Type.objects.create(name=name)
        message = ' - тип добавлен'
        return render(request, 'site_ddsapp/list_status.html', {'items':status, 'imtes':Type.objects.all(), 'message': message})  # перенаправление на страницу со списком
    else:
        return render(request, 'site_ddsapp/create_type.html')
    
def create_category(request):
    if request.method == 'POST':
        status = Category.objects.all()
        name = request.POST['name']
        new_category = Category.objects.create(name=name)
        message = ' - категория добавлена'
        return render(request, 'site_ddsapp/list_status.html', {'items':status, 'imtes':Category.objects.all(), 'message': message})  # перенаправление на страницу со списком
    else:
        return render(request, 'site_ddsapp/create_category.html')
    
def list_status(request):
    status = Status.objects.all()
    return render(request, 'site_ddsapp/list_status.html', {'items': status})

def list_type(request):
    status = Type.objects.all()
    return render(request, 'site_ddsapp/list_status.html', {'items': status})

def list_category(request):
    status = Category.objects.all()
    return render(request, 'site_ddsapp/list_status.html', {'items': status})


def create_page(request):
     return HttpResponse("""Добавление, редактирование и удаление статусов, типов,
категорий и подкатегорий, а также установление необходимых
зависимостей.""")


def edit_page(request):
    max_len = 2
    return render(request, "site_ddsapp/index.html", {'recipes_carussel': max_len})
#     return HttpResponse("""■ Форма для ввода данных.
# ■ Поле выбора категорий, автоматически фильтрующее
# подкатегории на основе выбранной категории.""")

def directory_management(request):
    return render(request, 'site_ddsapp/directory_management.html')