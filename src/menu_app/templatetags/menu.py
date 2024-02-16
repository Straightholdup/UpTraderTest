from django import template
from django.http import HttpRequest
from django.template import RequestContext

from menu_app.models import MenuItem
from django.urls import reverse, NoReverseMatch

register = template.Library()


def try_reverse(url):
    try:
        item_url = reverse(url)
    except NoReverseMatch:
        item_url = url
    return item_url


def get_item_by_url(items, url):
    for item in items:
        item_url = try_reverse(item.url)
        if item_url == url:
            return item


def get_menu(menu_name: str, current_path: str) -> list:
    items = MenuItem.objects.filter(menu__name=menu_name).order_by('pk')

    # Find item with url == current_path
    active_item = get_item_by_url(items, current_path)

    # Get children for the active item
    tree_children = [
        {'url': try_reverse(item.url), 'name': item.name}
        for item in items.filter(parent=active_item)
    ]

    if not active_item:
        return tree_children

    tree = {
        'url': try_reverse(active_item.url),
        'name': active_item.name,
        'children': tree_children
    }

    # While item has parent get children for the parent
    pivot = active_item
    while pivot:
        children = items.filter(parent=pivot.parent)
        tree_children = []
        for child in children:
            if child == pivot:
                tree_child = tree
            else:
                tree_child = {'url': try_reverse(child.url), 'name': child.name}
            tree_children.append(tree_child)

        if pivot.parent:
            tree = {'url': try_reverse(pivot.parent.url), 'name': pivot.parent.name, 'children': tree_children}
        else:
            tree = tree_children

        pivot = pivot.parent

    return tree


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context: RequestContext, menu_name: str) -> dict:
    current_path = context['request'].path \
        if 'request' in context and isinstance(context['request'], HttpRequest) \
        else ''
    return {'menu': get_menu(menu_name, current_path)}
