import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
import pickle
from flask import Flask, render_template, request
import pandas as pd

 

app = Flask(__name__) #Initialize the flask App

gradient_boost = pickle.load(open('gradient_boost.pkl','rb'))
RandomForest = pickle.load(open('RandomForest.pkl','rb'))

job_random = pickle.load(open('job_random.pkl','rb'))

bagging = pickle.load(open('job_bagging.pkl','rb'))

@app.route('/')

@app.route('/first')
def first():
	return render_template('first.html')

 

#@app.route('/future')
#def future():
#	return render_template('future.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)	

@app.route('/logins')
def logins():
	return render_template('logins.html')
@app.route('/uploads')
def uploads():
    return render_template('uploads.html')  
@app.route('/previews',methods=["POST"])
def previews():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("previews.html",df_view = df)	
 

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')
    
 

# Load the model (ensure this path is correct)
 

@app.route('/predict', methods=['POST'])
def predict():
    resul = {}  # Default empty dictionary
    result = ''  # Default empty string

    if request.method == 'POST': 
            resul = request.form.to_dict()
            print(resul)
       
            
            Company = request.form['company']
    
            if Company == '0':
                choices = 'Replit'
            elif Company == '1':
                choices = 'Gopuff'
            elif Company == '2':
                choices = 'Atmosphere'
            elif Company == '3':
                choices = 'Singularity 6'
            elif Company == '4':
                choices = 'Mainvest'
            elif Company == '5':
                choices = 'Indeed'
            elif Company == '6':
                choices = 'Motional'
            elif Company == '7':
                choices = 'Rivian'
            elif Company == '8':
                choices = 'Google'
            elif Company == '9':
                choices = 'Vacasa'
            elif Company == '10':
                choices = 'PrepLadder'
            elif Company == '11':
                choices = 'Simpl'
            elif Company == '12':
                choices = 'Arkane Studios'
            elif Company == '13':
                choices = 'Brilliant'
            elif Company == '14':
                choices = 'Hopin'
            elif Company == '15':
                choices = 'Enovix'
            elif Company == '16':
                choices = 'Cue Health'
            elif Company == '17':
                choices = 'Luminar'
            elif Company == '18':
                choices = 'Sprinklr'
            elif Company == '19':
                choices = 'Bakkt'
            elif Company == '20':
                choices = 'Peloton'
            elif Company == '21':
                choices = 'Cabify'
            elif Company == '22':
                choices = 'Assurance'
            elif Company == '23':
                choices = 'Sproutt'
            elif Company == '24':
                choices = 'Tesla'
            elif Company == '25':
                choices = 'Akili Interactive'
            elif Company == '26':
                choices = 'Getir'
            elif Company == '27':
                choices = 'Ola'
            elif Company == '28':
                choices = 'ComplYant'
            elif Company == '29':
                choices = 'Fisker'
            elif Company == '30':
                choices = 'HealthifyMe'
            elif Company == '31':
                choices = 'True Anomaly'
            elif Company == '32':
                choices = 'Grin'
            elif Company == '33':
                choices = 'Expedia'
            elif Company == '34':
                choices = 'Freenome'
            elif Company == '35':
                choices = 'Heureka Group'
            elif Company == '36':
                choices = '98point6'
            elif Company == '37':
                choices = 'OutSystems'
            elif Company == '38':
                choices = 'Homie'
            elif Company == '39':
                choices = 'The Good Glamm Group'
            elif Company == '40':
                choices = 'Showpad'
            elif Company == '41':
                choices = 'Stability AI'
            elif Company == '42':
                choices = 'Pax8'
            elif Company == '43':
                choices = 'ConnectWise'
            elif Company == '44':
                choices = 'Take-Two'
            elif Company == '45':
                choices = 'Tome'
            elif Company == '46':
                choices = 'Criteo'
            elif Company == '47':
                choices = 'Glovo'
            elif Company == '48':
                choices = 'TikTok'
            elif Company == '49':
                choices = 'Fabric'
            elif Company == '50':
                choices = 'Hinge Health'
            elif Company == '51':
                choices = 'Zoe'
            elif Company == '52':
                choices = 'Cornershop'
            elif Company == '53':
                choices = 'Scaler'
            elif Company == '54':
                choices = 'Checkr'
            elif Company == '55':
                choices = 'Intel'
            elif Company == '56':
                choices = 'Trendsales'
            elif Company == '57':
                choices = 'Fission'
            elif Company == '58':
                choices = 'Bolt.Earth'
            elif Company == '59':
                choices = 'Apple'
            elif Company == '60':
                choices = 'Agility Robotics'
            elif Company == '61':
                choices = 'Lightspeed Commerce'
            elif Company == '62':
                choices = 'Ghost Autonomy'
            elif Company == '63':
                choices = 'Vivian Health'
            elif Company == '64':
                choices = 'Amazon'
            elif Company == '65':
                choices = 'CoRover'
            elif Company == '66':
                choices = 'Kaseya'
            elif Company == '67':
                choices = 'New Relic'
            elif Company == '68':
                choices = 'Yummly'
            elif Company == '69':
                choices = "Byju's"
            elif Company == '70':
                choices = 'Lentra'
            elif Company == '71':
                choices = 'Thepeer'
            elif Company == '72':
                choices = 'Osso VR'
            elif Company == '73':
                choices = 'Identiq'
            elif Company == '74':
                choices = 'Ranger Insurance'
            elif Company == '75':
                choices = 'Rezi'
            elif Company == '76':
                choices = 'ChowNow'
            elif Company == '77':
                choices = 'Synctera'
            elif Company == '78':
                choices = 'GoPro'
            elif Company == '79':
                choices = 'Dell'
            elif Company == '80':
                choices = 'Verily'
            elif Company == '81':
                choices = 'Cybereason'
            elif Company == '82':
                choices = 'ShopBack'
            elif Company == '83':
                choices = 'Orbotech'
            elif Company == '84':
                choices = 'Airmeet'
            elif Company == '85':
                choices = 'Singular Genomics'
            elif Company == '86':
                choices = 'Longi'
            elif Company == '87':
                choices = 'Flock Freight'
            elif Company == '88':
                choices = 'Chipper Cash'
            elif Company == '89':
                choices = 'Blueboard'
            elif Company == '90':
                choices = 'Ancestry'
            elif Company == '91':
                choices = 'Textio'
            elif Company == '92':
                choices = 'Stash'
            elif Company == '93':
                choices = 'Phantom Auto'
            elif Company == '94':
                choices = 'IBM'
            elif Company == '95':
                choices = 'Deadspin'
            elif Company == '96':
                choices = 'Niche'
            elif Company == '97':
                choices = 'Inscribe'
            elif Company == '98':
                choices = 'Turnitin'
            elif Company == '99':
                choices = 'Totango'
            elif Company == '100':
                choices = 'Sorare'
            elif Company == '101':
                choices = 'Meta'
            elif Company == '102':
                choices = 'PlanetScale'
            elif Company == '103':
                choices = 'MessageBird'
            elif Company == '104':
                choices = 'Form Energy'
            elif Company == '105':
                choices = 'Verbit'
            elif Company == '106':
                choices = 'Edgio'
            elif Company == '107':
                choices = 'Melio'
            elif Company == '108':
                choices = 'Our Next Energy'
            elif Company == '109':
                choices = 'Project Ronin'
            elif Company == '110':
                choices = 'Pristyn Care'
            elif Company == '111':
                choices = 'Gro Intelligence'
            elif Company == '112':
                choices = 'Tonik'
            elif Company == '113':
                choices = 'Kevin'
            elif Company == '114':
                choices = 'Electronic Arts'
            elif Company == '115':
                choices = 'Treasury Prime'
            elif Company == '116':
                choices = 'Sony Interactive'
            elif Company == '117':
                choices = 'Bumble'
            elif Company == '118':
                choices = 'PropertyGuru'
            elif Company == '119':
                choices = 'WayCool'
            elif Company == '120':
                choices = 'Daraz'
            elif Company == '121':
                choices = 'Redesign Health'
            elif Company == '122':
                choices = 'Carbon Health'
            elif Company == '123':
                choices = 'Vice Media'
            elif Company == '124':
                choices = 'Affirm'
            elif Company == '125':
                choices = 'Finder'
            elif Company == '126':
                choices = 'BuzzFeed'
            elif Company == '127':
                choices = 'Aptiv'
            elif Company == '128':
                choices = 'Tails.com'
            elif Company == '129':
                choices = 'Auctane'
            elif Company == '130':
                choices = 'KnownOrigin'
            elif Company == '131':
                choices = 'Meati'
            elif Company == '132':
                choices = 'Farfetch'
            elif Company == '133':
                choices = 'Voi'
            elif Company == '134':
                choices = 'Toast'
            elif Company == '135':
                choices = 'Sonder'
            elif Company == '136':
                choices = 'Storytel'
            elif Company == '137':
                choices = 'CodeSee'
            elif Company == '138':
                choices = 'May Mobility'
            elif Company == '139':
                choices = 'Cisco'
            elif Company == '140':
                choices = 'Wint Wealth'
            elif Company == '141':
                choices = 'Away'
            elif Company == '142':
                choices = 'Instacart'
            elif Company == '143':
                choices = 'Mozilla'
            elif Company == '144':
                choices = 'Impinj'
            elif Company == '145':
                choices = 'Riskified'
            elif Company == '146':
                choices = 'Everybuddy'
            elif Company == '147':
                choices = 'Popcore'
            elif Company == '148':
                choices = 'Wisense'
            elif Company == '149':
                choices = 'SiriusXM'
            elif Company == '150':
                choices = 'Licious'
            elif Company == '151':
                choices = 'BlissClub'
            elif Company == '152':
                choices = 'Kandji'
            elif Company == '153':
                choices = 'Pure Storage'
            elif Company == '154':
                choices = 'Otovo'
            elif Company == '155':
                choices = 'Getaround'
            elif Company == '156':
                choices = 'Journera'
            elif Company == '157':
                choices = 'Grammarly'
            elif Company == '158':
                choices = 'Fireblocks'
            elif Company == '159':
                choices = 'Tenable'
            elif Company == '160':
                choices = 'Workfellow'
            elif Company == '161':
                choices = 'DocuSign'
            elif Company == '162':
                choices = 'Glowforge'
            elif Company == '163':
                choices = 'Snap'
            elif Company == '164':
                choices = 'Drizly'
            elif Company == '165':
                choices = 'BillGO'
            elif Company == '166':
                choices = 'Impact.com'
            elif Company == '167':
                choices = 'Astrate Medical'
            elif Company == '168':
                choices = 'Meetup'
            elif Company == '169':
                choices = 'Muvin'
            elif Company == '170':
                choices = 'Nomad Health'
            elif Company == '171':
                choices = 'Zwift'
            elif Company == '172':
                choices = 'Top Hat'
            elif Company == '173':
                choices = 'Cake Bikes'
            elif Company == '174':
                choices = 'Small Robot Company'
            elif Company == '175':
                choices = 'Twig'
            elif Company == '176':
                choices = 'Okta'
            elif Company == '177':
                choices = 'Zoom'
            elif Company == '178':
                choices = 'Illumina'
            elif Company == '179':
                choices = 'Polygon'
            elif Company == '180':
                choices = 'Indigo'
            elif Company == '181':
                choices = 'Proofpoint'
            elif Company == '182':
                choices = 'Trove Recommerce'
            elif Company == '183':
                choices = 'CircleCI'
            elif Company == '184':
                choices = 'Thinx'
            elif Company == '185':
                choices = 'Innoviz'
            elif Company == '186':
                choices = 'The Messenger'
            elif Company == '187':
                choices = 'Zuora'
            elif Company == '188':
                choices = 'PayPal'
            elif Company == '189':
                choices = 'Block'
            elif Company == '190':
                choices = 'Kiwi.com'
            elif Company == '191':
                choices = 'Aurora Solar'
            elif Company == '192':
                choices = 'Wattpad'
            elif Company == '193':
                choices = 'TechCrunch'
            elif Company == '194':
                choices = 'Noom'
            elif Company == '195':
                choices = 'Procore'
            elif Company == '196':
                choices = 'Vipps'
            elif Company == '197':
                choices = 'iRobot'
            elif Company == '198':
                choices = 'DispatchHealth'
            elif Company == '199':
                choices = 'Loopio'
            elif Company == '200':
                choices = 'Salesforce'
            elif Company == '201':
                choices = 'Flexport'
            elif Company == '202':
                choices = 'Productboard'
            elif Company == '203':
                choices = 'Microsoft'
            elif Company == '204':
                choices = 'Swiggy'
            elif Company == '205':
                choices = 'Veho'
            elif Company == '206':
                choices = 'Amperity'
            elif Company == '207':
                choices = 'MVPindex'
            elif Company == '208':
                choices = 'Business Insider'
            elif Company == '209':
                choices = 'Cova'
            elif Company == '210':
                choices = 'Jamf'
            elif Company == '211':
                choices = 'Cult.fit'
            elif Company == '212':
                choices = 'Personio'
            elif Company == '213':
                choices = 'Aurora'
            elif Company == '214':
                choices = 'Desktop Metal'
            elif Company == '215':
                choices = 'HubSpot'
            elif Company == '216':
                choices = 'SAP'
            elif Company == '217':
                choices = 'eBay'
            elif Company == '218':
                choices = 'Vroom'
            elif Company == '219':
                choices = 'Brex'
            elif Company == '220':
                choices = 'Cure.fit'
            elif Company == '221':
                choices = 'GoStudent'
            elif Company == '222':
                choices = 'GoTo'
            elif Company == '223':
                choices = 'Seedr'
            elif Company == '224':
                choices = 'Riot Games'
            elif Company == '225':
                choices = 'Xendit'
            elif Company == '226':
                choices = '2U'
            elif Company == '227':
                choices = 'SolarEdge'
            elif Company == '228':
                choices = 'Wayfair'
            elif Company == '229':
                choices = 'Fashinza'
            elif Company == '230':
                choices = 'Stitch Fix'
            elif Company == '231':
                choices = 'YouTube'
            elif Company == '232':
                choices = 'Sirplus'
            elif Company == '233':
                choices = 'SonderMind'
            elif Company == '234':
                choices = 'First Mode'
            elif Company == '235':
                choices = 'ALI Technologies'
            elif Company == '236':
                choices = 'Thursday'
            elif Company == '237':
                choices = 'Veeam'
            elif Company == '238':
                choices = 'GrabCAD'
            elif Company == '239':
                choices = 'Artifact'
            elif Company == '240':
                choices = 'Dastgyr'
            elif Company == '241':
                choices = 'Hologram'
            elif Company == '242':
                choices = 'Vendr'
            elif Company == '243':
                choices = 'New Work SE'
            elif Company == '244':
                choices = 'Playtika'
            elif Company == '245':
                choices = 'Discord'
            elif Company == '246':
                choices = 'Inmobi'
            elif Company == '247':
                choices = 'Audible'
            elif Company == '248':
                choices = '7Shifts'
            elif Company == '249':
                choices = 'Sisense'
            elif Company == '250':
                choices = 'Cloudflare'
            elif Company == '251':
                choices = '888'
            elif Company == '252':
                choices = 'Certinia'
            elif Company == '253':
                choices = 'Chief'
            elif Company == '254':
                choices = 'Dextrous Robotics'
            elif Company == '255':
                choices = 'Citrix'
            elif Company == '256':
                choices = 'IAC'
            elif Company == '257':
                choices = 'FreshDirect'
            elif Company == '258':
                choices = 'Beam Benefits'
            elif Company == '259':
                choices = 'Instagram'
            elif Company == '260':
                choices = 'ChargePoint'
            elif Company == '261':
                choices = 'SoFi'
            elif Company == '262':
                choices = 'Twitch'
            elif Company == '263':
                choices = 'Branch'
            elif Company == '264':
                choices = 'Nevro'
            elif Company == '265':
                choices = 'FullStory'
            elif Company == '266':
                choices = 'Uber Freight'
            elif Company == '267':
                choices = 'Rent the Runway'
            elif Company == '268':
                choices = 'Treasure Financial'
            elif Company == '269':
                choices = 'Humane'
            elif Company == '270':
                choices = 'EVBox'
            elif Company == '271':
                choices = 'Morning Consult'
            elif Company == '272':
                choices = 'Trend Micro'
            elif Company == '273':
                choices = 'Unity'
            elif Company == '274':
                choices = 'Flipkart'
            elif Company == '275':
                choices = 'NuScale Power'
            elif Company == '276':
                choices = 'Flexe'
            elif Company == '277':
                choices = 'Pitch'
            elif Company == '278':
                choices = 'BenchSci'
            elif Company == '279':
                choices = 'Here'
            elif Company == '280':
                choices = 'Ledger Investing'
            elif Company == '281':
                choices = 'Lendio'
            elif Company == '282':
                choices = 'MeridianLink'
            elif Company == '283':
                choices = 'LiveVox'
            elif Company == '284':
                choices = 'NanoString Technologies'
            elif Company == '285':
                choices = 'Lever'
            elif Company == '286':
                choices = 'Trigo'
            elif Company == '287':
                choices = 'InVision'
            elif Company == '288':
                choices = 'VideoAmp'
            elif Company == '289':
                choices = 'Xerox'
            elif Company == '290':
                choices = 'Lazada Group '
            elif Company == '291':
                choices = 'Orca Security'
            elif Company == '292':
                choices = 'Frontdesk'
            elif Company == '293':
                choices = 'Strake'
            elif Company == '294':
                choices = 'Paytm'
            elif Company == '295':
                choices = 'Hyperloop One'
            elif Company == '296':
                choices = 'Palmetto Clean Technology'
            elif Company == '297':
                choices = 'ShareChat'
            elif Company == '298':
                choices = 'InSightec'
            elif Company == '299':
                choices = 'Kaspien'
            elif Company == '300':
                choices = 'Enphase Energy'
            elif Company == '301':
                choices = 'Udaan'
            elif Company == '302':
                choices = 'Checkout.com'
            elif Company == '303':
                choices = 'Arm Holdings'
            elif Company == '304':
                choices = 'Delivery Hero'
            elif Company == '305':
                choices = 'Jellysmack'
            elif Company == '306':
                choices = 'Superpedestrian'
            elif Company == '307':
                choices = 'Cruise'
            elif Company == '308':
                choices = 'Solarisbank'
            elif Company == '309':
                choices = 'Bolt'
            elif Company == '310':
                choices = 'Curalie'
            elif Company == '311':
                choices = 'Curbio'
            elif Company == '312':
                choices = 'Flyhomes'
            elif Company == '313':
                choices = 'Stellar Pizza'
            elif Company == '314':
                choices = 'Invitae'
            elif Company == '315':
                choices = 'Etsy'
            elif Company == '316':
                choices = 'Analog Devices'
            elif Company == '317':
                choices = 'ForgeRock'
            elif Company == '318':
                choices = 'Flex'
            elif Company == '319':
                choices = 'FourKites'
            elif Company == '320':
                choices = 'Sojern'
            elif Company == '321':
                choices = 'TomTom'
            elif Company == '322':
                choices = 'Jungle Scout'
            elif Company == '323':
                choices = 'SmileDirectClub'
            elif Company == '324':
                choices = 'Sunfolding'
            elif Company == '325':
                choices = 'Zulily'
            elif Company == '326':
                choices = 'D2iQ'
            elif Company == '327':
                choices = 'Simplilearn'
            elif Company == '328':
                choices = 'Navan'
            elif Company == '329':
                choices = 'Tidal'
            elif Company == '330':
                choices = 'ZestMoney'
            elif Company == '331':
                choices = 'Incredibuild'
            elif Company == '332':
                choices = 'Bill.com'
            elif Company == '333':
                choices = 'Contentful'
            elif Company == '334':
                choices = 'Course Hero'
            elif Company == '335':
                choices = 'Pivo'
            elif Company == '336':
                choices = 'Yahoo'
            elif Company == '337':
                choices = 'Spotify'
            elif Company == '338':
                choices = 'TuSimple'
            elif Company == '339':
                choices = 'Meow Wolf'
            elif Company == '340':
                choices = 'DwellWell'
            elif Company == '341':
                choices = 'Twilio'
            elif Company == '342':
                choices = 'Filmic'
            elif Company == '343':
                choices = 'Loco'
            elif Company == '344':
                choices = 'Zepz'
            elif Company == '345':
                choices = 'Domo'
            elif Company == '346':
                choices = 'Mojo'
            elif Company == '347':
                choices = 'Pipedrive'
            elif Company == '348':
                choices = 'Vox Media'
            elif Company == '349':
                choices = 'Dataminr'
            elif Company == '350':
                choices = 'Multiverse'
            elif Company == '351':
                choices = 'Tier Mobility'
            elif Company == '352':
                choices = 'VMware'
            elif Company == '353':
                choices = 'Bytedance'
            elif Company == '354':
                choices = 'Veev'
            elif Company == '355':
                choices = 'Anar'
            elif Company == '356':
                choices = 'Alerzo'
            elif Company == '357':
                choices = 'McMakler'
            elif Company == '358':
                choices = 'Tulip Retail'
            elif Company == '359':
                choices = 'Jodo'
            elif Company == '360':
                choices = 'C3.ai'
            elif Company == '361':
                choices = 'Presto'
            elif Company == '362':
                choices = 'Physics Wallah'
            elif Company == '363':
                choices = 'NextGen Healthcare'
            elif Company == '364':
                choices = 'Buildertrend'
            elif Company == '365':
                choices = 'Jane'
            elif Company == '366':
                choices = 'Zazuu'
            elif Company == '367':
                choices = 'Sierra Space'
            elif Company == '368':
                choices = 'Paystack'
            elif Company == '369':
                choices = 'Beamery'
            elif Company == '370':
                choices = 'Sonos'
            elif Company == '371':
                choices = 'FintechOS'
            elif Company == '372':
                choices = 'FreshBooks'
            elif Company == '373':
                choices = 'Landing'
            elif Company == '374':
                choices = 'Uleet'
            elif Company == '375':
                choices = 'Chewy'
            elif Company == '376':
                choices = 'Sarcos'
            elif Company == '377':
                choices = 'Cake Group'
            elif Company == '378':
                choices = 'Halodoc'
            elif Company == '379':
                choices = 'Markforged'
            elif Company == '380':
                choices = 'Ping Identity'
            elif Company == '381':
                choices = 'TripAdvisor'
            elif Company == '382':
                choices = 'Bowery Farming'
            elif Company == '383':
                choices = 'Carta'
            elif Company == '384':
                choices = 'Commure'
            elif Company == '385':
                choices = 'OSlash'
            elif Company == '386':
                choices = 'BigCommerce'
            elif Company == '387':
                choices = 'CloudKitchens'
            elif Company == '388':
                choices = 'Oportun'
            elif Company == '389':
                choices = 'Zillow'
            elif Company == '390':
                choices = 'Nextdoor'
            elif Company == '391':
                choices = 'Zeus Living'
            elif Company == '392':
                choices = 'Ava Labs'
            elif Company == '393':
                choices = 'Moore Threads'
            elif Company == '394':
                choices = 'Pico Interactive'
            elif Company == '395':
                choices = 'F5'
            elif Company == '396':
                choices = 'NIO'
            elif Company == '397':
                choices = 'OpenSea'
            elif Company == '398':
                choices = 'Viasat'
            elif Company == '399':
                choices = 'Beyond Meat'
            elif Company == '400':
                choices = 'OpenSpace'
            elif Company == '401':
                choices = 'Orchard'
            elif Company == '402':
                choices = 'Sportradar'
            elif Company == '403':
                choices = 'Informatica'
            elif Company == '404':
                choices = 'Splunk'
            elif Company == '405':
                choices = 'Faire'
            elif Company == '406':
                choices = 'Sana Benefits'
            elif Company == '407':
                choices = 'Olive'
            elif Company == '408':
                choices = 'StepStone'
            elif Company == '409':
                choices = 'Hubilo'
            elif Company == '410':
                choices = 'Karat Financial'
            elif Company == '411':
                choices = 'Hippo Insurance'
            elif Company == '412':
                choices = 'Graphy'
            elif Company == '413':
                choices = 'Salsify'
            elif Company == '414':
                choices = ' F-Secure '
            elif Company == '415':
                choices = 'Virgio'
            elif Company == '416':
                choices = 'Exabeam'
            elif Company == '417':
                choices = 'Slync'
            elif Company == '418':
                choices = 'SiFive'
            elif Company == '419':
                choices = 'Pebble'
            elif Company == '420':
                choices = 'Shipt'
            elif Company == '421':
                choices = 'Parity Technologies'
            elif Company == '422':
                choices = 'Roblox China'
            elif Company == '423':
                choices = 'Tropic'
            elif Company == '424':
                choices = 'Convoy'
            elif Company == '425':
                choices = 'Bullhorn'
            elif Company == '426':
                choices = 'LegalZoom'
            elif Company == '427':
                choices = 'StellarAlgo'
            elif Company == '428':
                choices = 'ManoMano'
            elif Company == '429':
                choices = 'WeTransfer'
            elif Company == '430':
                choices = 'Plume'
            elif Company == '431':
                choices = 'Belora Paris'
            elif Company == '432':
                choices = 'Made Renovation'
            elif Company == '433':
                choices = 'Volta Trucks'
            elif Company == '434':
                choices = 'Waymo'
            elif Company == '435':
                choices = 'LinkedIn'
            elif Company == '436':
                choices = 'CityMall'
            elif Company == '437':
                choices = 'C2FO'
            elif Company == '438':
                choices = 'Kayak / OpenTable'
            elif Company == '439':
                choices = 'Bandcamp'
            elif Company == '440':
                choices = 'Stack Overflow'
            elif Company == '441':
                choices = 'PokerStars'
            elif Company == '442':
                choices = 'Adda247'
            elif Company == '443':
                choices = 'Uno Health'
            elif Company == '444':
                choices = 'Qualcomm'
            elif Company == '445':
                choices = 'Lending Club'
            elif Company == '446':
                choices = 'MariaDB'
            elif Company == '447':
                choices = 'Deepgram'
            elif Company == '448':
                choices = 'Acronis'
            elif Company == '449':
                choices = 'Neon'
            elif Company == '450':
                choices = 'Blue Origin'
            elif Company == '451':
                choices = 'Braid'
            elif Company == '452':
                choices = 'Product Hunt'
            elif Company == '453':
                choices = 'VTrips'
            elif Company == '454':
                choices = 'Juniper Networks'
            elif Company == '455':
                choices = 'InvestCloud'
            elif Company == '456':
                choices = 'Brave'
            elif Company == '457':
                choices = 'Dash'
            elif Company == '458':
                choices = 'Shift'
            elif Company == '459':
                choices = 'Yuga Labs'
            elif Company == '460':
                choices = 'Bizongo'
            elif Company == '461':
                choices = 'SchoolMint'
            elif Company == '462':
                choices = 'SeekOut'
            elif Company == '463':
                choices = 'Arrival'
            elif Company == '464':
                choices = 'Ledger'
            elif Company == '465':
                choices = 'Qualtrics'
            elif Company == '466':
                choices = 'Hopper'
            elif Company == '467':
                choices = 'Bird'
            elif Company == '468':
                choices = 'Dare'
            elif Company == '469':
                choices = 'Sendoso'
            elif Company == '470':
                choices = 'Chainalysis'
            elif Company == '471':
                choices = 'Synapse'
            elif Company == '472':
                choices = 'Chia Network'
            elif Company == '473':
                choices = 'IronNet'
            elif Company == '474':
                choices = 'Sono Motors'
            elif Company == '475':
                choices = 'Cowbell'
            elif Company == '476':
                choices = 'N26'
            elif Company == '477':
                choices = 'Andgo'
            elif Company == '478':
                choices = 'Vendasta'
            elif Company == '479':
                choices = 'Epic Games'
            elif Company == '480':
                choices = 'Lululemon Studio'
            elif Company == '481':
                choices = 'Fit Analytics'
            elif Company == '482':
                choices = 'Fi.Money'
            elif Company == '483':
                choices = 'Dunzo'
            elif Company == '484':
                choices = 'Talkdesk'
            elif Company == '485':
                choices = 'Lucid Software'
            elif Company == '486':
                choices = 'Eat Just'
            elif Company == '487':
                choices = 'Appsmith'
            elif Company == '488':
                choices = 'Roblox'
            elif Company == '489':
                choices = 'Foodpanda'
            elif Company == '490':
                choices = 'Recast'
            elif Company == '491':
                choices = 'DealShare'
            elif Company == '492':
                choices = 'Merative'
            elif Company == '493':
                choices = 'Robinhood'
            elif Company == '494':
                choices = 'Akudo'
            elif Company == '495':
                choices = 'Outreach'
            elif Company == '496':
                choices = 'Truss Works'
            elif Company == '497':
                choices = 'Nowadays'
            elif Company == '498':
                choices = 'Hooray Foods'
            elif Company == '499':
                choices = 'Sage Therapeutics copy'
            elif Company == '500':
                choices = '7shifts'
            elif Company == '501':
                choices = 'Velocity'
            elif Company == '502':
                choices = 'Airtable'
            elif Company == '503':
                choices = 'Project44'
            elif Company == '504':
                choices = 'R3'
            elif Company == '505':
                choices = 'Akili Labs'
            elif Company == '506':
                choices = 'Evolve'
            elif Company == '507':
                choices = 'Binance.US'
            elif Company == '508':
                choices = 'Paper'
            elif Company == '509':
                choices = 'Homeday'
            elif Company == '510':
                choices = 'At-Bay'
            elif Company == '511':
                choices = 'Eurora'
            elif Company == '512':
                choices = 'Chargebee'
            elif Company == '513':
                choices = 'Divvy Homes'
            elif Company == '514':
                choices = 'Grabango'
            elif Company == '515':
                choices = 'Bonterra '
            elif Company == '516':
                choices = 'Mollie'
            elif Company == '517':
                choices = 'Oyster'
            elif Company == '518':
                choices = 'Sensor Tower'
            elif Company == '519':
                choices = 'Drift'
            elif Company == '520':
                choices = 'Hijra'
            elif Company == '521':
                choices = 'Roku'
            elif Company == '522':
                choices = 'ForeScout'
            elif Company == '523':
                choices = 'Better.com'
            elif Company == '524':
                choices = 'iSpecimen'
            elif Company == '525':
                choices = 'MaxMilhas'
            elif Company == '526':
                choices = 'Absci'
            elif Company == '527':
                choices = 'Hodinkee'
            elif Company == '528':
                choices = 'Talent.com'
            elif Company == '529':
                choices = 'mPharma'
            elif Company == '530':
                choices = 'Xolo'
            elif Company == '531':
                choices = 'Nexar'
            elif Company == '532':
                choices = 'Khatabook'
            elif Company == '533':
                choices = 'Clearcover'
            elif Company == '534':
                choices = 'Gated'
            elif Company == '535':
                choices = 'Lunchtime'
            elif Company == '536':
                choices = 'Pegasystems'
            elif Company == '537':
                choices = 'Biofourmis'
            elif Company == '538':
                choices = 'Malwarebytes'
            elif Company == '539':
                choices = 'SkyKick'
            elif Company == '540':
                choices = 'Omuni'
            elif Company == '541':
                choices = 'Kenko Health'
            elif Company == '542':
                choices = 'Huma'
            elif Company == '543':
                choices = 'Zeplin'
            elif Company == '544':
                choices = '123Milhas'
            elif Company == '545':
                choices = 'Zebra Technologies'
            elif Company == '546':
                choices = 'CoinSwitch'
            elif Company == '547':
                choices = 'Clockwork'
            elif Company == '548':
                choices = 'SenseTime'
            elif Company == '549':
                choices = 'HackerRank'
            elif Company == '550':
                choices = 'Cuemath'
            elif Company == '551':
                choices = 'Fortinet'
            elif Company == '552':
                choices = 'Captiv8'
            elif Company == '553':
                choices = 'Chingari'
            elif Company == '554':
                choices = 'Atlas'
            elif Company == '555':
                choices = 'Veriff'
            elif Company == '556':
                choices = 'BlackLine'
            elif Company == '557':
                choices = 'Rivos'
            elif Company == '558':
                choices = 'Cellulant'
            elif Company == '559':
                choices = 'JOIN'
            elif Company == '560':
                choices = 'CoinDCX'
            elif Company == '561':
                choices = 'Datagen'
            elif Company == '562':
                choices = 'Hypefast'
            elif Company == '563':
                choices = 'Tempo Automation'
            elif Company == '564':
                choices = 'Recur'
            elif Company == '565':
                choices = 'Unite Us'
            elif Company == '566':
                choices = 'Twiga'
            elif Company == '567':
                choices = 'Spartan Poker'
            elif Company == '568':
                choices = 'Times Internet '
            elif Company == '569':
                choices = 'Detectify'
            elif Company == '570':
                choices = 'Embrace'
            elif Company == '571':
                choices = 'Zylo'
            elif Company == '572':
                choices = 'AppFolio'
            elif Company == '573':
                choices = 'StreamElements'
            elif Company == '574':
                choices = 'FlexCar'
            elif Company == '575':
                choices = 'Noice'
            elif Company == '576':
                choices = 'SecureWorks'
            elif Company == '577':
                choices = 'Easee'
            elif Company == '578':
                choices = 'CoinDesk'
            elif Company == '579':
                choices = 'iQiyi Smart'
            elif Company == '580':
                choices = 'LingoAce'
            elif Company == '581':
                choices = 'Shutterfly'
            elif Company == '582':
                choices = 'SHINE Technologies'
            elif Company == '583':
                choices = 'Hike'
            elif Company == '584':
                choices = 'NCC Group'
            elif Company == '585':
                choices = 'Blend'
            elif Company == '586':
                choices = 'Niantic'
            elif Company == '587':
                choices = 'Babylon Health'
            elif Company == '588':
                choices = 'Dealtale'
            elif Company == '589':
                choices = 'Bukalapak'
            elif Company == '590':
                choices = 'Podium'
            elif Company == '591':
                choices = 'Quizy'
            elif Company == '592':
                choices = 'StyleSeat'
            elif Company == '593':
                choices = 'Thoughtworks'
            elif Company == '594':
                choices = 'Rapid7'
            elif Company == '595':
                choices = 'MPL'
            elif Company == '596':
                choices = 'Doximity'
            elif Company == '597':
                choices = '23andMe'
            elif Company == '598':
                choices = 'Caliva'
            elif Company == '599':
                choices = 'Sendy'
            elif Company == '600':
                choices = 'Verse'
            elif Company == '601':
                choices = 'Qomplx'
            elif Company == '602':
                choices = 'CodeClan'
            elif Company == '603':
                choices = 'Astra'
            elif Company == '604':
                choices = 'Big Cabal Media'
            elif Company == '605':
                choices = 'Bardee'
            elif Company == '606':
                choices = 'Aware'
            elif Company == '607':
                choices = 'Ayoconnect'
            elif Company == '608':
                choices = 'Finastra'
            elif Company == '609':
                choices = 'Spinny'
            elif Company == '610':
                choices = 'Tekion'
            elif Company == '611':
                choices = 'BetterUp'
            elif Company == '612':
                choices = 'Augury'
            elif Company == '613':
                choices = 'Gem'
            elif Company == '614':
                choices = 'Gupy'
            elif Company == '615':
                choices = 'FamPay'
            elif Company == '616':
                choices = 'Actyv.ai'
            elif Company == '617':
                choices = 'ConnectedH'
            elif Company == '618':
                choices = 'DICE'
            elif Company == '619':
                choices = 'HackerOne'
            elif Company == '620':
                choices = 'Silofit'
            elif Company == '621':
                choices = 'Vesttoo'
            elif Company == '622':
                choices = 'Planet'
            elif Company == '623':
                choices = 'Archipelago'
            elif Company == '624':
                choices = 'Increff'
            elif Company == '625':
                choices = 'inDrive'
            elif Company == '626':
                choices = 'Outreach '
            elif Company == '627':
                choices = 'Qoala'
            elif Company == '628':
                choices = 'Fable'
            elif Company == '629':
                choices = 'Cambricon'
            elif Company == '630':
                choices = 'Kape Technologies'
            elif Company == '631':
                choices = 'Eroad'
            elif Company == '632':
                choices = 'Kape'
            elif Company == '633':
                choices = 'Homology'
            elif Company == '634':
                choices = 'Milkbasket'
            elif Company == '635':
                choices = 'Wish'
            elif Company == '636':
                choices = 'Point'
            elif Company == '637':
                choices = 'Akseleran'
            elif Company == '638':
                choices = 'Datree'
            elif Company == '639':
                choices = 'Degreed'
            elif Company == '640':
                choices = 'Copia'
            elif Company == '641':
                choices = 'Figure'
            elif Company == '642':
                choices = 'Calendly'
            elif Company == '643':
                choices = 'Myntra'
            elif Company == '644':
                choices = 'Kleos Space'
            elif Company == '645':
                choices = 'Ripl'
            elif Company == '646':
                choices = 'Deep Instict'
            elif Company == '647':
                choices = 'Pluralsight'
            elif Company == '648':
                choices = 'AppHarvest'
            elif Company == '649':
                choices = 'Arive'
            elif Company == '650':
                choices = 'Onfido'
            elif Company == '651':
                choices = 'PathAI'
            elif Company == '652':
                choices = 'Bundle Africa'
            elif Company == '653':
                choices = 'Viaplay'
            elif Company == '654':
                choices = 'Stoa'
            elif Company == '655':
                choices = 'MiQ'
            elif Company == '656':
                choices = 'Phunware'
            elif Company == '657':
                choices = 'Saarthi.ai'
            elif Company == '658':
                choices = 'AgentSync'
            elif Company == '659':
                choices = 'Inspirato'
            elif Company == '660':
                choices = 'Tilia'
            elif Company == '661':
                choices = 'Blue Apron'
            elif Company == '662':
                choices = 'Cameo'
            elif Company == '663':
                choices = 'Square Roots'
            elif Company == '664':
                choices = 'Code42'
            elif Company == '665':
                choices = 'Ezoic'
            elif Company == '666':
                choices = 'Lamudi Indonesia'
            elif Company == '667':
                choices = 'Binance'
            elif Company == '668':
                choices = 'PayScale'
            elif Company == '669':
                choices = 'Navi Technologies'
            elif Company == '670':
                choices = 'Skill Lync'
            elif Company == '671':
                choices = 'AudioCodes'
            elif Company == '672':
                choices = 'Deepwatch'
            elif Company == '673':
                choices = 'Centr'
            elif Company == '674':
                choices = 'Factorial'
            elif Company == '675':
                choices = 'Bark'
            elif Company == '676':
                choices = 'Khoros'
            elif Company == '677':
                choices = 'Netlify'
            elif Company == '678':
                choices = 'SAS'
            elif Company == '679':
                choices = 'Dapper Labs'
            elif Company == '680':
                choices = 'DeepVerge'
            elif Company == '681':
                choices = 'Freightos'
            elif Company == '682':
                choices = 'Circle'
            elif Company == '683':
                choices = 'CyberGRX'
            elif Company == '684':
                choices = 'Duck Creek Technologies'
            elif Company == '685':
                choices = 'Matterport'
            elif Company == '686':
                choices = 'Everquote'
            elif Company == '687':
                choices = 'Built Technologies'
            elif Company == '688':
                choices = 'Butterfly Network copy'
            elif Company == '689':
                choices = 'Dukaan'
            elif Company == '690':
                choices = 'Jasper'
            elif Company == '691':
                choices = 'FrontRow'
            elif Company == '692':
                choices = 'IntelyCare'
            elif Company == '693':
                choices = 'Latch'
            elif Company == '694':
                choices = 'Motive'
            elif Company == '695':
                choices = 'Medsaf'
            elif Company == '696':
                choices = 'Evernote'
            elif Company == '697':
                choices = 'PaulCamper'
            elif Company == '698':
                choices = 'Trellix'
            elif Company == '699':
                choices = 'Amdocs'
            elif Company == '700':
                choices = 'FNZ'
            elif Company == '701':
                choices = 'Perfect Day'
            elif Company == '702':
                choices = 'Solidigm'
            elif Company == '703':
                choices = 'TytoCare'
            elif Company == '704':
                choices = 'Circles.Life'
            elif Company == '705':
                choices = 'ConnectRN'
            elif Company == '706':
                choices = 'Crunchbase'
            elif Company == '707':
                choices = 'DayTwo'
            elif Company == '708':
                choices = 'Athennian'
            elif Company == '709':
                choices = 'Vista Group'
            elif Company == '710':
                choices = 'Highsnobiety'
            elif Company == '711':
                choices = 'Zip'
            elif Company == '712':
                choices = 'Buzzer'
            elif Company == '713':
                choices = 'Lunya'
            elif Company == '714':
                choices = 'MediaMath'
            elif Company == '715':
                choices = 'Petal'
            elif Company == '716':
                choices = 'Headspace'
            elif Company == '717':
                choices = 'Artsy'
            elif Company == '718':
                choices = 'Candy Digital'
            elif Company == '719':
                choices = 'Xiaomi India'
            elif Company == '720':
                choices = 'Torii'
            elif Company == '721':
                choices = 'Insider Intelligence'
            elif Company == '722':
                choices = 'Merama'
            elif Company == '723':
                choices = 'Qyuki'
            elif Company == '724':
                choices = 'Stripe'
            elif Company == '725':
                choices = 'Vowel'
            elif Company == '726':
                choices = 'ClickUp'
            elif Company == '727':
                choices = 'Ludia'
            elif Company == '728':
                choices = 'Karat'
            elif Company == '729':
                choices = 'Plex'
            elif Company == '730':
                choices = 'Starburst'
            elif Company == '731':
                choices = 'Zapier'
            elif Company == '732':
                choices = 'Selina'
            elif Company == '733':
                choices = 'Tibber'
            elif Company == '734':
                choices = 'ClearPay'
            elif Company == '735':
                choices = 'Eyowo'
            elif Company == '736':
                choices = 'Honor'
            elif Company == '737':
                choices = 'Lordstown Motors'
            elif Company == '738':
                choices = 'Waze'
            elif Company == '739':
                choices = 'Payoneer'
            elif Company == '740':
                choices = 'Joonko'
            elif Company == '741':
                choices = 'IRL'
            elif Company == '742':
                choices = 'Retool'
            elif Company == '743':
                choices = 'Anaplan'
            elif Company == '744':
                choices = 'Uber'
            elif Company == '745':
                choices = 'Tackle.io'
            elif Company == '746':
                choices = 'Ritual'
            elif Company == '747':
                choices = 'Friday Health Plans'
            elif Company == '748':
                choices = 'Mutiny'
            elif Company == '749':
                choices = 'Grab'
            elif Company == '750':
                choices = 'OLX Group'
            elif Company == '751':
                choices = 'AvantStay'
            elif Company == '752':
                choices = 'Karakuki'
            elif Company == '753':
                choices = 'Panther'
            elif Company == '754':
                choices = 'Fuzzy'
            elif Company == '755':
                choices = 'Mojocare'
            elif Company == '756':
                choices = 'Nikola'
            elif Company == '757':
                choices = 'Pilot'
            elif Company == '758':
                choices = 'Karshare'
            elif Company == '759':
                choices = 'CareRev'
            elif Company == '760':
                choices = 'TADA'
            elif Company == '761':
                choices = 'Cerner'
            elif Company == '762':
                choices = 'Bitwise'
            elif Company == '763':
                choices = 'TrueCar'
            elif Company == '764':
                choices = 'Olo'
            elif Company == '765':
                choices = 'Mamaearth'
            elif Company == '766':
                choices = 'Western Digital'
            elif Company == '767':
                choices = 'JupiterOne'
            elif Company == '768':
                choices = 'Zalando'
            elif Company == '769':
                choices = 'Grubhub'
            elif Company == '770':
                choices = 'GoCardless'
            elif Company == '771':
                choices = 'Pendo'
            elif Company == '772':
                choices = 'Chegg'
            elif Company == '773':
                choices = 'dot.LA'
            elif Company == '774':
                choices = 'TaxBit'
            elif Company == '775':
                choices = 'Tiki'
            elif Company == '776':
                choices = 'Trybe'
            elif Company == '777':
                choices = 'Expel'
            elif Company == '778':
                choices = 'Cityblock Health'
            elif Company == '779':
                choices = 'Highspot'
            elif Company == '780':
                choices = 'Cohesity'
            elif Company == '781':
                choices = 'Freshworks'
            elif Company == '782':
                choices = 'Opora'
            elif Company == '783':
                choices = 'Nubank'
            elif Company == '784':
                choices = 'Sumo Logic'
            elif Company == '785':
                choices = 'Flatiron Health'
            elif Company == '786':
                choices = 'HashiCorp'
            elif Company == '787':
                choices = 'Ursa Major'
            elif Company == '788':
                choices = 'Coherent'
            elif Company == '789':
                choices = 'Reddit'
            elif Company == '790':
                choices = 'Linktree'
            elif Company == '791':
                choices = 'Dragos'
            elif Company == '792':
                choices = 'Mara'
            elif Company == '793':
                choices = 'Bunnii'
            elif Company == '794':
                choices = 'Azibo'
            elif Company == '795':
                choices = 'Meati Foods'
            elif Company == '796':
                choices = 'ZoomInfo'
            elif Company == '797':
                choices = 'Staffbase'
            elif Company == '798':
                choices = 'Zume'
            elif Company == '799':
                choices = 'Haven Technologies'
            elif Company == '800':
                choices = 'Mural'
            elif Company == '801':
                choices = 'Glamyo Health'
            elif Company == '802':
                choices = 'Outbrain'
            elif Company == '803':
                choices = 'CloudTrucks'
            elif Company == '804':
                choices = 'CoachHub'
            elif Company == '805':
                choices = 'Fractal Software'
            elif Company == '806':
                choices = 'SentinelOne'
            elif Company == '807':
                choices = 'SmartAsset'
            elif Company == '808':
                choices = 'Zendesk'
            elif Company == '809':
                choices = 'ZipRecruiter'
            elif Company == '810':
                choices = 'Mux'
            elif Company == '811':
                choices = 'Taxfix'
            elif Company == '812':
                choices = 'Mensa Brands'
            elif Company == '813':
                choices = 'Coupa'
            elif Company == '814':
                choices = 'Nansen'
            elif Company == '815':
                choices = 'PacketFabric'
            elif Company == '816':
                choices = 'DHI Group'
            elif Company == '817':
                choices = 'BenevolentAI'
            elif Company == '818':
                choices = 'Circus Kitchens'
            elif Company == '819':
                choices = 'Kabam'
            elif Company == '820':
                choices = 'Guild'
            elif Company == '821':
                choices = 'WillowTree'
            elif Company == '822':
                choices = 'Flink'
            elif Company == '823':
                choices = 'Alibaba Cloud'
            elif Company == '824':
                choices = 'Brainly'
            elif Company == '825':
                choices = 'Reliance JioMart'
            elif Company == '826':
                choices = 'SoundCloud'
            elif Company == '827':
                choices = 'Tractable'
            elif Company == '828':
                choices = 'Daylight'
            elif Company == '829':
                choices = 'FemTech Health'
            elif Company == '830':
                choices = 'Paperless Parts'
            elif Company == '831':
                choices = 'Nuance Communications'
            elif Company == '832':
                choices = 'Moss'
            elif Company == '833':
                choices = 'Pie Insurance'
            elif Company == '834':
                choices = 'Clearbit'
            elif Company == '835':
                choices = 'dbt Labs'
            elif Company == '836':
                choices = 'L1ght'
            elif Company == '837':
                choices = 'Nextbite'
            elif Company == '838':
                choices = 'Formstack'
            elif Company == '839':
                choices = 'Lemonade'
            elif Company == '840':
                choices = 'DroneUp'
            elif Company == '841':
                choices = 'Quanto'
            elif Company == '842':
                choices = 'Cana'
            elif Company == '843':
                choices = 'Nuro'
            elif Company == '844':
                choices = 'Telenav'
            elif Company == '845':
                choices = 'Happay'
            elif Company == '846':
                choices = 'Slickdeals'
            elif Company == '847':
                choices = 'Toothsi'
            elif Company == '848':
                choices = 'Everlaw'
            elif Company == '849':
                choices = 'Tessera'
            elif Company == '850':
                choices = 'Varo'
            elif Company == '851':
                choices = 'CS Disco'
            elif Company == '852':
                choices = 'Redbubble'
            elif Company == '853':
                choices = 'Similarweb'
            elif Company == '854':
                choices = 'Akamai'
            elif Company == '855':
                choices = 'Sonatype'
            elif Company == '856':
                choices = 'Marqeta'
            elif Company == '857':
                choices = 'Momentis Surgical'
            elif Company == '858':
                choices = 'Glean AI'
            elif Company == '859':
                choices = 'Everledger'
            elif Company == '860':
                choices = 'Twist Bioscience'
            elif Company == '861':
                choices = 'Meesho'
            elif Company == '862':
                choices = 'Teachmint'
            elif Company == '863':
                choices = 'Eventus'
            elif Company == '864':
                choices = 'Shopify'
            elif Company == '865':
                choices = 'Sabre'
            elif Company == '866':
                choices = 'Scribe Media'
            elif Company == '867':
                choices = 'Autograph'
            elif Company == '868':
                choices = 'Earnix'
            elif Company == '869':
                choices = 'Karma'
            elif Company == '870':
                choices = 'Glassbox'
            elif Company == '871':
                choices = 'Upwork'
            elif Company == '872':
                choices = 'Cars24'
            elif Company == '873':
                choices = 'Brightcove'
            elif Company == '874':
                choices = 'Healthy.io'
            elif Company == '875':
                choices = 'Zymergen'
            elif Company == '876':
                choices = 'TheSkimm'
            elif Company == '877':
                choices = 'Brightline'
            elif Company == '878':
                choices = 'Bishop Fox'
            elif Company == '879':
                choices = 'Zoomo'
            elif Company == '880':
                choices = 'Vallai'
            elif Company == '881':
                choices = 'Lev'
            elif Company == '882':
                choices = 'PharmEasy'
            elif Company == '883':
                choices = 'Vah Vah!'
            elif Company == '884':
                choices = 'Cogito'
            elif Company == '885':
                choices = 'Embark Vet'
            elif Company == '886':
                choices = 'Poparazzi'
            elif Company == '887':
                choices = 'Providoor'
            elif Company == '888':
                choices = 'Dropbox'
            elif Company == '889':
                choices = 'Alteryx'
            elif Company == '890':
                choices = 'Greenhouse'
            elif Company == '891':
                choices = 'Rebellion Defense'
            elif Company == '892':
                choices = 'Poppulo'
            elif Company == '893':
                choices = 'Megaport'
            elif Company == '894':
                choices = 'Airtasker'
            elif Company == '895':
                choices = 'Tickertape'
            elif Company == '896':
                choices = 'Clubhouse'
            elif Company == '897':
                choices = 'Oddle'
            elif Company == '898':
                choices = 'Extramarks'
            elif Company == '899':
                choices = 'Teampay'
            elif Company == '900':
                choices = 'RenoRun'
            elif Company == '901':
                choices = 'Rapid'
            elif Company == '902':
                choices = 'Red Hat'
            elif Company == '903':
                choices = 'BigPanda'
            elif Company == '904':
                choices = 'Lyft'
            elif Company == '905':
                choices = 'Benchling'
            elif Company == '906':
                choices = 'Koo'
            elif Company == '907':
                choices = 'Open'
            elif Company == '908':
                choices = 'Gloat'
            elif Company == '909':
                choices = 'Insider'
            elif Company == '910':
                choices = 'Iress'
            elif Company == '911':
                choices = 'Lenovo'
            elif Company == '912':
                choices = 'WalkMe'
            elif Company == '913':
                choices = 'Opendoor'
            elif Company == '914':
                choices = 'Noon'
            elif Company == '915':
                choices = 'Culture Amp'
            elif Company == '916':
                choices = 'TRM Labs'
            elif Company == '917':
                choices = 'CoLab'
            elif Company == '918':
                choices = 'Ten Square Games'
            elif Company == '919':
                choices = 'Ynsect'
            elif Company == '920':
                choices = 'Kumu'
            elif Company == '921':
                choices = 'Utopia Music'
            elif Company == '922':
                choices = 'Quadream'
            elif Company == '923':
                choices = 'Drip Capital'
            elif Company == '924':
                choices = 'Community Gaming'
            elif Company == '925':
                choices = 'Calibrate'
            elif Company == '926':
                choices = 'OpenClassrooms'
            elif Company == '927':
                choices = 'Sayurbox'
            elif Company == '928':
                choices = 'Snyk'
            elif Company == '929':
                choices = 'Astronomer'
            elif Company == '930':
                choices = 'Bluepad'
            elif Company == '931':
                choices = 'Heygo'
            elif Company == '932':
                choices = 'Lazerpay'
            elif Company == '933':
                choices = 'Mediafly'
            elif Company == '934':
                choices = 'Science 37'
            elif Company == '935':
                choices = 'Medtronic'
            elif Company == '936':
                choices = 'Milkrun'
            elif Company == '937':
                choices = 'Redfin'
            elif Company == '938':
                choices = 'Permutive'
            elif Company == '939':
                choices = 'Examedi'
            elif Company == '940':
                choices = 'Acxiom'
            elif Company == '941':
                choices = 'Euler Motors'
            elif Company == '942':
                choices = 'Reforge'
            elif Company == '943':
                choices = 'Nori'
            elif Company == '944':
                choices = 'Practo'
            elif Company == '945':
                choices = 'Pear Therapeutics'
            elif Company == '946':
                choices = 'Workit Health'
            elif Company == '947':
                choices = 'Absolute Software'
            elif Company == '948':
                choices = 'Avocargo'
            elif Company == '949':
                choices = 'Amplitude'
            elif Company == '950':
                choices = '1K Kirana'
            elif Company == '951':
                choices = 'Foundation Medicine'
            elif Company == '952':
                choices = 'Boost'
            elif Company == '953':
                choices = 'Cin7'
            elif Company == '954':
                choices = 'Hyland Software'
            elif Company == '955':
                choices = 'View'
            elif Company == '956':
                choices = 'Guideline'
            elif Company == '957':
                choices = 'Domestika'
            elif Company == '958':
                choices = 'Airbyte'
            elif Company == '959':
                choices = 'Hulu'
            elif Company == '960':
                choices = 'LendingTree'
            elif Company == '961':
                choices = 'FanClash'
            elif Company == '962':
                choices = 'Loop'
            elif Company == '963':
                choices = 'Crossbeam'
            elif Company == '964':
                choices = 'AnswerLab'
            elif Company == '965':
                choices = 'Endowus'
            elif Company == '966':
                choices = 'GoodWorker'
            elif Company == '967':
                choices = 'Kyndryl'
            elif Company == '968':
                choices = 'Nowports'
            elif Company == '969':
                choices = 'Unacademy'
            elif Company == '970':
                choices = 'CoverMyMeds'
            elif Company == '971':
                choices = 'Seagate'
            elif Company == '972':
                choices = 'iCAD'
            elif Company == '973':
                choices = 'Anyline'
            elif Company == '974':
                choices = 'OnePipe'
            elif Company == '975':
                choices = 'Lucid Motors'
            elif Company == '976':
                choices = 'Blue Nile'
            elif Company == '977':
                choices = 'AEye'
            elif Company == '978':
                choices = 'Rackspace'
            elif Company == '979':
                choices = 'Better Therapeutics'
            elif Company == '980':
                choices = 'Aspiration'
            elif Company == '981':
                choices = 'The Meet Group'
            elif Company == '982':
                choices = 'Cimpress'
            elif Company == '983':
                choices = 'TakeOff'
            elif Company == '984':
                choices = 'Slite'
            elif Company == '985':
                choices = 'Logitech'
            elif Company == '986':
                choices = 'Glassdoor'
            elif Company == '987':
                choices = 'Wejo'
            elif Company == '988':
                choices = 'Copper'
            elif Company == '989':
                choices = 'Rewind'
            elif Company == '990':
                choices = 'Roofstock'
            elif Company == '991':
                choices = 'Just Eat'
            elif Company == '992':
                choices = 'Marvell'
            elif Company == '993':
                choices = 'Workhuman'
            elif Company == '994':
                choices = 'Xing'
            elif Company == '995':
                choices = 'Mr Yum'
            elif Company == '996':
                choices = 'Smallcase'
            elif Company == '997':
                choices = 'GAMURS Group'
            elif Company == '998':
                choices = 'Laybuy'
            elif Company == '999':
                choices = 'Huuuge Games'
            elif Company == '1000':
                choices = 'Livspace'
            elif Company == '1001':
                choices = 'Symend'
            elif Company == '1002':
                choices = 'Candor Technology'
            elif Company == '1003':
                choices = 'Runtastic'
            elif Company == '1004':
                choices = 'Leafly'
            elif Company == '1005':
                choices = 'Bonusly'
            elif Company == '1006':
                choices = 'Klaviyo'
            elif Company == '1007':
                choices = 'Boxed'
            elif Company == '1008':
                choices = 'TradeWindow'
            elif Company == '1009':
                choices = 'Hometap'
            elif Company == '1010':
                choices = 'Fetch'
            elif Company == '1011':
                choices = 'Anchorage Digital'
            elif Company == '1012':
                choices = 'Avidbots'
            elif Company == '1013':
                choices = 'Samsung'
            elif Company == '1014':
                choices = 'Kaleidoscope'
            elif Company == '1015':
                choices = 'GoTo Group'
            elif Company == '1016':
                choices = 'Cookpad'
            elif Company == '1017':
                choices = 'Xero'
            elif Company == '1018':
                choices = 'Shopee'
            elif Company == '1019':
                choices = 'Wave Financial'
            elif Company == '1020':
                choices = 'Morning Brew'
            elif Company == '1021':
                choices = 'Neoleukin Therapeutics'
            elif Company == '1022':
                choices = 'Toucan'
            elif Company == '1023':
                choices = 'Appcues'
            elif Company == '1024':
                choices = 'Catch'
            elif Company == '1025':
                choices = 'RDX Works'
            elif Company == '1026':
                choices = 'Take-Two Interactive'
            elif Company == '1027':
                choices = 'Atlassian'
            elif Company == '1028':
                choices = 'UKG'
            elif Company == '1029':
                choices = 'UpGrad'
            elif Company == '1030':
                choices = 'HomeLane'
            elif Company == '1031':
                choices = 'Ankorstore'
            elif Company == '1032':
                choices = 'No Fluff Jobs'
            elif Company == '1033':
                choices = 'Loft'
            elif Company == '1034':
                choices = 'Embark Trucks'
            elif Company == '1035':
                choices = 'Lendi'
            elif Company == '1036':
                choices = 'UserTesting'
            elif Company == '1037':
                choices = 'Airbnb'
            elif Company == '1038':
                choices = 'Accolade'
            elif Company == '1039':
                choices = 'Zscaler'
            elif Company == '1040':
                choices = 'MasterClass'
            elif Company == '1041':
                choices = 'Ambev Tech'
            elif Company == '1042':
                choices = 'Fittr'
            elif Company == '1043':
                choices = 'CNET'
            elif Company == '1044':
                choices = 'Comparis'
            elif Company == '1045':
                choices = 'Kandela'
            elif Company == '1046':
                choices = 'Truckstop.com'
            elif Company == '1047':
                choices = 'iFood'
            elif Company == '1048':
                choices = 'Color Health'
            elif Company == '1049':
                choices = 'PayFit'
            elif Company == '1050':
                choices = 'Yellow.ai'
            elif Company == '1051':
                choices = 'Protego Trust Bank'
            elif Company == '1052':
                choices = 'Eventbrite'
            elif Company == '1053':
                choices = 'DUX Education'
            elif Company == '1054':
                choices = 'Cerebral'
            elif Company == '1055':
                choices = 'Amount'
            elif Company == '1056':
                choices = 'Palantir'
            elif Company == '1057':
                choices = 'Stytch'
            elif Company == '1058':
                choices = 'BitSight'
            elif Company == '1059':
                choices = 'Twitter'
            elif Company == '1060':
                choices = 'Ericsson'
            elif Company == '1061':
                choices = 'SAP Labs'
            elif Company == '1062':
                choices = 'Velodyne Lidar'
            elif Company == '1063':
                choices = 'Medallia'
            elif Company == '1064':
                choices = 'Lucira Health'
            elif Company == '1065':
                choices = 'Stax'
            elif Company == '1066':
                choices = 'EQRx'
            elif Company == '1067':
                choices = 'Poshmark'
            elif Company == '1068':
                choices = 'OneFootball'
            elif Company == '1069':
                choices = 'The Iconic'
            elif Company == '1070':
                choices = 'EVgo'
            elif Company == '1071':
                choices = 'StrongDM'
            elif Company == '1072':
                choices = 'Messari'
            elif Company == '1073':
                choices = 'Vibrent Health'
            elif Company == '1074':
                choices = 'Synamedia'
            elif Company == '1075':
                choices = 'TaskUs'
            elif Company == '1076':
                choices = 'Arch Oncology'
            elif Company == '1077':
                choices = 'Immutable'
            elif Company == '1078':
                choices = 'Jounce Therapeutics'
            elif Company == '1079':
                choices = 'Locomation'
            elif Company == '1080':
                choices = 'Green Labs'
            elif Company == '1081':
                choices = 'Crunchyroll'
            elif Company == '1082':
                choices = 'Ethos Life'
            elif Company == '1083':
                choices = 'Basis Technologies'
            elif Company == '1084':
                choices = 'PeerStreet'
            elif Company == '1085':
                choices = 'MyGate'
            elif Company == '1086':
                choices = 'Kinde'
            elif Company == '1087':
                choices = 'Fipola'
            elif Company == '1088':
                choices = 'HP'
            elif Company == '1089':
                choices = 'Micron'
            elif Company == '1090':
                choices = 'Tencent'
            elif Company == '1091':
                choices = 'Digimarc'
            elif Company == '1092':
                choices = 'Reserve'
            elif Company == '1093':
                choices = 'The RealReal'
            elif Company == '1094':
                choices = 'Smartsheet'
            elif Company == '1095':
                choices = 'Wix'
            elif Company == '1096':
                choices = 'ServiceTitan'
            elif Company == '1097':
                choices = 'DigitalOcean'
            elif Company == '1098':
                choices = 'Betterment'
            elif Company == '1099':
                choices = 'Momentive'
            elif Company == '1100':
                choices = 'Observe.AI'
            elif Company == '1101':
                choices = 'Religion of Sports'
            elif Company == '1102':
                choices = 'Tackle'
            elif Company == '1103':
                choices = 'Vicarious Surgical'
            elif Company == '1104':
                choices = 'Blackbaud'
            elif Company == '1105':
                choices = 'CommerceHub'
            elif Company == '1106':
                choices = 'Dropp'
            elif Company == '1107':
                choices = 'HackerEarth'
            elif Company == '1108':
                choices = 'PhableCare'
            elif Company == '1109':
                choices = 'Udemy'
            elif Company == '1110':
                choices = 'Electric'
            elif Company == '1111':
                choices = 'EMX Digital'
            elif Company == '1112':
                choices = 'PetLove'
            elif Company == '1113':
                choices = 'Collective Health'
            elif Company == '1114':
                choices = 'Magic Eden'
            elif Company == '1115':
                choices = 'Casavo'
            elif Company == '1116':
                choices = 'Moladin'
            elif Company == '1117':
                choices = 'TripleLift'
            elif Company == '1118':
                choices = 'Titan Medical'
            elif Company == '1119':
                choices = 'TikTok India'
            elif Company == '1120':
                choices = 'Syft Technologies'
            elif Company == '1121':
                choices = 'Open Co'
            elif Company == '1122':
                choices = 'Rigetti Computing'
            elif Company == '1123':
                choices = 'Wonderschool'
            elif Company == '1124':
                choices = 'Misfits Market'
            elif Company == '1125':
                choices = 'Deliveroo'
            elif Company == '1126':
                choices = 'Olive AI'
            elif Company == '1127':
                choices = 'GitLab'
            elif Company == '1128':
                choices = 'REE Automotive'
            elif Company == '1129':
                choices = 'GitHub'
            elif Company == '1130':
                choices = 'Quillt'
            elif Company == '1131':
                choices = 'WeTrade'
            elif Company == '1132':
                choices = 'GoDaddy'
            elif Company == '1133':
                choices = 'Gusto'
            elif Company == '1134':
                choices = 'Gong'
            elif Company == '1135':
                choices = 'Equitybee'
            elif Company == '1136':
                choices = 'Baraja'
            elif Company == '1137':
                choices = 'Koho'
            elif Company == '1138':
                choices = 'Medly'
            elif Company == '1139':
                choices = 'Nearmap'
            elif Company == '1140':
                choices = 'Salesloft'
            elif Company == '1141':
                choices = 'Openpay'
            elif Company == '1142':
                choices = 'LearnUpon'
            elif Company == '1143':
                choices = 'Loggi'
            elif Company == '1144':
                choices = 'Catch.com.au'
            elif Company == '1145':
                choices = 'VinFast US'
            elif Company == '1146':
                choices = 'Pocket Aces'
            elif Company == '1147':
                choices = 'Clari'
            elif Company == '1148':
                choices = 'C6 Bank'
            elif Company == '1149':
                choices = 'TenureX'
            elif Company == '1150':
                choices = 'Kyruus'
            elif Company == '1151':
                choices = 'Lightico'
            elif Company == '1152':
                choices = 'Eightfold AI'
            elif Company == '1153':
                choices = 'FarEye'
            elif Company == '1154':
                choices = 'Protocol Labs'
            elif Company == '1155':
                choices = 'Built Technologies copy'
            elif Company == '1156':
                choices = 'Autodesk'
            elif Company == '1157':
                choices = 'Mindstrong'
            elif Company == '1158':
                choices = 'Miro'
            elif Company == '1159':
                choices = 'Bittrex'
            elif Company == '1160':
                choices = 'Snowplow'
            elif Company == '1161':
                choices = 'Articulate'
            elif Company == '1162':
                choices = 'NCSoft'
            elif Company == '1163':
                choices = 'Sharesies'
            elif Company == '1164':
                choices = 'Pinterest'
            elif Company == '1165':
                choices = 'DraftKings'
            elif Company == '1166':
                choices = 'Cyren'
            elif Company == '1167':
                choices = 'Workato'
            elif Company == '1168':
                choices = 'VerticalScope'
            elif Company == '1169':
                choices = 'Wheel'
            elif Company == '1170':
                choices = 'Appgate'
            elif Company == '1171':
                choices = 'Exterro'
            elif Company == '1172':
                choices = 'Ada'
            elif Company == '1173':
                choices = 'Bustle Digital Group'
            elif Company == '1174':
                choices = 'Frequency Therapeutics'
            elif Company == '1175':
                choices = 'Match Group'
            elif Company == '1176':
                choices = 'Omnipresent'
            elif Company == '1177':
                choices = 'Picnic'
            elif Company == '1178':
                choices = 'NetApp'
            elif Company == '1179':
                choices = 'Workday'
            elif Company == '1180':
                choices = 'Upstart'
            elif Company == '1181':
                choices = 'Software AG'
            elif Company == '1182':
                choices = 'Wefox'
            elif Company == '1183':
                choices = 'Tilting Point'
            elif Company == '1184':
                choices = 'Gokada'
            elif Company == '1185':
                choices = 'AU10TIX'
            elif Company == '1186':
                choices = 'National Instruments'
            elif Company == '1187':
                choices = 'OpenText'
            elif Company == '1188':
                choices = 'Philips'
            elif Company == '1189':
                choices = 'Groupon'
            elif Company == '1190':
                choices = 'Impossible Foods copy'
            elif Company == '1191':
                choices = 'Chrono24'
            elif Company == '1192':
                choices = 'BM Technologies'
            elif Company == '1193':
                choices = 'Olist'
            elif Company == '1194':
                choices = 'Prime Trust'
            elif Company == '1195':
                choices = 'Quantum SI'
            elif Company == '1196':
                choices = 'Hoxhunt'
            elif Company == '1197':
                choices = 'Me Poupe'
            elif Company == '1198':
                choices = 'CoinTracker'
            elif Company == '1199':
                choices = 'SSense'
            elif Company == '1200':
                choices = 'Ruggable'
            elif Company == '1201':
                choices = 'Synopsys'
            elif Company == '1202':
                choices = 'Heycar'
            elif Company == '1203':
                choices = 'Matrixport'
            elif Company == '1204':
                choices = 'Shakepay'
            elif Company == '1205':
                choices = '#Paid'
            elif Company == '1206':
                choices = 'Decent'
            elif Company == '1207':
                choices = 'Feedzai'
            elif Company == '1208':
                choices = 'Nate'
            elif Company == '1209':
                choices = 'Soundwide'
            elif Company == '1210':
                choices = 'Confluent'
            elif Company == '1211':
                choices = 'Glisser'
            elif Company == '1212':
                choices = 'DriveWealth'
            elif Company == '1213':
                choices = 'Mode Global'
            elif Company == '1214':
                choices = 'Plus One Robotics'
            elif Company == '1215':
                choices = 'Quora'
            elif Company == '1216':
                choices = 'Lam Research'
            elif Company == '1217':
                choices = 'Luno'
            elif Company == '1218':
                choices = 'Clear Capital'
            elif Company == '1219':
                choices = 'Guardant Health'
            elif Company == '1220':
                choices = 'SirionLabs'
            elif Company == '1221':
                choices = 'PagSeguro'
            elif Company == '1222':
                choices = 'Prosus'
            elif Company == '1223':
                choices = 'Innovaccer'
            elif Company == '1224':
                choices = 'PartnerStack'
            elif Company == '1225':
                choices = 'Gitpod'
            elif Company == '1226':
                choices = 'OFFOR Health'
            elif Company == '1227':
                choices = 'Venngage'
            elif Company == '1228':
                choices = 'Corvus Insurance'
            elif Company == '1229':
                choices = 'Icon'
            elif Company == '1230':
                choices = 'PagerDuty'
            elif Company == '1231':
                choices = 'Scoro'
            elif Company == '1232':
                choices = 'Innovid'
            elif Company == '1233':
                choices = 'Booktopia'
            elif Company == '1234':
                choices = 'Ermetic'
            elif Company == '1235':
                choices = 'Namogoo'
            elif Company == '1236':
                choices = 'Camp K12'
            elif Company == '1237':
                choices = 'Gemini'
            elif Company == '1238':
                choices = 'Yext'
            elif Company == '1239':
                choices = 'BUX'
            elif Company == '1240':
                choices = 'MediBuddy'
            elif Company == '1241':
                choices = 'BitTorrent'
            elif Company == '1242':
                choices = 'Enjoei'
            elif Company == '1243':
                choices = 'Edifecs'
            elif Company == '1244':
                choices = 'Citrine Informatics'
            elif Company == '1245':
                choices = 'Avalara'
            elif Company == '1246':
                choices = 'Cyteir Therapeutics'
            elif Company == '1247':
                choices = 'Zappos'
            elif Company == '1248':
                choices = 'Capital One'
            elif Company == '1249':
                choices = 'Proterra'
            elif Company == '1250':
                choices = 'WeWork '
            elif Company == '1251':
                choices = 'Saks.com'
            elif Company == '1252':
                choices = 'Hydrow'
            elif Company == '1253':
                choices = 'Earth Rides'
            elif Company == '1254':
                choices = 'Fandom'
            elif Company == '1255':
                choices = 'IAM Robotics'
            elif Company == '1256':
                choices = 'Icertis'
            elif Company == '1257':
                choices = 'Magnite'
            elif Company == '1258':
                choices = 'Mudafy'
            elif Company == '1259':
                choices = 'Personalis'
            elif Company == '1260':
                choices = 'Prisma'
            elif Company == '1261':
                choices = 'Spaceship'
            elif Company == '1262':
                choices = 'Wallbox'
            elif Company == '1263':
                choices = 'Sophos'
            elif Company == '1264':
                choices = 'Teladoc Health'
            elif Company == '1265':
                choices = '8x8'
            elif Company == '1266':
                choices = 'Pagaya'
            elif Company == '1267':
                choices = 'Benevity'
            elif Company == '1268':
                choices = 'Jumpcloud'
            elif Company == '1269':
                choices = 'nCino'
            elif Company == '1270':
                choices = 'Starry'
            elif Company == '1271':
                choices = 'Hootsuite'
            elif Company == '1272':
                choices = 'Clue'
            elif Company == '1273':
                choices = 'Addepar'
            elif Company == '1274':
                choices = '80 Acres Farms'
            elif Company == '1275':
                choices = 'Aiven'
            elif Company == '1276':
                choices = "Bally's Interactive"
            elif Company == '1277':
                choices = 'Betterfly'
            elif Company == '1278':
                choices = 'Cazoo'
            elif Company == '1279':
                choices = 'Coda'
            elif Company == '1280':
                choices = 'Cypress.io'
            elif Company == '1281':
                choices = 'Lucid Diagnostics'
            elif Company == '1282':
                choices = 'Mavenir'
            elif Company == '1283':
                choices = 'Britishvolt'
            elif Company == '1284':
                choices = 'Clutch'
            elif Company == '1285':
                choices = 'Exotel'
            elif Company == '1286':
                choices = 'Unico'
            elif Company == '1287':
                choices = 'Tul'
            elif Company == '1288':
                choices = 'American Robotics'
            elif Company == '1289':
                choices = 'Luxury Presence'
            elif Company == '1290':
                choices = 'RingCentral'
            elif Company == '1291':
                choices = 'Avaya'
            elif Company == '1292':
                choices = 'Fishbrain'
            elif Company == '1293':
                choices = 'GoMechanic'
            elif Company == '1294':
                choices = 'Oracle'
            elif Company == '1295':
                choices = 'Rappi'
            elif Company == '1296':
                choices = 'RateGenius'
            elif Company == '1297':
                choices = 'XP'
            elif Company == '1298':
                choices = 'PagBank'
            elif Company == '1299':
                choices = 'Gramophone'
            elif Company == '1300':
                choices = 'ClearCo'
            elif Company == '1301':
                choices = 'Ignition'
            elif Company == '1302':
                choices = 'Rebel Foods'
            elif Company == '1303':
                choices = 'Captain Fresh '
            elif Company == '1304':
                choices = 'Snappy'
            elif Company == '1305':
                choices = 'BharatAgri'
            elif Company == '1306':
                choices = 'DeHaat'
            elif Company == '1307':
                choices = 'Black Shark'
            elif Company == '1308':
                choices = 'Vial'
            elif Company == '1309':
                choices = 'Carvana'
            elif Company == '1310':
                choices = 'CoSchedule'
            elif Company == '1311':
                choices = 'GoCanvas'
            elif Company == '1312':
                choices = 'Jellyfish'
            elif Company == '1313':
                choices = 'SmartNews'
            elif Company == '1314':
                choices = 'Skit.ai'
            elif Company == '1315':
                choices = 'Pier'
            elif Company == '1316':
                choices = 'Blockchain.com'
            elif Company == '1317':
                choices = 'Lattice'
            elif Company == '1318':
                choices = 'Greenlight'
            elif Company == '1319':
                choices = 'Cashfree Payments'
            elif Company == '1320':
                choices = 'Mapbox'
            elif Company == '1321':
                choices = 'Definitive Healthcare'
            elif Company == '1322':
                choices = 'Career Karma'
            elif Company == '1323':
                choices = 'Crypto.com'
            elif Company == '1324':
                choices = 'Life360'
            elif Company == '1325':
                choices = 'Rock Content'
            elif Company == '1326':
                choices = 'Tipalti'
            elif Company == '1327':
                choices = 'Jumio'
            elif Company == '1328':
                choices = 'Intrinsic'
            elif Company == '1329':
                choices = 'Citizen'
            elif Company == '1330':
                choices = 'Limeade'
            elif Company == '1331':
                choices = 'Paddle'
            elif Company == '1332':
                choices = 'Coinbase'
            elif Company == '1333':
                choices = 'Till Payments'
            elif Company == '1334':
                choices = 'ConsenSys'
            elif Company == '1335':
                choices = 'Thinkific'
            elif Company == '1336':
                choices = 'LEAD'
            elif Company == '1337':
                choices = 'Parler'
            elif Company == '1338':
                choices = 'GoBolt'
            elif Company == '1339':
                choices = 'Relevel'
            elif Company == '1340':
                choices = 'Cart.com'
            elif Company == '1341':
                choices = '100 Thieves'
            elif Company == '1342':
                choices = 'Esper'
            elif Company == '1343':
                choices = 'WHOOP'
            elif Company == '1344':
                choices = 'Fate Therapeutics'
            elif Company == '1345':
                choices = 'Century Therapeutics'
            elif Company == '1346':
                choices = 'Editas Medicine'
            elif Company == '1347':
                choices = 'Scale AI'
            elif Company == '1348':
                choices = 'Minute Media'
            elif Company == '1349':
                choices = 'Integrate'
            elif Company == '1350':
                choices = 'Huobi'
            elif Company == '1351':
                choices = 'Bounce'
            elif Company == '1352':
                choices = 'CareerArc'
            elif Company == '1353':
                choices = 'CreateMe'
            elif Company == '1354':
                choices = 'Lantern'
            elif Company == '1355':
                choices = 'Mojo Vision'
            elif Company == '1356':
                choices = 'SuperRare'
            elif Company == '1357':
                choices = 'Cue'
            elif Company == '1358':
                choices = 'SoundHound'
            elif Company == '1359':
                choices = 'Socure'
            elif Company == '1360':
                choices = 'Genesis'
            elif Company == '1361':
                choices = 'Moglix'
            elif Company == '1362':
                choices = 'Everlane'
            elif Company == '1363':
                choices = 'Pecan AI'
            elif Company == '1364':
                choices = 'Personetics'
            elif Company == '1365':
                choices = 'Twine Solutions '
            elif Company == '1366':
                choices = 'UpScalio'
            elif Company == '1367':
                choices = 'Attentive'
            elif Company == '1368':
                choices = 'Compass'
            elif Company == '1369':
                choices = 'TCR2'
            elif Company == '1370':
                choices = 'Kaltura'
            elif Company == '1371':
                choices = 'Butterfly Network'
            elif Company == '1372':
                choices = 'Vimeo'
            elif Company == '1373':
                choices = 'Wyre'
            elif Company == '1374':
                choices = 'Uniphore'
            elif Company == '1375':
                choices = 'Harappa'
            elif Company == '1376':
                choices = 'Graphcore'
            elif Company == '1377':
                choices = 'Gousto'
            elif Company == '1378':
                choices = 'Bilibili'
            elif Company == '1379':
                choices = 'Octopus Network'
            elif Company == '1380':
                choices = 'PayU'
            elif Company == '1381':
                choices = 'Element'
            elif Company == '1382':
                choices = 'Willow'
            elif Company == '1383':
                choices = 'Back Market'
            elif Company == '1384':
                choices = 'Zoopla'
            elif Company == '1385':
                choices = 'Lendis'
            elif Company == '1386':
                choices = 'Chope'
            elif Company == '1387':
                choices = 'Briza'
            elif Company == '1388':
                choices = 'StreetBees'
            elif Company == '1389':
                choices = 'Zhihu'
            elif Company == '1390':
                choices = 'Homebot'
            elif Company == '1391':
                choices = 'Health IQ'
            elif Company == '1392':
                choices = 'Xiaomi'
            elif Company == '1393':
                choices = 'YourGrocer'
            elif Company == '1394':
                choices = 'Tomorrow'
            elif Company == '1395':
                choices = 'Revelate'
            elif Company == '1396':
                choices = ' E Inc.'
            elif Company == '1397':
                choices = 'Improbable'
            elif Company == '1398':
                choices = 'Modern Treasury'
            elif Company == '1399':
                choices = 'Reach'
            elif Company == '1400':
                choices = 'LeafLink'
            elif Company == '1401':
                choices = 'Workmotion'
            elif Company == '1402':
                choices = 'Apollo'
            elif Company == '1403':
                choices = 'JD.ID'
            elif Company == '1404':
                choices = 'Quanergy Systems'
            elif Company == '1405':
                choices = 'Thumbtack'
            elif Company == '1406':
                choices = 'Komodo Health'
            elif Company == '1407':
                choices = 'Viant'
            elif Company == '1408':
                choices = 'Freshly'
            elif Company == '1409':
                choices = 'Balto'
            elif Company == '1410':
                choices = 'Caribou'
            elif Company == '1411':
                choices = 'Outschool'
            elif Company == '1412':
                choices = 'Xentral'
            elif Company == '1413':
                choices = 'Autobooks'
            elif Company == '1414':
                choices = 'Convene'
            elif Company == '1415':
                choices = 'Bol.com'
            elif Company == '1416':
                choices = 'Share Now'
            elif Company == '1417':
                choices = 'Alice'
            elif Company == '1418':
                choices = 'Primer'
            elif Company == '1419':
                choices = 'Brodmann17'
            elif Company == '1420':
                choices = 'Digital Surge'
            elif Company == '1421':
                choices = 'N-able Technologies'
            elif Company == '1422':
                choices = 'ZenLedger'
            elif Company == '1423':
                choices = 'Glints'
            elif Company == '1424':
                choices = 'Buser'
            elif Company == '1425':
                choices = 'Otonomo'
            elif Company == '1426':
                choices = 'TechTarget'
            elif Company == '1427':
                choices = 'Inscripta'
            elif Company == '1428':
                choices = 'CyCognito'
            elif Company == '1429':
                choices = 'Armis'
            elif Company == '1430':
                choices = 'FireHydrant'
            elif Company == '1431':
                choices = 'Nerdy'
            elif Company == '1432':
                choices = 'Vanta'
            elif Company == '1433':
                choices = 'Vedantu'
            elif Company == '1434':
                choices = 'Plaid'
            elif Company == '1435':
                choices = 'Recur Forever'
            elif Company == '1436':
                choices = 'Relativity'
            elif Company == '1437':
                choices = 'Integral Ad Science'
            elif Company == '1438':
                choices = 'Houzz'
            elif Company == '1439':
                choices = 'Grover'
            elif Company == '1440':
                choices = 'Lithic'
            elif Company == '1441':
                choices = 'Zywave'
            elif Company == '1442':
                choices = 'Doma'
            elif Company == '1443':
                choices = 'Weedmaps'
            elif Company == '1444':
                choices = 'Adobe'
            elif Company == '1445':
                choices = 'Perimeter 81'
            elif Company == '1446':
                choices = 'Koinly'
            elif Company == '1447':
                choices = 'Bridgit'
            elif Company == '1448':
                choices = 'Filevine'
            elif Company == '1449':
                choices = 'Moove'
            elif Company == '1450':
                choices = 'Nextiva'
            elif Company == '1451':
                choices = 'OneStudyTeam'
            elif Company == '1452':
                choices = 'Swyftx'
            elif Company == '1453':
                choices = 'Aqua Security'
            elif Company == '1454':
                choices = 'DataRails'
            elif Company == '1455':
                choices = 'Elemy'
            elif Company == '1456':
                choices = 'Route'
            elif Company == '1457':
                choices = 'OYO'
            elif Company == '1458':
                choices = 'Bybit'
            elif Company == '1459':
                choices = 'Cognyte'
            elif Company == '1460':
                choices = 'Polly'
            elif Company == '1461':
                choices = 'Homebound'
            elif Company == '1462':
                choices = 'Lora DiCarlo'
            elif Company == '1463':
                choices = 'Carousell'
            elif Company == '1464':
                choices = 'Bizzabo'
            elif Company == '1465':
                choices = 'BloomTech'
            elif Company == '1466':
                choices = 'Springbig'
            elif Company == '1467':
                choices = 'SQZ Biotech'
            elif Company == '1468':
                choices = 'Strava'
            elif Company == '1469':
                choices = 'Synlogic'
            elif Company == '1470':
                choices = 'Yapily'
            elif Company == '1471':
                choices = 'DoorDash'
            elif Company == '1472':
                choices = 'Kraken'
            elif Company == '1473':
                choices = 'Happy Money'
            elif Company == '1474':
                choices = 'Ula'
            elif Company == '1475':
                choices = 'Wonder'
            elif Company == '1476':
                choices = 'StudySmarter'
            elif Company == '1477':
                choices = 'Ualá'
            elif Company == '1478':
                choices = 'Etermax'
            elif Company == '1479':
                choices = 'Thread'
            elif Company == '1480':
                choices = 'Elastic'
            elif Company == '1481':
                choices = 'Sana'
            elif Company == '1482':
                choices = 'Venafi'
            elif Company == '1483':
                choices = 'Bitso'
            elif Company == '1484':
                choices = 'Lyst'
            elif Company == '1485':
                choices = 'CoinJar'
            elif Company == '1486':
                choices = 'Bitfront'
            elif Company == '1487':
                choices = 'Codexis'
            elif Company == '1488':
                choices = 'Firework'
            elif Company == '1489':
                choices = 'Plerk'
            elif Company == '1490':
                choices = 'Proton.ai'
            elif Company == '1491':
                choices = 'Infarm'
            elif Company == '1492':
                choices = 'Wildlife Studios'
            elif Company == '1493':
                choices = 'Hirect'
            elif Company == '1494':
                choices = 'ApplyBoard'
            elif Company == '1495':
                choices = 'Ajaib'
            elif Company == '1496':
                choices = 'ResearchGate'
            elif Company == '1497':
                choices = 'BlockFi'
            elif Company == '1498':
                choices = 'FutureLearn'
            elif Company == '1499':
                choices = 'Inspectify'
            elif Company == '1500':
                choices = 'Ledn'
            elif Company == '1501':
                choices = 'NCX'
            elif Company == '1502':
                choices = 'Spora Health'
            elif Company == '1503':
                choices = 'Change Invest'
            elif Company == '1504':
                choices = 'Zilch'
            elif Company == '1505':
                choices = 'VerSe Innovation'
            elif Company == '1506':
                choices = 'Carwow'
            elif Company == '1507':
                choices = 'Vendease'
            elif Company == '1508':
                choices = 'Lemon'
            elif Company == '1509':
                choices = 'Quidax'
            elif Company == '1510':
                choices = 'Menulog'
            elif Company == '1511':
                choices = 'Assure'
            elif Company == '1512':
                choices = 'GoodGood'
            elif Company == '1513':
                choices = 'Muni Tienda'
            elif Company == '1514':
                choices = 'SWVL'
            elif Company == '1515':
                choices = 'SIRCLO'
            elif Company == '1516':
                choices = 'Movidesk'
            elif Company == '1517':
                choices = 'Trax'
            elif Company == '1518':
                choices = 'Flash Coffee'
            elif Company == '1519':
                choices = 'Natera'
            elif Company == '1520':
                choices = 'Rapyd'
            elif Company == '1521':
                choices = 'Reynen Court'
            elif Company == '1522':
                choices = 'Jumia'
            elif Company == '1523':
                choices = 'Kitopi'
            elif Company == '1524':
                choices = 'Devo'
            elif Company == '1525':
                choices = 'GloriFi'
            elif Company == '1526':
                choices = 'Zomato'
            elif Company == '1527':
                choices = 'Synthego'
            elif Company == '1528':
                choices = 'Splyt'
            elif Company == '1529':
                choices = 'Capitolis'
            elif Company == '1530':
                choices = 'Kavak'
            elif Company == '1531':
                choices = 'Metaplex'
            elif Company == '1532':
                choices = 'Ruangguru'
            elif Company == '1533':
                choices = 'StoryBlocks'
            elif Company == '1534':
                choices = 'Unchained Capital'
            elif Company == '1535':
                choices = 'Homepoint'
            elif Company == '1536':
                choices = 'Juni'
            elif Company == '1537':
                choices = 'Chili Piper'
            elif Company == '1538':
                choices = 'TealBook'
            elif Company == '1539':
                choices = '&Open'
            elif Company == '1540':
                choices = 'Wayflyer'
            elif Company == '1541':
                choices = 'Lokalise'
            elif Company == '1542':
                choices = 'Yotpo'
            elif Company == '1543':
                choices = 'D2L'
            elif Company == '1544':
                choices = 'Dance'
            elif Company == '1545':
                choices = 'Homeward'
            elif Company == '1546':
                choices = 'Infogrid'
            elif Company == '1547':
                choices = 'Kite'
            elif Company == '1548':
                choices = 'UiPath'
            elif Company == '1549':
                choices = 'Asana'
            elif Company == '1550':
                choices = 'OwnBackup'
            elif Company == '1551':
                choices = 'Deliveroo Australia'
            elif Company == '1552':
                choices = 'Properly'
            elif Company == '1553':
                choices = 'Protocol'
            elif Company == '1554':
                choices = 'Jimdo'
            elif Company == '1555':
                choices = 'The Zebra'
            elif Company == '1556':
                choices = 'Viber'
            elif Company == '1557':
                choices = 'CaptivateIQ'
            elif Company == '1558':
                choices = 'Apollo Insurance'
            elif Company == '1559':
                choices = 'Nirvana Money'
            elif Company == '1560':
                choices = 'Oatly'
            elif Company == '1561':
                choices = 'OfferUp'
            elif Company == '1562':
                choices = 'Outside'
            elif Company == '1563':
                choices = 'Rubicon Technologies'
            elif Company == '1564':
                choices = 'Typeform'
            elif Company == '1565':
                choices = 'Whispir'
            elif Company == '1566':
                choices = 'Sema4'
            elif Company == '1567':
                choices = 'iFit'
            elif Company == '1568':
                choices = 'Ribbon'
            elif Company == '1569':
                choices = 'Intercom'
            elif Company == '1570':
                choices = 'Science 37 '
            elif Company == '1571':
                choices = 'Cardlytics'
            elif Company == '1572':
                choices = 'Cloudinary'
            elif Company == '1573':
                choices = 'Nestcoin'
            elif Company == '1574':
                choices = 'Tricida'
            elif Company == '1575':
                choices = 'Forto'
            elif Company == '1576':
                choices = 'Chipax'
            elif Company == '1577':
                choices = 'Juniper'
            elif Company == '1578':
                choices = 'Offerpad'
            elif Company == '1579':
                choices = 'Juul'
            elif Company == '1580':
                choices = 'InfluxData'
            elif Company == '1581':
                choices = 'Wistia'
            elif Company == '1582':
                choices = 'Ocavu'
            elif Company == '1583':
                choices = 'Avast'
            elif Company == '1584':
                choices = 'SendCloud'
            elif Company == '1585':
                choices = 'Voly'
            elif Company == '1586':
                choices = 'Wavely'
            elif Company == '1587':
                choices = 'ZenBusiness'
            elif Company == '1588':
                choices = 'Root Insurance'
            elif Company == '1589':
                choices = 'Liftoff'
            elif Company == '1590':
                choices = 'Plum'
            elif Company == '1591':
                choices = 'HighRadius'
            elif Company == '1592':
                choices = 'Amobee'
            elif Company == '1593':
                choices = 'CloudFactory'
            elif Company == '1594':
                choices = 'Coursera'
            elif Company == '1595':
                choices = 'Faze Medicines'
            elif Company == '1596':
                choices = 'EverBridge'
            elif Company == '1597':
                choices = 'Repertoire Immune Medicines'
            elif Company == '1598':
                choices = 'Beat'
            elif Company == '1599':
                choices = 'NanoString'
            elif Company == '1600':
                choices = 'SADA'
            elif Company == '1601':
                choices = 'Dock'
            elif Company == '1602':
                choices = 'Domino Data Lab'
            elif Company == '1603':
                choices = 'Varonis'
            elif Company == '1604':
                choices = 'Practically'
            elif Company == '1605':
                choices = 'Planetly'
            elif Company == '1606':
                choices = 'KoinWorks'
            elif Company == '1607':
                choices = 'Exodus'
            elif Company == '1608':
                choices = 'Benitago Group'
            elif Company == '1609':
                choices = 'Mythical Games'
            elif Company == '1610':
                choices = 'Pleo'
            elif Company == '1611':
                choices = 'Shippo'
            elif Company == '1612':
                choices = 'LiveRamp'
            elif Company == '1613':
                choices = 'Provi'
            elif Company == '1614':
                choices = 'Rubius'
            elif Company == '1615':
                choices = 'Snapdocs'
            elif Company == '1616':
                choices = 'Studio'
            elif Company == '1617':
                choices = 'Chime'
            elif Company == '1618':
                choices = 'Checkmarx'
            elif Company == '1619':
                choices = 'Smava'
            elif Company == '1620':
                choices = 'Iron Ox'
            elif Company == '1621':
                choices = 'Digital Currency Gruop'
            elif Company == '1622':
                choices = 'BitMEX'
            elif Company == '1623':
                choices = 'Signicat'
            elif Company == '1624':
                choices = 'Argo AI'
            elif Company == '1625':
                choices = 'Booking.com'
            elif Company == '1626':
                choices = 'Oda'
            elif Company == '1627':
                choices = 'Drop'
            elif Company == '1628':
                choices = 'Tapps Games'
            elif Company == '1629':
                choices = 'Help Scout'
            elif Company == '1630':
                choices = 'Kry'
            elif Company == '1631':
                choices = 'Notarize'
            elif Company == '1632':
                choices = 'EquityZen'
            elif Company == '1633':
                choices = 'Doubtnut'
            elif Company == '1634':
                choices = 'Fifth Season'
            elif Company == '1635':
                choices = 'Advata'
            elif Company == '1636':
                choices = 'Springlane'
            elif Company == '1637':
                choices = 'Recharge'
            elif Company == '1638':
                choices = 'GoNuts'
            elif Company == '1639':
                choices = 'Spreetail'
            elif Company == '1640':
                choices = 'MindBody'
            elif Company == '1641':
                choices = 'GoFundMe'
            elif Company == '1642':
                choices = 'Carbon'
            elif Company == '1643':
                choices = 'Fundbox'
            elif Company == '1644':
                choices = 'Embroker'
            elif Company == '1645':
                choices = 'Vee'
            elif Company == '1646':
                choices = 'Callisto Media'
            elif Company == '1647':
                choices = 'OrCam'
            elif Company == '1648':
                choices = 'Antidote Health'
            elif Company == '1649':
                choices = 'Elinvar'
            elif Company == '1650':
                choices = 'Synapsica'
            elif Company == '1651':
                choices = 'Volta'
            elif Company == '1652':
                choices = 'Hotmart'
            elif Company == '1653':
                choices = 'Loom'
            elif Company == '1654':
                choices = 'Sales Boomerang'
            elif Company == '1655':
                choices = 'AtoB'
            elif Company == '1656':
                choices = 'InfoSum'
            elif Company == '1657':
                choices = 'Clever Real Estate'
            elif Company == '1658':
                choices = 'Collibra'
            elif Company == '1659':
                choices = 'Side'
            elif Company == '1660':
                choices = 'Ada Health'
            elif Company == '1661':
                choices = 'Tiendanube'
            elif Company == '1662':
                choices = 'Nuri'
            elif Company == '1663':
                choices = 'Flipboard'
            elif Company == '1664':
                choices = 'Huawei'
            elif Company == '1665':
                choices = 'Flux Systems'
            elif Company == '1666':
                choices = 'Qin1'
            elif Company == '1667':
                choices = 'Playdots'
            elif Company == '1668':
                choices = 'ExtraHop'
            elif Company == '1669':
                choices = '6sense'
            elif Company == '1670':
                choices = 'Sinch'
            elif Company == '1671':
                choices = 'MX'
            elif Company == '1672':
                choices = 'Pacaso'
            elif Company == '1673':
                choices = 'Sketch'
            elif Company == '1674':
                choices = 'Udacity'
            elif Company == '1675':
                choices = 'Linkfire'
            elif Company == '1676':
                choices = 'Emitwise'
            elif Company == '1677':
                choices = 'GSR'
            elif Company == '1678':
                choices = 'VanHack'
            elif Company == '1679':
                choices = 'HelloFresh'
            elif Company == '1680':
                choices = 'Pavilion Data'
            elif Company == '1681':
                choices = 'Nyriad'
            elif Company == '1682':
                choices = 'Collage.com'
            elif Company == '1683':
                choices = 'BioMarin'
            elif Company == '1684':
                choices = 'Rev.com'
            elif Company == '1685':
                choices = 'Impossible Foods'
            elif Company == '1686':
                choices = 'Atome'
            elif Company == '1687':
                choices = 'First AML'
            elif Company == '1688':
                choices = 'Foresight Insurance'
            elif Company == '1689':
                choices = 'Built In'
            elif Company == '1690':
                choices = 'TwinStrand'
            elif Company == '1691':
                choices = 'Fivetran'
            elif Company == '1692':
                choices = 'ActiveCampaign'
            elif Company == '1693':
                choices = 'Tempo'
            elif Company == '1694':
                choices = 'WazirX'
            elif Company == '1695':
                choices = 'Spin'
            elif Company == '1696':
                choices = 'Carsome'
            elif Company == '1697':
                choices = 'Pastel'
            elif Company == '1698':
                choices = 'Truepill'
            elif Company == '1699':
                choices = 'Westwing'
            elif Company == '1700':
                choices = 'Zenjob'
            elif Company == '1701':
                choices = 'Front'
            elif Company == '1702':
                choices = 'Konfio'
            elif Company == '1703':
                choices = 'Foxtrot'
            elif Company == '1704':
                choices = 'Truiloo'
            elif Company == '1705':
                choices = 'Pesto'
            elif Company == '1706':
                choices = 'NYDIG'
            elif Company == '1707':
                choices = 'Klarna'
            elif Company == '1708':
                choices = 'Made.com'
            elif Company == '1709':
                choices = 'Kitty Hawk'
            elif Company == '1710':
                choices = 'Candidate Labs'
            elif Company == '1711':
                choices = 'Curative'
            elif Company == '1712':
                choices = '99'
            elif Company == '1713':
                choices = 'Ouster'
            elif Company == '1714':
                choices = 'Vesalius Therapeutics'
            elif Company == '1715':
                choices = 'Clear'
            elif Company == '1716':
                choices = 'TrueLayer'
            elif Company == '1717':
                choices = 'LivePerson'
            elif Company == '1718':
                choices = 'Acast'
            elif Company == '1719':
                choices = 'WorkRamp'
            elif Company == '1720':
                choices = 'NextRoll'
            elif Company == '1721':
                choices = 'Netflix'
            elif Company == '1722':
                choices = 'Bitrise'
            elif Company == '1723':
                choices = 'Taboola'
            elif Company == '1724':
                choices = 'Patreon'
            elif Company == '1725':
                choices = 'Propzy'
            elif Company == '1726':
                choices = 'Quicko'
            elif Company == '1727':
                choices = 'Mode Analytics'
            elif Company == '1728':
                choices = 'Compete'
            elif Company == '1729':
                choices = 'Karbon'
            elif Company == '1730':
                choices = 'Sama'
            elif Company == '1731':
                choices = 'SkipTheDishes'
            elif Company == '1732':
                choices = 'Brighte'
            elif Company == '1733':
                choices = 'Amber Group'
            elif Company == '1734':
                choices = 'Capiter'
            elif Company == '1735':
                choices = 'CommonBond'
            elif Company == '1736':
                choices = 'DreamBox Learning'
            elif Company == '1737':
                choices = 'Flowhub'
            elif Company == '1738':
                choices = 'Lido Learning'
            elif Company == '1739':
                choices = 'Pomelo Fashion'
            elif Company == '1740':
                choices = 'Genome Medical'
            elif Company == '1741':
                choices = 'BigBear.ai'
            elif Company == '1742':
                choices = 'Realtor.com'
            elif Company == '1743':
                choices = 'Simple Feast'
            elif Company == '1744':
                choices = 'Rupeek'
            elif Company == '1745':
                choices = 'Demandbase'
            elif Company == '1746':
                choices = 'Firebolt'
            elif Company == '1747':
                choices = 'Xsight Labs'
            elif Company == '1748':
                choices = 'Brave Care'
            elif Company == '1749':
                choices = 'Lawgeex'
            elif Company == '1750':
                choices = 'Juniper Square'
            elif Company == '1751':
                choices = 'Medium'
            elif Company == '1752':
                choices = 'Kuda'
            elif Company == '1753':
                choices = 'Sea'
            elif Company == '1754':
                choices = '2TM'
            elif Company == '1755':
                choices = 'Urban Sports Club'
            elif Company == '1756':
                choices = 'Hedvig'
            elif Company == '1757':
                choices = 'GoodRx'
            elif Company == '1758':
                choices = 'Apartment List'
            elif Company == '1759':
                choices = 'Artnight'
            elif Company == '1760':
                choices = 'Snagajob'
            elif Company == '1761':
                choices = 'The Wing'
            elif Company == '1762':
                choices = 'Viamo'
            elif Company == '1763':
                choices = 'Immersive Labs'
            elif Company == '1764':
                choices = '54gene'
            elif Company == '1765':
                choices = 'Fungible'
            elif Company == '1766':
                choices = 'Skillz'
            elif Company == '1767':
                choices = 'Argyle'
            elif Company == '1768':
                choices = 'Loja Integrada'
            elif Company == '1769':
                choices = 'ShipBob'
            elif Company == '1770':
                choices = 'Reali'
            elif Company == '1771':
                choices = 'Pix'
            elif Company == '1772':
                choices = 'Packable'
            elif Company == '1773':
                choices = 'Q4'
            elif Company == '1774':
                choices = 'Skedulo'
            elif Company == '1775':
                choices = 'Plato'
            elif Company == '1776':
                choices = 'DataRobot'
            elif Company == '1777':
                choices = 'Kogan'
            elif Company == '1778':
                choices = 'Skillshare'
            elif Company == '1779':
                choices = 'Mr. Yum'
            elif Company == '1780':
                choices = 'ShopX'
            elif Company == '1781':
                choices = 'NSO'
            elif Company == '1782':
                choices = 'Tufin'
            elif Company == '1783':
                choices = 'Hodlnaut'
            elif Company == '1784':
                choices = 'Thirty Madison'
            elif Company == '1785':
                choices = 'Fluke'
            elif Company == '1786':
                choices = 'Warren'
            elif Company == '1787':
                choices = 'AlayaCare'
            elif Company == '1788':
                choices = 'Pliops'
            elif Company == '1789':
                choices = 'Woven'
            elif Company == '1790':
                choices = 'Edmodo'
            elif Company == '1791':
                choices = 'Updater'
            elif Company == '1792':
                choices = 'ContraFect'
            elif Company == '1793':
                choices = 'ThredUp'
            elif Company == '1794':
                choices = 'Anywell'
            elif Company == '1795':
                choices = 'Almanac'
            elif Company == '1796':
                choices = 'Core Scientific'
            elif Company == '1797':
                choices = 'Orbit'
            elif Company == '1798':
                choices = 'Calm'
            elif Company == '1799':
                choices = 'Marketforce'
            elif Company == '1800':
                choices = 'Expert360'
            elif Company == '1801':
                choices = 'Guidewire'
            elif Company == '1802':
                choices = 'Pollen'
            elif Company == '1803':
                choices = 'Vedanta Biosciences'
            elif Company == '1804':
                choices = 'GoHealth'
            elif Company == '1805':
                choices = 'Nutanix'
            elif Company == '1806':
                choices = 'Quanterix'
            elif Company == '1807':
                choices = 'MadeiraMadeira'
            elif Company == '1808':
                choices = 'Shogun'
            elif Company == '1809':
                choices = 'Dooly'
            elif Company == '1810':
                choices = 'Berkeley Lights'
            elif Company == '1811':
                choices = 'DailyPay'
            elif Company == '1812':
                choices = 'Haus'
            elif Company == '1813':
                choices = 'Sweetgreen'
            elif Company == '1814':
                choices = 'Warby Parker'
            elif Company == '1815':
                choices = 'Labelbox'
            elif Company == '1816':
                choices = 'Perion'
            elif Company == '1817':
                choices = 'Daily Harvest'
            elif Company == '1818':
                choices = 'Mejuri'
            elif Company == '1819':
                choices = 'Uberflip'
            elif Company == '1820':
                choices = 'Article'
            elif Company == '1821':
                choices = 'Jam City'
            elif Company == '1822':
                choices = '10X Genomics'
            elif Company == '1823':
                choices = 'On Deck'
            elif Company == '1824':
                choices = 'Nomad'
            elif Company == '1825':
                choices = 'StubHub'
            elif Company == '1826':
                choices = 'Zenius'
            elif Company == '1827':
                choices = 'Healthcare.com'
            elif Company == '1828':
                choices = 'Unbounce'
            elif Company == '1829':
                choices = 'The Org'
            elif Company == '1830':
                choices = 'CarDekho'
            elif Company == '1831':
                choices = 'Puppet'
            elif Company == '1832':
                choices = 'Talkwalker'
            elif Company == '1833':
                choices = 'Seegrid'
            elif Company == '1834':
                choices = 'Nylas'
            elif Company == '1835':
                choices = 'The Predictive Index'
            elif Company == '1836':
                choices = 'Stedi'
            elif Company == '1837':
                choices = 'Glossier'
            elif Company == '1838':
                choices = 'FuboTV'
            elif Company == '1839':
                choices = 'Hash'
            elif Company == '1840':
                choices = 'Classkick'
            elif Company == '1841':
                choices = 'OnlyFans'
            elif Company == '1842':
                choices = 'Perceptive Automata'
            elif Company == '1843':
                choices = 'Whereby'
            elif Company == '1844':
                choices = 'Metigy'
            elif Company == '1845':
                choices = 'Gatherly'
            elif Company == '1846':
                choices = 'Clearco'
            elif Company == '1847':
                choices = 'Imperfect Foods'
            elif Company == '1848':
                choices = 'Shelf Engine'
            elif Company == '1849':
                choices = 'Quantcast'
            elif Company == '1850':
                choices = 'Sherpa'
            elif Company == '1851':
                choices = 'CoinFLEX'
            elif Company == '1852':
                choices = 'MissFresh'
            elif Company == '1853':
                choices = 'Yabonza'
            elif Company == '1854':
                choices = 'Metromile'
            elif Company == '1855':
                choices = 'Allbirds'
            elif Company == '1856':
                choices = 'TextNow'
            elif Company == '1857':
                choices = 'Bikayi'
            elif Company == '1858':
                choices = 'Brainbase'
            elif Company == '1859':
                choices = 'Change.org'
            elif Company == '1860':
                choices = 'Tapas Media'
            elif Company == '1861':
                choices = 'Turntide'
            elif Company == '1862':
                choices = 'Coinsquare'
            elif Company == '1863':
                choices = 'Skai'
            elif Company == '1864':
                choices = 'Fiverr'
            elif Company == '1865':
                choices = 'InDebted'
            elif Company == '1866':
                choices = 'Dover'
            elif Company == '1867':
                choices = 'Pear Therapeutics '
            elif Company == '1868':
                choices = ' Included Health'
            elif Company == '1869':
                choices = 'Soluto'
            elif Company == '1870':
                choices = 'Eucalyptus'
            elif Company == '1871':
                choices = 'Workstream'
            elif Company == '1872':
                choices = 'Clarify Health'
            elif Company == '1873':
                choices = 'Arete'
            elif Company == '1874':
                choices = 'Boosted Commerce'
            elif Company == '1875':
                choices = 'Owlet'
            elif Company == '1876':
                choices = 'People.ai'
            elif Company == '1877':
                choices = 'Wizeline'
            elif Company == '1878':
                choices = 'AppGate'
            elif Company == '1879':
                choices = 'Rad Power Bikes'
            elif Company == '1880':
                choices = 'Lunchbox'
            elif Company == '1881':
                choices = 'RealSelf'
            elif Company == '1882':
                choices = 'Catalyst'
            elif Company == '1883':
                choices = 'Smarsh'
            elif Company == '1884':
                choices = 'Just Eat Takeaway'
            elif Company == '1885':
                choices = 'BlueStacks'
            elif Company == '1886':
                choices = 'Introhive'
            elif Company == '1887':
                choices = 'Zencity'
            elif Company == '1888':
                choices = 'Splice'
            elif Company == '1889':
                choices = 'Forma.ai'
            elif Company == '1890':
                choices = 'Arc'
            elif Company == '1891':
                choices = 'M1'
            elif Company == '1892':
                choices = 'SellerX'
            elif Company == '1893':
                choices = 'Stint'
            elif Company == '1894':
                choices = 'Capsule'
            elif Company == '1895':
                choices = 'PACT Pharma'
            elif Company == '1896':
                choices = 'Lusha'
            elif Company == '1897':
                choices = 'Bright Money'
            elif Company == '1898':
                choices = 'Heroes'
            elif Company == '1899':
                choices = 'Aspire'
            elif Company == '1900':
                choices = 'Zego'
            elif Company == '1901':
                choices = 'The Mom Project'
            elif Company == '1902':
                choices = 'Unstoppable Domains'
            elif Company == '1903':
                choices = 'Kiavi'
            elif Company == '1904':
                choices = 'Alto Pharmacy'
            elif Company == '1905':
                choices = 'Cosuno'
            elif Company == '1906':
                choices = 'Wave'
            elif Company == '1907':
                choices = 'Tonal'
            elif Company == '1908':
                choices = 'Bryter'
            elif Company == '1909':
                choices = 'Involves'
            elif Company == '1910':
                choices = 'CircleUp'
            elif Company == '1911':
                choices = 'Papa'
            elif Company == '1912':
                choices = 'Fraazo'
            elif Company == '1913':
                choices = 'Babylon'
            elif Company == '1914':
                choices = 'Airlift'
            elif Company == '1915':
                choices = 'Spring'
            elif Company == '1916':
                choices = 'SundaySky'
            elif Company == '1917':
                choices = 'Apeel Sciences'
            elif Company == '1918':
                choices = 'Forward'
            elif Company == '1919':
                choices = 'Ignite'
            elif Company == '1920':
                choices = 'PuduTech'
            elif Company == '1921':
                choices = 'Butler Hospitality'
            elif Company == '1922':
                choices = 'Next Insurance'
            elif Company == '1923':
                choices = 'Adwerx'
            elif Company == '1924':
                choices = 'Emotive'
            elif Company == '1925':
                choices = 'Cedar'
            elif Company == '1926':
                choices = 'Remote'
            elif Company == '1927':
                choices = 'Anodot'
            elif Company == '1928':
                choices = 'SQream'
            elif Company == '1929':
                choices = 'Motif Foodworks'
            elif Company == '1930':
                choices = 'eToro'
            elif Company == '1931':
                choices = 'Bullish'
            elif Company == '1932':
                choices = 'Transmit Security'
            elif Company == '1933':
                choices = 'Thimble'
            elif Company == '1934':
                choices = 'Syte'
            elif Company == '1935':
                choices = 'Lightricks'
            elif Company == '1936':
                choices = 'Chessable'
            elif Company == '1937':
                choices = 'Sendle'
            elif Company == '1938':
                choices = 'Gorillas'
            elif Company == '1939':
                choices = 'Celsius'
            elif Company == '1940':
                choices = 'LetsGetChecked'
            elif Company == '1941':
                choices = 'Perx Health'
            elif Company == '1942':
                choices = 'Zepto'
            elif Company == '1943':
                choices = 'WanderJaunt'
            elif Company == '1944':
                choices = 'Canoo'
            elif Company == '1945':
                choices = 'Bamboo Health'
            elif Company == '1946':
                choices = 'Teleport'
            elif Company == '1947':
                choices = 'Remesh'
            elif Company == '1948':
                choices = 'Enjoy'
            elif Company == '1949':
                choices = 'Crejo.Fun'
            elif Company == '1950':
                choices = 'Stash Financial'
            elif Company == '1951':
                choices = 'Stream'
            elif Company == '1952':
                choices = 'Finleap Connect'
            elif Company == '1953':
                choices = 'Abra'
            elif Company == '1954':
                choices = 'Gavelytics'
            elif Company == '1955':
                choices = 'Secfi'
            elif Company == '1956':
                choices = 'Sundae'
            elif Company == '1957':
                choices = 'Toppr'
            elif Company == '1958':
                choices = 'Qumulo'
            elif Company == '1959':
                choices = 'Parallel Wireless'
            elif Company == '1960':
                choices = 'Oye Rickshaw'
            elif Company == '1961':
                choices = 'Rows'
            elif Company == '1962':
                choices = 'Baton'
            elif Company == '1963':
                choices = 'Substack'
            elif Company == '1964':
                choices = 'CommentSold'
            elif Company == '1965':
                choices = 'HomeLight'
            elif Company == '1966':
                choices = 'Modsy'
            elif Company == '1967':
                choices = 'Volt Bank'
            elif Company == '1968':
                choices = 'WhiteHat Jr'
            elif Company == '1969':
                choices = 'StockX'
            elif Company == '1970':
                choices = 'Sidecar Health'
            elif Company == '1971':
                choices = 'Vezeeta'
            elif Company == '1972':
                choices = 'Bright Machines'
            elif Company == '1973':
                choices = 'HealthMatch'
            elif Company == '1974':
                choices = 'Nova Benefits'
            elif Company == '1975':
                choices = 'Una Brands'
            elif Company == '1976':
                choices = 'AppLovin'
            elif Company == '1977':
                choices = 'Banxa'
            elif Company == '1978':
                choices = 'SafeGraph'
            elif Company == '1979':
                choices = 'Postscript'
            elif Company == '1980':
                choices = 'Bitpanda'
            elif Company == '1981':
                choices = 'Sunday'
            elif Company == '1982':
                choices = 'Bestow'
            elif Company == '1983':
                choices = 'Feather'
            elif Company == '1984':
                choices = 'Give Legacy'
            elif Company == '1985':
                choices = 'Aura'
            elif Company == '1986':
                choices = 'Pipl'
            elif Company == '1987':
                choices = 'Vouch'
            elif Company == '1988':
                choices = 'Voyage SMS'
            elif Company == '1989':
                choices = 'Kune'
            elif Company == '1990':
                choices = 'Mark43'
            elif Company == '1991':
                choices = 'Ro'
            elif Company == '1992':
                choices = 'Bungalow'
            elif Company == '1993':
                choices = 'Mindgeek'
            elif Company == '1994':
                choices = 'Ebanx'
            elif Company == '1995':
                choices = 'Community'
            elif Company == '1996':
                choices = 'Sourcegraph'
            elif Company == '1997':
                choices = 'Frubana'
            elif Company == '1998':
                choices = 'SuperLearn'
            elif Company == '1999':
                choices = 'Tray.io'
            elif Company == '2000':
                choices = 'SummerBio'
            elif Company == '2001':
                choices = 'Aqgromalin'
            elif Company == '2002':
                choices = 'Bonsai'
            elif Company == '2003':
                choices = 'BitOasis'
            elif Company == '2004':
                choices = 'Finite State'
            elif Company == '2005':
                choices = 'JOKR'
            elif Company == '2006':
                choices = 'Zumper'
            elif Company == '2007':
                choices = 'Circulo Health'
            elif Company == '2008':
                choices = 'Swappie'
            elif Company == '2009':
                choices = 'Wealthsimple'
            elif Company == '2010':
                choices = 'Weee!'
            elif Company == '2011':
                choices = 'Elementor'
            elif Company == '2012':
                choices = 'Tonkean'
            elif Company == '2013':
                choices = 'Airtame'
            elif Company == '2014':
                choices = 'OpenWeb'
            elif Company == '2015':
                choices = 'Swyft'
            elif Company == '2016':
                choices = 'Crehana'
            elif Company == '2017':
                choices = 'JetClosing'
            elif Company == '2018':
                choices = 'Sami'
            elif Company == '2019':
                choices = 'Breathe'
            elif Company == '2020':
                choices = 'Hunty'
            elif Company == '2021':
                choices = 'TIFIN'
            elif Company == '2022':
                choices = 'Addi'
            elif Company == '2023':
                choices = 'Wave Sports and Entertainment'
            elif Company == '2024':
                choices = 'Automox'
            elif Company == '2025':
                choices = 'Berlin Brands Group'
            elif Company == '2026':
                choices = 'Sanar'
            elif Company == '2027':
                choices = 'Freetrade'
            elif Company == '2028':
                choices = 'Albert'
            elif Company == '2029':
                choices = 'Keepe'
            elif Company == '2030':
                choices = 'Liongard'
            elif Company == '2031':
                choices = 'Ziroom'
            elif Company == '2032':
                choices = 'OneTrust'
            elif Company == '2033':
                choices = 'Daniel Wellington'
            elif Company == '2034':
                choices = 'Boozt'
            elif Company == '2035':
                choices = 'The Grommet'
            elif Company == '2036':
                choices = 'Stashaway'
            elif Company == '2037':
                choices = 'Preply'
            elif Company == '2038':
                choices = 'Starship'
            elif Company == '2039':
                choices = 'Trade Republic'
            elif Company == '2040':
                choices = 'iPrice Group'
            elif Company == '2041':
                choices = 'Memmo'
            elif Company == '2042':
                choices = 'Lummo'
            elif Company == '2043':
                choices = 'ID.me'
            elif Company == '2044':
                choices = 'KiwiCo'
            elif Company == '2045':
                choices = 'Bond'
            elif Company == '2046':
                choices = 'CyberCube'
            elif Company == '2047':
                choices = 'Dutchie'
            elif Company == '2048':
                choices = 'Deep Instinct'
            elif Company == '2049':
                choices = 'Eruditus'
            elif Company == '2050':
                choices = 'Afterverse'
            elif Company == '2051':
                choices = 'Superhuman'
            elif Company == '2052':
                choices = 'Food52'
            elif Company == '2053':
                choices = '5B Solar'
            elif Company == '2054':
                choices = 'Favo'
            elif Company == '2055':
                choices = 'PolicyGenius'
            elif Company == '2056':
                choices = 'Yojak'
            elif Company == '2057':
                choices = 'Envato'
            elif Company == '2058':
                choices = 'Stord'
            elif Company == '2059':
                choices = 'Gather'
            elif Company == '2060':
                choices = 'Shef'
            elif Company == '2061':
                choices = 'Esme Learning'
            elif Company == '2062':
                choices = 'Kaodim'
            elif Company == '2063':
                choices = 'Rain'
            elif Company == '2064':
                choices = 'Udayy'
            elif Company == '2065':
                choices = 'Curve'
            elif Company == '2066':
                choices = 'Impala'
            elif Company == '2067':
                choices = 'Eaze'
            elif Company == '2068':
                choices = 'Truck It In'
            elif Company == '2069':
                choices = 'Replicated'
            elif Company == '2070':
                choices = 'Tomo'
            elif Company == '2071':
                choices = 'Getta'
            elif Company == '2072':
                choices = 'BookClub'
            elif Company == '2073':
                choices = 'Mobile Premier League'
            elif Company == '2074':
                choices = 'SumUp'
            elif Company == '2075':
                choices = 'Tempus Ex'
            elif Company == '2076':
                choices = 'Daloopa'
            elif Company == '2077':
                choices = 'Uncapped'
            elif Company == '2078':
                choices = 'Akerna'
            elif Company == '2079':
                choices = 'Terminus'
            elif Company == '2080':
                choices = 'VTEX'
            elif Company == '2081':
                choices = 'Dazn'
            elif Company == '2082':
                choices = 'Lacework'
            elif Company == '2083':
                choices = 'Kontist'
            elif Company == '2084':
                choices = 'Coterie Insurance'
            elif Company == '2085':
                choices = 'Zapp'
            elif Company == '2086':
                choices = 'Buenbit'
            elif Company == '2087':
                choices = 'BeyondMinds'
            elif Company == '2088':
                choices = 'Airtime'
            elif Company == '2089':
                choices = 'MFine'
            elif Company == '2090':
                choices = 'Picsart'
            elif Company == '2091':
                choices = 'Zak'
            elif Company == '2092':
                choices = 'AliExpress Russia'
            elif Company == '2093':
                choices = 'Subspace'
            elif Company == '2094':
                choices = 'Section4'
            elif Company == '2095':
                choices = 'Tripwire'
            elif Company == '2096':
                choices = 'Meero'
            elif Company == '2097':
                choices = 'Reef'
            elif Company == '2098':
                choices = 'divvyDOSE'
            elif Company == '2099':
                choices = 'Progrexion'
            elif Company == '2100':
                choices = 'SEND'
            elif Company == '2101':
                choices = 'Colossus'
            elif Company == '2102':
                choices = 'Mainstreet'
            elif Company == '2103':
                choices = 'Ideoclick'
            elif Company == '2104':
                choices = 'Vise'
            elif Company == '2105':
                choices = 'Bizpay'
            elif Company == '2106':
                choices = 'Thrasio'
            elif Company == '2107':
                choices = 'Avo'
            elif Company == '2108':
                choices = 'Wahoo Fitness'
            elif Company == '2109':
                choices = 'Sigfox'
            elif Company == '2110':
                choices = 'Clyde'
            elif Company == '2111':
                choices = 'Xiaohongshu'
            elif Company == '2112':
                choices = 'Facily'
            elif Company == '2113':
                choices = 'QuintoAndar'
            elif Company == '2114':
                choices = 'Humble'
            elif Company == '2115':
                choices = 'Halcyon Health'
            elif Company == '2116':
                choices = 'Ahead'
            elif Company == '2117':
                choices = 'Goodfood'
            elif Company == '2118':
                choices = 'Workrise'
            elif Company == '2119':
                choices = 'Fast'
            elif Company == '2120':
                choices = 'Legible'
            elif Company == '2121':
                choices = 'Rasa'
            elif Company == '2122':
                choices = 'Furlenco'
            elif Company == '2123':
                choices = 'Grove Collaborative'
            elif Company == '2124':
                choices = 'Curology'
            elif Company == '2125':
                choices = 'Trell'
            elif Company == '2126':
                choices = 'Knock'
            elif Company == '2127':
                choices = 'Talis Biomedical'
            elif Company == '2128':
                choices = 'Sezzle'
            elif Company == '2129':
                choices = 'Adaptive Biotechnologies'
            elif Company == '2130':
                choices = 'Hyperscience'
            elif Company == '2131':
                choices = 'WeDoctor'
            elif Company == '2132':
                choices = 'OKCredit'
            elif Company == '2133':
                choices = 'Lido'
            elif Company == '2134':
                choices = 'Virgin Hyperloop'
            elif Company == '2135':
                choices = 'Trustly'
            elif Company == '2136':
                choices = 'Liv Up'
            elif Company == '2137':
                choices = 'Defined.ai'
            elif Company == '2138':
                choices = 'Rhino'
            elif Company == '2139':
                choices = 'Protonn'
            elif Company == '2140':
                choices = 'BitTitan'
            elif Company == '2141':
                choices = 'Ozy Media'
            elif Company == '2142':
                choices = 'Genius'
            elif Company == '2143':
                choices = 'Treehouse'
            elif Company == '2144':
                choices = 'Casper'
            elif Company == '2145':
                choices = 'Tanium'
            elif Company == '2146':
                choices = 'Flockjay'
            elif Company == '2147':
                choices = 'Pagarbook'
            elif Company == '2148':
                choices = 'Katerra'
            elif Company == '2149':
                choices = 'Lambda School'
            elif Company == '2150':
                choices = 'Madefire'
            elif Company == '2151':
                choices = 'HuffPo'
            elif Company == '2152':
                choices = 'Clumio'
            elif Company == '2153':
                choices = 'DJI'
            elif Company == '2154':
                choices = 'Ninjacart'
            elif Company == '2155':
                choices = 'Limelight'
            elif Company == '2156':
                choices = 'Quandoo'
            elif Company == '2157':
                choices = 'Hubba'
            elif Company == '2158':
                choices = 'Privitar'
            elif Company == '2159':
                choices = 'Postmates'
            elif Company == '2160':
                choices = 'Pocketmath'
            elif Company == '2161':
                choices = 'Aura Financial'
            elif Company == '2162':
                choices = 'Simple'
            elif Company == '2163':
                choices = 'Pulse Secure'
            elif Company == '2164':
                choices = 'Breather'
            elif Company == '2165':
                choices = 'Actifio'
            elif Company == '2166':
                choices = 'Zinier'
            elif Company == '2167':
                choices = 'Aya'
            elif Company == '2168':
                choices = 'Domio'
            elif Company == '2169':
                choices = 'Bridge Connector'
            elif Company == '2170':
                choices = 'Tidepool'
            elif Company == '2171':
                choices = 'Igenous'
            elif Company == '2172':
                choices = 'Scoop'
            elif Company == '2173':
                choices = 'Worksmith'
            elif Company == '2174':
                choices = 'Rubica'
            elif Company == '2175':
                choices = 'Bossa Nova'
            elif Company == '2176':
                choices = 'Remedy'
            elif Company == '2177':
                choices = 'Knotel'
            elif Company == '2178':
                choices = 'Cheetah'
            elif Company == '2179':
                choices = 'CodeCombat'
            elif Company == '2180':
                choices = 'Quibi'
            elif Company == '2181':
                choices = 'GetYourGuide'
            elif Company == '2182':
                choices = 'OLX India'
            elif Company == '2183':
                choices = 'Chef'
            elif Company == '2184':
                choices = 'TheWrap'
            elif Company == '2185':
                choices = 'HumanForest'
            elif Company == '2186':
                choices = 'Air'
            elif Company == '2187':
                choices = 'NS8'
            elif Company == '2188':
                choices = 'Bleacher Report'
            elif Company == '2189':
                choices = 'HubHaus'
            elif Company == '2190':
                choices = 'Swing Education'
            elif Company == '2191':
                choices = 'Awok'
            elif Company == '2192':
                choices = 'Big Fish Games'
            elif Company == '2193':
                choices = 'GoBear'
            elif Company == '2194':
                choices = 'MakeMyTrip'
            elif Company == '2195':
                choices = 'kununu'
            elif Company == '2196':
                choices = 'Superloop'
            elif Company == '2197':
                choices = 'Spaces'
            elif Company == '2198':
                choices = 'StreamSets'
            elif Company == '2199':
                choices = 'Docly'
            elif Company == '2200':
                choices = 'Mapify'
            elif Company == '2201':
                choices = 'Lumina Networks'
            elif Company == '2202':
                choices = 'HopSkipDrive'
            elif Company == '2203':
                choices = 'Eatsy'
            elif Company == '2204':
                choices = 'The Appraisal Lane'
            elif Company == '2205':
                choices = 'Thriver'
            elif Company == '2206':
                choices = 'Vesta'
            elif Company == '2207':
                choices = 'Buy.com / Rakuten'
            elif Company == '2208':
                choices = 'tZero'
            elif Company == '2209':
                choices = 'Pared'
            elif Company == '2210':
                choices = 'Zeitgold'
            elif Company == '2211':
                choices = 'Perkbox'
            elif Company == '2212':
                choices = 'Sorabel'
            elif Company == '2213':
                choices = 'Lighter Capital'
            elif Company == '2214':
                choices = 'Curefit'
            elif Company == '2215':
                choices = 'Snaptravel'
            elif Company == '2216':
                choices = 'Optimizely'
            elif Company == '2217':
                choices = 'Skyscanner'
            elif Company == '2218':
                choices = 'Yelp'
            elif Company == '2219':
                choices = 'Zilingo'
            elif Company == '2220':
                choices = 'PaySense'
            elif Company == '2221':
                choices = 'Funding Circle'
            elif Company == '2222':
                choices = 'OnDeck'
            elif Company == '2223':
                choices = 'Sharethrough'
            elif Company == '2224':
                choices = 'Kongregate'
            elif Company == '2225':
                choices = 'Havenly'
            elif Company == '2226':
                choices = 'G2'
            elif Company == '2227':
                choices = 'Hired'
            elif Company == '2228':
                choices = 'Engine eCommerce'
            elif Company == '2229':
                choices = 'Byton'
            elif Company == '2230':
                choices = 'Gojek'
            elif Company == '2231':
                choices = 'ScaleFactor'
            elif Company == '2232':
                choices = 'Dark'
            elif Company == '2233':
                choices = 'Intuit'
            elif Company == '2234':
                choices = 'WeWork'
            elif Company == '2235':
                choices = 'Atlas Obscura '
            elif Company == '2236':
                choices = 'Navi'
            elif Company == '2237':
                choices = 'PaisaBazaar'
            elif Company == '2238':
                choices = 'Redox'
            elif Company == '2239':
                choices = 'Conga'
            elif Company == '2240':
                choices = 'Stockwell AI'
            elif Company == '2241':
                choices = 'SynapseFI'
            elif Company == '2242':
                choices = 'ScaleFocus'
            elif Company == '2243':
                choices = 'Her Campus Media'
            elif Company == '2244':
                choices = 'Integrate.ai'
            elif Company == '2245':
                choices = 'The Athletic'
            elif Company == '2246':
                choices = 'Lastline'
            elif Company == '2247':
                choices = 'Builder'
            elif Company == '2248':
                choices = 'Outdoorsy'
            elif Company == '2249':
                choices = 'Monzo'
            elif Company == '2250':
                choices = 'SpotHero'
            elif Company == '2251':
                choices = 'Credit Sesame'
            elif Company == '2252':
                choices = 'Circ'
            elif Company == '2253':
                choices = 'Descartes Labs'
            elif Company == '2254':
                choices = 'MakerBot'
            elif Company == '2255':
                choices = 'CrowdStreet'
            elif Company == '2256':
                choices = 'Loftium'
            elif Company == '2257':
                choices = 'BookMyShow'
            elif Company == '2258':
                choices = 'The Sill'
            elif Company == '2259':
                choices = 'Instructure'
            elif Company == '2260':
                choices = 'Bluprint'
            elif Company == '2261':
                choices = 'Acorns'
            elif Company == '2262':
                choices = 'Teamwork'
            elif Company == '2263':
                choices = 'Cvent'
            elif Company == '2264':
                choices = 'PickYourTrail'
            elif Company == '2265':
                choices = 'Glitch'
            elif Company == '2266':
                choices = 'Kapten / Free Now'
            elif Company == '2267':
                choices = 'Samsara'
            elif Company == '2268':
                choices = 'Stay Alfred'
            elif Company == '2269':
                choices = 'Dotscience'
            elif Company == '2270':
                choices = 'Divvy'
            elif Company == '2271':
                choices = 'Agoda'
            elif Company == '2272':
                choices = 'Rubrik'
            elif Company == '2273':
                choices = 'Intapp'
            elif Company == '2274':
                choices = 'Datera'
            elif Company == '2275':
                choices = 'Magicbricks'
            elif Company == '2276':
                choices = 'Lendingkart'
            elif Company == '2277':
                choices = 'Masse'
            elif Company == '2278':
                choices = 'Quartz'
            elif Company == '2279':
                choices = 'Ridecell'
            elif Company == '2280':
                choices = 'Veem'
            elif Company == '2281':
                choices = 'Sift'
            elif Company == '2282':
                choices = 'TicketSwap'
            elif Company == '2283':
                choices = 'Workfront'
            elif Company == '2284':
                choices = 'Deliv'
            elif Company == '2285':
                choices = 'Mercos'
            elif Company == '2286':
                choices = 'Kickstarter'
            elif Company == '2287':
                choices = 'Intersect'
            elif Company == '2288':
                choices = 'BetterCloud'
            elif Company == '2289':
                choices = 'WeFit'
            elif Company == '2290':
                choices = 'Zymergen '
            elif Company == '2291':
                choices = 'Stone'
            elif Company == '2292':
                choices = 'Mixpanel'
            elif Company == '2293':
                choices = 'Hireology'
            elif Company == '2294':
                choices = 'Datto'
            elif Company == '2295':
                choices = 'Revolut'
            elif Company == '2296':
                choices = 'Cadre'
            elif Company == '2297':
                choices = 'Jump'
            elif Company == '2298':
                choices = 'Numbrs'
            elif Company == '2299':
                choices = 'Flywire'
            elif Company == '2300':
                choices = 'SalesLoft'
            elif Company == '2301':
                choices = 'Tally'
            elif Company == '2302':
                choices = 'Airy Rooms'
            elif Company == '2303':
                choices = 'Validity'
            elif Company == '2304':
                choices = 'Flatiron School'
            elif Company == '2305':
                choices = 'Rubicon Project'
            elif Company == '2306':
                choices = 'Segment'
            elif Company == '2307':
                choices = 'OPay'
            elif Company == '2308':
                choices = 'ThoughtSpot'
            elif Company == '2309':
                choices = 'Andela'
            elif Company == '2310':
                choices = 'Workable'
            elif Company == '2311':
                choices = 'Cloudera'
            elif Company == '2312':
                choices = 'Handshake'
            elif Company == '2313':
                choices = 'League'
            elif Company == '2314':
                choices = 'Careem'
            elif Company == '2315':
                choices = 'Oriente'
            elif Company == '2316':
                choices = 'Element AI'
            elif Company == '2317':
                choices = 'Deputy'
            elif Company == '2318':
                choices = 'Castlight Health'
            elif Company == '2319':
                choices = 'Trivago'
            elif Company == '2320':
                choices = 'LiveTiles'
            elif Company == '2321':
                choices = 'Namely'
            elif Company == '2322':
                choices = 'Culture Trip'
            elif Company == '2323':
                choices = 'Sandbox VR'
            elif Company == '2324':
                choices = 'Virtudent'
            elif Company == '2325':
                choices = 'Monese'
            elif Company == '2326':
                choices = 'Automatic'
            elif Company == '2327':
                choices = 'Flynote'
            elif Company == '2328':
                choices = 'Care.com'
            elif Company == '2329':
                choices = 'AirMap'
            elif Company == '2330':
                choices = 'PicoBrew'
            elif Company == '2331':
                choices = 'Lime'
            elif Company == '2332':
                choices = 'Transfix'
            elif Company == '2333':
                choices = 'Yoco'
            elif Company == '2334':
                choices = 'Renmoney'
            elif Company == '2335':
                choices = 'App Annie'
            elif Company == '2336':
                choices = 'OpenX'
            elif Company == '2337':
                choices = 'PayJoy'
            elif Company == '2338':
                choices = 'Shipsi'
            elif Company == '2339':
                choices = 'Migo'
            elif Company == '2340':
                choices = 'Automation Anywhere'
            elif Company == '2341':
                choices = 'Qwick'
            elif Company == '2342':
                choices = 'Stoqo'
            elif Company == '2343':
                choices = 'Submittable'
            elif Company == '2344':
                choices = 'Divergent 3D'
            elif Company == '2345':
                choices = 'Ada Support'
            elif Company == '2346':
                choices = 'UPshow'
            elif Company == '2347':
                choices = 'Horizn Studios'
            elif Company == '2348':
                choices = 'Welkin Health'
            elif Company == '2349':
                choices = 'Jiobit'
            elif Company == '2350':
                choices = 'TutorMundi'
            elif Company == '2351':
                choices = 'Cheddar'
            elif Company == '2352':
                choices = 'Zenefits'
            elif Company == '2353':
                choices = 'Oscar Health'
            elif Company == '2354':
                choices = 'Simon Data'
            elif Company == '2355':
                choices = 'PowerReviews'
            elif Company == '2356':
                choices = 'Singular'
            elif Company == '2357':
                choices = 'Magic Leap'
            elif Company == '2358':
                choices = 'When I Work'
            elif Company == '2359':
                choices = 'Ike'
            elif Company == '2360':
                choices = 'Freshbooks'
            elif Company == '2361':
                choices = 'Politico / Protocol'
            elif Company == '2362':
                choices = 'Bringg'
            elif Company == '2363':
                choices = 'Klook'
            elif Company == '2364':
                choices = 'GumGum'
            elif Company == '2365':
                choices = 'Kueski'
            elif Company == '2366':
                choices = 'Zum'
            elif Company == '2367':
                choices = 'Hipcamp'
            elif Company == '2368':
                choices = 'Motif Investing'
            elif Company == '2369':
                choices = 'BlackBuck'
            elif Company == '2370':
                choices = 'ContaAzul'
            elif Company == '2371':
                choices = 'Labster'
            elif Company == '2372':
                choices = 'Tor'
            elif Company == '2373':
                choices = 'BitGo'
            elif Company == '2374':
                choices = 'Dispatch'
            elif Company == '2375':
                choices = 'Influitive'
            elif Company == '2376':
                choices = 'CarGurus'
            elif Company == '2377':
                choices = 'Funding Societies'
            elif Company == '2378':
                choices = 'CleverTap'
            elif Company == '2379':
                choices = 'CrowdRiff'
            elif Company == '2380':
                choices = 'Grailed'
            elif Company == '2381':
                choices = 'LumenAd'
            elif Company == '2382':
                choices = 'Purse'
            elif Company == '2383':
                choices = 'SquadVoice'
            elif Company == '2384':
                choices = 'Shop101'
            elif Company == '2385':
                choices = 'Akulaku'
            elif Company == '2386':
                choices = 'Parsable'
            elif Company == '2387':
                choices = 'Kodiak Robotics'
            elif Company == '2388':
                choices = 'Dude Solutions'
            elif Company == '2389':
                choices = 'SweetEscape'
            elif Company == '2390':
                choices = 'TouchBistro'
            elif Company == '2391':
                choices = 'Envoy'
            elif Company == '2392':
                choices = 'VSCO'
            elif Company == '2393':
                choices = 'DataStax'
            elif Company == '2394':
                choices = 'Xerpa'
            elif Company == '2395':
                choices = 'RedDoorz'
            elif Company == '2396':
                choices = 'Zoox'
            elif Company == '2397':
                choices = 'EasyPost'
            elif Company == '2398':
                choices = 'Clearbanc'
            elif Company == '2399':
                choices = 'BeeTech'
            elif Company == '2400':
                choices = 'NuoDB'
            elif Company == '2401':
                choices = 'Rhumbix'
            elif Company == '2402':
                choices = 'Atsu'
            elif Company == '2403':
                choices = 'Geekwire'
            elif Company == '2404':
                choices = 'FloQast'
            elif Company == '2405':
                choices = 'Omie'
            elif Company == '2406':
                choices = 'Clinc'
            elif Company == '2407':
                choices = 'Lighthouse Labs'
            elif Company == '2408':
                choices = 'LoopMe'
            elif Company == '2409':
                choices = 'CipherTrace'
            elif Company == '2410':
                choices = 'Elliptic'
            elif Company == '2411':
                choices = 'Zest AI'
            elif Company == '2412':
                choices = 'Unison'
            elif Company == '2413':
                choices = 'Unbabel'
            elif Company == '2414':
                choices = 'Button'
            elif Company == '2415':
                choices = 'Eden / Managed By Q'
            elif Company == '2416':
                choices = 'BVAccel'
            elif Company == '2417':
                choices = 'Kenoby'
            elif Company == '2418':
                choices = 'Connected'
            elif Company == '2419':
                choices = 'GetNinjas'
            elif Company == '2420':
                choices = 'Spyce'
            elif Company == '2421':
                choices = 'Creditas'
            elif Company == '2422':
                choices = 'Lytics'
            elif Company == '2423':
                choices = 'Slice Labs'
            elif Company == '2424':
                choices = 'TechAdvance'
            elif Company == '2425':
                choices = 'Zola'
            elif Company == '2426':
                choices = 'ezCater'
            elif Company == '2427':
                choices = 'Sage Therapeutics'
            elif Company == '2428':
                choices = 'Branch Metrics'
            elif Company == '2429':
                choices = 'Newfront Insurance'
            elif Company == '2430':
                choices = 'Ibotta'
            elif Company == '2431':
                choices = 'Virta Health'
            elif Company == '2432':
                choices = 'Group Nine Media'
            elif Company == '2433':
                choices = 'Payfactors'
            elif Company == '2434':
                choices = 'Nav'
            elif Company == '2435':
                choices = 'AskNicely'
            elif Company == '2436':
                choices = 'RainFocus'
            elif Company == '2437':
                choices = 'BounceX'
            elif Company == '2438':
                choices = 'Wordstream'
            elif Company == '2439':
                choices = 'BusBud'
            elif Company == '2440':
                choices = 'Borrowell'
            elif Company == '2441':
                choices = 'PerkSpot'
            elif Company == '2442':
                choices = 'Bitfarms'
            elif Company == '2443':
                choices = 'Iflix'
            elif Company == '2444':
                choices = 'Gympass'
            elif Company == '2445':
                choices = 'Minted'
            elif Company == '2446':
                choices = 'Traveloka'
            elif Company == '2447':
                choices = 'Arrive Logistics'
            elif Company == '2448':
                choices = 'Jetty'
            elif Company == '2449':
                choices = 'Opencare'
            elif Company == '2450':
                choices = 'Anagram'
            elif Company == '2451':
                choices = 'G/O Media Group'
            elif Company == '2452':
                choices = 'DSCO'
            elif Company == '2453':
                choices = 'Tripbam'
            elif Company == '2454':
                choices = 'Avantage Entertainment'
            elif Company == '2455':
                choices = 'Alegion'
            elif Company == '2456':
                choices = 'AllyO'
            elif Company == '2457':
                choices = 'Mews'
            elif Company == '2458':
                choices = 'PeopleGrove'
            elif Company == '2459':
                choices = 'The Muse'
            elif Company == '2460':
                choices = 'ClassPass'
            elif Company == '2461':
                choices = 'eGym'
            elif Company == '2462':
                choices = 'Industrious'
            elif Company == '2463':
                choices = '1stdibs'
            elif Company == '2464':
                choices = 'ThirdLove'
            elif Company == '2465':
                choices = 'Shuttl'
            elif Company == '2466':
                choices = 'Jobcase'
            elif Company == '2467':
                choices = 'Dynamic Signal'
            elif Company == '2468':
                choices = 'FiscalNote'
            elif Company == '2469':
                choices = 'Sauce Labs'
            elif Company == '2470':
                choices = 'Humu'
            elif Company == '2471':
                choices = 'Coding Dojo'
            elif Company == '2472':
                choices = 'Instamojo'
            elif Company == '2473':
                choices = 'Synergysuite'
            elif Company == '2474':
                choices = 'Atlanta Tech Village'
            elif Company == '2475':
                choices = 'Capillary'
            elif Company == '2476':
                choices = 'The Modist'
            elif Company == '2477':
                choices = 'Booksy'
            elif Company == '2478':
                choices = 'Flymya'
            elif Company == '2479':
                choices = 'PatientPop'
            elif Company == '2480':
                choices = 'Earnin'
            elif Company == '2481':
                choices = 'Wonolo'
            elif Company == '2482':
                choices = 'Acko'
            elif Company == '2483':
                choices = 'Moovel'
            elif Company == '2484':
                choices = 'Crayon'
            elif Company == '2485':
                choices = 'Pana'
            elif Company == '2486':
                choices = 'Sensibill'
            elif Company == '2487':
                choices = 'Usermind'
            elif Company == '2488':
                choices = 'Incredible Health'
            elif Company == '2489':
                choices = 'Currency'
            elif Company == '2490':
                choices = 'GOAT Group'
            elif Company == '2491':
                choices = 'Le Tote'
            elif Company == '2492':
                choices = 'Levelset'
            elif Company == '2493':
                choices = 'Pebblepost'
            elif Company == '2494':
                choices = 'WhyHotel'
            elif Company == '2495':
                choices = 'KeepTruckin'
            elif Company == '2496':
                choices = 'AdRoll'
            elif Company == '2497':
                choices = 'Rover'
            elif Company == '2498':
                choices = 'Turo'
            elif Company == '2499':
                choices = 'uShip'
            elif Company == '2500':
                choices = 'SkySlope'
            elif Company == '2501':
                choices = 'Siteimprove'
            elif Company == '2502':
                choices = 'AngelList'
            elif Company == '2503':
                choices = 'Zenoti'
            elif Company == '2504':
                choices = 'DialSource'
            elif Company == '2505':
                choices = 'Adara'
            elif Company == '2506':
                choices = 'Claravine'
            elif Company == '2507':
                choices = 'Kazoo'
            elif Company == '2508':
                choices = 'Snap Finance'
            elif Company == '2509':
                choices = 'Zerto'
            elif Company == '2510':
                choices = 'RigUp'
            elif Company == '2511':
                choices = 'FabHotels'
            elif Company == '2512':
                choices = 'Hibob'
            elif Company == '2513':
                choices = 'Maven'
            elif Company == '2514':
                choices = 'Blume Global'
            elif Company == '2515':
                choices = 'Catalant'
            elif Company == '2516':
                choices = 'Starship Technologies'
            elif Company == '2517':
                choices = 'Loftsmart'
            elif Company == '2518':
                choices = 'Iris Nova'
            elif Company == '2519':
                choices = 'Cuyana'
            elif Company == '2520':
                choices = 'Amplero'
            elif Company == '2521':
                choices = 'Polarr'
            elif Company == '2522':
                choices = 'TravelTriangle'
            elif Company == '2523':
                choices = 'OneWeb'
            elif Company == '2524':
                choices = 'HOOQ'
            elif Company == '2525':
                choices = 'Restaurant365'
            elif Company == '2526':
                choices = 'Blueground'
            elif Company == '2527':
                choices = 'Zipcar'
            elif Company == '2528':
                choices = 'Mogo'
            elif Company == '2529':
                choices = 'DISCO'
            elif Company == '2530':
                choices = 'Raken'
            elif Company == '2531':
                choices = 'Bench'
            elif Company == '2532':
                choices = 'Oh My Green'
            elif Company == '2533':
                choices = 'Bevi'
            elif Company == '2534':
                choices = 'Opal'
            elif Company == '2535':
                choices = 'Bcredi'
            elif Company == '2536':
                choices = 'Make School'
            elif Company == '2537':
                choices = 'Pivot3'
            elif Company == '2538':
                choices = 'B8ta'
            elif Company == '2539':
                choices = 'Fareportal'
            elif Company == '2540':
                choices = 'Ecobee'
            elif Company == '2541':
                choices = 'Passport'
            elif Company == '2542':
                choices = 'Peerspace'
            elif Company == '2543':
                choices = 'GoSpotCheck'
            elif Company == '2544':
                choices = 'Consider.co'
            elif Company == '2545':
                choices = 'Nativo'
            elif Company == '2546':
                choices = 'TripActions'
            elif Company == '2547':
                choices = 'Lyric'
            elif Company == '2548':
                choices = 'Rangle'
            elif Company == '2549':
                choices = "O'Reilly Media"
            elif Company == '2550':
                choices = 'OutboundEngine'
            elif Company == '2551':
                choices = 'Overtime'
            elif Company == '2552':
                choices = 'Jama'
            elif Company == '2553':
                choices = 'Element Analytics'
            elif Company == '2554':
                choices = 'Clutter'
            elif Company == '2555':
                choices = 'Universal Standard'
            elif Company == '2556':
                choices = 'Takl'
            elif Company == '2557':
                choices = 'Foodsby'
            elif Company == '2558':
                choices = 'TravelBank'
            elif Company == '2559':
                choices = 'Flowr'
            elif Company == '2560':
                choices = 'Peerfit'
            elif Company == '2561':
                choices = 'The Guild'
            elif Company == '2562':
                choices = 'Drip'
            elif Company == '2563':
                choices = 'GrayMeta'
            elif Company == '2564':
                choices = 'Triplebyte'
            elif Company == '2565':
                choices = 'Ladder Life'
            elif Company == '2566':
                choices = 'Cabin'
            elif Company == '2567':
                choices = 'Eight Sleep'
            elif Company == '2568':
                choices = 'Flywheel Sports'
            elif Company == '2569':
                choices = 'Peek'
            elif Company == '2570':
                choices = 'CTO.ai'
            elif Company == '2571':
                choices = 'Yonder'
            elif Company == '2572':
                choices = 'Service'
            elif Company == '2573':
                choices = 'Ejento'
            elif Company == '2574':
                choices = 'Remote Year'
            elif Company == '2575':
                choices = 'Lola'
            elif Company == '2576':
                choices = 'Anyvision'
            elif Company == '2577':
                choices = 'Popin'
            elif Company == '2578':
                choices = 'Tuft & Needle'
            elif Company == '2579':
                choices = 'Flytedesk'
            elif Company == '2580':
                choices = 'Help.com'
            elif Company == '2581':
                choices = 'Panda Squad'
            elif Company == '2582':
                choices = 'Tamara Mellon'

            Location = request.form['location']
            if Location == '0':
                 choice = 'SF Bay Area'
            elif Location == '1':
                 choice = 'Philadelphia'
            elif Location == '2':
                 choice = 'Austin'
            elif Location == '3':
                choice = 'Los Angeles'
            elif Location == '4':
                choice = 'Boston'
            elif Location == '5':
                choice = 'Pittsburgh'
            elif Location == '6':
                choice = 'Portland'
            elif Location == '7':
                choice = 'New Delhi'
            elif Location == '8':
                choice = 'Bengaluru'
            elif Location == '9':
                choice = 'London'
            elif Location == '10':
                choice = 'San Diego'
            elif Location == '11':
                choice = 'Orlando'
            elif Location == '12':
                choice = 'New York City'
            elif Location == '13':
                choice = 'Atlanta'
            elif Location == '14':
                choice = 'Madrid'
            elif Location == '15':
                choice = 'Seattle'
            elif Location == '16':
                choice = 'Hartford'
            elif Location == '17':
                choice = 'Denver'
            elif Location == '18':
                choice = 'Sacramento'
            elif Location == '19':
                choice = 'Prague'
            elif Location == '20':
                choice = 'Salt Lake City'
            elif Location == '21':
                choice = 'Ghent'
            elif Location == '22':
                choice = 'Tampa Bay'
            elif Location == '23':
                choice = 'Detroit'
            elif Location == '24':
                choice = 'Paris'
            elif Location == '25':
                choice = 'Barcelona'
            elif Location == '26':
                choice = 'Dublin'
            elif Location == '27':
                choice = 'Santiago'
            elif Location == '28':
                choice = 'Copenhagen'
            elif Location == '29':
                choice = 'Vancouver'
            elif Location == '30':
                choice = 'Montreal'
            elif Location == '31':
                choice = 'Miami'
            elif Location == '32':
                choice = 'Pune'
            elif Location == '33':
                choice = 'Lagos'
            elif Location == '34':
                choice = 'Tel Aviv'
            elif Location == '35':
                choice = 'Singapore'
            elif Location == '36':
                choice = 'Yavne'
            elif Location == '37':
                choice = "Xi'an"
            elif Location == '38':
                choice = 'Lehi'
            elif Location == '39':
                choice = 'Amsterdam'
            elif Location == '40':
                choice = 'Phoenix'
            elif Location == '41':
                choice = 'Gurugram'
            elif Location == '42':
                choice = 'Vilnius'
            elif Location == '43':
                choice = 'Chennai'
            elif Location == '44':
                choice = 'Sydney'
            elif Location == '45':
                choice = 'Krakow'
            elif Location == '46':
                choice = 'Manchester'
            elif Location == '47':
                choice = 'Boulder'
            elif Location == '48':
                choice = 'Stockholm'
            elif Location == '49':
                choice = 'Ann Arbor'
            elif Location == '50':
                choice = 'Nashik'
            elif Location == '51':
                choice = 'Berlin'
            elif Location == '52':
                choice = 'Oslo'
            elif Location == '53':
                choice = 'Chicago'
            elif Location == '54':
                choice = 'Baltimore'
            elif Location == '55':
                choice = 'Espoo'
            elif Location == '56':
                choice = 'Fort Collins'
            elif Location == '57':
                choice = 'Toronto'
            elif Location == '58':
                choice = 'Salisbury'
            elif Location == '59':
                choice = 'Cayman Islands'
            elif Location == '60':
                choice = 'Brno'
            elif Location == '61':
                choice = 'Santa Barbara'
            elif Location == '62':
                choice = 'Minneapolis'
            elif Location == '63':
                choice = 'Munich'
            elif Location == '64':
                choice = 'Walldorf'
            elif Location == '65':
                choice = 'Vienna'
            elif Location == '66':
                choice = 'Jakarta'
            elif Location == '67':
                choice = 'Washington D.C.'
            elif Location == '68':
                choice = 'Dallas'
            elif Location == '69':
                choice = 'Tokyo'
            elif Location == '70':
                choice = 'Columbus'
            elif Location == '71':
                choice = 'Tallinn'
            elif Location == '72':
                choice = 'Karachi'
            elif Location == '73':
                choice = 'Hamburg'
            elif Location == '74':
                choice = 'Saskatoon'
            elif Location == '75':
                choice = 'Memphis'
            elif Location == '76':
                choice = 'Corvallis'
            elif Location == '77':
                choice = 'Norwalk'
            elif Location == '78':
                choice = 'Milwaukee'
            elif Location == '79':
                choice = 'Noida'
            elif Location == '80':
                choice = 'Charleston'
            elif Location == '81':
                choice = 'Haifa'
            elif Location == '82':
                choice = 'Shanghai'
            elif Location == '83':
                choice = 'Lodz'
            elif Location == '84':
                choice = 'Nashville'
            elif Location == '85':
                choice = 'Abuja'
            elif Location == '86':
                choice = 'Santa Fe'
            elif Location == '87':
                choice = 'Mumbai'
            elif Location == '88':
                choice = 'Ibadan'
            elif Location == '89':
                choice = 'St. Louis'
            elif Location == '90':
                choice = 'Omaha'
            elif Location == '91':
                choice = 'Bucharest'
            elif Location == '92':
                choice = 'Birmingham'
            elif Location == '93':
                choice = 'Beijing'
            elif Location == '94':
                choice = 'St. Gallen'
            elif Location == '95':
                choice = 'Helsinki'
            elif Location == '96':
                choice = 'Shenzen'
            elif Location == '97':
                choice = 'Calgary'
            elif Location == '98':
                choice = 'Kansas City'
            elif Location == '99':
                choice = 'Stamford'
            elif Location == '100':
                choice = 'Leeds'
            elif Location == '101':
                choice = 'Zurich'
            elif Location == '102':
                choice = 'Sao Paulo'
            elif Location == '103':
                choice = 'Jacksonville'
            elif Location == '104':
                choice = 'Raleigh'
            elif Location == '105':
                choice = 'Edinburgh'
            elif Location == '106':
                choice = 'Charlotte'
            elif Location == '107':
                choice = 'Belo Horizonte'
            elif Location == '108':
                choice = 'Accra'
            elif Location == '109':
                choice = 'Hong Kong'
            elif Location == '110':
                choice = 'Nairobi'
            elif Location == '111':
                choice = 'Kolkata'
            elif Location == '112':
                choice = 'Indianapolis'
            elif Location == '113':
                choice = 'Sandnes'
            elif Location == '114':
                choice = 'Melbourne'
            elif Location == '115':
                choice = 'Auckland'
            elif Location == '116':
                choice = 'Luxembourg'
            elif Location == '117':
                choice = 'Lexington'
            elif Location == '118':
                choice = 'Evansville'
            elif Location == '119':
                choice = "Ra'anana"
            elif Location == '120':
                choice = 'Mexico City'
            elif Location == '121':
                choice = 'Førde'
            elif Location == '122':
                choice = 'Boise'
            elif Location == '123':
                choice = 'Alamosa'
            elif Location == '124':
                choice = 'Seoul'
            elif Location == '125':
                choice = 'Reno'
            elif Location == '126':
                choice = 'Chemnitz'
            elif Location == '127':
                choice = 'Charlottesville'
            elif Location == '128':
                choice = 'Kfar Saba'
            elif Location == '129':
                choice = 'Hangzhou'
            elif Location == '130':
                choice = 'Houston'
            elif Location == '131':
                choice = 'Norfolk'
            elif Location == '132':
                choice = 'Cluj-Napoca'
            elif Location == '133':
                choice = 'Las Vegas'
            elif Location == '134':
                choice = 'Brisbane'
            elif Location == '135':
                choice = 'Ottawa'
            elif Location == '136':
                choice = 'Riyadh'
            elif Location == '137':
                choice = 'Wrocław'
            elif Location == '138':
                choice = 'Manila'
            elif Location == '139':
                choice = 'Zug'
            elif Location == '140':
                choice = 'Cincinnati'
            elif Location == '141':
                choice = 'Little Rock'
            elif Location == '142':
                choice = 'Cleveland'
            elif Location == '143':
                choice = 'Monterrey'
            elif Location == '144':
                choice = 'Nashua'
            elif Location == '145':
                choice = 'San Antonio'
            elif Location == '146':
                choice = 'New Hope'
            elif Location == '147':
                choice = 'Kyiv'
            elif Location == '148':
                choice = 'Geneva'
            elif Location == '149':
                choice = 'Chester'
            elif Location == '150':
                choice = 'Warsaw'
            elif Location == '151':
                choice = 'Linz'
            elif Location == '152':
                choice = 'Madison'
            elif Location == '153':
                choice = 'Kitchener'
            elif Location == '154':
                choice = 'Wellington'
            elif Location == '155':
                choice = 'Gydnia'
            elif Location == '156':
                choice = 'Blumenau'
            elif Location == '157':
                choice = 'Baton Rouge'
            elif Location == '158':
                choice = 'Albany'
            elif Location == '159':
                choice = 'Milan'
            elif Location == '160':
                choice = 'Frankfurt'
            elif Location == '161':
                choice = 'Waterloo'
            elif Location == '162':
                choice = 'Karlsruhe'
            elif Location == '163':
                choice = 'Curitiba'
            elif Location == '164':
                choice = 'New Haven'
            elif Location == '165':
                choice = 'Coimbra'
            elif Location == '166':
                choice = 'Jersey City'
            elif Location == '167':
                choice = 'Kiel'
            elif Location == '168':
                choice = 'Oxford'
            elif Location == '169':
                choice = 'Wilmington'
            elif Location == '170':
                choice = 'Providence'
            elif Location == '171':
                choice = 'Bogota'
            elif Location == '172':
                choice = 'Durham'
            elif Location == '173':
                choice = 'Buenos Aires'
            elif Location == '174':
                choice = 'Indore'
            elif Location == '175':
                choice = 'Patna'
            elif Location == '176':
                choice = 'Bismarck'
            elif Location == '177':
                choice = 'Grand Rapids'
            elif Location == '178':
                choice = 'Beau Vallon'
            elif Location == '179':
                choice = 'Utrecht'
            elif Location == '180':
                choice = 'Burlington'
            elif Location == '181':
                choice = 'Bend'
            elif Location == '182':
                choice = 'Guadalajara'
            elif Location == '183':
                choice = 'Cairo'
            elif Location == '184':
                choice = 'Dubai'
            elif Location == '185':
                choice = 'Gothenburg'
            elif Location == '186':
                choice = 'Dover'
            elif Location == '187':
                choice = 'Malmö'
            elif Location == '188':
                choice = 'Logan'
            elif Location == '189':
                choice = 'Eindhoven'
            elif Location == '190':
                choice = 'Athens'
            elif Location == '191':
                choice = 'Hyderabad'
            elif Location == '192':
                choice = 'Nebraska City'
            elif Location == '193':
                choice = 'Non-U.S.'
            elif Location == '194':
                choice = 'Trondheim'
            elif Location == '195':
                choice = 'Düsseldorf'
            elif Location == '196':
                choice = 'San Luis Obispo'
            elif Location == '197':
                choice = 'Jerusalem'
            elif Location == '198':
                choice = 'Brussels'
            elif Location == '199':
                choice = 'The Hague'
            elif Location == '200':
                choice = 'Kuala Lumpur'
            elif Location == '201':
                choice = 'Bristol'
            elif Location == '202':
                choice = 'Budapest'
            elif Location == '203':
                choice = 'Ho Chi Minh City'
            elif Location == '204':
                choice = 'Winnipeg'
            elif Location == '205':
                choice = 'Bangkok'
            elif Location == '206':
                choice = 'Richmond'
            elif Location == '207':
                choice = 'Porto Alegre'
            elif Location == '208':
                choice = 'Victoria'
            elif Location == '209':
                choice = 'Ferdericton'
            elif Location == '210':
                choice = 'Dakar'
            elif Location == '211':
                choice = 'Florianópolis'
            elif Location == '212':
                choice = 'Lahore'
            elif Location == '213':
                choice = 'Louisville'
            elif Location == '214':
                choice = 'Huntsville'
            elif Location == '215':
                choice = 'Spokane'
            elif Location == '216':
                choice = 'Lima'
            elif Location == '217':
                choice = 'Malmo'
            elif Location == '218':
                choice = 'Brasilia'
            elif Location == '219':
                choice = 'Selangor'
            elif Location == '220':
                choice = 'Manama'
            elif Location == '221':
                choice = 'Istanbul'
            elif Location == '222':
                choice = 'Moscow'
            elif Location == '223':
                choice = 'Davenport'
            elif Location == '224':
                choice = 'Toulouse'
            elif Location == '225':
                choice = 'Montevideo'
            elif Location == '226':
                choice = 'Fayetteville'
            elif Location == '227':
                choice = 'Sofia'
            elif Location == '228':
                choice = 'Cork'
            elif Location == '229':
                choice = 'Ahmedabad'
            elif Location == '230':
                choice = 'Joinville'
            elif Location == '231':
                choice = 'Hanoi'
            elif Location == '232':
                choice = 'Dusseldorf'
            elif Location == '233':
                choice = 'Lisbon'
            elif Location == '234':
                choice = 'Cape Town'
            elif Location == '235':
                choice = 'Missoula'
            elif Location == '236':
                choice = 'Quebec'
            elif Location == '237':
                choice = 'Yangon'
            elif Location == '238':
                choice = 'New Orleans'


            Industry = request.form['industry']
            if  Industry == '0':
                ind = 'Product'
            elif Industry == '1':
                ind = 'Food'
            elif Industry == '2':
                ind = 'Other'
            elif Industry == '3':
                ind = 'Finance'
            elif Industry == '4':
                ind = 'HR'
            elif Industry == '5':
                ind = 'Transportation'
            elif Industry == '6':
                ind = 'Consumer'
            elif Industry == '7':
                ind = 'Travel'
            elif Industry == '8':
                ind = 'Education'
            elif Industry == '9':
                ind = 'Hardware'
            elif Industry == '10':
                ind = 'Energy'
            elif Industry == '11':
                ind = 'Healthcare'
            elif Industry == '12':
                ind = 'Support'
            elif Industry == '13':
                ind = 'Crypto'
            elif Industry == '14':
                ind = 'Fitness'
            elif Industry == '15':
                ind = 'Aerospace'
            elif Industry == '16':
                ind = 'Marketing'
            elif Industry == '17':
                ind = 'Retail'
            elif Industry == '18':
                ind = 'Real Estate'
            elif Industry == '19':
                ind = 'AI'
            elif Industry == '20':
                ind = 'Infrastructure'
            elif Industry == '21':
                ind = 'Logistics'
            elif Industry == '22':
                ind = 'Security'
            elif Industry == '23':
                ind = 'Manufacturing'
            elif Industry == '24':
                ind = 'Recruiting'
            elif Industry == '25':
                ind = 'Media'
            elif Industry == '26':
                ind = 'Data'
            elif Industry == '27':
                ind = 'Sales'
            elif Industry == '28':
                ind = 'Construction'
            elif Industry == '29':
                ind = 'Legal' 

            Stage = request.form['stage']
            if Stage == '0':
                sta = 'Unknown'
            elif Stage == '1':
                sta  = 'Series H'
            elif Stage == '2':
                sta  = 'Series D'  
            elif Stage == '3':
                sta  = 'Series B'
            elif Stage == '4':
                sta  = 'Acquired'  
            elif Stage == '5':
                sta  = 'Post-IPO'  
            elif Stage == '6':
                sta  = 'Series E'  
            elif Stage == '7':
                sta  = 'Series J'  
            elif Stage == '8':
                sta  = 'Seed'  
            elif Stage == '9':
                sta  = 'Series G'  
            elif Stage == '10':
                sta  = 'Series C'  
            elif Stage == '11':
                sta  = 'Private Equity'   
            elif Stage == '12':
                sta  = 'Series A'  
            elif Stage == '13':
                sta  = 'Subsidiary'  
            elif Stage == '14':
                sta  = 'Series F'  
            elif Stage == '15':
                sta  = 'Series I'  
                                           
            Country = request.form['country']
            if Country == '0':
                cou = 'United States'
            elif Country == '1':
                cou = 'India'
            elif Country == '2':
                cou = 'United Kingdom'
            elif Country == '3':
                cou = 'Spain'
            elif Country == '4':
                cou = 'Czech Republic'
            elif Country == '5':
                cou = 'Belgium'
            elif Country == '6':
                cou = 'France'
            elif Country == '7':
                cou = 'Ireland'
            elif Country == '8':
                cou = 'Chile'
            elif Country == '9':
                cou = 'Denmark'
            elif Country == '10':
                cou = 'Canada'
            elif Country == '11':
                cou = 'Nigeria'
            elif Country == '12':
                cou = 'Israel'
            elif Country == '13':
                cou = 'Singapore'
            elif Country == '14':
                cou = 'China'
            elif Country == '15':
                cou = 'Netherlands'
            elif Country == '16':
                cou = 'Lithuania'
            elif Country == '17':
                cou = 'Australia'
            elif Country == '18':
                cou = 'Poland'
            elif Country == '19':
                cou = 'Sweden'
            elif Country == '20':
                cou = 'Germany'
            elif Country == '21':
                cou = 'Norway'
            elif Country == '22':
                cou = 'Finland'
            elif Country == '23':
                cou = 'Cayman Islands'
            elif Country == '24':
                cou = 'Austria'
            elif Country == '25':
                cou = 'Indonesia'
            elif Country == '26':
                cou = 'Japan'
            elif Country == '27':
                cou = 'Estonia'
            elif Country == '28':
                cou = 'Pakistan'
            elif Country == '29':
                cou = 'Romania'
            elif Country == '30':
                cou = 'Switzerland'
            elif Country == '31':
                cou = 'Brazil'
            elif Country == '32':
                cou = 'Ghana'
            elif Country == '33':
                cou = 'Hong Kong'
            elif Country == '34':
                cou = 'Kenya'
            elif Country == '35':
                cou = 'New Zealand'
            elif Country == '36':
                cou = 'Luxembourg'
            elif Country == '37':
                cou = 'Mexico'
            elif Country == '38':
                cou = 'South Korea'
            elif Country == '39':
                cou = 'Saudi Arabia'
            elif Country == '40':
                cou = 'Philippines'
            elif Country == '41':
                cou = 'Ukraine'
            elif Country == '42':
                cou = 'Italy'
            elif Country == '43':
                cou = 'Portugal'
            elif Country == '44':
                cou = 'Colombia'
            elif Country == '45':
                cou = 'Argentina'
            elif Country == '46':
                cou = 'Seychelles'
            elif Country == '47':
                cou = 'Egypt'
            elif Country == '48':
                cou = 'Greece'
            elif Country == '49':
                cou = 'Malaysia'
            elif Country == '50':
                cou = 'Hungary'
            elif Country == '51':
                cou = 'Vietnam'
            elif Country == '52':
                cou = 'Thailand'
            elif Country == '53':
                cou = 'Senegal'
            elif Country == '54':
                cou = 'United Arab Emirates'
            elif Country == '55':
                cou = 'Peru'
            elif Country == '56':
                cou = 'Bahrain'
            elif Country == '57':
                cou = 'Turkey'
            elif Country == '58':
                cou = 'Russia'
            elif Country == '59':
                cou = 'Uruguay'
            elif Country == '60':
                cou = 'Bulgaria'
            elif Country == '61':
                cou = 'South Africa'
            elif Country == '62':
                cou = 'Myanmar'

            Funds_raised = float(request.form['funds_raised'])
            Day = int(request.form['day'])
            Month = int(request.form['month'])
            Year = int(request.form['year'])
            model = request.form['model']
            # Ensure input data is in the correct format
            input_variables = pd.DataFrame([[Company, Location, Industry, Stage, Country, Funds_raised, Day, Month, Year]],
                                            columns=['company', 'location', 'industry', 'stage', 'country', 'funds_raised', 'day', 'month', 'year'],
                                            index=['input'])

            # You may need to preprocess 'Company', 'Location', etc. if they are categorical variables
            # Assuming preprocessing is not required for simplicity
            
            # Convert the dataframe to the format required by the model
            final_features = input_variables.to_numpy()
            print(final_features)

            # Make the prediction
            # prediction = layoff.predict(final_features)
            if model == 'GradientBoostingRegressor':
                prediction = gradient_boost.predict(final_features)
                output = int(prediction[0])
                result =int(output) * int(output) * int(output)
            elif model == 'RandomForestRegressor':
                prediction = RandomForest.predict(final_features)
                output = int(prediction[0])
                result =int(output) * int(output) * int(output)

            # Assuming the prediction returns a value that needs to be cubed
            # output = int(prediction[0])
            # print(output)  
            # result =int(output) * int(output) * int(output) 
        

    return render_template('result.html', prediction_text=int(result), model=model, choices=choices,choice=choice,ind=ind,sta=sta,cou=cou,Funds_raised=Funds_raised,Day=Day,Month=Month,Year=Year)
 
