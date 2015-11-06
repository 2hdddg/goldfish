'use strict';

import React from 'react';
import log from '../infrastructure/log';
import * as pages from '../pages/pages';

export default class PageArea{
    constructor(application, atElement){
        this._application = application;
        this._atElement = atElement;
    }

    _renderAnonymous(){
        return (<span>Nothing to show... anonym</span>);
    }

    _render(resource){
        let cls = resource.cls;
        let pageCtor = pages[cls];

        if (!pageCtor){
            log.error(() => "Unable to find pagearea view for: " + cls);
            throw "Unable to find pagearea view for: " + cls;
        }

        let pageFactory = React.createFactory(pageCtor);
        let page = pageFactory({resource});

        log.info(() => "Rendering view in pagearea for " + cls);

        return page;
    }

    render(){
        let resource = this._application.current;
        let html = resource ?
            this._render(resource) : this._renderAnonymous();

        React.render(
            html,
            this._atElement
        );
    }
}
