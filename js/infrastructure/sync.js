'use strict';

import Subscriptions from './subscriptions.js';
import log from './log.js';

export default class Sync{
    constructor(){
        this._subscriptions = new Subscriptions();
    }

    onAction(actionResponse){
        let references = actionResponse.references;

        references.forEach(ref => {
            let data = {
                events: actionResponse.getEventsFromRef(ref),
                modelJson: actionResponse.getEmbeddedFromRef(ref)
            };
            log.info("Publishing action response for " + ref + " " +
                (data.modelJson ? "with data" : "without data") +
                " and " +
                (data.events && data.events.length ? ("events:" + data.events) : "no events"));
            this._subscriptions.publish(ref, data);
        });
    }

    start(model, callback){
        let ref = model.ref;
        let subscription = this._subscriptions.add(ref, (eventname, eventdata) => {
            callback(eventdata);
        });

        return {
            stop: () => {
                this._subscriptions.remove(subscription);
            }
        }
    }
}
