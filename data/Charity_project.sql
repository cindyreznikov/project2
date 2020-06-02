-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/Be1Fic


CREATE TABLE charity_coord (
    charity_id int   NOT NULL,
    city VARCHAR(20),
    state_abbr VARCHAR(4), 
    lat dec,
    lng dec   
);

CREATE TABLE charity_data (
    charity_id int   NOT NULL,
    accountability_score DEC, 
    administrative_expenses DEC,   
    charity_name VARCHAR(100),  
    charity_url VARCHAR(100),  
    city VARCHAR(20), 
    cn_advisory VARCHAR(10), 
    compensation_leader_compensation DEC, 
    compensation_leader_expense_percent DEC,   
    compensation_leader_title VARCHAR(30), 
    excess_or_deficit_for_year DEC, 
    financial_score DEC,   
    fundraising_expenses INT,
    net_assets DEC,
    organization_type VARCHAR(30), 
    other_revenue DEC,  
    overall_score DEC,  
    payments_to_affiliates DEC, 
    program_expenses DEC, 
    state_abbr VARCHAR(4),  
    total_contributions DEC   
    CONSTRAINT pk_charity_data PRIMARY KEY (
        charity_id
     )
);

ALTER TABLE charity_coord ADD CONSTRAINT fk_charity_coord_charity_id FOREIGN KEY(charity_id)
REFERENCES charity_data (charity_id);

create table charity_all as
select charity_data.*,charity_coord.lat, charity_coord.lng
from charity_data left join charity_coord
on charity_data.charity_id=charity_coord.charity_id;