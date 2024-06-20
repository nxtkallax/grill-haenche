def on_gesture_screen_down():
    for index in range(3):
        music.play_melody("B C5 B C5 B C5 B C5 ", 500)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_b():
    music.set_tempo(155)
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    music.play_tone(175, music.beat(BeatFraction.WHOLE))
    music.play_tone(196, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(196, music.beat(BeatFraction.WHOLE))
    music.play_tone(175, music.beat(BeatFraction.WHOLE))
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    music.play_tone(175, music.beat(BeatFraction.WHOLE))
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_forever():
    basic.show_leds("""
        # # # # #
        # # # # #
        # . # . #
        # # # # #
        # . . . #
        """)
basic.forever(on_forever)

def on_every_interval():
    if input.temperature() > 30:
        basic.set_led_color(0xff0000)
    elif input.temperature() == 30:
        basic.set_led_color(0xffff00)
    elif input.temperature() < 30:
        basic.set_led_color(0x00ff00)
loops.every_interval(100, on_every_interval)
