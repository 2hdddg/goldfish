'use strict';

import {setCallbacks as setCurrentPageCallbacks } from './infrastructure/currentpage';
import Server from './infrastructure/server';
import Sync from './infrastructure/sync';
import ModelFactory from './models/modelfactory';
import Application from './models/application';
import HeaderArea from './areas/headerarea';
import PageArea from './areas/pagearea';

export default function start(applicationJson){
    let server = new Server();
    let sync = new Sync();
    let modelFactory = new ModelFactory(server, sync);
    let application = new Application(
        applicationJson, server, modelFactory, sync);
    let headerArea = new HeaderArea(application, document.getElementById('account'));
    let pageArea = new PageArea(application, document.getElementById('content'));

    setCurrentPageCallbacks((url, resource) => {
        if (resource){
            application.current = resource;
            pageArea.render();
        }
        else{
            server
                .getJson(url)
                .then(json => {
                    application.current = json;
                    pageArea.render();
                });
        }
    });

    let rerender = () => {
        headerArea.render();
        pageArea.render();
    };

    application.subscribe('logged_in', rerender);
    application.subscribe('logged_out', rerender);

    rerender();
}
