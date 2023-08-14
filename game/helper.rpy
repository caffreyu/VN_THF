init python:
    config.keymap['hide_windows'] = []
    config.keymap['dismiss'].append('mousedown_5')

init python:
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False

init python:
    # change punch variable
    hpunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
    vpunch = Move((0, 30), (0, -30), .50, bounce=True, repeat=True, delay=.275)


# basic animations for characters
transform offscreenbottom:
    xpos 0.5 xanchor 0.5 ypos 2.0 yanchor 1.0

transform offscreenleft:
    xpos 0.0 xanchor 1.0 ypos 0.5 yanchor 0.5

transform offscreenright:
    xpos 1.0 xanchor 1.0 ypos 0.5 yanchor 0.5

define bottomside = MoveTransition(
                    delay=0.5,
                    enter=offscreenbottom,
                    leave=offscreenbottom,
                    old=False,
                    layers=['master'],
                    time_warp=ease,
                    enter_time_warp=None,
                    leave_time_warp=None
)

define leftside = MoveTransition(
                    delay=0.5,
                    enter=offscreenleft,
                    leave=offscreenleft,
                    old=False,
                    layers=['master'],
                    time_warp=ease,
                    enter_time_warp=None,
                    leave_time_warp=None
)

define rightside = MoveTransition(
                    delay=0.5,
                    enter=offscreenright,
                    leave=offscreenright,
                    old=False,
                    layers=['master'],
                    time_warp=ease,
                    enter_time_warp=None,
                    leave_time_warp=None
)




# character positions
transform char_mid:
    zoom 0.2
    xalign 0.5
    yalign 0.27

transform char_left:
    zoom 0.2
    xalign 0.2
    yalign 0.27

transform char_right:
    zoom 0.2
    xalign 0.8
    yalign 0.27

transform large:
    xalign 0.5
    yalign 0.85

transform cg0:
    zoom 0.5

transform cg1:
    zoom 0.8
    xalign 0.4
    yalign 0.53