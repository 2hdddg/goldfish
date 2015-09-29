'use strict';

let _onOpen = (() => { throw "Routing not initialized"; });

export function setCallbacks(onOpen){
    _onOpen = onOpen;
}

export function open(url){
    window.history.pushState(null, null, url);
    _onOpen(url);
}

export function state(s){
}

window.onpopstate = function(event){
    let url = document.location;
    _onOpen(url);
}