import numpy as np

# ------------------------------------------------------------------------------------------------------------------
# 1. PV configuration of the NEHLA case study
STEP1_PERIOD_min = 15 # time resolution of the planner
STEP2_PERIOD_min = 15 # time resolution of the controller

STEP1_PERIOD_hour = STEP1_PERIOD_min / 60  # (hours)
STEP2_PERIOD_hour = STEP2_PERIOD_min / 60 # (hours)

# ------------------------------------------------------------------------------------------------------------------
# 3. BESS PARAMETERS
# PV_BESS_ratio = 100 # 100 * (BATTERY_CAPACITY / PV_CAPACITY) (%)
# PV_BATTERY_CAPACITY = PV_BESS_ratio / 100 # (kWh)

BATTERY_CAPACITY = 567 # (kWh)
BATTERY_POWER = 250 # (kW)
SOC_INI = 187.5 # (kWh)
SOC_END = SOC_INI # (kWh)

SOC_MAX = 453.6 # (kWh)
SOC_MIN = 113.4 # (kWh)

CHARGE_EFFICIENCY = 0.93 # (%)
DISCHARGE_EFFICIENCY = 0.93 # (%)
CHARGING_POWER = BATTERY_CAPACITY # (kW)
DISCHARGING_POWER = BATTERY_CAPACITY # (kW)
HIGH_SOC_PRICE = 0 # (euros/kWh) Fee to use the BESS

# ------------------------------------------------------------------------------------------------------------------

DE_params = {"DE1_min": 100, # (kW)
             "DE1_max": 750, # (kW)
             "DE1_ramp_up": 800, # (kW)
             "DE1_ramp_down": 800,
             "DE1_reserve_up": 100,
             "DE1_reserve_down": 50,
             "DE1_p_rate": 80}


ES_params = {"capacity": BATTERY_CAPACITY,  # (kWh)
               "soc_min": SOC_MIN,  # (kWh)
               "soc_max": SOC_MAX,  # (kWh)
               "soc_ini": SOC_INI,  # (kWh)
               "soc_end": SOC_END,  # (kWh)
               "charge_eff": CHARGE_EFFICIENCY,  # (/)
               "discharge_eff": DISCHARGE_EFFICIENCY,  # (/)
               "power_min": 0,  # (kW)
               "power_max": BATTERY_POWER}  # (kW)

RG_params = {"PV_min": 0,
             "PV_max": 600,
             "PV_ramp_up": 520,
             "PV_ramp_down": 520,
             "PV_capacity": 600,
             "WT_min": 0,
             "WT_max": 500,
             "WT_ramp_up": 200,
             "WT_ramp_down": 200,
             "WT_cpapacity": 300}

cost_params = {"DE1_a": 0.001,
               "DE1_b": 0.015,
               "DE1_c": 0.059,
               "DE1_m_pos": 0.005,
               "DE1_m_neg": 0.005,
               "ES_m_O&M": 0.0,
               "PV_m_cut_pre": 0.01,
               "WT_m_cut_pre": 0.008,
               "DE1_m_pos_re": 0.02,
               "DE1_m_neg_re": 0.02,
               "ES_m_O&M_re": 0.01,
               "PV_m_cut_re": 0.08,
               "WT_m_cut_re": 0.07,
               "PV_m_cut_cn": 0.005,
               "WT_m_cut_cn": 0.01}

load_params = {"ramp_up": 280,
               "ramp_down": 280}

pwl = {"num": 10}
u_1 = np.ones(96)

PARAMETERS = {}
PARAMETERS["period_hours"] = STEP1_PERIOD_min / 60  # (hours)
PARAMETERS['RG'] = RG_params
PARAMETERS['cost'] = cost_params
PARAMETERS['DE'] = DE_params
PARAMETERS['ES'] = ES_params
PARAMETERS['load'] = load_params
PARAMETERS['PWL'] = pwl
PARAMETERS['u_1'] = u_1
