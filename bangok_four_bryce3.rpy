init python in bangok_four_bryce3_store:
    unplayed = True
    maverick_in = False
    sebastian_in = False

    # Train variables
    sebtarget = None
    knotfuck = False
    brycetarget = None
    brycews = None
    brycebroke = False
    mavtarget = None
    mavws = False
    mavbroke = False

    mavbackout = False

    # MP variables
    mavcondomleftin = False

    mc_bottom = True
    protection = False

    # Menu options
    top_mav = True




label bangok_four_bryce3_skipmenu:
    play sound "fx/system3.wav"
    s "Join the team-building exercise?"
    menu:
        "Yes. Join the team-building exercise.":
            play sound "fx/system3.wav"
            s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
            $ bryce3mood = 2
            show bryce at Position(xanchor = 1.0, xpos = 1.175)
            show sebastian normal flip at left
            show maverick normal behind bryce at Position(xpos=0.825)
            show zhong normal flip at Position(xpos = 0.05)
            with Fade(0.5,0.5,1.0)
            play music "mx/hydrangea.ogg" fadein 2.0
            jump bangok_four_bryce3_intro
        "No. Have a nonsexual BBQ.":
            pass
    jump bangok_four_bryce3_skip_return





label bangok_four_bryce3_intro:
    Br laugh "Wait, you're out too? What about the best part?"
    c "Best part?"
    Br smirk "A bit of teambuilding, a bit of exercise."
    Zh shy "A bit of poor decision making in which I will not be involving myself."
    Br normal "Oh don't be like that. You don't have to sit every one of these out."
    Zh "I'd prefer to."
    Br smirk "Don't get lost in the dark, then."
    hide zhong with easeoutleft
    if bangok_four_xsebastian_unplayed == False:
        show sebastian shy flip with dissolve
    Sb "You're not actually proposing this in front of the ambassador, are you?"
    Mv angry "Really, Bryce. This is too far, even for you."
    menu:
        "What is \"this\"?":
            pass
        "Is \"this\" what I think it is?" if bangok_four_bryce1_unplayed == False:
            pass
        "I get the feeling we might still need the babysitter.":
            $ renpy.pause (0.5)
            $ bryce3mood -= 1
            Br stern "We're all adults here. We can have an adult conversation about this."
    Br normal "It's just a bit of casual sex between friends. You don't all have to make a big deal about inviting one more."
    Sb disapproval flip "It is if you didn't discuss it with anyone else first."
    Br laugh "Oh come on. We haven't started. This {i}is{/i} the discussion."
    if bangok_four_bryce1_unplayed == False:
        Br normal "What do you say, [player_name]? Up to have a bit of fun again?"
        if bangok_four_xsebastian_unplayed == False:
            show sebastian shy flip with dissolve
        Sb "Again?"
    else:
        Br normal "What do you say, [player_name]? Up to get a little closer to the rest of the team?"
    menu:
        "No thanks.":
            Mv "Even [player_name] doesn't want it."
            Mv normal "The least discussion you could have had was with the person you were surprising us with."
            Mv angry "But instead you--"
            Br stern "I get it, fine. None of you are interested."
            Br brow "I'm sorry for trying to keep some semblance of normality around here."
            Sb normal flip "I'd say the BBQ went well enough. And there's always next year."
            Br stern "True enough I suppose."
            Sb disapproval flip "With that, I'm off. See you all tomorrow."
            hide sebastian with dissolve
            Br brow "Maverick?"
            Mv normal "..."
            Mv normal "Thanks for inviting me, Bryce."
            Br normal "Of course. Wouldn't be the same without you."
            m "Maverick gave me one more look before slinking off into the night."
            $ renpy.pause (0.3)
            hide maverick with dissolve
            $ renpy.pause (0.5)
            show bryce at center with ease
            $ renpy.pause (0.3)
            Br brow "Sorry for springing that on you. I didn't want it to look to Maverick like I was coaching you before you came over."
            if bangok_four_bryce1_unplayed == False:
                Br "I thought after last time you'd be interested in..."
                Br flirty "I thought after last time you'd be interested in{fast} further expanding your horizons."
            menu:
                "I was drunk last time." if bangok_four_bryce1_unplayed == False:
                    Br sad "..."
                "I don't do groups.":
                    Br sad "Ah. Sorry. I really messed that up, then."
                "Don't worry about it.":
                    show bryce sad with dissolve
                    c "Just wasn't feeling it, especially because they weren't."
                    Br sad "Still. It's my fault for assuming all this would just work out."
            $ renpy.pause(1.2)
            jump bangok_four_bryce3_playershouldleave
        "I don't want to get in the way of you all...":
            $ bryce3mood -= 1
            Mv "There is no getting in the way. Nothing is happening."
            Mv normal "Naomi is the only one as interested in the exercise as you. She's not here."
            Mv angry "And I'm not even part of your team right now. Thanks to--"
        "I would if they want to.":
            Mv normal "Then it's settled, because we are not."
            Br brow "Aren't you kinda speaking for Sebastian there?"
            Mv angry "No member of our police force should be proposing something like this with one of {i}them{/i}. Especially not--"
        "Sounds fun.":
            $ bryce3mood -= 1
            Mv angry "We're not here for your kind's enjoyment. Can't--"
    
    show sebastian disapproval flip with dissolve
    Br stern "I thought you agreed to keep this civil. Getting angry about things we're trying to leave out of tonight doesn't qualify in my book."
    if bryce3mood < 2:
        Mv "They are the only known associate of the lone suspect in three murders."
        Mv "Sleeping with a suspect's associate doesn't qualify as proper police work in my book."
        $ renpy.pause (1.2)
        Sb "Let's just call it a night and all go home."
        Sb "Mavers?"
        Mv normal "..."
        Mv "Fine."
        hide maverick with dissolve
        Sb "Until next year."
        Br sad "Yeah, yeah."
        hide sebastian with dissolve
        $ renpy.pause (0.5)
        show bryce at center with ease
        $ renpy.pause (0.3)
        Br brow "Sorry for springing that on you. I didn't want it to look to Maverick like I was coaching you before you came over."
        Br sad "It's my fault for assuming all this would just work out like normal."
        c "Hey, it's not so bad. Most of the BBQ went well."
        Br normal "'Spose that's true."
        $ renpy.pause (1.2)
        jump bangok_four_bryce3_playershouldleave

    Br normal "[player_name] has done their best to fit in and participate tonight. The least you could do is the same."
    $ renpy.pause(0.8)
    $ bangok_four_bryce3_store.maverick_in = True
    Mv normal "..."
    $ renpy.pause(0.4)
    Mv "Sebastian, where do you sit with this?"
    if bangok_four_xsebastian_unplayed == False:
        $ bangok_four_bryce3_store.sebastian_in = True
        Sb shy flip "I, ah. I'm for this."
        Sb drop flip "Though I can't bottom like normal for you two if I'll be on shift tomorrow morning."
    else:
        Sb drop flip "I'm not going to take sides on what you three should be doing."
        Sb disapproval flip "I know my shift starts early tomorrow morning, and that's my excuse to bow out."
        Br normal "That's fair. Get a good night's rest in."
        Sb normal flip "Thanks. Until next year."
        hide sebastian with dissolve
        $ renpy.pause(0.5)
        Mv "Bryce, if you're offering, you're bottoming."

    Br normal "I can do that."
    if bangok_four_bryce1_unplayed == False:
        show bryce flirty with dissolve
    else:
        show bryce smirk with dissolve
    Br "I can do that. {fast}Unless [player_name] would like to?"

    $ bangok_four_bryce3_store.mc_bottom = True # Used temporarily for a conversation option
    $ bangok_four_bryce3_store.top_mav = True
    label bangok_four_bryce3_bottom_choice:
    menu:
        "Wait, bottom all three of you?" if (bangok_four_bryce3_store.mc_bottom == True) and (bangok_four_bryce3_store.sebastian_in == True):
            show sebastian normal flip with dissolve
            $ bangok_four_bryce3_store.mc_bottom = False
            if bangok_four_bryce1_unplayed == False:
                Br smirk "I think you can manage it."
            else:
                Br normal "It's just a thought. You don't have to take it seriously."
            jump bangok_four_bryce3_bottom_choice
        "Wait, bottom both of you?" if (bangok_four_bryce3_store.mc_bottom == True) and (bangok_four_bryce3_store.sebastian_in == False):
            $ bangok_four_bryce3_store.mc_bottom = False
            if bangok_four_bryce1_unplayed == False:
                Br smirk "I think you can manage it."
            else:
                Br normal "It's just a thought. You don't have to take it seriously."
            jump bangok_four_bryce3_bottom_choice
        "Why isn't Maverick...?" if bangok_four_bryce3_store.top_mav == True:
            $ bangok_four_bryce3_store.top_mav = False
            Mv angry "I won't be beneath you."
            Sb disapproval flip "Don't ask Maverick to bottom. He's not a fan."
            Br brow "Understatement."
            jump bangok_four_bryce3_bottom_choice
        "I'll bottom.":
            $ bangok_four_bryce3_store.mc_bottom = True
            show maverick nice
            if bangok_four_bryce3_store.sebastian_in == True:
                show sebastian shy flip
                show bryce flirty
                with dissolve
                $ renpy.pause(0.3)
                Br "Oh?"
                Sb "You sure, [player_name]? That's not a statement to be made lightly."
                Sb drop flip "At least Bryce is in the size class to take Maverick."
                Sb shy flip "You're, ah..."
                Br smirk "[player_name] will be fine."
                Br smirk flip "I stashed some supplies up here in the rocks. And if it's too much, I'll take over."
                hide bryce with easeoutright
            else:
                show bryce flirty
                with dissolve
                Br "Oh?"
                $ renpy.pause (0.5)
                Br smirk flip "Alright. Let me go get the supplies I stashed."
        "Don't let me stop you, Bryce.":
            $ bangok_four_bryce3_store.mc_bottom = False
            show maverick normal
            show bryce laugh
            with dissolve
            Br "It's not my usual thing."
            Br normal "But I don't mind."
            Br normal flip "Alright. Let me go get the supplies I stashed."


    hide bryce with easeoutright
    $ renpy.pause (0.5)
    if bangok_four_bryce3_store.sebastian_in == True:
        Sb drop flip "Of course you brought supplies, even without talking it over with any of us."
    menu:
        "Maverick, are you okay with this?":
            Mv angry "It changes nothing."
            Mv normal "But Bryce has asked us to leave those concerns out of tonight. I will if you will."
            c "Consider it done, then."
        "Does he do that a lot?":
            c "You know, stash stuff in advance?"
            Mv normal "Yes."
            $ renpy.pause(1.2)
            m "I waited, but Maverick did not elaborate."

    show bryce normal at Position(xanchor = 1.0, xpos = 1.175) with easeinright
    m "Bryce returned with an open-top wicker basket, handle clenched in his teeth. A sizeable bottle of lube and four open boxes of condoms peeked out."
    Br "So. We've got condoms and lube. Should fit everyone."
    if bangok_four_bryce3_store.sebastian_in == True:
        if bangok_four_bryce3_store.mc_bottom == False:
            Br laugh "Personally I don't care, but Seb, if you want to skip cleaning yourself up later."
        else:
            Br "Seb, if you want to use one and skip cleaning yourself up later..."
        Br smirk "Or you could take a dip in the ocean when you're done tonight."
        Sb disapproval flip "I'd rather use protection than have sand up there, thanks."
    else:
        if bangok_four_bryce3_store.mc_bottom == False:
            Br "I don't give a damn about the condoms tonight."
            Br laugh "Gotta clean myself up later anyway."
            Br normal "But if either of you want 'em."
            
    if bangok_four_bryce3_store.mc_bottom == True:
        Br normal "So [player_name], normally we'd just go at it without protection. But I'm guessing you weren't expecting two dragonloads tonight, so if you'd like us to use them..."
        menu:
            "I'd prefer if you used condoms.":
                $ bangok_four_bryce3_store.protection = True
                Br normal "Sure."
            "I'm fine going unprotected.":
                $ bangok_four_bryce3_store.protection = False
                Br smirk "Alright."

    c "I should go strip, then."
    Br smirk "Go strip? Why not do that here?"
    if bangok_four_bryce3_store.sebastian_in == True:
        Sb normal flip "We're going to see you without your clothes before the night is over anyway."
    Mv normal "You may as well show us what you're hiding now."
    Br stern "Maverick."

    m "Swallowing my hesitation, I stripped out of my upper clothes before I could think about it, then dropped my drawers into the sand."

    if bangok_four_playerhasdick is None:
        menu:
            "The cool night air tickled my dick.":
                $ bangok_four_playerhasdick = True
            "The cool night air teased my lower lips.":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        m "The cool night air tickled my dick, eliciting a small rush of blood and a twitch."
        if bangok_four_bryce1_unplayed == True:
            Br smirk "Guessing you're a guy, then."

        menu:
            "Take a condom.":
                $ bangok_four_bryce3_store.protection = True
            "Go without.":
                $ bangok_four_bryce3_store.protection = False
    else:
        m "The cool night air teased my lower lips, eliciting a small rush of blood that left my groin flushed and warm."
        if bangok_four_bryce1_unplayed == True:
            Br brow "Does something come out of that, or...?"
            c "No. It's not a slit for a penis."
            Br flirty "Oh."
        
        if bangok_four_bryce3_store.mc_bottom == False:
            Br smirk "You know, I'm not sure exactly how you're going to top me if you haven't got anything to stick inside."
            menu:
                "You'll just have to find out.":
                    Br smirk "Can't wait to see."
                "Well, you'll be on your back...":
                    Br flirty "Now I almost don't want the surprise spoiled."

    if bangok_four_bryce3_store.mc_bottom == True:
        jump bangok_four_bryce3_mcbottom
    else:
        jump bangok_four_bryce3_mctop


label bangok_four_bryce3_mcbottom:
    $ renpy.pause(0.5)
    if bangok_four_bryce3_store.protection == True:
        Br stern "Do have to say, if you want me and Maverick wearing protection, you're going to have to get it on."
        c "Shouldn't it have been designed with your species putting it on in mind?"
        Br brow "It sorta was. But they didn't design it to also deal with sand on our paws."
        Br laugh "Oh the rare curses of four feet."
        c "Alright."
        scene beachx at Pan ((300, 0), (300, 0), 0.0) with dissolve
        m "I knelt in the sand next to the basket, briefly searching through the condom boxes in the moonlight until I found the largest available."
    else:
        Br normal "Well, Maverick and I will fit a lot more easily lubed up."
        if bangok_four_bryce3_store.sebastian_in == True:
            Sb normal flip "Or fit at all."
        Br smirk "Mind helping us out?"
        scene beachx at Pan ((300, 0), (300, 0), 0.0) with dissolve
        m "I knelt in the sand next to the basket, preparing to service the two larger dragons."
    show bryce flirty:
        zoom 1.35
        yanchor 1.0
        xanchor 0.5
        xpos 0.8
        ypos 1.0
    with easeinright
    m "Bryce moved in on my right, putting his large shaft within my reach."
    if bangok_four_bryce3_store.protection == True:
        m "I rolled one condom down his length, earning a flirty wink."
        show bryce smirk with dissolve
    m "I turned to the basket for a squirt of lube, then returned to Bryce's cock to spread it around."
    show maverick nice flip:
        zoom 1.35
        yanchor 1.0
        xanchor 0.5
        xpos 0.1
        ypos 1.0
    with easeinleft
    m "Maverick closed in on my other side. His cock was larger than Bryce's, but he still kept it just out of my reach, avoiding getting too close to me himself."
    $ renpy.pause(0.3)
    show bryce smirk:
        xpos 0.9
    show maverick normal flip:
        xpos 0.2
    with ease
    if bangok_four_bryce3_store.protection == True:
        m "I took a squirt of lube and another condom, then shuffled within reach of Maverick to apply it. The large dragon held his ground, refusing to show discomfort at my proximity."
    else:
        m "I took a squirt of lube, then shuffled within reach of Maverick to apply it. The large dragon held his ground, refusing to show discomfort at my proximity."

    $ renpy.pause(0.8)
    if bangok_four_bryce3_store.sebastian_in == True:
        Br smirk "Seb, do you want first go?"
        Sb smile "If you can share, you don't have to wait."
        Br brow "What do you mean, \"if I can share\"?"
        Br stern "I share! I'm just too big for you to take the front while I take the back."
        Sb smile "We can resolve that if you were on your back with [player_name] on top."
        Br brow "Hm."
        Br "[player_name]? What do you think?"
        menu:
            "I'd prefer to take you all one at a time.":
                jump bangok_four_bryce3_mcbottom_train
            "Sure, sounds fun.":
                jump bangok_four_bryce3_mcbottom_bryceseb_dp
            "You know, I should be able to take all three of you." if bangok_four_playerhasdick == False:
                c "If you got on top of the pile, Maverick?"
                Mv nice flip "..."
                Br flirty "I'm into it if you think you can take it."
                Sb drop "Seems a little extreme."
                jump bangok_four_bryce3_mcbottom_mav_bryce_mp
    else:
        Br normal "I assume you want me first, to ease up to Maverick's size."
        if bangok_four_playerhasdick == True:
            c "Yeah."
        else:
            $ bangok_four_bryce3_store.top_mav = True
            label bangok_four_bryce3_mcbottom_train_or_mp:
            menu:
                "Yeah, Bryce first.":
                    show bryce normal
                    show maverick nice
                    with dissolve
                "How about Maverick first?" if bangok_four_bryce3_store.top_mav == True:
                    $ bangok_four_bryce3_store.top_mav = False
                    show bryce brow with dissolve
                    Mv angry flip "I won't be responsible for severely injuring you if you're too small to take either of us."
                    Br brow "Really, [player_name]. At your size, you don't want to jump up to Maverick's in one go unless you're way more malleable than you look. Not when there's someone my size to ease the way."
                    jump bangok_four_bryce3_mcbottom_train_or_mp
                "Why not both of you?":
                    c "If you got on top of the pile, Maverick?"
                    show maverick nice
                    show bryce smirk
                    with dissolve
                    Mv nice "..."
                    Br flirty "Both? Damn. I'm into it if you think you can take it."
                    jump bangok_four_bryce3_mcbottom_mav_bryce_mp
        jump bangok_four_bryce3_mcbottom_train

