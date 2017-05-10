from Project import create_app

app = create_app()

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.jinja_env.auto_reload = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(host='0.0.0.0', debug=True)
