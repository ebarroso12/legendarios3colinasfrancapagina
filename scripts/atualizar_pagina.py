import sys,re
src,out=sys.argv[1],sys.argv[2]
t=open(src,encoding='utf-8').read()
s=t.find('<!doctype html><html lang="pt-BR">'); e=t.find('</html>',s)+7
h=t[s:e]
WA_NUM='5516993243128'
WA=f'https://wa.me/{WA_NUM}?text=Ol%C3%A1!%20Quero%20informa%C3%A7%C3%B5es%20sobre%20o%20TOP%201922%20-%20Legend%C3%A1rios%203%20Colinas%20(Franca)'
IG='https://www.instagram.com/legendarios3colinas'
TK='https://ticketandgo.com.br/legendarios-top-1922-track-3-colinas?id=baf5a82b-9324-4927-91a9-493e86c52877'
OLD_TK='https://ticketandgo.com.br/legendarios-top-1782-track-3-colinas?id=6ba864f0-6579-48ca-83d6-ba4b16dfcaab'
VIP='https://chat.whatsapp.com/LkfTncbrJAfAPutDtjay8L'
def rep(a,b,count=None):
    global h
    n=h.count(a)
    assert n>0,a
    if count is not None: assert n==count,(a,n)
    h=h.replace(a,b)
ARROW='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
WAICON='<svg width="{s}" height="{s}" viewBox="0 0 32 32" fill="#fff" aria-hidden="true"><path d="M16.04 3C9 3 3.3 8.7 3.3 15.74c0 2.25.59 4.45 1.71 6.39L3.2 28.8l6.85-1.8a12.7 12.7 0 0 0 5.99 1.52h.01c7.03 0 12.74-5.71 12.74-12.75C28.79 8.7 23.08 3 16.04 3Zm0 23.36h-.01a10.6 10.6 0 0 1-5.4-1.48l-.39-.23-4.07 1.07 1.09-3.96-.25-.41a10.56 10.56 0 0 1-1.62-5.62c0-5.85 4.76-10.6 10.62-10.6a10.6 10.6 0 0 1 10.6 10.61c0 5.86-4.76 10.62-10.57 10.62Zm5.81-7.94c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.72.16-.21.32-.82 1.04-1.01 1.25-.19.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.9-1.78-2.22-.19-.32-.02-.49.14-.65.14-.14.32-.37.48-.56.16-.19.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.72-1.73-.98-2.37-.26-.62-.52-.54-.72-.55h-.61c-.21 0-.56.08-.85.4-.29.32-1.12 1.09-1.12 2.66s1.14 3.08 1.3 3.3c.16.21 2.25 3.43 5.44 4.81.76.33 1.35.52 1.81.67.76.24 1.45.21 2 .13.61-.09 1.89-.77 2.15-1.52.27-.75.27-1.39.19-1.52-.08-.13-.29-.21-.61-.37Z"/></svg>'
IGICON='<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1" fill="currentColor" stroke="none"/></svg>'

# ---- HEAD / SEO
rep('<title>Legendários — TOP 1782 · Inscrições Abertas</title>','<title>Legendários 3 Colinas — TOP 1922 · Edição Especial de 1 Ano · Franca-SP</title>')
rep('content="Homens inquebrantáveis. Histórias dignas de serem contadas. Garanta sua vaga no TOP 1782 — 27 a 30 de Agosto."',
    'content="TOP 1922 Legendários 3 Colinas — Edição Especial de 1 Ano. 26 a 29 de Novembro de 2026 em Franca-SP. Inscrições abertas, vagas limitadas. Garanta seu ingresso."><meta property="og:title" content="TOP 1922 · Legendários 3 Colinas · 26 a 29 de Novembro"><meta property="og:description" content="Edição Especial de 1 Ano. 72h de imersão em Franca-SP. Inscrições abertas — vagas limitadas."><meta name="theme-color" content="#080808"')

# ---- TICKER
rep('<span>TOP 1782 · 27 A 30 DE AGOSTO</span>','<span>TOP 1922 · 26 A 29 DE NOVEMBRO</span><span class="dot">✦</span> <span>EDIÇÃO ESPECIAL DE 1 ANO</span>',2)
rep('<span>3 COLINAS · 3 DIAS · 1 MISSÃO</span>','<span>3 COLINAS · FRANCA-SP</span><span class="dot">✦</span> <span>ATENDIMENTO 24H · (16) 99324-3128</span>',2)

