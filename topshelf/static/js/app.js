///**
// * Created by zhilabug on 3/13/14.
// */
//
//var app = angular.module('topshelf', ['ngRoute'], ['autocomplete']);
//
////routeProvider is like django's URLs-- specify routes here.
////controllers handle all the logic for the page. Function below is multiple functions strung together.
//
//app.config(['$routeProvider', function($routeProvider){
//    $routeProvider.
//        when('/', {templateUrl: '/static/views/pantry.html', controller: PantryCtrl}).
//        otherwise({redirectTo: '/'});
//}]);

angular.module('plunker', ['ui.bootstrap']);
function TypeaheadCtrl($scope, $http, $location) {

  $scope.pantry = undefined;
  $http.get('http://127.0.0.1:8000/api/v1/all_ingredients/?format=json&limit=0').
      success(function(classes){
    //    On success, it passes in the returned item and puts it into a scope variable with the label classes.
//          $scope.states = classes.objects;
          states = []
//          Note: Below probably isn't the most efficient way to do this.
          for (var i = 0; i < classes.objects.length; i++){
              states.push(classes.objects[i].ing)
          }
//          console.log(classes.objects);
          console.log(states);
          $scope.states = states;
    });

  $scope.submitForm = function() {
  $http.post('/api/v1/pantry/?format=json', $scope.pantry).
        success(function(response){
            $location.path("/");
        })
    }
}