#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSE- 551 FOUNDATION OF ALGORITHMS - HOME WORK ASSIGNMENT 4
Algorithm for computation of max capacity for Flight Scheculing Problem
from Cities LosAngles to Newyork. 
@author: teja
"""

##Import Libraries
import pandas as pd
#################
#Utility function to convert 12hrs to 24 hrs format.
def time12to24hr(t):
    [h,m] = t.strip().split(':')
    
    if m.upper().endswith('AM'):    
        if int(h) > 12 or int(h) < 0:
            raise ValueError("Provide correct time format")
        h = 00 if int(h)==12 else int(h)
        exact_time = (int(h)*60)+int(m[0:2])
        h = int(h)+1 if int(m[0:2])>=30 else int(h) 
        
    elif m.upper().endswith('PM'):
        if int(h) > 12 or int(h) < 0:
            raise ValueError("Provide correct time format")
            
        h = 12 if int(h)==12 else int(h)+12
        exact_time = (int(h)*60)+int(m[0:2])
        h = int(h)+1 if (int(m[0:2])>=30 and int(h)!=23 ) else int(h)
    else :
        if not(0<int(h)<24):
            raise ValueError("Provide correct time format")
        exact_time = (int(h)*60)+int(m[0:2])
        h = int(h)+1 if (int(m[0:2])>=30 and int(h)!=23 ) else int(h)  
    return  (h,exact_time)

#Main Class 
class FlightMaxCapacity : 
    def __init__(self,TimeSpaceDict):
        self.TotalCapacity = 0 # Instance Variable
    # Main method
    def capacity(self):
        count = 0
        while(True) :
          Start="LAX"
          FlightDepartured=0
          FlightArrived=1
          path=[]
          visited_airports=[]
          destination=""
          min_capacity=10000000
          airplane=""
          capacity = 0
          
                  
          for key,values in TimeSpaceDict.items(): 
             if (Start in values["StartLocation"])  and (FlightDepartured==0) and (Start not in visited_airports):
                index = 0               
                for lstitem in values["Start"]  :
                    
                    if Start == lstitem[0] and lstitem[1] not in visited_airports:
                       destination = lstitem[1]
                       capacity= lstitem[2]
                       airplane = lstitem[3]
                       FlightDepartured=1
                       FlightArrived=0 
                       visited_airports.extend([key,index,Start,airplane])
                       path.append(Start) #Building the Augumented Path
                       if capacity < min_capacity : # Ford Fulkerson - calculated min capacity for augumented path.
                           min_capacity = capacity   
                       break
                    index+=1
	               
             if airplane in values["FlightNumbers"] and destination in values["EndLocation"] and FlightArrived==0 and destination!="JFK":
               index=0
               for endListItem in values["End"]:
                  if endListItem[1]==destination and endListItem[3]==airplane and endListItem[1] not in visited_airports:
                    Start = endListItem[1]
                    FlightDepartured=0
                    FlightArrived=1
                    visited_airports.extend([key,index])
                    
                    time_reached=endListItem[4]
                    if (Start in values["StartLocation"])  and (FlightDepartured==0) and (Start not in visited_airports):
                        index = 0
                        for lstitem in values["Start"] :
                             if Start == lstitem[0] and time_reached < lstitem[4] and lstitem[1] not in visited_airports :
                                 destination = lstitem[1]
                                 capacity= lstitem[2]
                                 airplane = lstitem[3]
                                 FlightDepartured=1
                                 FlightArrived=0 
                                 visited_airports.extend([key,index,Start,airplane])
                                 path.append(Start) #Building the Augumented Path
                                 if capacity < min_capacity : # Ford Fulkerson - calculated min capacity for augumented path.
                                     min_capacity = capacity   
                                 break
                             index+=1
                        
                    break
                  index+=1
                    
             if destination == "JFK":
                 self.TotalCapacity+=min_capacity
                 path.append(destination)
                 count +=1
                 i=0
                 cycle=0
                 while i<len(visited_airports):
                   if cycle%2==0:
                      TimeSpaceDict[visited_airports[i]]["Start"][visited_airports[i+1]][2]-=min_capacity
                      if TimeSpaceDict[visited_airports[i]]["Start"][visited_airports[i+1]][2]==0:
                         TimeSpaceDict[visited_airports[i]]["StartLocation"].remove(visited_airports[i+2])
                         TimeSpaceDict[visited_airports[i]]["FlightNumbers"].remove(visited_airports[i+3])
                         TimeSpaceDict[visited_airports[i]]["Start"]=TimeSpaceDict[visited_airports[i]]["Start"][0:visited_airports[i+1]]+TimeSpaceDict[visited_airports[i]]["Start"][visited_airports[i+1]+1:]
                      i=i+4
                   else:
                       TimeSpaceDict[visited_airports[i]]["End"][visited_airports[i+1]][2]-=min_capacity
                       if TimeSpaceDict[visited_airports[i]]["End"][visited_airports[i+1]][2]==0:
                           TimeSpaceDict[visited_airports[i]]["EndLocation"].remove(visited_airports[i+4])
                           TimeSpaceDict[visited_airports[i]]["FlightNumbers"].remove(visited_airports[i-1])
                           TimeSpaceDict[visited_airports[i]]["End"]=TimeSpaceDict[visited_airports[i]]["End"][0:visited_airports[i+1]]+TimeSpaceDict[visited_airports[i]]["End"][visited_airports[i+1]+1:]
                       i=i+2
                   cycle+=1
                 break
                  
          # Remove the nodes if flight to destination is not found      
          if destination!="JFK":
                 if len(visited_airports)==0: 
                      print ("Total Capacity: ",self.TotalCapacity)
                      count=0
                      for keys,values in TimeSpaceDict.items():                
                           count+=len(values["Start"])+len(values["End"])
                      break                  
                 TimeSpaceDict[visited_airports[len(visited_airports)-2]]["EndLocation"].remove(TimeSpaceDict[visited_airports[len(visited_airports)-2]]["End"][visited_airports[len(visited_airports)-1]][1])
                 TimeSpaceDict[visited_airports[len(visited_airports)-2]]["FlightNumbers"].remove(visited_airports[len(visited_airports)-3])
                 TimeSpaceDict[visited_airports[len(visited_airports)-2]]["End"]=TimeSpaceDict[visited_airports[len(visited_airports)-2]]["End"][0:visited_airports[len(visited_airports)-1]]+TimeSpaceDict[visited_airports[len(visited_airports)-2]]["End"][visited_airports[len(visited_airports)-1]+1:]
                 TimeSpaceDict[visited_airports[len(visited_airports)-6]]["StartLocation"].remove(visited_airports[len(visited_airports)-4])
                 TimeSpaceDict[visited_airports[len(visited_airports)-6]]["FlightNumbers"].remove(visited_airports[len(visited_airports)-3])
                 TimeSpaceDict[visited_airports[len(visited_airports)-6]]["Start"]=TimeSpaceDict[visited_airports[len(visited_airports)-6]]["Start"][0:visited_airports[len(visited_airports)-5]]+TimeSpaceDict[visited_airports[len(visited_airports)-6]]["Start"][visited_airports[len(visited_airports)-5]+1:]
if __name__ == "__main__" :
    
    TimeSpaceDict={}
    for hour in range(0,24):
       TimeSpaceDict[hour] = {}
        
    flightCapacity = {'A220':105,'A319':128,'A320':150,'A321':185,"A321neo":196,
                  "A330-200":230,"A330-300":290,"A330-900neo":280,"A350-900":300,
                  "717-200":110,"737-700	":126,"737-800":165,"737-900":180,
                  "737-900ER":180,"737-Max 9":	180,"757-200":180,
                  "757-300":230,"767-300":200,"767-300ER":225,
                  "767-400ER":	240,"777-200":270,"777-200ER":270,
                  "777-200LR":	280,"777-300":	300,"787-8":	235,
                  "787-9":	280,"Embraer 170":72,"Embraer 175 (E 75)":78,
                  "Embraer 190	":100,"McDonnell Douglas MD - 88":	150,
                  "McDonnell Douglas MD - 90-30":	150,"CRJ 700":75,
                  "MD-88":150,"MD-90":150,"CRJ 900":75,"Canadair Regional Jet 900":75,"Canadair Regional Jet 700":75,"Embraer 175":78,"Embraer 175 (Enhanced Winglets)":75,"Embraer E175":78,"757-232":295,"757":295,"CRJ-200":50,"Boeing 717":134,"Bombardier CS100":145}



    for i in range(0,24):
	    TimeSpaceDict[i]["Start"]=[]
	    TimeSpaceDict[i]["End"]=[]
	    TimeSpaceDict[i]["FlightNumbers"]=[]
	    TimeSpaceDict[i]["StartLocation"]=[]
        
	    TimeSpaceDict[i]["EndLocation"]=[]
        
    # Note: Replace the input csv file for the tool
    # Inputs in csv - Start and Destination cities,time and capacity
    try :
      data=pd.read_csv("/Users/teja/Desktop/foa/Hw4_FOA/Final/flight_details.csv")
    except :
         raise ValueError("Make sure the input csv file is valid and path is correct")
    
    flightNumbers = ''
    
    # Constructing the Static Hash table/dictionary Lookups
    # Key values are time components or node for 24 hours time period(0-23) 12.00 am is node 0 and 11.00pm is node 23
    for row in range(0,data.shape[0]):   
	    (StartTime,start_exact_time)= time12to24hr(data.loc[row][2])# Read the start time and convert from 12hrs format to 24 hrs
	    try:
                  if int(data.loc[row][4]):
                      Capacity = data.loc[row][4]
	    except ValueError:
                  for i,value in enumerate(flightCapacity.keys()):
                      if value in data.loc[row][4]:
                          try :
                            Capacity = int(flightCapacity[value])
                          except TypeError :
                             Capacity = 0 
	    TimeSpaceDict[StartTime]["Start"].append([data.loc[row][0],data.loc[row][1],Capacity,data.loc[row][5],start_exact_time])
	    TimeSpaceDict[StartTime]["FlightNumbers"].append(data.loc[row][5])
	    TimeSpaceDict[StartTime]["StartLocation"].append(data.loc[row][0])
	    (ArrivalTime,EndExacttime)= time12to24hr(data.loc[row][3])# Read the arrival time and convert from 12hrs format to 24 hrs    
	    TimeSpaceDict[ArrivalTime]["End"].append([data.loc[row][0],data.loc[row][1],Capacity,data.loc[row][5],EndExacttime])
	    TimeSpaceDict[ArrivalTime]["FlightNumbers"].append(data.loc[row][5])
	    TimeSpaceDict[ArrivalTime]["EndLocation"].append(data.loc[row][1])        

        
	    TimeSpaceDict[StartTime]["FlightNumbers"].append(data.loc[row][5])
    
    FMC= FlightMaxCapacity(TimeSpaceDict)
    FMC.capacity()
    
   
    




    
