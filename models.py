from .app import db


class Charity(db.Model):
    __tablename__ = 'charities'

    charity_id = db.Column(db.Integer, primary_key=True)
    accountability_score = db.Column(db.Float)
    administrative_expenses = db.Column(db.Float)
    charity_name = db.Column(db.String(64))
    charity_url = db.Column(db.String(64))
    city = db.Column(db.String(64))
    cn_advisory = db.Column(db.String(64))
    compensation_leader_compensation = db.Column(db.Float)
    compensation_leader_expense_percent = db.Column(db.Float)
    compensation_leader_title = db.Column(db.String(64))
    excess_or_deficit_for_year = db.Column(db.Float)
    financial_score = db.Column(db.Float)
    fundraising_expenses = db.Column(db.Float)
    net_assets = db.Column(db.Float)
    organization_type = db.Column(db.String(64))
    other_revenue = db.Column(db.Float) 
    overall_score = db.Column(db.Float)
    payments_to_affiliates = db.Column(db.Float)
    program_expenses = db.Column(db.Float)
    state_abbr = db.Column(db.String(64))
    total_contributions = db.Column(db.Float)


    def __repr__(self):
        return '<Charity %r>' % (self.name)


class Charity(db.Model):
    __tablename__ = 'city_coord'

    charity_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64))
    state_abbr = db.Column(db.String(64))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __repr__(self):
        return '<Charity %r>' % (self.name)
