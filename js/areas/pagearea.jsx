'use strict';

import React from 'react';
import * as pages from '../pages/pages';

export default class PageArea{
    constructor(application, atElement){
        this._application = application;
        this._atElement = atElement;
    }

    _renderAnonymous(){
        return (<span>No model... anonym</span>);
    }

    _render(model){
        let cls = model.cls;
        let pageCtor = pages[cls];
        let pageFactory = React.createFactory(pageCtor);
        let page = pageFactory({model});

        return page;
    }

    render(){
        let model = this._application.current;
        let html = model ?
            this._render(model) : this._renderAnonymous();

        React.render(
            html,
            this._atElement
        );
    }
}
