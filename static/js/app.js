
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var kmDriven = document.getElementById("uiKmDriven");
  var location = document.getElementById("uiLocation");
  var carName = document.getElementById("uiCarName");
  var regYear = document.getElementById("uiRegYear");
  var ownerType = getOwnerType();
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/api/predict-used-car-price";

  $.post(url, {
      km_driven: parseInt(kmDriven.value),
      variant_name: carName.value,
      location: location.value,
      reg_year: regYear.value,
      owner_type: ownerType

  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function getOwnerType() {
  var uiOwner = document.getElementsByName("uiOwner");
  for(var i in uiOwner) {
    if(uiOwner[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function loadCarNames(){
    var url = "http://127.0.0.1:5000/api/get-car-names";
       $.get(url,function(data, status) {
          console.log("got response for get_brand_names request");
          if(data) {
              var carNames = data.car_names;
              var uiCarName = document.getElementById("uiCarName");
              $('#uiCarName').empty();
              for(var i in carNames) {
                  var opt = new Option(carNames[i]);
                  $('#uiCarName').append(opt);
              }
          }
      });
}

function loadCities(){
    var url = "http://127.0.0.1:5000/api/get-cities";
       $.get(url,function(data, status) {
          console.log("got response for get_brand_names request");
          if(data) {
              var cities = data.cities;
              var uiLocation = document.getElementById("uiLocation");
              $('#uiLocation').empty();
              for(var i in cities) {
                  var opt = new Option(cities[i]);
                  $('#uiLocation').append(opt);
              }
          }
      });
}


function onPageLoad() {
  console.log( "document loaded" );
  loadCarNames();
  loadCities();
}

window.onload = onPageLoad;

