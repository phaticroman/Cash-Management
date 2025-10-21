from django.shortcuts import render, redirect, get_object_or_404

from ManageCash.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        contact_no=request.POST.get('contact_no')
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                contact_no=contact_no,


            )
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")



@login_required
def add_cash_view(request):
    if request.method == "POST":
        source = request.POST['source']
        amount = request.POST['amount']
        datetime = request.POST.get('datetime')  # Defaults to current time if not provided
        description = request.POST.get('description', '')

        AddCash.objects.create(
            user=request.user,
            source=source,
            amount=amount,
            datetime=datetime,
            description=description
        )
        
        return redirect('cash_dashboard')
    
    return render(request, 'add_cash.html')


@login_required
def update_cash_view(request, cash_id):
    cash_entry = AddCash.objects.get(id=cash_id)
    
    
    context={
        'cash_entry':cash_entry
            }

    if request.method == 'POST':
        cash_entry.source = request.POST['source']
        cash_entry.amount = request.POST['amount']
        cash_entry.datetime = request.POST['datetime']
        cash_entry.description = request.POST['description']
        cash_entry.save()
        return redirect('cash_dashboard')

    return render(request, 'update_cash.html',context )

login_required
def delete_cash_view(request, cash_id):
    
    AddCash.objects.get(id=cash_id).delete()
    
    return redirect('cash_dashboard')


def cash_dashboard(request):
    cash_entries = AddCash.objects.filter(user=request.user)
    expenses = ExpenseModel.objects.filter(user=request.user)
    context={
        'cash_entries': cash_entries,
        'expenses': expenses,
        
        }
    return render(request, 'cash_dashboard.html',context)



@login_required
def add_expense(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        datetime = request.POST.get('datetime')

        expense = ExpenseModel.objects.create(
            user=request.user,
            description=description,
            amount=amount,
            datetime=datetime
        )

        return redirect('cash_dashboard')  
    
    return render(request, 'add_expense.html')


@login_required
def update_expense_view(request, expense_id):
    expense = ExpenseModel.objects.get(id=expense_id)
    
    context={
        'expense':expense
        }

    if request.method == 'POST':
        expense.description = request.POST['description']
        expense.amount = request.POST['amount']
        expense.datetime = request.POST['datetime']
        expense.save()
        return redirect('cash_dashboard')

    return render(request, 'update_expense.html',context)

@login_required
def delete_expense_view(request, expense_id):
    
    ExpenseModel.objects.get(id=expense_id).delete()
    
    return redirect('cash_dashboard')
def editcash(req):
    
    return render(req,'editcash.html')

