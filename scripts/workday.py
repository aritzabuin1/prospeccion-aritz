"""
Utilidad de calendario laboral español.

Reglas:
- Días laborables: lunes a viernes.
- Excluye festivos nacionales de España (librería `holidays`).
- Para prospección, ventanas óptimas por tipo de toque:
    * T1 / Paso2 LinkedIn → lunes a viernes (volumen 80/sem, reparto L-V)
    * T2 reciprocidad    → martes, miércoles, jueves
    * T3 break-up        → martes, miércoles

Si `holidays` no está instalado, degrada elegantemente a solo lun-vie.
"""

import datetime as dt

try:
    import holidays
    ES_HOLIDAYS = holidays.country_holidays("ES")
except ImportError:
    ES_HOLIDAYS = set()


def es_laborable(fecha: dt.date) -> bool:
    """True si `fecha` es lun-vie y no es festivo nacional ES."""
    if fecha.weekday() >= 5:  # 5=sab, 6=dom
        return False
    if fecha in ES_HOLIDAYS:
        return False
    return True


def es_dia_optimo(fecha: dt.date, tipo_toque: str) -> bool:
    """
    Ventanas de envío óptimas por tipo de toque.
    tipo_toque ∈ {"t1", "t2", "t3", "paso2"}
    weekday(): lun=0, mar=1, mié=2, jue=3, vie=4
    """
    if not es_laborable(fecha):
        return False
    wd = fecha.weekday()
    if tipo_toque in ("t1", "paso2"):
        return wd in (0, 1, 2, 3, 4)  # lun-vie (reparto volumen 80/sem)
    if tipo_toque == "t2":
        return wd in (1, 2, 3)  # mar, mié, jue
    if tipo_toque == "t3":
        return wd in (1, 2)  # mar, mié
    return True


def siguiente_dia_optimo(desde: dt.date, tipo_toque: str, max_dias: int = 14) -> dt.date:
    """Primera fecha desde `desde` (inclusive) que sea óptima para ese toque."""
    cursor = desde
    for _ in range(max_dias):
        if es_dia_optimo(cursor, tipo_toque):
            return cursor
        cursor += dt.timedelta(days=1)
    return cursor  # fallback


if __name__ == "__main__":
    hoy = dt.date.today()
    print(f"Hoy {hoy} ({hoy.strftime('%A')}):")
    print(f"  Laborable: {es_laborable(hoy)}")
    for toque in ("t1", "t2", "t3", "paso2"):
        siguiente = siguiente_dia_optimo(hoy, toque)
        print(f"  Siguiente óptimo para {toque}: {siguiente} ({siguiente.strftime('%A')})")
