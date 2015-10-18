'use strict';

import Subscriptions from '../infrastructure/subscriptions.js';
import log from '../infrastructure/log.js';
import Action from './action';
import ActionResponse from './actionresponse';
import { get_property } from './properties';

export default class Resource {
    constructor(json, server, factory, sync){
        this._server = server;
        this._json = json;
        this._factory = factory;
        this._sync = sync;
        this._syncing = null;
        this._subscriptions = null;
        this._onSyncCallback = this._onSyncCallback.bind(this);
    }

    get ref(){
        return this._json.ref;
    }

    get cls(){
        return this._json.cls;
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

    getAction(name){
        let json = this._json.actions[name];
        if (!json){
            throw "Unable to find json for action named " + name;
        }

        let onSubmit = (actionJson) => {
            let actionResponse = new ActionResponse(actionJson, this._factory);
            this._sync.onAction(actionResponse);
            return actionResponse;
        };
        return new Action(name, json, this._server, onSubmit);
    }

    hasAction(name){
        let json = this._json.actions[name];
        return !!json;
    }

    _repr(){
        return this.ref + "[" + 0 + "]";
    }

    _onSyncCallback(data){
        // Update my own state
        if (data.model){
            this._json = data.model._json;
            log.info(() => "Updated resource " + this._repr() + " with fresh json.");
        }

        // Notify all my subscribers
        data.events.forEach(eventName =>
            this._subscriptions.publish(eventName, this));
    }

    subscribe(name, callback){
        if (!this._syncing){
            this._syncing = this._sync.start(this, this._onSyncCallback);
            log.info(() => "Registered resource " + this._repr() + " for sync.");
        }

        if (!this._subscriptions){
            this._subscriptions = new Subscriptions();
        }

        return this._subscriptions.add(name, eventData => {
            log.info(() => "Got event '" + name + "' on " + this._repr() + ", passing on...");
            callback(name, eventData);
        });
    }

    unsubscribe(subscription){
        this._subscriptions.remove(subscription);
        if (this._subscriptions.empty()){
            this._syncing.stop();
            this._syncing = null;
            log.info(() => "Unregistered resource " + this._repr() + " for sync.");
        }
    }

    getLink(name){
        return this._json.links[name];
    }

    hasLink(name){
        return !!this.getLink(name);
    }
}
