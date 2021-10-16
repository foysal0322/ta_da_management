from django.shortcuts import render,HttpResponse,redirect
from TADA.models import *
from .forms import UpdateTada
from io import BytesIO
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template

# Create your views here.
def index(request):
    
    if  request.method== 'POST':
        date=request.POST.get('date')
        emp_name=request.POST.get('emp_name')
        tr_cost=request.POST.get('tr_cost')
        ln_cost=request.POST.get('ln_cost')
        ins_cost=request.POST.get('ins_cost')
       
        paid=request.POST.get('ispaid')
        def totalcost():
            tr_cost=request.POST.get('tr_cost')
            ln_cost=request.POST.get('ln_cost')
            ins_cost=request.POST.get('ins_cost')
            sum=tr_cost+ln_cost+ins_cost
            return sum

        emp=Employee(emp_name=emp_name)
        emp.save(force_insert=True)
        td=TaDa(date=date,emp_name=emp,tr_cost=tr_cost,ln_cost=ln_cost,ins_cost=ins_cost,paid=paid) #fetching & passing  employee name from given emplyoee table 
        td.save()
        return redirect('/tada_history')
    
    emp=Employee.objects.values('emp_name').distinct()
    return render(request, 'index.html',{'emp':emp})





    ###-----------generating & passing data for tada_history page-------########

def tada_history(request):
 
    td_history=TaDa.objects.all().order_by('date').order_by('-paid') #sorting history first by date and later by paid status

    sum=[]  #list for total sum
    for i in td_history:
        k=int(i.tr_cost)+int(i.ln_cost)+int(i.ins_cost) # calculating total sum

        sum.append(k)

    zip_test=zip(td_history,sum) #creating dictionary since we can only pass data as dictionary

    return render(request, 'tada_history.html',{'data':zip_test})

    ######-----------//////////\\\\\\\\\\\\\\----------################




###-----------paid status update function------------#######

def tada_update(request,pk):
    td_history=TaDa.objects.get(id=pk)
    prikey=td_history.id
    form = UpdateTada(instance=td_history)
    if request.method == "POST":
        form = UpdateTada(request.POST,instance=td_history)
        if form.is_valid():
            form.save()
            return redirect('/tada_history')

    context={'form':form}
    return render(request,'tada_update.html',context)

######-----------//////////\\\\\\\\\\\\\\----------################








def render_pdf_view(request):
    td_history=TaDa.objects.all().order_by('date').order_by('-paid')
    
    sum=[] #usimg same approach as tada_history
    for i in td_history:
        k=int(i.tr_cost)+int(i.ln_cost)+int(i.ins_cost)
        sum.append(k)
    data=zip(td_history,sum)
    template_path = 'pdf_template.html'
    context = {'data': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"' #for download
    # response['Content-Disposition'] =  'filename="report.pdf"' #for view
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show message
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

