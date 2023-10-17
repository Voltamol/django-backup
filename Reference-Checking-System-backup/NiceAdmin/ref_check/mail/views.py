from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from analytics.models import Referee

def email(request):
    if request.method == 'POST':
        
        html_message = render_to_string('email_template.html', {'variable': 'value'})
        plain_message = strip_tags(html_message)
        from_email = 'seanchirenje@gmail.com'  # Replace with your email
        #to_email = 'lordvoltamol@gmail.com'  # Replace with the recipient's email
        referee=Referee.objects.first()
        subject = 'Hello {0}! please verify the following candidates on our website'.format(referee.referee_name) #
        send_mail(
            subject, 
            plain_message, 
            from_email, 
            [referee.company_email], 
            html_message=html_message
        )
        return HttpResponse("email sent successfully...")
    else:
        return render(request,'mail/sendmails.html')
    