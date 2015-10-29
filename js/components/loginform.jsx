'use strict';

import React from 'react';
import { StackedActionForm } from './actionform'
import { open } from '../infrastructure/currentpage'

export default class LoginForm extends React.Component{
    constructor(){
        super();
        this._form = new StackedActionForm();
        this.state = {
            isBusy: false,
            message: ''
        };
        this._submit = this._submit.bind(this);
    }
    _submit(event){
        let loginAction = this.props.application.getAction('login');
        let data = this._form.getData(loginAction, this);

        this.setState({isBusy: true});

        loginAction.submit(data)
            .then(actionResponse => {
                this.setState({isBusy: false, message: ''});
                let requestClose = this.props.requestClose;
                if (requestClose){
                    requestClose();
                }
                let user = actionResponse
                    .getEmbeddedFromEvent('logged_in')
                    .filter(x => x.cls === 'User')[0];
                let calendars_link = user.getLink('calendars');
                open(calendars_link);
            })
            .catch(error => {
                if (error.response && error.response.status === 401){
                    this.setState({isBusy: false, message: 'Wrong username or password'});
                }
                else{
                    this.setState({isBusy: false, message: 'Unknown error'});
                    throw error;
                }
            });
        event.preventDefault();
    }
    render(){
        let html;
        let application = this.props.application;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else if (!application.hasAction('login')){
        }
        else{
            let loginAction = application.getAction('login');
            let lookup = {
                label: {
                    username: 'Email',
                    password: 'Password'
                },
                placeholder: {
                    username: 'Your email',
                    password: 'Password'
                }
            }
            html = this._form.htmlFormForAction(
                loginAction, 'Please enter your credentials.', 'Log in', (usage, fieldname) => lookup[usage][fieldname], this._submit);
        }

        return (
            <div>{html}<span>{this.state.message}</span></div>);
    }
};
