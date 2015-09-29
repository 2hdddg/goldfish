'use strict';

import {setCallbacks as setCurrentPageCallbacks } from './infrastructure/currentpage';
import Server from './infrastructure/server';
import Application from './models/application';
import AccountArea from './areas/accountarea';
import ContentArea from './areas/contentarea';

function start(applicationJson){
    let server = new Server();
    let application = new Application(
        applicationJson, server);
    let accountArea = new AccountArea(application, document.getElementById('account'));
    let contentArea = new ContentArea(application, document.getElementById('content'));

    setCurrentPageCallbacks(url => {
        server
            .getJson(url)
            .then(json => {
                application.current = json;
                contentArea.render();
            });
    });

    application.on('login', (/*event, model*/) => {
        accountArea.render();
        contentArea.render();
    });

    accountArea.render();
    contentArea.render();
}

export default start;