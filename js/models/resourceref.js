'use strict';

import { get_property } from './properties';

export default class ResourceRef {
    constructor(json, server, factory, sync){
        this._json = json;
        this._factory = factory;
    }

    get ref(){
        return this._json.ref;
    }

    get cls(){
        return this._json.cls;
    }

    get refcls(){
        return this._json.refcls;
    }

    property(name, dflt){
        return get_property(
            {
                json: this._json,
                name,
                dflt,
                factory: this._factory
            });
    }
}