# ---- NAV: add Instagram shortcut
rep('<nav><a class="nav-logo" href="#">LEGENDÁRIOS<span>MOVIMENTO DE HOMENS</span></a></nav>',
    f'<nav><a class="nav-logo" href="#">LEGENDÁRIOS<span>MOVIMENTO DE HOMENS</span></a><a class="nav-ig" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram @legendarios3colinas">{IGICON.format(s=20)}</a></nav>')

# ---- HERO
rep('<div class="hero-badge">Inscrições Abertas · Vagas Limitadas</div>',
    '<div class="hero-badge">Inscrições Abertas · Vagas Limitadas</div><div class="hero-special">★ Edição Especial de 1 Ano ★</div>')
rep('<div class="hero-number">1782</div>','<div class="hero-number">1922</div>')
rep('<div class="date-item"><div class="num">27</div><div class="lbl">Agosto</div></div>','<div class="date-item"><div class="num">26</div><div class="lbl">Novembro</div></div>')
rep('<div class="date-item"><div class="num">30</div><div class="lbl">Agosto</div></div>','<div class="date-item"><div class="num">29</div><div class="lbl">Novembro</div></div>')
rep('<span class="cd-label-top">⏱ Faltam para o evento</span>','<p class="hero-local">📍 Franca-SP · Track 3 Colinas</p><span class="cd-label-top">⏱ Faltam para o TOP 1922</span>')
rep(f'<a href="{VIP}" target="_blank" class="hero-cta">{ARROW} ENTRAR NO GRUPO VIP COM DESCONTO</a><p class="hero-sub">Inscrições Abertas &nbsp;·&nbsp; <strong>TOP 1782 · 27 a 30 de Agosto</strong></p>',
    f'<a href="{TK}" target="_blank" rel="noopener" class="hero-cta">{ARROW} GARANTIR MINHA VAGA NO TOP 1922</a>'
    f'<a href="{WA}" target="_blank" rel="noopener" class="hero-wa">{WAICON.format(s=18)} Dúvidas? Fale com a equipe — 24h</a>'
    '<p class="hero-sub">Inscrições Abertas &nbsp;·&nbsp; <strong>TOP 1922 · 26 a 29 de Novembro</strong></p>')

# ---- STRIP
rep('<div class="s-val">1782</div><div class="s-lbl">Número da Edição</div>','<div class="s-val">1922</div><div class="s-lbl">Número da Edição</div></div><div class="strip-sep"></div><div class="strip-item"><div class="s-val">1 ANO</div><div class="s-lbl">Edição Especial</div>')

# ---- JORNADA label
rep('<span class="fade-up section-label">TOP 1782 · A Jornada</span>','<span class="fade-up section-label">TOP 1922 · A Jornada</span>')

# ---- CTA block
rep('<span class="cta-eyebrow">TOP 1782 · 27 a 30 de Agosto</span>','<span class="cta-eyebrow">TOP 1922 · 26 a 29 de Novembro · Franca-SP</span>')
rep('<p class="fade-up">Entre agora e garanta sua vaga. As vagas são limitadas e se encerram rapidamente.</p>',
    '<p class="fade-up">Edição Especial de 1 Ano do Legendários 3 Colinas. Garanta agora seu ingresso — as vagas são limitadas e se encerram rapidamente.</p>')
rep(f'<a href="{VIP}" target="_blank" class="fade-up cta-btn">{ARROW} ENTRAR NO GRUPO VIP COM DESCONTO</a><p class="fade-up cta-note">Inscrições Abertas &nbsp;·&nbsp; <strong>Vagas Limitadas</strong> &nbsp;·&nbsp; TOP 1782</p>',
    f'<a href="{TK}" target="_blank" rel="noopener" class="fade-up cta-btn">{ARROW} COMPRAR MEU INGRESSO</a>'
    f'<p class="fade-up cta-note">Inscrições Abertas &nbsp;·&nbsp; <strong>Vagas Limitadas</strong> &nbsp;·&nbsp; TOP 1922</p>'
    f'<div class="fade-up cta-alt"><a href="{WA}" target="_blank" rel="noopener" class="cta-alt-wa">{WAICON.format(s=18)} WhatsApp 24h · (16) 99324-3128</a>'
    f'<a href="{IG}" target="_blank" rel="noopener" class="cta-alt-ig">{IGICON.format(s=18)} @legendarios3colinas</a></div>')

