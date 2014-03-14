/**
 * Created by zhilabug on 3/13/14.
 */

function PantryCtrl($scope, $http) {
    $http.get('/api/v1/all_ingredients/?format=json').
        //        Creates new object called students, on success.
        success(function(pantry){
            console.log("yay!");
//            $scope.pantry = pantry.objects;
        });
}

