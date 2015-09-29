'use strict';

import React from 'react';
import { open } from '../infrastructure/currentpage'

class ApplicationLink extends React.Component {
    constructor(){
        super();
        this._click = this._click.bind(this);
    }

    _click(event){
        open(this.props.link);
    }

    render(){
        return (
            <span class="ApplicationLink" href={this.props.link} onClick={this._click}>{this.props.text}</span>);
    }
}

export default ApplicationLink;