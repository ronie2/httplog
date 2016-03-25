# import server

cfg = {
    "service": {
        "home": {
            "host": "http://127.0.0.1",
            "port": ":8080",
            }
            },
    "server": {
        "new-inspections": {
            "GET": {
                "method": "GET",
                "endpoint": "/v2/new-inspections",
                "handle": "new_inspections_get"
            },
            "POST": {
                "method": "POST",
                "endpoint": "/v2/new-inspections",
                "handle": "new_inspections_post"
            }
        },
        "wild_card_listener": {
            "GET_POST_PUT_ELSE": {
                "method": "*",
                "endpoint": "/v2/wild-card",
                "handle": "wild_method"
            },
        },
        "assignment-status": {
            "GET": {
                "method": "GET",
                "endpoint": "/v2/assignment-status",
                "handle": "assignment_status_get"
             },
            "POST": {
                "method": "POST",
                "endpoint": "/v2/assignment-status",
                "handle": "assignment_status_post"

            }
         }
    }
}
