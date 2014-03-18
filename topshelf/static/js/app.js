/**
* Created by zhilabug on 3/13/14.
*/
var app = angular.module('app', ['ngRoute', 'ui.bootstrap']);
app.config(['$routeProvider', function($routeProvider){
    $routeProvider.
        when('/:id/pantry/', {templateUrl: '/static/views/pantry.html', controller: PantryCtrl}).
        when('/:id/recipe/', {templateUrl: '/static/views/recipe.html', controller: RecipeCtrl}).
        otherwise({redirectTo: '/'});
}]);
//Need to add a test recipe page, using the HTTP Response object I created.

///**
//* Created by zhilabug on 3/13/14.
//*/
//angular.module('app', ['ui.bootstrap']);
//
//function TypeaheadCtrl($scope, $http) {
////   $http.get("/app/"+$routeParams.id+"/pantry/").success(function(data) {
////                 $scope.record = data;
////        });
//  $scope.pantry = undefined;
//  $http.get('http://127.0.0.1:8000/api/v1/all_ingredients/?format=json&limit=0').
//      success(function(food){
//    //    On success, it passes in the returned item and puts it into a scope variable with the label food.
////          $scope.list_items = food.objects;
//          list_items = []
////          Note: Below probably isn't the most efficient way to do this.
//          for (var i = 0; i < food.objects.length; i++){
//              list_items.push(food.objects[i].ing)
//          }
////          console.log(food.objects);
//          console.log(list_items);
//          $scope.list_items = list_items;
//    });
//
//  $scope.submitForm = function() {
//      console.log($scope.pantry);
//  $http.post('/api/v1/pantry/?format=json', $scope.pantry).
//        success(function(response){
//          console.log($scope.pantry);
//            $location.path("/");
//        })
//    }
//}
