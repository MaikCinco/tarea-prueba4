from pathlib import Path

def generar_reporte_html(titulo, screenshots, nombre_archivo):
    with open(nombre_archivo, "w") as f:
        f.write("<html><head><title>{}</title></head><body>".format(titulo))
        f.write("<h1>{}</h1>".format(titulo))
        for img in screenshots:
            f.write('<img src="{}" style="width:800px;"><br>'.format(img))
        f.write("</body></html>")

