'use strict';

export default class Action {
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
            .then(json => this._onSubmit(json));
    }
}
