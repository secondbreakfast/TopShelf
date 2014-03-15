/**
 * Created by zhilabug on 3/13/14.
 */

//Every controller has $scope built into it. Will take in more values as the file gets larger.

function PantryCtrl($scope, $http) {
//    Generic format for making a get call, using HTTP library. Uses a period instead of {} to link items.
    $http.get('/api/v1/pantry/?format=json').
        //        Creates new object called students, on success.
        success(function(pantry){
//            Sets a student variable. Need to use students.objects because it will include metadata and get an error. Will not allow you to loop through.
            $scope.pantry = pantry.objects;
        });

}