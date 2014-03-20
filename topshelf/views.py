import difflib
import json
from django.http import HttpResponse
import requests

from topshelf.forms import IngredForm

# Additional features:
#When a user adds it to their database, add a count to their ingredients.

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from topshelf.forms import SignupForm, LoginForm
from topshelf.models import UserIngred, IngredMaster


def angular(request):
    return render(request, 'base.html')

def index(request):
    return render(request, "index.html")
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
                return redirect("/{}/pantry".format(user.id))
    else:
        form = LoginForm
    data = {"form": form}
    return render(request, "signup.html", data)

# def pantry(request, user_id):
#     if request.method=="POST":
#         form = IngredForm(request.POST)
#         if form.is_valid():
#             if form.save():
#                 return redirect("{}/pantry/".format(user_id))
#     else:
#         form = IngredForm()
#     data = {'form': form}
#     return render(request, "pantry.html", data)

# Test view. Don't want to mess up the original.
# Need to let user pick 3 ingredients for API call. Add this functionality later, if needed.

# Note: look up model_to_dict for re-importing data, or make another element that stores "contains" info from the new list.
def recipe1(request, user_id):
    # Empty list to add ingredients from the user's pantry.
    ingred_part1 = []
    user_test = UserIngred.objects.filter(user=request.user)
    for item in user_test:
        ingred_part1.append(item.ing_master.ing_test)

    # # Some recipes have water as an ingredient-- users might forget to add those, so they're added here to the search. Salt is also included.
    ingred_part2 = ["water", "ice", "hot water", "cool water", "warm water", "lukewarm water", "salt", "table salt"]
    ingred = ingred_part1 + ingred_part2

    # # Sample output for ingred below.
    # ingred = ["kale", "lemon juice", "tomatoes", "garlic cloves", "butter", "vegetable oil", "flat leaf parsley", "capers", "mushrooms"]
    recipes = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83&maxResult=1000')
    recipes = recipes.json()

    ingred.sort()

    match = []
    for item in recipes['matches']:
        s = difflib.SequenceMatcher(None, ingred, item['ingredients'], autojunk=True).ratio()
        if s > .04:
            item['ratio']= s
            match.append(item)

    return HttpResponse(json.dumps(match),content_type='application/json')


# User.objects.filter(reduce(operator.or_, (Q(first_name__contains=x) for x in ['x', 'y', 'z'])))
#
# for x in [1,2,3]:
#     Q(first_name__containes=x)
#
# Q(first_name__contains=1) | Q(first_name__contains=2) | Q(first_name__contains=3)










# # Need to let user pick 3 ingredients for API call.
# def recipe(request, user_id):
#     # form = RecipeForm()
#     ingred = []
#     user_test = UserIngred.objects.filter(user=request.user)
    # Some recipes have water as an ingredient-- users might forget to add those, so they're added here to the search. Salt is also included.
    # more_ingreds = ["water", "ice", "hot water", "cool water", "warm water", "lukewarm water", "salt", "table salt"]
    # ingred = ingred + more_ingreds

#     for item in user_test:
#         ingred.append(item.ing_master.ing)
#     # # ingred = ["kale", "tomatoes", "fresh lemon juice", "large garlic cloves", "unsalted butter", "vegetable oil", "flat leaf parsley", "capers", "mushrooms"]
#     recipes = requests.get('http://api.yummly.com/v1/api/recipes?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83&allowedIngredient[]=garlic&allowedIngredient[]=mushroom&maxResult=1000')
#     recipes = recipes.json()
#
#     match = []
#     for item in recipes['matches']:
#         recipe_ing = item['ingredients']
#         if not set(recipe_ing) - set(ingred):
#             match.append(item)
#
#             # Tried making an object out of
#             # name = item['recipeName']
#             # recipe_id = item['id']
#             # source = item['sourceDisplayName']
#             # img = item['smallImageUrls']
#             # match[name] = {}
#             # match[name]['recipe_id'] = recipe_id
#             # match[name]['source'] = source
#             # match[name]['img'] = img
#         # else:
#         #     match = "Not a match!"
#        data = {"match": match, "ingred": ingred}
#
#     return render(request, "recipe.html", data)
#
#     # data = {"match": ingred}
#     # return render(request, "recipe.html", data)
#

def recipe_detail(request, user_id):
    recipes = requests.get('http://api.yummly.com/v1/api/recipe/Garlic-butter-roasted-mushrooms-305440?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83&')
    match = recipes.json()

    data = {"match": match}
    return render(request, "recipeDetail.html", data)

def favorites(request):
    data = {"hi": "Your favorite recipes"}
    return render(request, "favorite.html", data)
