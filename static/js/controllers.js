      app.controller('myCtrl', function($scope, $http, parkingHttpFacade) {



/*    $http.get("/api/todo1")
      .success(function(data, status, headers, config) {
        $scope.todos = data;
      })
      .error(function(data, status, headers, config) {
        switch(status) {
          case 401: {
            $scope.message = "You must be authenticated!"
            break;
          }
          case 500: {
            $scope.message = "Something went wrong!";
            break;
          }
        }
        console.log(data, status);
      });*/
    $scope.parkCar = function(car) {
        parkingHttpFacade.saveCar(car)
            .then(function(response) {
                $scope.message = "Car Parked";
                retrieveCars()
            });
    }

    var retrieveCars = function () {
        parkingHttpFacade.getCars()
            .then(function(response) {
                $scope.cars = response.data;
            });


};
retrieveCars();

/*      $scope.parkCar = function (car) {
        $http.post("/api/cars", car)
            .success(function (data, status, headers, config) {
                retrieveCars();
                $scope.message = "The car was parked successfully!";
             })
            .error(function (data, status, header, config) {
                switch(status) {
                    case 401: {
                        $scope.message = "You must be autheticated!";
                        be;
                        }
                    case 500: {
                        $scope.message = "Something went wrong!";
                     }
                 }
                 console.log(data,status);
             });
      };*/
});