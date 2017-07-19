from flask import Flask, render_template, request, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from scrapping.bet365 import bet365_scrapping
from scrapping.bet10 import bet10_scrapping
from scrapping.titanbet import titan_scrapping
from scrapping.betfred import betfred_scrapping
from scrapping.coral import coral_scrapping
from scrapping.eight88 import eight88_scrapping
from scrapping.ladbrokes import ladbrokes_scrapping
from scrapping.netbet import netbet_scrapping
from scrapping.paddy import paddy_scrapping
from scrapping.real import real_scrapping
from scrapping.stan import stan_scrapping

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/josh'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email


class Bet365(db.Model):
    __tablename__ = "bet365s"
    id = db.Column(db.Integer, primary_key=True)
    sports = db.Column(db.Float)
    casino = db.Column(db.Float)
    poker = db.Column(db.Float)
    games_bingo = db.Column(db.Float)
    total = db.Column(db.Float)
    withdrawal = db.Column(db.Float)
    balance = db.Column(db.Float)

    def __init__(self, sports, casino, poker, games_bingo, total, withdrawal, balance):
        self.sports = sports
        self.casino = casino
        self.poker = poker
        self.games_bingo = games_bingo
        self.total = total
        self.withdrawal = withdrawal
        self.balance = balance


class Eight88(db.Model):
    __tablename__ = "eight88s"
    id = db.Column(db.Integer, primary_key=True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    lead = db.Column(db.Integer)
    money_player = db.Column(db.Integer)
    balance = db.Column(db.Float)

    def __init__(self, impression, click, registration, lead, money_player, balance):
        self.impression = impression
        self.click = click
        self.registration = registration
        self.lead = lead
        self.money_player = money_player
        self.balance = balance


class Bet10(db.Model):
    __tablename__ = "bet10s"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.String(80))

    def __init__(self, merchant, impression, click, registration, new_deposit, commission):
        self.merchant = merchant
        self.impression = impression
        self.click = click
        self.registration = registration
        self.new_deposit = new_deposit
        self.commission = commission


class RealDeal(db.Model):
    __tablename__ = "realDeals"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.Float)

    def __init__(self, merchant, impression, click, registration, new_deposit, commission):
        self.merchant = merchant
        self.impression = impression
        self.click = click
        self.registration = registration
        self.new_deposit = new_deposit
        self.commission = commission



class LadBroke(db.Model):
    __tablename__ = "ladBrokes"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.String(30))

    def __init__(self, balance):
        self.balance = balance


class BetFred(db.Model):
    __tablename__ = "betFreds"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.String(20))

    def __init__(self, merchant, impression, click, registration, new_deposit, commission):
        self.merchant = merchant
        self.impression = impression
        self.click = click
        self.registration = registration
        self.new_deposit = new_deposit
        self.commission = commission


class Paddy(db.Model):
    __tablename__ = "paddyies"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.String(20))

    def __init__(self, balance):
        self.balance = balance


class NetBet(db.Model):
    __tablename__ = "netBets"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.String(20))

    def __init__(self, balance):
        self.balance = balance


class TitanBet(db.Model):
    __tablename__ = "titanBets"
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.String(20))

    def __init__(self, balance):
        self.balance = balance


class Stan(db.Model):
    __tablename__ = "stans"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.String(20))

    def __init__(self, merchant, impression, click, registration, new_deposit, commission):
        self.merchant = merchant
        self.impression = impression
        self.click = click
        self.registration = registration
        self.new_deposit = new_deposit
        self.commission = commission


class Coral(db.Model):
    __tablename__ = "corals"
    id = db.Column(db.Integer, primary_key=True)
    merchant = db.Column(db.String(80), unique = True)
    impression = db.Column(db.Integer)
    click = db.Column(db.Integer)
    registration = db.Column(db.Integer)
    new_deposit = db.Column(db.Integer)
    commission = db.Column(db.Float)

    def __init__(self, merchant, impression, click, registration, new_deposit, commission):
        self.merchant = merchant
        self.impression = impression
        self.click = click
        self.registration = registration
        self.new_deposit = new_deposit
        self.commission = commission



@app.route('/')
def dashboard():
	return render_template('home.html')


@app.route('/bet365/')
def bet365():
    data = db.session.query(Bet365).all()[0]
    return render_template('pages/bet365.html', data = data)


@app.route('/eight88/')
def eight88():
	data = db.session.query(Eight88).all()[0]
	return render_template('pages/eight88.html', data = data)


@app.route('/bet10/')
def bet10():
	data = db.session.query(Bet10).all()[0]
	return render_template('pages/bet10.html', data = data)


@app.route('/realDeal/')
def realDeal():
	data = db.session.query(RealDeal).all()[0]
	return render_template('pages/realDeal.html', data = data)


