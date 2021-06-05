from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

def contact(request):
    if request.method == 'POST':
        property = request.POST['property']
        property_id = request.POST['property_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_name = request.POST['realtor_name']
        realtor_email = request.POST['realtor_email']

        contact = Contact(property=property, property_id=property_id, name=name, email=email, phone=phone, message=message, user_id=user_id, realtor_name=realtor_name)

        #check if user have made an inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, property_id=property_id)
            if has_contacted:
                messages.warning(request, f'You have made an inquiry already to this property.')
                return redirect('/listings/'+ property_id)

        contact.save()

        send_mail(
            'Property inquiry',
            'There has been an inquiry for '+ property + ' Sign into the admin panel to check details!',
            'backend.dev.inquiry@gamil.com',
            ['backend.devcheck@gmail.com'],
            fail_silently=True,
        )

        messages.success(request, f'Your request has been submitted, a realtor will get back to you soon!')
        return redirect('/listings/'+ property_id)
  