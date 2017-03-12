var app = angular.module('sparql', []);

app.controller('MainCtrl', function($scope, $http) {
  $scope.name = 'World';
  
  $http({
    url: 'http://10.201.0.89:8890/sparql', 
    headers: { 'Content-type' : 'application/x-www-form-urlencoded',
            'Accept' : 'application/sparql-results+json' },
    method: "GET",
    params: {
            query : "select ?s ?p ?o where {?s ?p ?o} limit 20",
            format: "json"
        }
  })
  
  .success(function(data, status, headers, config) {
    $scope.results = data.results.bindings;
   })
   
  .error(function(data, status, headers, config) { 
  });
 
 
  
});
