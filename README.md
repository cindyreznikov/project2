Group: Ronaldo, Cindy, Andrew, Jade, & Jodi

Project Plan:
1.	 Charity Navigator metrics, via Kaggle
a.	Clean data and make initial observations via Python & Jupyter notebook (Ronaldo & Jade) // by EOD 05/30 -- further notes on the data transformation below with “Plans for data tables” -- DONE
b.	Design, create and load data into database (via SQLite) (Ronaldo & Jade) // by 05/31 or early 06/02 -- on track
c.	Simultaneously:
i.	initialize Python Flask App (Andrew & Ronaldo) and pulling data from the database // by EOD 06/02 - start by 06/02
ii.	create HTML/CSS/Bootstrap document + default dashboard page that includes a description of the site/project (Cindy & Jodi) // by EOD 05/31 -- (mostly) DONE
d.	Data vizzes: create 3 interactive visualizations, each on their own page and with some user-interface directions (All) // all visualizations by EOD 06/04 -- start by 06/02
i.	Map with charity headquarter markers, by charity type, via Mapbox & Leaflet (Jodi)
ii.	Detailed metrics on a charity -- CEO compensation, accountability score, financial score, total contributions (Cindy & Andrew)
1.	Incorporate a JS library (typeahead.js, autoComplete.js) that can help autocomplete a search bar for the user’s input when searching for a charity 
iii.	Charity rankings -- top 10 & bottom 10 based on filtered metrics + potential scatter plot to test correlation of accountability score & other metrics via d3 & Plotly (Ronaldo & Jade)

Chosen Topic: Charities in the United States - Founded in 2001, Charity Navigator has become the nation's largest and most-utilized evaluator of charities. 
Their professional analysts have examined tens of thousands of non-profit financial documents. 
They’ve used this knowledge to develop an unbiased, objective, numbers-based rating system to assess over 9,000 of America's best-known and some lesser known, 
but worthy, charities.
Data is sourced from: https://www.kaggle.com/cyaris/charities-in-the-united-states
Further details on the Charity Navigator metrics can be found here: Metadata for Charity Navigator

Questions we want to answer…and how this impacts user inputs/interface
The overall goal of our project is to help a potential user decide where to give their charitable donations, especially if they consider some of the following questions and charity criteria:
1.	Where charities are headquartered? 
a.	This could help someone looking for a “local” charity to find one by a particular location in the U.S., whether their current or past “home”.
b.	User could pick a state from their dropdown menu and then it will populate the charities listed there, their overall score, and other select information.
2.	How much are charity CEOs compensated and how does this compare to other metrics within the organization?
a.	If a user is curious about a particular charity, this could provide an overall picture of key metrics, including their financial & accountability scores, the total contributions that charity receives per year, etc.
3.	Which charities rank the highest, according to the Charity Navigator score? The lowest?
a.	Have a default interface that shows the US overall
b.	Incorporate a scatterplot that plots the accountability score against the overall score or the financial score to see if there is some correlation - would show the user how these scores work together

Plans for data tables:
SQLite Database with 2 tables 
Charity table - charity_id, name, url, city, state, org_type, overall_score
Finances table - charity_id, admin_expenses, leader_compensation, yearly_excess_deficit, financial_score, fund_raising_expenses, net_assets, other_rev, payment_to_affiliates, pgm_expenses, total_contributions 

