from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("""Тестовое задание: Веб-сервис для управления движением денежных средств (ДДС)\n Таблица с записями о ДДС.
■ Фильтры по дате, статусу, типу, категории и подкатегории.""")

def directory_management(request):
    return HttpResponse("""Добавление, редактирование и удаление статусов, типов,
категорий и подкатегорий, а также установление необходимых
зависимостей.""")

def creat_edit_entry(request):
    return HttpResponse("""■ Форма для ввода данных.
■ Поле выбора категорий, автоматически фильтрующее
подкатегории на основе выбранной категории.""")