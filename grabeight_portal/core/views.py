from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#Dashboard page
@login_required #hindi pwedeng ma-access kapag hindi logged in
def dashboard(request):
    return render(request,'dashboard.html')

#Employee profile page
@login_required  # ❗ protected din
def profile(request):
    return render(request,'profile.html')