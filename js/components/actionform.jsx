'use strict';

import React from 'react';

export class StackedActionForm{
    _label(field, getFieldText){
        let name = field.name;
        let label = getFieldText('label', name);
        return <label htmlFor={name}>{label}</label>;
    }
    _input(field, type, getFieldText){
        let name = field.name;
        let placeholder = getFieldText('placeholder', name);
        return <input id={name} type={type} placeholder={placeholder} ref={name} />;
    }
    appendHtmlForField(htmlForm, field, getFieldText){
        let type = field.type;
        const inputs = {
            email: (f, g) => this._input(f, 'email', g),
            password: (f, g) => this._input(f, 'password', g),
            name: (f, g) => this._input(f, 'text', g)
        };
        let input = inputs[type](field, getFieldText)

        htmlForm.push(this._label(field, getFieldText));
        htmlForm.push(input);
    }
    htmlFormForAction(action, headerText, submitText, getFieldText, submit){
        let fields = [];
        action.getFormFields().forEach(f =>
            this.appendHtmlForField(fields, f, getFieldText));
        return (<form className="pure-form pure-form-stacked">
                    <fieldset>
                        <legend>{headerText}</legend>
                        {fields}
                        <button className="pure-button pure-button-primary" onClick={submit}>{submitText}</button>
                    </fieldset>
                </form>);
    }
    getData(action, view){
        let data = {};
        let refs = view.refs;
        action.getFormFields().forEach(f => {
            let name = f.name;
            let value = React.findDOMNode(refs[name]).value.trim();
            data[name] = value;
        });
        return data;
    }
}
