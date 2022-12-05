import time
import pandas as pd
from selenium import webdriver
import GoogleAPI #get API function
# using redfin data to collect the distance and the dirvingtime to campus by using Google API
def getResult(place):
    path =place+'_info.csv'
    address_list = pd.read_csv(path)

    result=[]
    result_distance =[]
    result_dringtime=[]
    raw=[]
    output={}
    i=0
    # clean the address format from redfin
    while (i<len(address_list)):

        b=address_list.loc[i]['address'].split(' ')
        if 'Ave' in b :
            result.append(b[0:b.index('Ave')+1])
        elif 'Rd' in b:
            result.append(b[0:b.index('Rd') + 1])
        elif 'St' in b:
            result.append(b[0:b.index('St') + 1])
        elif 'Unit' in b:
            result.append(b[0:b.index('Unit')])
        elif b[-1][0]=='#':
            result.append(b[0:-2])
        else:
            result.append(b)
        i+=1
    #use formate data to get latitude and longtitude
    l=[]
    for i in result:
        temp = i[0]
        for ii in i[1:]:
            temp += '+'+ii
            temp =temp.replace('\n','')
        l_result=[]
        lat=str(GoogleAPI.getlatitude(temp))
        l_result.append(lat)
        time.sleep(1)
        print(temp)
            # print(lat)
        lng=str(GoogleAPI.getlongtidue(temp))
        l_result.append(lng)
        time.sleep(1)
        l.append(l_result)

    # use latitude and longtitude to get driving time and distance to campus
        try:
            raw_data=GoogleAPI.drivingtime_raw(lat, lng)
            raw.append(raw_data)
            time.sleep(1)
            dis=GoogleAPI.campusdistance(lat, lng)
            print(dis)
            result_distance.append(dis)
            time.sleep(1)
            time1=GoogleAPI.campusdringtime(lat,lng)
            print(time1)
            result_dringtime.append(time1)
            time.sleep(1)
        except ConnectionResetError:
            pass

    output['name']=address_list['address'].values.tolist()
    output['lat&lng']=l
    output['distance']=result_distance
    output['drivingtime']=result_dringtime
    final_result = pd.DataFrame(output)
    final_result.to_csv('north_squirrel_campusdistance.csv')
