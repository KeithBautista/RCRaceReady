from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


def contactUs(request):

    """
    a view to display the contactform
    and handle form submission
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Thank you for getting in contact! \
                 We will reach out to you shortly.')
            return HttpResponseRedirect('/contactus?submitted=True')

        else:
            form = ContactForm()
            messages.warning(request, 'Message not sent. Please try again.')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()

    form = ContactForm()
    template = 'contactus/contact_us.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
