import json

from django.core.management.base import BaseCommand

from menu_app.models import Menu, MenuItem

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    Menu.objects.all().delete()
    MenuItem.objects.all().delete()


def seed_menu(menu_instance, menu_tree, parent=None):
    for item_data in menu_tree:
        menu_item = MenuItem.objects.create(
            menu=menu_instance,
            parent=parent,
            name=item_data['name'],
            url=item_data['url']
        )
        if 'children' in item_data:
            seed_menu(menu_instance, item_data['children'], parent=menu_item)


def run_seed(self, mode):
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    with open('static/main_menu.json', 'r', encoding='utf-8') as json_file:
        menu = json.load(json_file)

    menu_instance = Menu.objects.create(name="main_menu", description="main menu")
    seed_menu(menu_instance, menu)
