from cairosvg import svg2pdf


def process(svg: str):
    svg = svg.replace('&', '&amp;')
    buff = svg.encode('utf-8')
    buff = svg2pdf(buff)

    return buff
