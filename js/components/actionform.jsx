'use strict';

import React from 'react';

export class StackedActionForm{
    appendHtmlForField(htmlForm, field, getFieldText){
        let name = field.name;
        let label = getFieldText('label', name);
        let placeholder = getFieldText('placeholder', name);
        htmlForm.push(<label htmlFor={name}>{label}</label>);
        htmlForm.push(<input id={name} type={field.type} placeholder={placeholder} ref={name} />);
    }
    htmlFormForAction(action, headerText, submitText, getFieldText, submit){
        let fields = [];
        for (let field of action.getFormFields()){
            this.appendHtmlForField(fields, field, getFieldText);
        }
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
        for (let field of action.getFormFields()){
            let name = field.name;
            let value = React.findDOMNode(refs[name]).value.trim();
            data[name] = value;
        }
        return data;
    }
}
