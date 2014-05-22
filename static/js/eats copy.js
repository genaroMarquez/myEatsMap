/* global angular */
var data = angular.module('data',[]);

data.config(function($interpolateProvider) {
    //allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

data.controller('mapController', function mapController($scope, $http) {

    $scope.loadEntries = function() {
        $scope.entries = $http.get('/api/entries/').then(function(response){
            return response.data;
        });
    };

    $scope.loadEntries();

});
