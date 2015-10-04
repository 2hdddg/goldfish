'use strict';

import Subscriptions from '../infrastructure/subscriptions.js'

class Action {
    constructor(name, json, server, onSubmit){
        this._name = name;
        this._json = json;
        this._server = server;
        this._onSubmit = onSubmit;
    }

    getFormFields(){
        return this._json.form;
    }

    submit(data){
        return this._server
            .postJson(this._json.ref, data)
            .then(json => {
                this._onSubmit(json);
                return true;
            });
    }
}

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

    getAction(name){
        let json = this._json.actions[name];
        if (!json){
            throw "Unable to find json for action named " + name;
        }
        let onSubmit = (responseJson) => {
            this._json = responseJson;
            this._actionCompleted(name);
        };
        return new Action(name, json, this._server, onSubmit);
    }

    hasAction(name){
        let json = this._json.actions[name];
        return !!json;
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