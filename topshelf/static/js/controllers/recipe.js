// Add a search redo function. Allow for filtering meals, diet, etc.

function RecipeCtrl($scope, $http, $location) {
//    Need to add user selections before food can be passed back.
  $scope.recipe = undefined;
  $http.get('/1/recipe_test/').
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



