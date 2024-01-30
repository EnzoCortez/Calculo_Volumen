# Volumen total del tanque (en metros cúbicos)
volumen_total_tanque = volumen_total

# Volumen en litros (1 metro cúbico = 1000 litros)
volumen_total_litros = volumen_total_tanque * 1000

# Tiempo de llenado al 90% de su capacidad (en segundos)
tiempo_llenado_90_porcentaje = (volumen_total_litros * 0.9) / 10

# Convertir el tiempo de llenado a horas
tiempo_llenado_horas = tiempo_llenado_90_porcentaje / 3600

# Verificar si el volumen total es superior a 45000 litros
if volumen_total_litros > 45000:
    print("El volumen total del tanque es superior a 45000 litros.")

    # Verificar si el tiempo de llenado al 90% de su capacidad es menor a 3 horas
    if tiempo_llenado_horas < 3:
        print("El tiempo de llenado al 90% de su capacidad es menor a 3 horas.")
        print("¡Se recomienda la construcción de los tanques!")
    else:
        print("El tiempo de llenado al 90% de su capacidad es mayor o igual a 3 horas.")
        print("No se recomienda la construcción de los tanques debido al tiempo de llenado demasiado largo.")
else:
    print("El volumen total del tanque es inferior a 45000 litros.")
    print("No se recomienda la construcción de los tanques debido a la capacidad insuficiente.")
