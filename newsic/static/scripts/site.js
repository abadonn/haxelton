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

app.controller("playerController", function($scope, $http, $sce){
	$http.get('api/playlist').then(function(result){
		$scope.data = result.data;
		$scope.soundcloudUrl = $scope.data[0].link;
		setupPlayer($scope.soundcloudUrl);
	});

	$scope.isPlaying = false;
	
	$scope.trustSrc = function() {
    	return $sce.trustAsResourceUrl($scope.soundcloudUrl);
  	};
	  
	function setupPlayer(url){
		angular.element("#jquery_jplayer_1").jPlayer({
			volume: 0.8,
			 muted: false,
			 backgroundColor: '#000000',
			 cssSelectorAncestor: '#jp_container_1',
			 cssSelector: {
			  play: '.jp-play',
			  pause: '.jp-pause',
			  stop: '.jp-stop',
			  next: '.jp-next',
			  prev: '.jp-prev',
			  seekBar: '.jp-seek-bar',
			  playBar: '.jp-play-bar',
			  mute: '.jp-mute',
			  unmute: '.jp-unmute',
			  volumeBar: '.jp-volume-bar',
			  volumeBarValue: '.jp-volume-bar-value',
			  volumeMax: '.jp-volume-max',
			  playbackRateBar: '.jp-playback-rate-bar',
			  playbackRateBarValue: '.jp-playback-rate-bar-value',
			  currentTime: '.jp-current-time',
			  duration: '.jp-duration',
			  title: '.jp-title',
			  gui: '.jp-gui',
			  remainingDuration: true,
        	  toggleDuration: true
			 },
			 errorAlerts: false,
			 warningAlerts: false,
		   ready: function () {
		    angular.element(this).jPlayer("setMedia", {
		     mp3: url,
		    });
		   },
		   supplied: "mp3"
		  });
	} 
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
		if(redirectToUrl === "")
			redirectToUrl = "/profile";
			
		$window.location.href = url.replace("{0}", $scope.username).replace("{1}", $scope.password).replace("{2}", redirectToUrl);
	};
});