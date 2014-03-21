// Add a search redo function. Allow for filtering meals, diet, etc.

function RecipeCtrl($scope, $http, $location) {
//    Need to add user selections before food can be passed back.
  $scope.recipe = undefined;
  $http.get('/1/recipe_test/').
      success(function(food){
        console.log(food);
        $scope.food = food;
    });

$scope.loadDeets = function (item) {
    $http.get('http://api.yummly.com/v1/api/recipe/'+item.id + '?_app_id=935e1518&_app_key=b1f4ba0e9b7eb98208ed4a0d44d7cc83').
        success(function(data) {
      recipes.deets = data
    });
  }

}