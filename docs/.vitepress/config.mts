import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'

// pixel size of a docs image (webp, png, gif), so each <img> carries width/height: the browser reserves
// its space before it loads, and a search result or #anchor link lands on its heading instead of
// being pushed down by the images that load above it
const imageSizes = new Map<string, [number, number] | null>()
function imageSize(src: string): [number, number] | null {
    if (imageSizes.has(src)) return imageSizes.get(src)!
    let size: [number, number] | null = null
    try {
        const b = fs.readFileSync(path.resolve(__dirname, '..', src.replace(/^\//, '')))
        const tag = b.toString('ascii', 12, 16)
        if (b.toString('ascii', 0, 4) === 'RIFF' && tag === 'VP8X') {
            size = [1 + b.readUIntLE(24, 3), 1 + b.readUIntLE(27, 3)]
        } else if (tag === 'VP8 ') {
            size = [b.readUInt16LE(26) & 0x3fff, b.readUInt16LE(28) & 0x3fff]
        } else if (tag === 'VP8L') {
            const bits = b.readUInt32LE(21)
            size = [1 + (bits & 0x3fff), 1 + ((bits >> 14) & 0x3fff)]
        } else if (b.toString('ascii', 1, 4) === 'PNG') {
            size = [b.readUInt32BE(16), b.readUInt32BE(20)]
        } else if (b.toString('ascii', 0, 3) === 'GIF') {
            size = [b.readUInt16LE(6), b.readUInt16LE(8)]
        }
    } catch { }
    imageSizes.set(src, size)
    return size
}

const IS_MPA = false;
const ONLY_EN = false;

const order = [
    '/',
    '/gettingstarted',
    '/files',
    '/scene',
    '/topology',
    '/material',
    '/shading',
    '/postprocess',
    '/background',
    '/camera',
    '/transform',
    '/stroke',
    '/painting',
    '/symmetry',
    '/operation',
    '/layers',
    '/settings',
    '/interface',
    '/tools',
    '/history',
    '/faq',
    '/tips',
]

// icons found in page titles, turned into css by the sidebar-icons plugin
const sidebarIcons = new Set<string>()

function getSidebar(lang: string) {
    const dir = path.resolve(__dirname, lang.length ? `../i18n/${lang}` : `..`)
    const fileOf = (base: string) => base === '/' ? 'index.md' : base.slice(1) + '.md'
    // a page not translated yet (new English page, before the sync pass): the English one stands in
    const translated = (base: string) => fs.existsSync(path.join(dir, fileOf(base)))

    const getText = (base: string) => {
        const full = translated(base) ? path.join(dir, fileOf(base)) : path.resolve(__dirname, '..', fileOf(base))
        const firstLine = fs.readFileSync(full, 'utf8').split('\n').find(l => l.trim().startsWith('#')) || ''
        const icon = firstLine.match(/!\[[^\]]*]\(\/icons\/([^)]+)\.webp\)/)?.[1]
        const title = firstLine.replace(/^#+\s*/, '').replace(/!\[[^\]]*]\([^)]*\)\s*/g, '').replace(/\s*\{#.*?\}\s*$/, '').trim()
        if (icon) sidebarIcons.add(icon)
        // empty span for pages without icon, to keep titles aligned
        return `<span class="sidebar-icon"${icon ? ` data-icon="${icon}"` : ''}></span>${title}`
    }
    return [{
        items: order.map(base => ({
            text: getText(base),
            link: lang && translated(base) ? base === '/' ? `/${lang}/` : `/${lang}${base}` : base
        }))
    }]
};

// strings of the theme itself (outline title, page footer, search box...): locales/<lang>.json,
// same keys as locales/en.json. A locale without its file keeps the English defaults.
function uiStrings(lang: string) {
    const file = path.resolve(__dirname, 'locales', `${lang}.json`)
    return fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, 'utf8')) : null
}

function getLocaleTheme(lang: string) {
    const ui = uiStrings(lang)
    if (!ui) return { sidebar: getSidebar(lang) }
    const { outlineLabel, ...theme } = ui.theme
    return {
        ...theme,
        sidebar: getSidebar(lang),
        outline: { level: 'deep', label: outlineLabel },
        nav: [
            { text: ui.nav.home, link: 'https://nomadsculpt.com' },
            { text: ui.nav.forum, link: 'https://forum.nomadsculpt.com' }
        ],
    }
}

function searchLocales() {
    const locales: Record<string, { translations: object }> = {}
    for (const file of fs.readdirSync(path.resolve(__dirname, 'locales'))) {
        const lang = file.replace(/\.json$/, '')
        if (lang !== 'en') locales[lang] = { translations: uiStrings(lang).search }
    }
    return locales
}

