import streamlit as st
from src import models, calculations

st.title("LEO Satellite Interference Analysis Tool")

# Satellite Inputs
st.header("Satellite Parameters")
altitude = st.number_input("Altitude (km)", min_value=100.0, value=500.0)
eirp = st.number_input("EIRP (dBW)", value=20.0)
frequency = st.number_input("Frequency (MHz)", value=1950.0)
inclination = st.number_input("Inclination (degrees)", value=53.0)

# Terrestrial Inputs
st.header("Terrestrial Service Parameters")
service_name = st.text_input("Service Name", value="5G")
service_frequency = st.number_input("Service Frequency (MHz)", value=1950.0)
interference_threshold = st.number_input("Interference Threshold (dBm)", value=-125.0)
rx_gain = st.number_input("Receiver Antenna Gain (dBi)", value=0.0)
noise_figure = st.number_input("Receiver Noise Figure (dB)", value=6.0)
bandwidth = st.number_input("Bandwidth (MHz)", value=20.0)

# Interference Criteria
criteria = st.selectbox(
    "Interference Criteria",
    ["Interference Threshold (dBm)", "I/N ratio (dB) < -6 dB", "C/I ratio (dB) > 20 dB"]
)

if st.button("Run Analysis"):
    sat = models.Satellite(altitude, eirp, frequency, inclination)
    service = models.TerrestrialService(service_name, service_frequency,
                                        interference_threshold, rx_gain,
                                        noise_figure, bandwidth)
    result = calculations.analyze_interference(sat, service, criteria)

    st.subheader("Results")
    for k, v in result["details"].items():
        st.write(f"{k}: {v}")

    if result["interference_detected"]:
        st.error("⚠️ Potential for harmful interference DETECTED.")
    else:
        st.success("✅ No harmful interference detected.")