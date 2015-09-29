'use strict';

import React from 'react';

export class UserTemplate extends React.Component {
    render(){
        return (<span>{this.props.model.cls}</span>);
    }
}