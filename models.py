class Satellite:
    def __init__(self, altitude_km, eirp_dbw, frequency_mhz, inclination_deg):
        self.altitude_km = altitude_km
        self.eirp_dbw = eirp_dbw
        self.frequency_mhz = frequency_mhz
        self.inclination_deg = inclination_deg


class TerrestrialService:
    def __init__(self, name, frequency_mhz, interference_threshold_dbm,
                 rx_gain_dbi=0.0, noise_figure_db=6.0, bandwidth_mhz=20.0):
        self.name = name
        self.frequency_mhz = frequency_mhz
        self.interference_threshold_dbm = interference_threshold_dbm
        self.rx_gain_dbi = rx_gain_dbi
        self.noise_figure_db = noise_figure_db
        self.bandwidth_mhz = bandwidth_mhz