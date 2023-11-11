import streamlit as st

# Ini bagian Heading aplikasi StreamLit
st.title("Kuliah Analisis Big Data") 
st.write("Rania Yasmin")
st.write("# Heading 1")


#Kinerja Unit
st.metric("Kinerja", 40,-1)
st.metric("Response Time", 30, 20)
st.metric("Saham",100,20)

pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write (pilih1)
st.write (pilih2)

makanan= st.radio('Makanan Kesukaan', ['Bakso','Nasi Goreng','Mie Ayam'])
st.write (makanan)

minuman = st.selectbox('Pilih minuman yang akan dipesan', 
            ['Es Teh', 'Kopi', 'Jus'])

st.write (minuman)


bayar = st.multiselect('Bayar Pakai:',
                       ['Tunai', 'Ovo', 'Gopay'])
st.write(bayar)

