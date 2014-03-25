// Add a search results filter and search redo. 

function RecipeCtrl($scope, $http, $routeParams, $location, Data) {
    $scope.recipe = undefined;

    queryParams = Data;
    //    Test to make sure the angular service works.
    console.log(Data);

//      Extracts ingredients that will be used as search parameters. This isn't DRY. Also used in pantry.js.
    var include1 = "%26allowedIngredient[]=" + queryParams.first.ing_master.ing_test;
    console.log(include1);
    var include2 = "%26allowedIngredient[]=" + queryParams.second.ing_master.ing_test;
    var include3 = "%26allowedIngredient[]=" + queryParams.third.ing_master.ing_test;


// Gets user id, which is used below to load and collect data from django views.
    var id = $routeParams.id;
    console.log(id);

//      Builds query text so that it can be passed to the django view. I'll eventually add more search params here.
    $http.get('/'+id+'/recipe_data/?queryParams='+include1+include2+include3).
        success(function(food) {
//              Testing out what the search parameters actually look like.
            console.log(include1+include2+include3);
            $scope.food = food
        });

    $scope.loadDeets = function(item) {
        $http.get('/'+id+'/recipe_detail_data/?recipe_id='+item.id).
            success(function(data) {
                $scope.deets = data;
                console.log(data);
            });
    }
}



