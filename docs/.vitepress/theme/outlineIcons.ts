// Icons in the "On this page" outline (the aside and the mobile dropdown).
// VitePress builds the outline from the headings' text only, so the heading icons are lost:
// each outline link gets a copy of its heading's icon, or an empty slot to keep the text aligned.
// The outline renders lazily (the dropdown only exists while open) and Vue rewrites a link's text
// when the page changes (which drops the icon), so the links are watched and decorated again.

function decorate(link: HTMLAnchorElement) {
    const id = decodeURIComponent(link.hash.slice(1))
    const current = link.querySelector('.outline-icon')
    if (current && link.dataset.iconFor === id) return
    current?.remove()
    link.dataset.iconFor = id

    const heading = id ? document.getElementById(id) : null
    const src = heading?.querySelector<HTMLImageElement>('img[src*="/icons/"]')
    const icon = document.createElement(src ? 'img' : 'span')
    icon.className = 'outline-icon'
    if (src) {
        const img = icon as HTMLImageElement
        img.src = src.src
        img.alt = ''
        // light mode inverts the white icons, not the colored ones (same rule as the page)
        if (src.classList.contains('can_invert')) img.classList.add('can_invert')
    }
    link.prepend(icon)
}

function scan(root: ParentNode) {
    root.querySelectorAll<HTMLAnchorElement>('a.outline-link').forEach(decorate)
}

export function setupOutlineIcons() {
    scan(document)
    new MutationObserver(records => {
        for (const r of records) {
            const target = r.target instanceof Element ? r.target : r.target.parentElement
            const link = target?.closest<HTMLAnchorElement>('a.outline-link')
            if (link) decorate(link)
            r.addedNodes.forEach(n => { if (n instanceof Element) scan(n) })
        }
    }).observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ['href'] })
}
