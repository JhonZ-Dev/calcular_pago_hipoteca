def calcular_pago_hipoteca(monto_prestamo, tasa_interes_anual, plazo_anios):
    """
    Esta función calcula el pago mensual de una hipoteca.
    """
    tasa_interes_mensual = (tasa_interes_anual / 100) / 12
    numero_pagos = plazo_anios * 12

    pago_mensual = (monto_prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** -numero_pagos)

    return pago_mensual

# Ejemplo de uso:
monto_prestamo = 200000  # $200,000
tasa_interes_anual = 4.5  # 4.5% de tasa de interés anual
plazo_anios = 30  # Plazo de 30 años

pago_mensual = calcular_pago_hipoteca(monto_prestamo, tasa_interes_anual, plazo_anios)
print(f'El pago mensual de la hipoteca es: ${pago_mensual:.2f}')
