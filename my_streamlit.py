# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 19:24:46 2021

@author: Pranav Gowtham Bulusu
"""

import pickle
import streamlit as st


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

def predict(brand,model,yearofregistration,offertype_Gesuch,vehicletype_bus,vehicletype_cabrio,
                                    vehicletype_coupe,vehicletype_kleinwagen,vehicletype_kombi,vehicletype_limousine,
                                    vehicletype_suv,gearbox_manuell,kilometer_10000,kilometer_20000,kilometer_30000,
                                    kilometer_40000, kilometer_50000,kilometer_60000,kilometer_70000,kilometer_80000,
                                    kilometer_90000,kilometer_100000,kilometer_125000,kilometer_150000,monthofregistration_2,
                                    monthofregistration_3,monthofregistration_4,monthofregistration_5,monthofregistration_6,
                                    monthofregistration_7,monthofregistration_8,monthofregistration_9,monthofregistration_10,
                                    monthofregistration_11,monthofregistration_12,fueltype_benzin,fueltype_cng,fueltype_diesel,
                                    fueltype_elektro,fueltype_hybrid,fueltype_lpg,notrepaireddamage_1,powerps_bin_2,powerps_bin_3,
                                    powerps_bin_4):
    


    prediction=classifier.predict([[brand,model,yearofregistration,offertype_Gesuch,vehicletype_bus,vehicletype_cabrio,
                                    vehicletype_coupe,vehicletype_kleinwagen,vehicletype_kombi,vehicletype_limousine,
                                    vehicletype_suv,gearbox_manuell,kilometer_10000,kilometer_20000,kilometer_30000,
                                    kilometer_40000, kilometer_50000,kilometer_60000,kilometer_70000,kilometer_80000,
                                    kilometer_90000,kilometer_100000,kilometer_125000,kilometer_150000,monthofregistration_2,
                                    monthofregistration_3,monthofregistration_4,monthofregistration_5,monthofregistration_6,
                                    monthofregistration_7,monthofregistration_8,monthofregistration_9,monthofregistration_10,
                                    monthofregistration_11,monthofregistration_12,fueltype_benzin,fueltype_cng,fueltype_diesel,
                                    fueltype_elektro,fueltype_hybrid,fueltype_lpg,notrepaireddamage_1,powerps_bin_2,powerps_bin_3,
                                    powerps_bin_4]])
    return prediction

def main():
    st.title("Used Car Price Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
      
    #In - 1
    brandlist = {0 : "alfa_romeo",1 : "audi",2 : "bmw",3 : "chevrolet",4 : "chrysler",5 : "citroen",6 : "dacia",7 : "daewoo",
           8 : "daihatsu",9 : "fiat",10 : "ford",11 : "honda",12 : "hyundai",13 : "jaguar",14 : "jeep",15 : "kia",16 : "lada",
           17 : "lancia",18 : "land_rover",19 : "mazda",20 : "mercedes_benz",21 : "mini",22 : "mitsubishi",23 : "nissan",
           24 : "opel",25 : "peugeot",26 : "porsche",27 : "renault",28 : "rover",29 : "saab",30 : "seat",31 : "skoda",32 : "smart",
           33 : "subaru",34 : "suzuki",35 : "toyota",36 : "volkswagen",37 : "volvo"}

    def format_func(option):
        return brandlist[option]

    brand = st.selectbox("Select Car Brand [Type for suggestion]", options=list(brandlist.keys()), format_func=format_func)
    st.write(f"Your car selected brand is {format_func(brand)}")
        
    #In - 2
    modellist = {0 : "100",1 : "145",2 : "147",3 : "156",4 : "159",5 : "1_reihe",6 : "1er",7 : "200",8 : "2_reihe",9 : "300c",10 : "3_reihe",
             11 : "3er",12 : "4_reihe",13 : "500",14 : "5_reihe",15 : "5er",16 : "6_reihe",17 : "6er",18 : "7er",19 : "80",20 : "850",
             21 : "90",22 : "900",23 : "9000",24 : "911",25 : "a1",26 : "a2",27 : "a3",28 : "a4",29 : "a5",30 : "a6",31 : "a8",32 : "a_klasse",
             33 : "accord",34 : "agila",35 : "alhambra",36 : "almera",37 : "altea",38 : "amarok",39 : "antara",40 : "arosa",41 : "astra",
             42 : "auris",43 : "avensis",44 : "aveo",45 : "aygo",46 : "b_klasse",47 : "b_max",48 : "beetle",49 : "berlingo",50 : "bora",
             51 : "boxster",52 : "bravo",53 : "c1",54 : "c2",55 : "c3",56 : "c4",57 : "c5",58 : "c_klasse",59 : "c_max",60 : "c_reihe",
             61 : "caddy",62 : "calibra",63 : "captiva",64 : "carisma",65 : "carnival",66 : "cayenne",67 : "cc",68 : "ceed",69 : "charade",
             70 : "cherokee",71 : "citigo",72 : "civic",73 : "cl",74 : "clio",75 : "clk",76 : "clubman",77 : "colt",78 : "combo",79 : "cooper",
             80 : "cordoba",81 : "corolla",82 : "corsa",83 : "cr_reihe",84 : "croma",85 : "crossfire",86 : "cuore",87 : "cx_reihe",88 : "defender",
             89 : "delta",90 : "discovery",91 : "discovery_sport",92 : "doblo",93 : "ducato",94 : "duster",95 : "e_klasse",96 : "elefantino",
             97 : "eos",98 : "escort",99 : "espace",100 : "exeo",101 : "fabia",102 : "fiesta",103 : "focus",104 : "forester",105 : "forfour",
             106 : "fortwo",107 : "fox",108 : "freelander",109 : "fusion",110 : "g_klasse",111 : "galant",112 : "galaxy",113 : "getz",
             114 : "gl",115 : "glk",116 : "golf",117 : "grand",118 : "i3",119 : "i_reihe",120 : "ibiza",121 : "impreza",122 : "insignia",
             123 : "jazz",124 : "jetta",125 : "jimny",126 : "juke",127 : "justy",128 : "ka",129 : "kadett",130 : "kaefer",131 : "kalina",
             132 : "kalos",133 : "kangoo",134 : "kappa",135 : "kuga",136 : "laguna",137 : "lancer",138 : "lanos",139 : "legacy",140 : "leon",
             141 : "lodgy",142 : "logan",143 : "lupo",144 : "lybra",145 : "m_klasse",146 : "m_reihe",147 : "materia",148 : "matiz",149 : "megane",
             150 : "meriva",151 : "micra",152 : "mii",153 : "modus",154 : "mondeo",155 : "move",156 : "musa",157 : "mustang",158 : "mx_reihe",
             159 : "navara",160 : "niva",161 : "note",162 : "nubira",163 : "octavia",164 : "omega",165 : "one",166 : "outlander",167 : "pajero",  
             168 : "panda",169 : "passat",170 : "phaeton",171 : "picanto",172 : "polo",173 : "primera",174 : "ptcruiser",175 : "punto",176 : "q3",
             177 : "q5",178 : "q7",179 : "qashqai",180 : "r19",181 : "range_rover",182 : "range_rover_evoque",183 : "range_rover_sport",
             184 : "rangerover",185 : "rav",186 : "rio",187 : "roadster",188 : "roomster",189 : "rx_reihe",190 : "s60",191 : "s_klasse",
             192 : "s_max",193 : "s_type",194 : "samara",195 : "sandero",196 : "santa",197 : "scenic",198 : "scirocco",199 : "seicento",
             200 : "serie_2",201 : "sharan",202 : "signum",203 : "sirion",204 : "sl",205 : "slk",206 : "sorento",207 : "spark",208 : "spider",
             209 : "sportage",210 : "sprinter",211 : "stilo",212 : "superb",213 : "swift",214 : "terios",215 : "tigra",216 : "tiguan",
             217 : "toledo",218 : "touareg",219 : "touran",220 : "transit",221 : "transporter",222 : "tt",223 : "tucson",224 : "twingo",
             225 : "up",226 : "v40",227 : "v50",228 : "v60",229 : "v70",230 : "v_klasse",231 : "vectra",232 : "verso",233 : "viano",234 : "vito",
             235 : "vivaro",236 : "voyager",237 : "wrangler",238 : "x_reihe",239 : "x_trail",240 : "x_type",241 : "xc_reihe",242 : "yaris",
             243 : "yeti",244 : "ypsilon",245 : "z_reihe",246 : "zafira"}

    def format_func_2(option):
        return modellist[option]


    model = st.selectbox("Select Car Model [Type for suggestion]", options=list(modellist.keys()), format_func=format_func_2)
    st.write(f"Your selected model is {format_func_2(model)}")
        
    #In - 3
    yearofregistration = st.selectbox("Select Car YoR", options=[1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991,
                 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
                 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018])
    st.write(f"Your selected year is {(yearofregistration)}")
    
        
    #In - 4
    offertype = st.selectbox("Select Type of offer", options=['Offer', 'Request'])
    st.write(f"Your selected offer type is {(offertype)}")
    if(offertype=='Request'):
        offertype_Gesuch=1
    else:
        offertype_Gesuch=0
        
    #In - 5        
    vehicletype = st.selectbox("Select Vehicle Type", options=['Bus', 'Convertible', 'Coupe', 'Hatchback', 'Station Wagon', 
                                                                'limousine', 'SUV', 'Other'])
    st.write(f"Your selected vehicle type is {(vehicletype)}")
    if(vehicletype=='Bus'):
        vehicletype_bus=1
        vehicletype_cabrio=0
        vehicletype_coupe=0
        vehicletype_kleinwagen=0
        vehicletype_kombi=0
        vehicletype_limousine=0
        vehicletype_suv=0
    elif(vehicletype=='Convertible'):
        vehicletype_bus=0
        vehicletype_cabrio=1
        vehicletype_coupe=0
        vehicletype_kleinwagen=0
        vehicletype_kombi=0
        vehicletype_limousine=0
        vehicletype_suv=0
    elif(vehicletype=='Coupe'):
        vehicletype_bus=0
        vehicletype_cabrio=0
        vehicletype_coupe=1
        vehicletype_kleinwagen=0
        vehicletype_kombi=0
        vehicletype_limousine=0
        vehicletype_suv=0
    elif(vehicletype=='Hatchback'):
        vehicletype_bus=0
        vehicletype_cabrio=0
        vehicletype_coupe=0
        vehicletype_kleinwagen=1
        vehicletype_kombi=0
        vehicletype_limousine=0
        vehicletype_suv=0
    elif(vehicletype=='Station Wagon'):
        vehicletype_bus=0
        vehicletype_cabrio=0
        vehicletype_coupe=0
        vehicletype_kleinwagen=0
        vehicletype_kombi=1
        vehicletype_limousine=0
        vehicletype_suv=0
    elif(vehicletype=='limousine'):
        vehicletype_bus=0
        vehicletype_cabrio=0
        vehicletype_coupe=0
        vehicletype_kleinwagen=0
        vehicletype_kombi=0
        vehicletype_limousine=1
        vehicletype_suv=0
    elif(vehicletype=='SUV'):
        vehicletype_bus=0
        vehicletype_cabrio=0
        vehicletype_coupe=0
        vehicletype_kleinwagen=0
        vehicletype_kombi=0
        vehicletype_limousine=0
        vehicletype_suv=1
    else:
        vehicletype_bus=0
        vehicletype_cabrio=0
        vehicletype_coupe=0
        vehicletype_kleinwagen=0
        vehicletype_kombi=0
        vehicletype_limousine=0
        vehicletype_suv=0
            
    #IN - 6
    gearbox = st.selectbox("Select Gear Box Type", options=['Manual', 'Automatic'])
    st.write(f"Your selected gear box type is {(gearbox)}")
    if(gearbox=='Manual'):
        gearbox_manuell=1
    else:
        gearbox_manuell=0

    
    #IN - 7
    kilometer = st.selectbox("Select Number of Kilometers Driven", options=['0-5,000', '5,000-10,000', '10,000-20,000', '20,000-30,000',
                                                                            '30,000-40,000', '40,000-50,000', '50,000-60,000', '60,000-70,000',
                                                                            '70,000-80,000', '80,000-90,000', '90,000-100,000',
                                                                            '100,000-125,000', '125,000-150,000'])
    st.write(f"Your selected Number of Kilometers Driven is {(kilometer)}")
    if(kilometer=='5,000-10,000'):
        kilometer_10000=1
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='10,000-20,000'):
        kilometer_10000=0
        kilometer_20000=1
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='20,000-30,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=1
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='30,000-40,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=1
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='40,000-50,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=1
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='50,000-60,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=1
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='60,000-70,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=1
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='70,000-80,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=1
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='80,000-90,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=1
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='90,000-100,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=1
        kilometer_125000=0
        kilometer_150000=0
    elif(kilometer=='100,000-125,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=1
        kilometer_150000=0
    elif(kilometer=='125,000-150,000'):
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=1
    else:
        kilometer_10000=0
        kilometer_20000=0
        kilometer_30000=0
        kilometer_40000=0
        kilometer_50000=0
        kilometer_60000=0
        kilometer_70000=0
        kilometer_80000=0
        kilometer_90000=0
        kilometer_100000=0
        kilometer_125000=0
        kilometer_150000=0

    
    #IN - 8
    monthofregistration = st.selectbox("Select Month of Registration", options=['January', 'February', 'March', 'April', 'May', 
                                                                                'June','July', 'August', 'September', 'October',
                                                                                'November','December'])
    st.write(f"Your selected Month of Registration is {(monthofregistration)}")
    if(monthofregistration=='February'):
        monthofregistration_2=1
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='March'):
        monthofregistration_2=0
        monthofregistration_3=1
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='April'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=1
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='May'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=1
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='June'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=1
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='July'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=1
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='August'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=1
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='September'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=1
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='October'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=1
        monthofregistration_11=0
        monthofregistration_12=0
    elif(monthofregistration=='November'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=1
        monthofregistration_12=0
    elif(monthofregistration=='December'):
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=1
    else:
        monthofregistration_2=0
        monthofregistration_3=0
        monthofregistration_4=0
        monthofregistration_5=0
        monthofregistration_6=0
        monthofregistration_7=0
        monthofregistration_8=0
        monthofregistration_9=0
        monthofregistration_10=0
        monthofregistration_11=0
        monthofregistration_12=0

    
    #IN - 9
    fueltype = st.selectbox("Select Fuel Type", options=['Petrol', 'CNG', 'Diesel', 'Electric', 'Hybrid', 'LPG','Other'])
    st.write(f"Your selected Fuel Type is {(fueltype)}")
    if(fueltype=='Petrol'):
        fueltype_benzin=1
        fueltype_cng=0
        fueltype_diesel=0
        fueltype_elektro=0
        fueltype_hybrid=0
        fueltype_lpg=0
    elif(fueltype=='CNG'):
        fueltype_benzin=0
        fueltype_cng=1
        fueltype_diesel=0
        fueltype_elektro=0
        fueltype_hybrid=0
        fueltype_lpg=0
    elif(fueltype=='Diesel'):
        fueltype_benzin=0
        fueltype_cng=0
        fueltype_diesel=1
        fueltype_elektro=0
        fueltype_hybrid=0
        fueltype_lpg=0
    elif(fueltype=='Electric'):
        fueltype_benzin=0
        fueltype_cng=0
        fueltype_diesel=0
        fueltype_elektro=1
        fueltype_hybrid=0
        fueltype_lpg=0
    elif(fueltype=='Hybrid'):
        fueltype_benzin=0
        fueltype_cng=0
        fueltype_diesel=0
        fueltype_elektro=0
        fueltype_hybrid=1
        fueltype_lpg=0
    elif(fueltype=='LPG'):
        fueltype_benzin=0
        fueltype_cng=0
        fueltype_diesel=0
        fueltype_elektro=0
        fueltype_hybrid=0
        fueltype_lpg=1
    else:
        fueltype_benzin=0
        fueltype_cng=0
        fueltype_diesel=0
        fueltype_elektro=0
        fueltype_hybrid=0
        fueltype_lpg=0
    
    #IN - 10
    notrepaireddamage = st.radio('Any Pending Repairs?', ['Yes','No'])
    if(notrepaireddamage=='Yes'):
        notrepaireddamage_1 =1
    else:
        notrepaireddamage_1 =0

    
    #IN - 11
    powerps = st.radio('Vehicle Power in PS', ['50-100','100-200','200-300','300+'])
    if(powerps=='100-200'):
        powerps_bin_2=1
        powerps_bin_3=0
        powerps_bin_4=0
    elif(powerps=='200-300'):
        powerps_bin_2=0
        powerps_bin_3=1
        powerps_bin_4=0
    elif(powerps=='300+'):
        powerps_bin_2=0
        powerps_bin_3=0
        powerps_bin_4=1
    else:
        powerps_bin_2=0
        powerps_bin_3=0
        powerps_bin_4=0


    result=""
    if st.button("Predict"):
        result=predict(brand,model,yearofregistration,offertype_Gesuch,vehicletype_bus,vehicletype_cabrio,
                       vehicletype_coupe,vehicletype_kleinwagen,vehicletype_kombi,vehicletype_limousine,
                       vehicletype_suv,gearbox_manuell,kilometer_10000,kilometer_20000,kilometer_30000,
                       kilometer_40000, kilometer_50000,kilometer_60000,kilometer_70000,kilometer_80000,
                       kilometer_90000,kilometer_100000,kilometer_125000,kilometer_150000,monthofregistration_2,
                       monthofregistration_3,monthofregistration_4,monthofregistration_5,monthofregistration_6,
                       monthofregistration_7,monthofregistration_8,monthofregistration_9,monthofregistration_10,
                       monthofregistration_11,monthofregistration_12,fueltype_benzin,fueltype_cng,fueltype_diesel,
                       fueltype_elektro,fueltype_hybrid,fueltype_lpg,notrepaireddamage_1,powerps_bin_2,powerps_bin_3,
                       powerps_bin_4)
    
    st.success('The car can be sold for € {}'.format(result))


if __name__ == '__main__':
    main()