@app.route('/ladBroke/')
def ladBroke():
	data = db.session.query(LadBroke).all()[0]
	return render_template('pages/ladBroke.html', data = data)


@app.route('/betFred/')
def betFred():
	data = db.session.query(BetFred).all()[0]
	return render_template('pages/betFred.html', data = data)


@app.route('/paddy/')
def paddy():
	data = db.session.query(Paddy).all()[0]
	return render_template('pages/paddy.html', data = data)


@app.route('/netBet/')
def netBet():
	data = db.session.query(NetBet).all()[0]
	return render_template('pages/netBet.html', data = data)


@app.route('/titanBet/')
def titanBet():
	data = db.session.query(TitanBet).all()[0]
	return render_template('pages/titanBet.html', data = data)


@app.route('/stan/')
def stan():
	data = db.session.query(Stan).all()[0]
	return render_template('pages/stan.html', data = data)


@app.route('/coral/')
def coral():
	data = db.session.query(Coral).all()[0]
	return render_template('pages/coral.html', data = data)


@app.route('/skyBet')
def skyBet():
    data = "Woops, credential is not valid. Please tell me account info."
    return render_template('pages/error.html', data = data)


@app.route('/william')
def william():
    data = "Woops, credential is not valid. Please tell me account info."
    return render_template('pages/error.html', data = data)


@app.route('/victor')
def victor():
    data = "Woops, credential is not valid. Please tell me account info."
    return render_template('pages/error.html', data = data)


@app.route('/testing/')
def testing():
    # # NetBet insert data starting
    # data = netbet_scrapping()
    
    # balance = data
    # result = NetBet(balance)
    # db.session.add(result)
    # db.session.commit()

    #Bet365 insert data starting
    data = bet365_scrapping()
    
    sports = float(data[0])
    casino = float(data[1])
    poker = float(data[2])
    games_bingo = float(data[3])
    total = float(data[4])
    withdrawal = float(data[5])
    balance = float(data[6])
    result = Bet365(sports, casino, poker, games_bingo, total, withdrawal, balance)

    db.session.add(result)
    db.session.commit()

    # Eight88 insert data starting
    data = eight88_scrapping()
    
    impression = int(data[0])
    click = int(data[1])
    registration = int(data[2])
    lead = int(data[3])
    money_player = int(data[4])
    result = Eight88(impression, click, registration, lead, money_player, 999)

    db.session.add(result)
    db.session.commit()

    #Bet10 insert data starting
    data = bet10_scrapping()
    
    merchant = str(data[0])
    impression = int(data[1])
    click = int(data[2])
    registration = int(data[3])
    new_deposit = int(data[4])
    commission = float(data[5])
    result = Bet10(merchant, impression, click, registration, new_deposit, commission)

    db.session.add(result)
    db.session.commit()

    # RealBet insert data starting
    data = real_scrapping()
    
    merchant = str(data[0])
    impression = int(data[1])
    click = int(data[2])
    registration = int(data[3])
    new_deposit = int(data[4])
    commission = str(data[5])
    result = RealDeal(merchant, impression, click, registration, new_deposit, commission)

    db.session.add(result)
    db.session.commit()

    #Ladbrokes insert data starting
    data = ladbrokes_scrapping()
    
    balance = data
    result = LadBroke(balance)

    db.session.add(result)
    db.session.commit()

    #BetFred insert data starting
    data = betfred_scrapping()
    
    merchant = str(data[0])
    impression = int(data[1])
    click = int(data[2])
    registration = int(data[3])
    new_deposit = int(data[4])
    commission = str(data[5])
    result = BetFred(merchant, impression, click, registration, new_deposit, commission)

    db.session.add(result)
    db.session.commit()

    #Paddy insert data starting
    data  = paddy_scrapping()
    
    balance = data
    result = Paddy(balance)

    db.session.add(result)
    db.session.commit()

    #TitanBet insert data starting
    data = titan_scrapping()
    
    balance = data
    result = TitanBet(balance)

    db.session.add(result)
    db.session.commit()    

    #Stan insert data starting
    data = stan_scrapping()
    
    merchant = data[0]
    impression = int(data[1])
    click = int(data[2])
    registration = int(data[3])
    new_deposit = int(data[4])
    commission = data[5]
    result = Stan(merchant, impression, click, registration, new_deposit, commission)

    db.session.add(result)
    db.session.commit()

    #Coral insert data starting
    data = coral_scrapping()
    
    merchant = data[0]
    impression = int(data[1])
    click = int(data[2])
    registration = int(data[3])
    new_deposit = int(data[4])
    commission = float(data[5])
    result = Coral(merchant, impression, click, registration, new_deposit, commission)

    db.session.add(result)
    db.session.commit()
        
    return ('Thanks for your time')


if __name__ == '__main__':
	app.debug = True
	app.run()