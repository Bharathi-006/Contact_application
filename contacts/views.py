from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact

def contact_list(request):
    contacts= Contact.objects.all().order_by('name')
    return render(request,'front_page.html', {'contacts':contacts})

def contact_details(request, pk):
    contact= get_object_or_404(Contact,pk=pk)
    if request.method== 'POST':
        if 'delete' in request.POST:
            contact.delete()
            return redirect('contact_list')
        contact.name=request.POST.get('name')
        contact.email=request.POST.get('email')
        contact.ph_no=request.POST.get('ph_no')
        contact.save()
        return redirect('contact_details',pk=contact.pk)
    return render(request,'contact_details.html',{'contact':contact})
def contact_create(request):
    if request.method == 'POST':
        # Get the data from the submitted form
        name = request.POST.get('name')
        email = request.POST.get('email')
        ph_no = request.POST.get('ph_no')
        
        # Create a new contact object
        Contact.objects.create(name=name, email=email, ph_no=ph_no)
        
        # Redirect back to the main list
        return redirect('contact_list')
        
    # If it's a GET request, just show the blank form
    return render(request, 'contact_form.html')