'use strict';

import React from 'react';

export class UserTemplate extends React.Component {

    constructor(){
        super();
        this.state = {
            isBusy: false,
            validationMessage: ''
        };
    }

    render(){
        let html;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else{
            html = (<div>Skapa konto</div>);
        }
        return html;
    }
}