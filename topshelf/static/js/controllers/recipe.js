function RecipeCtrl($scope, $http, $routeParams, $location, Data) {
//   Gets user search preferences, launches search and returns results.
//   This will be dynamic and allow the user to redo their search in the same window.

    $scope.recipe = undefined;
    var id = $routeParams.id;
    console.log(id);

    $scope.feedLimit = 5;

    $http.get('/api/v1/pantry/?format=json').
        success(function(user_pantry_list){
            console.log(user_pantry_list);
            $scope.pantry_list = user_pantry_list.objects;
        });

    $scope.loadData = function(){
        //  Loads user's query parameters, to fetch search results in loadData.
        queryParams = Data;
        //    Test to make sure the angular service works.
        console.log(Data);

        //      Extracts ingredients that will be used as search parameters. This isn't DRY. Also used in pantry.js.
        var include1 = "%26allowedIngredient[]=" + queryParams.first.ing_master.ing_test;
        console.log(include1);
        var include2 = "%26allowedIngredient[]=" + queryParams.second.ing_master.ing_test;
        var include3 = "%26allowedIngredient[]=" + queryParams.third.ing_master.ing_test;
        // Gets user id, which is used below to load and collect data from django views.

//      Builds query text so that it can be passed to the django view. I'll eventually add more search params here.
        $http.get('/'+id+'/recipe_data/?queryParams='+include1+include2+include3).
            success(function(food) {
//              Testing out what the search parameters actually look like.
                console.log(include1+include2+include3);
                $scope.food = food
            });


    }

    //Loads user data on open.
    $scope.loadData();


//Once the user clicks on a recipe, it displays recipe details. The data is not loaded until the user clicks.
    $scope.loadDeets = function(item) {
        $http.get('/'+id+'/recipe_detail_data/?recipe_id='+item.id).
            success(function(data) {
                $scope.deets = data;
                console.log($scope.deets);
            });
    }
}



