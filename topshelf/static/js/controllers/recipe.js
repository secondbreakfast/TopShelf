// Add a search results filter and search redo.

function RecipeCtrl($scope, $http, $routeParams, Data) {
  queryParams = Data;
//    Test to make sure the angular service works.
  console.log(Data);

// Gets user id, which is used below to load and collect data from django views.
   var id = $routeParams.id;

  $scope.recipe = undefined;

//      Extracts ingredients that will be used as search parameters. This isn't DRY. Also used in pantry.js.
//       Will work on DRYness later.
//      Builds query text so that it can be passed to the django view. I'll eventually add more search params here.
      include1 = "&allowedIngredient[]=" + queryParams.first.ing_master.ing_test
      include2 = "&allowedIngredient[]=" + queryParams.second.ing_master.ing_test
      include3 = "&allowedIngredient[]=" + queryParams.third.ing_master.ing_test

      $http.get('/'+id+'/recipe_data/?queryParams='+include1+include2+include3).
            success(function(food) {
//              Testing out what the search parameters actually look like.
//              They are formatted in the same way as required by the yummly api.
                console.log(include1+include2+include3);
                $scope.food = food
        });

//    Sample query from above. Need to add other parameters.
//    http://127.0.0.1:8000/1/recipe_data/?queryParams=almonds


  $scope.loadDeets = function(item) {
        $http.get('/'+id+'/recipe_detail_data/?recipe_id='+item.id).
            success(function(data) {
                $scope.deets = data;
                console.log(data);
        });
      }
}



