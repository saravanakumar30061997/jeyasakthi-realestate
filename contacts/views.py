from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from listings.models import Listing  # Import Listing model
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')  # Ensure it's an integer
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id') or None
        realtor_email = request.POST.get('realtor_email')

        # ✅ Get the Listing instance using listing_id (convert it to int)
        listing = get_object_or_404(Listing, id=int(listing_id))

        # ✅ Check if user has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(listing=listing, user_id=user_id).exists()
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing.")
                return redirect('/listings/' + listing.slug)

        # ✅ Save Contact correctly (listing is now a ForeignKey, not a string)
        contact = Contact(
            listing=listing,  # Pass the Listing object, not a string
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        contact.save()

        # ✅ Send email notification
        try:
            send_mail(
                'Property Listing Inquiry',
                f'There has been an inquiry for {listing.title}. Sign into the admin panel for more info.',
                'jeyasakthirealestate@gmail.com',
                [realtor_email, 'saravanask1997@gmail.com', 'jeyasakthi0528@gmail.com'],
                fail_silently=False
            )
        except Exception:
            # If email fails (timeout, auth error), do not crash the app.
            messages.error(request, "Your inquiry was saved, but the email notification could not be sent.")

        messages.success(request, "Your request has been submitted, a realtor will get back to you soon.")
        return redirect('/listings/' + listing.slug)
