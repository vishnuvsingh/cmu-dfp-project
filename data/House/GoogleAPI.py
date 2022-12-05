import requests
import json
# different methonds by using Google API to get reuqired data

#use formate data to get latitude
def getlatitude(temp):
 url = "https://maps.googleapis.com/maps/api/geocode/json?address="+temp+",+Pittsburgh,+PA&key=AIzaSyDpmHRoPWTuKXXMW1evCYp8zO2Ao3yvKmY"

 payload = {}
 headers = {}

 response = requests.request("GET", url, headers=headers, data=payload)
 all=[]
 lat =[]
 lng=[]
 response_dict=json.loads(response.text)
 response_dict =response_dict['results'][0]
 return response_dict['geometry']['location']['lat']
# use formate data to get  longtitude
def getlongtidue(temp):
 url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + temp + ",+Pittsburgh,+PA&key=AIzaSyDpmHRoPWTuKXXMW1evCYp8zO2Ao3yvKmY"

 payload = {}
 headers = {}

 response = requests.request("GET", url, headers=headers, data=payload)
 all = []
 lat = []
 lng = []
 response_dict = json.loads(response.text)
 response_dict = response_dict['results'][0]
 return response_dict['geometry']['location']['lng']

Campus_address='carnegie+mellon+university'
campus_latitude=str(getlatitude(Campus_address))
campus_longtitue=str(getlongtidue(Campus_address))

def nearbysupermarket(lat,lng):
 url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+lat+"%2C"+lng+"&radius=2500&type=supermarket&key=AIzaSyDpmHRoPWTuKXXMW1evCYp8zO2Ao3yvKmY"

 payload = {}
 headers = {}

 response = requests.request("GET", url, headers=headers, data=payload)

 response_dict = json.loads(response.text)
 response_dict = response_dict['results']

 for i in response_dict:
  print(i['name'])
  if 'rating' in i.keys():
   print(i['name']+"rating is " +i['rating'])
  else:
   print(i['name'] +" has no rating information")
  if 'price_level' in i.keys():
   print(i['name']+"price level is "+i['price_level'])
  else:
   print(i['name']+"has no price_level information")
#use latitude and longtitude to get distance between home and campus
def campusdistance(lat,lng):
 Campus_address='carnegie+mellon+university'
 campus_latitude=str(getlatitude(Campus_address))
 campus_longtitue=str(getlongtidue(Campus_address))
 url ="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+lat+"%2C"+lng+"&destinations="+campus_latitude+"%2C"+campus_longtitue+"&key=AIzaSyDpmHRoPWTuKXXMW1evCYp8zO2Ao3yvKmY"

 payload={}
 headers = {}
 response = requests.request("GET", url, headers=headers, data=payload)
 dic=json.loads(response.text)
 info = dic['rows'][0]['elements'][0]
 response.close()
 return info['distance']['text']

#use latitude and longtitude to get drivingtime between home and campus
def campusdringtime(lat,lng):

 url ="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+lat+"%2C"+lng+"&destinations="+campus_latitude+"%2C"+campus_longtitue+"&key=AIzaSyDpmHRoPWTuKXXMW1evCYp8zO2Ao3yvKmY"

 payload={}
 headers = {}
 response = requests.request("GET", url, headers=headers, data=payload)
 dic=json.loads(response.text)
 info = dic['rows'][0]['elements'][0]
 response.close()
 return info['duration']['text']

def drivingtime_raw(lat,lng):
 url ="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+lat+"%2C"+lng+"&destinations="+campus_latitude+"%2C"+campus_longtitue+"&key=AIzaSyDpmHRoPWTuKXXMW1evCYp8zO2Ao3yvKmY"

 payload = {}
 headers = {}
 response = requests.request("GET", url, headers=headers, data=payload)
 return str(response.text)