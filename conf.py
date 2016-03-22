# import server

cfg = {
    "service":{
        "home": {
             "host": "http://127.0.0.1",
             "port": ":8080",
             "resource": "",
                }
        },
    "server": {
        "new-inspections": {
            "GET": {
                "method": "GET",
                "endpoint": "/",
                "handle": "hello"
            },
            "POST": {
                "method": "POST",
                "endpoint": "/",
                "handle": "hello"
            }
        },
        "assignment-status": {
            "GET": {
                "method": "GET",
                "endpoint": "/v2/assignment-status",
                "handle": "hello"
             }
         }
    }
}
