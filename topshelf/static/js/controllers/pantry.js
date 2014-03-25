function PantryCtrl($scope, $http, $routeParams, $location, Data) {
//    Sets scope to the service variable called Data, which shares this variable between the two controllers.
    $scope.queryParams = Data;
//  Gets user id from url and prints it in console.
    var id = $routeParams.id;
    console.log(id);
    $scope.id = id;

//    Gets the master list of ingredients, which the user can add to their pantry.
// The user's ingredients are a subset of the master list.
// This is for data consistency and will be useful later once the recipe data is normalized.

    $scope.pantry = undefined;

    $http.get('/api/v1/all_ingredients/?format=json&limit=0').
        success(function(food){
            list_items = []
//     This populates the autocomplete in pantry.html.
            $scope.list_items = food.objects;
        });

//   Gets the user's pantry. (List of ingredients that they have at home).
    $scope.loadData = function(){
        $http.get('/api/v1/pantry/?format=json').
            success(function(user_pantry_list){
                $scope.pantry_data = user_pantry_list.objects;
            });
    }
    //Loads user data on open.
    $scope.loadData();

//    Takes the ingredients a user selects and adds it to their personal inventory.
//    A user's inventory is a subset of the master list of ingredients.
    $scope.submitForm = function() {
        $http.post('/api/v1/pantry/?format=json', $scope.pantry).
            success(function(response){
              $scope.loadData();
            })
    }

//Deletes an item from a user's inventory. Not working, as of now.
    $scope.deleteItem = function(item) {
        console.log(item);
        $http.delete(item.resource_uri + '?format=json').
            success(function(){
                console.log("Item deleted!")
                $scope.loadData();
            });
    }

//  Sends the user's preferences to an API, which will be called in the recipe search.
    $scope.recipeSearchForm = function(queryParams, id) {
//      This sets the data for the service, which is accessed by the other controller.
        Data = queryParams;

//      Extracts ingredients that will be used as search parameters.
//      Builds query text so that it can be passed to the django view. I'll eventually add more search params here.
//      This isn't DRY. I'll work on it!
        var include1 = "%26allowedIngredient[]=" + queryParams.first.ing_master.ing_test;
        var include2 = "%26allowedIngredient[]=" + queryParams.second.ing_master.ing_test;
        var include3 = "%26allowedIngredient[]=" + queryParams.third.ing_master.ing_test;

        $http.get('/'+id+'/recipe_data/?queryParams='+include1+include2+include3).
            success(function(params) {
//              Testing out what the search parameters actually look like.
//              They are formatted in the same way as required by the yummly api.
                console.log(include1+include2+include3);
//                console.log(id);
            });
    }


}
