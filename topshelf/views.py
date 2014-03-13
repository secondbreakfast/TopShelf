import requests

from topshelf.forms import IngredForm

#When a user adds it to their database, add a count to their ingredients.
# Add about page?
# Need to enable login

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from topshelf.forms import SignupForm, LoginForm



from topshelf.models import UserIngred


def index(request):
    return render(request, "index.html")

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

#Initialized login page, authenticates, and redirects to pantry. Maybe make a user dashboard?
def login_page(request):
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],)
            if user is not None:
                login(request, user)
                return redirect("/{}/pantry".format(user.id))
    else:
        form = LoginForm
    data = {"form": form}
    return render(request, "signup.html", data)

def logout_page(request):
    logout(request)

#Activate this when we want login to work. Need to link it to a user profile.
# @login_required
def pantry(request, user_id):
    if request.method=="POST":
        form = IngredForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("{}/pantry/".format(user_id))
    else:
        form = IngredForm()
    data = {'form': form}
    return render(request, "pantry.html", data)


#Change this later to show which ingredients the user is missing.
def recipe(request, user_id):
    # print date.now()

    # Produces the user's ingredients as a list, which is then compared with the recipes.

    ingred = []
    user_test = UserIngred.objects.filter(user=request.user)
    for item in user_test:
        ingred.append(item.ing_master)
    #     {% for food in match %}
    #     {{ food.ing_master }}
    # {% endfor %}

    # # ingred = ["tomatoes", "kale", "fresh lemon juice", "large garlic cloves", "unsalted butter", "vegetable oil", "flat leaf parsley", "capers", "mushrooms"]
    # recipes = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83&allowedIngredient[]=garlic&allowedIngredient[]=mushroom&maxResult=10')
    # recipes = recipes.json()
    #
    # #make results a dictionary to feed to homepage.
    # goodFood = {}
    # for item in recipes['matches']:
    #     # match = item['ingredients']
    #     recipe_ing = item['ingredients']
    #     if not set(recipe_ing) - set(ingred):
    #         name = item['recipeName']
    #         recipe_id = item['id']
    #         source = item['sourceDisplayName']
    #         img = item['smallImageUrls']
    #         goodFood[name] = {}
    #         goodFood[name]['recipe_id'] = recipe_id
    #         goodFood[name]['source'] = source
    #         goodFood[name]['img'] = img
    #     # else:
    #     #     match = "Not a match!"
    #     data = {"match": goodFood}

    data = {"match": ingred}
    return render(request, "recipe.html", data)
    # return render(request, "recipe.html", data)

def favorites(request):
    data = {"hi": "Your favorite recipes"}
    return render(request, "favorite.html", data)