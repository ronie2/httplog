async def logger_writer(request):
    from aiohttp import web
    import datetime

    for i in request.text():
        print (i)
    wwweee()
    return web.Response()

def wwweee():
    import datetime
    log_name = "log.log"
    mode = "a+"
    line_width = 50
    with open(log_name, mode, encoding="utf-8") as log:
        log.write("\n" + "*" * line_width + "\n")
        log.write(str(datetime.datetime.now()))
        log.write("\n" + "*" * line_width + "\n")
        # log.write(repr(request))
        log.write("\n")
    return
