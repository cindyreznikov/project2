
function buildCharts(organization, newPara) {
  // @TODO: Use `d3.json` to Fetch the Sample Data for the Plots
  // d3.json(`/ranking/${organization}`).then((data) => {
  d3.json("/ranking").then((data) => {
    // @TODO: Build a Bubble Chart Using the Data
    var filteredData = [];
    filteredData = data.filter(obj => {return obj.organization_type === organization})
    var dataOri = filteredData;
    // Sort filteredData
    console.log(filteredData.sort((a, b) => parseInt(b.overall_score) - parseInt(a.overall_score)));
     // slice for top 15 of each
    var charity_id15= filteredData.slice(0,15).map(record => "ID" + record.charity_id.toString());
    var scores15 = filteredData.slice(0,15).map(record => record.overall_score);
    var total_contributions15 = filteredData.slice(0,15).map(record =>  record.total_contributions );
    var charity_name15= filteredData.slice(0,15).map(record =>  record.charity_name );
    var admin_expenses15=filteredData.slice(0,15).map(record =>  record.administrative_expenses );
    var leader_compensation15=filteredData.slice(0,15).map(record =>  record.compensation_leader_compensation );
    var selectedPara;
    switch (newPara) {
      case 'leader_compensation':
      selectedPara = filteredData.slice(0,15).map(record =>  record.compensation_leader_compensation);
      break;
      case 'admin_expenses':
      selectedPara = filteredData.slice(0,15).map(record =>  record.administrative_expenses);
      break;
      case 'total_contributions':
      selectedPara = filteredData.slice(0,15).map(record =>  record.total_contributions);
      break;
      case 'program_expenses':
      selectedPara = filteredData.slice(0,15).map(record =>  record.program_expenses);
      break;
      case 'fundraising_expenses':
      selectedPara = filteredData.slice(0,15).map(record =>  record.fundraising_expenses);
      break;
    }
    var trace1 = [{
        y: charity_id15,
        x: selectedPara,
        hovertext:charity_name15,
        type: "bar",
        orientation: "h"
    }];
    var layout ={
        title:`<b> ${newPara} in ${organization} category </b>`,
        yaxis:{autorange:'reversed'},
        height: 550,
        width: 700
    };
    Plotly.newPlot("chart", trace1, layout);
    var charity_id= dataOri.map(record => "ID" + record.charity_id.toString());
    var charityN= dataOri.map(record => record.charity_id);
    var scores = dataOri.map(record => record.overall_score);
    var total_contributions = dataOri.map(record =>  record.total_contributions );
    var charity_name= dataOri.map(record =>  record.charity_name );
    var organization_type = data.map(record =>  record.organization_type );
    // @TODO: Build a Histogram Chart
    var organization_type = data.map(record =>  record.organization_type );
    var hisData = [
      {
        x: organization_type,
        type: "histogram",
        marker: {
          color:"rgba(100,200,102,0.7)",
        }
      }
    ]
    Plotly.newPlot("histo", hisData,);
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
  });
  var selector2 = d3.select("#selpara");
  d3.json('/paras').then((parNames) => {
    parNames.forEach((param) => {
      selector2
        .append("option")
        .text(param)
        .property("value", param);
    });
  });
  // Use the First Sample from the List to Build Initial Plots
  const firstOrg = "International";
  const firstPar = "total_contributions";
  buildCharts(firstOrg, firstPar);
}
function optionChanged(newOrg) {
  // Fetch New Data Each Time a New Sample is Selected
  console.log('Running optionChanged Function')
  var dropdownMenu = d3.selectAll("#selDataset").node();
  var newOrg = dropdownMenu.value;
  var dropdownMenu2 = d3.selectAll("#selpara").node();
  var newPar = dropdownMenu2.value;
  buildCharts(newOrg, newPar);
}
// Initialize the Dashboard
init();

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  