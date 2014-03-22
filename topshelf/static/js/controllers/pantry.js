function PantryCtrl($scope, $http, $location, foodChoices) {
  $scope.queryParams = foodChoices.sharedObject;
//    Gets the full list of ingredients, which the user can add to their pantry.
  $scope.pantry = undefined;
  $http.get('/api/v1/all_ingredients/?format=json&limit=0').
      success(function(food){
          list_items = []
//          Note: Below probably isn't the most efficient way to do this.
          for (var i = 0; i < food.objects.length; i++){
              list_items.push(food.objects[i].ing_test)
          }
//          $scope.list_items = list_items;

          $scope.list_items = food.objects;
    });

//    Takes the ingredients they select and adds it to their inventory.
  $scope.submitForm = function() {
      $http.post('/api/v1/pantry/?format=json', $scope.pantry).
            success(function(response){
//                console.log($scope.pantry);
                $location.path("/:id/pantry/");
        })
    }

//   Gets the user's pantry. (List of ingredients that they have at home).
  $http.get('/api/v1/pantry/?format=json').
      success(function(user_pantry_list){
          $scope.pantry_data = user_pantry_list.objects;
    });


//    Takes the ingredients they select and adds it to their inventory.
  $scope.submitForm = function() {
      $http.post('/api/v1/pantry/?format=json', $scope.pantry).
            success(function(response){
//                console.log($scope.pantry);
                $location.path("/:id/pantry/");
        })
    }

//Deletes an item from a user's inventory. Not working, as of now.
  $scope.deleteItem = function(ingredient) {
      console.log(ingredient);
      $http.delete(ingredient + '?format=json').
          success(function(){
             console.log("Item deleted!")
        });
    }

    //Sends the user's preferences to an API, which will be called in the recipe search.
  $scope.recipeSearchForm = function(queryParams) {
        $http.get('/1/recipe/?queryParams='+queryParams.first.ing_master.ing_test).
            success(function(data) {
                console.log(queryParams.first.ing_master.ing_test);
        });
      }
}
