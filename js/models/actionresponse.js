'use strict';

export default class ActionResponse{
    constructor(json, factory){
        this._json = json;
        this._factory = factory;
    }

    get references(){
        let refs = new Set();
        for (let name in this._json.events){
            let targets = this._json.events[name];
            targets.forEach(target => refs.add(target.ref));
        }
        for (let e in this._json.embedded){
            refs.add(this._json.embedded[e].ref);
        }
        return refs;
    }

    getEmbeddedFromRef(ref){
        let json = this._json.embedded[ref];
        if (json){
            let model = this._factory.createFromJson(json);
            return model;
        }
        return;
    }

    getEventsFromRef(ref){
        let events = [];
        for (let eventName in this._json.events){
            let refs = this._json.events[eventName];
            if (refs.some(x => x.ref === ref)){
                events.push(eventName);
            }
        }
        return events;
    }

    getEmbeddedFromEvent(eventName){
        let affected = this._json.events[eventName] || [];
        let embedded = [];
        affected.forEach(repr => {
            let resource = this.getEmbeddedFromRef(repr.ref);
            if (resource){
                embedded.push(resource);
            }
        });
        return embedded;
    }
}
