from django.shortcuts import HttpResponse,Http404



def view(request):

    raise Http404

    return HttpResponse("MiddlewareMixin")