label bangok_four_bryce3_mcbottom_mav_bryce_mp:
    hide bryce with dissolve
    m "Bryce rolled onto his back, cock swinging proudly into the air as his tail kicked up sand."
    hide maverick with dissolve
    m "Swallowing as I considered what I'd just decided to do, I went to the basket for one more handful of lube, then went back to Bryce to spread it over his length."
    Br flirty "Climb on up."
    scene stars at Pan((0, 360), (0, 0), 6.0) with dissolvemed
    $ renpy.pause (5.0)
    if bangok_four_bryce3_store.sebastian_in == True:
        m "I climbed onto Bryce's belly and lay back, trying to find the position I'd need once Maverick and Sebastian joined the party."
    else:
        m "I climbed onto Bryce's belly and lay back, trying to find the position I'd need once Maverick joined the party."
    m "I nestled into his chest easily, the position comfortable enough to sleep in."
    m "But I was looking for something much more fun."
    m "Picking myself up on my feet, straddling his belly, I lifted his cockhead to my rear entrance."
    Br smirk "Take this slow, okay?"
    Br normal "Don't want to hurt you and have to undo this cock pretzel."
    c "I'll try."
    m "Gently, I pushed more of my weight onto Bryce's tip, wiggling my hips to wedge open my rear and take Bryce's girth."
    $ renpy.pause(0.8)
    m "It was a struggle until the tip was in. I held myself for a moment, gasping as I adjusted to the wide spread. Then the long, slow slide down his lubricated length left me panting with need and want."
    $ renpy.pause(1.2)
    m "With Bryce hilted inside me, I leaned back again, splaying across Bryce's belly, legs spread to reveal where his cock held me in place, and my dribbling cunt where Maverick's would soon go."
    Br pant "W-Wow."
    m "He curled his head over, exhaling over my shoulder and upper body."
    Br flirty "Alright Maverick."
    Br laugh "Try not to step on me too much!"
    show maverick normal:
        zoom 1.3
        yanchor 0.0
        xanchor 0.25
        xpos 0.5
        ypos 0.7
    with easeinbottom
    $ renpy.pause (0.3)
    Mv nice "..."
    show maverick nice:
        ease 2.0 zoom 1.5 ypos 0.4
    with None
    $ renpy.pause(0.3)
    scene black with dissolvemed
    m "Maverick stepped carefully over Bryce's hindquarters, then overtop me."
    m "I caught my breath, the space between the two dragons' chests rapidly warming, the chill of the night air displaced by their heat."
    m "Then I felt Maverick's tip slide along one of my thighs, before finding my outer lips."
    m "His head flared wider than any penis I'd ever felt down there before. At first I worried it wouldn't fit, until he began to apply pressure and I felt his head compress slightly to nestle in my outer folds."

    Br laugh "Think I can feel you, there!"
    Br flirty "You coming in?"

    if bangok_four_bryce3_store.sebastian_in == True:
        Sb disapproval "If it hurts, [player_name], say something."

        Br normal "[player_name] will be fine. Probably."
        Br normal "You ready for Maverick?"

        $ renpy.pause(0.5)
        c "Yeah."

    Mv "..."
    Mv "I'm not trying to hurt you. Tell me if I need to stop."

    c "I will."

    m "Hesitantly, Maverick began to press forward, the lube on his tip squishing into every nook and cranny of my lips."
    m "I squirmed, Bryce's cock twisting slightly in my ass as I struggled to help aim the flat pressure on my cunt deeper into my passage, where there was space for Maverick to enter."
    m "Then his tip popped in, stretching my hole to its limit, rubbing my inner walls as he sank a couple inches inside me."
    c "Ah! W-Wow."
    m "Squaring his feet, Maverick kept pushing, sinking wide, thick cockflesh into my cooch at a steady pace. My lower body fell limp, muscles rendered inoperable by the stretching, sliding waves of pleasure and pain as Maverick's cock invaded."
    menu:
        "Oh holy fuck!":
            pass
        "[[Incoherent babbling.]":
            pass
        "Maverick, you're {i}huge{/i}!":
            Br laugh "Yeah he is!"
    Mv nice "..."
    Br smirk "You okay there, [player_name]? I can feel Mavers sliding into you."
    m "I could feel it too; the pair of massive cocks squished the walls of my colon and vagina together, the muscles of the latter stimulating both as they tried and failed to squeeze the large insertion plowing through."
    m "Then I ran out of room."
    c "S-Stop! Ngh!"
    m "Maverick stopped immediately, even pulling back slightly as his tip brushed my innermost gate, length stretching me around him through the entire depth of my canal."

    $ renpy.pause(0.8)

    Mv nice "Is that your cervix?"
    m "A few spasms of my deepest muscles confirmed Maverick's guess."
    c "Y-Yeah. Ow."
    Br normal "Y'know, Mav's ex would take it through there."
    Mv angry "You don't need to share that with [player_name]!"
    if bangok_four_bryce3_store.sebastian_in == True:
        Sb drop "[player_name] isn't Maverick's ex, Bryce."
    if not persistent.bangok_cervpen:
        c "Humans can't do that. I definitely can't."
        jump bangok_four_bryce3_mcbottom_mav_bryce_mp_nocervpen 
    menu:
        "I want it all.":
            if bangok_four_bryce3_store.sebastian_in == True:
                Sb drop "You can't be serious."
            else:
                Mv normal "..."
            Br flirty "I mean, worth a shot, right?"
            Mv normal "..."
            if bangok_four_bryce3_store.sebastian_in == True:
                Sb drop "Bryce, maybe. But Maverick? Without preparation? I don't know how anyone runner size or smaller can take that."
                Br smirk "You take that."
                Sb disapproval "I don't have a cervix, Bryce."
            else:
                Br smirk "Just think about it. Sebastian can take all of you. Why not [player_name]?"
            Mv normal "Are you sure, [player_name]?"
            menu:
                "Fuck yes!":
                    $ bangok_four_bryce3_store.mavtarget = "womb"
                    if bangok_four_bryce3_store.sebastian_in == True:
                        Sb drop "Oh damn."
                    Br smirk "This is gonna feel great."
                "Er...":
                    $ bangok_four_bryce3_store.mavtarget = "vag"
                    Mv normal "Then we won't."
        "I can't take more than this.":
            label bangok_four_bryce3_mcbottom_mav_bryce_mp_nocervpen:
            $ bangok_four_bryce3_store.mavtarget = "vag"
            if bangok_four_bryce3_store.sebastian_in == True:
                Sb normal "That's good. Keep your limits in mind."
            Br laugh "Fair enough."

    if bangok_four_bryce3_store.mavtarget == "womb":
        m "Maverick returned his tip to my innermost gate, then began to apply pressure."
        m "The attempted insertion became painful in mere moments, his tip far too wide to stretch me around him properly, as he'd done at my outer entrance."
        $ renpy.pause(0.8)
        m "I spread my legs a little wider while I still had control over them, struggling to find something to do with my arms as I gasped and hissed, taking the pressure far beyond what I thought safe or possible."
        $ renpy.pause(1.2)
        m "Then my cervix gave, bowing inward before being finally stretched open to admit Maverick's girth into my deepest center."
        scene white with fadequick
        m "Every nerve in my lower body whited out, the width to which I'd been stretched too much to comprehend. I came, thrown over my peak by the sensation of intense penetration."
        $ renpy.pause(1.0)
        scene black with dissolveslow
        $ renpy.pause(0.3)
        m "When I came back down, Bryce and Maverick both were hilted in me. I could feel their cocks rubbing together within me through my inner walls, as my body shifted. I rose and fell with Bryce's breathing, sandwiched between his belly and Maverick's and stuffed inside with their man meat."
        $ renpy.pause(0.5)
        if bangok_four_bryce3_store.sebastian_in == True:
            Sb drop "Are you okay, [player_name]? You, ah, made a lot of noise when Maverick went in."
        else:
            Br smirk "Cock to cock in you."
        m "I slid a hand between my belly and Maverick's hard plates, feeling the contour of his cock through my skin and womb. Most of the pain at my innermost gate was gone, blanketed under a statickey feeling of arousal at every twitch in Maverick's length."
        c "That... was... incredible."
        Br laugh "Was it, now?"
        Br flirty "You know the fucking comes next, right?"
    else:
        m "I spent several long moments adapting to the feeling of the two large cocks competing for space inside me."
        m "I could feel them rubbing together through my inner walls, as my body shifted. I rose and fell with Bryce's breathing, sandwiched between his belly and Maverick's and stuffed inside with their meat."
        m "I slid a hand between my belly and Maverick's hard plates, feeling the contour of his cock through my skin and vagina. My inner walls squeezed back at every twitch in Maverick's length, unable to gather the strength to contract properly around the massive penetration without the stimulation."
        c "So, now..."

    if bangok_four_bryce3_store.sebastian_in == True:
        m "Maverick backed his head up and Bryce lolled his back, exposing my face to the cold nighttime air."
        m "Then a concerned-looking Sebastian stepped over Bryce's head, condom-enwrapped cock not far from my face."
        Sb disapproval "Are you sure you're prepared for this? I'm worried you might have trouble getting these two's attention if--"
        m "Bryce nudged Sebastian's hindquarters with his snout, pushing him closer to me."
        Br normal "If something goes wrong, [player_name] will get your attention and you'll get ours."
        Br smirk "But the hard part is already over. We fit."
        Sb drop "I don't recall that being the hard part."
        $ renpy.pause(0.8)
        Sb normal "[player_name], how deep are you okay with me going in your mouth?"
        menu:
            "Mouth.":
                $ bangok_four_bryce3_store.sebtarget = "mouth"
            "Throat.":
                $ bangok_four_bryce3_store.sebtarget = "throat"
        Sb smile "Alright."

        $ renpy.pause (0.8)

        m "Sebastian stepped close enough I could accept his condom-wrapped tip into my mouth. Then he pushed a little further, filling my mouth with the warmth of his length and the taste of the condom. I began to slurp and lick, preparing for the next step."

    $ renpy.pause (0.5)
    play soundloop "fx/rub2.ogg"
    m "The gangbang began for real with Maverick pulling back and taking his first thrust, then his next, and his next, at a rough cadence."
    m "Bryce rolled his hips, fucking my ass lightly with what little room he could move. He hardly needed to do more, as Maverick's thrusting above drove through my body, stimulating both of us."

    # Going to borrow `top_mav` here again to decide if Mav uses you and gets off before everyone else or if he and Bryce go at the same time.

    if bangok_four_bryce3_store.sebastian_in == True:
        if bangok_four_bryce3_store.sebtarget == "throat":
            m "Pushing lightly against each of Maverick's thrusts, Sebastian worked to the back of my mouth, then began gently holding himself in place as I was shoved to take him in my throat, slightly deeper each time."
        else:
            m "Pushing lightly agaisnt each of Maverick's thrusts, Sebastian explored the nooks and crannies of my mouth, brushing over, under, and around my tongue as I tried my best to suck him with all the mindblowing sensations in my lower half."


        $ renpy.pause (0.8)
        m "Abruptly Sebastian thrust at a slightly odd angle. I gagged and Sebastian pulled out. Bryce's head nearly bumped into mine as he nuzzled into Sebastian's crotch with me."
        Sb drop "Ha. Ah. How are you holding up?"
        menu:
            "{i}More{/i}":
                $ bangok_four_bryce3_store.top_mav = False
                Sb smile "Sure."
                m "Bryce's tongue flicked my nose as he licked Sebastian's length, even while Sebastian slipped back into my mouth."
                if bangok_four_bryce3_store.sebtarget == "throat":
                    m "Then the cock in my mouth was back in my throat, fucking deeper."
                m "Bryce lolled his head back, slapping his tail to the ground, thrusting harder into my ass, pressing me up against Maverick with his hips."
            "I-- Agh-- Ngh--":
                $ bangok_four_bryce3_store.top_mav = True
                Sb disapproval "Do you need help?"
                m "I couldn't deny the rough fuck hurt, but my inflamed nerves desperately didn't want the sensations to end. If they pulled out, I wasn't sure I'd push through the pain to let them back in."
                c "N-No."
                m "Even still Bryce slowed, easing up on the pressing angles in my ass. Maverick didn't change his pace in the slightest. Sebastian's condom tip bapped against my face."
                Sb normal "May I?"
                if bangok_four_bryce3_store.sebtarget == "throat":
                    m "I accepted him back into my mouth, took a breath, then took him deeper, plugging all three of my holes with cock."
                else:
                    m "I accepted him back into my mouth, licking and slurping his head to try to give him a fraction of what I was feeling, while Bryce licked his base."
        $ renpy.pause (0.8)
        m "I swooned, the thick meat stuffing me from every angle more than a human mind could take."
    else:
        $ renpy.pause (0.8)
        Br pantflirt "Ngh. Hah. You ok there?"
        menu:
            "{i}More{/i}":
                $ bangok_four_bryce3_store.top_mav = False
                Br pant "You got it."
                m "Bracing his tail on the ground, Bryce pushed harder into my ass, pressing me up against Maverick with his hips."
            "I-- Agh-- Ngh--":
                $ bangok_four_bryce3_store.top_mav = True
                m "I couldn't deny the rough fuck hurt, but my inflamed nerves desperately didn't want the sensations to end. If they pulled out, I wasn't sure I'd push through the pain to let them back in."
                m "Bryce slowed, easing up on the pressing angles in my ass. Maverick didn't change his pace in the slightest."
        $ renpy.pause (0.8)
        m "I swooned, the thick meat stuffing me from both sides more than a human mind could take."

    m "More than a dozen thrusts passed with my mind numb, my body limp, experience of the world awash with arousal and heat shared by the dragons filling me."

    if bangok_four_bryce3_store.mavtarget == "womb":
        if bangok_four_bryce3_store.top_mav == True:
            m "When I came back to my senses, it was to Maverick's thrusts increasing in depth and urgency. The slit between his horizontal plates pressed up against my spread outer folds on every thrust, pushing my legs wider and shoving me a little ways up Bryce's cock."
        else:
            m "When I came back to my senses, it was to Maverick's and Bryce's thrusts both increasing in depth and urgency. The slit between Maverick's horizontal plates pressed up against my spread outer folds on every thrust. Bryce pressed on my shoulder, holding me down so each of his thrusts spread my cheeks against his hard plates."
        m "On each pull out, Maverick withdrew closer and closer to my cervix, his head tugging back on my gate and sending electric shocks through my lower body."
        stop soundloop fadeout 0.5
        m "Then Maverick's head popped out of my womb, the explosion of sensation bringing me just within grasping distance of another peak. I reached for it."
        play soundloop "fx/rub1.ogg"
        scene white with fadequick
        m "When Maverick redoubled his pace, punching through my cervix with every thrust, I was blown away."
    else:
        m "When I came back to my senses, it was to Maverick's thrusts increasing in depth and urgency. His head kissed and tapped my cervix, not pressing, but reaching just deep enough to trigger the electric sparks of pain and pleasure."
        m "On each pull out, Maverick withdrew closer and closer to my entrance, his head tugging back on my spread outer folds. The stretching of my lips dealing with his large head rubbed my clit, flooding my head with yet more waves of arousal."
        stop soundloop fadeout 0.5
        m "Then Maverick popped his head all the way out of my passage, the explosion of sensation in my lips bringing me just within grasping distance of my peak. I reached for it."
        play soundloop "fx/rub1.ogg"
        scene white with fadequick
        m "When Maverick redoubled his pace, spearing my entire canal and kissing my cervix with every thrust, I was blown away."

    $ renpy.pause(0.8)
    stop soundloop fadeout 0.3
    if bangok_four_bryce3_store.top_mav == True:
        jump bangok_four_bryce3_mcbottom_mav_bryce_mp_top_mav
    else:
        jump bangok_four_bryce3_mcbottom_mav_bryce_mp_twin_climax

label bangok_four_bryce3_mcbottom_mav_bryce_mp_twin_climax:
    Br pant "Ohh-h d-damn!"
    if bangok_four_bryce3_store.mavtarget == "womb":
        if persistent.bangok_knot == True:
            m "Bryce's tail wrapped around Maverick's, slowing the rough pace but for a last few thrusts. Both of them avoided slamming all the way inside me as they worked their way over their now-inevitable peaks."
        else:
            m "Bryce's tail wrapped around Maverick's, slowing the rough pace but for a last few thrusts. With Bryce's paw on my shoulder, both of them bottomed out, sheathing inside me in prepearation for their now-inevitable peaks."
    else:
        if persistent.bangok_knot == True:
            m "Bryce's tail wrapped around Maverick's, slowing the rough pace but for a last few thrusts. Both of them avoided slamming all the way inside me as they worked their way over their now-inevitable peaks."
        else:
            m "Bryce's tail wrapped around Maverick's, slowing the rough pace but for a last few thrusts. With Bryce's paw on my shoulder, he held me in place, using Maverick's reticence to breach my innermost gate to lift his hips high enough to bottom out in my ass for his now-inevitable peak."

    play sound "fx/dragonpain.ogg"
    $ renpy.pause(0.3)
    play sound2 "fx/snarl.ogg"
    $ renpy.pause(1.0)

    m "Squeezing my lower body between them, Bryce and Maverick came to twitching, roaring orgasm inside me."
    if bangok_four_bryce3_store.mavtarget == "womb":
        if bangok_four_bryce3_store.protection == True:
            m "Jets of hot seed bloated their condoms, one expanding to fill my womb, the other deep in my rear. The cocks twitched and pulsed against each other, squeezing my stretched canal and dilated cervix, dragging out my own peak as they poured into me."
            scene black with dissolvemed
            if persistent.bangok_inflation == True:
                if bangok_four_bryce3_store.sebastian_in == True:
                    m "Their loads kept coming, condoms filling like balloons, forcing my womb and colon to expand around them. My breath left me in a rush around Sebastian's cock as my belly bloated with condom-contained cum, prying my two draconic fillers apart."
                else:
                    m "Their loads kept coming, condoms filling like balloons, forcing my womb and colon to expand around them. My breath left me in a rush as my belly bloated with condom-contained cum, prying my two draconic fillers apart."
    else:
        if bangok_four_bryce3_store.protection == True:
            m "Jets of hot seed spilled into their condoms, one rapidly filling in my stretched canal, the other deep in my rear. The cocks twitched and pulsed, against each other, squeezing my stretched canal and dragging out my peak as they poured into me."
            scene black with dissolve
            if persistent.bangok_inflation == True:
                m "Maverick pulled back to the limit before his head popped free, tugging his condom reservoir and Bryce's hindquarters back. Even still his load kept coming, the condom filling like a balloon in my tight channel until it was pressing against my every inner wall for an escape."
                m "The combined expansion of my love passage and colon pressed my belly outward with condom-contained cum, prying my two draconic fillers apart."
        else:
            m "Maverick's first jet of cum spattered against my innermost gate. The second pushed the first through."

    if bangok_four_bryce3_store.protection == False:
        m "Rope after rope of cum spilled into my womb and guts, flooding my most and least sacred places with hot dragon seed. Their cocks twitched and pulsed against each other, squeezing my stretched and abused love canal, dragging out my own peak as they poured into me."
        scene black with dissolvemed
        if persistent.bangok_inflation == True:
            m "The load in my womb kept coming, seed packing my tubes and womb until no room remained. Yet more cum came, forcing my womb to expand around it. My guts filled too, colon packed with Bryce's seed, before more pulsing jets forced the seed even deeper."
            m "My belly bloated, pregnant and stuffed with twin dragonloads."
    play soundloop "fx/breathing.ogg" fadein 1.0
    m "Their pulses slowed, {w=0.3}then {w=0.3}finally came to an end. Maverick panted above me, tired out by having to lift Bryce's hindquarters with his thrusts toward their last few moments."
    if bangok_four_bryce3_store.sebastian_in == True:
        m "Sebastian withdrew his cock from my mouth, and Bryce uncoiled his tail from Maverick's to slump slightly out of my ass."
    else:
        m "Bryce uncoiled his tail from Maverick's, the weight of his hindquarters falling pulling some of his cock out of my ass."
    Br pantflirt "H-Hot damn."
    Br pant "I'm spent. That... ahh."
    Br pantflirt "[player_name]? We, ah, didn't hurt you, right?"
    menu:
        "Amazing.":
            Br pant "Alright!"
        "Can't... move...":
            Br smirk "You know we're still inside you, right?"
        "Gonna be really sore.":
            Br smirk "Kinda unavoidable. Did you have fun, though?"
            if bangok_four_bryce3_store.sebastian_in == True:
                Sb drop "That amount of sore doesn't sound like fun, Bryce."
        "I think I'll take stock once I'm done tonight.":
            if bangok_four_bryce3_store.sebastian_in == True:
                Br pant "I don't think finishing Sebastian will make things much worse."
                Sb disapproval "If this has been too much, I'm not going to force that on [player_name]."
            else:
                Br pant "You are done. Just... gotta get us back out."








