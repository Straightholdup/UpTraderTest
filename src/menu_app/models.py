from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
