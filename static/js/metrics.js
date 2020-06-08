// Project 2 - displaying key charity info based on organization type
// using 'type ahead' feature on the organization type and a drop down menu for
// charity name.
var tbody = d3.select("tbody");
var tableBody = document.querySelector("tbody");
var inputValue = "";
var button = d3.select("#clear-btn")

// Use D3 to read the json data from file or Flask (via SQLite)

// d3.json("./data/charity.json").then((InputData) => {
d3.json("/metrics").then((InputData) => {

    var charityData = InputData.map(data => data)
    var charityOrgType = InputData.map(data => data.organization_type);

    console.log("input data: ", charityData);

    //  call the typeahead javascript library 

    var charityOrgType = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: charityOrgType
      });
      
      $('#bloodhound .typeahead').typeahead({
        hint: true,
        highlight: true,
        minLength: 1
      },
      {
        name: 'charityOrgType',
        source: charityOrgType
      });

      $('.typeahead').bind('typeahead:select', function(ev, suggestion) {
        var newType = suggestion;
        console.log('newType is: ' + newType);

        // filter the charities based on the selected organization type
        var filteredData = [];
        filteredData = charityData.filter(obj => {return obj.organization_type === suggestion})

        // insert the charity names in the dropdown menu
        document.getElementById("selName").innerHTML = "";
        var charityNames = filteredData.map(data => data.charity_name);
        d3.select("#selName").selectAll("div")
            .data(charityNames)
           .enter()
           .append("option")
           .html(d => d);


        //call this functions to display the filtered charity data in the table

        buildTable(filteredData); 
        // buildTable(charityNames[[0]]); 
      });  
});

//  This function will load the table for display
function buildTable(charity) {

    console.log('Running buildTable Function');
    console.log("charity data: ", charity);
    // if (typeof(charity) === "string"){charity = JSON.parse(charity)};

    document.getElementById("table-body").innerHTML = "";
    var tbody = d3.select("tbody");

    charity.forEach((charity) => {
      var row = tbody.append("tr");

      adminExp = accounting.formatMoney(charity.administrative_expenses);
      leaderComp = accounting.formatMoney(charity.compensation_leader_compensation);
      totalContrib = accounting.formatMoney(charity.total_contributions);

      row.insert("td").text(charity.charity_name);
      row.insert("td").text(charity.city);
      row.insert("td").text(charity.state_abbr);
      row.insert("td").text(charity.organization_type);
      row.insert("td").text(charity.overall_score);
      row.insert("td").text(adminExp);
      row.insert("td").text(leaderComp);
      row.insert("td").text(totalContrib);
      
    });

};

// Function called by DOM change to get new charity data for table
function optionChanged(newCharity) {

    console.log('Running optionChanged Function')
    var dropdownMenu = d3.selectAll("#selName").node();
    var newCharity = dropdownMenu.value;
    console.log(`New Charity: ${newCharity}`)

    // d3.json("./data/charity.json").then((InputData) => {
    d3.json("/metrics").then((InputData) => {  
        var charityData = InputData.map(data => data)
        filteredData = charityData.filter(id => id.charity_name == newCharity);
        console.log("filtered data in option changed: ", filteredData)

        buildTable(filteredData)
    });
};

button.on("click", function() {
  console.log("button was clicked");
  document.getElementById("table-body").innerHTML = "";

});