label bangok_four_bryce3_mcbottom_mav_bryce_mp_top_mav:
    if bangok_four_bryce3_store.mavtarget == "womb":
        if persistent.bangok_knot == True:
            if bangok_four_bryce3_store.sebastian_in == False:
                m "Abruptly, Maverick stuttered to a stop, through my cervix but a little short of hilting me. Even still, the violent thrust pushed me up Bryce's cock a distance I could feel sliding out."
            elif bangok_four_bryce3_store.sebtarget == "throat":
                m "Abruptly, Maverick stuttered to a stop, through my cervix but a little short of hilting me. Even still, the violent thrust pushed me up Bryce's cock, and shoved Sebastian's slit into my face as his cock hilted in my neck."
            else:
                m "Abruptly, Maverick stuttered to a stop, through my cervix but a little short of hilting me. Even still, the violent shove pushed me up Bryce's cock, and shoved Sebastian's shaft to the back of my mouth."
        else:
            if bangok_four_bryce3_store.sebastian_in == False:
                m "Abruptly, Maverick slammed me into his hips, hilting me as deep as he could go, spearing my womb and stretching my vagina around his dragonhood like a toy. The violent thrust pushed me up Bryce's cock a distance I could feel."
            elif bangok_four_bryce3_store.sebtarget == "throat":
                m "Abruptly, Maverick slammed me into his hips, hilting me as deep as he could go, spearing my womb and stretching my vagina around his dragonhood like a toy. The violent thrust pushed me up Bryce's cock and shoved Sebastian's slit into my face as his cock hilted in my neck."
            else:
                m "Abruptly, Maverick slammed me into his hips, hilting me as deep as he could go, spearing my womb and stretching my vagina around his dragonhood like a toy. The violent thrust pushed me up Bryce's cock and shoved Sebastian's shaft to the back of my mouth."
        play sound "fx/dragonpain.ogg"
        $ renpy.pause(1.0)
        
        if bangok_four_bryce3_store.protection == True:
            m "Maverick's condom's tip bloated in my womb, flooded with his seed, expanding to fill my most sacred place. His cock twitched and pulsed against my stretched canal and dilated cervix, dragging out my peak as he poured into me."
            scene black with dissolvemed
            if persistent.bangok_inflation == True:
                m "His load kept coming, the condom filling like a balloon, forcing my womb to expand around it, pressing back against Bryce's cock in my ass and Maverick's belly above me."
    else:
        m "Abruptly, Maverick stuttered to a stop, in the middle of my passage, twitching enough to lift me partly up Bryce's length."
        play sound "fx/dragonpain.ogg"
        $ renpy.pause(1.0)
        if bangok_four_bryce3_store.protection == True:
            m "Maverick's cum spilled into his condom, rapidly filling it in my stretched canal. His cock twitched and pulsed, dragging out my peak as he poured into me."
            scene black with dissolve
            if persistent.bangok_inflation == True:
                m "He pulled back to the limit before his head popped free, tugging his condom reservoir back. Even still his load kept coming, the condom filling like a balloon in my tight channel until it was pressing against my every inner wall for an escape."
                m "It put heady pressure on Bryce's cock within me and Maverick's belly above."
        else:
            m "Maverick's first jet of cum spattered against my innermost gate. The second pushed the first through."


    if bangok_four_bryce3_store.protection == False:
        m "Rope after rope of cum spilled into my womb, flooding my most sacred place with Maverick's seed. His cock twitched and pulsed, dragging out my peak as he poured into me."
        scene black with dissolvemed
        if persistent.bangok_inflation == True:
            m "His load kept coming, seed packing my tubes and womb until no room remained. Yet more cum came, forcing my womb to expand around it, pressing back against Bryce's cock in my ass and Maverick's belly above me."
    play soundloop "fx/breathing.ogg" fadein 1.0
    m "His pulses slowed, {w=0.3}then {w=0.3}finally came to an end. Maverick panted above me, tired out by the angle he'd had to take to work on top of Bryce."
    if bangok_four_bryce3_store.sebastian_in == True:
        m "Sebastian withdrew his cock from my mouth, and Bryce stilled, giving everyone a chance to check on me."
    else:
        m "Bryce stilled, taking the moment after Maverick's climax to check on me."
    Br flirty "That felt amazing, and I'm not even you."
    Br normal "How are you feeling?"
    menu:
        "Amazing.":
            Br laugh "Alright!"
        "Can't... move...":
            Br smirk "You know he's still inside you, right?"
        "Gonna be really sore.":
            Br smirk "Kinda unavoidable. Did you have fun, though?"
            if bangok_four_bryce3_store.sebastian_in == True:
                Sb drop "That amount of sore doesn't sound like fun, Bryce."
        "I think I'll take stock once I'm done tonight.":
            Br flirty "Can't wait for more, huh?"

    # if persistent.bangok_watersports == True:
    #     Br smirk "Hm. Y'know, Maverick and I had a few drinks in that party."
    #     if bangok_four_bryce3_store.sebastian_in == True:
    #         Sb normal "Oh, here we go."

    m "Maverick began carefully to pull out, large girth tugging on my limp inner muscles."
    if bangok_four_bryce3_store.protection == True:
        menu:
            "N-No...":
                Br brow "No? What's wrong?"
                m "Maverick paused, leaving me spread around him."
                menu:
                    "L-Leave the condom in?" if bangok_four_bryce3_store.protection == True:
                        Br laugh "Ha! Damn, that's kinky."
                        Br flirty "I'd appreciate it if you did, Mavers."
                        $ renpy.pause(0.8)
                        Mv normal "Fine."
                        $ bangok_four_bryce3_store.mavcondomleftin = True
                        m "Working backward with his forelegs, Maverick arched his back until he could reach one sandy paw back. He wiped his paw on my leg, ridding it most of the grains before squeezing and tugging at the condom material."
                        m "Inching maddeningly slowly back out of me, Maverick slid his length from the condom, leaving the long protective sheath and his liquid gift both resting inside me."
                        if bangok_four_bryce3_store.sebastian_in == True:
                            m "Before Maverick pulled out completely, Sebastian knelt down next to our joining."
                            Sb normal "Here. Let me tie it off with actual hands."
                            m "He squeezed off the condom material just after Maverick's head tugged back through my folds. The cold keratin of his claws scraped my thighs."
                            m "I felt the stretching and twisting as he tugged slightly more of the condom out of me to tie it off. Then it relaxed, as Sebastian dropped the knot back against my folds."
                            Sb smile "There. That what you were going for, [player_name]?"
                        else:
                            m "When his head tugged back through my folds, Maverick pinched off the condom with a squeeze and a twist, the cold keratin of his claws scraping the insides of my thighs."
                            m "Then he worked his way back until he could get his muzzle between my legs. With a combination of his scaly lips, paw, and tugging and holding the condom against the side of my leg, he managed to get it tied off."
                            m "The stretched material snapped the knot against my abused folds when he let it go."

                        if bangok_four_bryce3_store.mavtarget == "womb":
                            if persistent.bangok_inflation == True:
                                m "I sighed with contentment, my pregnancy of cum full, round, and undisturbed."
                            else:
                                m "I sighed with contentment, feeling Maverick's balloon of seed resting deeper inside me than any human could hope to deliver."
                        else:
                            if persistent.bangok_inflation == True:
                                m "I sighed happily, my vagina feeling just as stuffed by Maverick's bloated cum balloon as when he himself had been inside."
                            else:
                                m "I sighed happily, feeling Maverick's load resting deep inside my canal, almost at my inner gate."
                    "G-Go more slowly.":
                        Mv normal "I'm taking this as slowly as I can."
            "Ohhh...":
                pass

    if bangok_four_bryce3_store.mavcondomleftin == False:
        if bangok_four_bryce3_store.mavtarget == "womb":
            if bangok_four_bryce3_store.protection == True:
                if persistent.bangok_inflation == True:
                    m "The balloon of cum pulled at my inner gate, thick, heavy, and unwilling to move from my bloated belly."
                    m "Maverick stopped, cognizant he couldn't make any more progress without hurting me or breaking the condom."
                    menu:
                        "J-Just tear it.":
                            Mv "You are sure?"
                            m "I nodded, knowing that as my cervix began to recover, it'd make getting the uncooperative balloon of cum out of me all the more painful."
                            m "Maverick tugged harder, managing to stretch the condom material to the point his head had almost pulled through my folds."
                            play sound "fx/bubbles.ogg"
                            play sound2 "fx/spray.ogg"
                            $ bangok_four_bryce3_store.mavbroke == True
                            m "He pulled out, tearing the condom material and leaving my cunt lips empty and gaped in one pull. I gasped as the barrier's stretching force disappeared, a river of cum leaking from my breached inner gate to spatter over my legs and Bryce's cock and hindquarters."
                            Br laugh "Hey! I didn't think I'd be getting the mess!"
                        "H-How do we get it out?":
                            m "Gently, Maverick curled his tail around, then pressed it against my distended belly."
                            m "I gasped, feeling almost like I was pissing as Maverick's cum flowed from the reservoir of his condom to pool in and around his tip, forced out by the added pressure of Maverick's tail."
                            m "Then the rest of the reservoir popped through, the blob of cum shoving Maverick's cock out of me."
                            play sound "fx/uncork.ogg"
                            m "The bloated condom plopped out onto Bryce's tail, before Maverick dragged it away to the ground."
                else:
                    m "When his head tugged out of my fuck-hole it gaped, easily allowing his condom's reservoir to pop free and bounce off Bryce's cock."
            else:
                m "As he pulled back through my cervix, fluid splashed from my womb, saturating my canal's walls."
                if persistent.bangok_inflation == True:
                    m "When his head tugged out of my fuck-hole it gaped, letting a river of cum pour from inside me onto Bryce's cock and hindquarters."
                    Br laugh "Hey! I didn't think I'd be getting the mess!"
                else:
                    m "When Maverick's head tugged through my lips, I remained gaped open. A dribble of cum spilled from my canal onto where Bryce's cock speared my ass, the rest still trapped much deeper inside me."
        else:
            if bangok_four_bryce3_store.protection == True:
                m "Maverick's condom popped free of my abused folds, bouncing off where Bryce's cock still speared my ass."
            else:
                m "When Maverick's head tugged through my lips, I remained gaped open. A dribble of cum spilled from my canal onto where Bryce's cock speared my ass, the rest still trapped much deeper inside me."

    stop soundloop fadeout 3.0
    scene stars at Pan((0, 20), (0, 20), 0.0) with dissolvemed
    if bangok_four_bryce3_store.sebastian_in == True:
        Sb disapproval "Maverick? Where are you going?"
    else:
        Br brow "Maverick? Going somewhere?"
    Mv normal "Home."
    Br stern "After {i}that{/i}? There's no way [player_name] is walking after that. You're kinda big, and that was not nearly enough prep."
    if bangok_four_bryce3_store.sebastian_in == True:
        Sb drop "I'm not going to be able to stay and help, so if Bryce needs help getting [player_name] home..."
        Mv normal "No. I think Bryce has that covered."
    else:
        Br brow "If I need help getting [player_name] home..."
        Mv normal "No. I think you have that covered."

    $ renpy.pause(0.5)
    Br stern "Maverick!"
    m "Bryce's shout vibrated through my back, and his cock still in my ass. I slumped, unable to contribute to the situation."
    $ renpy.pause(1.2)
    Br "He left."

    $ renpy.pause(0.8)
    Sb drop "Not to be that asshole, but I do have to go sooner rather than later."
    if bangok_four_bryce3_store.mavcondomleftin == True:
        Sb normal "[player_name], it looks like there's room to fuck you past Maverick's condom. Or we could finish the way we started. Or if Maverick's actions didn't really leave you in the mood... Up to you."
    else:
        Sb normal "[player_name], I'm happy with wherever you want me to finish. Or if Maverick's actions didn't really leave you in the mood... Up to you."
    menu:
        "Fuck me.":
            pass
        "Finish in my mouth.":
            pass
        "I'm done. N-No more.":
            pass


    jump todo_out_of_content_bangok_four_bryce3

