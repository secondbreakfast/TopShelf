/**
* Created by zhilabug on 3/13/14.
*/
var app = angular.module('app', ['ngRoute', 'ui.bootstrap']);
app.factory("foodChoices", function(){
      return {
    sharedObject: { queryParams: 'default' }
  };
});
app.config(['$routeProvider', function($routeProvider){
    $routeProvider.
        when('/:id/pantry/', {templateUrl: '/static/views/pantry.html', controller: PantryCtrl}).
        when('/:id/recipe/', {templateUrl: '/static/views/recipe.html', controller: RecipeCtrl}).
        otherwise({redirectTo: '/'});
}]);
