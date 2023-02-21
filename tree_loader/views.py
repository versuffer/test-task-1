from contextlib import redirect_stdout

from django.http import HttpResponse
from treelib import Tree

from .models import Employee


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
    with open('tree.txt', 'w') as file_obj:
        with redirect_stdout(file_obj):
            tree.show(line_type='ascii')


def EmployeeTreeView(request):
    create_tree()
    with open('tree.txt', 'r') as file_obj:
        data = file_obj.read()
        return HttpResponse(data, content_type='text/plain')
