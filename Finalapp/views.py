from django.shortcuts import render
from django.http import HttpResponse
from Finalapp.models import  Expense,Collection,Budget

# Create your views here.
def function(request):
    return render(request,'home.html',context={})

def login_view(request):
        if request.method=='POST':
            name = request.POST['NAME']
            pwd = request.POST['PASSWORD']
            return function(request)
        return render(request,'login.html',{})

def budget_view(request):
    return render(request,'budget.html')

def expenses_view(request):
    return render(request,'expenses.html')

def collection_view(request):
    return render(request,'collection.html')


def logout_view(request):
        return login_view(request)

def bud_add_page(request):
    if request.method=='POST':
        cl_name=request.POST['client_name']
        cl_id=request.POST['client_id']
        cl_phone=request.POST['client_phone']
        cl_email=request.POST['client_email']
        cl_purpose=request.POST['client_purpose']
        cl_chequeno=request.POST['client_chequeno']
        cl_chequeamount=request.POST['client_chequeamount']
        cl_issuedate=request.POST['client_issuedate']
        cl_chequedate=request.POST['client_chequedate']
        cl_preparedby=request.POST['client_preparedby']
        cl_signedby=request.POST['client_signedby']
        cl_bankname=request.POST['client_bankname']
        cl_branchname=request.POST['client_branchname']
        cl_chequestatus=request.POST['client_chequestatus']
        cl_cleareddata=request.POST['client_cleareddata']
        cl_remarks=request.POST['client_remarks']
        store=Budget(client_name=cl_name,client_phone=cl_phone,client_email=cl_email,client_purpose=cl_purpose,
        client_chequeno=cl_chequeno,client_chequeamount=cl_chequeamount,client_issuedate=cl_issuedate,client_chequedate=cl_chequedate,
        client_preparedby=cl_preparedby,client_signedby=cl_signedby,client_bankname=cl_bankname,client_branchname=cl_branchname,
        client_chequestatus=cl_chequestatus,client_cleareddata=cl_cleareddata,client_remarks=cl_remarks)
        store.save()
        return budget_view(request)
    return render(request,'budgetadd.html')

def bud_search_page(request):
    if request.method=='POST':
        cl_name=request.POST['client_name']
        store=Budget.objects.filter(client_name=cl_name).all()
        print(store)
        return render(request,'budview.html',{'stores': store})

    else:
        return render(request,'budgetsearch.html')

def bud_update_page(request):
    if request.method=='POST':
        cl_email=request.POST['client_email']
        cl_phone=request.POST['client_phone']
        store=Budget.objects.filter(client_email=cl_email).update(client_phone=cl_phone)
        #store.save()
        return render(request,'budget.html',{})
    else:
        return render(request,'budgetupdate.html')


def exp_add_page(request):
    if request.method=='POST':
        e_recivername=request.POST['E_recivername']
        e_month=request.POST['E_month']
        e_email=request.POST['E_email']
        e_purpose=request.POST['E_purpose']
        e_expenseamount=request.POST['E_expenseamount']
        e_previous_due_date=request.POST['E_previous_due_date']
        e_total_expense_amount=request.POST['E_total_expense_amount']
        e_planned_period_of_payment=request.POST['E_planned_period_of_payment']
        e_actual_period_of_payment=request.POST['E_actual_period_of_payment']
        e_amount_paid=request.POST['E_amount_paid']
        e_date_of_payment=request.POST['E_date_of_payment']
        e_mode_of_payment=request.POST['E_mode_of_payment']
        e_dd_no=request.POST['E_dd_no']
        e_cheque_no=request.POST['E_cheque_no']
        e_transaction_no=request.POST['E_transaction_no']
        e_cheque_date=request.POST['E_cheque_date']
        e_dd_date=request.POST['E_dd_date']
        e_transaction_date=request.POST['E_transaction_date']
        e_total_due_amount=request.POST['E_total_due_amount']
        e_payment_status=request.POST['E_payment_status']
        store1=Expense(E_recivername=e_recivername,E_month=e_month,E_email=e_email,E_purpose=e_purpose,
        E_expenseamount=e_expenseamount,E_previous_due_date=e_previous_due_date,E_total_expense_amount=e_total_expense_amount,
        E_planned_period_of_payment=e_planned_period_of_payment,E_actual_period_of_payment=e_actual_period_of_payment,
        E_amount_paid=e_amount_paid,E_date_of_payment=e_date_of_payment,E_mode_of_payment=e_mode_of_payment,
        E_dd_no=e_dd_no,E_cheque_no=e_cheque_no,E_transaction_no=e_transaction_no,E_cheque_date=e_cheque_date,
        E_dd_date=e_dd_date,E_transaction_date=e_transaction_date,E_total_due_amount=e_total_due_amount,E_payment_status=e_payment_status)
        store1.save()
        return expenses_view(request)
    return render(request,'expensesadd.html')


def exp_search_page(request):
    if request.method=='POST':
        e_recivername=request.POST['E_recivername']
        store1=Expense.objects.filter(E_recivername=e_recivername).all()
        print(store1)
        return render(request,'expview.html',{'stores': store1})
    else:
        return render(request,'expensessearch.html')

def exp_update_page(request):
    if request.method=='POST':
        e_recivername=request.POST['E_recivername']
        e_amount_paid=request.POST['E_amount_paid']
        store1=Expense.objects.filter(E_recivername=e_recivername).update(E_amount_paid=e_amount_paid)
        return render(request,'expenses.html',{})
    else:
        return render(request,'expensesupdate.html')


def collection_add_page(request):
    if request.method=='POST':
        c_mode_of_payment=request.POST['C_mode_of_payment']
        c_date=request.POST['C_date']
        c_amount_paid=request.POST['C_amount_paid']
        store2=Collection(C_mode_of_payment=c_mode_of_payment,C_date=c_date,C_amount_paid=c_amount_paid)
        store2.save()
        return collection_view(request)
    return render(request,'collectionadd.html')


def collection_search_page(request):
    if request.method=='POST':
        c_date=request.POST['C_date']
        store2=Collection.objects.filter(C_date=c_date).all()
        return render(request,'collview.html',{'stores': store2})
    else:
        return render(request,'collectionsearch.html')

def collection_update_page(request):
    if request.method=='POST':
        c_amount_paid=request.POST['C_amount_paid']
        c_mode_of_payment=request.POST['C_mode_of_payment']
        c_date=request.POST['C_date']
        store2=Collection.objects.filter(C_date=c_date).update(C_mode_of_payment=c_mode_of_payment,C_amount_paid=c_amount_paid)
        return render(request,'collection.html',{})
    else:
        return render(request,'collectionupdate.html')
