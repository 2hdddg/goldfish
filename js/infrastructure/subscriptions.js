'use strict';

class Subscriptions{
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
    }

    remove(callback){
    }

    publish(name, data){
        let subscriptions = this.get(name);
        for (let subscription of subscriptions){
           window.setTimeout(function(){
                let event = Object.assign({name}, data);
                subscription(event);
            }, 1);
        }
    }
}

export default Subscriptions;