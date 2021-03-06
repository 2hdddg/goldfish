'use strict';

import Application from './application';
import Resource from './resource';
import Representation from './representation';
import log from '../infrastructure/log';

export default class ModelFactory{
    constructor(server, sync){
        this._server = server;
        this._sync = sync;
        this._concretes = {
            'Application': Application,
            'Representation': Representation
        }
    }

    createFromJson(json){
        if (!json){
            log.error(() => "ModelFactory: No json to create model from.");
            throw "Can not create model from nothing";
        }

        let cls = json.cls;

        if (!cls){
            log.error(() => "ModelFactory: Json has no cls property.");
            throw "Can not create model without cls";
        }

        let ctor = this._concretes[cls];
        if (ctor){
            log.info(() => "Creating concrete model instance: " + cls);
            return new ctor(json, this._server, this);
        }

        log.info(() => "Creating generic model instance: " + cls);
        return new Resource(json, this._server, this, this._sync);
    }
}
