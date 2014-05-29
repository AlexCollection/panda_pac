function suffix(s1,s2){return s1.indexOf(s2,s1.length-s2.length)!==-1};
  function FindProxyForURL(url, host) {
  var PROXY = "%s";
  var DEFAULT = "DIRECT";

  if (suffix(host, ".cn")||isPlainHostName(host)||dnsDomainIs(host,".local")||/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/i.test(host)){ return DEFAULT; }

  var proxy_domains=%s;
  for(i = 0; i < proxy_domains.length; i++) {
    if(suffix(host, proxy_domains[i])) {
      return PROXY;
    }
  }

  var auto_list=%s;
  for(i = 0; i < auto_list.length; i++) {
    if(suffix(host, auto_list[i])) {
      return DEFAULT;
    }
  }
  return PROXY;
}