// https://vitepress.dev/reference/site-config
let conf = {
    title: 'Nomad',
    description: 'Nomad Sculpt Manual',
    appearance: 'dark',
    outDir: '../dist/manual',

    cleanUrls: IS_MPA ? false : true,
    base: IS_MPA ? './' : '/manual/',
    mpa: IS_MPA,

    // https://vitepress.dev/reference/default-theme-config
    themeConfig: {
        siteTitle: '',
        logo: {
            light: '/logo_black.png',
            dark: '/logo_white.png',
        },

        nav: [
            { text: 'Home', link: 'https://nomadsculpt.com' },
            { text: 'Forum', link: 'https://forum.nomadsculpt.com' }
        ],

        sidebar: getSidebar(''),

        outline: { level: 'deep' },
        // aside : false,

        search: {
            provider: 'local',
            // https://lucaong.github.io/minisearch/classes/_minisearch_.minisearch.html
            options: {
                locales: searchLocales(),
                miniSearch: {
                    options: {},
                    searchOptions: {
                        // fuzzy : 0.2,
                        // prefix : true,
                        // boost : { title : 4, text : 2, titles : 1 },
                    },
                },
            },
        },

        // https://github.com/vuejs/vitepress/blob/main/src/client/theme-default/support/socialIcons.ts
        // https://simpleicons.org/
        socialLinks: [
            { icon: 'x', link: 'https://x.com/nomadsculpt' },
            { icon: 'instagram', link: 'https://instagram.com/nomadsculpt' },
            { icon: 'threads', link: 'https://threads.net/nomadsculpt' },
            { icon: 'facebook', link: 'https://facebook.com/nomadsculpt' },
            { icon: 'github', link: 'https://github.com/stephomi/nomadsculpt.com' },
            { icon: 'discord', link: 'https://discord.com/invite/8h7BwpRz29' },
            // { icon: 'linkedin', link: 'https://www.linkedin.com/company/81461884/admin/dashboard/' },
            // { icon: 'youtube', link: '' },
            // { icon: 'mastodon', link: '' },
            // { icon: 'slack', link: '' },
        ]
    },

    vite: {
        plugins: [{
            name: 'sidebar-icons',
            resolveId: id => id === 'virtual:sidebar-icons.css' ? '\0virtual:sidebar-icons.css' : undefined,
            load: id => {
                if (id !== '\0virtual:sidebar-icons.css') return
                return [...sidebarIcons].map(icon => {
                    const url = `url(/icons/${icon}.webp)`
                    return `.sidebar-icon[data-icon="${icon}"] { -webkit-mask-image: ${url}; mask-image: ${url}; }`
                }).join('\n')
            }
        }]
    },

    markdown: {
        config: md => {
            const colored = [
                'group.webp',
                'group_to_mask.webp',
                'group_separate.webp',
                'gizmo.webp',
                'flag_',
                'tool_planar.webp',
                'tool_pinch.webp',
                'tool_paint.webp',
                'tool_nudge.webp',
                'tool_move.webp',
                'tool_layer.webp',
                'tool_inflate.webp',
                'tool_gizmo.webp',
                'tool_flatten.webp',
                'tool_faceGroup.webp',
                'tool_drag.webp',
                'tool_crease.webp',
                'tool_clearLayer.webp',
                'tool_clay.webp',
                'tool_brush.webp',
                'tool_stamp.webp',
                'tool_smooth.webp',
                'tool_smudge.webp',
                'tool_polish.webp',
                'tool_elastic.webp',
                'tool_vdm.webp'
            ]
            md.renderer.rules.image = function (tokens, idx, options, env, self) {
                const token = tokens[idx]
                const src = token.attrGet('src')
                if (src && src.includes('/videos')) {
                    var srcImg = src.replace('.mp4', '.webp')
                    const vsize = imageSize(srcImg)
                    var tag = '<video controls preload="metadata" poster="$0"' +
                        (vsize ? ` width="${vsize[0]}" height="${vsize[1]}"` : '') + '>'
                    tag += '<source src="$1" type="video/mp4">'
                    tag += '</video>\n'
                    tag = tag.replace('$0', srcImg)
                    tag = tag.replace('$1', src)
                    return tag
                }
                if (src && src.includes('/images')) {
                    token.attrJoin('class', 'image')
                    const size = imageSize(src)
                    if (size) {
                        token.attrSet('width', String(size[0]))
                        token.attrSet('height', String(size[1]))
                    }
                }
                if (src && src.includes('/icons')) {
                    token.attrJoin('class', 'icon')
                    if (!colored.some(color => src.includes(color))) token.attrJoin('class', 'can_invert')
                }
                return self.renderToken(tokens, idx, options)
            }
        }
    },

    head: [
        ['link', { rel: 'icon', href: '/favicon.ico' }],
        ['meta', { name: 'theme-color', content: '#ebbe6c' }],
        ['meta', { name: 'mobile-web-app-capable', content: 'yes' }],
        ['meta', { name: 'apple-mobile-web-app-title', content: 'Nomad Sculpt' }],
        ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
        ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
        ['script', { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-DSF8ZS1RCC' }],
        [
            'script', {},
            `window.dataLayer = window.dataLayer || [];
            function gtag() { dataLayer.push(arguments); } gtag('js', new Date()); gtag('config', 'G-DSF8ZS1RCC');`
        ]
    ],

    locales: {
        root: { lang: 'en', label: 'English' },
        "zh-hans": { lang: 'zh-Hans', themeConfig: getLocaleTheme('zh-hans'), label: '简体中文' },
        "zh-hant": { lang: 'zh-Hant', themeConfig: getLocaleTheme('zh-hant'), label: '繁體中文' },
        ja: { lang: 'ja', themeConfig: getLocaleTheme('ja'), label: '日本語' },
        ko: { lang: 'ko', themeConfig: getLocaleTheme('ko'), label: '한국어' },
        th: { lang: 'th', themeConfig: getLocaleTheme('th'), label: 'ไทย' },
        cs: { lang: 'cs', themeConfig: getLocaleTheme('cs'), label: 'Čeština' },
        de: { lang: 'de', themeConfig: getLocaleTheme('de'), label: 'Deutsch' },
        es: { lang: 'es', themeConfig: getLocaleTheme('es'), label: 'Español' },
        fr: { lang: 'fr', themeConfig: getLocaleTheme('fr'), label: 'Français' },
        it: { lang: 'it', themeConfig: getLocaleTheme('it'), label: 'Italiano' },
        id: { lang: 'id', themeConfig: getLocaleTheme('id'), label: 'Bahasa Indonesia' },
        ms: { lang: 'ms', themeConfig: getLocaleTheme('ms'), label: 'Melayu' },
        nl: { lang: 'nl', themeConfig: getLocaleTheme('nl'), label: 'Nederlands' },
        pl: { lang: 'pl', themeConfig: getLocaleTheme('pl'), label: 'Polski' },
        pt: { lang: 'pt', themeConfig: getLocaleTheme('pt'), label: 'Português' },
        ru: { lang: 'ru', themeConfig: getLocaleTheme('ru'), label: 'Русский' },
        sv: { lang: 'sv', themeConfig: getLocaleTheme('sv'), label: 'Svenska' },
        tr: { lang: 'tr', themeConfig: getLocaleTheme('tr'), label: 'Türkçe' },
        vi: { lang: 'vi', themeConfig: getLocaleTheme('vi'), label: 'Tiếng Việt' },
        hi: { lang: 'hi', themeConfig: getLocaleTheme('hi'), label: 'हिन्दी' },
        ar: { lang: 'ar', themeConfig: getLocaleTheme('ar'), label: 'العربية', dir: 'rtl' },
        he: { lang: 'he', themeConfig: getLocaleTheme('he'), label: 'עברית', dir: 'rtl' },
    },

    rewrites: {
        'i18n/:locale/:file*': ':locale/:file*'
    },

    async transformHtml(code, id) {
        if (!this.mpa) return code;

        const isLocale = Object.keys(conf.locales).some(k => k !== 'root' && id.replace(/\\/g, '/').includes(`/${k}/`));
        const prefix = isLocale ? '../' : './';
        const baseReg = conf.base.replace(/\//g, '\\/');

        return code
            // 1. Fix assets (CSS, JS, images)
            .replace(/(src|href)="(?:\.\/|\/)(assets|icons|images|videos)\//g, `$1="${prefix}$2/`)
            // 2. Fix internal links for offline (append index.html / .html)
            .replace(new RegExp(`href="(?:${baseReg}|\\/)(?!http|\\/\\/|mailto)([^"]*)"`, 'g'), (_, p) => {
                p = p.replace(/^\//, '');
                p = (p === '' || p.endsWith('/')) ? p + 'index.html' : (!p.includes('.') ? p + '.html' : p);
                return `href="${prefix}${p}"`;
            });
    }
};

if (ONLY_EN) {
    conf.rewrites = {};
    conf.locales = {};
    conf.srcExclude = ['i18n/**'];
    conf.themeConfig.sidebar = getSidebar('');
}

export default defineConfig(conf)