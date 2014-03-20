function RecipeCtrl($scope, $http, $location) {
//    Need to add user selections before food can be passed back.
  $scope.recipe = undefined;
  $http.get('/:id/recipe_test/').
      success(function(food){
        console.log(food);
        $scope.food = food;
    });

}
