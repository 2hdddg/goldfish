'use strict';

import React from 'react';

export default class ActionLink extends React.Component {
    constructor(){
        super();
        this._click = this._click.bind(this);
    }

    _click(event){
        event.preventDefault();
        this.props.actionhandler();
    }

    render(){
        return (
            <a href='#' className={this.props.classes} onClick={this._click}>{this.props.text}</a>);
    }
}
