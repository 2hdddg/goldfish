'use strict';

import Model from './model'
import * as models from './models';

function _createModelFromJson(json, server){
    let cls = json.cls;

    if (!cls){
        throw "Can not create model from nothing";
    }

    let ctor = models[cls];
    if (!ctor){
        throw "Unable to find model constructor named:" + cls;
    }

    return new ctor(json, server)
}

export default class Application extends Model {
    constructor(json, server){
        super(json, server);
        this._current = null;
    }

    canLogin(){
        return this._hasAction('login');
    }

    login(username, password){
        let loginUrl = this._getAction('login');

        return this._server
            .postJson(loginUrl, {
                username: username,
                password: password
            })
            .then(json => {
                this._json = json;
                this._actionCompleted('login');
                return true;
            });
    }

    get current(){
        if (!this._current){
            // Check if backend has supplied us
            // with a current model
            let embedded = this._json.embedded.current;
            if (embedded){
                this._current =_createModelFromJson(embedded, this._server);
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
            this._current = _createModelFromJson(json, this._server);
        }
    }
}
