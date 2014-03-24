function PantryCtrl($scope, $http, $routeParams, Data) {
//    Sets scope to the service variable called Data, which shares this variable between the two controllers.
  $scope.queryParams = Data;

// Gets user's id from URL, which is used to send data back to django views.
   var id = $routeParams.id;

//    Gets the master list of ingredients, which the user can add to their pantry.
// The user's ingredients are a subset of the master list.
// This is for data consistency and will be useful later once the recipe data is normalized.

  $scope.pantry = undefined;
  $http.get('/api/v1/all_ingredients/?format=json&limit=0').
      success(function(food){
          list_items = []

//    Old way to populate list of autocomplete items.
////          Note: Below probably isn't the most efficient way to do this.
//          for (var i = 0; i < food.objects.length; i++){
//              list_items.push(food.objects[i].ing_test)
//          }
////          $scope.list_items = list_items;

//     This populates the autocomplete in pantry.html.
          $scope.list_items = food.objects;
    });

//    Takes the ingredients a user selects and adds it to their personal inventory.
//    A user's inventory is a subset of the master list of ingredients.
  $scope.submitForm = function() {
      $http.post('/api/v1/pantry/?format=json', $scope.pantry).
            success(function(response){
//                console.log($scope.pantry);
                $location.path("/pantry/");
        })
    }

//   Gets the user's pantry. (List of ingredients that they have at home).
  $http.get('/api/v1/pantry/?format=json').
      success(function(user_pantry_list){
          $scope.pantry_data = user_pantry_list.objects;
    });


//Deletes an item from a user's inventory. Not working, as of now.
  $scope.deleteItem = function(item) {
      console.log(item);
      $http.delete(item.resource_uri + '?format=json').
          success(function(){
             console.log("Item deleted!")
        });
    }

    //Sends the user's preferences to an API, which will be called in the recipe search.
  $scope.recipeSearchForm = function(queryParams) {
      Data = queryParams

//      Extracts ingredients that will be used as search parameters.
//      Builds query text so that it can be passed to the django view. I'll eventually add more search params here.
      include1 = "&allowedIngredient[]=" + queryParams.first.ing_master.ing_test
      include2 = "&allowedIngredient[]=" + queryParams.second.ing_master.ing_test
      include3 = "&allowedIngredient[]=" + queryParams.third.ing_master.ing_test

      $http.get('/'+id+'/recipe_data/?queryParams='+include1+include2+include3).
            success(function(params) {
//              Testing out what the search parameters actually look like.
//              They are formatted in the same way as required by the yummly api.
                console.log(include1+include2+include3);
        });
      }
}
