'use strict';

export default class ActionResponse{
    constructor(json){
        this._json = json;
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
        return this._json.embedded[ref];
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

    getAffectedFromEvent(eventName){
        return this._json.events[eventName] || [];
    }
}