label bangok_four_bryce3_mcbottom_train:
    scene beachx:
        xanchor 0.5
        yanchor 1.0
        xpos 0.5
        ypos 1.0
    with dissolve
    m "I moved further from the basket, finding an empty spot on the beach so that any kicked up sand wouldn't wind up in Bryce's protection supplies."
    m "Then, thinking about the dragons' limited articulation, I got on all fours, presenting my ass back at them."
    Br flirty "That's a view."
    if bangok_four_bryce3_store.sebastian_in == True:
        Br normal "Sebastian, care to ease [player_name] into this?"
        m "Sebastian's footsteps padded up behind me. Then I felt near-frigid claws spreading my backside."
        if bangok_four_playerhasdick == True:
            $ bangok_four_bryce3_store.sebtarget = "ass"
        else:
            Sb normal "Front or back?"
            menu:
                Sb "Front or back?{fast}"
                "Anal.":
                    $ bangok_four_bryce3_store.sebtarget = "ass"
                "Vaginal.":
                    $ bangok_four_bryce3_store.sebtarget = "vag"
        Sb smile "Mind if I have a taste, first?"
        menu:
            "Go for it.":
                if bangok_four_bryce3_store.sebtarget == "ass":
                    m "Sebastian moved lower between my thighs, momentarily nestling his snout between my cheeks. Hot exhales washed over the small of my back, before his tongue pressed up to, then into my sphincter."
                else: #vag
                    m "Sebastian moved lower between my thighs, momentarily nestling his snout in my taint. Hot exhales washed over the lower part of my belly, before his tongue darted into my folds."
                Br smirk "Are you kidding me? You already ate!"
                m "I felt Sebastian wiggle as he drove his tongue deeper. Then I heard his tail strike the sand, flicking a grainy spray back at Bryce and Maverick."
                Br laugh "Okay! Okay! Have fun in there. Just don't take all night."
                if bangok_four_bryce3_store.sebtarget == "ass":
                    # Sebastian the ass man
                    m "I pushed my hips back, clenching around Sebastian's tongue as he drove yet deeper, smearing my hole with saliva."
                else:
                    m "I pushed my hips back, squeezing Sebastian's tongue with my inner walls as he lapped up my juices."
                m "Then Sebastian pulled back, panting."

            "Let's skip to the next step.":
                Sb disapproval "Sure."

        m "Holding onto my back, Sebastian worked his way forward, condom-wrapped cock bouncing off one of my cheeks."
        if bangok_four_bryce3_store.sebtarget == "ass":
            m "Then he placed his tip up against my ass."
        else:
            m "Then he nestled his tip between my pussy lips."
        Br flirty "Now the show starts!"
        Sb smile "Ready?"
        $ renpy.pause(0.5)
        c "Yeah."
        $ renpy.pause(0.5)
        m "Sebastian slid into me, lubrication on the condom letting me spread with relative ease."
        m "I thrust back against him, heady with the first taste of cock this evening, what I knew would be the first of many."
        play soundloop "fx/rub2.ogg" fadein 0.5
        show beachx:
            linear 0.15 zoom 1.008
            ease 0.5 zoom 1.0
            repeat
        with None
        if bangok_four_bryce3_store.sebtarget == "ass":
            m "Picking up on my lack of discomfort with him, Sebastian quickly began a faster pace, sinking deep enough into my ass with each thrust to slap his thighs against mine."
            $ renpy.pause(0.8)
            m "I leaned forward into the sand, the hard assfucking already more than I'd imagined I'd get from this BBQ, and yet still only the first act."
        else:
            m "Picking up on my lack of discomfort with him, Sebastian quickly began a faster pace, thrusting deep enough into my love canal with each thrust that my lips met his."
            $ renpy.pause(0.8)
            m "I leaned forward into the sand, the hard fucking already more than I'd imagined I'd get from this BBQ, and yet still only the first act."
        $ renpy.pause(1.2)

        Br flirty "Damn! Taking you like a champ, Sebastian!"
        Br smirk "Probably won't be quite so easy when it's Maverick, though."
        menu:
            "Wait... and... see.":
                Br laugh "Oh! That's a challenge!"
                Br smirk "What do you say to that, Maverick?"
                Mv nice "..."
            "[[Moan.]":
                Sb shy "G-Glad you're having fun."
            "[[Thrust back.]":
                pass
        m "Putting some of his weight on my shoulders, Sebastain leaned forward, increasing the depth of shaft he moved with each thrust, all but pulling out of me with each withdrawl before spearing all the way back down."
        if bangok_four_bryce3_store.sebtarget == "vag":
            m "My inner walls spasmed, kneading at his cock when they could, before rapidly losing their hold and being left with the ghost of sensation."

        if persistent.bangok_knot == True:
            Br smirk "You know, [player_name] takes you so easily, you could probably knotfuck."
            Br flirty "Help spread [player_name] out for us."
            Sb smile "Do... you... want that?"
            menu:
                "Ngh. Would... rather... not.":
                    $ bangok_four_bryce3_store.knotfuck = False
                "[[Moan.]":
                    Sb disapproval "That's... not clear."
                    Br laugh "Do it anyway!"
                    Sb disapproval "Bryce!"
                    Br flirty "They want it."
                    menu:
                        "Nod head.":
                            $ bangok_four_bryce3_store.knotfuck = True
                            Sb smile "Well... maybe..."
                        "Shake head.":
                            $ bangok_four_bryce3_store.knotfuck = False
                            Sb disapproval "No... they... don't."
                        "Keep moaning.":
                            $ bangok_four_bryce3_store.knotfuck = True
                            Sb disapproval "Well... maybe..."
                "Yes.":
                    $ bangok_four_bryce3_store.knotfuck = True
                    Sb smile "Sure."
        else:
            $ renpy.pause(1.5)

        if bangok_four_bryce3_store.sebtarget == "ass":
            m "Sebastian bore down on my ass, the stimulation pushing me toward my peak despite ignoring my genitals."
            if bangok_four_playerhasdick == True:
                m "My cock twitched, a few small droplets of pre dribbling onto the sand as I neared sweet release."
            else:
                m "My empty hole spasmed, juices leaking down my thighs as I neared sweet release."
        else:
            m "Sebastian bore down, carrying me upward toward my peak."
            m "My hole squeezed, juices dribbling around his length and down my legs as I neared sweet release."
        stop soundloop fadeout 0.5
        show beachx:
            linear 0.15 zoom 1.0
        with None
        play sound "fx/snarl.ogg"
        if persistent.bangok_knot == False or (persistent.bangok_knot == True and bangok_four_bryce3_store.knotfuck == True):
            m "Then, abruptly, before I could get there, he yanked my hips flush against his and came to a stop. Heat spurt into me, filling the condom reservoir at his tip."
            if persistent.bangok_inflation == True:
                if bangok_four_bryce3_store.sebtarget == "ass":
                    m "The load kept growing, pulse after pulse expanding the reservoir until it began to stretch down my colon, leaving me with a heady sense of fullness."
                else:
                    m "The load kept growing, pulse after pulse expanding the reservoir until it filled what little space remained in my passage after his shaft. I squirmed from the pressure on my innermost gate."
            m "He panted onto my back as his orgasm came to an end."
            $ renpy.pause (0.5)
            if persistent.bangok_knot == True and bangok_four_bryce3_store.knotfuck == True:
                Br smirk "Knotfuck time."
                if bangok_four_bryce3_store.sebtarget == "ass":
                    m "As Sebastian began to tug back, I felt the bulge of flesh near his base squeezed tight by my sphincter. I hissed, forced wide as he pulled the thick nodule through my tight hole. When the pressure abruptly released, my hole closing around the far side, I gasped with relief."
                    m "Then Sebastian switched directions."
                    c "Nngh!"
                    m "The knot went in more easily than it came out, wedging through my muscle and leaving Sebastian fully nestled inside me again. Then he switched once more."
                    c "Ah! Hah!"
                    m "Pulling back this time, Seb slowed at his knot's widest point, leaving my spasming hole spread around his knot like a stretched rubber band. Gently, he pushed forward an achingly tiny amount, then pulled back that far on the other side of the equilibrium point."
                    m "I struggled to keep my ass steady as my upper body squirmed, slight pain spicing the pleasure as he fucked me with a width more than twice what he'd started."
                    m "Then with an outpouring of breath, he tugged me off his knot, pulling out fully until the condom reservoir popped clear of my rear."
                else:
                    m "As Sebastian began to tug back, I felt the bulge of flesh near his base sliding past my inner walls, then squeezed tightly by my outer lips."
                    m "I hissed, forced wide as he pulled the thick nodule through my tight hole. When the pressure abruptly released, my lower lips clasping around the far side, I gasped with relief."
                    m "Then Sebastian switched directions."
                    c "Mmh!"
                    m "The knot went in more easily than it came out, kissing my lips, then stretching all my folds taught until it was through, leaving Sebastian fully nestled inside me again."
                    m "Then he switched once more."
                    c "Ah! Hah!"
                    m "Pulling back this time, Seb slowed at his knot's widest point, leaving my spasming hole spread around his knot like a stretched rubber band. Gently, he pushed forward an achingly tiny amount, then pulled back that far on the other side of the equilibrium point."
                    m "I struggled to keep my hips steady as my upper body squirmed, slight pain spicing the pleasure as he fucked me with a width more than twice what he'd started."
                    m "Then with an outpouring of breath, he tugged me off his knot, pulling out fully until the condom reservoir popped clear of my canal."
                Br brow "That's it?"
                Br flirty "C'mon. I know you can knotfuck better than that."
                Sb drop "Not after that. I'm feeling {i}really{/i} sensitive right now."
            else:
                $ renpy.pause(1.2)
                m "After a few seconds, he began to pull out, still-hard length giving one last stimulating sendoff to my insides before he stepped back with a sigh."
        else:
            m "Then, abruptly, before I could get there, he jerked to a stop, a little ways short of hilting himself inside. Heat spurt into me, filling the condom reservoir at his tip."
            if persistent.bangok_inflation == True:
                if bangok_four_bryce3_store.sebtarget == "ass":
                    m "The load kept growing, pulse after pulse expanding the reservoir until it began to stretch down my colon, leaving me with a heady sense of fullness."
                else:
                    m "The load kept growing, pulse after pulse expanding the reservoir until it filled what little space remained in my passage after his shaft. I squirmed from the pressure on my innermost gate."
            m "He panted onto my back as his orgasm came to an end."
            $ renpy.pause(1.2)
            m "After a few seconds, he began to pull out, still-hard length giving one last stimulating sendoff to my insides before he stepped back with a sigh."
        Sb disapproval "I think I need to call it a night now. Take this off and get some rest."
        Sb smile "Thanks for that, [player_name]."
        m "Panting myself, I got back to hands and knees, feeling the echoes of Sebastian's warmth against my back fading into the cool night air."
        c "Sure."
        Br laugh "Alright. Have a good night, Sebastian. See you tomorrow."
        m "As Sebastian trudged off, I heard Bryce's plodding footsteps close in."
        if bangok_four_playerhasdick == True:
            $ bangok_four_bryce3_store.brycetarget = "ass"
        else:
            Br smirk "So, Seb's already gotten you a little ready there. Do you want me to take the same hole, or the other one?"
            menu:
                Br "Same hole? Or the other one?{fast}"
                "Same.":
                    $ bangok_four_bryce3_store.brycetarget = bangok_four_bryce3_store.sebtarget
                "Anal.":
                    $ bangok_four_bryce3_store.brycetarget = "ass"
                "Vaginal.":
                    $ bangok_four_bryce3_store.brycetarget = "vag"
                "Both.":
                    $ bangok_four_bryce3_store.sebastian_in = False
                    Br brow "Both? I don't know what you've heard or read, [player_name], but I was only born with the one."
                    c "I've changed my mind. Let's not make Maverick wait."
                    Mv nice "..."
                    Br flirty "Damn. I'm into it if you think you can take it."
                    jump bangok_four_bryce3_mcbottom_mav_bryce_mp
    else:
        m "Bryce trudged up, admiring my rear."
        if bangok_four_playerhasdick == True:
            $ bangok_four_bryce3_store.brycetarget = "ass"
        else:
            Br smirk "Looks like we've got a choice here."
            Br flirty "Front or back?"
            menu:
                Br "Front or back?{fast}"
                "Anal.":
                    $ bangok_four_bryce3_store.brycetarget = "ass"
                "Vaginal.":
                    $ bangok_four_bryce3_store.brycetarget = "vag"

    Br normal "Alright. Might have some trouble lining up in this position. Mind lending a hand?"
    m "Bryce stepped overtop me, thick legs planting down on either side of my arms. The hard segmented plates of his belly scraped over my spine, his internal warmth immediately flushing my back with heat."

    if bangok_four_bryce3_store.brycetarget == "ass":
        m "Wiping one of my hands off on my chest to rid it of grains of sand, I reached back for his length, guiding his tip up to my sphincter."
    else:
        m "Wiping one of my hands off on my chest to rid it of grains of sand, I reached back for his length, guiding his tip down to my cunt lips."

    if bangok_four_bryce3_store.brycetarget == bangok_four_bryce3_store.sebtarget:
        if bangok_four_bryce3_store.protection == True:
            m "My hole, already slightly parted from Sebastian's fucking, easily admitted the lukewarm, lubricated condom tip of Bryce's cock."
        else:
            m "My hole, already slightly parted from Sebastian's fucking, easily admitted the warm, lubricated tip of Bryce's cock. I shivered as I felt a few small beads of pre drip inside me."
    else:
        if bangok_four_bryce3_store.protection == True:
            m "The lukewarm, lubricated condom tip nestled in my hole, ensuring there would be no missing when he pushed."
        else:
            m "The warm, lubricated tip of Bryce's cock nestled in my hole, ensuring there would be no missing when he pushed."

    m "Bryce kneaded the sand with his claws, clearly eager, as I braced both hands back against the sand."
    Br smirk "Ready?"
    c "Y-Yeah."

    m "He didn't wait for me to fully finish my acknowledgment before easing slightly more weight onto his shaft, and by extension me."
    if bangok_four_bryce3_store.brycetarget == "ass":
        if (bangok_four_bryce3_store.sebastian_in == True) and (persistent.bangok_knot == True) and (bangok_four_bryce3_store.knotfuck == True):
            m "I took deep breaths and tried to relax my ass. Even still, Bryce's tip was slightly larger than Sebastian's knot had been, making him a challenge to take anally."
        else:
            m "I took deep breaths and tried to relax my ass. Even still, Bryce's tip was big, a challenge to take."
    else:
        m "I took deep breaths, inner walls shivering in anticipation as they waited for Bryce to spread me enough to pass my outer lips"
        
    m "I had to lean forward, all but planting my face in the sand, before Bryce wedged his tip inside."
    Br laugh "Ha! Damn!"
    Br flirty "Alright down there?"
    menu:
        "Mmmmh.":
            c "More than alright."
            Br smirk "Perfect."
        "Yes.":
            pass
        "Y-You're going to split me open!":
            Br stern "Wait, really?"
            c "Ngh. M-Maybe not that bad. But... give me a minute."
            Br brow "Of course."
            $ renpy.pause(1.0)
            m "I kept breathing deeply, sand grains scattering away from my mouth and nose in the moonlight."
            $ renpy.pause(1.0)
            c "That... that's starting to feel better."
        "Y-you feel bigger than last time!" if bangok_four_bryce1_unplayed == False:
            Br laugh "Being sober can do that to you!"
            Mv angry "..."
    $ renpy.pause(0.8)
    Br smirk "Mind if I start moving?"
    c "Go ahead. Slowly."
    Br laugh "What'd you think I was going to do? Start pounding?"

    m "Gently, Bryce applied more pressure, feeding more of his big dragon dick inside of me."

    if bangok_four_bryce3_store.brycetarget == "vag":
        m "As the pressure on my insides abruptly began to increase, I gasped."
        c "B-Bryce! Stop!"
        m "He obliged immediately, leaving my vagina stuffed with his cock, tip resting against my cervix!"
        Br brow "Is that what I think it is?"
        if persistent.bangok_cervpen:
            menu:
                "This is as deep as I go.":
                    label bangok_four_bryce3_mcbottom_train_bryce_nocervpen:
                    Br brow "Am I hurting you being this deep?"
                    c "You're up against my cervix. I don't--"
                    m "I squirmed, discomforted by the deep penetration."
                    c "If you could back off just a little..."
                    Br stern "Got it."
                "I want you in my womb.":
                    Br stern "You realize how dangerous that is, right?"
                    Br stern "Most women find that extremely painful."
                    if bangok_four_bryce1_unplayed == False and bangok_four_bryce1.fuckwomb == True:
                        Br brow "Last time, I think I only fit because we were drunk halfway out of our minds. I'm really not sure this time will be as easy or fun."
                    menu:
                        "I'm sure.":
                            $ bangok_four_bryce3_store.brycetarget = "womb"
                            Br brow "..."
                            $ renpy.pause (0.5)
                            Br smirk "If you insist."
                        "Maybe... maybe not.":
                            Br stern "Definitely not."
        else:
            c "This is as deep as I go."
            jump bangok_four_bryce3_mcbottom_train_bryce_nocervpen
    if bangok_four_bryce3_store.brycetarget == "womb":
        m "Gradually, Bryce applied more and more pressure to my innermost gate, opening me millimeter by millimeter."
        m "It was nigh impossible to keep from tensing up, the stress on my vagina rising to the point of feeling like it'd tear me in half."
        menu:
            "Take Bryce's hand.":
                m "Dropping my face into the sand, I gave up on holding myself up, instead reaching out to intertwine my fingers with the claws on one of Bryce's forepaws."
                m "I squeezed the cold keratin, feeling the warmth of his leg against my wrist."
                $ renpy.pause (0.8)
            "Breathe.":
                m "I lowered my face gently to the sand, protecting my nose and mouth as I struggled to get the absolute best-possible position."
                m "Every breath added yet more tension to my groin, but brought fresh air with which to focus on relaxing and letting Bryce through."
                $ renpy.pause (0.8)
            "Tough it out.":
                m "Gritting my teeth, I buried my face in my hands."
                m "I'd signed up for a dragon train and I was going to take every dragon, damnit!"
                m "I wondered if I would have been better off taking him in my ass, where there wouldn't be an inner gate to worry about."
                $ renpy.pause (0.3)
        m "Then he popped in like a dam bursting."

        menu:
            "Gasp.":
                pass
            "Moan.":
                pass
            # "Cry out.":
            #     Br stern "Damnit."
            #     m "He jerked back, pulling out of my womb, but it still took several seconds for me to even begin to recover."
            #     $ renpy.pause (1.5)
            #     c "T-Too deep."
            #     Br stern "I gathered."
            #     $ renpy.pause (0.8)
            #     Br brow "Will you be okay?"
            #     c "..."
            #     c "I think so."
            #     Br stern "Clearly we're not trying that again."

        m "He'd clearly pushed a little too far forward on his balance, as the rest of his shaft slid inside me in one long, electrifying, maddenning slide."
    elif bangok_four_bryce3_store.brycetarget == "ass":
        m "He slid smoothly now that he was in, the lube I'd applied earlier doing its job. His thick, meaty pillar filled out my hole."


    if bangok_four_bryce3_store.brycetarget in ["womb","ass"]:
        m "His groin molded my hindquarters, hard plates against soft, yielding flesh mating to form a tight seal."

    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycetarget in ["womb","ass"]:
        m "Hilted inside me, Bryce leaned down over my shoulder."
        if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
            Br smirk "You know, had a few drinks during that BBQ."
            Br flirty "Could use a leak like last time."
        elif persistent.bangok_watersports == True and bangok_four_bryce1_unplayed == False:
            Br brow "I know you weren't interested in taking it last time, but I've got a few drinks in me if you'd... want me to take a leak."
        else:
            Br smirk "You know, had a few drinks during that BBQ."
            Br flirty "I could do with taking a leak. If you'd want that inside you."
        Mv angry "Really, Bryce?"
        if bangok_four_bryce3_store.protection == True:
            Br laugh "What? I have a condom on!"
            Mv normal "I'm not sure I want sloppy seconds on your piss, whether it touched [player_name]'s insides or not."
        else:
            Mv normal "I'm not sure I want sloppy seconds on your piss."
        Br smirk "Not like you mind pissing on or in me every now and then."
        Br flirty "What do you say, [player_name]?"
        menu:
            "Sure.":
                $ bangok_four_bryce3_store.brycews = "before"
                Br smirk "If you say so."
            # "Can I get a shower instead?":
            #     $ bangok_four_bryce3_store.brycews = "shower"
            #     if bangok_four_bryce3_store.protection == True:
            #         Br smirk "Sure. But it'll have to wait until after I get the condom off."
            #     else:
            #         Br laugh "Right now? But I'm already so deep in you."
            #         Br smirk "How about I shower you off once we're done..."
            #         Br flirty "And for now we get to the fun part?"
            #     menu:
            #         "I can wait for that.":
            #             Br smirk "Sure."
            #         "I'll take it inside now, then.":
            #             $ bangok_four_bryce3_store.brycews = "before"
            #             Br flirty "Oh?"
            #             Br smirk "If you say so."
            "Please don't.":
                Br laugh "Okay, fine. I'll hold it."
                Br brow "Didn't need to go that bad anyway. Just had a feeling you'd be into it."

        if bangok_four_bryce3_store.brycews == "before":
            if bangok_four_bryce3_store.brycetarget == "ass":
                m "Bryce tugged back a little, shifting his feet as he found a more comfortable angle to piss in my upturned ass."
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "Then I felt his shaft twitch, and a liquid warmth began pooling in my colon."
                Br laugh "Ahhh..."
                if bangok_four_bryce3_store.protection == True:
                    m "The condom reservoir bloated, becoming a small balloon of piss as Bryce urinated into my guts."
                    if persistent.bangok_inflation == True:
                        m "It didn't stay small, pressing against my walls and beginning to work its way deeper as the flood kept coming."
                else:
                    m "My pipes drained his well, letting his stream of urine flow deeper inside me unimpeded, thanks to gravity and the angle I took him."
                    if persistent.bangok_inflation == True:
                        m "Even still the flood kept coming, the pool deepening inside me as gravity let it coalesce."
            elif bangok_four_bryce3_store.brycetarget == "vag":
                m "Bryce tugged back a little, shifting his feet as he found a more comfortable angle to piss in my passage."
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "Then I felt his shaft twitch, and a hot stream battered against my innermost gate. It packed the space remaining in my canal in a moment, then went the only direction it could."
            else: # "womb":
                m "Bryce tugged back a little, the feeling electric through my cervix. He shifted his feet, looking for a more comfortable angle to piss inside my most sacred temple."
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                if bangok_four_bryce3_store.protection == True:
                    m "Then I felt his shaft twitch, and a hot stream forced his condom's reservoir to expand deep inside me."
                else:
                    m "Then I felt his shaft twitch, and a hot stream battered my innermost center."

            if bangok_four_bryce3_store.brycetarget in ["vag","womb"]:
                Br laugh "Ahhh..."
                if bangok_four_bryce3_store.protection == True:
                    m "Using his condom inside me as his urinal, Bryce filled his piss balloon inside my womb."
                    if persistent.bangok_inflation == True:
                        m "It didn't stay small, pressing against my walls and forcing me to expand slightly around it."
                else:
                    m "Using me as a living urinal, Bryce defiled my womb with his piss, saturating my walls and deepest recesses."
                    if persistent.bangok_inflation == True:
                        m "The pool deepened inside me as gravity let it coalesce, pressing outward as the liquid pressure increased."
            stop soundloop fadeout 2.0
            m "After a few more seconds, Bryce's leak came to an end, leaving me comfortably warmed by his pissload."
            $ renpy.pause(0.8)
            Br flirty "Mmm. Now ready for more fun stuff?"
            if bangok_four_bryce3_store.protection == True:
                if bangok_four_bryce3_store.brycetarget == "womb":
                    m "He pulled back through my innermost gate, stretching the thin condom material between his shaft and his deposition of liquid gold."
                else:
                    m "He pulled back experimentally, stretching the thin condom material between his shaft and his deposition of liquid gold."
                if bangok_four_bryce3_store.brycetarget in ["vag","womb"]:
                    m "I gasped as it tugged, trying to pull through my cervix."
                Br brow "That'll be hard to keep from breaking."
                m "Then, heedless of his own warning, he kept pulling out."
    else:
        m "Bryce gave me a few seconds there, letting me adjust to his size."
        $ renpy.pause(2.0)

    play soundloop "fx/rub2.ogg" fadein 2.0
    show beachx:
        linear 0.15 zoom 1.01
        ease 0.5 zoom 1.0
        repeat
    with None
    m "Bryce began to thrust, gently at first, then with increasing need as I didn't voice any discomfort."
    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
        if bangok_four_bryce3_store.brycetarget == "ass":
            m "Each slam of Bryce's crotch into my hindquarters sent the liquid load inside me sloshing, heightening the experience."
        elif bangok_four_bryce3_store.brycetarget == "vag":
            m "He plunged in and out through my passage, thick shaft weakening my muscles. Piss leaked from my womb each time he pulled out, only to be forced back by his return, the repeated motion saturating my vaginal walls."
        else: # womb
            m "He plunged in and out of my womb, forcing my cervix wide with the repeated penetrations. Each time in he forced my womb to expand, cockhead displacing some of his piss and increasing the pressure on the walls of my defiled sacred place."
    else:
        if bangok_four_bryce3_store.brycetarget == "ass":
            m "My guts could barely take the punishment, shifting and pulling with his thrusts as his shaft molded me to his shape."
        elif bangok_four_bryce3_store.brycetarget == "vag":
            m "He plunged in and out through my passage, thick shaft weakening my muscles. Yet he took care not to impact my cervix at his deepest depth, leaving me with all the pleasure of every inch of his thrusts, and none of the pain of too-deep penetration."
        else: # "womb":
            m "He plunged in and out of my womb, forcing my cervix wide with the repeated penetrations. I swooned, lower body blank with pleasure from the experience."
    $ renpy.pause(1.2)
    Br laugh "Maverick, you're going to love this."
    Mv angry "I'm not going to enjoy fucking one of--"
    $ renpy.pause(0.5)
    Mv normal "..."
    $ renpy.pause(0.5)
    Br flirty "Don't be like that. You know [player_name] is doing this of their own free will."
    Br laugh "As if anyone could take this as part of some sort of evil plan."
    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
        Mv "Did you really have to piss inside?"
        Br pant "H-Hey. [player_name] wanted it."
        $ renpy.pause(0.5)
        Br pantflirt "[player_name] might... want yours too... if you need to go."
        Br flirty "What... do you say... [player_name]?"
        menu:
            "[[Moan.]":
                Br laugh "That's it!"
                Mv nice "..."
                $ bangok_four_bryce3_store.mavws = True
            "N-No.":
                Br brow "Oh? Damn, Mav. Rejected."
                $ bangok_four_bryce3_store.mavws = False
            "{i}Please{/i}.":
                Br flirty "I'm sure Maverick appreciates you asking nicely."
                Mv nice "..."
                $ bangok_four_bryce3_store.mavws = True
        if bangok_four_bryce3_store.brycetarget == "ass":
            m "Bryce let out a barking half laugh, then gasped as the vibrations translated directly to my ass, stimulating us both."
        else:
            m "Bryce let out a barking half laugh, then gasped as the vibrations translated directly to my cunt, stimulating us both."
    else:
        Mv angry "How can you rule that out?"
        Br stern "I'm in the middle... of something. Could we... not?"
        Mv angry "You asked me to leave the case out of tonight. Now you're bringing it up."
        m "Bryce's breathing came heavier as he approached his peak, despite the ongoing argument."
        Br brow "All I said... was you'd enjoy... fucking [player_name]."
        Br stern "Then you... almost... threw an... insult."
        Mv angry "Calling humans what they are is not an insult."
        Br stern "I... Mmmh..."
        m "Bryce hit the ground, kicking up a small cascade of sand next to my head."
    Br pantflirt "N-not long...!"

    $ renpy.pause(1.2)
    m "I could feel his thrusts get more uneven, more needy."
    m "That slight uncertainty was the last thing my endurance could take."
    show beachx:
        ease 0.5 zoom 1.0
    show black with fadequick
    if bangok_four_bryce3_store.brycetarget == "ass":
        if bangok_four_playerhasdick == True:
            play sound "fx/extinguish.ogg"
            m "As his cock slid over the pleasure button inside me once more, I clenched down and came, spurting ropes into the sand beneath me."
        else:
            m "As his cock bottomed out inside me once more, I clenched down and came, my empty cunt spasming and leaking."
    elif bangok_four_bryce3_store.brycetarget == "vag":
        m "As he plunged inside just short of my innermost gate yet again, I clenched down and came, squeezing with what tiny grip my muscles had left."
    else: # "womb":
        m "As his cock rammed deep into my womb once more, I clenched down and came, sparks of additional pleasure flying from my dilated cervix and my love passage used as sleeves for his pleasure."

    m "My orgasm was the last Bryce could take, too."
    stop soundloop fadeout 0.5
    play sound "fx/snarl.ogg"
    # This is gonna be painful. So many possibilities.
    if bangok_four_bryce3_store.brycetarget == "ass":
        if persistent.bangok_knot == True:
            m "Bryce stopped short of hilting me, length twitching as he pushed hot pulses into my ass."
        else:
            m "Bryce speared my ass, filling me with his meat before beginning to twitch and pulse."

        if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
            if bangok_four_bryce3_store.protection == True:
                m "His cum spilled into the already bloated condom reservoir, mixing with his piss."
                if persistent.bangok_inflation == True:
                    m "I moaned, jet after jet stretching the balloon of Bryce's fluids yet deeper inside me."
                    m "The pressure of his seed gave my guts no choice but to expand, distending my belly as he came deep inside."
            else:
                m "His cum spilled into his pool of piss within me, hot and heavy as it slid down my upturned body to the top of my colon."
                if persistent.bangok_inflation == True:
                    m "I moaned, jet after jet adding to the fluid gifts within me, forcing the rest deeper into my innards."
                    m "The pressure of his seed gave my guts no choice but to expand, distending my belly as he packed my insides white and gold."
        else:
            if bangok_four_bryce3_store.protection == True:
                m "His cum spilled into the condom, packing the reservoir in the tip with his load."
                if persistent.bangok_inflation == True:
                    m "I moaned as yet more jets came, forcing the reservoir to bloat and expand, stretching deeper into my innards."
                    m "The pressure of his seed gave my guts no choice but to expand, distending my belly as he came deep inside."
            else:
                m "His cum spilled into my guts, hot and heavy as it slid down my upturned body to the top of my colon."
                if persistent.bangok_inflation == True:
                    m "I moaned as yet more jets came, packing my colon before forcing his liquid load even deeper into my innards."
                    m "The pressure of his seed gave my guts no choice but to expand, distending my belly as he came deep inside."
    elif bangok_four_bryce3_store.brycetarget == "vag":
        m "Barely able to control his depth, Bryce kissed my cervix with his tip, then tugged back again to give room as he began to twitch and pulse thick ropes against my inner gate."

        if bangok_four_bryce3_store.protection == True:
            # No ws in vaginal-depth protected. Trying to remove cum-through-cervix-with-condom so...
            m "His cum spilled into the condom, packing the reservoir in the tip with his load."
            if persistent.bangok_inflation == True:
                m "I moaned as yet more jets came, forcing the reservoir to bloat and expand, until it pressed against every wall of my canal."
                m "He pulled back further, giving more room for his cum before the membrane's pressure against my cervix could cause me real pain."
                m "Even still, my vagina was forced to expand, every inner fold stretched flat and my belly pushed slightly out by the cumload."
        else:
            m "There was too much cum to stop. After packing the end of my vagina, it spurted through my cervix, hot and heavy as it defiled my sacred temple, saturating my walls and deepest recesses."
            if persistent.bangok_inflation == True:
                m "I moaned as the pulses continued, until my womb was out of room, packed solid with Bryce's seed."
                m "The pressure gave my womb no choice but to expand, distending my belly until I appeared slightly pregnant with nothing but his cum."
    else: # if bangok_four_bryce3_store.brycetarget == "womb"
        if persistent.bangok_knot == True: # avoiding knotting
            m "Bryce stopped short of hilting me, then began to twitch and pulse thick ropes directly into my womb."
        else: # no knotting risk
            m "Bryce speared my canal and cervix through, tip hanging deep inside my womb. Then he began to twitch and pulse thick, hot ropes directly inside."

        if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
            if bangok_four_bryce3_store.protection == True:
                m "His cum spilled into the already bloated condom reservoir, mixing with his piss."
                if persistent.bangok_inflation == True:
                    m "I moaned, my already distended womb forced to take yet more."
                    m "My belly expanded from the force exerted on my womb, leaving me pregnant with a balloon of cum and piss."
            else:
                m "His cum spilled into my saturated inner temple, layering over his piss to thoroughly defile my deepest center."
                if persistent.bangok_inflation == True:
                    m "I moaned, my already distended womb forced to take yet more."
                    m "My belly expanded from the force exerted on my womb, leaving me pregnant with cum and piss."
        else:
            if bangok_four_bryce3_store.protection == True:
                m "His cum spilled into the condom, packing the reservoir in the tip with his load."
                if persistent.bangok_inflation == True:
                    m "I moaned as yet more jets came, forcing the reservoir to bloat and expand, until it pressed against every wall of my womb."
                    m "The pressure of his seed gave my womb no choice but to expand, leaving me pregnant with a balloon of cum."
            else:
                m "His cum spilled unprotected into my innermost center, hot and heavy as it defiled my sacred temple, saturating my walls and deepest recesses."
                if persistent.bangok_inflation == True:
                    m "I moaned as the pulses continued, until my womb was out of room, packed solid with Bryce's seed."
                    m "The pressure gave my womb no choice but to expand, distending my belly until I appeared pregnant with nothing but his cum."
    $ renpy.pause(0.5)
    hide black with dissolveslow
    m "Bryce and I came down from our peaks together, breathing hard."

    if persistent.bangok_inflation == True:
        if bangok_four_playerhasdick == True:
            m "My bulging belly rubbed my cum into the sand as I struggled to catch my breath."
        else:
            m "My bulging belly rubbed against the sand beneath me as I struggled to catch my breath."

        Br laugh "D-Damn. Didn't know I could produce that much."
        $ renpy.pause(0.8)
        Br smirk "You ready for the pull-out?"

        menu:
            "C-Carefully!":
                $ bangok_four_bryce3_store.brycebroke = False
                Br normal "Of course."
            "{i}Please.{/i}":
                python in bangok_four_bryce3_store:
                    if protection:
                        brycebroke = True
            "[[Keep catching my breath.]":
                python in bangok_four_bryce3_store:
                    if protection:
                        brycebroke = True

        if bangok_four_bryce3_store.brycebroke == True:
            m "Bryce stepped back, tugging hard to pull his cock from inside me."
            if bangok_four_bryce3_store.brycetarget == "ass":
                m "I could feel that the large balloon stuffed with his fluids wasn't coming with him, instead stretching taut inside me."
                c "B-Bryce--!"
                play sound "fx/bubbles.ogg"
                if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                    m "The barrier broke, tearing open in an instant and exposing my guts to Bryce's slurry of cum and piss."
                else:
                    m "The barrier broke, tearing open in an instant and exposing my guts to Bryce's thick load of cum."
                c "Urp!"
                m "Without the added tension of the condom, the fluids shifted to equilibrium, flooding even deeper into my innards before settling in my distended belly."
            elif bangok_four_bryce3_store.brycetarget == "vag":
                $ bangok_four_bryce3_store.brycebroke = False
                m "I could feel that the large balloon stuffed with his fluids wasn't coming with him, held in place by my taut vaginal walls."
                c "B-Bryce--!"
                m "My inner walls let go at what felt like the last moment, his bloated condom reservoir pouring from my folds to smear my juices between my legs."
                jump bangok_four_bryce3_mcbottom_train_bryce_condom_pullout_success
            else: # "womb":
                m "I could feel that the large balloon stuffed with his fluids wasn't coming with him, instead stretching taught through my still-distended cervix."
                c "B-Bryce--!"
                play sound "fx/bubbles.ogg"
                if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                    m "The barrier broke, tearing open in an instant, defiling and saturating my innermost temple with Bryce's slurry of piss and cum."
                else:
                    m "The barrier broke, tearing open in an instant, defiling and saturating my innermost temple with Bryce's thick load of cum."
                c "Urp!"
                m "Without the added tension of the condom, the fluids shifted to equilibrium, reaching into my deepest recesses and pouring out my widened cervix, until it met the barrier of Bryce's cockhead."
            Br sad "Oh. Fuck. {w=0.5}I forgot we had that on."
            menu:
                "You fucking idiot!":
                    Br stern "It was an accident, okay?"
                    c "How is it okay? I asked you to use protection!"
                    Br brow "Well we can't exactly undo it now. You might as well finish the night."
                    c "..."
                "Ohhh...":
                    c "That felt... that felt good."
                    Br flirty "It did?"
                    Br laugh "Did you set that up on purpose? 'Cause that gave me a serious fright!"
                    Br flirty "Want Maverick to do the same thing?"
                    c "M-Maybe."
        elif bangok_four_bryce3_store.protection == True:
            m "Bryce began to pull out, then clearly felt what I did: his balloon of fluids wasn't coming back with him."
            c "T-Take it slowly."
            Br stern "Trying."
            if bangok_four_bryce3_store.brycetarget == "ass":
                m "I pushed myself up against Bryce's belly to make the journey flat, then clenched what inner muscles I still could, working the condom's reservoir back, while Bryce used small amounts of tension to accomplish the same thing."
                m "Eventually his cockhead pulled through my sphincter."
                play sound "fx/pour.ogg" fadein 0.5
                m "Then the bloated reservoir followed, spilling between my legs onto the sand in one big blob."
            elif bangok_four_bryce3_store.brycetarget == "vag":
                m "I pushed myself up against Bryce's belly to make the journey flat, then clenched what inner muscles I still could."
                play sound "fx/pour.ogg" fadein 0.5
                m "It was gravity that did the work, though. Bryce's load slowly poured into the part of the condom Bryce gradually pulled out of my snatch."
                m "The bloated reservoir itself followed, spilling between my legs onto the sand in one big blob."
            else: # "womb":
                m "I pushed myself up against Bryce's belly to make the journey flat, then clenched what inner muscles I still could."
                play sound "fx/pour.ogg" fadein 0.5
                m "It was gravity that did the work, though. Bryce's load poured through my innermost gate, until the remaining blob could pop through and join the rest spilling between my legs on the sand in one big blob."
            label bangok_four_bryce3_mcbottom_train_bryce_condom_pullout_success:
            stop sound fadeout 1.0
            m "I slumped back down as it spilled clear, too exhausted and empty to move."
        
        if (bangok_four_bryce3_store.protection == False) or (bangok_four_bryce3_store.brycebroke == True):
            if bangok_four_bryce3_store.brycetarget == "vag":
                m "Bryce pulled out all the way, my tight cervix keeping most of his load packed deep within me, but for a slow dribble out into my cunt."
            else:
                if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                    m "Bryce pulled out all the way, a small fountain of cum and piss briefly splattering his cock and running down my thighs as the pressure on my innards equalized a little with the outside air through my gaping hole."
                else:
                    m "Bryce pulled out all the way, a small fountain of cum briefly running down my thighs as the pressure on my innards equalized a little with the outside air through my gaping hole."
    else:
        Br laugh "D-Damn. Thanks for that."
        if bangok_four_bryce3_store.protection == True:
            m "Stepping back, Bryce pulled out, his condom's reservoir of cum popping free with him to leave me gaping and achingly empty."
        else:
            m "Stepping back, Bryce pulled out. I sighed, achingly empty but for the mess he'd left behind, but warm in the knowledge another cock was coming soon."

    Br smirk "Maverick?"
    $ renpy.pause(1.2)
    m "Bryce retreated a few more steps, but I didn't hear Maverick's footsteps approaching."
    m "I wiggled my rear slightly, trying to entice him to finish off the night."

    Mv normal "..."
    m "Slowly, I felt his presence arrive. He stepped over me carefully, as if afraid my naked, used body might be concealing a weapon I'd use against him."
    $ bangok_four_bryce3_store.mavtarget = bangok_four_bryce3_store.brycetarget
    if bangok_four_bryce3_store.mavtarget == "ass":
        m "Then his claws dug into the sand to either side of my head, and I felt his tip at my ass."
        m "His cockhead flared wider than Bryce's! At first I worried there was no way for it to fit, until he began to apply pressure and I felt his head compress slightly to nestle just inside my stretched hole."
    else:
        m "Then his claws dug into the sand to either side of my head, and I felt his tip at my lower lips."
        m "His cockhead flared wider than Bryce's! At first I worried there was no way for it to fit, until he began to apply pressure and I felt his head compress slightly to nestle just inside my parted and stretched outer folds."

    menu:
        "This-- Y-You're too big. I can't...":
            Br stern "Damnit. Maverick--"
            m "Maverick pulled out immediately, stepping away and leaving me to slump onto the ground."
            scene beachx at Pan ((300, 0), (300, 0), 0.0) with hpunch
            jump bangok_four_bryce3_mcbottom_train_bryce_takeover_mav_turn
        "H-Hah! Oh, this'll be fun.":
            jump bangok_four_bryce3_mcbottom_train_mav_turn

