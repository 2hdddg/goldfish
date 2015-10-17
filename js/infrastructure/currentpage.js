'use strict';

import log from './log';

let _onOpen = (() => { throw "Routing not initialized"; });

export function setCallbacks(onOpen){
    _onOpen = onOpen;
}

export function open(url){
    log.info(() => "Navigating to " + url);
    window.history.pushState(null, null, url);
    _onOpen(url);
}

export function state(s){
}

window.onpopstate = function(event){
    let url = document.location;
    log.info(() => "Going back to " + url);
    _onOpen(url);
}