'use strict';

import {setCallbacks as setCurrentPageCallbacks } from './infrastructure/currentpage';
import Server from './infrastructure/server';
import Application from './models/application';
import HeaderArea from './areas/headerarea';
import PageArea from './areas/pagearea';

export default function start(applicationJson){
    let server = new Server();
    let application = new Application(
        applicationJson, server);
    let accountArea = new HeaderArea(application, document.getElementById('account'));
    let pageArea = new PageArea(application, document.getElementById('content'));

    setCurrentPageCallbacks(url => {
        server
            .getJson(url)
            .then(json => {
                application.current = json;
                pageArea.render();
            });
    });

    application.on('login', (/*event, model*/) => {
        debugger;
        accountArea.render();
        pageArea.render();
    });

    accountArea.render();
    pageArea.render();
}
