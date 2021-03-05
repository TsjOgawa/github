bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Heart)
})
bluetooth.startAccelerometerService()
basic.showLeds(`
    # . . . .
    . # # # .
    . . . . .
    . . . . .
    . . . . .
    `)
