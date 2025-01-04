import streamlit as st

# Judul aplikasi
st.title("Penghitung Debit Air dengan Streamlit")

# Input untuk luas penampang (m^2)
area = st.number_input("Masukkan luas penampang (m²):", value=0.0)

# Input untuk kecepatan aliran (m/s)
velocity = st.number_input("Masukkan kecepatan aliran (m/s):", value=0.0)

# Hitung debit air (Q = A * v)
if st.button("Hitung Debit Air"):
    debit_air = area * velocity
    st.write(f"Debit air: {debit_air} m³/s")
