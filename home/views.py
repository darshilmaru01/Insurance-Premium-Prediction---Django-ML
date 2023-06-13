from django.shortcuts import render, HttpResponse
import joblib
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

model = joblib.load('static/random_forest_regressor')

# Create your views here.
def home(request):
    # return HttpResponse("This is the home page") 
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("This is the about page") 
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("This is the contact page") 
    return render(request, 'contact.html')

def login(request):
    # return HttpResponse("This is the login page") 
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Registration successful. Welcome, {username}!")
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration.html', {'form': form})

def prediction(request):
    # return HttpResponse("This is the prediction page")
    if request.method == "POST":
        # print("enter into the post request")
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        # print(age, bmi, sex, children, smoker, region)

        pred = round(model.predict([[age, sex, bmi, children, smoker, region]])[0])

        # print(pred)

        output = {
            "output": pred
        }

        return render(request, 'prediction.html', output)

    else:
        return render(request, 'prediction.html')


