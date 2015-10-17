'use strict';

export function get_property(params){
    let {json, name, dflt, factory} = params;

    let val = json.data[name];
    if (val === undefined){
        if (dflt === undefined){
            throw "Unknown property " + name;
        }
        return def;
    }

    if (val !== null && typeof val === 'object'){
        return factory.createFromJson(val);
    }

    return val;
}
