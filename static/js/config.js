app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "/static/templates/parking.html"
    })
    .when("/main", {
        templateUrl : "/static/templates/main.html"
    })
    .when("/green", {
        templateUrl : "green.htm"
    })
    .when("/blue", {
        templateUrl : "blue.htm"
    });
});
