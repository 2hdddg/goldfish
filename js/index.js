'use strict';

import {setCallbacks as setCurrentPageCallbacks } from './infrastructure/currentpage';
import Server from './infrastructure/server';
import Sync from './infrastructure/sync';
import ModelFactory from './models/modelfactory';
import Application from './models/application';
import HeaderArea from './areas/headerarea';
import PageArea from './areas/pagearea';
import log from './infrastructure/log';

export default function start(applicationJson){
    let server = new Server();
    let sync = new Sync();
    let modelFactory = new ModelFactory(server, sync);
    let application = new Application(
        applicationJson, server, modelFactory, sync);
    let headerArea = new HeaderArea(application, document.getElementById('header'));
    let pageArea = new PageArea(application, document.getElementById('content'));

    let renderErrorPage = error => {
        application.current = {
            cls: 'Error'
        };
        pageArea.render();
    };

    let renderResource = resource => {
        application.current = resource;
        try {
            pageArea.render();
        }
        catch(e){
            log.error(() => "Failed to render resource: " + e);
            renderErrorPage(e);
            throw e;
        }
    };


    setCurrentPageCallbacks((url, resource) => {
        if (resource){
            renderResource(resource);
        }
        else{
            server
                .getJson(url)
                .then(json => {
                    renderResource(json);
                })
                .catch(e => {
                    log.error(() => "Resource load failed: " + e);
                    renderErrorPage(e);
                });
        }
    });

    let rerender = () => {
        headerArea.render();
        try {
            pageArea.render();
        }
        catch (e){
            log.error(() => "Failed to render built-in resource: " + e);
            renderErrorPage(e);
            throw e;
        }
    };

    application.subscribe('logged_in', rerender);
    application.subscribe('logged_out', rerender);

    rerender();
}
