import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task_1.settings")
django.setup()

from tree_loader.models import Employee

from treelib import Tree


def get_data():
    return Employee.objects.order_by('supervisor_id')


def create_tree():
    queryset = get_data()
    tree = Tree()
    tree.create_node('Hierarchy', 0)
    for instance in queryset:
        tree.create_node(
            f'{instance.first_name} {instance.last_name}', instance.id,
            parent=instance.supervisor_id
        )
    tree.save2file('tree.txt')





