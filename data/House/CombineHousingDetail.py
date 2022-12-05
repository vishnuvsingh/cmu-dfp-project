import pandas as pd
# def combineList(district):
l=['south_squirrel','north_squirrel','oakland','shadyside']
for i in l:
    path =i+'_info.csv'
    house_list = pd.read_csv(path)
    path1 =i+'_campusdistance.csv'
    distance_list =pd.read_csv(path1)
    merge_house=pd.concat([house_list,distance_list],axis=1)
    del merge_house['name']
    merge_house=merge_house.drop(columns ='Unnamed: 0')
    del merge_house['lat&lng']
    merge_house=merge_house[['address','urls','pics','price','bed','baths','sqFt','policy','distance','drivingtime']]
    result = i+'_final_housing.csv'
    merge_house.to_csv(result)