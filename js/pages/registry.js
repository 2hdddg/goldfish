'use strict';

import log from '../infrastructure/log';

let registry = {};

export function register(cls, ctor){
    let existing = registry[cls];
    if (existing){
        log.warn(() => "Double registration of page for " + cls);
    }

    log.info(() => "Registering page " + ctor.name + " for resource class " + cls);
    registry[cls] = ctor;
}

export function lookup(cls){
    let ctor = registry[cls];
    if (!ctor){
        log.error(() => "Failed to find page for resource class " + cls);
    }
    return ctor;
}