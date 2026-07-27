# Clubes TED-Ed CRM — Assets

Materiales de onboarding y documentación visual del CRM de **Clubes TED-Ed Argentina (Fundación IQT)**, implementado en monday.com. Todos los HTML son autocontenidos (CSS/JS inline, sin build) y se sirven vía GitHub Pages.

**URL base de GitHub Pages:** https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/

## Assets

| Asset | Archivo | URL |
|---|---|---|
| 🎓 **Intro a Clubes TED-Ed CRM** (todo-en-uno: bienvenida animada + agenda Reunión 27/7 + video intro de 12 escenas + 4 tutoriales interactivos + arquitectura) | `index.html` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/ |
| 🗺️ Pestaña Arquitectura del sistema (versión simple + BPMN técnico) — deep-link directo | `index.html#arq` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/#arq |
| 🗓️ Pestaña Reunión 27/7 (objetivos + agenda con tiempos) — deep-link directo | `index.html#r27` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/#r27 |
| ▶️ Video intro standalone (pantalla completa, para proyectar o grabar) | `intro-clubes-ted-ed-crm.html` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/intro-clubes-ted-ed-crm.html |
| 📚 Índice de tutoriales standalone | `tutoriales-index.html` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/tutoriales-index.html |
| 📍 Tutorial 1 · Básicos de monday en Instituciones | `tutorial-1-basicos-instituciones.html` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/tutorial-1-basicos-instituciones.html |
| 🎫 Tutorial 2 · Tabla Licencias | `tutorial-2-licencias.html` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/tutorial-2-licencias.html |
| 🧑‍🏫 Tutorial 3 · Facilitadores Únicos | `tutorial-3-facilitadores.html` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/tutorial-3-facilitadores.html |
| 💬 Tutorial 4 · Cómo dar feedback | `tutorial-4-feedback.html` | https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/tutorial-4-feedback.html |
| 🗂️ Copia de respaldo del artifact de la Academia | `academia-crm-artifact.html` | — |
| ⚙️ Generador Python de tutoriales standalone | `gen_tutoriales.py` | — |

## Logos

En [`logos/`](logos/):

- `clubes-ted-ed.svg` — lockup Clubes TED-Ed Argentina (full color, para fondos claros; recreación vectorial fiel al brand kit).
- `clubes-ted-ed-blanco.svg` — lockup negativo blanco (para fondos oscuros o rojos).
- `ted-logo.svg` — wordmark oficial TED, re-exportado con el rojo oficial del brand kit de Clubes (`#dd2e26`).
- `hm-systemic-logo.svg` / `.png` — logo de HM Systemic, **Partner Tecnológico de Clubes TED-Ed Argentina** (monocromo `#121212`, fondo transparente; sobre fondos oscuros usar `filter: brightness(0) invert(1)`).

## Diagramas

En [`diagramas/`](diagramas/):

- `bpmn_crm.png` — diagrama BPMN de la arquitectura del CRM (tablas, flujos Make F1–F8, integraciones).
- `bpmn_crm.svg` — versión vectorial (Canva lo acepta como elemento al subirlo).
- `arquitectura-crm-bpmn.drawio` — fuente editable: abrilo gratis en [app.diagrams.net](https://app.diagrams.net) o importalo en Lucidchart (Archivo → Importar). Cada caja y flecha es un objeto.

## Cómo embeber en monday.com

1. En el dashboard o Home del workspace: **Agregar widget → "Insertar todo" (Embed Everything)**.
2. Pegá la URL del asset (por ejemplo la Academia: `https://hernanmelinsky.github.io/Clubes-TED-Ed-CRM-Assets/`).
3. Listo — el contenido queda navegable dentro de monday.

**Deep-links de la Academia:** `#video`, `#t1`…`#t4` y `#arq` abren directo esa pestaña (saltean la ventana de bienvenida). Útil para embeber una sección puntual como widget propio.

## Cómo agregar un asset nuevo

1. Creá el HTML autocontenido (CSS/JS inline; Poppins vía Google Fonts).
2. Subilo a la raíz (o en su carpeta con `index.html` si tiene varios archivos).
3. Sumalo a la tabla de este README con su URL de Pages.

### Branding

Tipografía **Poppins**, títulos EN MAYÚSCULA. Paleta oficial: rojo `#dd2e26` (único rojo permitido), índigo `#2a2765`, celeste `#12c2ec`, amarillo `#ecdb14`, teal `#0a8baa`, azul `#345faa`. Voz en español rioplatense (vos/podés).

---

Clubes TED-Ed Argentina · Fundación IQT · CRM en monday.com