label bangok_four_bryce3_mcbottom_train_bryce_takeover_mav_turn:
    show bryce brow at right with dissolve
    Br "I'll take over. You going to be okay, [player_name]?"
    c "Y-Yeah. I-I think I will now."
    show maverick nice flip at left with dissolve
    Mv "I did not intend you any harm."
    c "I-I know. You're just... big."
    Br smirk "Well, relax. I'm big enough to handle big."
    show bryce smirk flip with dissolve
    m "Bryce wandered a few steps away, then lifted his tail to expose his hindquarters."
    if bangok_four_bryce3_store.protection == True:
        m "After one more almost apologetic look back at me, Maverick tugged his condom off with a claw, then moved over to Bryce."
    else:
        m "After one more almost apologetic look back at me, Maverick moved over to Bryce."
    show maverick nice flip at center behind bryce with ease
    jump bangok_four_bryce3_mcbottom_train_bryce_takeover_mavgoes_merge

label bangok_four_bryce3_mcbottom_train_mav_turn:
    m "He pressed forward, spreading me open wider than Bryce had. Then he stopped, once his whole cockhead was in."
    Mv nice "Is this at all painful?"
    m "After Bryce's fucking, just being spread around a thick shaft was a non-issue. I shook my head."
    c "F-Feels good."
    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
        if bangok_four_bryce3_store.mavws == False:
            Br smirk "You know, [player_name], Maverick does this whole piss thing for me all the time."
            Br flirty "You sure you don't want his too?"

            Mv angry "It's not \"all the time.\""
            Mv nice "I know Bryce can be pushy with his..."
            Mv normal "fetish."
        else:
            $ renpy.pause(0.8)
        Mv nice "Do you actually want me to urinate in you?"

        menu:
            "Accept.":
                $ bangok_four_bryce3_store.mavws = True
                Mv nice "In that case..."
            "Reject.":
                $ bangok_four_bryce3_store.mavws = False
                Mv angry "I keep telling you, Bryce, to cut back on pushing that."
                Br brow "Look, more people than you expect are into it around here."
                Br flirty "Maybe [player_name] just likes mine."

        if bangok_four_bryce3_store.mavws == True:
            m "Arranging his feet, Maverick pushed a small distance deeper."
            play soundloop "fx/faucet1.ogg" fadein 0.5
            queue soundloop "fx/faucet2.ogg"
            if bangok_four_bryce3_store.protection == True and bangok_four_bryce3_store.brycebroke == True:
                if bangok_four_bryce3_store.mavtarget == "ass":
                    m "Then his cock twitched and a hot balloon of fresh piss took shape, bloating in my rectum just beyond his tip."
                    if persistent.bangok_inflation == True:
                        m "I moaned, feeling the piss stretching the condom's reservoir out deeper into my ass, pushing back against Bryce's load."
                else:
                    m "Then his cock twitched and a hot balloon of fresh piss took shape, bloating in my canal just beyond his tip."
                    if persistent.bangok_inflation == True:
                        m "I moaned, feeling the piss stretching the condom's reservoir to fill my vagina, stuffing me with a length made of pure piss, pushing back against Bryce's load within my womb."

            elif bangok_four_bryce3_store.protection == True:
                if bangok_four_bryce3_store.mavtarget == "ass":
                    m "Then his cock twitched and a hot balloon of fresh piss took shape, bloating in my rectum just beyond his tip."
                else:
                    m "Then his cock twitched and a hot ballon of fresh piss took shape, bloating in my canal just beyond his tip."

                if persistent.bangok_inflation == True and bangok_four_bryce3_store.brycebroke == False:
                    m "I moaned as I felt my belly pressed out a little yet again, stretched once more from empty by the fluid of a different dragon."
            else:
                m "Then his cock twitched and a hot stream of fresh piss flooded my insides."
                if persistent.bangok_inflation == True:
                    m "I moaned as I felt my belly grow still further, the fresh urine pouring in stretching me even larger than before."
            stop soundloop fadeout 0.5
            m "Maverick finished in me faster than Bryce had. Even still, I writhed in ecstacy, the pressure feeling like he'd pissed even more than Bryce had."
            m "I had to wonder at how lucky I was, travelling to another world to get to serve as a urinal for these magnificent beasts."
            Mv nice "Satisfied?"
            m "I nodded languidly, his hot urine suffusing my whole body with warmth."


    m "Maverick arranged his feet, stepping forward. Then he pressed in, sheathing inch after inch of cock within me."
    if persistent.bangok_watersports == True and bangok_four_bryce3_store.mavws == True and bangok_four_bryce3_store.protection == True:
        m "At the third inch, I realized the deeper tugging I was feeling wasn't his cockhead, but was actually his condom's reservoir."
        m "Fluid pressure held it taught against my walls, but his cock was forcing the fluid inside deeper and stretching the thin tip even thinner!"
        c "Mav--!"
        play sound "fx/bubbles.ogg"
        $ bangok_four_bryce3_store.mavbroke = True
        if bangok_four_bryce3_store.mavtarget == "ass":
            m "Hot piss poured out of the split tip, forced immediately deeper into my intestines to escape Maverick's encroaching head."
        else:
            m "Hot piss poured out of the split tip, suffusing my vaginal walls as it flowed with gravity to pool at the end of my canal."

        if bangok_four_bryce3_store.brycebroke == False:
            Mv scared "..."
            menu:
                "You idiot!":
                    Br stern "What happened?"
                    Br brow "Oh. Did it break?"
                    c "Yes it broke!"
                    m "Maverick hurriedly pulled out completely. The torn end of the condom left dribbling golden trails down my thighs."
                    Br normal "Oh. Oh well. That could honestly be a lot worse."
                    c "Worse? I asked you two to use protection!"
                    Mv angry "You then asked us to risk it. These clearly aren't designed with urination in mind."
                    c "How is it my fault that--"
                    m "I turned to try to look back at Maverick, but slumped to the ground, my abused lower body protesting at the suggestion of movement."
                    scene beachx at Pan ((300, 0), (300, 0), 0.0) with hpunch
                    show bryce normal at right with dissolve
                    Br "[player_name], just calm down. It was an accident. I'll take over bottoming, okay?"
                    c "..."
                    show bryce smirk flip with dissolve
                    m "Bryce wandered a few steps away, then lifted his tail to expose his hindquarters."
                    m "After one more irritated look back at me, Maverick pulled off the remains of his condom with a claw, then moved over to Bryce."
                    show maverick normal flip at center behind bryce with dissolve
                    jump bangok_four_bryce3_mcbottom_train_bryce_takeover_mavgoes_merge
                "Ohhh...":
                    c "That felt... that felt good."
                    Br brow "What? What did?"
                    Mv scared "The condom broke."
                    Br smirk "Oh?"
                    Br laugh "Damn. So you actually got to piss inside, huh?"
                    Br smirk "Well, it looks like [player_name] is happy with it."
                    Br normal "I guess you should keep going."
        else:
            Br brow "..."
            Br laugh "Man. I really have to not buy that brand again."
            menu:
                "Are you kidding me?":
                    Mv angry "You asked us to engage in risky behaviour pissing in it."
                    Br normal "Condoms aren't really designed for it. It's a little on you, [player_name]."
                    $ renpy.pause(0.8)
                    c "Fine."
                "[[Moan.]":
                    Br smirk "Well, it looks like [player_name] is happy with it."
                    Br normal "I guess you should keep going."


        m "After a few moments hesitation, Maverick resumed pushing."

    if bangok_four_bryce3_store.mavtarget in ["vag","womb"]:
        m "His large head spread my inner walls, feeling almost like a fist as it pushed deeper. It flattened out my inner folds, stretching my muscles and scraping deeper every drop of fluid within me."
        if bangok_four_bryce3_store.mavtarget == "vag" or not persistent.bangok_cervpen:
            m "I gasped, crotch already afire with overstimulation as he kissed my cervix with his tip."
        else: # "womb":
            m "I gasped, crotch already afire with overstimulation as he kissed my dilated cervix with his tip."
            Mv nice "As deep as Bryce went?"
            menu:
                "All the way.":
                    Mv nice "..."
                "I-I don't think I can take you there.":
                    $ bangok_four_bryce3_store.mavtarget = "vag"
                    Mv normal "Then we won't test it."

        if bangok_four_bryce3_store.mavtarget == "womb":
            if persistent.bangok_inflation == True:
                m "I shuddered as Maverick pressed harder into my innermost gate, forcing back through it the pool of fluids that had escaped from, and bulging my belly back to where it had been when Bryce first came."
            m "He leaned, my dilated cervix still not wide enough to take his head."
            show black with fadequick
            if persistent.bangok_inflation == True:
                m "Then he slipped through, displacing one thick shaft's cockhead worth of Bryce's load."
                m "I blasted over my peak, stimulated both by my innermost gate bending yet wider, and the forced pressure on my inner walls, leaving my belly bigger than ever before."
                $ renpy.pause(1.0)
            else:
                if bangok_four_bryce3_store.protection and (not bangok_four_bryce3_store.brycebroke) and (not bangok_four_bryce3_store.mavbroke) :
                    m "Then he slipped through, sinking fully into my womb."
                else:
                    m "Then he slipped through, sinking fully into my defiled womb."
                m "I came again, the fresh popping of my cervix more than my mind was prepared to handle."
                $ renpy.pause(1.0)
            hide black with dissolveslow
            $ renpy.pause(0.5)
            m "Maverick waited, patiently, for me to come back down."
            $ renpy.pause(0.5)
            m "Just when my breathing began to even out again, Maverick resumed pushing in his last couple inches."
            m "The hard plates of his underbelly met my back as he hilted inside, stuffing me more completely than ever before with thick, hard cock."
    else:
        m "His large head spread my inner walls, feeling almost like a fist as it pushed deeper. It pressed outward on my colon, stretching my muscles and scraping deeper every drop of Bryce's fluids."
        m "I didn't even consciously register wriggling to take the deep penetration, as I was so lost in the sensation of the wide stretch."
        m "The hard plates of his underbelly met my back as he hilted inside, stuffing me more completely than ever before with thick, hard cock."

    $ renpy.pause(0.8)
    Mv nice "How are you feeling with this depth?"
    menu:
        "Incredible.":
            Mv normal "..."
        "So full...":
            Mv normal "..."
            Mv nice "I'll try to avoid going this deep, then."
            c "N-No! Please."
            Mv normal "If this is your limit, I need to know. I can start to get... rough once I get going."
            c "I'll be fine."
            $ renpy.pause(0.8)
            Mv "..."
        "I can't. I-I can't.":
            m "I could tell from his size and force that this {i}wasn't{/i} going to be the good time I had thought it would be. I repeated the two words like a mantra, praying it wasn't too late to back out."
            Br stern "Maverick."
            m "Maverick put a paw on my shoulder, sand and scales digging into my back as held me against the surface of the beach."
            if persistent.bangok_inflation == True and ((not bangok_four_bryce3_store.protection) or bangok_four_bryce3_store.brycebroke or bangok_four_bryce3_store.mavbroke):
                m "Then he dragged back, long and slow, my insides gurgling as fluid flowed and shifted to follow him. His head popped free with a wet spatter down my legs."
            else:
                m "Then he dragged back, long and slow. His head popping out sent a wave of relaxation through my innards, as my hole spasmed against the cool night air."

            # Using mavbroke to indicate maverick has pissed inside so I don't have to think about yet another variable
            $ bangok_four_bryce3_store.mavbroke = True
            m "Finally, he lifted his paw from my shoulderblades, releasing me from my service to his cock. I gasped as I slumped to the ground, thanking my lucky stars I'd avoided that internal organ rearrangement."
            scene beachx at Pan ((300, 0), (300, 0), 0.0) with hpunch
            jump bangok_four_bryce3_mcbottom_train_bryce_takeover_mav_turn
    Br laugh "Any time you want to start."
    $ renpy.pause(0.8)
    m "Maverick put one paw on my shoulder, sand and scales digging into my back as he held me against the surface of the beach."
    if persistent.bangok_inflation == True and ((not bangok_four_bryce3_store.protection) or bangok_four_bryce3_store.brycebroke or bangok_four_bryce3_store.mavbroke):
        m "Then he dragged back, long and slow, my insides gurgling as fluid flowed and shifted to follow him. He stopped when the ridge of skin around his head tugged at my hole, just a bit of force from popping out."
        if (not bangok_four_bryce3_store.protection) or bangok_four_bryce3_store.brycebroke:
            m "He thrust back in, harder, shoving Bryce's load deep inside me as he molded me to his shape."
        elif persistent.bangok_watersports == True and bangok_four_bryce3_store.mavbroke == True:
            m "He thrust back in, harder, shoving his pissload deep inside me as he molded me to his shape."
        else:
            m "He thrust back in, harder, molding me to his shape by force."

        if bangok_four_bryce3_store.mavtarget == "vag":
            m "I was almost disappointed when he had to stop to avoid breaching my womb, wishing I could sink his entire shaft inside of me."
        elif bangok_four_bryce3_store.mavtarget == "womb":
            m "He didn't slow down for my cervix this time, breaching my womb like a battering ram before hilting."
            m "I could feel my uterus bulge out, a month or two of pregnancy growth passing in a second-long thrust as I was forced to expand."
        else:
            m "He didn't slow as my guts gurgled, fluid rammed even deeper inside me."
            m "I could feel my belly bulge out, a half dozen full meals of weight stuffed deep in my gut in a second-long thrust as I was forced to expand."
    else:
        m "Then he dragged back, long and slow, until the the ridge of skin around his head tugged at my hole, just a bit of force from popping out."
        m "He thrust back in, harder, molding me to his shape by force."

    m "I had thought his thrust had been a one time test, a bit of stimulation and stretching before a longer, slower fuck."
    m "The next thrust went the same distance, but faster."
    play soundloop "fx/rub2.ogg"
    show beachx:
        linear 0.15 zoom 1.02
        ease 0.5 zoom 1.0
        repeat
    with None
    c "Ah!"
    m "Held in place by Maverick's paw, I could do nothing but hold on to consciousness through Maverick's rough fucking, as the sensations rapidly threatened me with climax after climax."

    if bangok_four_bryce3_store.mavtarget == "vag":
        m "Trying to avoid kissing my cervix, Maverick pulled completely out more than once, wide head blasting through my outer folds harder than I could deal with."
    elif bangok_four_bryce3_store.mavtarget == "womb":
        m "The muscles in my love passage gave up, falling limp and pliable as Maverick treated my hole like a sleeve to get to my cervix. That he popped through again, bottoming out so hard I worried he was kissing the far end of my womb."
    else:
        m "My sphincter gave up, stretched wide enough by Maverick's abuse to simply remain that way as, more than once, Maverick pulled the ring of his tip out before plunging back inside to his hilt."

    if (bangok_four_bryce3_store.mavtarget in ["womb", "ass"]) and ((not bangok_four_bryce3_store.protection) or bangok_four_bryce3_store.brycebroke or bangok_four_bryce3_store.mavbroke):
        m "Some of the fluid that had been deposited inside me spattered out as we fucked, scooped out by Maverick's head or sprayed out by his rough inward thrusts."

    if bangok_four_playerhasdick == False:
        show black with fadequick
        m "I flew over yet another peak, arms dropping limp with my head lying on the sand as Maverick held me in place to ram me."
        $ renpy.pause(1.0)
        hide black with dissolveslow
        $ renpy.pause(0.5)
        m "I came back down into exactly the same situation, my body stuffed and mind fractured. But I had no more orgasms left to give, as the rough sensations overstimulated me into just mindless swooning."
    else:
        m "I writhed under Maverick's paw, his rough ramming punching past my pleasure button, even though I was all tapped out."
        m "The intense overstimulation left me swooning."

    $ renpy.pause(1.2)

    stop soundloop fadeout 0.5
    show beachx:
        linear 0.15 zoom 1.0
    with None
    play sound "fx/rub1.ogg"

    if bangok_four_bryce3_store.mavtarget == "ass":
        m "Finally, Maverick stopped, abruptly, halfway into me. Then his hips bucked, fucking my asshole fast and shallow with a few more short thrusts."
        play sound "fx/dragonpain.ogg"
        $ renpy.pause(1.0)
        if bangok_four_bryce3_store.protection and not bangok_four_bryce3_store.mavbroke:
            m "Cock twitching, Maverick stopped shallow in my ass, then began to spurt thick, hot seed into his condom."
        else:
            m "Cock twitching, Maverick stopped shallow in my ass, then began to spurt thick, hot jets of seed into my guts."

        if persistent.bangok_knot == True:
            m "Just a few spurts into his orgasm he pushed, pressing forward and jamming his seed deeper into me until a huge bulge at his base stopped him."
            m "Shoving me a little in the sand, Maverick pressed his knot up against my rear, barely able to wedge it between my cheeks, much less fit it inside me."
        else:
            m "Just a few spurts into his orgasm he pushed, pressing forward and jamming his seed deeper into me until his slit pressed against my wide sphincter, feeding every bit of his cockflesh inside me."

        if persistent.bangok_inflation == True:
            if (not bangok_four_bryce3_store.protection) or bangok_four_bryce3_store.brycebroke:
                if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                    m "The massive shaft in my ass was the only plug tight enough to deal with the fluid pressure inside me as Maverick's cum continued to spill into me."
                    m "With my intestines packed with cum and piss, I began to feel the sensations flood even deeper, spilling from my guts into my stomach."
                    m "I burped as I was packed solid from stem to stern, my belly left bloated as nothing but these dragons' toilet for urine and seed."
                else:
                    if (not bangok_four_bryce3_store.protection) or bangok_four_bryce3_store.mavbroke:
                        m "The massive shaft in my ass plugged Maverick's seed in, forcing it to flood into Bryce's thick cream filling."
                        m "My intestines gurgled as they were packed solid, my belly left bloated as nothing but these dragons' cum tank."
                    else:
                        m "The massive shaft in my ass plugged Bryce's seed in as Maverick's condom tip ballooned outward into it."
                        m "My intestines gurgled as Bryce's load flowed around the balloon of Maverick's seed, until I was packed solid, my belly left bloated as a pressurized tank of Bryce's cum."
            else: # Bryce protected, so protection==True 
                if persistent.bangok_watersports == True and bangok_four_bryce3_store.mavws == True:
                    # mavbroke must be true
                    m "The massive shaft in my ass plugged Maverick's piss and cum in, forcing the hot load far into my intestines as still more pulses jetted from his tip."
                    m "I felt bloated and full, my guts nothing but Maverick's toilet for urine and seed."
                else:
                    # mavbroke must be false, no ws, so must just be condom of cum
                    m "His condom tip ballooned deep inside my guts, pulse after pulse of hot seed forcing it to expand deeper, to find more space within me as more cum forced its way in behind."
            m "Heady warmth suffused my every organ as Maverick's pulses came to an end, leaving my muscles totally limp."
        else:
            jump todo_out_of_content_bangok_four_bryce3
    elif bangok_four_bryce3_store.mavtarget == "vag":
        m "Finally, Maverick stopped, abruptly, halfway down my canal. Then his hips bucked, fucking my pussy fast and shallow with a few more short thrusts."
        play sound "fx/dragonpain.ogg"
        $ renpy.pause(1.0)
        if bangok_four_bryce3_store.protection:
            # Mavbroke is impossible on this route because no ws in vaginal-depth.
            m "Cock twitching, Maverick stopped short just an inch past his head inside my pussy, then began to spurt thick, hot seed into his condom."
        else:
            m "Cock twitching, Maverick stopped just an inch past his head inside my pussy, then began to paint my inner walls white with thick, hot jets of seed."

        m "He groaned as he held his place, legs shuddering as he kept himself from continuing to fuck me, and risk punching his load into my delicate cervix with his cock's size and volume."

        if bangok_four_bryce3_store.protection:
            m "As his condom reservoir bloated he yanked himself, then it out of me."
            m "My juices ran down my legs, rubbed in by his shaft and the condom tip as both twitched and bobbed between my thighs."
        else:
            m "His reticence to move did nothing to stop his spurts of cum. My lower body swam in and out of electric sparks of sensation, tossed about on the tide of Maverick's pulses against my innermost gate."
            if persistent.bangok_inflation == True:
                m "My already filled and defiled womb bloated further, helpless to provide any other escape for the twin dragonloads within me while my canal remained plugged by Maverick's massive shaft."
                m "My pregnancy of cum advanced, belly bulging, leaving me thoroughly bred by my two draconic companions."
    else:
        m "Finally, Maverick stopped, abruptly, just short of my cervix. Then his hips bucked, fucking my womb fast and shallow with a few more short thrusts."
        play sound "fx/dragonpain.ogg"
        $ renpy.pause(1.0)
        if bangok_four_bryce3_store.protection and not bangok_four_bryce3_store.mavbroke:
            m "Cock twitching, Maverick stopped again with his head punched through my cervix, then began to spurt thick, hot seed into his condom."
        else:
            m "Cock twitching, Maverick stopped again with his head punched through my cervix, then began to spurt thick, hot jets of seed into my womb."

        if persistent.bangok_knot == True:
            m "Just a few spurts into his orgasm he pushed, pressing forward and spreading my cervix and canal wider around him until a huge bulge at his base stopped his entry."
            m "Shoving me a little in the sand, Maverick pressed his knot up against my lips, barely able to wedge it between my thighs, much less fit it inside me."
        else:
            m "Just a few spurts into his orgasm he pushed, pressing forward and spreading my cervix and canal wider around him until his slit pressed against my stretched lips, feeding every bit of his cockflesh inside me."

        if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
            if ((bangok_four_bryce3_store.protection == False) or (bangok_four_bryce3_store.brycebroke == True and bangok_four_bryce3_store.mavbroke == True)):
                # Bryce and Maverick unprotected
                if persistent.bangok_inflation == True:
                    m "My already filled and defiled womb distended further, helpless to provide any other escape for the slurry of cum and piss within me while my canal remained plugged by Maverick's massive shaft."
                    m "My pregnancy of cum advanced, belly bulging, leaving my deepest recesses bloated as nothing but these dragons' toilet for urine and seed."
                else:
                    m "Maverick's cum layered over the slurry of seed and urine that already defiled my deepest recesses, mixing and flowing together into a thick painting of wanton lust on my innermost walls."
            elif bangok_four_bryce3_store.mavws == False:
                # Bryce broke, Maverick protected.
                if persistent.bangok_inflation == True:
                    m "My already filled and defiled womb bloated further as Maverick's cum balloon filled inside."
                    m "I was helpless to give Bryce's slurry of cum and piss within me any other escape while my canal remained plugged by Maverick's massive shaft."
                    m "My pregnancy of fluids advanced, belly bulging, leaving my deepest recesses bloated as nothing but a toilet for Bryce's urine and seed, pressurized by Maverick's reservoir of cum."
                else:
                    m "Maverick's cum balloon rested on Bryce's slurry of seed and urine that already defiled my deepest recesses, a wobbling, fluid-filled statue of moderation atop the painting of wanton lust on my innermost walls."
            else:
                # Bryce protected, Maverick not.
                m "Maverick's cum jetted into my saturated inner temple, layering over his piss to thoroughly defile my deepest center."
                if persistent.bangok_inflation == True:
                    m "My womb, already distended by his massive shaft and urine, was forced to expand further around his seed."
                    m "My belly visibly bloated, pregnant with cum and piss as Maverick used my deepest recesses as nothing but a toilet for his fluids." 
        else:
            if bangok_four_bryce3_store.protection == False:
                # Unprotected 2nd load
                if persistent.bangok_inflation == True:
                    m "My already filled and defiled womb distended further, helpless to provide any other escape for the mix of two dragons' seed within me while my canal remained plugged by Maverick's massive shaft."
                    m "My pregnancy of seed advanced, belly bulging, leaving my deepest recesses bloated as nothing but these dragons' cum tank."
                else:
                    m "Maverick's cum layered over Bryce's white ropes within my deepest recesses, mixing and flowing together into a thick painting of wanton lust on my innermost walls."
            elif bangok_four_bryce3_store.brycebroke == True:
                # Bryce broke, Maverick protected
                if persistent.bangok_inflation == True:
                    m "My already expanded and defiled womb bloated further as Maverick's cum balloon filled inside."
                    m "I was helpless to give Bryce's packed load within me any other escape while my canal remained plugged by Maverick's massive shaft."
                    m "My pregnancy of seed advanced, belly bulging, leaving my deepest recesses bloated as nothing but a tank of Bryce's seed, pressurized by Maverick's reservoir of cum."
                else:
                    m "Maverick's cum balloon rested on Bryce's white ropes of seed that already defiled my deepest recesses, a wobbling, fluid-filled statue of moderation atop the painting of wanton lust on my innermost walls."
            else:
                # Bryce protected, Maverick protected
                if persistent.bangok_inflation == True:
                    m "Like Bryce before him, Maverick continued to twitch and pulse, inflating his condom's reservoir like a balloon within the tight confines of my womb."
                    m "My belly bulged, cum pressing me outward until once again I appeared bred, this time by Maverick's reservoir of seed."
                else:
                    m "I felt every twitch and jet as Maverick spilled into his condom, his tip hilted in my womb as he used my anatomy to satisfy his needs."
    $ renpy.pause (0.5)
    play sound "fx/breathing.ogg" fadein 0.5
    $ renpy.pause (1.0)
    m "As Maverick came down from his peak, his breathing was hot and wet above me."
    if bangok_four_bryce3_store.mavtarget == "vag" and bangok_four_bryce3_store.protection == True:
        m "Finally, he lifted his paw from my shoulderblades, releasing me from my service to his cock."
        Br stern "..."
        Br brow "[player_name]? Are you okay?"
        menu:
            "{i}Amazing...{/i}":
                Br flirty "Damn you're kinky."
            "[[Moan.]":
                Br flirty "Damn you're kinky."
            "E-Everything hurts.":
                Br stern "I think I can see that."
    else:
        m "Finally, he lifted his paw from my shoulderblades, releasing me from my service to his cock, even if it was still buried deep within my body."
        Br stern "..."
        Br brow "[player_name]? Are you okay?"
        menu:
            "{i}Amazing...{/i}":
                Br flirty "Damn you're kinky."
            "[[Moan.]":
                Br flirty "Damn you're kinky."
            "E-Everything hurts.":
                Br stern "I think I can see that."
                Br brow "Maverick? Pull out. Gently."
            "P-Please get him o-out of me.":
                Br stern "Maverick!"
                Mv angry "Fine."
        m "Lifting me from the sand to straighten his shaft's journey, Maverick began gently pulling out."
        if bangok_four_bryce3_store.mavtarget == "ass":
            if persistent.bangok_inflation == True:
                if bangok_four_bryce3_store.protection == False or bangok_four_bryce3_store.mavbroke == True:
                    # Maverick unprotected
                    play sound "fx/spray.ogg"
                    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                        m "When his head tugged through my asshole it gaped, letting a river of cum and piss pour from inside me onto the sand."
                    else:
                        m "When his head tugged through my asshole it gaped, letting a river of cum pour from inside me onto the sand."
                else:
                    # Maverick protected
                    if bangok_four_bryce3_store.brycebroke == True:
                        m "Bryce's fluids, still coating my intestines, lubricated Maverick's condom as it tugged after his shaft though my insides."
                        m "My asshole gaped behind Maverick's tip, making it easy for the bloated reservoir to pour out between my legs."
                        play sound "fx/spray.ogg"
                        m "Abruptly, the last of the condom spilled out of me, followed by a splatter of Bryce's leavings following it out of my hole."
                    else:
                        m "The bloated condom's reservoir stuck, the fluid pressure against my guts too much for it to slide out with Maverick's cock."
                        Mv normal "You need to push as well."
                        menu:
                            "J-Just tear it.":
                                Mv normal "You are sure?"
                                m "I nodded, knowing that after the rough fucking I wouldn't be able to convince my muscles to contract against any part of the balloon snaking through my insides."
                                m "Maverick tugged harder, managing to stretch the condom material to the point his head was almost out of my hole."
                                play sound "fx/bubbles.ogg"
                                play sound2 "fx/spray.ogg"
                                $ bangok_four_bryce3_store.mavbroke == True
                                m "He pulled out, tearing the condom material and leaving my asshole gaped in one go. In a moment his cum rushed to equilibrium within me, saturating my intestinal walls and spurting out of my ass and over my legs in a small river."
                            "[[Push.]":
                                m "I strained, abused muscles fighting against spasms of pain to contract against any part of the balloon snaking through my insides."
                                m "Then I felt fluids flowing within me, and Maverick retreated a few more inches."
                                m "After a few such cycles, Maverick's head popped free, leaving my hole gaping around the taut condom material."
                                m "Gripping the neck, Maverick pulled free of the bloated condom in my ass, leaving the end to let a river of cum flow out of me and over my legs."
                                m "Then he pulled the rest of the condom out in one long blob."
            else:
                if bangok_four_bryce3_store.protection == False or bangok_four_bryce3_store.mavbroke == True:
                    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                        if bangok_four_playerhasdick == True:
                            m "When his head tugged through my asshole my sphincter gaped, letting a dribble of cum and piss run down my taint, over my balls, and down my spent shaft."
                        else:
                            m "When his head tugged through my asshole my sphincter gaped, letting a dribble of cum and piss run down my taint and over my flushed lips."
                    else:
                        if bangok_four_playerhasdick == True:
                            m "When his head tugged through my asshole my sphincter gaped, letting a dribble of cum run down my taint, over my balls, and down my spent shaft."
                        else:
                            m "When his head tugged through my asshole my sphincter gaped, letting a dribble of cum run down my taint and over my flushed lips."
                else:
                    play sound "fx/uncork.ogg"
                    if bangok_four_playerhasdick == True:
                        m "When his head tugged through my asshole my sphincter gaped, easily letting his filled reservoir plop out to slap my spent balls."
                    else:
                        m "When his head tugged through my asshole my sphincter gaped, easily letting his filled reservoir plop out to swing past my flushed lips."
        elif bangok_four_bryce3_store.mavtarget == "vag":
            # Only unprotected path gets here.
            if bangok_four_bryce3_store.brycetarget == "vag":
                m "When Maverick's head tugged through my lips, I remained gaped open. A dribble of the fluids inside me followed him, the rest still trapped much deeper inside me."
            else:
                if persistent.bangok_inflation == True:
                    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                        m "When Maverick's head tugged through my lips, I remained gaped open. A river of cum and piss spilled from my canal onto the sand, spattering my legs."
                    else:
                        m "When Maverick's head tugged through my lips, I remained gaped open. A river of cum spilled from my canal onto the sand, spattering my legs."
                else:
                    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                        m "When Maverick's head tugged through my lips, I remained gaped open. A dribble of cum and piss followed him, the rest still trapped much deeper inside me."
                    else:
                        m "When Maverick's head tugged through my lips, I remained gaped open. A dribble of cum spilled from my canal onto the sand, the rest still trapped much deeper inside me."
        elif bangok_four_bryce3_store.mavtarget == "womb":
            if (bangok_four_bryce3_store.protection == False and bangok_four_bryce3_store.mavws == True) or bangok_four_bryce3_store.mavbroke == True:
                m "As he pulled back through my cervix, fluid splashed from my womb, saturating my canal's walls."

            if persistent.bangok_inflation == True:
                if bangok_four_bryce3_store.protection == False or bangok_four_bryce3_store.mavbroke == True:
                    # Maverick unprotected
                    play sound "fx/spray.ogg"
                    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                        m "When his head tugged out of my fuck-hole it gaped, letting a river of cum and piss pour from inside me onto the sand."
                    else:
                        m "When his head tugged out of my fuck-hole it gaped, letting a river of cum pour from inside me onto the sand."
                else:
                    # Maverick protected
                    if bangok_four_bryce3_store.brycebroke == True:
                        m "The balloon of cum pulled at my inner gate, pressed flat against it by the pressure from the rest of my distended womb."
                        m "Maverick stopped, cognizant he couldn't make any more progress without hurting me or breaking the condom."
                        menu:
                            "J-Just tear it.":
                                Mv "You are sure?"
                                m "I nodded, knowing that as my cervix began to recover, it'd make getting the balloon of cum and all the other fluid out of me all the harder."
                                m "Maverick tugged harder, managing to stretch the condom material to the point his head had almost pulled through my folds."
                                play sound "fx/bubbles.ogg"
                                play sound2 "fx/spray.ogg"
                                $ bangok_four_bryce3_store.mavbroke == True
                                m "He pulled out, tearing the condom material and leaving my cunt lips empty and gaped in one pull. I gasped as the barrier's stretching force disappeared, a river of cum leaking from my breached inner gate to spatter over my legs and the sand."
                            "H-How do we get it out?":
                                m "Gently, Maverick curled his tail around, then pressed it against my distended belly."
                                m "I gasped, feeling almost like I was pissing as Maverick's cum flowed from the reservoir of his condom to pool in and around his tip, forced out by the added pressure of Maverick's tail."
                                m "Then the rest of the reservoir popped through, the blob of cum shoving Maverick's cock out of me as Bryce's load in my womb pushed on it."
                                play sound "fx/uncork.ogg"
                                m "The bloated condom plopped out onto my legs, followed by a small river of cum."
                    else:
                        m "The balloon of cum pulled at my inner gate, thick, heavy, and unwilling to move from my bloated belly."
                        m "Maverick stopped, cognizant he couldn't make any more progress without hurting me or breaking the condom."
                        menu:
                            "J-Just tear it.":
                                Mv "You are sure?"
                                m "I nodded, knowing that as my cervix began to recover, it'd make getting the balloon of cum out of me all the harder."
                                m "Maverick tugged harder, managing to stretch the condom material to the point his head had almost pulled through my folds."
                                play sound "fx/bubbles.ogg"
                                play sound2 "fx/spray.ogg"
                                $ bangok_four_bryce3_store.mavbroke == True
                                m "He pulled out, tearing the condom material and leaving my cunt lips empty and gaped in one pull. I gasped as the barrier's stretching force disappeared, a river of cum leaking from my breached inner gate to spatter over my legs and the sand."
                            "H-How do we get it out?":
                                m "Gently, Maverick curled his tail around, then pressed it against my distended belly."
                                m "I gasped, feeling almost like I was pissing as Maverick's cum flowed from the reservoir of his condom to pool in and around his tip, forced out by the added pressure of Maverick's tail."
                                m "Then the rest of the reservoir popped through, the blob of cum shoving Maverick's cock out of me."
                                play sound "fx/uncork.ogg"
                                m "The bloated condom plopped out onto my legs."
            else:
                if bangok_four_bryce3_store.protection == False or bangok_four_bryce3_store.mavbroke == True:
                    play sound "fx/spray.oggg"
                    if persistent.bangok_watersports == True and bangok_four_bryce3_store.brycews == "before":
                        m "When his head tugged through my cunt lips he left me gaping, letting a dribble of cum and piss run down my lips and over my legs."
                    else:
                        m "When his head tugged through my cunt lips he left me gaping, letting a dribble of cum run down my lips and over my legs."
                else:
                    play sound "fx/uncork.ogg"
                    m "When his head tugged through my cunt lips he left me gaping, easily letting his filled reservoir slide out of me."
        else:
            $ renpy.error("Wh- What? How did you finish Maverick in your \"%r\"?"%bangok_four_bryce3_store.mavtarget)

    $ renpy.pause(0.8)

    if persistent.bangok_inflation == True and ((bangok_four_bryce3_store.protection == False) or (bangok_four_bryce3_store.brycebroke == True) or (bangok_four_bryce3_store.mavbroke == True)):
        m "Maverick stepped away from me. I slumped into the sand, unable to move with my insides rearranged around my bloated belly."
    else:
        m "Maverick stepped away from me. I slumped into the sand, unable to move with my insides partly rearranged by the rough fuck."

    $ renpy.pause(0.8)
    Br brow "Maverick, where are you going?"
    Mv nice "Home."
    Br stern "After {i}that{/i}? There's no way [player_name] is walking after that. That was a {i}really{/i} punishing pace."
    Br brow "You could at least hold on a few minutes to help me make sure they're okay."
    Mv normal "It sounds like you have that covered."
    $ renpy.pause(0.5)
    Br stern "Maverick!"
    $ renpy.pause(1.2)
    show bryce brow at center with dissolvemed
    Br "He left."

    menu:
        "G-good riddance.":
            Br stern "..."
        "B-But that was such a great fuck...":
            show bryce smirk with dissolve
            $ renpy.pause(0.5)
            Br "Better than mine?"
            menu:
                "S- Ah! Sarcasm, Bryce!":
                    c "F-Fuck everything hurts."
                    Br stern "..."
                "Yeah.":
                    Br brow "Oh."
                "You're better.":
                    Br flirty "Good to hear."
        "H-His choice.":
            Br stern "..."
        "[[Say nothing.]":
            pass

    $ renpy.pause(0.8)
    Br brow "Damn, now everyone left without cleaning up their trash."
    Br normal "You wouldn't mind sticking around to help, would you?"
    menu:
        "Not at all.":
            pass
        "I-I don't think I can move.":
            pass
        "I... think I'll just cheer from the sidelines.":
            pass
    show bryce stern with dissolve
    $ renpy.pause(0.5)
    hide bryce with dissolvemed
    show bryce normal:
        zoom 2.8
    with dissolvemed
    Br "Grab my horns."
    $ renpy.pause(0.5)
    show black
    hide bryce
    with dissolve
    m "I managed to get my arms up onto Bryce's head, grabbing hold of his horns like handlebars."
    m "Dragging my shut-down lower body, Bryce carried me up the beach on his snout, setting me down where I could sit against the still-warm rocks where Sebastian's fire had cooked dinner."
    hide black with dissolve

    if persistent.bangok_inflation == True and ((bangok_four_bryce3_store.protection == False) or (bangok_four_bryce3_store.brycebroke == True) or (bangok_four_bryce3_store.mavbroke == True)):
        m "A trail of fluids led from between my legs back down the beach to where the dragons had their way with me."

    m "Picking up my clothes with his maw, Bryce carried them up and set them within my reach."
    show bryce normal with dissolve
    menu:
        "Thanks, Bryce.":
            pass
        "I don't think I should put those on yet.":
            Br brow "Then don't. I had just assumed you might get cold, being without scales, and want to drape those over you."
            c "Oh. Thanks."
        "[[Say nothing.]":
            pass
    hide bryce with dissolve
    m "Bryce started to clean up, starting first with our foodscraps. But with the amount of trash left by five people, it was clear it would take a while."

    $ bangok_four_bryce3_store.unplayed = False
    $ bangok_four_bryce3_store.mc_bottom = True

    show bryce brow with dissolve

    jump bangok_four_bryce3_wannaknowscars

