# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:27:07 2020

@author: 16509
"""
#Question3
#PArt1
mWorldCup= {'Brazil':[1958, 1962, 1970, 1994, 2002],
            'Germany':[1954, 1974, 1990, 2014],
            'Italy':[1934, 1938, 1982, 2006],
            'Argentina':[1978, 1986],
            'France':[1998,2018],
            'England':[1966],
            'Spain':[2010],
            'Uruguay':[1930,1950]}
#Part2
print(mWorldCup['England'])
print(mWorldCup['Italy'])
print(mWorldCup['Brazil'][0])
print(len(mWorldCup['France']))
print(mWorldCup['Germany'][-1])

#PArt3
mWC_Continent= {'sa': {'Brazil':[1958, 1962, 1970, 1994, 2002],
                       'Argentina':[1978, 1986],
                       'Uruguay':[1930,1950]},
                'eur': {'Germany':[1954, 1974, 1990, 2014],
                        'Italy':[1934, 1938, 1982, 2006],
                        'France':[1998,2018],
                        'England':[1966],
                        'Spain':[2010]}}

#PArt4
print("All South American Continents", mWC_Continent['sa'])
print("Spain Winning Years", mWC_Continent['eur']['Spain'])
print("Argentia World Cup Years", mWC_Continent['sa']['Argentina'])


UruguayYears= mWC_Continent['sa']['Uruguay']
print('UruguayYears',UruguayYears)


                




