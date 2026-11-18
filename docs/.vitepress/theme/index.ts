// https://vitepress.dev/guide/custom-theme
import './style.css'
import 'virtual:sidebar-icons.css'

import mediumZoom from 'medium-zoom';
import { useRoute } from 'vitepress';
import Theme from 'vitepress/theme'
import { h, nextTick, onMounted, watch } from 'vue'
import { setupOutlineIcons } from './outlineIcons'

export default {
    extends: Theme,
    Layout: () => {
        return h(Theme.Layout, null, {
            // https://vitepress.dev/guide/extending-default-theme#layout-slots
        })
    },
    enhanceApp({ app, router, siteData }) {
        // ...
    },

    // https://github.com/francoischalifour/medium-zoom
    setup() {
        const route = useRoute();
        const initZoom = () => {
            // screenshots only (class set by the markdown renderer), not icons: the built src
            // of both is a hashed /assets/ file
            var images = document.querySelectorAll('img.image');
            new mediumZoom(images, {
                background: 'var(--vp-c-bg)',
                scrollOffset: 10,
            });
        };
        onMounted(() => {
            initZoom();
            setupOutlineIcons();
        });
        watch(
            () => route.path,
            () => nextTick(() => initZoom())
        );
    }
}
