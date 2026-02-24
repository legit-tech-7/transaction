from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from .models import Transaction
from .forms import DepositForm
from .utils import send_transaction_notification

@login_required
@staff_member_required
def deposit_form(request):
    """Deposit form view - restricted to staff users"""
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            
            # Send email notification
            send_transaction_notification(transaction)
            
            messages.success(request, 'Transaction created successfully!')
            return redirect('transaction_receipt', ref=transaction.transaction_ref)
    else:
        form = DepositForm()
    
    return render(request, 'transactions/deposit_form.html', {
        'form': form,
    })

@login_required
@staff_member_required
def transaction_receipt(request, ref):
    """Transaction receipt view"""
    transaction = get_object_or_404(Transaction, transaction_ref=ref)
    return render(request, 'transactions/receipt.html', {
        'transaction': transaction
    })

@login_required
@staff_member_required
def transaction_list(request):
    """List all transactions"""
    transactions = Transaction.objects.all()
    
    # Search
    search = request.GET.get('search')
    if search:
        transactions = transactions.filter(
            models.Q(transaction_ref__icontains=search) |
            models.Q(sender_name__icontains=search) |
            models.Q(receiver_name__icontains=search)
        )
    
    return render(request, 'transactions/list.html', {
        'transactions': transactions
    })