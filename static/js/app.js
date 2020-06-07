
function buildCharts(organization) {
  // @TODO: Use `d3.json` to Fetch the Sample Data for the Plots
  // d3.json(`/ranking/${organization}`).then((data) => {

    var orgurl = "/ranking/" + organization;
    d3.json(orgurl).then((data) => {
    //d3.json(`/ranking/<organization>`).then((data) => {
    // @TODO: Build a Bubble Chart Using the Sample Data
    // console.log(data.filter(function(item){
    //     return item.organization_type == organization;
    // }));
    var charity_id= data.charity_id;
    var charity_name = data.charity_name;
    var scores = data.scores;
    var total_contributions=data.total_contributions;
    var organization_type=data.organization_type;
    // @TODO: Build a bubble Chart
    var bubbleLayout = {
      margin: { t: 0 },
      hovermode: "closests",
      title:'<b> All Data for Category: ${organization} </b>',
      xaxis: { title: "Charity ID"},
      yaxis: { title: "overall score"}
    }
    var bubbleData = [
      {
        x: charity_id,
        y: scores,
        text: charity_name,
        mode: "markers",
        marker: {
          size: scores,
          color: charity_id,
          colorscale: "Earth"
        }
      }
    ]
    Plotly.plot("bubble", bubbleData, bubbleLayout);
      // var sampleData=data;
     // Prepare a list of objects for sorting
    var list = [];
    for (var i = 0; i < data.charity_id.length; i++) {
              // Push each object into the list
          list.push({'charity_id': data.charity_id[i],'charity_name': data.charity_name[i], 'overall_score': data.scores[i], 'total_contributions':data.total_contributions[i]});
    }
    // Sort function of objects by samples values in array
    console.log(list.sort((a, b) => parseInt(b.overall_score) - parseInt(a.overall_score)));
   // slice for top 15 of each
    var charity_id15= list.slice(0,15).map(record => "ID" + record.charity_id.toString());
    var values15 = list.slice(0,15).map(record => record.overall_score);
    var total_contributions15 = list.slice(0,15).map(record =>  record.total_contributions );
    var charity_name15= list.slice(0,15).map(record =>  record.charity_name );
    var trace1 = [{
        x: values15,
        y: charity_id15,
        hovertext:charity_name15,
        type: "bar",
        orientation: "h"
    }];
    var layout = {
        title:'<b> Top 15 Charities for Category: ${organization} </b>',
        yaxis:{autorange:'reversed'},
        height: 550,
        width: 700
    };
    Plotly.newPlot("chart", trace1, layout);
  })
}
function init() {
  // Grab a Reference to the Dropdown Select Element
  var selector = d3.select("#selDataset");
  // Use the List of Sample Names to Populate the Select Options
  d3.json('/names').then((orgNames) => {
    orgNames.forEach((organization) => {
      selector
        .append("option")
        .text(organization)
        .property("value", organization);
    });
    // Use the First Sample from the List to Build Initial Plots
    const firstOrg = orgNames[0];
    buildCharts(firstOrg);
  });
}
function optionChanged(newOrg) {
  // Fetch New Data Each Time a New Sample is Selected
  buildCharts(newOrg);
}
// Initialize the Dashboard
init();