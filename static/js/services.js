


app.factory("parkingHttpFacade", ["$http", function ($http) {


    var _getCars = function() {
        return $http.get("/api/cars");
    };
    var _saveCar = function(car) {
            var req = {
                method: 'POST',
                url: '/api/cars',
                headers: {'Content-Type': 'application/json'},
                data: { plate: car }
            }
        return $http(req);
    };
    return {
        getCars: _getCars,
        saveCar: _saveCar
    };
}]);

