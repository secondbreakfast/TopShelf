function PantryCtrl($scope, $http, $location) {
  $scope.pantry = undefined;
  $http.get('/api/v1/all_ingredients/?format=json&limit=0').
      success(function(food){
          list_items = []
//          Note: Below probably isn't the most efficient way to do this.
          for (var i = 0; i < food.objects.length; i++){
              list_items.push(food.objects[i].ing)
          }
          console.log(list_items);
          $scope.list_items = list_items;

          $scope.list_items = food.objects;
    });

  $scope.submitForm = function() {

      $http.post('/api/v1/pantry/?format=json', $scope.pantry).
            success(function(response){
                console.log($scope.pantry);
                $location.path("/:id/pantry/");
        })
    }
}
