import pathlib
import sys

sys.path.append(pathlib.Path(__file__).parent.parent)

from django.http import HttpResponse

from tree_renderer import create_tree


def employee_tree_view(request):
    create_tree()
    with open('tree.txt', 'r') as file_obj:
        data = file_obj.read()
        return HttpResponse(data, content_type='text/plain')
