def create_callback(message):
    def callback():
        print(message)
    return callback

callback = create_callback("Hello, World!")
callback()