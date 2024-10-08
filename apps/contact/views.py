from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import ContactForm
from .models import ContactMessage
from apps.users.models import UserProfile


# Centralized function to check if the user is a staff member
def is_staff_user(user):
    """
    Checks if the given user is a staff member.

    Args:
        user (User): The user instance to check.

    Returns:
        bool: True if the user is staff, otherwise False.
    """
    return user.is_staff


# View to list contact messages in the admin dashboard. Only staff users can access.
@login_required
def admin_message_list(request):
    """
    Displays a list of new contact messages for staff users.

    This view is only accessible to users with staff privileges.
    It fetches all contact messages with a status of 'new'.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered template with contact messages or a forbidden response.
    """
    if is_staff_user(request.user):  # Check if the user is staff
        contact_messages = ContactMessage.objects.filter(
            status="new"
        )  # Fetch only new messages
        return render(
            request,
            "admin_dashboard/admin_message_list.html",
            {"contact_messages": contact_messages},
        )
    else:
        return HttpResponseForbidden(
            "You do not have permission to access this page."
        )  # Show error if not staff


# View to respond to a specific message. Staff members can view and respond.
@login_required
def admin_respond(request, message_id):
    """
    Renders a page for staff to respond to a specific contact message.

    This view retrieves the message by its ID and presents it for staff to respond.

    Args:
        request (HttpRequest): The request object.
        message_id (int): The ID of the contact message.

    Returns:
        HttpResponse: Rendered template for responding to the message or a forbidden response.
    """
    if is_staff_user(request.user):  # Check if the user is staff
        message = get_object_or_404(
            ContactMessage, id=message_id
        )  # Get the message by ID or return 404 error
        context = {"contact": message}  # Pass the message details to the template
        return render(
            request, "admin_dashboard/admin_respond.html", context
        )  # Render the response page
    else:
        return HttpResponseForbidden(
            "You do not have permission to access this page."
        )  # Show error if not staff


# View to update the status of a contact message (mark as read). Only staff users can update.
@login_required
def update_status(request, message_id):
    """
    Updates the status of a contact message to 'read'.

    This view is accessible only to staff members and marks the message
    as read.

    Args:
        request (HttpRequest): The request object.
        message_id (int): The ID of the contact message.

    Returns:
        HttpResponse: Redirects to the message list after updating the status
        or a forbidden response.
    """
    if is_staff_user(request.user):  # Check if the user is staff
        message = get_object_or_404(
            ContactMessage, id=message_id
        )  # Get the message by ID
        message.status = "read"  # Mark the message as read
        message.save()  # Save the updated status
        messages.success(request, "Message marked as read.")  # Show success message
        return redirect("admin_message_list")  # Redirect to the message list
    else:
        return HttpResponseForbidden(
            "You do not have permission to access this page."
        )  # Show error if not staff


# View to delete a contact message. Only staff users can delete.
@login_required
def delete_message(request, message_id):
    """
    Deletes a specific contact message.

    This view is accessible only to staff members and allows them
    to delete a message from the database.

    Args:
        request (HttpRequest): The request object.
        message_id (int): The ID of the contact message to delete.

    Returns:
        HttpResponse: Redirects to the message list after deletion
        or a forbidden response.
    """
    if is_staff_user(request.user):  # Check if the user is staff
        message = get_object_or_404(
            ContactMessage, id=message_id
        )  # Get the message by ID
        message.delete()  # Delete the message
        messages.success(
            request, "Message successfully deleted."
        )  # Show success message
        return redirect("admin_message_list")  # Redirect to the message list
    else:
        return HttpResponseForbidden(
            "You do not have permission to access this page."
        )  # Show error if not staff


# Contact form view, accessible by all users. Handles form submission and saves the message.
def contact(request):
    """
    Displays the contact form for users to submit messages.

    This view handles both GET and POST requests. For POST requests,
    it validates and saves the submitted message.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered template for the contact form.
    """
    if request.method == "POST":  # If the request is a POST (form submission)
        contact_form = ContactForm(
            data=request.POST
        )  # Initialize the form with POST data
        if contact_form.is_valid():  # Check if the form is valid
            contact_message = contact_form.save(
                commit=False
            )  # Create a message instance, but don't save yet
            # Check if the user is authenticated, and attach the user profile to the message
            contact_message.user_profile = (
                UserProfile.objects.get(user=request.user)
                if request.user.is_authenticated and UserProfile.objects.filter(user=request.user).exists()
                else None
            )
            contact_message.save()  # Save the message to the database
            messages.success(
                request,
                "Contact message received. We will respond within 2 business days.",
            )  # Success message
            return redirect("contact")  # Redirect to the same contact page
    else:
        contact_form = ContactForm()  # If GET request, initialize an empty form

    return render(
        request, "contact/contact.html", {"contact_form": contact_form}
    )  # Render the contact form