# ---- CONTACT section before AHU
CONTACT=(f'<section class="contato"><span class="fade-up section-label">Atendimento</span><h2 class="fade-up">FALE COM A <em>EQUIPE 3 COLINAS</em></h2>'
 '<p class="fade-up contato-sub">Dúvidas sobre inscrição, pagamento, o que levar ou como funciona o TOP? Nossa equipe responde 24 horas pelo WhatsApp.</p>'
 '<div class="contato-grid">'
 f'<a class="fade-up contato-card" href="{WA}" target="_blank" rel="noopener"><span class="contato-ico wa">{WAICON.format(s=26)}</span><span class="contato-t">WhatsApp · 24 horas</span><span class="contato-v">(16) 99324-3128</span><span class="contato-go">Chamar agora →</span></a>'
 f'<a class="fade-up contato-card" href="{IG}" target="_blank" rel="noopener" style="transition-delay:.1s"><span class="contato-ico ig">{IGICON.format(s=26)}</span><span class="contato-t">Instagram</span><span class="contato-v">@legendarios3colinas</span><span class="contato-go">Seguir →</span></a>'
 f'<a class="fade-up contato-card" href="{TK}" target="_blank" rel="noopener" style="transition-delay:.2s"><span class="contato-ico tk"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9V6a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v3a3 3 0 0 0 0 6v3a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-3a3 3 0 0 0 0-6Z"/><path d="M13 5v2M13 11v2M13 17v2"/></svg></span><span class="contato-t">Ingresso oficial</span><span class="contato-v">Ticket and Go</span><span class="contato-go">Comprar →</span></a>'
 '</div></section>')
rep('<div class="ahu"><p class="ahu-title">AHU</p>',CONTACT+'<div class="ahu"><p class="ahu-title">AHU</p>')

# ---- FOOTER
rep('<p>© 2026 Legendários 3 Colinas · Todos os direitos reservados</p>',
    f'<div class="footer-social"><a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IGICON.format(s=20)}</a><a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{WAICON.format(s=20)}</a></div>'
    '<p>TOP 1922 · 26 a 29 de Novembro de 2026 · Franca-SP</p><p style="margin-top:.4rem">© 2026 Legendários 3 Colinas · Todos os direitos reservados</p>')

# ---- FLOATING: ticket + WhatsApp 24h
rep(f'<div class="float-cta"><div class="float-btn-wrap"><div class="float-label">Garantir Vaga · TOP 1782</div><a href="{OLD_TK}" target="_blank" class="float-btn" aria-label="Garantir minha vaga">',
    f'<div class="float-cta"><div class="float-btn-wrap"><div class="float-label">Garantir Vaga · TOP 1922</div><a href="{TK}" target="_blank" rel="noopener" class="float-btn" aria-label="Garantir minha vaga">')
rep('</a></div></div><script>',
    f'</a></div><div class="float-btn-wrap"><div class="float-label wa-label">Atendimento 24h · WhatsApp</div><a href="{WA}" target="_blank" rel="noopener" class="wa-float" aria-label="WhatsApp atendimento 24 horas">{WAICON.format(s=30)}<span class="wa-badge">24h</span></a></div></div><script>')

# ---- COUNTDOWN
rep("new Date('2026-08-27T08:00:00-03:00')","new Date('2026-11-26T08:00:00-03:00')")
rep("if(diff<=0) return;","if(diff<=0){document.querySelector('.cd-label-top').textContent='🔥 O TOP 1922 começou!';return;}")