label bangok_four_bryce3_mcbottom_train_epilogue:
    Br normal "I suppose I'll have to tell you about the second scar some other time."
    Br brow "Your apartment is on the other side of town, and if you're not moving on your own yet, I don't think we should be taking you that far."
    m "I pulled my knees in and struggled to push myself up off the rocks, but only managed a few inches before pain in my midriff had me slumping back."
    c "What do you want me to do, then? Sleep here?"
    Br laugh "I wouldn't do that to you. You can sleep over at my place."
    menu:
        "Thanks.":
            show bryce normal with dissolve
        "If you insist.":
            show bryce brow with dissolve
        "Is this an excuse to sneak in a round two?":
            Br flirty "Depends, would you want that?"
            menu:
                "Please, no.":
                    Br laugh "Sorry, sorry. I was kidding."
                "Oh yes.":
                    Br laugh "Maybe."
                    Br smirk "I don't know if I'm recovered from the first one yet."
                    $ renpy.pause(0.3)
                    show bryce stern with dissolve
                    $ renpy.pause(0.8)
                    Br normal "Yeah. Make that a prolly not."
    c "You're not going to drag me on the ground to your apartment though, right?"
    Br brow "I hope not. Came up with a couple ideas while packing the trash."
    m "He lay down in front of me."
    Br normal "Here. Try getting on my back."

    $ renpy.pause (0.3)
    scene black with dissolvemed
    $ renpy.pause (1.0)
    scene padx at Pan ((0, 240), (0,360), 3.0) with dissolveslow
    $ renpy.pause (1.3)
    show bryce brow with dissolve
    if (bangok_four_bryce3_store.protection == False) or (bangok_four_bryce3_store.brycebroke == True) or (bangok_four_bryce3_store.mavbroke == True):
        Br "I think I've got a towel around here somewhere for any leaks."
    jump bryce3skip


