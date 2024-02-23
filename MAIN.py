# Developer Mavi16
# TÜRKÇE TAKVİM

import calendar # Gereken tek kütüphaneyi çağırıyoruz

yil = int(input("Takvim yılını giriniz: "))
cal=calendar.LocaleTextCalendar(0,"TURKISH") # "TURKISH" yazarak Türkçe diline ayarlıyoruz
cal.pryear(yil)