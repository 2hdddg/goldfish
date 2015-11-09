'use strict';

import React from 'react';
import PageLink from '../components/pagelink';
import ModalLink from '../components/modallink';
import ActionLink from '../components/actionlink';
import LoginForm from '../components/loginform';

export default class HeaderArea{
    constructor(application, atElement){
        this._application = application;
        this._atElement = atElement;
        this._getLoginForm = this._getLoginForm.bind(this);
        this._logout = this._logout.bind(this);
    }

    _getLoginForm(requestClose){
        return <LoginForm application={this._application} requestClose={requestClose} />;
    }

    _logout(){
        let logout = this._application.getAction('logout');
        logout.submit({})
            .then(actionResponse => {
            })
            .catch(error => {
            });
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
                    <PageLink classes={menuitemClasses} key="createuser" text="Sign Up" link={userTemplateLink} />
                </li>);
        }

        let userRepr = application.property('user_repr', null);
        if (userRepr){
            let name = userRepr.property('first_name') + " " + userRepr.property('last_name');
            let link = userRepr.ref;
            menuitems.push(
                <li key="user" className="pure-menu-item">
                    <PageLink classes={menuitemClasses} key="showuser" text={name} link={link} />
                </li>);
        }

        if (application.hasAction('logout')){
            menuitems.push(
                <li key="login" className="pure-menu-item">
                    <ActionLink classes={menuitemClasses} key="logout" text="Logout" actionhandler={this._logout} />
                </li>);
        }

        let home = application.getLink('default');
        let html = (
            <div style={{background: '#1A1A1B'}} className="pure-menu pure-menu-horizontal">
                <PageLink classes={["pure-menu-heading"]} text="Goldfish" link={home}></PageLink>
                <ul className="pure-menu-list" style={{float: 'right'}}>
                    {menuitems}
                </ul>
            </div>);
        //       <a className="pure-menu-heading" href="/">Goldfish</a>

        React.render(
            html,
            this._atElement
        );
    }
}