label bangok_four_bryce3_mctop:
    scene beachx at Pan ((300, 0), (300, 0), 0.0) with dissolve
    show bryce smirk flip at right with dissolve
    m "Bryce wandered a few steps away from his basket of supplies, then lifted his tail to expose his hindquarters."
    
    if bangok_four_bryce3_store.sebastian_in == True:
        Br "Sebastian? I know you want to keep things short."
        Br smirk flip "Plus, it's not like you're leaving anyone sloppy seconds."
        show sebastian drop flip at center behind bryce with dissolve
        Sb "Alright, alright."
        show sebastian disapproval flip:
            xpos 0.51
            ypos 1.15
        with ease
        Sb normal flip "What if I want to make you a little sloppy first?"
        Br laugh flip "Damn, you and licking people."
        if bangok_four_playerhasdick == True:
            Br normal flip "I don't know. [player_name]? You're the only one I can think of who might object."
            Br smirk flip "You fine with sticking it in a bit of dragon saliva?"
            menu:
                "I'd love to have your mouth.":
                    c "Thanks so much for offering."
                    Br flirty flip "Oh?"
                    Br laugh flip "Not what I was saying, but I'm in."
                    Br normal flip "Wait until Sebastian's done, though. Let's everyone take their turns so nobody gets hurt."
                "No objection here.":
                    Br normal flip "Alright. Have fun back there."
                "I might have a taste myself.":
                    Br laugh flip "Let's let Sebastian finish up first."
                "I'd rather not.":
                    show bryce brow flip with dissolve
                    Sb disapproval flip "Then I suppose I can skip it."
                    jump bangok_four_bryce3_mctop_seb_rimming_skip
        show bryce normal flip with dissolve
        hide sebastian with easeoutbottom
        m "Bryce laid his tail over Sebastian's head and down his back as the small runner got on his knees under Bryce's thighs."
        m "Sebastian ran his snout up Bryce's shaft, the tip of his tongue sticking out to lap at Bryce's length."
        if persistent.bangok_cloacas == True:
            m "Then, at the base of Bryce's large cock, Sebastian dug his muzzle into Bryce's slit."
        else:
            m "He kept going, running his tongue one plate back on Bryce's underside, before digging his muzzle into another, better-hidden slit."
        show bryce laugh flip with dissolve
        Br "You can't be that hungry; you just ate!"
        show bryce smirk flip with dissolve
        m "Sebastian's licking continued for a few seconds more before he pulled back, horns nestling Bryce's tail on his head like a massive hat before he began to rise."
        show sebastian smile flip behind bryce:
            yanchor 1.0
            xanchor 0.5
            xpos 0.51
            ypos 1.2
        with easeinbottom
        Sb smile flip "What can I say? I know what I like."
        $ renpy.pause(0.5)
        label bangok_four_bryce3_mctop_seb_rimming_skip:
        show sebastian normal flip:
            yanchor 1.0
            xanchor 0.5
            xpos 0.51
            ypos 1.05
        with ease
        show bryce normal flip:
            ypos 1.05
        with ease
        m "Hugging Bryce's tail, Sebastian lifted it up while guiding Bryce's hindquarters until the larger dragon knelt on the sand."
        m "Then Sebastian lined up with Bryce's ass."
        show sebastian smile flip:
            xpos 0.52
            ypos 1.05
        with ease
        show bryce smirk flip with dissolve
        show bryce smirk flip:
            xpos 0.99
        with ease
        show sebastian smile flip:
            xpos 0.51
            ypos 1.05
        with ease
        play soundloop "fx/rub2.ogg" fadein 0.5
        show sebastian smile flip:
            ease 0.15 xpos 0.52 ypos 1.05
            ease 0.5 xpos 0.51 ypos 1.05
            repeat
        show bryce normal flip:
            ease 0.15 xpos 0.995
            ease 0.5 xpos 0.99
            repeat
        with None
        $ renpy.pause(0.5)
        Br laugh flip "Ah, fuck I needed this."
        Sb shy flip "You won't be saying that when it's Maverick's turn."
        Sb smile flip "He's probably the reason Zhong sits each of these out."
        Mv angry "I'm not that rough."
        Br "Whatever you say!"
        $ renpy.pause(1.2)
        Br smirk flip "You know, Sebastian, I can almost feel you back there."
        Sb smile flip "I'd say \"fuck you, Bryce,\" but, well..."
        Br laugh flip "You've got that covered!"
        $ renpy.pause(0.5)
        Sb normal flip "Mm."
        $ renpy.pause(0.8)
        Sb shy flip "A-About to--"
        show bryce smirk flip with dissolve
        show sebastian shy flip:
            ease 0.15 xpos 0.52 ypos 1.05
        show bryce smirk flip:
            ease 0.15 xpos 0.995
        with None
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg"
        m "Sebastian pulled Bryce's hips and tail flush against himself and stiffened."
        m "Bryce threw a smile back over his shoulder as Sebastian came."
        if persistent.bangok_knot == True:
            $ renpy.pause(0.8)
            Br "Up for a bit of knotfucking?"
            if bangok_four_playerhasdick == False:
                $ bangok_four_bryce3_store.knotfuck = True
            else:
                Sb drop flip "I don't want to stretch you out even more than usual for [player_name]."
                Br flirty flip "Oh come on. I'm tight."
                Br laugh flip "As if you could stretch me out."
                menu:
                    "This I'd like to see.":
                        $ bangok_four_bryce3_store.knotfuck = True
                        show bryce smirk flip with dissolve
                        Br smirk flip "Well, Sebastian?"
                    "That sounds... weird.":
                        $ bangok_four_bryce3_store.knotfuck = False
                        show bryce brow flip with dissolve

            if bangok_four_bryce3_store.knotfuck == False:
                Sb drop flip "I think I'm too sensitive to do that right now anyway."
                show sebastian drop flip:
                    xpos 0.51
                    ypos 1.05
                with ease
                m "Sebastian tugged free of Bryce, a bulb of flesh at his base momentarily spreading Bryce's underbelly plates further."
            else:
                show sebastian disapproval flip with dissolve
                $ renpy.pause(0.3)
                show sebastian disapproval flip:
                    ease 2.0 xpos 0.515 ypos 1.05
                with None
                m "Sebastian eased back extremely slowly."
                m "Where his hips separated from Bryce's, I saw a bulb of flesh at his base spreading Bryce's underbelly plates, stretching the hide beneath."
                show bryce pant flip with dissolve
                Br "There's a good stretch! Mmh!"
                show sebastian disapproval flip:
                    xpos 0.518 ypos 1.05
                with ease
                show sebastian drop flip with dissolve
                show sebastian drop flip:
                    xpos 0.51 ypos 1.05
                with ease
                m "Sebastian pushed his knot back in, faster, then yanked all the way out to his tip with a gasp."
                Br brow flip "That's it?"
                Br flirty flip "C'mon. I know you can knotfuck better than that."
                Sb drop flip "N-Not right now. I'm feeling {i}really{/i} sensitive after that."
                Br normal flip "If you say so."
                m "With a wince, Sebastian pulled his cockhead out."
        else:
            m "After a few long seconds, Sebastian relaxed, then began to pull himself out."
        show sebastian smile flip with dissolve
        show sebastian smile flip:
            xpos 0.51
        with ease

        if persistent.bangok_inflation == True:
            play sound "fx/uncork.ogg"
            m "Sebastian's blob of cum followed, condom reservoir inflated to larger than my fist as it popped free of Bryce's hindquarters."
        else:
            m "His meagre cumload wrapped in its condom reservoir plopped free of Bryce, making Sebastian's shaft bob and wiggle."
        show sebastian drop flip:
            xpos 0.49
        with ease
        m "Then Sebastian stepped completely out of the way."
        Sb disapproval "I think I need to call it a night now. Take this off and get some rest."
        Sb smile "Thanks for that, Bryce."
        show bryce normal flip with dissolve
        show bryce normal:
            ypos 1.0
        with ease
        show bryce normal with dissolve
        m "Bryce shook out his tail, then turned to give Sebastian a nod."
        Br "Have a good walk home now."
        hide sebastian with dissolve
        $ renpy.pause(0.5)
        show bryce normal flip with dissolve
        show bryce at right with ease
        m "Then Bryce turned and lifted his tail for me and Maverick."

    Br "So, Maverick, [player_name], which of you wants first?"
    $ bangok_four_bryce3_store.top_mav = True
    label bangok_four_bryce3_mctop_mavfirst_menu:
    menu:
        "What'll happen if Maverick goes before me?" if bangok_four_bryce3_store.top_mav == True:
            $ bangok_four_bryce3_store.top_mav = False
            Br laugh flip "I'll be loose and sloppy is what'll happen!"
            Br smirk flip "There's always the chance Maverick could get me off with the assfucking too. Not a big chance, but a chance."
            Mv normal "It's common when we take this position."
            Br laugh flip "Hey!"
            if bangok_four_playerhasdick == False:
                Br normal flip "Anyway. If I do get off, refractory period means I might not be able to go fucking anyone. If that's what you had planned because of your... y'know... not having a penis, then keep that in mind."
            else:
                Br normal flip "Anyway. I could still take your cock, but refractory period means playing with mine'll be a little too intense for me. Just keep that in mind."
            jump bangok_four_bryce3_mctop_mavfirst_menu
        "I'll go first?":
            $ bangok_four_bryce3_store.top_mav = False
            Mv nice "..."
            Br flirty flip "Works for me."
        "Maverick? If you'd like to go.":
            $ bangok_four_bryce3_store.top_mav = True
            Mv normal "..."
            Br flirty flip "Works for me."

    if persistent.bangok_watersports == True:
        Br flirty flip "You know, speaking of {i}go{/i}ing..."
        Mv angry "Really, Bryce?"
        Br laugh flip "What? If you or [player_name] happen to have urinary needs to exercise..."
        Br flirty flip "I'm not opposed to doing my part to keep it out of our beautiful natural locations."
        Br smirk flip "And by that I mean--"
        Mv normal "We know what you mean, Bryce."
        menu:
            "Okay. Ew.":
                label bangok_four_bryce3_mctop_nows:
                Br brow flip "Oh."
                Br stern flip "Nevermind then. I guess we'll just skip that part of the fun."
                $ bangok_four_bryce3_store.brycews = None
                $ bangok_four_bryce3_store.mavws = False
            "I'm not sure I want to fuck you after someone's pissed in you.":
                jump bangok_four_bryce3_mctop_nows
            "I'm going to be sloppy in {i}Maverick's{/i} piss?" if bangok_four_bryce3_store.top_mav == True:
                Br flirty flip "Like the idea?"
                menu:
                    "No!":
                        jump bangok_four_bryce3_mctop_nows
                    "Kinda...":
                        pass
                    "Yes.":
                        pass
                $ bangok_four_bryce3_store.brycews = "before"
                $ bangok_four_bryce3_store.mavws = True
            "Thanks. Could use someplace to go.":
                Br flirty flip "Happy to be of service."
                $ bangok_four_bryce3_store.brycews = "before"
                $ bangok_four_bryce3_store.mavws = True

    if bangok_four_bryce3_store.top_mav == True:
        jump bangok_four_bryce3_mctop_mavgoes
    else:
        jump bangok_four_bryce3_mctop_mcgoes

