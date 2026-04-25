from django.shortcuts import render, redirect
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
            message = contact_form.save(commit=False)
            if request.user.is_authenticated:
                message.name = f"{request.user.first_name} {request.user.last_name}"
                message.email = request.user.email
            message.save()
            messages.add_message(request, messages.SUCCESS, 
                                 'Your message has been sent')
            return redirect('home')
        else:
            if request.user.is_authenticated:
                contact_form = MessageForm(initial={
                    "name": f"{request.user.first_name} {request.user.last_name}",
                    "email": request.user.email })
    else:     
        contact_form = MessageForm()

    return render(
        request,
        "contact/contact.html",
        { "contact_form": contact_form }
    )
