from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from votreg.models import State
from votreg.models import Page
from django.utils.text import slugify
# import json



def index(request):

    state_list = State.objects.all()
    
    states = []
    for state in state_list:
        state_lookup_name = state.name.replace(' ', '_')
        # return state_lookup_name
        # state_name = state_name.replace('_', ' ')
        # print state_name
        # state = State.objects.get(name=state_name)
        # context_dict['state_name'] = state.name

        # context_dict['pages'] = pages
        # context_dict['state'] = state
        states.append({'name': state_lookup_name, 'display': state.name})
    pages = Page.objects.filter(states=state).prefetch_related("pages")
    context_dict = {'states': states, 'state_list': state_list, 'pages': pages}


    if 'search_state' in request.POST:
        try:
            search = request.POST['state_name']
            # search_name = search.upper()
            state_results = State.objects.filter(name=search)
            return HttpResponseRedirect("/state/%s" % search)

        except State.DoesNotExist:

            pass

    return render(request, 'votreg/index.html', context_dict)

def about(request):

    return HttpResponse("About!")

def state(request, state_name):

    context_dict = {}

    try:
        state_name = state_name.replace('_', ' ')
        print state_name
        state = State.objects.get(name=state_name)
        context_dict['state_name'] = state.name
        pages = Page.objects.filter(states=state)
        context_dict['pages'] = pages
        context_dict['state'] = state

    except State.DoesNotExist:

        pass


    return render(request, 'votreg/state.html', context_dict)

        # state(state_results)

# def json_data(request):

#     state = State.objects.all()
#     json_state = []

#     for state in state:
#         state_dict = {}
#         state_dict['name'] = state.name

#         json_state.append(state_dict)

#     response_data = simplejson.dumps(json_state)

#     return HttpResponse(response_data, mimetype='application/json')








    







