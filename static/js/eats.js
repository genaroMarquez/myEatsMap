//Ideas
//Create a marker event listener
//if event then return lat/lng
//if lat/lng correspond to marker lat/lng then update


var map = angular.module("map", ['leaflet-directive']);
map.controller("MapController", function($scope, $http, leafletEvents) {
    angular.extend($scope, {
        dc: {
            lat: 38.8951,
            lng: -77.0367,
            zoom: 13
        },
		defaults: {
			tileLayer: 'https://{s}.tiles.mapbox.com/v3/gmarquez.h2jefa94/{z}/{x}/{y}.png',
		},
	});
	
	$scope.markers = new Array();
	
    $scope.entries = $http.get('/api/entries/').then(function(response){
		angular.forEach(response.data, function(value, key) {
			$scope.markers.push({
				lat:Number(value.lat),
				lng:Number(value.lng),
				message:String(value.score),
				id:value.id,
			});
		});
	});
	
    $scope.events = {
        markers: {
            enable: leafletEvents.getAvailableMarkerEvents(),
        }
    };
	
	$scope.$on('leafletDirectiveMarker.dblclick', function(event, args){
		console.log(args.leafletEvent.latlng.lat);
	});

	

});
