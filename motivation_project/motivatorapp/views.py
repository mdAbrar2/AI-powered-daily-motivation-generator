from django.shortcuts import render
from authen.models import Profile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# from .models import Profile
# from django.contrib.auth.models import User
# Create your views here.

def home(request):
    profle = Profile.objects.get(user=request.user) 
    return render(request, 'home.html',{'profile': profle})

# def motivator(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         motivation = request.POST.get('motivation')
#         return render(request, 'motivator.html', {'name': name, 'motivation': motivation})
#     else:
#         return render(request, 'motivator.html')

# # motivator/views.py
# import requests
# from django.shortcuts import render
# from .models import DailyQuote
# from django.utils import timezone



def welcomePage(request):
    return render(request,'WelcomePage.html')

    



# motivator/utils.py
import requests
from django.core.mail import send_mail

def fetch_quote():
    response = requests.get("https://zenquotes.io/api/today")
    if response.status_code == 200:
        data = response.json()[0]
        return f"{data['q']} — {data['a']}"
    return "Stay strong. Keep moving forward. — Unknown"

# def send_motivation_email(request,recipient):
#     quote = fetch_quote()
#     print(quote)
#     subject = "Your Daily Dose of Motivation 💪"
#     message = f"Hello!\n\nHere's your motivational quote for today:\n\n{quote}\n\nHave a great day!"
    
#     send_mail(
#         subject,
#         message,
#         None,
#         [recipient],
#         fail_silently=False,
#     )

#     return render(request,'startjourney.html',{'quote': quote})


@login_required
def send_motivation_email(request):
    # Get the recipient email from the logged-in user
    recipient = request.user.email

    # Fetch the motivational quote
    quote = fetch_quote()

    # Email subject and message
    subject = "Your Daily Dose of Motivation 💪"
    message = f"Hello!\n\nHere's your motivational quote for today:\n\n{quote}\n\nHave a great day!"

    # Send the email
    #   

    result = send_mail(
    subject,
    message,

    settings.DEFAULT_FROM_EMAIL,
    [recipient],
    fail_silently=False,
   )
    print(result)  # Should print 1 if the email was sent successfully


    # Render the start journey page
    return render(request, 'startjourney.html', {'quote': quote})




