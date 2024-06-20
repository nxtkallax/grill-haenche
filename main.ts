input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    music.setTempo(155)
    music.playTone(220, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(294, music.beat(BeatFraction.Whole))
    music.playTone(220, music.beat(BeatFraction.Whole))
    music.playTone(208, music.beat(BeatFraction.Whole))
    music.playTone(208, music.beat(BeatFraction.Whole))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(165, music.beat(BeatFraction.Whole))
    music.playTone(175, music.beat(BeatFraction.Whole))
    music.playTone(196, music.beat(BeatFraction.Whole))
    music.playTone(220, music.beat(BeatFraction.Whole))
    music.playTone(196, music.beat(BeatFraction.Whole))
    music.playTone(175, music.beat(BeatFraction.Whole))
    music.playTone(165, music.beat(BeatFraction.Whole))
    music.playTone(175, music.beat(BeatFraction.Whole))
})
input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index < 3; index++) {
        music.playMelody("B C5 B C5 B C5 B C5 ", 500)
    }
})
basic.forever(function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # . # . #
        # # # # #
        # . . . #
        `)
})
loops.everyInterval(100, function () {
    if (input.temperature() > 30) {
        basic.setLedColor(0xff0000)
    } else if (input.temperature() == 30) {
        basic.setLedColor(0xffff00)
    } else if (input.temperature() < 30) {
        basic.setLedColor(0x00ff00)
    }
})
