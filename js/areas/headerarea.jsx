'use strict';

import React from 'react';
import ApplicationLink from '../components/applicationlink';
import ModalLink from '../components/modallink';
import LoginForm from '../components/loginform';

export default class HeaderArea{
    constructor(application, atElement){
        this._application = application;
        this._atElement = atElement;
        this._getLoginForm = this._getLoginForm.bind(this);
    }

    _getLoginForm(requestClose){
        return <LoginForm application={this._application} requestClose={requestClose} />;
    }

    render(){
        let application = this._application;
        let menuitemClasses = "pure-menu-link";
        let menuitems = [];
        if (application.hasAction('login')){
            menuitems.push(
                <li key="login" className="pure-menu-item">
                    <ModalLink classes={menuitemClasses} key="login" text="Login" link="Log In" getContent={this._getLoginForm} />
                </li>);
        }

        let userTemplateLink =
            application.getLink('userTemplate');
        if (userTemplateLink){
            menuitems.push(
                <li key="signup" className="pure-menu-item">
                    <ApplicationLink classes={menuitemClasses} key="createuser" text="Sign Up" link={userTemplateLink} />
                </li>);
        }

        let userRepr = application.property('user_repr', null);
        if (userRepr){
            let name = userRepr.property('first_name') + " " + userRepr.property('last_name');
            let link = userRepr.ref;
            menuitems.push(
                <li key="user" className="pure-menu-item">
                    <ApplicationLink classes={menuitemClasses} key="showuser" text={name} link={link} />
                </li>);
        }

        let html = (
            <div style={{background: '#1A1A1B'}} className="pure-menu pure-menu-horizontal">
                <a className="pure-menu-heading" href="">Goldfish</a>
                <ul className="pure-menu-list" style={{float: 'right'}}>
                    {menuitems}
                </ul>
            </div>);

        React.render(
            html,
            this._atElement
        );
    }
}
