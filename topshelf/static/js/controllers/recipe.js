// Add a search redo function. Allow for filtering meals, diet, etc.

function RecipeCtrl($scope, $http, $location, foodChoices) {
  $scope.queryParams = foodChoices.sharedObject;
  $scope.recipe = undefined;
  $http.get('/1/recipe/').
      success(function(food){
        console.log(food);
        $scope.food = food;
    })

  $scope.loadDeets = function(item) {
        $http.get('/1/recipe_detail/?recipe_id='+item.id).
            success(function(data) {
                $scope.deets = data;
                console.log(data);
        });
      }
}



