"""
Anonimización obligatoria de todo texto antes de escribir a outbox/.
Sustituye nombres reales por versiones genéricas. Lanza excepción si
aparece un término prohibido.
"""

import re


# Sustituciones seguras (case-insensitive)
SUSTITUCIONES = [
    (r"(?i)\bEuromanager\b", "una consultora de RRHH"),
    (r"(?i)\bCaf[èe]s?\s*Cornell[àa]\b", "una cadena con más de 100 establecimientos de café"),
    (r"(?i)\bOpoRuta\b", "aplicaciones SaaS propias"),
]

# Términos prohibidos — si aparecen, es un error grave
PROHIBIDOS = [
    (r"(?i)\bNOMOS\b", "NOMOS"),
    (r"(?i)\bTelef[oó]nica\b", "Telefónica"),
]


def anonimizar(texto: str) -> str:
    """
    Recibe un texto y:
    1. Lanza excepción si contiene términos prohibidos
    2. Sustituye nombres reales por versiones anónimas
    Devuelve el texto limpio.
    """
    # Primero verificar prohibidos
    for patron, nombre in PROHIBIDOS:
        if re.search(patron, texto):
            raise ValueError(
                f"TÉRMINO PROHIBIDO detectado: '{nombre}'. "
                f"Este texto NO puede salir al exterior. Regenerar sin este término."
            )

    # Aplicar sustituciones
    for patron, reemplazo in SUSTITUCIONES:
        texto = re.sub(patron, reemplazo, texto)

    return texto


def _self_test():
    """Tests básicos de anonimización."""
    # Sustituciones
    assert "consultora de RRHH" in anonimizar("Trabajamos con Euromanager en 2025")
    assert "100 establecimientos" in anonimizar("El caso de Cafès Cornellà fue clave")
    assert "100 establecimientos" in anonimizar("Cafes Cornella también funciona")
    assert "SaaS propias" in anonimizar("He construido OpoRuta desde cero")

    # Prohibidos
    try:
        anonimizar("Proyecto con NOMOS en marcha")
        assert False, "Debería haber lanzado excepción para NOMOS"
    except ValueError as e:
        assert "NOMOS" in str(e)

    try:
        anonimizar("Contrato con Telefónica cerrado")
        assert False, "Debería haber lanzado excepción para Telefónica"
    except ValueError as e:
        assert "Telefónica" in str(e)

    # Texto limpio pasa sin cambios
    texto_limpio = "He automatizado procesos para una cadena de restaurantes"
    assert anonimizar(texto_limpio) == texto_limpio

    print("anonimizar: todos los tests OK")


if __name__ == "__main__":
    _self_test()
