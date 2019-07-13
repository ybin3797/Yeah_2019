import pandas as pd
import numpy as np



data_homeless = pd.read_csv('../../LA_Homelessness_Count.csv')
data_homeless.head()

clean_data = pd.DataFrame(columns=('Year', 'Count', 'Latitude', 'Longitude'))
j = 0

data_homeless['Latitude'] = 0
data_homeless['Longitude'] = 0 # 위도, 경도 열 추가

for i in range(len(data_homeless)):

    if data_homeless.loc[i, 'Variable'] == 'Unsheltered Population': # Filtering Unsheltered Population
        location = data_homeless.loc[i, ['Location']].values

        location = str(location[0]).replace('(','')
        location = location.replace(')', '')
        location = location.replace(' ', '')
        location = location.split(',') # 위도, 경도 추출

        # data_homeless에 위도, 경도 열 추가
        data_homeless.loc[i, 'Latitude'] = location[0]
        data_homeless.loc[i, 'Longitude'] = location[1]

        # save data_homeless.loc[i, ['year', 'count', 'lat', 'lot']]
        clean_data.loc[j] = data_homeless.loc[i, ['Year', 'Count', 'Latitude', 'Longitude']]
        j += 1

# save clean_data in 'Unshelterd_Homeless_Population_Data.cav'
clean_data.to_csv('Unshelterd_Homeless_Population_Data.csv', mode='w')