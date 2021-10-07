init:
    # Settings menu
    screen bangok_modsettings tag smallscreen2:
        modal True
        window id "bangok_modsettings" at popup2:
            style "smallwindow"

            vbox:
                align (0.5, 0.5)
                spacing 10

                if persistent.nsfwtoggle:
                    text "Fetishes:":
                        align (0.5, 0.5)

                    text "If you do not know what an option means, look it up or leave it deselected."

                    null

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_watersports"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Watersports"

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_inflation"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Inflation"

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_knot"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Knotting"

                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        imagebutton:
                            xcenter 0.5
                            ycenter 0.5
                            idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                            hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                            selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                            selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                            action [MTSTogglePersistentBool("bangok_cloacas"),
                                    Play("audio", "se/sounds/yes.wav")]
                            hovered Play("audio", "se/sounds/select.ogg")
                            focus_mask None
                        text "Cloacas"
                else:
                    text "This mod's content is primarily":
                        align (0.5,0.5)
                    text "---- Not-Safe-For-Work ----":
                        align (0.5,0.5)
                    text "Re-enable NSFW scenes or uninstall the mod.":
                        align (0.5,0.5)
                    text "This mod does not guarantee all NSFW content is inaccessible\nwhile NSFW scenes are disabled, though an attempt was made.":
                        align (0.5,0.5)

            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("my_cool_screen"), Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button

    # Locations
    image bangok_four_bryce1_apartment night = "bg/in/apts/pad_night.png"
    image bangok_four_bryce1_apartment night ceiling = "bg/in/apts/pad_night_ceil.png"


    image bangok_four_xipsum_bedroom normal = "bg/in/apts/ipsum_bedroom.png"
    image bangok_four_xipsum_bedroom_bed = "bg/in/apts/ipsum_bedroom_bed.png"
    image bangok_four_xipsum_bedroom ceiling = "bg/in/apts/ipsum_bedroom_ceiling.png"

    # CGs
    image bangok_four_xipsum_afterglow = "cg/lorem-x-ipsum_purpleroom.png"

    # People
    image bangok_four_bryce_underside_large dk = im.Recolor("cr/bryce_underside_large.png", 70, 70, 100, 255)
    image bangok_four_bryce_underside_large dk flip = im.Recolor(im.Flip("cr/bryce_underside_large.png",horizontal=True), 70, 70, 100, 255)

    image lorem bangok normal = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_normal.png",
        (626,591), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok normal flip = im.Flip(renpy.display.image.ImageReference('lorem bangok normal'),horizontal=True)
    image lorem bangok happy = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_happy.png",
        (626,591), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok happy flip = im.Flip(renpy.display.image.ImageReference('lorem bangok happy'),horizontal=True)
    image lorem bangok sad = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_sad.png",
        (626,591), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok sad flip = im.Flip(renpy.display.image.ImageReference('lorem bangok sad'),horizontal=True)
    image lorem bangok relieved = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_relieved.png",
        (626,591), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok relieved flip = im.Flip(renpy.display.image.ImageReference('lorem bangok relieved'),horizontal=True)
    image lorem bangok shy = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_shy.png",
        (626,591), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok shy flip = im.Flip(renpy.display.image.ImageReference('lorem bangok shy'),horizontal=True)
    image lorem bangok think = im.Composite(
        (1240,650), 
        (0,0),"cr/lorem_think.png",
        (626,591), "cr/lorem_bangok_peek.png"
    )
    image lorem bangok think flip = im.Flip('lorem bangok think',horizontal=True)

    image lorem bangok hidepeek = "cr/lorem_bangok_hidepeek.png"
    image lorem bangok hidepeek flip = im.Flip("cr/lorem_bangok_hidepeek.png",horizontal=True)

    image ipsum normal bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_normal.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum normal flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum normal bangok'),horizontal=True)
    image ipsum happy bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_happy.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum happy flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum happy bangok'),horizontal=True)
    image ipsum sad bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_sad.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum sad flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum sad bangok'),horizontal=True)
    image ipsum think bangok = im.Composite(
        (650,800),
        (0,0), "cr/ipsum_think.png",
        (214,684),"cr/ipsum_bangok_pen.png"
    )
    image ipsum think flip bangok = im.Flip(renpy.display.image.ImageReference('ipsum think bangok'),horizontal=True)


init python:
    # First time per run, obv.
    bangok_four_firsttime = True
    bangok_four_playerhasdick = None