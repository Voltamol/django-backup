from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from analytics.models import Referee

def email(request):
    if request.method == 'POST':

        referees = Referee.objects.all()
        url_template:str=request.POST.get('url')
        for referee in referees:
            recipient = referee.company_email

            # Customize email content for each recipient
            url = "".join([url_template,"/",recipient]) # Replace 'example.com' with your actual website domain
            html_message = render_to_string('mail/email_template.html', {'variable': 'value', 'url': url})
            plain_message = strip_tags(html_message)
            from_email = 'seanchirenje@gmail.com'  # Replace with your email
            subject = 'Hello {0}! Please verify the following candidates on our website'.format(referee.referee_name)

            send_mail(
                subject,
                plain_message,
                from_email,
                [recipient],
                html_message=html_message
            )

        return HttpResponse("Emails sent successfully...")
    else:
        return render(request, 'mail/sendmails.html')
    

def referee_redirect(request,referee_email):
    return HttpResponseRedirect(reverse('analytics:referee_candidate_list',args=(referee_email,)))
    ...