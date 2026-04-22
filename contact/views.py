from django.shortcuts import render
from django.contrib import messages
from .forms import MessageForm

# Create your views here.
def contact(request):
    """
    Display a contact form for :model: `contact.Message`

    **Context**
    ``contact_form`` 
        The form to send a message to the site admin   

    **Template**
    :template: contact/contact.html
    """

    if request.method == "POST":
        contact_form = MessageForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, 
                                 'Your message has been sent')
            

    contact_form = MessageForm()

    return render(
        request,
        "contact/contact.html",
        { "contact_form": contact_form }
    )
