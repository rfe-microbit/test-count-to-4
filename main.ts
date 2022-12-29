let x = 0
input.onButtonPressed(Button.A, function () {
    x = 1
    for (let index = 0; index < 4; index++) {
        basic.showNumber(x)
        x += 1
    }
})
