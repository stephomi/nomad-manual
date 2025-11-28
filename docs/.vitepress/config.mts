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
        return firstLine.replace(/^#+\s*/, '').replace(/!\[[^\]]*]\([^)]*\)\s*/g, '').trim()
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
export default defineConfig({
    title: 'Nomad',
    description: 'Nomad Sculpt Manual',
    cleanUrls: true,
    appearance: 'dark',
    base: '/manual/',
    outDir: '../dist/manual',

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
            { icon: { svg: '<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Threads</title><path d="M12.186 24h-.007c-3.581-.024-6.334-1.205-8.184-3.509C2.35 18.44 1.5 15.586 1.472 12.01v-.017c.03-3.579.879-6.43 2.525-8.482C5.845 1.205 8.6.024 12.18 0h.014c2.746.02 5.043.725 6.826 2.098 1.677 1.29 2.858 3.13 3.509 5.467l-2.04.569c-1.104-3.96-3.898-5.984-8.304-6.015-2.91.022-5.11.936-6.54 2.717C4.307 6.504 3.616 8.914 3.589 12c.027 3.086.718 5.496 2.057 7.164 1.43 1.783 3.631 2.698 6.54 2.717 2.623-.02 4.358-.631 5.8-2.045 1.647-1.613 1.618-3.593 1.09-4.798-.31-.71-.873-1.3-1.634-1.75-.192 1.352-.622 2.446-1.284 3.272-.886 1.102-2.14 1.704-3.73 1.79-1.202.065-2.361-.218-3.259-.801-1.063-.689-1.685-1.74-1.752-2.964-.065-1.19.408-2.285 1.33-3.082.88-.76 2.119-1.207 3.583-1.291a13.853 13.853 0 0 1 3.02.142c-.126-.742-.375-1.332-.75-1.757-.513-.586-1.308-.883-2.359-.89h-.029c-.844 0-1.992.232-2.721 1.32L7.734 7.847c.98-1.454 2.568-2.256 4.478-2.256h.044c3.194.02 5.097 1.975 5.287 5.388.108.046.216.094.321.142 1.49.7 2.58 1.761 3.154 3.07.797 1.82.871 4.79-1.548 7.158-1.85 1.81-4.094 2.628-7.277 2.65Zm1.003-11.69c-.242 0-.487.007-.739.021-1.836.103-2.98.946-2.916 2.143.067 1.256 1.452 1.839 2.784 1.767 1.224-.065 2.818-.543 3.086-3.71a10.5 10.5 0 0 0-2.215-.221z"/></svg>' }, link: 'https://threads.net/nomadsculpt' },
            { icon: 'facebook', link: 'https://facebook.com/nomadsculpt' },
            { icon: 'github', link: 'https://github.com/stephomi/nomadsculpt.com' },
            { icon: 'discord', link: 'https://discord.com/invite/8h7BwpRz29' },
            // { icon: 'linkedin', link: 'https://www.linkedin.com/in/stéphane-ginier-74a89477' },
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
        zh_hans: { lang: 'zh-Hans', themeConfig: getLocaleTheme('zh-hans'), label: '简体中文' },
        zh_hant: { lang: 'zh-Hant', themeConfig: getLocaleTheme('zh-hant'), label: '繁體中文' },
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
        ar: { lang: 'ar', themeConfig: getLocaleTheme('ar'), label: 'العربية' },
        he: { lang: 'he', themeConfig: getLocaleTheme('he'), label: 'עברית' },
    },

})