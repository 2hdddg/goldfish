'use strict';

import React from 'react';
import ApplicationLink from '../components/applicationlink';
import Login from '../components/login';

class AccountArea{
    constructor(application, atElement){
        this._application = application;
        this._atElement = atElement;
    }

    render(){
        let application = this._application;

        let parts = [];
        if (application.canLogin()){
            parts.push(
                <Login key="login" application={application} />);
        }

        let userTemplateLink =
            application.getLink('userTemplate');
        if (userTemplateLink){
            parts.push(
                <ApplicationLink key="createuser" text="New account" link={userTemplateLink} />);
        }

        let html = (
            <div>
                {parts}
            </div>);

        React.render(
            html,
            this._atElement
        );
    }
}

export default AccountArea;
