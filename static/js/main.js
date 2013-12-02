var app = angular.module('churn.app', []);

app.controller('AppController', ['$scope', '$http', function($scope, $http){
  $scope.tasks = [];
  $http.get('/api/tasks/').then(function(result){
    angular.forEach(result.data, function(item){
      $scope.tasks.push(item);
    });
  });
}]);

app.controller('EditController', ['$scope', '$http', function($scope, $http){
  $scope.save = function(){
    data = {title: $("#title").val()}
    $http.post('/api/tasks/', data).success(function(result){
      $scope.tasks.push(result);
    });
  };
}]);
