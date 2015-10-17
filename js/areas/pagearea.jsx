'use strict';

import React from 'react';
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
        let pageFactory = React.createFactory(pageCtor);
        let page = pageFactory({resource});

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
