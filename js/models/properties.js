'use strict';

import log from '../infrastructure/log.js';

let _conversions = {
    'undefined': () => undefined,
    'boolean': b => b,
    'number': n => n,
    'string': s => s,
    'object': (o, f) => _convertObject(o, f)
}

function _convertObject(o, factory){
    if (o === null){
        return null;
    }

    if (Array.isArray(o)){
        return o.map(x => _convert(x));
    }

    if (o.cls){
        return factory.createFromJson(o);
    }
}

function _convert(val, factory){
    let converter = _conversions[typeof val];
    if (!converter){
        throw "Unable to find property converter for " + val;
    }

    return converter(val, factory);
}

export function get_property(params){
    let {json, name, dflt, factory} = params;

    let val = json.data[name];
    if (val === undefined){
        if (dflt === undefined){
            throw "Unknown property " + name;
        }
        return def;
    }

    return _convert(val, factory);
}
