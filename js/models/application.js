'use strict';

import Resource from './resource'

export default class Application extends Resource {

    constructor(json, server, factory, sync){
        super(json, server, factory, sync);
        this._current = null;
    }

    get current(){
        if (!this._current){
            // Check if backend has supplied us
            // with a current resource
            let current_link = this.getLink('current');
            if (current_link){
                let embedded = this._json.embedded[current_link];
                this._current = this._factory.createFromJson(embedded);
            }
        }
        return this._current;
    }

    set current(json){
        // Special case happens when trying to
        // set application as current, this actually
        // means that we should use the initial embedded
        // resource as current (if there is one)
        if (json.cls === this._json.cls){
            this._current = null;
        }
        else{
            this._current = this._factory.createFromJson(json);
        }
    }
}
