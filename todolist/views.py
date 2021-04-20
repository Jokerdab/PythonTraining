from django.shortcuts import render, redirect #для отображения и редиректа берем необходимые классы
from django.http import HttpResponse
from .models import Chapter, Progress_type, Card, Category #не забываем наши модели
from django.urls import reverse

def redirect_view(request):
    return redirect(reverse('Chapters')) #редирект с главной на страницу с главами

def cardlist(request):
    card_list = Card.objects.all() #Запрашиваем все объекты из менеджера объектов
    chapters = Chapter.objects.all()

    return render(request, "cards_list.html", {"card_list": card_list, "chapters": chapters})


def chapters_list(request):
    chapters_list_all = Chapter.objects.all()

    return render(request, "chapters.html", {"chapters_list_all": chapters_list_all})
