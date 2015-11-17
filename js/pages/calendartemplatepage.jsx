'use strict';

import React from 'react';
import { open } from '../infrastructure/currentpage';
import { StackedActionForm } from '../components/actionform';
import { register } from './registry';

export default class CalendarTemplatePage extends React.Component {

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
        let template = this.props.resource;
        let createAction = template.getAction('create');
        let data = this._form.getData(createAction, this);

        this.setState({isBusy: true, message: ''});

        createAction.submit(data)
            .then(actionResponse => {
                this.setState({isBusy: false, message: ''});

                let calendar = actionResponse
                    .getEmbeddedFromEvent('created')
                    .filter(x => x.cls === 'Calendar')[0];
                open(calendar);
            })
            .catch(error => {
                this.setState({isBusy: false, message: 'Unknown error'});
            });
        event.preventDefault();
    }
    render(){
        let html;
        let template = this.props.resource;

        if (this.state.isBusy){
            html = (<span>Busy</span>);
        }
        else{
            let createAction = template.getAction('create');
            html = this._form.htmlFormForAction(
                createAction, 'Whatever.', 'Register', (usage, fieldname) => fieldname, this._submit);
        }

        return (
            <div>{html}<span>{this.state.message}</span></div>);
    }
}

register('CalendarTemplate', CalendarTemplatePage);