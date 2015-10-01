'use strict';

import Subscriptions from '../infrastructure/subscriptions.js'

class Model {
    constructor(json, server){
        this._server = server;
        this._subscriptions = null;
        this._json = json;
    }

    get ref(){
        return this._json.ref;
    }

    get cls(){
        return this._json.cls;
    }

    _getAction(name){
        return this._json.actions[name];
    }

    _hasAction(name){
        return !!this._getAction(name);
    }

    _actionCompleted(name){
        if (this._subscriptions){
            this._subscriptions.publish(name, {model:this});
        }
    }

    on(name, callback){
        if (!this._subscriptions){
            this._subscriptions = new Subscriptions();
        }
        this._subscriptions.add(name, callback);
    }

    getLink(name){
        return this._json.links[name];
    }

    hasLink(name){
        return !!this.getLink(name);
    }
}

export default Model;