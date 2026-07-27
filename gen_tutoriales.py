# -*- coding: utf-8 -*-
"""Genera tutoriales HTML interactivos de Clubes TED-Ed CRM con estilo compartido."""
import json, os

OUT = os.path.dirname(os.path.abspath(__file__))

TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — TUTORIAL CRM CLUBES TED-ED</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<style>
:root{{--rojo:#dd2e26;--indigo:#2a2765;--celeste:#12c2ec;--amarillo:#ecdb14;--teal:#0a8baa;--azul:#345faa}}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif}}
body{{background:#f4f4f8;color:var(--indigo);min-height:100vh}}
header{{background:var(--rojo);color:#fff;padding:26px 6vw;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}}
.lockup{{display:flex;align-items:center;gap:12px}}
.lockup .sq{{background:#fff;color:var(--rojo);font-weight:800;border-radius:10px;padding:6px 12px;font-size:.9rem}}
.lockup span{{font-weight:600;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase}}
header h1{{font-weight:800;text-transform:uppercase;font-size:clamp(1.1rem,2.6vw,1.7rem);width:100%}}
header .meta{{font-weight:300;font-style:italic;font-size:.85rem}}
a.back{{color:#fff;font-weight:600;font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;text-decoration:none;border:1.5px solid rgba(255,255,255,.6);border-radius:999px;padding:6px 16px}}
main{{max-width:860px;margin:0 auto;padding:34px 5vw 90px}}
#dots{{display:flex;gap:8px;justify-content:center;margin-bottom:26px;flex-wrap:wrap}}
.dot{{width:34px;height:6px;border-radius:3px;background:#d8d8e4;cursor:pointer;transition:.25s}}
.dot.done{{background:var(--celeste)}} .dot.cur{{background:var(--rojo)}}
.card{{background:#fff;border-radius:20px;box-shadow:0 10px 34px rgba(42,39,101,.1);padding:34px;display:none;animation:in .45s ease}}
.card.active{{display:block}}
@keyframes in{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:none}}}}
.card .stepno{{font-weight:600;font-style:italic;letter-spacing:.25em;font-size:.7rem;color:var(--teal);text-transform:uppercase}}
.card h2{{font-weight:700;text-transform:uppercase;font-size:clamp(1.15rem,2.4vw,1.55rem);margin:6px 0 14px}}
.card p{{font-weight:300;font-size:1rem;line-height:1.65;margin-bottom:12px}}
.card p b{{font-weight:600}}
.action{{background:#fdf7d9;border-left:5px solid var(--amarillo);border-radius:0 14px 14px 0;padding:16px 20px;margin:18px 0}}
.action .tag{{font-weight:700;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:#a08c00}}
.action p{{margin:6px 0 0;font-weight:400}}
.tip{{background:#e2f7fd;border-left:5px solid var(--celeste);border-radius:0 14px 14px 0;padding:14px 20px;margin:14px 0}}
.tip .tag{{font-weight:700;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--teal)}}
.tip p{{margin:6px 0 0;font-weight:400;font-size:.92rem}}
.warn{{background:#fdeceb;border-left:5px solid var(--rojo)}}
.warn .tag{{color:var(--rojo)}}
.check{{display:flex;align-items:flex-start;gap:12px;padding:10px 0;cursor:pointer}}
.check input{{width:20px;height:20px;accent-color:var(--rojo);margin-top:2px}}
.check span{{font-weight:400;font-size:.98rem;line-height:1.5}}
nav.paginate{{display:flex;justify-content:space-between;margin-top:26px;gap:12px}}
button.nv{{background:var(--indigo);color:#fff;border:none;border-radius:999px;padding:12px 30px;font-weight:600;
  font-size:.85rem;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;transition:.2s}}
button.nv:hover{{background:var(--rojo)}} button.nv:disabled{{opacity:.25;cursor:default}}
.quiz-q{{font-weight:600;margin:16px 0 10px}}
.opt{{display:block;width:100%;text-align:left;background:#f4f4f8;border:2px solid transparent;border-radius:12px;
  padding:12px 16px;margin-bottom:8px;font-size:.95rem;cursor:pointer;font-weight:400;transition:.2s}}
.opt:hover{{border-color:var(--celeste)}}
.opt.ok{{background:#e5f8e9;border-color:#2e9e4f;font-weight:600}}
.opt.bad{{background:#fdeceb;border-color:var(--rojo)}}
.done-banner{{display:none;background:var(--indigo);color:#fff;border-radius:16px;padding:22px;text-align:center;margin-top:18px}}
.done-banner b{{color:var(--amarillo);text-transform:uppercase}}
footer{{text-align:center;padding:18px;font-weight:300;font-size:.75rem;color:#8b8ba5}}
</style>
</head>
<body>
<header>
  <div class="lockup"><div class="sq">CLUBES TED-Ed</div><span>Argentina</span></div>
  <a class="back" href="tutoriales-index.html">← Todos los tutoriales</a>
  <h1>{title}</h1>
  <div class="meta">{subtitle} · ⏱ {mins} min</div>
</header>
<main>
  <div id="dots"></div>
  {cards}
</main>
<footer>Clubes TED-Ed Argentina · Fundación IQT · CRM en monday.com</footer>
<script>
const cards=[...document.querySelectorAll('.card')],dots=document.getElementById('dots');
let cur=0;
cards.forEach((c,k)=>{{const d=document.createElement('div');d.className='dot';d.onclick=()=>go(k);dots.appendChild(d)}});
function go(n){{cur=Math.max(0,Math.min(cards.length-1,n));
  cards.forEach((c,k)=>c.classList.toggle('active',k===cur));
  [...dots.children].forEach((d,k)=>{{d.className='dot'+(k<cur?' done':k===cur?' cur':'')}});
  window.scrollTo({{top:0,behavior:'smooth'}});}}
function quiz(btn,ok){{const sib=[...btn.parentElement.querySelectorAll('.opt')];
  sib.forEach(b=>b.disabled=true);
  btn.classList.add(ok?'ok':'bad');
  if(!ok) sib.find(b=>b.dataset.ok==='1').classList.add('ok');
  const done=btn.closest('.card').querySelector('.done-banner');
  if(done && [...btn.closest('.card').querySelectorAll('.opt.ok')].length>= +done.dataset.need) done.style.display='block';
}}
go(0);
</script>
</body>
</html>"""

CARD = """<section class="card">
  <div class="stepno">Paso {n} de {total}</div>
  <h2>{h}</h2>
  {body}
  <nav class="paginate">
    <button class="nv" onclick="go(cur-1)" {prevdis}>← Anterior</button>
    <button class="nv" onclick="go(cur+1)" {nextdis}>{nextlabel}</button>
  </nav>
</section>"""

def p(t): return f"<p>{t}</p>"
def action(t): return f'<div class="action"><div class="tag">✋ Hacelo vos</div><p>{t}</p></div>'
def tip(t): return f'<div class="tip"><div class="tag">💡 Tip</div><p>{t}</p></div>'
def warn(t): return f'<div class="tip warn"><div class="tag">⚠️ Importante</div><p>{t}</p></div>'
def checks(items):
    return "".join(f'<label class="check"><input type="checkbox"><span>{i}</span></label>' for i in items)
def quiz(qs):
    html, need = "", 0
    for q, opts in qs:
        need += 1
        html += f'<div class="quiz-q">{q}</div>'
        for txt, ok in opts:
            flag = "1" if ok else "0"
            html += f'<button class="opt" data-ok="{flag}" onclick="quiz(this,{str(ok).lower()})">{txt}</button>'
    html += f'<div class="done-banner" data-need="{need}">🎉 <b>¡Tutorial completado!</b><br>Ya podés aplicarlo en el CRM. Ante dudas, consultá el Diccionario o mandá tu pregunta por el formulario de feedback.</div>'
    return html

def build(fname, title, subtitle, mins, steps):
    total = len(steps)
    cards = ""
    for k, (h, body) in enumerate(steps):
        cards += CARD.format(n=k+1, total=total, h=h, body=body,
            prevdis="disabled" if k==0 else "",
            nextdis="disabled" if k==total-1 else "",
            nextlabel="Siguiente →" if k<total-1 else "Fin")
    html = TEMPLATE.format(title=title, subtitle=subtitle, mins=mins, cards=cards)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("OK", fname)

# ---------- TUTORIAL 1: BÁSICOS DE MONDAY EN INSTITUCIONES ----------
build("tutorial-1-basicos-instituciones.html",
"BÁSICOS DE MONDAY EN LA TABLA INSTITUCIONES",
"Tu primera vuelta por el CRM", 8, [
("¿Qué es la tabla Instituciones?",
 p("Es el corazón del CRM: <b>1.729 escuelas</b> con clubes activos, geocodificadas y organizadas por provincia, hub, año y tipo de gestión.")+
 p("Cada <b>fila es un elemento</b> (una institución) y cada <b>columna</b> guarda un tipo de dato: texto, estado, ubicación, personas, vínculos a otras tablas.")+
 action("Entrá a monday con tus credenciales y abrí la tabla <b>Instituciones</b> desde el Home del CRM.")+
 tip("Si es tu primera vez, integrá tu email desde tu perfil para que tus comunicaciones queden registradas.")),
("La ficha de un elemento",
 p("Al hacer clic en el nombre de una institución se abre su <b>ficha</b>: todos sus datos, sus actualizaciones, emails y actividades, y sus vínculos con Licencias y Videos.")+
 action("Abrí la ficha de cualquier institución y recorré las pestañas: <b>Actualizaciones</b>, <b>Emails y Actividades</b> y <b>Registro de actividad</b>.")+
 tip("El historial de versiones guarda todo: si algo se cambió por error, se puede recuperar.")),
("Filtrar, agrupar, ocultar y buscar",
 p("Arriba de la tabla tenés las herramientas para ver <b>solo lo que necesitás</b>:")+
 checks([
   "<b>Buscar:</b> escribí el nombre de una escuela en la lupa.",
   "<b>Filtros:</b> filtrá por provincia, hub o año. Probá «Provincia = Córdoba».",
   "<b>Agrupar:</b> agrupá por tipo de gestión y mirá cómo se reorganiza la tabla.",
   "<b>Ocultar:</b> escondé las columnas que no uses (no se borran, solo se ocultan).",
   "<b>Persona:</b> filtrá por responsable con el ícono de personas."])+
 tip("Marcá cada casilla a medida que lo pruebes en el CRM.")),
("Las vistas",
 p("Una <b>vista</b> es una configuración guardada de filtros, agrupamientos y columnas. La tabla tiene la <b>Tabla Principal</b> y la vista <b>2026 x Hub</b>, y se pueden crear más.")+
 action("Cambiá entre «Tabla Principal» y «2026 x Hub» desde las pestañas superiores y notá la diferencia.")+
 warn("Modificar una vista compartida la cambia para todo el equipo. Si querés experimentar, creá tu propia vista y dale tu nombre.")),
("Permisos: qué podés tocar y qué no",
 p("Todos pueden <b>ver, agregar y modificar elementos y fichas</b>, y crear vistas. Lo que queda reservado a admin:")+
 checks([
   "Crear o modificar <b>columnas</b>.",
   "Hacer <b>importaciones masivas</b>.",
   "Editar campos <b>sincronizados con Educabot</b> (ID Educabot y datos de sync)."])+
 warn("Educabot es la fuente de verdad: si un dato sincronizado está mal, no lo corrijas a mano — reportalo por el formulario de feedback.")),
("Poné a prueba lo aprendido",
 quiz([
   ("¿Qué pasa si edito a mano un campo sincronizado con Educabot?",
    [("Nada, se guarda para siempre", False),
     ("La sincronización lo puede pisar y puedo romper el flujo — mejor reportarlo", True),
     ("Se actualiza también en Educabot", False)]),
   ("Quiero ver solo las escuelas de mi hub en 2026. ¿Qué uso?",
    [("Borro las demás filas", False),
     ("La vista «2026 x Hub» o un filtro por hub", True),
     ("Pido un Excel exportado", False)]),
 ])),
])

# ---------- TUTORIAL 2: LICENCIAS ----------
build("tutorial-2-licencias.html",
"TABLA LICENCIAS: UN CLUB POR CICLO",
"Entender el registro histórico del programa", 6, [
("¿Qué es una licencia?",
 p("Cada fila de la tabla Licencias es <b>un club en un ciclo académico</b>. Hay <b>6.142 licencias</b> entre 2022 y 2026.")+
 p("El <b>nombre del elemento es el ID de Educabot</b>: es la clave de sincronización y no se edita.")+
 action("Abrí la tabla <b>Licencias</b> y ordená por ciclo académico para ver la evolución del programa.")),
("Columnas y vinculaciones",
 p("Además de los datos propios del club, cada licencia tiene dos vínculos clave:")+
 checks([
   "<b>Institución:</b> la escuela donde funciona el club.",
   "<b>Facilitadores Únicos:</b> las personas que lo llevan adelante."])+
 action("Desde una licencia, hacé clic en la institución vinculada: saltás directo a su ficha sin buscarla.")+
 tip("Las vinculaciones funcionan en ambos sentidos: desde la institución también ves todas sus licencias.")),
("¿Qué datos encuentro acá?",
 checks([
   "Historial de clubes de una escuela a través de los años.",
   "Estado de cada licencia en el ciclo actual.",
   "Qué facilitadores tuvo cada club.",
   "Cortes por ciclo académico para reportes."])+
 tip("¿Cuántos clubes tuvo una escuela desde 2022? Abrí la ficha de la institución y contá sus licencias vinculadas.")),
("Automatizaciones y sincro",
 p("La tabla se actualiza sola: el flujo <b>F2 de Make</b> sincroniza las licencias desde Educabot. Las automatizaciones de monday avisan cambios de estado y mantienen ordenado el tablero.")+
 warn("No edites el nombre del elemento (ID Educabot) ni los campos de sincronización: son la clave que une el CRM con Educabot.")),
("Repaso rápido",
 quiz([
   ("Una escuela participó en 2023, 2024 y 2025. ¿Cuántas licencias tiene?",
    [("Una sola que se actualiza", False),
     ("Tres: una por ciclo académico", True),
     ("Depende de cuántos facilitadores tuvo", False)]),
   ("¿Qué representa el nombre de cada elemento en Licencias?",
    [("El nombre de la escuela", False),
     ("El ID de Educabot — la clave de sync, no se toca", True),
     ("Un número interno de monday", False)]),
 ])),
])

# ---------- TUTORIAL 3: FACILITADORES ÚNICOS ----------
build("tutorial-3-facilitadores.html",
"FACILITADORES ÚNICOS: UNA PERSONA, UNA FILA",
"DNI, idFac y subitems sin misterios", 6, [
("El tablero maestro de personas",
 p("Facilitadores Únicos tiene <b>4.646 personas</b>: <b>una fila por DNI</b>. Es el maestro de todas las personas que facilitaron clubes.")+
 p("Ojo: el <b>idFac no es único por persona</b>. Una misma persona puede tener varios idFac, uno por cada ciclo en que participó. Todos se acumulan en su fila.")+
 action("Buscá un facilitador por nombre o DNI y abrí su ficha.")),
("Los subitems: una inscripción por licencia",
 p("Dentro de cada persona vas a ver <b>subitems</b>: cada uno es <b>una inscripción a una licencia</b>. Así, la historia completa de la persona vive en un solo lugar.")+
 action("Expandí los subitems de un facilitador con varios ciclos y mirá sus inscripciones año a año.")+
 tip("¿Un facilitador aparece dos veces? Probablemente sea un DNI mal cargado en origen — reportalo por el formulario.")),
("Vinculaciones",
 checks([
   "<b>Licencias:</b> los clubes en los que participó.",
   "<b>Instituciones:</b> a través de las licencias, las escuelas por las que pasó.",
   "<b>Historial de comunicación:</b> emails y actividades registradas con esa persona."])+
 tip("Para contactar a los facilitadores activos de un hub: filtrá por ciclo 2026 y hub, y usá esa selección.")),
("Sincro y cuidado de los datos",
 p("El flujo <b>F3 de Make</b> alimenta este tablero desde Educabot: crea inscripciones, actualiza el maestro y genera los subitems.")+
 warn("Los campos idFac y DNI son claves de matching. Si ves un dato de identidad mal, no lo edites: reportalo para corregirlo en la fuente.")),
("Repaso rápido",
 quiz([
   ("Una persona facilitó en 2023 y 2026. En Facilitadores Únicos tiene…",
    [("Dos filas, una por año", False),
     ("Una fila con dos subitems (una inscripción por licencia)", True),
     ("Una fila por cada idFac", False)]),
   ("¿El idFac identifica de forma única a una persona?",
    [("Sí, siempre", False),
     ("No: la clave de persona es el DNI; puede haber varios idFac", True),
     ("Solo en el ciclo 2026", False)]),
 ])),
])

# ---------- TUTORIAL 4: CÓMO DAR FEEDBACK ----------
build("tutorial-4-feedback.html",
"CÓMO DAR FEEDBACK Y PEDIR AYUDA",
"Tu opinión construye el CRM", 4, [
("Un solo canal: el formulario",
 p("Todas las consultas, ideas y reportes de errores entran por el <b>formulario de feedback</b>. Así nada se pierde en chats o mails sueltos.")+
 action("Guardá el link del formulario en favoritos. Al enviarlo, recibís <b>confirmación y respuesta</b>.")+
 tip("¿Encontraste un dato raro (duplicado, campo mal sincronizado)? También va por el formulario — no lo corrijas a mano si es un campo de sync.")),
("La tabla de feedback: votá y comentá",
 p("Todo lo enviado cae en una <b>tabla de feedback</b> visible para el equipo. Antes de proponer algo, revisá si alguien ya lo pidió: podés <b>votarlo o comentarlo</b> para sumarle fuerza.")+
 action("Entrá a la tabla de feedback, buscá una propuesta que te interese y dejá tu voto o comentario.")),
("Los plazos",
 checks([
   "<b>2 semanas</b> de ventana para preguntas y mejoras rápidas.",
   "Próxima reunión de equipo: <b>semana del 10/8/26</b>.",
   "Mientras tanto: explorá el CRM, probá los tutoriales y anotá todo lo que te haga ruido."])+
 tip("¿Querés empezar a relevar algo que hoy no está en el sistema? Proponelo por el formulario y lo definimos entre todos dónde va.")),
("Repaso rápido",
 quiz([
   ("Encontré una institución con la provincia mal sincronizada. ¿Qué hago?",
    [("La corrijo a mano en la tabla", False),
     ("La reporto por el formulario de feedback", True),
     ("Le mando un mail a todo el equipo", False)]),
   ("Alguien ya propuso la mejora que yo quería pedir. ¿Qué hago?",
    [("La propongo de nuevo igual", False),
     ("La voto o comento en la tabla de feedback", True),
     ("Nada, ya está pedida", False)]),
 ])),
])

# ---------- INDEX ----------
INDEX = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TUTORIALES — CRM CLUBES TED-ED ARGENTINA</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<style>
:root{--rojo:#dd2e26;--indigo:#2a2765;--celeste:#12c2ec;--amarillo:#ecdb14;--teal:#0a8baa;--azul:#345faa}
*{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif}
body{background:var(--indigo);color:#fff;min-height:100vh}
header{padding:60px 6vw 30px;text-align:center}
.lockup{display:inline-flex;align-items:center;gap:12px;margin-bottom:22px}
.lockup .sq{background:var(--rojo);color:#fff;font-weight:800;border-radius:12px;padding:8px 14px}
.lockup span{font-weight:600;font-size:.7rem;letter-spacing:.3em;text-transform:uppercase}
h1{font-weight:800;text-transform:uppercase;font-size:clamp(1.6rem,4vw,2.8rem)}
header p{font-weight:300;margin-top:10px;font-size:1.05rem}
header p i{color:var(--celeste)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:20px;max-width:1100px;margin:30px auto 20px;padding:0 5vw}
a.tcard{display:block;background:#fff;color:var(--indigo);border-radius:20px;padding:26px;text-decoration:none;
  transition:transform .2s, box-shadow .2s;border-top:8px solid var(--c)}
a.tcard:hover{transform:translateY(-6px);box-shadow:0 18px 44px rgba(0,0,0,.35)}
.tcard .ic{font-size:2rem}
.tcard h2{font-weight:700;text-transform:uppercase;font-size:1rem;margin:10px 0 8px;line-height:1.3}
.tcard p{font-weight:300;font-size:.85rem;line-height:1.55}
.tcard .go{display:inline-block;margin-top:14px;font-weight:700;font-size:.72rem;letter-spacing:.18em;
  text-transform:uppercase;color:var(--c)}
.video{max-width:1100px;margin:0 auto 60px;padding:0 5vw}
a.vbanner{display:flex;align-items:center;gap:20px;background:var(--rojo);color:#fff;border-radius:20px;
  padding:24px 30px;text-decoration:none;transition:transform .2s}
a.vbanner:hover{transform:translateY(-4px)}
.vbanner .play{font-size:2.4rem}
.vbanner h2{font-weight:800;text-transform:uppercase;font-size:1.1rem}
.vbanner p{font-weight:300;font-size:.85rem;margin-top:4px}
footer{text-align:center;padding:24px;font-weight:300;font-size:.75rem;color:rgba(255,255,255,.55)}
</style>
</head>
<body>
<header>
  <div class="lockup"><div class="sq">CLUBES TED-Ed</div><span>Argentina</span></div>
  <h1>TUTORIALES DEL CRM</h1>
  <p>Aprendé a usar el sistema a tu ritmo · <i>paso a paso, con práctica y repaso</i></p>
</header>
<div class="video">
  <a class="vbanner" href="intro-clubes-ted-ed-crm.html">
    <div class="play">▶</div>
    <div><h2>VIDEO: INTRODUCCIÓN AL CRM</h2>
    <p>El recorrido completo de la reunión de lanzamiento, animado. 2 minutos.</p></div>
  </a>
</div>
<div class="grid">
  <a class="tcard" style="--c:var(--rojo)" href="tutorial-1-basicos-instituciones.html">
    <div class="ic">📍</div><h2>1 · Básicos de monday en Instituciones</h2>
    <p>Tabla, columnas, ficha, filtros, vistas y permisos. Empezá por acá.</p>
    <span class="go">Empezar → · 8 min</span></a>
  <a class="tcard" style="--c:var(--celeste)" href="tutorial-2-licencias.html">
    <div class="ic">🎫</div><h2>2 · Tabla Licencias</h2>
    <p>Un club por ciclo académico: columnas, vinculaciones y sincro con Educabot.</p>
    <span class="go">Empezar → · 6 min</span></a>
  <a class="tcard" style="--c:var(--amarillo)" href="tutorial-3-facilitadores.html">
    <div class="ic">🧑‍🏫</div><h2>3 · Facilitadores Únicos</h2>
    <p>DNI vs idFac, subitems por inscripción y cómo leer la historia de cada persona.</p>
    <span class="go">Empezar → · 6 min</span></a>
  <a class="tcard" style="--c:var(--teal)" href="tutorial-4-feedback.html">
    <div class="ic">💬</div><h2>4 · Cómo dar feedback</h2>
    <p>El formulario, la tabla de propuestas, votos y plazos hasta la próxima reunión.</p>
    <span class="go">Empezar → · 4 min</span></a>
</div>
<footer>Clubes TED-Ed Argentina · Fundación IQT · CRM en monday.com</footer>
</body>
</html>"""
with open(os.path.join(OUT, "tutoriales-index.html"), "w", encoding="utf-8") as f:
    f.write(INDEX)
print("OK tutoriales-index.html")
