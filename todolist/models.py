from django.db import models
from django.utils import timezone

class Chapter(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, blank=True)

    class Meta:
        # Дадим возможность отправлять только карточки этого типа
        ordering = ["-title"]
        verbose_name = ("Chapters on project")

    def __str__(self):
        return self.title


class Category(models.Model):
    # Категоризация данных по направлениям
    type_category = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.type_category


class Progress_type(models.Model):
    #Сюда мы будем добавлять значения наших прогресс-данных
    # Чтобы потом извлекать в Card-
    type_of_progress = models.CharField(max_length=100)

    class Meta:
        # Создадим возможность фильтровать по статусам
        ordering = ["-type_of_progress"] 
        verbose_name = ("Progress by card")
    
    def __str__(self):
        return self.type_of_progress


class Card(models.Model):
    subtitle = models.ForeignKey(Chapter, default="Oink-oink", on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True) # дата создания
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) #до какой даты нужно было сделать дело
    category = models.ForeignKey(Category, default="general",on_delete=models.PROTECT) # foreignkey с помощью которой мы будем осуществлять связь с таблицей Категорий
    progress_type = models.ForeignKey(Progress_type, default="None", on_delete=models.PROTECT)
    card_name = models.CharField(max_length=50)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
