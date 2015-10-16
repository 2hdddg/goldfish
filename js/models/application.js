'use strict';

import Model from './model'

export default class Application extends Model {

    constructor(json, server, factory, sync){
        super(json, server, factory, sync);
        this._current = null;
    }

    get current(){
        if (!this._current){
            // Check if backend has supplied us
            // with a current model
            let current_url = this._json.data.current_url;
            if (current_url){
                let embedded = this._json.embedded[current_url];
                this._current = this._factory.createFromJson(embedded);
            }
        }
        return this._current;
    }

    set current(json){
        // Special case happens when trying to
        // set application as current, this actually
        // means that we should use the initial embedded
        // model as current (if there is one)
        if (json.cls === this._json.cls){
            this._current = null;
        }
        else{
            this._current = this._factory.createFromJson(json);
        }
    }
}
