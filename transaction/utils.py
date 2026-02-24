from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_transaction_notification(transaction):
    """Send email notification to receiver"""
    try:
        subject = f'Transaction Notification - {transaction.transaction_ref}'
        
        context = {
            'transaction': transaction,
            'amount': f"{transaction.amount:,.2f}",
            'date': transaction.created_at.strftime('%Y-%m-%d'),
            'time': transaction.created_at.strftime('%H:%M:%S')
        }
        
        html_message = render_to_string('emails/transaction_notification.html', context)
        plain_message = render_to_string('emails/transaction_notification.txt', context)
        
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[transaction.receiver_email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False