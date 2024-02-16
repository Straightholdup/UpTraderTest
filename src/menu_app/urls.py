import json

from django.urls import path
from menu_app.views import index


def generate_urlpatterns(menu, parent_url=None):
    urlpatterns = []

    for item in menu:
        url = f"{parent_url}{item['url']}/" if parent_url else f"{item['url']}/"
        urlpatterns.append(path(url, index, name=item['url']))
        if 'children' in item:
            urlpatterns += generate_urlpatterns(item['children'], url)

    return urlpatterns


with open('static/main_menu.json', 'r', encoding='utf-8') as json_file:
    menu = json.load(json_file)

urlpatterns = [
                  path('', index, name='main_menu'),
              ] + generate_urlpatterns(menu)