@app.route('/predictions')
def predictions():
    return render_template('predictions.html')
    
 

# Load the model (ensure this path is correct)
 

@app.route('/predicts', methods=['POST'])
def predicts():
    resuls = {}  # Default empty dictionary
    results = ''  # Default empty string

    if request.method == 'POST': 
            resuls = request.form.to_dict()
            print(resuls)
       
            
             
            Age = request.form['Age']                             
            Department = request.form['Department']
            if Department == '0':
                Depa = 'Sales'
            elif Department == '1':
                Depa = 'Research & Development'
            elif Department == '2':
                Depa = 'Human Resources'
            DistanceFromHome = request.form['DistanceFromHome']   
            EducationField = request.form['EducationField']
            if EducationField == '0':
                Edu = 'Life Sciences'
            elif EducationField == '1':
                Edu = 'Other'
            elif EducationField == '2':
                Edu = 'Medical'
            elif EducationField == '3':
                Edu = 'Marketing'
            elif EducationField == '4':
                Edu = 'Technical Degree'
            elif EducationField == '4':
                Edu = 'Human Resources'        

            EmployeeNumber = request.form['EmployeeNumber']
            Gender = request.form['Gender']
            if Gender == '0':
                Gens = 'Female'
            elif Gender == '1':
                Gens = 'Male'

            JobRole = request.form['JobRole']
            if JobRole == '0':
                Job = 'Sales Executive'
            elif JobRole == '1':
                Job = 'Research Scientist'
            elif JobRole == '2':
                Job = 'Research Scientist' 
            elif JobRole == '3':
                Job = 'Research Scientist'
            elif JobRole == '4':
                Job = 'Research Scientist'  
            elif JobRole == '5':
                Job = 'Research Scientist'
            elif JobRole == '6':
                Job = 'Research Scientist' 
            elif JobRole == '7':
                Job = 'Research Scientist'
            elif JobRole == '8':
                Job = 'Research Scientist'    

             
            JobSatisfaction = request.form['JobSatisfaction']
            if JobSatisfaction == '1':
                jobs = 'Low'
            elif JobSatisfaction == '2':
                jobs = 'Medium'
            elif JobSatisfaction == '3':
                jobs = 'High'
            elif JobSatisfaction == '4':
                jobs = 'Very High' 
            MaritalStatus = request.form['MaritalStatus']
            if MaritalStatus == '0':
                Marital = 'Single'
            elif MaritalStatus == '1':
                Marital = 'Married'
            elif MaritalStatus == '2':
                Marital = 'Divorced'
                        
            MonthlyIncome = request.form['MonthlyIncome']
            NumCompaniesWorked = request.form['NumCompaniesWorked']
            OverTime = request.form['OverTime']
            if OverTime == '0':
                over = 'Yes'
            elif OverTime == '1':
                over = 'No'
            PercentSalaryHike = request.form['PercentSalaryHike']
            PerformanceRating = request.form['PerformanceRating']
            StandardHours = request.form['StandardHours']
            TotalWorkingYears = request.form['TotalWorkingYears']
            WorkLifeBalance = request.form['WorkLifeBalance']
            if WorkLifeBalance == '1':
                Works = 'Bad'
            elif WorkLifeBalance == '2':
                Works = 'Good'
            elif WorkLifeBalance == '3':
                Works = 'Better'
            elif WorkLifeBalance == '4':
                Works = 'Best' 
            YearsAtCompany = request.form['YearsAtCompany']
            YearsInCurrentRole = request.form['YearsInCurrentRole']
            YearsSinceLastPromotion = request.form['YearsSinceLastPromotion']
            YearsWithCurrManager = request.form['YearsWithCurrManager']    
            Model = request.form['Model']
            # Ensure input data is in the correct format
            input_variables = pd.DataFrame([[Age, Department, DistanceFromHome, EducationField, EmployeeNumber, Gender, JobRole, JobSatisfaction, MaritalStatus,MonthlyIncome,NumCompaniesWorked,OverTime,PercentSalaryHike,PerformanceRating,StandardHours,TotalWorkingYears,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager]],
                                            columns=['Age','Department','DistanceFromHome','EducationField','EmployeeNumber','Gender','JobRole','JobSatisfaction','MaritalStatus','MonthlyIncome','NumCompaniesWorked','OverTime','PercentSalaryHike','PerformanceRating','StandardHours','TotalWorkingYears','WorkLifeBalance','YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager'],
                                            index=['input'])

            # You may need to preprocess 'Company', 'Location', etc. if they are categorical variables
            # Assuming preprocessing is not required for simplicity
            
            # Convert the dataframe to the format required by the model
            final_features = input_variables.to_numpy()
            print(final_features)

            # Make the prediction
            # prediction = layoff.predict(final_features)
            if Model == 'RandomForestClassifier':
                prediction = job_random.predict(final_features)
                outputs = prediction[0]
         
            elif Model == 'BaggingClassifier':
                prediction = bagging.predict(final_features)
                outputs = prediction[0]
             

            # Assuming the prediction returns a value that needs to be cubed
            # output = int(prediction[0])
            # print(output)  
            # result =int(output) * int(output) * int(output) 
        

    
    return render_template('results.html', prediction_text=outputs, model=Model,Age=Age, Depa=Depa,DistanceFromHome=DistanceFromHome,Edu=Edu,EmployeeNumber=EmployeeNumber,Gens=Gens,Job=Job,jobs=jobs, Marital=Marital,MonthlyIncome=MonthlyIncome,NumCompaniesWorked=NumCompaniesWorked,over=over,PercentSalaryHike=PercentSalaryHike,PerformanceRating=PerformanceRating,StandardHours=StandardHours,TotalWorkingYears=TotalWorkingYears,Works=Works,YearsAtCompany=YearsAtCompany,YearsInCurrentRole=YearsInCurrentRole,YearsSinceLastPromotion=YearsSinceLastPromotion,YearsWithCurrManager=YearsWithCurrManager)

	# int_feature = [x for x in request.form.values()]
	# print(int_feature)
	# int_feature = [float(i) for i in int_feature]
	# final_features = [np.array(int_feature)]
	# prediction = sales.predict(final_features)

	# output =format(float(prediction[0]))
	# print(output)  
	# result =float(output) * float(output) * float(output)
	# return render_template('prediction.html', prediction_text= int(result))

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/charts')
def charts():
    return render_template('charts.html') 

@app.route('/performance')
def performance():
    return render_template('performance.html')    

 
    
if __name__ == "__main__":
    app.run(debug=True)
