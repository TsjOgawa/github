def on_bluetooth_connected():
    pass
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    pass
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

bluetooth.start_temperature_service()
basic.show_icon(IconNames.HAPPY)

def on_forever():
    pass
basic.forever(on_forever)
