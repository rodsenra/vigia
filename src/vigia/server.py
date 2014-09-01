# -*- coding: utf-8 -*-

import os
from flask import Flask, request
from vigia.settings import environments

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

run_in_shell = """
/usr/bin/osascript -e '
tell application "iTerm"
   activate
   set myterm to (make new terminal)
   tell myterm
       launch session "MySession"
       set number of columns to 80
       set number of rows to 25
       set _session1 to current session
       tell _session1
          write text "{0}"
       end tell
   end tell
end tell
'
"""

run_in_browser = """
/usr/bin/open {0}
"""

def execute(action, action_string):
    if action is None:
        return
    if type(action) is list:
        for action_item in action:
            os.system(action_string.format(action_item))
    else:
        os.system(action_string.format(action))


@app.route('/')
def root():
    return app.send_static_file('brainiak.html')


@app.route('/userAction')
def userAction():
    env_name = request.args.get('env', None)
    if env_name is None:
        return "Environment undefined"

    env = environments[env_name]

    element_id = request.args.get('element_id', None)
    if element_id is None:
        return "No action defined"

    element = env.get(element_id, None)
    if element is None:
        return "No action for {0}".format(element_id)

    sh_action = element.get("sh", None)
    execute(sh_action, run_in_shell)

    web_action = element.get("web", None)
    execute(web_action, run_in_browser)

    return "Ok {0}".format(element_id)


@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)


if __name__ == '__main__':  # pragma: no cover
    app.run(port=8088)
