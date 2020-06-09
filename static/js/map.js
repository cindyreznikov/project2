// Create a function called `createMap` that will take in `bikestations` as an argument.
// function to create the initial map layer
function createMap(charityHqs) {
    // charityHqs

    // Create the tile layer that will be the background
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openlightmap.org/\">Openlightmap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "light-v10",
        // id: "streets-v11"
        accessToken: API_KEY
    });

    // Create a baseMaps object to hold the lightmap layer
    var baseMaps = {
        "US Map": lightmap
    };

    // Create an overlayMaps object to hold the charity headquarters layer
    var overlayMaps = {
        "Charity Headquarters": charityHqs
    }

    // Create the map object with options
    var map = L.map("map", {
        center: [37.09, -95.71],
        zoom: 3,
        layers: [lightmap, charityHqs]
        // , charityHqs
    });

    // Create a "layer control", pass in baseMaps and overlayMaps & add this to the map object we just created above
    // , overlayMaps
    L.control.layers(baseMaps, overlayMaps).addTo(map);
    // collapsed: false}


    // return map;

}

// createMap();

// Create a new marker cluster group
var markers = L.markerClusterGroup();

function createMarkers(response) {
    // print "hello" to ensure this function is running
    console.log("hello jodi");
    console.log(response);


    // Initialize an array to hold bike markers
    var charitiesArray = [];

    // Loop through the charities array
    // if (charityInfo.charity_name && charityInfo.city && charityInfo.lat && charityInfo.lng)
    for (var i = 0; i < response.length; i++) {
        var charityInfo = response[i];

        if (charityInfo.charity_name && charityInfo.city && charityInfo.lat && charityInfo.lng) {

            var charityMarker = L.marker([charityInfo.lat, charityInfo.lng])
                // Give each marker a popup to display the name and capacity of its charityInfo.
                .bindPopup("Charity Name: " + charityInfo.charity_name + "<br></br>" + "City: " + charityInfo.city);

            // Add the marker to the charitiesArray array
            charitiesArray.push(charityMarker);

            var descriptor = "abc"

            // Add a new marker to the cluster group and bind a pop-up
            markers.addLayer(charityMarker);
            // .bindPopup(descriptor);
            // .marker([location.coordinates[1], location.coordinates[0]]).bindPopup(response[i].descriptor));

        }
        // console.log(charityInfo.lat)
    }

    // map.addLayer(markers)
    createMap(L.layerGroup(markers));

}

// // Perform a GET request using D3 to the [Citi Bike Station Information Endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json) that will call the `createMarkers` function.
// Call on the createMarkers function and call on the API -- able to do them both within the d3.json execution
d3.json("/location", createMarkers);
