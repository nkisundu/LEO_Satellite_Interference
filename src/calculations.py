import math

def analyze_interference(satellite, service, criteria="Interference Threshold (dBm)"):
    # Constants
    c = 3e8  # Speed of light (m/s)
    f_hz = satellite.frequency_mhz * 1e6
    d_m = satellite.altitude_km * 1e3

    # Free space path loss (FSPL)
    fspl_db = 20 * math.log10(d_m) + 20 * math.log10(f_hz) - 147.55

    # Received power in dBm
    prx_dbm = satellite.eirp_dbw + 30 + service.rx_gain_dbi - fspl_db

    # Noise power in dBm
    k = -174  # dBm/Hz
    noise_dbm = k + 10 * math.log10(service.bandwidth_mhz * 1e6) + service.noise_figure_db

    result = {
        "Received Power (dBm)": f"{prx_dbm:.2f}",
        "Noise Floor (dBm)": f"{noise_dbm:.2f}",
        "Path Loss (dB)": f"{fspl_db:.2f}"
    }

    if criteria == "Interference Threshold (dBm)":
        interfere = prx_dbm > service.interference_threshold_dbm
    elif criteria == "I/N ratio (dB) < -6 dB":
        i_n_db = prx_dbm - noise_dbm
        result["I/N (dB)"] = f"{i_n_db:.2f}"
        interfere = i_n_db > -6
    elif criteria == "C/I ratio (dB) > 20 dB":
        desired_signal_dbm = noise_dbm + 10
        c_i_db = desired_signal_dbm - prx_dbm
        result["C/I (dB)"] = f"{c_i_db:.2f}"
        interfere = c_i_db < 20
    else:
        interfere = False

    return {
        "interference_detected": interfere,
        "details": result
    }