label bangok_four_bryce3_mctop_mcgoes:
    show bryce normal flip at center with ease
    m "Walking over to Bryce, I considered my options."
    menu:
        "Fuck Bryce's ass." if bangok_four_playerhasdick == True and bangok_four_bryce3_store.top_mav == False:
            jump todo_out_of_content_bangok_four_bryce3
        "Fuck Bryce's gaping, sloppy ass." if bangok_four_playerhasdick == True and bangok_four_bryce3_store.top_mav == True:
            jump todo_out_of_content_bangok_four_bryce3
        "Fuck Bryce's mouth." if bangok_four_playerhasdick == True:
            jump todo_out_of_content_bangok_four_bryce3
        "Ride Bryce's mouth." if bangok_four_playerhasdick == False:
            jump todo_out_of_content_bangok_four_bryce3
        "Ride Bryce's shaft....":
            if bangok_four_playerhasdick == False:
                m "With your..."
                menu:
                    m "With your..."
                    "Ass.":
                        jump todo_out_of_content_bangok_four_bryce3
                    "Vagina.":
                        jump todo_out_of_content_bangok_four_bryce3
    jump todo_out_of_content_bangok_four_bryce3

label bangok_four_bryce3_mctop_mavgoes:
    show maverick normal flip at center behind bryce with dissolve
    m "Maverick watched me with suspicion as he walked over to Bryce."
    m "Only when he'd nearly stepped on Bryce's tail did he focus on his partner."
    label bangok_four_bryce3_mcbottom_train_bryce_takeover_mavgoes_merge:
    $ bangok_four_bryce3_store.mavtarget = "bryce"
    show maverick nice flip with dissolve
    show bryce smirk flip:
        transform_anchor True
        ease 0.8 rotate 20 xpos 0.93 ypos 1.3
    with None
    m "After having his tail nudged out of the way, Bryce dropped to his chest, folding his forelegs as he presented his ass."
    show maverick nice flip:
        xpos 0.55
    with ease
    m "Maverick stepped over him, bending Bryce's tail back against his underbelly. I could now see Maverick's shaft emerging, thick and long enough to be visible between his hindlegs even with him standing normally."
    
    if bangok_four_bryce3_store.mc_bottom == False:
        show bryce stern flip with dissolve
        m "Then Bryce's face fell."
        Br "Fuck. [player_name], would you mind lubing me and Maverick? This isn't going to work otherwise."
        c "Sure."
        show bryce normal flip with dissolve
        show maverick normal flip with dissolve
        m "I slid Bryce's basket of supplies over, then took a large spurt of lube into my hands to spread over Maverick."
        show maverick angry flip with dissolve
        m "Maverick stiffened, but otherwise refused to show discomfort at my proximity. His shaft twitched as I rubbed on the lube, excited by the physical contact."
        m "I gave Maverick another two spurts, then rubbed the mess on my hands off on Bryce's ass. The rest I wiped off on his underbelly plates, all around his slit."
        Br laugh flip "Alright, get some distance and enjoy the show."
        show maverick normal flip with dissolve

        m "After I sat the supplies and myself a little further up the beach, Bryce wiggled his hips under Maverick."
    Br flirty flip "Alright, Mavers. Plow me."
    if persistent.bangok_watersports == True and bangok_four_bryce3_store.mavws == True and bangok_four_bryce3_store.mavbroke == False and bangok_four_bryce3_store.mc_bottom == False:
        Mv normal flip "And your urination fetish?"
        Br "If you don't mind."
        $ renpy.pause(0.3)
        play soundloop "fx/faucet1.ogg" fadein 0.5
        queue soundloop "fx/faucet2.ogg"
        m "With a twitch of his shaft, Maverick began to piss, clear stream in the moonlight spattering Bryce's slit and running down his underbelly plates, over the tip of his shaft."
        show maverick nice flip:
            xpos 0.555
        show bryce flirty flip:
            xpos 0.9325
        with ease
        m "Then Maverick pushed his tip into Bryce's ass, still pissing."
        Br pant flip "Haaahhh!"
        m "I watched, mesmerised as Maverick held his position. I could still hear the stream of liquid pooling inside Bryce."
        stop soundloop fadeout 0.8
        $ renpy.pause(0.8)
        m "Finally, Maverick ran dry. He switched to feeding Bryce's ass cockflesh instead."
        show maverick nice flip:
            ease 1.5 xpos 0.57
        with None
        $ renpy.pause(0.8)
        m "Bryce's guts audibly settled slightly as Maverick worked his whole shaft inside, until he was lying on Maverick's tail and back."
    else:
        show maverick nice flip:
            xpos 0.555
        show bryce flirty flip:
            xpos 0.9325
        with ease
        m "Maverick pushed his tip into Bryce's ass, quickly. Bryce's maw fell open, exhaling abruptly."
        Br pant flip "Haaahhh!"
        m "After giving Bryce a few moments to adjust, Maverick kept pushing, feeding Bryce's ass all the cockflesh he had to give."
        show maverick nice flip:
            ease 1.5 xpos 0.57
        with None
        $ renpy.pause(0.8)
        m "Maverick lay on Bryce's tail and back a moment, both of them catching their breath."

    m "Bryce's tail tip flicked against Maverick's neck."
    Br pantflirt flip "Y-You're, ah, crushing my circulation there."

    show maverick nice flip:
        transform_anchor True
        ease 0.3 rotate 2 xpos 0.57 ypos 1.02
    show bryce pant flip with dissolve
    show bryce pant flip:
        transform_anchor True
        ease 0.8 rotate 22 xpos 0.93 ypos 1.3
    with None
    m "Maverick responded by closing his teeth on the hard spines at the end of Bryce's tail, then tugging Bryce's rear further forward."

    Br pant flip "Haaahhh..."






    jump todo_out_of_content_bangok_four_bryce3

label todo_out_of_content_bangok_four_bryce3:
    play sound "fx/system3.wav"
    s "Out of content. Rollback and save, or prepare to crash."
    $ renpy.error("TODO: Out of content.")