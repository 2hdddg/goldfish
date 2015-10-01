'use strict';

import React from 'react';
import { open } from '../infrastructure/currentpage'

export default class ApplicationLink extends React.Component {
    constructor(){
        super();
        this._click = this._click.bind(this);
    }

    _click(event){
        event.preventDefault();
        open(this.props.link);
    }

    render(){
        return (
            <a href={this.props.link} className={this.props.classes} onClick={this._click}>{this.props.text}</a>);
    }
}
