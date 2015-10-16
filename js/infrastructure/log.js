'use strict';

function log(m){
    window.console.log("GOLDFISH:" + m);
}

export default {
    info: log,
    debug: log,
    error: log,
    warn: log
};