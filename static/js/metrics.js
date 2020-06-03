// Project 2 - creating Charity Metrics Graph using Plotly and D3
var tbody = d3.select("tbody");
var tableBody = document.querySelector("tbody");
var inputValue = "";

// Use D3 to read the csv file
d3.csv("./data/charity_all.csv").then((InputData) => {
    
    var charityData = InputData.map(data => data)
    var charityNames = InputData.map(data => data.charity_name);
    var charityCity = InputData.map(data => data.city);
    var charityState = InputData.map(data => data.state_abbr);
    var charityOrgType = InputData.map(data => data.organization_type);
    var charityScore = InputData.map(data => data.overall_score);

    console.log("input data: ", charityData);

    // insert the names in the dropdown menu
    d3.select("#selName").selectAll("div")
        .data(charityNames)
        .enter()
        .append("option")
        .html(d => d);

    // insert the city in the dropdown menu
    d3.select("#selCity").selectAll("div")
        .data(charityCity)
        .enter()
        .append("option")
        .html(d => d);
        
    // insert the state in the dropdown menu
    d3.select("#selState").selectAll("div")
        .data(charityState)
        .enter()
        .append("option")
        .html(d => d);

    // insert the org type in the dropdown menu
    d3.select("#selOrgType").selectAll("div")
        .data(charityOrgType)
        .enter()
        .append("option")
        .html(d => d);

    // insert the Overall Score in the dropdown menu
    d3.select("#selScore").selectAll("div")
        .data(charityScore)
        .enter()
        .append("option")
        .html(d => d);

    //call this functions to display the 1st entry's data in the table

    // buildTable(charityData); 
    buildTable(charityData[[0]]); 

});

//  This function will filter the desired charity data and display on webpage
function buildTable(charity) {

    console.log('Running buildTable Function');
    console.log("charity data: ", charity);

        var filteredData = [];

        //filteredData = charity.filter(id => id.charity_name == charity);
        // var tbody = d3.select("tbody");
        
        // // Clear prior data
        // webPage.html("");
        // var row = tbody.insert("tr");
        // Object.entries(filteredData[0]).forEach(([key, value]) => {
        //     row.insert("td").text(`${key}:  ${value}`);
        // });

        // var row = tbody.append("tr");
        // charity.forEach(function(data){
        //     row.insert("td").text(data.charity_name);
        //     row.insert("td").text(data.city);
        //     row.insert("td").text(data.state_abbr);
        //     row.append("td").text(data.organization_type);
        //     row.append("td").text(data.overall_score);
        //     row.append("td").text(data.administrative_expenses);
        //     row.append("td").text(data.compensation_leader_compensation);
        //     row.append("td").text(data.total_contributions);
        //     
        // });

            adminExp = accounting.formatMoney(charity.administrative_expenses)
            leaderComp = accounting.formatMoney(charity.compensation_leader_compensation)
            totalContrib = accounting.formatMoney(charity.total_contributions)

            var tbody = d3.select("tbody");
            var row = tbody.append("tr");
            console.log("new charity name: ", charity.charity_name)
            row.insert("td").text(charity.charity_name);
            row.insert("td").text(charity.city);
            row.insert("td").text(charity.state_abbr);
            row.append("td").text(charity.organization_type);
            row.append("td").text(charity.overall_score);
            row.append("td").text(adminExp);
            row.append("td").text(leaderComp);
            row.append("td").text(totalContrib);


};

// Function called by DOM change to get new charity data for table
function optionChanged(newCharity) {

    console.log('Running optionChanged Function')
    var dropdownMenu = d3.selectAll("#selName").node();
    var newCharity = dropdownMenu.value;
    console.log(`New Charity: ${newCharity}`)

    d3.csv("./data/charity_all.csv").then((InputData) => {
        var charityData = InputData.map(data => data)
        filteredData = charityData.filter(id => id.charity_name == newCharity);
        console.log("filtered data: ", filteredData)
        document.getElementById("table-body").innerHTML = "";
        buildTable(filteredData[0])
    });
};

// function optionChanged(newOrgType) {

// constructs the suggestion engine
var inputField = d3.select(".typeahead")

inputField.on("change", function(){
    var newOrgType = d3.event.target.value;
})

// constructs the suggestion engine
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
