import streamlit as st
import math

ev_fiyat = st.number_input("Ev fiyatı", 1250000)
kira = st.number_input("Kira", 8000)
isim = st.text_input("İsminiz", "Hakan")
birikim = st.number_input("Birikim", 3000)
kredi_süresi = st.number_input("Kredi süresi (yıl)", 15)
peşinat_oranı = st.number_input("Peşinat oranı (%)", 20)

peşinat = ev_fiyat * (peşinat_oranı / 100)
kredi_tutarı = ev_fiyat - peşinat
kredi_taksiti = kredi_tutarı / (kredi_süresi * 12)

kira_gelir_grafisi = st.line_chart(data=[[0, 0], [65, kira * (ev_fiyat / birikim - kredi_taksiti / birikim)]])

kredi_borcu_geri_odeme_grafisi = st.line_chart(data=[[0, kredi_tutarı], [65, 0]])

birikim_yuvarla = math.floor(ev_fiyat / birikim)

st.write("**Sonuç**")
st.write(f"{isim}, 25 yaşından 65 yaşına kadar her ay {birikim} TL birikim yaptığında, 65 yaşına geldiğinde {birikim_yuvarla} daire satın alabilir. Bu dairelerden elde edeceği kira geliri ise {birikim_yuvarla} daire * {kira} TL = {kira * birikim_yuvarla} TL'dir.")
