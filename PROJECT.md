# LLM Wiki — Base de Conocimiento Personal

**Tipo:** knowledge-base personal
**Stack:** Obsidian (visor) + Claude Code (motor LLM) + Markdown
**Deploy:** local (~/vault-kb), abierto como vault en Obsidian

## Autonomía
- ¿Crear/actualizar páginas wiki sin confirmar? Sí
- ¿Modificar archivos en raw/? NUNCA — son inmutables
- ¿Archivar outputs de queries en wiki/analysis/? Sí, previa oferta
- ¿Aplicar fixes de lint automáticamente? Solo si es seguro (enlaces, backlinks). Preguntar para cambios de contenido

## Contexto
Vault inicializado en abril 2026. Sistema basado en el patrón LLM Wiki de Karpathy:
raw sources → wiki compilada por LLM → queries → outputs archivados.

El humano deposita material en raw/ y hace preguntas. El LLM mantiene la wiki.

## Plugins Obsidian necesarios
- Web Clipper (extensión navegador) — destino: raw/web-clips/
- Dataview — consultas sobre frontmatter YAML
- Calendar — navegación de daily notes
- Marp Slides (opcional) — renderizar presentaciones generadas

## Dominio
Aritz es AI Solutions Architect freelance en Bilbao.
Proyectos: OpoRuta (SaaS oposiciones), Cafès Cornellà (reporting+RAG), NOMOS (Telefónica), Club de Remo Estrella (app).
Verticales comerciales: hostelería, dental/estética, fitness.
Contenido: LinkedIn en español, TikTok para OpoRuta.
