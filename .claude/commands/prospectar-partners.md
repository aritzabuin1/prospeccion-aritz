# /prospectar-partners

Canal complementario al outbound directo. Busca empresas que puedan
convertirse en **partners estratégicos** (agencias, consultoras, gestorías,
integradores) que refieran clientes a cambio de comisión o intercambio.

NO prospecta clientes finales. Para eso está `/prospectar-tanda`.

## Objetivo (alineado con plan-v2-partners-packs.md)

- 10-15 partners candidatos por ejecución
- Ejecutar 1 vez/semana (viernes)
- Meta a 120 días: **70 contactados, 2-3 acuerdos activos, 1 conversación
  avanzada con asociación sectorial**
- Distribución: 25 CFO Copilot + 25 Gestoría IA + 20 HORECA Cockpit

## Alcance

NACIONAL. Prioridad de ciudades por densidad: Madrid, Barcelona, Valencia,
Zaragoza, Sevilla, Málaga, Bilbao, Palma, Las Palmas, Alicante.
NUNCA priorizar partners por proximidad a Bilbao.

## Niveles de partner

- **Nivel 1 — Asociaciones sectoriales:** AECE, AEDAF, FEHR, ENATIC, AEDRH,
  Consejo General Gestores, etc. Ángulo: ponencia gratis + caso anonimizado.
- **Nivel 2 — Partners nacionales:** Holded, Sage, A3, Lightspeed, Lefebvre,
  Grant Thornton, BDO, Auren. Implantadores con >100 clientes.
- **Nivel 3 — Boutique regional:** agencias B2B, consultoras, gestorías,
  despachos. Selección por fit vertical, no por cercanía.

## Pasos

1. Lee `playbook-partners.md` completo para cargar los ángulos de entrada
   por tipo de partner.

2. Lee `config/queries_partners.json` y decide qué tipos de partner
   priorizar en esta ejecución. Si el usuario no especifica, rotar entre
   tiers (tier 1 tiene prioridad: agencias digitales y consultoras).

3. Ejecuta descubrimiento con las queries del tipo elegido:
   - Usar Google Custom Search con las queries del tipo
   - Aplicar exclusiones comunes
   - Obtener 2-3 candidatos por query

4. Para cada candidato, extrae:
   - Nombre empresa
   - Web
   - Tipo (agencia / consultora / gestoría / etc.)
   - Tier (1, 2, 3)
   - Tamaño aproximado (si detectable)
   - Ubicación
   - Motivo de encaje (1 línea: qué hace que esta empresa sea buen partner)

5. Presenta al usuario una tabla:
   ```
   #   Tier  Tipo                Empresa                          Ciudad     Encaje
   ----------------------------------------------------------------------------------------
    1   1    agencia_digital     Quiet Marketing                  Madrid     Clientes B2B tech, piden automatización
    2   1    consultora          Boutique Strategy SL             Bilbao     Transformación en PYMES industriales
    3   2    gestoría            Asesores Ibérica                 Valencia   Cartera 500+ PYMES, oferta servicios
    ...
   ```

6. Pregunta al usuario cuáles quiere contactar. Para los aprobados:
   - Invoca skill `prospeccion` con el dossier adaptado a partner
     (menos profundidad que cliente final, más foco en: tamaño, cartera,
     stack tecnológico, canales comerciales)
   - Genera mensaje T1 usando la plantilla de `playbook-partners.md`
     correspondiente al tipo (agencia / gestoría / consultora / etc.)
   - Guarda en `outbox/{fecha}/partners/{slug}/`:
     * `email-t1.md` + `email-t1.html`
     * `linkedin-paso1.md`
     * `contacto.md`

7. Registra en `data/partners.json` (crear si no existe):
   ```json
   {
     "partners_potenciales": {
       "{slug}": {
         "empresa": "...",
         "tipo": "agencia_digital",
         "tier": 1,
         "ciudad": "...",
         "web": "...",
         "estado": "contactado|respondio|firmado|descartado",
         "fecha_primer_contacto": "YYYY-MM-DD",
         "comision_acordada": null,
         "historial": []
       }
     }
   }
   ```

8. Resumen final:
   ```
   Prospección partners — {fecha}
   Candidatos encontrados: N
   Aprobados para contacto: K
   Mensajes generados en outbox/{fecha}/partners/
   
   Partners totales en pipeline: X
   Activos: Y | En seguimiento: Z
   ```

## Reglas

- NUNCA prometer exclusividad (salvo AI Mate, ya acordado)
- NUNCA citar AI Mate ni otros partners por nombre en mensajes
- NUNCA mencionar clientes finales reales (aplicar `anonimizar.py`)
- El ángulo es **alianza silenciosa**, no subcontratación barata
- Si un partner potencial parece que busca reventa 3x en vez de colaboración
  real, descartar
- Seguimiento: marcar respuestas con `/marcar-respuesta {slug} partner {temperatura}`

## Nota importante sobre AI Mate

Aritz ya trabaja con AI Mate como partner principal. Los clientes actuales
(Euromanager, Viajes de lujo, Cornella) vienen de ese canal. Este comando
**busca partners adicionales** con perfiles complementarios, no reemplaza
la relación con AI Mate.