# ---- CSS additions
CSS='''.hero-cta{display:flex;width:max-content;max-width:100%;margin:0 auto}.strip-inner{max-width:1100px;gap:2.2rem}
.nav-ig{position:absolute;right:1.5rem;top:4px;color:#fff;opacity:.8;display:flex;padding:8px;border-radius:50%;border:1px solid rgba(255,255,255,.18);transition:all .25s}.nav-ig:hover{opacity:1;color:var(--gold);border-color:var(--gold)}
.hero-special{display:block;width:max-content;max-width:100%;margin:0 auto 1.1rem;font-family:Oswald,sans-serif;font-size:.78rem;font-weight:600;letter-spacing:.28em;text-transform:uppercase;color:#fff;background:linear-gradient(90deg,var(--gold-dim),var(--gold),var(--gold-dim));padding:6px 16px;border-radius:3px;box-shadow:0 0 30px rgba(245,112,10,.35)}
.hero-local{font-family:Oswald,sans-serif;font-size:.8rem;letter-spacing:.22em;text-transform:uppercase;color:#fff;opacity:.9;margin:-1rem 0 1.6rem;text-shadow:0 1px 10px #000}
.hero-wa{display:flex;align-items:center;justify-content:center;gap:8px;margin:1rem auto 0;width:max-content;max-width:100%;font-family:Oswald,sans-serif;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;color:#fff;text-decoration:none;padding:10px 18px;border:1px solid rgba(37,211,102,.55);border-radius:4px;background:rgba(37,211,102,.12);backdrop-filter:blur(6px);transition:all .25s}.hero-wa:hover{background:rgba(37,211,102,.28)}
.cta-alt{display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;margin-top:1.8rem}.cta-alt a{display:inline-flex;align-items:center;gap:8px;font-family:Oswald,sans-serif;font-size:.8rem;letter-spacing:.08em;color:#fff;text-decoration:none;padding:10px 16px;border-radius:4px;border:1px solid rgba(255,255,255,.14);transition:all .25s}.cta-alt-wa{background:rgba(37,211,102,.14);border-color:rgba(37,211,102,.45)!important}.cta-alt a:hover{transform:translateY(-2px);border-color:var(--gold)!important}
.contato{padding:6rem 1.5rem;max-width:1000px;margin:0 auto;text-align:center}.contato h2{font-family:'Bebas Neue',sans-serif;font-size:clamp(2rem,5.5vw,3rem);letter-spacing:.08em;line-height:1.1;margin-bottom:1rem}.contato h2 em{font-style:normal;color:var(--gold)}.contato-sub{color:rgba(255,255,255,.72);line-height:1.7;max-width:560px;margin:0 auto 2.5rem}
.contato-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}.contato-card{display:flex;flex-direction:column;align-items:center;gap:.4rem;padding:2rem 1.2rem;background:var(--bg3);border:1px solid rgba(245,112,10,.12);border-radius:6px;color:#fff;text-decoration:none;transition:border-color .3s,transform .3s}.contato-card:hover{border-color:rgba(245,112,10,.5);transform:translateY(-3px)}
.contato-ico{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:.6rem;color:#fff}.contato-ico.wa{background:#25D366}.contato-ico.ig{background:linear-gradient(45deg,#F58529,#DD2A7B,#8134AF)}.contato-ico.tk{background:var(--gold)}
.contato-t{font-family:Oswald,sans-serif;font-size:.68rem;letter-spacing:.25em;text-transform:uppercase;color:var(--muted)}.contato-v{font-family:'Bebas Neue',sans-serif;font-size:1.6rem;letter-spacing:.05em}.contato-go{font-family:Oswald,sans-serif;font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold)}
.footer-social{display:flex;justify-content:center;gap:1rem;margin-bottom:1rem}.footer-social a{display:flex;width:40px;height:40px;align-items:center;justify-content:center;border-radius:50%;border:1px solid rgba(245,112,10,.3);color:var(--gold)}.footer-social a svg[fill="#fff"]{fill:var(--gold)}
.wa-float{position:relative;width:62px;height:62px;background:#25D366;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 22px rgba(37,211,102,.5);transition:transform .25s;animation:wa-pulse 2.4s ease-out infinite}.wa-float:hover{transform:scale(1.08)}
@keyframes wa-pulse{0%{box-shadow:0 0 0 0 rgba(37,211,102,.55),0 4px 22px rgba(37,211,102,.5)}70%{box-shadow:0 0 0 16px rgba(37,211,102,0),0 4px 22px rgba(37,211,102,.5)}100%{box-shadow:0 0 0 0 rgba(37,211,102,0),0 4px 22px rgba(37,211,102,.5)}}
.wa-badge{position:absolute;top:-4px;right:-4px;background:#fff;color:#128C7E;font-family:Oswald,sans-serif;font-size:.62rem;font-weight:700;padding:2px 6px;border-radius:10px;box-shadow:0 2px 6px rgba(0,0,0,.35)}
.float-btn-wrap .wa-label{opacity:1;transform:none;border-color:rgba(37,211,102,.4)}
@media(max-width:768px){.contato-grid{grid-template-columns:1fr}.nav-ig{right:1rem}.float-btn-wrap .wa-label{display:none}}
@media(prefers-reduced-motion:reduce){.wa-float{animation:none}}
</style></head>'''
rep('</style></head>',CSS,1)

assert '1782' not in h, [m.start() for m in re.finditer('1782',h)]
assert VIP not in h
open(out,'w',encoding='utf-8').write(h)
print('ok',len(h))
