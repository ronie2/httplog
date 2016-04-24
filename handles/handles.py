import asyncio
import aiohttp
from aiohttp import web
from handles.plugins import get_log, write_log, sleep, middleware_log
from config.conf import cfg

DEMO = "-demo"

async def new_inspections(request):

    if request.method == "GET":
        if request.path_qs == "/v1/new-inspections":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["new-inspections"]["config"]["log_file"]))
        elif request.path_qs == "/v2/new-inspections":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["new-inspections" + DEMO]["config"]["log_file"]))

    elif request.method == "POST":
        if request.path_qs == "/v1/new-inspections":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["new-inspections"]["config"]["log_file"])
            await sleep("new-inspections", "config")
            return web.Response(body = b"POST PROCESSED")
        elif request.path_qs == "/v2/new-inspections":
            await write_log(request, log_file_name=cfg["server"] \
                ["new-inspections" + DEMO]["config"]["log_file"])
            await sleep("new-inspections" + DEMO, "config")
            return web.Response(body=b"POST PROCESSED")

    else:
        return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

async def assignment_status(request):

    if request.method == "GET":
        if request.path_qs == "/v1/assignment-status":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["assignment-status"]["config"]["log_file"]))

        elif request.path_qs == "/v2/assignment-status":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["assignment-status" + DEMO]["config"]["log_file"]))

    elif request.method == "POST":
        if request.path_qs == "/v1/assignment-status":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["assignment-status"]["config"]["log_file"])
            await sleep("assignment-status", "config")
            return web.Response(body = b"POST PROCESSED")

        elif request.path_qs == "/v2/assignment-status":
            await write_log(request, log_file_name=cfg["server"] \
                ["assignment-status" + DEMO]["config"]["log_file"])
            await sleep("assignment-status", "config")
            return web.Response(body=b"POST PROCESSED")

    else:
        return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

async def vendor_completion(request):
    if request.method == "GET":

        if request.path_qs == "/v1/vendor-completion":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["vendor-completion"]["config"]["log_file"]))

        elif request.path_qs == "/v2/vendor-completion":
            return web.Response(text=await \
                get_log(log_file_name=cfg["server"] \
                    ["vendor-completion" + DEMO]["config"]["log_file"]))

    elif request.method == "POST":
        if request.path_qs == "/v1/vendor-acceptance":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["vendor-completion"]["config"]["log_file"])
            await sleep("vendor-completion", "config")
            return web.Response(body = b"POST PROCESSED")
        elif request.path_qs == "/v2/vendor-completion":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["vendor-completion" + DEMO]["config"]["log_file"])
            await sleep("vendor-completion" + DEMO, "config")
            return web.Response(body = b"POST PROCESSED")
    else:
        return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

async def vendor_acceptance(request):
    if request.path_qs == "/v1/vendor-acceptance":
        if request.method == "GET":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["vendor-acceptance"]["config"]["log_file"]))
        elif request.method == "POST":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["vendor-acceptance"]["config"]["log_file"])
            await sleep("vendor-acceptance" + DEMO, "config")
            return web.Response(body = b"POST PROCESSED")
        else:
            return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")
    if request.path_qs == "/v2/vendor-acceptance":
        if request.method == "GET":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["vendor-acceptance" + DEMO]["config"]["log_file"]))
        elif request.method == "POST":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["vendor-acceptance" + DEMO]["config"]["log_file"])
            await sleep("vendor-acceptance" + DEMO, "config")
            return web.Response(body = b"POST PROCESSED")
        else:
            return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

async def qa_status(request):
    if request.path_qs == "/v1/qa-status":
        if request.method == "GET":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["qa-status"]["config"]["log_file"]))
        elif request.method == "POST":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["qa-status"]["config"]["log_file"])
            await sleep("qa-status", "config")
            return web.Response(body = b"POST PROCESSED")
        else:
            return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

    if request.path_qs == "/v2/qa-status":
        if request.method == "GET":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["qa-status" + DEMO]["config"]["log_file"]))
        elif request.method == "POST":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["qa-status" + DEMO]["config"]["log_file"])
            await sleep("qa-status" + DEMO, "config")
            return web.Response(body = b"POST PROCESSED")
        else:
            return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

async def vendor_status(request):
    if request.path_qs == "/v1/vendor-status":
        if request.method == "GET":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["vendor-status"]["config"]["log_file"]))
        elif request.method == "POST":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["vendor-status"]["config"]["log_file"])
            await sleep("vendor-status", "config")
            return web.Response(body = b"POST PROCESSED")
        else:
            return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")
    elif request.path_qs == "/v2/vendor-status":
        if request.method == "GET":
            return web.Response(text= await \
                            get_log(log_file_name=cfg["server"]\
                                    ["vendor-status" + DEMO]["config"]["log_file"]))
        elif request.method == "POST":
            await write_log(request, log_file_name=cfg["server"]\
                                    ["vendor-status" + DEMO]["config"]["log_file"])
            await sleep("vendor-status" + DEMO, "config")
            return web.Response(body = b"POST PROCESSED")
        else:
            return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

async def middleware_logs(request):
    if request.method == "GET":
        return web.Response(text= await middleware_log())
    else:
        return web.Response(body = b"OTHER METHOD WAS NOT PROCESSED")

async def wild_method(request):
    if request.method == "GET":
        return web.Response(body = b"Hello, GET world!")
    elif request.method == "POST":
        return web.Response(body = b"Hello, POST world!")
    else:
        return web.Response(body = b"Hallo OTHER METHOD")