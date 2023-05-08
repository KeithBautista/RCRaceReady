from django.shortcuts import render, get_list_or_404
from .models import Event

# Create your views here.


def events_all(request):

    events = get_list_or_404(Event)

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)
