from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from votreg.models import State
from votreg.models import Page



def index(request):

    state_list = State.objects.all()  
    context_dict = {'states': state_list}


    if 'search_state' in request.POST:
        try:
            search = request.POST['state_name']
            state_results = State.objects.filter(name = search)
            return HttpResponseRedirect("/state/%s" % search)

        except State.DoesNotExist:

            pass

    return render(request, 'votreg/index.html', context_dict)

def about(request):

    return HttpResponse("About!")

def state(request, state_name):

    context_dict = {}

    try:

        state = State.objects.get(name = state_name)
        context_dict['state_name'] = state.name
        pages = Page.objects.filter(states=state)
        context_dict['pages'] = pages
        context_dict['state'] = state

    except State.DoesNotExist:

        pass


    return render(request, 'votreg/state.html', context_dict)

        # state(state_results)



    







