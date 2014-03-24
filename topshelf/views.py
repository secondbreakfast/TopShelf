import difflib
import json
from django.http import HttpResponse
import requests

from topshelf.forms import IngredForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from topshelf.forms import SignupForm, LoginForm
from topshelf.models import UserIngred, IngredMaster

def index(request):
    return render(request, "index.html")

def angular(request):
    return render(request, 'base.html')

#
# def about(request):
#     return render(request, "about.html")

def signup(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
             user = User.objects.create_user(
             form.cleaned_data["username"],
             form.cleaned_data["email"],
             form.cleaned_data["password"],
            )
    else:
        form = SignupForm()
    data = {'form': form}
    return render(request, "signup.html", data)


#Initialized login page, authenticates, and redirects to pantry.
def login_page(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],)
            if user is not None:
                login(request, user)
                return redirect("/app/#/{}/pantry".format(user.id))
    else:
        form = LoginForm
    data = {"form": form}
    return render(request, "signup.html", data)

# Gets the user's preferences from pantry.js (passed as a search parameter) and uses it in the Yummly web API search.
def recipe(request, user_id):
    api_params = request.GET.get('queryParams')
    # Sample API search params, defined by the user:
    # &allowedIngredient[]=almonds&allowedIngredient[]=flour&allowedIngredient[]=soymilk

    # Pull ingredients from the user's pantry into a list, for comparision with recipe ingredients.
    ingred = []
    user_test = UserIngred.objects.filter(user=request.user)
    for item in user_test:
        ingred.append(item.ing_master.ing_test)

    # Sample output for user ingredients list below.
    # ingred = ["kale", "lemon juice", "tomatoes", "garlic cloves", "butter", "vegetable oil", "flat leaf parsley", "capers", "mushrooms"]

    # API call pulls 500 recipes to filter through. This number will change as the data gets normalized, and more efficient.
    recipes = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83'+api_params+'&maxResult=500')
    recipes = recipes.json()

    # Sorts ingredients by alpha order. Not sure if this actually helps the matching go faster, but it may.
    ingred.sort()

    # This section compares the text in the user's ingredients record with each recipe's set of ingredients.
    # It's not great, but is a quick way to get some results. This will change substantially as the data gets normalized.
    # Right now, this just uses a library (DiffLib) to compare text and assigns a similarity ratio. Not great, but ok.
    match = []
    for item in recipes['matches']:
        match_ratio = difflib.SequenceMatcher(None, ingred, item['ingredients'], autojunk=True).ratio()
        greatest_ratio = 0
        if match_ratio > .04:
            if match_ratio > greatest_ratio:
                greatest_ratio = match_ratio
                item['ratio']= match_ratio
                match.insert(0, item)
            else:
                match.insert(-1, item)
    return HttpResponse(json.dumps(match),content_type='application/json')

# Searches for individual recipe detail. This only fires when a user clicks on a recipe record at recipe.html
def recipe_detail(request, user_id):
    recipe_id = request.GET.get('recipe_id')
    resp = requests.get("http://api.yummly.com/v1/api/recipe/{0}?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83".format(recipe_id))
    recipe_data = resp.json()
    data = {"recipe_data":recipe_data}

    return HttpResponse(json.dumps(data),content_type='application/json')
