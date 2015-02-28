var PROXY = "__PROXY__";
var DEFAULT = "DIRECT";

var whitelist = __WHITELIST__;

var hasOwnProperty = Object.hasOwnProperty;
function suffix2(s1,s2){return s1.indexOf(s2,s1.length-s2.length)!==-1};

function FindProxyForURL(url, host) {

    if (suffix2(host, ".cn")||isPlainHostName(host)||dnsDomainIs(host,".local")||/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/i.test(host)){ return DEFAULT; }

    var suffix;
    var pos = host.lastIndexOf('.');
    for (;;) {
        suffix = host.substring(pos + 1);
        if (hasOwnProperty.call(whitelist, suffix)) {
            return DEFAULT;
        }
        if (pos <= 0) {
            return PROXY;
        }
        pos = host.lastIndexOf('.', pos - 1);
    }
}
