# -*- coding: utf-8 -*-

dev = {
    "brainiak": {
        "sh": "ssh watcher@host891.replaceme.com",
        "web": "http://brainiak.semantica.dev.replaceme.com"
    },
    "virtuoso_master": {
        "web": "http://dev.virtuoso.replaceme.com:8890/sparql-auth"
    },
    "redis": {
        "sh": "redis-cli -h redis.dev.replaceme.com"
    },
    "elasticsearch": {
        "web": "http://esearch.dev.replaceme.com/tools/elasticsearch-head/"
    },
    "solr": {
        "web": "master.solr.semantica.dev.replaceme.com"
    },
    "mercury": {
        "sh": "ssh username@host44.replaceme.com",
        "web": "http://host44.replaceme.com:8036/healthcheck"
    },
    "barramento": {
        "sh": ["ssh username@host775.replaceme.com", "ssh username@host776.replaceme.com"],
        "web": "http://barramento.backstage.dev.replaceme.com/admin/queues.jsp"
    },
}

prod = {
    "brainiak": {
        "sh": "csshX username@host89lb11.replaceme.com username@host90lb11.replaceme.com",
        "web": ["http://brainiak.semantica.replaceme.com",
                "http://datacenter.replaceme.com/server.cgi?targets=host89lb11",
                "http://datacenter.replaceme.com/server.cgi?targets=host90lb11"]
    },
    "virtuoso_master": {
        "web": "http://virtuoso.semantica.replaceme.com/sparql"
    },
    "redis": {
        "sh": "redis-cli -h redis.brainiak.replaceme.com -p 20019 -a 4fdfa56255f21ccf01b3d78f999caea3"
    },
    "elasticsearch": {
        "web": "http://esearch.replaceme.com/tools/elasticsearch-head/"
    },
    "solr": {
        "web": "master.solr.semantica.replaceme.com"
    },
    "mercury": {
        "sh": ["ssh username@host40lb14.replaceme.com", "ssh username@host41lb14.replaceme.com"],
        "web": ["http://host40lb14.replaceme.com:8036/healthcheck", "http://host41lb14.replaceme.com:8036/healthcheck"]
    },
    "barramento": {
        "sh": ["ssh username@riolb517.replaceme.co", "ssh username@host518.replaceme.com"],
        "web": "http://barramento.backstage.replaceme.com/admin/queues.jsp"
    },
}


environments = {"env_dev": dev, "env_qa01": qa01, "env_prod": prod}
