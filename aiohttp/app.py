import json
from aiohttp import web


async def handle(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj), status=200)

async def new_user(request):
    try:
        user = request.query['name']
        print("Creating a new user with name: {}".format(user))
        response_obj = {'status': 'success', 'message': 'User successfully created'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'message': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_post('/user', new_user)
# Ele criou um "post" meio estranho neste exemplo,
# pois as informações do user devem ir via url, por exemplo:
# curl -X POST 0.0.0.0:8080/user?name=teste
# Mas ok, já deu pra entender.

web.run_app(app)
