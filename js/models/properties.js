'use strict';

function get_property(json, name, dflt){
    let val = this._json.data[name];
    if (val === undefined){
        if (dflt === undefined){
            throw "Unknown property " + name;
        }
        return def;
    }

    // If property is object, use object factory to
    // initiate

    return val;
}
