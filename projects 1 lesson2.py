ves_zakaza = 4.5 # 4.5 kg
stoimocti_chereshni = 34 # 34 rub\kg
dengi = 1000
print(dengi-(ves_zakaza*stoimocti_chereshni))

tovar_one = 3 # 3 kg
stoimocti_tone = 30 # 30rub\kg
stoimocti_ttwo = 23 # 23 rub\kg
tovar_two = 6 # 6 kg
print(dengi-((ves_zakaza*stoimocti_chereshni)+(tovar_two*stoimocti_ttwo)+(tovar_one*stoimocti_tone))) #общая сдача
print(tovar_two*stoimocti_ttwo) #чек по 2-му товару (стоимость товара)
print(tovar_one*stoimocti_tone) #чек по 1-му товару (стоимость товара)
print(ves_zakaza*stoimocti_chereshni) # чек по черешне (стоимость товара)