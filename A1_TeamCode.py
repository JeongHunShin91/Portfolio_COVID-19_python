import pandas as pd
import numpy as np
#1번 문제
#파일 불러오기
ex1 = pd.read_csv(r'C:\Users\tj-bu\PycharmProjects\pythonProject1\data\COVID19data\2021\12-31-2020.csv')
#01-01-2021의 나라와 확진자수와 사망자수 뽑아오기
ex1db = ex1[['Country_Region','Confirmed','Deaths']]
#GroupBy 해서 중복되는 나라 Sum해서 통합식
ex12 = ex1db.groupby('Country_Region').sum()
print(ex12)
#파일 불러오기
ex2 = pd.read_csv(r'C:\Users\tj-bu\PycharmProjects\pythonProject1\data\COVID19data\2021\12-31-2021.csv')
#12-31-2021의 나라와 확진자수와 사망자수 뽑아오기
ex2db = ex2[['Country_Region','Confirmed','Deaths']]
#GroupBy 해서 중복되는 나라 Sum해서 통합식
ex22 = ex2db.groupby('Country_Region').sum()
print(ex22)
#1년간 발생한 확진자수와 사망자수 계산식
final = ex22 - ex12
print(final)

#일일 평균 확진자 수 계산식
a1 = final['Confirmed'] // 365
#일일 평균 사망자 수 계산식
a2 = final['Deaths'] // 365
#일일 평균 확진자 수
print(a1)
#일일 평균 사망자 수
print(a2)
#일일 평균 확진자수 행렬 추가
final['dailyConfirmed'] = a1
#일일 평균 사망자수 행렬 추가
final['dailyDeaths'] = a2
#행 추가 되어있는지 확인
final.head()
print(final)
#2번
#값이 None 일때 그 행들 출력
list = final[final["Confirmed"].isnull()];final[final["Deaths"].isnull() ]
print(list)
#값이 None 일때 그 행들 삭제
final = final.dropna()
print(final)
#이 밑은 가장 많은 20위를 추려서 내림차순 한것
final_Confirmed = final['Confirmed'].sort_values(ascending=False)
final_Deaths = final['Deaths'].sort_values(ascending=False)
final_dailyConfirmed = final['dailyConfirmed'].sort_values(ascending=False)
final_dailyDeaths = final['dailyDeaths'].sort_values(ascending=False)
#3번 문제
#일일 감염자수 가장 많은 수로 총 20위까지 내림차순한것
final_dailyConfirmed[:20]
#일일 사망자수 가장 많은 수로 총 20위까지 내림차순한것
final_dailyDeaths[:20]
#1년간의 총 감염자수 가장 많은 수로 총 20위까지 내림차순한것
final_Confirmed[:20]
#1년간의 총 사망자수 가장 많은 수로 총 20위까지 내림차순한것
final_Deaths[:20]

#4번
#1년간 대한민국에서 발생한 총 감염자수 총 사망자수 일일 평균 감염자수 사망자수를 나타내는것
final.loc[['Korea, South'],:]
final.to_csv("final_Covid_Code1.csv", index=True)
