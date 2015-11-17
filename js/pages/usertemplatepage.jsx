'use strict';

import React from 'react';

import { register } from './registry';
import { StackedActionForm } from '../components/actionform';
import { open } from '../infrastructure/currentpage';

export class UserTemplatePage extends React.Component {

    constructor(){
        super();
        this.state = {
            isBusy: false,
            validationMessage: ''
        };
        this._form = new StackedActionForm();
        this._submit = this._submit.bind(this);
    }
    _submit(event){
        let userTemplate = this.props.resource;
        let createAction = userTemplate.getAction('create');
        let data = this._form.getData(createAction, this);

        this.setState({isBusy: true, message: ''});

        createAction.submit(data)
            .then(actionResponse => {
                this.setState({isBusy: false, message: ''});

                let user = actionResponse
                    .getEmbeddedFromEvent('created')
                    .filter(x => x.cls === 'User')[0];
                let calendars_link = user.getLink('calendars');
                open(calendars_link);
            })
            .catch(error => {
                this.setState({isBusy: false, message: 'Unknown error'});
            });
        event.preventDefault();
    }
    render(){
        let html;
        let userTemplate = this.props.resource;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else{
            let createAction = userTemplate.getAction('create');
            html = this._form.htmlFormForAction(
                createAction, 'Please register.', 'Register', (usage, fieldname) => fieldname, this._submit);
        }

        return (
            <div>{html}<span>{this.state.message}</span></div>);
    }
}

register('UserTemplate', UserTemplatePage);