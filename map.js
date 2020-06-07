// README instructions: Create a function called `createMap` that will take in `bikestations` as an argument.
// function to create the initial map layer
function createMap(charityHqs) {

    // Create the tile layer that will be the background
    // called lightmap b/c of the id -- more info?
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        // still not sure what other types of maps are available - could look through past activities as well
        id: "light-v10",
        accessToken: API_KEY
    });
    
    // note: the objects we are creating are DICTIONARIES (correct?)
    // Create a baseMaps object to hold the lightmap layer
    var baseMaps = {
        "Light Map": lightmap
    };
    
    // Create an overlayMaps object to hold the bikeStations layer
    var overlayMaps = {
        "Bike Stations": bikeStations
    }
    
    // Create the map object with options
    // -- different from the tileLayer, this is the actual map object
    // notice the L.map(passes the html element)
    var map = L.map("map-id", {
        center: [40.73, -74.0059],
        zoom: 12,
        // holds an array of options
        layers: [lightmap, bikeStations]
    });
    
    // Create a "layer control", pass in baseMaps and overlayMaps & add this to the map object we just created above
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(map);
    
    // close out the createMap function
    }
    
    // have not called this function yet, so nothing would appear if we try to run this, nothing would display on the site yet
    
    
    // README: Create a second function `createMarkers` that will take `response` as an argument.
    // introduce the createMarkers function
    // uses a "response" parameter
    function createMarkers(response) {
        
        // Pull the "stations" property off of response.data
        var stations = response.features.stations;
    
        // Initialize an array to hold bike markers
        var bikeMarkers = [];
    
        // Loop through the stations array
        for (var i = 0; i < stations.length; i++) {
            var station = stations[i];
    
            // For each station, create a marker and bind a popup with the station's name
            // Using the response from a future d3 call loop through the stations and create a marker to represent each station.
            var bikeMarker = L.marker([station.lat, station.lon])
            // Give each marker a popup to display the name and capacity of its station.
                .bindPopup("<h3>" + station.name + "<h3><h3>Capacity: " + station.capacity + "</h3>")
    
            // Add the marker to the bikeMarkers array
            // bikeMarker.push(bikeMarkers) -- wrong order
            bikeMarkers.push(bikeMarker);
            // think of it as the object itself IS BEING PUSHED into/onto the list
    
        // exiting the for loop
        }
    // not closed out of the createMarkers func yet
    createMap(L.layerGroup(bikeMarkers));
    
    // now closing out of createMarkers function
    }
    
    // Perform a GET request using D3 to the [Citi Bike Station Information Endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json) that will call the `createMarkers` function.
    // Call on the createMarkers function and call on the API -- able to do them both within the d3.json execution
    d3.json("https://gbfs.citibikenyc.com/gbfs/en/station_information.json", createMarkers);
    