from .models import Contact ,  Picture
from .forms import ContactForm,PictureForm



from django.db.models import Q

from django.core.paginator import Paginator

from django.shortcuts import render,redirect, get_object_or_404
from .forms import ContactForm


from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseRedirect, HttpResponseRedirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.decorators import login_required



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Check if the phone number already exists in the database
        if Contact.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone number already exists!')
            phone_exists = True
        else:
            contact = Contact(name=name, phone=phone, subject=subject, message=message)
            contact.save()
            messages.success(request, 'Your form was submitted successfully!')
            phone_exists = False

        return render(request, 'contact.html', {'phone_exists': phone_exists})

    return render(request, 'contact.html')

def portfolio(request):
    return render (request,'portfolio.html')
def index(request):
    return render (request,'index.html')
def adminclick_view(request):
    if request.user.is_authenticated:
        return redirect('admin-dashboard')
    return redirect('adminlogin')


def afterlogin_view(request):
        return redirect('admin-dashboard')
 
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    return render(request,'admin/dashboard.html')


def admin_404(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')

@login_required(login_url='adminlogin')
def admin_contact_view(request):
    contact_list = Contact.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        contact_list = contact_list.filter(
            Q(name__icontains=search_query) |
            Q(phone__icontains=search_query)|
            Q(subject__icontains=search_query) |
            Q(message__icontains=search_query)
        )
    paginator = Paginator(contact_list, 5) # Change the number of contacts per page here
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    context = {'contacts': contacts}
    return render(request, 'admin/contact.html', context)



@login_required(login_url='adminlogin')
def admin_delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
       
    return redirect('admin-contact')
@login_required(login_url='adminlogin')
def admin_edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated successfully')
            return redirect('admin-contact')
    else:
        form = ContactForm(instance=contact)

    context = {'form': form, 'contact_id': contact_id}
    return render(request, 'admin/edit_contact.html', context)


def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = PictureForm()
    return render(request, 'admin/admin_upload.html', {'form': form})

def views_pictures(request):
    pictures = Picture.objects.all()
    return render(request, 'views_pictures.html', {'pictures': pictures})




    


