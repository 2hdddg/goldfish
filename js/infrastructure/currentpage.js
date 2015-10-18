'use strict';

import log from './log';

let _onOpen = (() => { throw "Routing not initialized"; });

export function setCallbacks(onOpen){
    _onOpen = onOpen;
}

export function open(urlOrModel){
    let url, resource;

    if (typeof urlOrModel === 'string'){
        url = urlOrModel;
    }
    else if (urlOrModel.ref && urlOrModel.cls){
        url = urlOrModel.ref;
        if (!urlOrModel.refcls){
            resource = urlOrModel;
        }
    }

    if (!url){
        throw "Can not determine url from " + urlOrModel;
    }

    log.info(() => "Navigating to " + url + (resource ? ", need no request already got data" : ""));
    window.history.pushState(null, null, url);
    _onOpen(url, resource);
}

export function state(s){
}

window.onpopstate = function(event){
    let url = document.location;
    log.info(() => "Going back to " + url);
    _onOpen(url);
}