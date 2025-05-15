from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate form data
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'registration.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'registration.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('create_profile')  # Redirect to the login page after registration

    return render(request, 'registration.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# profile creation

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def add_profile_details_view(request):
    # Get the profile for the logged-in user
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Get data from the form
        bio = request.POST.get('bio')
        mood_preference = request.POST.get('mood_preference')
        profile_picture = request.FILES.get('profile_picture')

        # Update the profile object
        profile.bio = bio
        profile.mood_preference = mood_preference
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()

        # Redirect to the profile page after saving
        return redirect('profile')

    # Render the form template
    return render(request, 'createProfile.html', {'profile': profile})





def login_view(request):
    if request.method == 'POST':
         # Get username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'Login successful!')
            
            return redirect('home')  # Redirect to the profile page or any other page
        else:
            # Invalid credentials
            messages.error(request, 'Invalid username or password.')
        

        
    return render(request, 'login.html')




def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user': request.user, 'profile': profile})


# profile creation or editing


@login_required
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        mood_preference = request.POST.get('mood_preference')
        profile_picture = request.FILES.get('profile_picture')

        profile.bio = bio
        profile.mood_preference = mood_preference
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()

        return redirect('profile')  # Redirect to the profile page

    return render(request, 'createProfile.html', {'profile': profile})



from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


#used to automatically create a profile when a user is created
# signals.py
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

