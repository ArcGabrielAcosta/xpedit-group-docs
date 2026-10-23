"""Presentación institucional de Xpedit Group. Regenera el pptx de esta carpeta."""

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

INK = RGBColor(0x16, 0x3F, 0x49)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
WARM = RGBColor(0xF6, 0xF4, 0xEF)
ACCENT = RGBColor(0xA6, 0x6D, 0x50)

W = 13.333333
H = 7.5
FONT = "Segoe UI"
FONT_LIGHT = "Segoe UI Light"
FONT_SEMI = "Segoe UI Semibold"

OUT = r"C:\Users\USER\Github\Xpedit-Group\modelo-de-negocio\Xpedit-Group-marco-institucional.pptx"


def rgb_of(color):
    return f"{color[0]:02X}{color[1]:02X}{color[2]:02X}"


def set_run_font(run, name, size, color, bold=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = False
    run.font.color.rgb = color
    r_pr = run._r.get_or_add_rPr()
    for tag in ("a:latin", "a:ea", "a:cs"):
        node = r_pr.find(qn(tag))
        if node is None:
            node = etree.SubElement(r_pr, qn(tag))
        node.set("typeface", name)


def fill_solid(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def add_rect(slide, l, t, w, h, color, radius=None):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if radius is not None else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(kind, Inches(l), Inches(t), Inches(w), Inches(h))
    fill_solid(shape, color)
    if radius is not None:
        shape.adjustments[0] = radius
    return shape


def send_back(slide, shape):
    tree = slide.shapes._spTree
    element = shape._element
    tree.remove(element)
    tree.insert(2, element)


def background(slide, color):
    shape = add_rect(slide, 0, 0, W, H, color)
    send_back(slide, shape)
    return shape


def write(slide, l, t, w, h, paragraphs, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT, margin=0.0):
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.vertical_anchor = anchor
    tf.margin_left = Inches(margin)
    tf.margin_right = Inches(margin)
    tf.margin_top = Inches(margin if margin else 0)
    tf.margin_bottom = Inches(0)
    for index, item in enumerate(paragraphs):
        text, size, color, bold, font, space_before, space_after, paragraph_align, spacing = item
        p = tf.paragraphs[0] if index == 0 else tf.add_paragraph()
        p.alignment = paragraph_align or align
        p.line_spacing = spacing
        p.space_before = Pt(space_before)
        p.space_after = Pt(space_after)
        run = p.add_run()
        run.text = text
        set_run_font(run, font, size, color, bold)
    return box


def P(text, size, color, bold=False, font=FONT, before=0, after=0, align=None, spacing=1.05):
    return (text, size, color, bold, font, before, after, align, spacing)


def chrome(slide, kicker, title, number, total):
    background(slide, WARM)
    add_rect(slide, 0, 0, 0.08, H, ACCENT)
    write(
        slide,
        0.58,
        0.32,
        10.5,
        0.28,
        [P(kicker.upper(), 11, ACCENT, True, FONT_SEMI, spacing=1)],
    )
    write(
        slide,
        0.56,
        0.58,
        11.6,
        0.62,
        [P(title, 28, INK, False, FONT_LIGHT, spacing=1.0)],
    )
    add_rect(slide, 0.58, 1.28, 1.15, 0.035, ACCENT)
    write(
        slide,
        0.58,
        7.12,
        8.5,
        0.26,
        [P("Xpedit Group   ·   Marco institucional v1.0   ·   Octubre 2026", 10, INK, False, FONT, spacing=1)],
    )
    write(
        slide,
        10.4,
        7.12,
        2.35,
        0.26,
        [P(f"{number:02d}   /   {total:02d}", 10, INK, False, FONT, align=PP_ALIGN.RIGHT, spacing=1)],
    )


def divider(slide, number, title, subtitle):
    background(slide, INK)
    add_rect(slide, 0, 0, 0.08, H, ACCENT)
    write(slide, 0.72, 2.15, 4, 0.4, [P(number, 18, ACCENT, True, FONT_SEMI, spacing=1)])
    add_rect(slide, 0.74, 2.68, 1.15, 0.035, ACCENT)
    write(
        slide,
        0.7,
        2.9,
        11,
        1.3,
        [P(title, 44, WHITE, False, FONT_LIGHT, spacing=0.98)],
    )
    write(
        slide,
        0.72,
        4.35,
        9.5,
        0.8,
        [P(subtitle, 18, WARM, False, FONT, spacing=1.15)],
    )


def build():
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    prs.core_properties.title = "Xpedit Group — Marco institucional, principios y régimen de conducta"
    prs.core_properties.subject = "Documento institucional v1.0 · octubre 2026"
    prs.core_properties.author = "Xpedit Group"
    blank = prs.slide_layouts[6]
    total = 21

    def new():
        return prs.slides.add_slide(blank)

    # 1. Portada
    s = new()
    background(s, INK)
    add_rect(s, 0, 0, 0.08, H, ACCENT)
    write(s, 0.72, 1.55, 10, 0.32, [P("XPEDIT GROUP    ·    OCTUBRE 2026", 13, ACCENT, True, FONT_SEMI, spacing=1)])
    write(
        s,
        0.68,
        2.05,
        11.5,
        2.15,
        [
            P("Donde corresponde,", 54, WHITE, False, FONT_LIGHT, spacing=0.95),
            P("cuando importa.", 54, WHITE, False, FONT_LIGHT, before=0, spacing=0.95),
        ],
    )
    add_rect(s, 0.74, 4.45, 1.35, 0.04, ACCENT)
    write(
        s,
        0.72,
        4.7,
        10,
        0.85,
        [
            P("Marco institucional, principios de actuación ética", 20, WARM, False, FONT, spacing=1.05),
            P("y régimen de conducta.", 20, WARM, False, FONT, spacing=1.05),
        ],
    )
    write(
        s,
        0.72,
        6.55,
        10,
        0.3,
        [P("Versión 1.0    ·    Documento institucional    ·    Argentina", 13, WARM, False, FONT, spacing=1)],
    )

    # 2. Tres piezas
    s = new()
    chrome(s, "El documento", "Tres piezas, un solo código", 2, total)
    pieces = [
        ("01", "Marco institucional", "Valores, misión y visión. La promesa de marca y las fronteras del módulo."),
        ("02", "Principios de actuación", "Criterios para decidir y para tratar con afiliados, clientes, equipo, proveedores y la comunidad."),
        ("03", "Régimen de conducta", "Conductas prohibidas para quien diseña, construye, comunica o administra Xpedit."),
    ]
    for i, (num, title, body) in enumerate(pieces):
        y = 1.65 + i * 1.7
        add_rect(s, 0.58, y, 12.15, 1.52, WHITE, radius=0.08)
        write(s, 0.85, y + 0.28, 1.3, 0.9, [P(num, 28, ACCENT, False, FONT_LIGHT, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)
        write(
            s,
            2.3,
            y + 0.28,
            9.9,
            1.0,
            [
                P(title, 22, INK, False, FONT_LIGHT, spacing=1),
                P(body, 15, INK, False, FONT, before=6, spacing=1.05),
            ],
            anchor=MSO_ANCHOR.MIDDLE,
        )

    # 3. El módulo
    s = new()
    chrome(s, "El proyecto", "La emergencia, dentro de la app de la cobertura", 3, total)
    write(
        s,
        0.58,
        1.5,
        12.1,
        0.85,
        [P("SaaS de bandera blanca para obras sociales y prepagas. El afiliado no instala otra aplicación. Xpedit no despacha ambulancias: el pedido confirmado entra a la red que la cobertura ya contrató.", 16, INK, False, FONT, spacing=1.12)],
    )
    steps = [
        ("01", "Teléfono bloqueado", "Tres pulsaciones abren la ventana, sin buscar la app."),
        ("02", "Confirmación", "Solo el deslizamiento envía. A los 10 segundos se cierra."),
        ("03", "Paquete mínimo", "Ficha, cobertura, contacto y GPS, cifrados."),
        ("04", "Cartilla vigente", "El destino es un prestador con convenio de esa cobertura."),
    ]
    card_w = 2.92
    gap = 0.16
    for i, (num, title, body) in enumerate(steps):
        x = 0.58 + i * (card_w + gap)
        add_rect(s, x, 2.55, card_w, 2.7, WHITE, radius=0.08)
        write(s, x + 0.24, 2.74, 2.45, 0.4, [P(num, 18, ACCENT, False, FONT_LIGHT, spacing=1)])
        add_rect(s, x + 0.26, 3.2, 0.48, 0.03, ACCENT)
        write(s, x + 0.24, 3.38, 2.45, 0.7, [P(title, 18, INK, False, FONT_LIGHT, spacing=1.0)])
        write(s, x + 0.24, 4.15, 2.45, 0.9, [P(body, 14, INK, False, FONT, spacing=1.05)])
    write(
        s,
        0.58,
        5.5,
        12.1,
        1.2,
        [P("La ficha —alergias, grupo sanguíneo, cobertura y contacto— se carga en calma. En la crisis, la decisión es una: confirmar o no. La ficha de esta etapa no es la historia clínica.", 16, INK, False, FONT, spacing=1.15)],
    )

    # 4. Encuesta
    s = new()
    chrome(s, "Evidencia", "La confianza está en la cobertura", 4, total)
    write(
        s,
        0.58,
        1.5,
        12.1,
        0.6,
        [P("Encuesta de validación, N = 384. El código toma estos resultados como deberes de diseño.", 16, INK, False, FONT, spacing=1.05)],
    )
    stats = [
        ("50 %", "Confía si la solución la ofrece su obra social o prepaga."),
        ("5 %", "Confiaría si fuera una aplicación independiente."),
        ("60 %", "Señala la demora de la ayuda como la mayor preocupación."),
    ]
    for i, (num, body) in enumerate(stats):
        x = 0.58 + i * 4.15
        add_rect(s, x, 2.35, 3.95, 3.55, WHITE, radius=0.08)
        write(s, x + 0.32, 2.7, 3.3, 1.05, [P(num, 46, ACCENT, False, FONT_LIGHT, spacing=1)])
        add_rect(s, x + 0.34, 3.9, 0.62, 0.03, ACCENT)
        write(s, x + 0.32, 4.15, 3.3, 1.35, [P(body, 16, INK, False, FONT, spacing=1.12)])

    # 5. Roles
    s = new()
    chrome(s, "Datos", "Quién custodia, y con qué rol", 5, total)
    roles = [
        ("Titular", "El afiliado, o quien está a cargo si la ficha es de un familiar.", "Decide, accede, rectifica y puede pedir la supresión."),
        ("Responsable", "La obra social o la prepaga.", "Define la finalidad, informa y responde ante el titular."),
        ("Encargado", "Xpedit Group.", "Trata los datos solo por instrucciones del responsable."),
        ("Destinatarios", "Prestador de la cartilla y contacto designado.", "Reciben lo necesario para salir o para ser avisados."),
    ]
    for i, (title, who, duty) in enumerate(roles):
        y = 1.58 + i * 1.32
        add_rect(s, 0.58, y, 12.15, 1.18, WHITE, radius=0.07)
        add_rect(s, 0.58, y + 0.28, 0.07, 0.62, ACCENT)
        write(s, 0.9, y + 0.16, 2.5, 0.86, [P(title, 16, ACCENT, True, FONT_SEMI, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)
        write(s, 3.5, y + 0.16, 4.3, 0.86, [P(who, 15, INK, False, FONT, spacing=1.05)], anchor=MSO_ANCHOR.MIDDLE)
        write(s, 8.0, y + 0.16, 4.4, 0.86, [P(duty, 15, INK, False, FONT, spacing=1.05)], anchor=MSO_ANCHOR.MIDDLE)

    # 6. Divisor marco
    s = new()
    divider(s, "01", "Marco institucional", "Valores, misión, visión y las fronteras que cambian el producto si se cruzan.")

    # 7. Misión y visión
    s = new()
    chrome(s, "Marco institucional", "Misión y visión", 7, total)
    add_rect(s, 0.58, 1.6, 12.15, 2.35, WHITE, radius=0.08)
    write(s, 0.9, 1.8, 2.2, 0.35, [P("MISIÓN", 12, ACCENT, True, FONT_SEMI, spacing=1)])
    write(
        s,
        0.9,
        2.2,
        11.5,
        1.45,
        [P("Hacer que, en una emergencia, la persona con cobertura active la red que ya le corresponde, con los datos justos y una confirmación explícita, mientras el 107 sigue disponible cuando esa es la vía correcta, con la rapidez que amerita dicha emergencia.", 18, INK, False, FONT, spacing=1.12)],
    )
    add_rect(s, 0.58, 4.15, 12.15, 2.15, INK, radius=0.08)
    write(s, 0.9, 4.35, 2.2, 0.35, [P("VISIÓN", 12, ACCENT, True, FONT_SEMI, spacing=1)])
    write(
        s,
        0.9,
        4.75,
        11.5,
        1.25,
        [P("Ser el módulo con el que obras sociales y prepagas responden ese primer minuto: sereno en la crisis, preciso en la derivación y riguroso con los datos que se tratan por cuenta de ellas.", 18, WHITE, False, FONT, spacing=1.12)],
    )

    # 8. Valores
    s = new()
    chrome(s, "Marco institucional", "Tres valores, con consecuencia", 8, total)
    values = [
        ("Velocidad serena", "Inmediatez operativa controlada, sin generar pánico.", "Se acorta el camino. El lenguaje y el color contienen. El rojo de urgencia queda para la confirmación y los estados críticos."),
        ("Precisión operativa", "Asignar el prestador que corresponde según la cobertura.", "El destino sale de la cartilla vigente. Un criterio comercial paralelo no desplaza el convenio."),
        ("Confianza humana", "Una interfaz y una voz que calman y contienen.", "La persona entiende qué va a pasar antes de confirmar. La marca visible es la de su cobertura."),
    ]
    for i, (title, definition, effect) in enumerate(values):
        x = 0.58 + i * 4.15
        add_rect(s, x, 1.6, 3.95, 5.15, WHITE, radius=0.08)
        write(s, x + 0.3, 1.95, 3.35, 1.15, [P(title, 24, INK, False, FONT_LIGHT, spacing=1.0)])
        add_rect(s, x + 0.32, 3.2, 0.55, 0.03, ACCENT)
        write(s, x + 0.3, 3.45, 3.35, 1.2, [P(definition, 15, ACCENT, False, FONT, spacing=1.08)])
        write(s, x + 0.3, 4.8, 3.35, 1.65, [P(effect, 14, INK, False, FONT, spacing=1.08)])

    # 9. Límites
    s = new()
    chrome(s, "Marco institucional", "Fronteras del módulo", 9, total)
    write(
        s,
        0.58,
        1.5,
        12.1,
        0.5,
        [P("Cruzar una de estas fronteras cambia el producto y obliga a revisar el código.", 16, INK, False, FONT, spacing=1)],
    )
    limits = [
        ("01", "Ordena el acceso", "La atención la presta el efector que la cobertura contrató."),
        ("02", "Sin flota propia", "Xpedit no opera ambulancias ni arma una red de móviles."),
        ("03", "La vía pública permanece", "El 107 y el 911 siguen cuando esa es la vía que corresponde."),
        ("04", "Código rojo", "El módulo no es canal de medicina domiciliaria ni de consultas menores."),
        ("05", "Bandera blanca", "En esta etapa no hay una app de marca Xpedit para el afiliado."),
        ("06", "Ficha, no historia clínica", "No se registran actos médicos, diagnósticos ni evolución."),
    ]
    for i, (num, title, body) in enumerate(limits):
        col = i % 2
        row = i // 2
        x = 0.58 + col * 6.3
        y = 2.15 + row * 1.5
        add_rect(s, x, y, 6.05, 1.35, WHITE, radius=0.08)
        write(s, x + 0.22, y + 0.22, 0.7, 0.9, [P(num, 16, ACCENT, True, FONT_SEMI, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)
        write(
            s,
            x + 1.0,
            y + 0.2,
            4.8,
            0.95,
            [
                P(title, 16, INK, True, FONT_SEMI, spacing=1),
                P(body, 13, INK, False, FONT, before=3, spacing=1.05),
            ],
            anchor=MSO_ANCHOR.MIDDLE,
        )

    # 10. Divisor principios
    s = new()
    divider(
        s,
        "02",
        "Principios de actuación ética",
        "Si dos principios entran en tensión, prevalecen la salud, la seguridad y el bienestar de la persona.",
    )

    # 11. Cómo se decide
    s = new()
    chrome(s, "Principios", "De dónde salen los criterios", 11, total)
    sources = [
        ("Ingeniería de software", "Código ACM / IEEE, versión 5.2. Ocho principios. El primero es el interés público: aprobar solo software con fundamento de seguridad, revelar peligros y decir con exactitud qué hace el producto."),
        ("Privacidad y daño", "Código ACM 2018. Evitar el daño, respetar la privacidad —mínimo dato, finalidad, plazo— y diseñar una seguridad que la persona pueda usar bajo estrés."),
        ("Información de salud", "Código IMIA. Autonomía, justicia, beneficencia y no maleficencia, bajados al dato: apertura, seguridad, acceso, la alternativa menos intrusiva y rendición de cuentas."),
    ]
    for i, (title, body) in enumerate(sources):
        y = 1.58 + i * 1.72
        add_rect(s, 0.58, y, 12.15, 1.58, WHITE, radius=0.08)
        add_rect(s, 0.58, y + 0.32, 0.07, 0.94, ACCENT)
        write(s, 0.95, y + 0.18, 11.4, 0.38, [P(title, 18, INK, False, FONT_LIGHT, spacing=1)])
        write(s, 0.95, y + 0.62, 11.4, 0.78, [P(body, 14, INK, False, FONT, spacing=1.08)])
    # The third card might collide with footer. y of third = 1.58+3.44 = 5.02, height 1.58 ends 6.60. Footer at 7.12. OK.

    # 12. Principios 1-6
    s = new()
    chrome(s, "Principios", "Doce criterios de Xpedit", 12, total)
    principles_a = [
        ("01", "La persona primero", "Una métrica, un plazo o una demo no desplazan la seguridad de quien pide ayuda."),
        ("02", "La confirmación es cuidado", "La velocidad empieza después de un gesto explícito."),
        ("03", "Mínimo dato, una finalidad", "Se informa antes de la carga. Otro uso pide otra base."),
        ("04", "La custodia es del financiador", "Xpedit trata por encargo y no arma un archivo propio de salud."),
        ("05", "Verdad operativa", "Lo que se dice del producto coincide con lo que el sistema hace."),
        ("06", "La vía pública permanece", "El módulo convive con el 107 y el 911."),
    ]
    principles_b = [
        ("07", "Seguridad usable", "Un control que en la práctica se saltea deja de ser una protección."),
        ("08", "El secreto continúa", "La reserva sigue después de terminada la relación con Xpedit."),
        ("09", "Hay rastro, y se repara", "Accesos y activaciones quedan registrados. El daño se mitiga y se avisa."),
        ("10", "La objeción se escucha", "Plantear un riesgo ético es parte del trabajo, sin represalia."),
        ("11", "Dentro de la competencia", "Se dice el límite de experiencia cuando afecta la seguridad o la licitud."),
        ("12", "La cartilla es el criterio", "La derivación no suma preferencia por pago, vínculo o conveniencia."),
    ]

    def principles(slide, items):
        for i, (num, title, body) in enumerate(items):
            col = i % 2
            row = i // 2
            x = 0.58 + col * 6.3
            y = 1.55 + row * 1.75
            add_rect(slide, x, y, 6.05, 1.6, WHITE, radius=0.08)
            write(slide, x + 0.22, y + 0.22, 0.85, 0.4, [P(num, 16, ACCENT, True, FONT_SEMI, spacing=1)])
            write(slide, x + 0.22, y + 0.62, 5.55, 0.35, [P(title, 16, INK, True, FONT_SEMI, spacing=1)])
            write(slide, x + 0.22, y + 1.02, 5.55, 0.42, [P(body, 13, INK, False, FONT, spacing=1.02)])

    principles(s, principles_a)

    s = new()
    chrome(s, "Principios", "Doce criterios de Xpedit", 13, total)
    principles(s, principles_b)

    # 14. Relaciones — wait, numbers shift. I set total=18 then added an extra principles slide.
    # Recount at the end and pass the right numbers. I'll set numbers after building by editing,
    # or compute total first.
    # Current plan after this insertion:
    # 1 cover, 2 piezas, 3 modulo, 4 encuesta, 5 roles, 6 divider, 7 mision, 8 valores, 9 limites,
    # 10 divider, 11 fuentes, 12 principios a, 13 principios b, 14 relaciones, 15 divider conducta,
    # 16 regimen, 17 recordar, 18 incidente, 19 legal, 20 pendientes, 21 cierre
    # That's 21. Let me continue and fix numbers in a second pass by storing slides.
    # Easier: I'll hardcode after I know the count. I'll use a list and stamp footers at the end.
    # For now the chrome() already wrote numbers. I'll fix by not using chrome numbers until the end.
    # Too late for slides already created. I'll rebuild numbering in a cleanup: the function already wrote text.
    # I'll change approach: continue, then I'll update the script's total and the sequence is fixed
    # if I set total = 21 and the remaining chrome calls use 14..21.
    # Slides already called with total=18 and numbers 2-13. I need to fix those.
    # Best: finish content, then do a text replace... ugly.
    # I'll set TOTAL = 21 now in my head and patch the earlier calls by editing the file before running.
    # Since I haven't run yet, I can set total = 21 and fix the numbers in chrome() calls I already wrote
    # by editing this file after write... I'm still writing the file. Let me use total = 21
    # and correct the numbers I already passed:
    # 2 piezas ok if total becomes 21, the "18" in the string is wrong.
    # I will replace total variable usage. Let me set total = 21 at the top of build after I finish
    # and update each chrome number. I'll do a search replace after the write if counts are wrong.
    #
    # Planned final order and numbers:
    # 1 portada (no chrome)
    # 2 tres piezas
    # 3 modulo
    # 4 encuesta
    # 5 roles
    # 6 divider marco (no number in footer)
    # 7 mision
    # 8 valores
    # 9 limites
    # 10 divider principios
    # 11 fundamentos
    # 12 principios 1-6
    # 13 principios 7-12
    # 14 relaciones
    # 15 divider conducta
    # 16 cinco grupos
    # 17 seis conductas
    # 18 incidente
    # 19 piso legal
    # 20 pendientes
    # 21 cierre
    # total 21. Dividers don't have the footer number. Cover and close neither.
    # Content slides that need n/total: 2,3,4,5,7,8,9,11,12,13,14,16,17,18,19,20 = 16 content + 3 dividers + cover + close = 21.
    # I'll pass total=21 and fix earlier numbers with a replace after this write if I used 18.
    # Continuing with total still 18 in the closure - I must update the variable. I'll change `total = 18` 
    # by writing the rest with explicit numbers and then fix the header of the function.
    # Simplest path: use a mutable counter.

    # 14 Relaciones
    s = new()
    chrome(s, "Principios", "Con quién, y con qué criterio", 14, total)
    relations = [
        ("Afiliado", "Es titular de sus datos, no el cliente que paga. La ficha se carga en calma. En la crisis, confirma."),
        ("Cliente", "Obra social o prepaga. Compra el módulo y es responsable del archivo. Su interés cabe en el interés público."),
        ("Prestador", "Recibe el mínimo para salir. Lo elige la cartilla vigente, no un criterio paralelo."),
        ("Equipo", "El acceso dura lo que dura la tarea. La objeción ética se registra y se responde."),
        ("Proveedor", "Entra con autorización y contrato. No usa los datos para su producto ni elige el país por precio."),
        ("Comunidad", "El módulo es para el código rojo. La descongestión del 107 es un efecto buscado, no una cifra ya medida."),
    ]
    for i, (title, body) in enumerate(relations):
        col = i % 3
        row = i // 3
        x = 0.58 + col * 4.15
        y = 1.58 + row * 2.6
        add_rect(s, x, y, 3.95, 2.4, WHITE, radius=0.08)
        write(s, x + 0.24, y + 0.28, 3.45, 0.45, [P(title, 18, INK, False, FONT_LIGHT, spacing=1)])
        add_rect(s, x + 0.26, y + 0.85, 0.55, 0.03, ACCENT)
        write(s, x + 0.24, y + 1.08, 3.45, 1.1, [P(body, 13, INK, False, FONT, spacing=1.08)])

    # 15 divider conducta
    s = new()
    divider(
        s,
        "03",
        "Régimen de conducta",
        "Sigue prohibido aunque lo pida un cliente, un prestador o alguien con más experiencia.",
    )

    # 16 grupos
    s = new()
    chrome(s, "Régimen de conducta", "Cinco grupos, treinta y tres conductas", 16, total)
    write(
        s,
        0.58,
        1.48,
        12.1,
        0.7,
        [P("Obliga a quien diseña, desarrolla, prueba, documenta, comunica o administra Xpedit, en el trabajo de esta etapa y en un piloto futuro. El listado completo está en el documento.", 15, INK, False, FONT, spacing=1.08)],
    )
    groups = [
        ("01 – 10", "Datos y secreto", "Curiosidad, demos, modelos, cesión, publicidad y credenciales ajenas."),
        ("11 – 18", "Producto", "Confirmación, cifrado, pruebas, defectos ocultos, trazas y cartilla."),
        ("19 – 23", "Promesa", "Reemplazo del 107, flota propia, pánico visual y alta de la ficha incompleta."),
        ("24 – 30", "Cliente y equipo", "Uso fuera del encargo, soborno, conflicto oculto y represalia."),
        ("31 – 33", "Sistema público", "Demanda no crítica, esconder el 107 y pruebas que parecen una emergencia real."),
    ]
    for i, (num, title, body) in enumerate(groups):
        y = 2.3 + i * 0.9
        add_rect(s, 0.58, y, 12.15, 0.8, WHITE, radius=0.06)
        write(s, 0.82, y + 0.16, 1.7, 0.5, [P(num, 14, ACCENT, True, FONT_SEMI, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)
        write(s, 2.6, y + 0.16, 2.5, 0.5, [P(title, 16, INK, True, FONT_SEMI, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)
        write(s, 5.2, y + 0.14, 7.2, 0.55, [P(body, 14, INK, False, FONT, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)

    # 17 recordar
    s = new()
    chrome(s, "Régimen de conducta", "Seis reglas para tener a mano", 17, total)
    rules = [
        ("Datos reales", "No salen del encargo: ni a una demo, ni a un chat, ni a un modelo, ni a una laptop."),
        ("Sin confirmación", "No se debilita el deslizamiento, el cierre a los 10 segundos ni la cancelación para mejorar una métrica."),
        ("Defectos", "No se oculta un fallo que pueda desviar el pedido, perder la ubicación o exponer una ficha."),
        ("La promesa", "Xpedit no se presenta como reemplazo del 107, como flota ni como historia clínica."),
        ("El contrato", "No se ceden ni se conservan datos fuera de lo que el responsable autorizó."),
        ("La objeción", "No se sanciona a quien señala, de buena fe, un riesgo ético o legal."),
    ]
    for i, (title, body) in enumerate(rules):
        col = i % 2
        row = i // 2
        x = 0.58 + col * 6.3
        y = 1.55 + row * 1.75
        add_rect(s, x, y, 6.05, 1.6, WHITE, radius=0.08)
        add_rect(s, x, y + 0.32, 0.07, 0.96, ACCENT)
        write(s, x + 0.28, y + 0.22, 5.5, 0.38, [P(title, 16, INK, True, FONT_SEMI, spacing=1)])
        write(s, x + 0.28, y + 0.68, 5.5, 0.72, [P(body, 14, INK, False, FONT, spacing=1.05)])

    # 18 incidente
    s = new()
    chrome(s, "Régimen de conducta", "Si hay una duda, o si ya pasó", 18, total)
    incident = [
        ("1", "Frenar", "Se detiene el acto que involucra datos reales o un despliegue, antes de seguir."),
        ("2", "Avisar", "Se plantea a quien conduce el proyecto. Si hay cliente afectado, también a su contacto de seguridad o legal."),
        ("3", "Registrar", "Fecha, hecho, decisión y seguimiento. El registro no copia la ficha."),
    ]
    for i, (num, title, body) in enumerate(incident):
        x = 0.58 + i * 4.15
        add_rect(s, x, 1.6, 3.95, 3.15, WHITE, radius=0.08)
        write(s, x + 0.28, 1.85, 3.4, 0.7, [P(num, 32, ACCENT, False, FONT_LIGHT, spacing=1)])
        write(s, x + 0.28, 2.6, 3.4, 0.45, [P(title, 22, INK, False, FONT_LIGHT, spacing=1)])
        write(s, x + 0.28, 3.2, 3.4, 1.25, [P(body, 14, INK, False, FONT, spacing=1.08)])
    add_rect(s, 0.58, 5.0, 12.15, 1.75, INK, radius=0.08)
    write(
        s,
        0.9,
        5.25,
        11.5,
        1.3,
        [
            P("Ocultar el incidente tiene la misma gravedad que el hecho.", 18, WHITE, False, FONT_LIGHT, spacing=1),
            P("Hasta el cierre jurídico del piloto, los entornos de diseño, demostración y prueba usan datos ficticios.", 15, WARM, False, FONT, before=8, spacing=1.05),
        ],
    )

    # 19 legal
    s = new()
    chrome(s, "Piso legal", "Lo que estas reglas no pueden aflojar", 19, total)
    laws = [
        ("Ley 25.326", "Dato de salud es dato sensible. Consentimiento informado, seguridad, secreto y encargo. La autoridad es la AAIP."),
        ("Ley 26.529", "Intimidad y confidencialidad del paciente. La ficha del módulo se mantiene distinta de la historia clínica."),
        ("Código Penal", "Artículos 156 y 157 bis: revelar un secreto sin justa causa, y acceder o alterar un banco de datos personales."),
        ("Convenio 108+", "Ley 27.699. Amplía los datos sensibles a genéticos y biométricos. Esta ficha no los pide."),
    ]
    for i, (title, body) in enumerate(laws):
        col = i % 2
        row = i // 2
        x = 0.58 + col * 6.3
        y = 1.58 + row * 2.55
        add_rect(s, x, y, 6.05, 2.35, WHITE, radius=0.08)
        write(s, x + 0.28, y + 0.28, 5.5, 0.45, [P(title, 20, INK, False, FONT_LIGHT, spacing=1)])
        add_rect(s, x + 0.3, y + 0.85, 0.6, 0.03, ACCENT)
        write(s, x + 0.28, y + 1.1, 5.5, 0.95, [P(body, 14, INK, False, FONT, spacing=1.08)])

    # 20 pendientes
    s = new()
    chrome(s, "Antes de un piloto", "Lo que todavía tiene que cerrar un asesor", 20, total)
    pending = [
        ("01", "Contrato de encargo", "Instrucciones, seguridad, subencargados, conservación y destrucción."),
        ("02", "Responsable e inscripción", "Confirmar el carácter del financiador y el estado de su archivo ante la AAIP."),
        ("03", "Dónde viven los datos", "Si el alojamiento sale de la Argentina, la base de la transferencia internacional."),
        ("04", "Texto para el afiliado", "Finalidad, destinatarios, contacto de emergencia y familiar a cargo."),
        ("05", "Procedimiento de incidente", "Acordado con el cliente, antes de que exista un caso real."),
    ]
    for i, (num, title, body) in enumerate(pending):
        y = 1.52 + i * 1.02
        add_rect(s, 0.58, y, 12.15, 0.92, WHITE, radius=0.06)
        write(s, 0.82, y + 0.18, 0.7, 0.56, [P(num, 16, ACCENT, True, FONT_SEMI, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)
        write(s, 1.7, y + 0.12, 3.5, 0.68, [P(title, 16, INK, True, FONT_SEMI, spacing=1)], anchor=MSO_ANCHOR.MIDDLE)
        write(s, 5.3, y + 0.12, 7.1, 0.68, [P(body, 14, INK, False, FONT, spacing=1.02)], anchor=MSO_ANCHOR.MIDDLE)

    # 21 cierre
    s = new()
    background(s, INK)
    add_rect(s, 0, 0, 0.08, H, ACCENT)
    write(s, 0.72, 1.85, 11, 0.3, [P("XPEDIT GROUP", 13, ACCENT, True, FONT_SEMI, spacing=1)])
    write(
        s,
        0.68,
        2.3,
        11.5,
        2.0,
        [
            P("Donde corresponde,", 48, WHITE, False, FONT_LIGHT, spacing=0.98),
            P("cuando importa.", 48, WHITE, False, FONT_LIGHT, spacing=0.98),
        ],
    )
    add_rect(s, 0.74, 4.55, 1.35, 0.04, ACCENT)
    write(
        s,
        0.72,
        4.85,
        10.5,
        1.15,
        [P("Este código rige el trabajo de la etapa. Se revisa si cambia el alcance, si la ficha suma datos, o cuando exista el primer contrato con un financiador.", 16, WARM, False, FONT, spacing=1.12)],
    )
    write(
        s,
        0.72,
        6.45,
        10,
        0.3,
        [P("Versión 1.0    ·    Octubre 2026    ·    Documento institucional", 13, WARM, False, FONT, spacing=1)],
    )

    prs.save(OUT)


if __name__ == "__main__":
    build()
