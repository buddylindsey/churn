var app = angular.module('churn.app', ['ngResource']);

app.factory('Task', ['$resource', function($resource) {
    return $resource('/api/tasks/:id/', { id: '@id' }, {
      update: { method: 'PUT' }
    });
  }
]);


app.controller('AppController', ['$scope', 'Task', function($scope, Task){
  $scope.tasks = Task.query();
  $scope.newTask = new Task();

  $scope.markComplete = function(){
    var task = this.task;
    task.completion_date = new Date();
    task.$update()
  };

  $scope.deleteTask = function(){
    this.task.$delete().then(function(){
      var idx = $scope.tasks.indexOf(this.task);
      $scope.tasks.slice(idx, 1);
    });
  };

  $scope.save = function() {
    $scope.newTask.$save().then(function(result) {
      $scope.tasks.push(result);
    }).then(function() {
      $scope.newTask = new Task();
    });
  };
}]);
