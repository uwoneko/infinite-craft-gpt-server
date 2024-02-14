// ==UserScript==
// @name         Infinite Craft API Interceptor
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Redirects any infinity craft api requests to your localhost
// @author       yusp48
// @match        *://*.neal.fun/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const _oldFetch = window.fetch;
    window.fetch = function(url, ...args) {
        if (url.startsWith('https://neal.fun/api/infinite-craft/pair')) {
            url = url.replace('https://neal.fun/api/infinite-craft/pair', 'http://localhost:8000');
        }

        return _oldFetch.apply(this, [url, ...args]);
    };
})();
