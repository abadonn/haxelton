/// <reference path="../../typings/angularjs/angular.d.ts"/>
var app = angular.module('NewsicApp', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

app.controller("profileController", function($scope, $http){
	$scope.currentSlide = 0;
	
	$scope.categories = [];
	$scope.catsILike = [];
	$scope.catsAndSubs = {};
	
	$http.get('api/topiclist').then(function(data){
		$scope.categories = data.data;
	});
	
	$scope.next = function(){
		$scope.currentSlide++;
		angular.element('#carousel-categories').carousel('next');
	};
	
	$scope.like = function(key, likeIt){
		if(likeIt){
			$scope.catsILike.push(key);
		}
		else if($scope.catsILike.indexOf(key) != -1){
			$scope.catsILike.Pop(key);
		}
		if($scope.currentSlide <= Object.keys($scope.categories).length)
			$scope.next();
	};
	
	$scope.select = function(cat, sub){
		
		if($scope.catsAndSubs[cat] !== undefined){
			if($scope.catsAndSubs[cat].indexOf(sub) != -1)
				$scope.catsAndSubs[cat].pop(sub);
			else
				$scope.catsAndSubs[cat].push(sub);
		}
		else{
			$scope.catsAndSubs[cat] = [];
			$scope.catsAndSubs[cat].push(sub);
		}
	};
	
	$scope.complete = function(){
		$http.post('api/saveProfile', {data: $scope.catsAndSubs});
	};
});

app.controller("playerController", function($scope, $http){
	$scope.soundcloudUrl = "https://soundcloud.com/octobersveryown/remyboyz-my-way-rmx-ft-drake";
});

app.controller("userController", function($scope, $window, $location){
	
	$scope.username;
	$scope.password;
	var url = "api/login?username={0}&password={1}&next={2}";
	
	function getParameterByName(name) {
    	name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    	var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        	results = regex.exec(location.search);
    	return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
	}
	
	$scope.login = function(){
		var redirectToUrl = getParameterByName("next");
		$window.location.href = url.replace("{0}", $scope.username).replace("{1}", $scope.password).replace("{2}", redirectToUrl);
	};
});