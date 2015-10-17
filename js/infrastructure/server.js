'use strict';

import 'whatwg-fetch';
import log from './log';

function _checkStatus(response){
    if (response.status >= 200 && response.status < 300){
        return response;
    }
    var error = new Error(response.statusText);
    error.response = response;
    throw error;
}

class Server{
    getJson(url){
        log.info(() => "Getting " + url + " from server");
        return fetch(url, {
                credentials: 'same-origin',
                headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json',
                    // For Flask is_xhr to work
                    'X-Requested-With': 'XMLHttpRequest'
                },
            })
            .then(_checkStatus)
            .then(response => response.json());
    }

    postJson(url, json){
        log.info(() => "Posting data to server at " + url);
        let body = JSON.stringify(json);

        return fetch(url, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-type': 'application/json',
                    // For Flask is_xhr to work
                    'X-Requested-With': 'XMLHttpRequest'
                },
                credentials: 'same-origin',
                body: body
            })
            .then(_checkStatus)
            .then(response => response.json());
    }
}

export default Server;