


def single_pole_breaker (voltage):
    if 110 <= voltage <= 123:
        return "All Good"
    elif voltage > 123:
        return "Warning...High Voltage Detected"
    else:
        return "Fault"
    

def two_pole_breaker (voltage):
    if 220 <= voltage <= 246:
        return "All Good"
    elif voltage > 240:
        return "Warning...High Voltage Detected"
    else:
        return "Fault"

def single_pole_amperage (amperage):
    if 10.2 <= amperage <= 13:
        return "System Clean, Check your shit though, this is HIGH"
    elif amperage > 13:
        return "Current is high"
    else:
        return "Keeping it low and the savings wild" # have some fun with it here,comment out if boring

def two_pole_amerage (dual_amperage):
    if dual_amperage <= 18:
        return "System Clean, don't panic, it's running"
    elif dual_amperage > 18:
        return "Current is too high"
    else:
        return "Free Breaker??" # change wording or comment out if not needed ;)



def kwh_to_amps(kwh, voltage, hours):
    """
    Converts kWh to Amps.
    Formula: (kWh * 1000) / (Voltage * Hours)
    """
    if hours == 0 or voltage == 0:
        return 0
    amps = (kwh * 1000) / (voltage * hours)
    return amps