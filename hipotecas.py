def calcular_pago_hipoteca(monto_prestamo, tasa_interes_anual, plazo_anios):
     """
    Esta función calcula el pago mensual de una hipoteca.
    """
    tasa_interes_mensual = (tasa_interes_anual / 100) / 12
    numero_pagos = plazo_anios * 12
    pago_mensual = (monto_prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -numero_pagos)