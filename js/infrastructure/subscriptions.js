'use strict';

export default class Subscriptions{
    constructor(){
        this._subscriptions = {};
    }

    get(name){
        let subscribers = this._subscriptions[name] || [];
        return subscribers;
    }

    add(name, callback){
        let subscribers = this.get(name);
        subscribers.push(callback);
        this._subscriptions[name] = subscribers;
        return { name, callback };
    }

    remove(subscription){
        let subscribers = this.get(subscription.name);
        if (!subscribers){
            return;
        }

        let subscribers_left = subscribers.filter(s => s !== subscription.callback);

        if (subscribers_left.length > 0){
            this._subscriptions[name] = subscribers_left;
        }
        else{
            delete this._subscriptions[name];
        }
    }

    publish(name, data){
        let subscriptions = this.get(name);
        for (let subscription of subscriptions){
           window.setTimeout(function(){
                subscription(name, data);
            }, 1);
        }
    }
}
