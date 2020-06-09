// Create map object
var map = L.map("map", {
    center: [37.09, -95.71],
    zoom: 3,
    // layers: [lightmap, charityHqs]
    // , charityHqs
});

// Add tile layer to the map
// var lightmap = 
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openlightmap.org/\">Openlightmap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "light-v10",
        // id: "streets-v11"
        accessToken: API_KEY
}).addTo(map);

// Grab the data with d3
d3.json("/location", function(response) {

    // Create a new marker cluster group
    var markers = L.markerClusterGroup();

    // Loop through data
    for (var i = 0; i < response.length; i++) {

        // Set the data information to a variable
        var charityInfo = response[i];

        // Check for all necessary properties
        if (charityInfo.charity_name && charityInfo.city && charityInfo.lat && charityInfo.lng) {

            // Add a new marker to the cluster group and bind a pop-up
            markers.addLayer(L.marker([charityInfo.lat, charityInfo.lng])
                .bindPopup("Charity Name: " + charityInfo.charity_name + "<br></br>" + "City: " + charityInfo.city));
        }

    }

    map.addLayer(markers);

});
