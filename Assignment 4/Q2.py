cities = {'karachi':{'country':'Pakistan','Population':'1M','fact':'City of Lights'},'mumbai':{'country':'India','Population':'12M','fact':'Big'},'Islamabad':{'country':'Pakistan','Population':'1M','fact':'Capital'}}

for key in cities.keys():
    print(key)

    for keys,vals in cities[key].items():
        print(keys,vals)