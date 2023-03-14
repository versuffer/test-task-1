import pathlib
import sys

sys.path.append(pathlib.Path(__file__).parent.parent)

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from tree_renderer import create_tree


class EmployeeTreeView(View):

    def get(self, request):
        create_tree()
        with open('tree.txt', 'r') as file_obj:
            data = file_obj.read()
            # return HttpResponse(data, content_type='text/plain')
            return render(request, 'home.html', {'tree': data}, content_type='text/html')
