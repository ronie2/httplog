# import server

cfg = {
    "service": {
        "home": {
            "host": "10.24.64.112",
            "port": ":5000",
            }
            },
    "server": {
        "new-inspections": {
           "config": {
                "method": "*",
                "endpoint": "/v1/new-inspections",
                "handle": "new_inspections",
                "timeout": 280,
                "log_file": "new_inspections.log"
           }
        },
       "assignment-status": {
            "config": {
                "method": "*",
                "endpoint": "/v1/assignment-status",
                "handle": "assignment_status",
                "timeout": 280,
                "log_file": "assignment_status.log"
             },
         },
        "vendor-completion": {
             "config": {
                "method": "*",
                "endpoint": "/v1/vendor-completion",
                "handle": "vendor_completion",
                "timeout": 280,
                "log_file": "vendor_completion.log"
             },
        },
        "vendor-acceptance": {
             "config": {
                "method": "*",
                "endpoint": "/v1/vendor-acceptance",
                "handle": "vendor_acceptance",
                "timeout": 280,
                "log_file": "vendor_acceptance.log"
             },
        },
        "qa-status": {
             "config": {
                "method": "*",
                "endpoint": "/v1/qa-status",
                "handle": "qa_status",
                "timeout": 280,
                "log_file": "qa_status.log"
             },
        },
        "vendor-status": {
            "config": {
                "method": "*",
                "endpoint": "/v1/vendor-status",
                "handle": "vendor_status",
                "timeout": 280,
                "log_file": "vendor_status.log"
            },
        },
        "middleware-log": {
            "config": {
                "method": "*",
                "endpoint": "/v1/logs",
                "handle": "middleware_logs",
                "timeout": 0,
             },
         },
        "wild_card_listener": {
            "GET_POST_PUT_ELSE": {
                "method": "*",
                "endpoint": "/v1/wild-card",
                "handle": "wild_method"
            },
        },
        "new-inspections-demo": {
            "config": {
                "method": "*",
                "endpoint": "/v2/new-inspections",
                "handle": "new_inspections",
                "timeout": 0,
                "log_file": "new_inspections_demo.log"
            }
        },
        "assignment-status-demo": {
            "config": {
                "method": "*",
                "endpoint": "/v2/assignment-status",
                "handle": "assignment_status",
                "timeout": 0,
                "log_file": "assignment_status_demo.log"
            },
        },
        "vendor-completion-demo": {
            "config": {
                "method": "*",
                "endpoint": "/v2/vendor-completion",
                "handle": "vendor_completion",
                "timeout": 0,
                "log_file": "vendor_completion_demo.log"
            },
        },
        "vendor-acceptance-demo": {
            "config": {
                "method": "*",
                "endpoint": "/v2/vendor-acceptance",
                "handle": "vendor_acceptance",
                "timeout": 0,
                "log_file": "vendor_acceptance_demo.log"
            },
        },
        "qa-status-demo": {
            "config": {
                "method": "*",
                "endpoint": "/v2/qa-status",
                "handle": "qa_status",
                "timeout": 0,
                "log_file": "qa_status_demo.log"
            },
        },
        "vendor-status-demo": {
            "config": {
                "method": "*",
                "endpoint": "/v2/vendor-status",
                "handle": "vendor_status",
                "timeout": 0,
                "log_file": "vendor_status_demo.log"
            },
        },
        "middleware-log-demo": {
            "config": {
                "method": "*",
                "endpoint": "/v2/logs",
                "handle": "middleware_logs",
                "timeout": 0,
            },
        },

    }
}
