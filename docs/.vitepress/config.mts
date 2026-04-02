import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'

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
    '/stroke',
    '/painting',
    '/symmetry',
    '/layers',
    '/settings',
    '/interface',
    '/tools',
    '/history',
    '/faq',
    '/tips',
]

function getSidebar(lang: string) {
    const dir = path.resolve(__dirname, lang.length ? `../i18n/${lang}` : `..`)

    const getTitle = (base: string) => {
        const file = base === '/' ? 'index.md' : base.slice(1) + '.md'
        const full = path.join(dir, file)
        const firstLine = fs.readFileSync(full, 'utf8').split('\n').find(l => l.trim().startsWith('#')) || ''
        return firstLine.replace(/^#+\s*/, '').replace(/!\[[^\]]*]\([^)]*\)\s*/g, '').replace(/\s*\{#.*?\}\s*$/, '').trim()
    }
    return [{
        items: order.map(base => ({
            text: getTitle(base),
            link: lang ? base === '/' ? `/${lang}/` : `/${lang}${base}` : base
        }))
    }]
}

function getLocaleTheme(lang: String) {
    return { sidebar: getSidebar(lang) }
}

// https://vitepress.dev/reference/site-config
let conf = {
    title: 'Nomad',
    description: 'Nomad Sculpt Manual',
    appearance: 'dark',
    outDir: '../dist/manual',

    cleanUrls: true,
    base: '/manual/',

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

    markdown: {
        config: md => {
            const colored = [
                'faceGroup.webp',
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
                'tool_smooth.webp'
            ]
            md.renderer.rules.image = function (tokens, idx, options, env, self) {
                const token = tokens[idx]
                const src = token.attrGet('src')
                if (src && src.startsWith('/videos')) {
                    var srcImg = src.replace('.mp4', '.webp')
                    var tag = '<video controls preload="metadata" poster="$0">'
                    tag += '<source src="$1" type="video/mp4">'
                    tag += '</video>\n'
                    tag = tag.replace('$0', srcImg)
                    tag = tag.replace('$1', src)
                    return tag
                }
                if (src && src.startsWith('/images')) {
                    token.attrJoin('class', 'image')
                }
                if (src && src.startsWith('/icons')) {
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

    rewrites: {
        'i18n/:locale/:file*': ':locale/:file*'
    },

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
};

// find docs -maxdepth 1 -name "*.md" -exec sed -i '' 's|\](/|\](./|g' {} +
// find docs/i18n -name "*.md" -exec sed -i '' 's|\](/|\](../../|g' {} +
// "mpa": "vitepress build --mpa docs",
if (false) {
    conf.mpa = true;
    conf.cleanUrls = false;
    conf.base = './';
}

export default defineConfig(conf)