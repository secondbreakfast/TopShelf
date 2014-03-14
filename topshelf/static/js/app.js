/**
 * Created by zhilabug on 3/13/14.
 */

var topshelf = angular.module('topshelf', ['ngRoute']);

//routeProvider is like django's URLs-- specify routes here.
//controllers handle all the logic for the page. Function below is multiple functions strung together.

topshelf.config(['$routeProvider', function($routeProvider){
    $routeProvider.
        when('/app/pantry/', {templateUrl: '/static/views/pantry.html', controller: PantryCtrl}).
        otherwise({redirectTo: '/'});
}]);


