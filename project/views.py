


from django.shortcuts import render, HttpResponse
from project import views
# Create your views here


def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")





from django.shortcuts import render, redirect
from .models import Student

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        message = request.POST.get('message')

        # Save to database
        Student.objects.create(
            name=name,
            email=email,
            course=course,
            message=message
        )

        return render(request, 'thank_you.html')  # or redirect

    return render(request, 'index.html')



from django.shortcuts import render


from .forms import ContactForm
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # 🔥 This actually stores the data in DB
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


import openpyxl
from django.http import HttpResponse
from .models import Contact

def export_contacts_to_excel(request):
    # Create a workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Contact Messages"

    # Header row including all fields
    ws.append([
        'Name', 
        'Email', 
        'Phone', 
        'College Name', 
        'Course', 
        'Branch', 
        'Message', 
        'Date Sent'
    ])

    # Data rows
    for contact in Contact.objects.all():
        ws.append([
            contact.name,
            contact.email,
            contact.phone,
            contact.college_name,
            contact.course,
            contact.branch,
            contact.message,
            contact.created_at.replace(tzinfo=None) if contact.created_at else ''
        ])

    # Create the response object
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=contacts.xlsx'
    wb.save(response)

    return response
