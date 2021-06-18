from flask import Flask, request
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn

app=Flask(__name__)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welocme to used car price prediction"

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print("Entered if loop of predict method")
        
        #In - 1
        brand = request.args.get('brand')
        print(brand)
        
        #In - 2
        model = request.args.get('model')
        print(model)
        
        #In - 3
        yearofregistration = request.args.get('yearofregistration')
        print(yearofregistration)
        
        #In - 4
        offertype = request.args.get('offertype')
        if(offertype=='Request'):
            offertype_Gesuch=1
        else:
            offertype_Gesuch=0
        print(offertype)   
        print(offertype_Gesuch)
        
        #In - 5        
        vehicletype = request.args.get('vehicletype')
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
        print(vehicletype)
        print(vehicletype_bus)
        print(vehicletype_cabrio)
        print(vehicletype_coupe)
        print(vehicletype_kleinwagen)
        print(vehicletype_kombi)
        print(vehicletype_limousine)
        print(vehicletype_suv)
                
        #IN - 6
        gearbox = request.args.get('gearbox')
        if(gearbox=='Manual'):
            gearbox_manuell=1
        else:
            gearbox_manuell=0
        print(gearbox)
        print(gearbox_manuell)
        
        #IN - 7
        kilometer = request.args.get('kilometer')
        if(kilometer=='<10,000'):
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
        print(kilometer)
        print(kilometer_10000)
        print(kilometer_20000)
        print(kilometer_30000)
        print(kilometer_40000)
        print(kilometer_50000)
        print(kilometer_60000)
        print(kilometer_70000)
        print(kilometer_80000)
        print(kilometer_90000)
        print(kilometer_100000)
        print(kilometer_125000)
        print(kilometer_150000)
        
        #IN - 8
        monthofregistration = request.args.get('monthofregistration')
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
        print(monthofregistration)
        print(monthofregistration_2)
        print(monthofregistration_3)
        print(monthofregistration_4)
        print(monthofregistration_5)
        print(monthofregistration_6)
        print(monthofregistration_7)
        print(monthofregistration_8)
        print(monthofregistration_9)
        print(monthofregistration_10)
        print(monthofregistration_11)
        print(monthofregistration_12)
        
        #IN - 9
        fueltype = request.args.get('fueltype')
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
        print(fueltype)
        print(fueltype_benzin)
        print(fueltype_cng)
        print(fueltype_diesel)
        print(fueltype_elektro)
        print(fueltype_hybrid)
        print(fueltype_lpg)
        
        #IN - 10
        notrepaireddamage = request.args.get('notrepaireddamage')
        if(notrepaireddamage=='Yes'):
            notrepaireddamage_1 =1
        else:
            notrepaireddamage_1 =0
        print(notrepaireddamage)
        print(notrepaireddamage_1)
        
        #IN - 11
        powerps = request.args.get('powerps')
        if(powerps=='100-200'):
            powerps_bin_2=1
            powerps_bin_3=0
            powerps_bin_4=0
        elif(powerps=='200-300'):
            powerps_bin_2=0
            powerps_bin_3=1
            powerps_bin_4=0
        elif(powerps=='300-350'):
            powerps_bin_2=0
            powerps_bin_3=0
            powerps_bin_4=1
        else:
            powerps_bin_2=0
            powerps_bin_3=0
            powerps_bin_4=0
        print(powerps)
        print(powerps_bin_2)
        print(powerps_bin_3)
        print(powerps_bin_4)
            
        #Prediction
        print("Predicting")
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
        print("Rounding off the numbers")
        output=round(prediction[0],2)
        print("Done")
        return "The Predicted Value is €"+ str(output)
              
    else:
        return "Inspect Error"

if __name__ == '__main__':
    app.run()