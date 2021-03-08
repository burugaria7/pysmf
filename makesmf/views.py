from django.shortcuts import render  # render(request, 'hello.html', context)
from django.http import HttpResponse  # HttpResponse('Hello, World !!')
from django.shortcuts import render
from django.views import View

class HelloView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'message': "Hello World! from View!!!!!",
        }
        return render(request, 'hello.html', context)

    def post(self, request, *args, **kwargs):
        context = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }
        return render(request, 'hello.html', context)

hello = HelloView.as_view()