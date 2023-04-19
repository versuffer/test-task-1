import os
from functools import lru_cache
from contextlib import redirect_stdout

import django
from treelib import Tree

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

from tree_loader.models import Employee


def get_data():
    return Employee.objects.order_by('supervisor_id')



@lru_cache
def create_tree():
    queryset = get_data()
    tree = Tree()
    tree.create_node('Hierarchy', 0)
    for instance in queryset:
        tree.create_node(
            f'{instance.first_name} {instance.last_name} {instance.position}', instance.id,
            parent=instance.supervisor_id
        )
    render_tree(tree)


def render_tree(tree_obj):
    with open('tree.txt', 'w') as file_obj:
        with redirect_stdout(file_obj):
            tree_obj.show(line_type='ascii')
