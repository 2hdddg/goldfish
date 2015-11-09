'use strict';

function expand(f){
    return "GOLDFISH:" + f();
}

export default {
    info: f => console.info(expand(f)),
    debug: f => console.debug(expand(f)),
    error: f => console.error(expand(f)),
    warn: f => console.warn(expand(f))
};