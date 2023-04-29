import streamlit as st
from streamlit_option_menu import option_menu 

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Perhitungan Analisis Titrimetri',
    ['Hitung Nilai Normalitas',
    'Hitung Nilai Molaritas',
    'Hitung Nilai PPM'],
    default_index=0)
    
# halaman hitung nilai normalitas 
if (selected == 'Hitung Nilai Normalitas') :
    st.title('Hitung Nilai Normalitas')
    
    Massa = st.number_input('Masukan Nilai Massa')
    Volume = st.number_input('Masukan Nilai Volume')
    BE = st.number_input('Masukan Nilai BE')
    
    tombol = st.button('Hitung Nilai Normalitas')
    
    if tombol:
        nilai_normalitas = Massa/(BE*Volume)
        st.success(f'Nilai Normalitas adalah {nilai_normalitas}')
        
# halaman hitung nilai molaritas 
if (selected == 'Hitung Nilai Molaritas') :
    st.title('Hitung Nilai Molaritas')
    
    Massa = st.number_input('Masukan Nilai Massa')
    Volume = st.number_input('Masukan Nilai Volume')
    Mr = st.number_input('Masukan Nilai Mr')
    
    tombol = st.button('Hitung Nilai Molaritas')
    
    if tombol:
        nilai_normalitas = Massa/(Mr*Volume)
        st.success(f'Nilai Normalitas adalah {nilai_Molaritas}')
        
# halaman hitung nilai PPM 
if (selected == 'Hitung Nilai PPM') :
    st.title('Hitung Nilai PPM')
    
    Molaritas Titran = st.number_input('Masukan Nilai Molaritas Titran')
    Volume Titran = st.number_input('Masukan Nilai Volume Titran')
    BM = st.number_input('Masukan Nilai BM')
    Volume Sampel (L) = st.number_input('Masukan Nilai Volume Sampel (L)')
    
    tombol = st.button('Hitung Nilai PPM')
    
    if tombol:
        nilai_PPM = (Molaritas Titran*Volume Titran*BM)/Volume Sampel (L)
        st.success(f'Nilai PPM adalah {nilai_PPM}')