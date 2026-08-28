#!/usr/bin/env python3
"""Gera os ícones do app 'Meu Ministério', no mesmo espírito visual do Planejar:
fundo escuro, moldura arredondada na cor de destaque, glifo simples em creme."""
from PIL import Image, ImageDraw

BG = (14, 22, 33, 255)        # fundo escuro (tom "azul" bem escuro)
ACCENT = (47, 106, 196, 255)  # azul (--barra do tema azul do Planejar)
PAPER = (241, 244, 238, 255)  # creme claro (mesmo tom do --surf2 do Planejar)

def rounded_square(size, radius_ratio):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius_ratio), fill=BG)
    return img, d

def draw_glyph(d, size, inset_ratio=0.16, frame_w_ratio=0.052):
    inset = size * inset_ratio
    frame_w = max(2, int(size * frame_w_ratio))
    box = [inset, inset, size - inset, size - inset]
    d.rounded_rectangle(box, radius=int(size * 0.14), outline=ACCENT, width=frame_w)

    # glifo: livro aberto simples (duas "páginas" com uma lombada central),
    # ecoando o motivo de linhas do ícone do Planejar mas em forma de livro.
    cx = size / 2
    top = size * 0.34
    bottom = size * 0.68
    half_w = size * 0.205
    gap = size * 0.012

    # página esquerda
    d.line([(cx - gap, top), (cx - half_w, top + size * 0.03)], fill=PAPER, width=int(size * 0.045))
    left_pts = [
        (cx - gap, top + size * 0.01),
        (cx - half_w, top + size * 0.045),
        (cx - half_w, bottom - size * 0.02),
        (cx - gap, bottom - size * 0.055),
    ]
    d.line(left_pts, fill=PAPER, width=int(size * 0.045), joint='curve')
    # página direita
    right_pts = [
        (cx + gap, top + size * 0.01),
        (cx + half_w, top + size * 0.045),
        (cx + half_w, bottom - size * 0.02),
        (cx + gap, bottom - size * 0.055),
    ]
    d.line(right_pts, fill=PAPER, width=int(size * 0.045), joint='curve')
    # lombada central
    d.line([(cx, top - size * 0.01), (cx, bottom - size * 0.04)], fill=ACCENT, width=int(size * 0.04))

def make(size, radius_ratio=0.225, maskable=False):
    if maskable:
        # zona segura maior: o glifo ocupa só ~60% do centro
        img, d = rounded_square(size, 0.0)
        d.rectangle([0, 0, size, size], fill=BG)
        inner = int(size * 0.66)
        off = (size - inner) // 2
        sub = Image.new('RGBA', (inner, inner), (0, 0, 0, 0))
        sd = ImageDraw.Draw(sub)
        draw_glyph(sd, inner, inset_ratio=0.1, frame_w_ratio=0.06)
        img.alpha_composite(sub, (off, off))
        return img
    img, d = rounded_square(size, radius_ratio)
    draw_glyph(d, size)
    return img

import os
out = os.path.dirname(os.path.abspath(__file__)) + '/icons'
os.makedirs(out, exist_ok=True)

make(512).save(out + '/icon-512.png')
make(192).save(out + '/icon-192.png')
make(512, maskable=True).save(out + '/icon-maskable-512.png')
make(192, maskable=True).save(out + '/icon-maskable-192.png')

# apple-touch-icon: sem transparência (iOS ignora alpha e arredonda sozinho)
at = make(180, radius_ratio=0.0)
flat = Image.new('RGB', at.size, BG[:3])
flat.paste(at, mask=at.split()[3])
flat.save(out + '/apple-touch-icon.png')

make(32).save(out + '/favicon-32.png')
make(16).save(out + '/favicon-16.png')

print('ok', os.listdir(out))
