from django.http import HttpResponse
from django.core.mail import send_mail


def sendmail(request):

    send_mail(subject='vaqti',
              message='', 
              from_email='odina3194@gmail.com',
              recipient_list=['mamajonovibrokhimjon@gmail.com'],
              fail_silently=False)
    return HttpResponse("email jo'natildi")