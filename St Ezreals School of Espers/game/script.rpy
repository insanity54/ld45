# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miyake", color="#0b2987")
define s = Character("Shizuma", color="#bdbba6")
define t = Character("Tanaka", color="#FFFFFF")
define a = Character("Aldo", color="7000ff")
define admin = Character("Administrator", color="#7e7e7e")
define mystery = Character("???", color="#808080")

define projectionDissolve = ImageDissolve("projection.jpg", 1.0, 0)


label start:
    menu:
        "Begin the game":
            jump start
        "Miyake's first projection":
            jump projection
        "After the entrance exam":
            jump campus


    scene bg lecturehall

    "Nervously sitting at his desk, Miyake glanced around the room to see that most of his peers were already relaxing with their pencils down."
    "Five minutes and five seconds remained on the clock and Miyake couldn't stop sweating."

    show miyake blue grimacing
    m "They can't be done yet. That's impossible! They have to be cheating."

    hide miyake blue grimacing
    show administrator grey neutral
    admin "The hour is almost complete, please finish up your entrance exams within the next five minutes."

    hide administrator grey neutral
    show miyake blue grimacing
    m "Shit! My exam isn't even half complete."

    "Miyake quickly flipped through the incomplete pages, barely eyeing the masses of text. "

    m "There's no way! This much would take me another thirty minutes!"

    "A bead of sweat formed on his brow. Holding his exam with both hands, a pencil between his index and middle finger, Miyake looked again at the room."
    "The light gently shone in through the tall, contemporary windows. Luckily they were diffused so he couldn't see outside, that would only distract him."
    "He was sitting in the middle of the lecture hall, about half way up the elevated seating."
    "From the view up here he could see the exam admin at the front of the room before the large green chalkboard."
    "There the words \"St. Ezreal Esper Academy Entrance Exam\" were written in big letters."

    m "Who am I kidding. This is St. Ezreal's after all."

    "Amidst the sound of pencils on paper, Miyake was ready to concede, close his eyes and put his head down."
    "With eyes halfway shut, Miyake suddenly noticed a girl in the front row, frantically flipping through pages similarly to as Miyake had just done."
    "So focused on the test, Miyake hadn't noticed her before."

    hide miyake blue grimacing
    show miyake blue grimacing at left
    show shizuma pink flustered at center

    m "damn, she is actually kind of cute."

    "The girl had platinum blonde hair put in a side pony tail."

    hide shizuma pink flustered
    show shizuma pink surprised at center

    m "Is she even wearing makeup? Maybe she's just a natural beauty."

    "The sound of pencils stopped."
    "Heads seemed to turn in slow motion towards Miyake."
    "Although softly, Miyake had thought out loud, and now many students were looking up at him."
    "The girl in the front seemed to have heard as well, and her expression had changed from hasted to surprised."
    "Her eyes were wide open and met with Miyake's. Miyake just stared, not knowing what to do."
    "She had green eyes, big green eyes."

    "The class let out a laugh and the test administrator stood up."

    show administrator grey neutral at right
    admin "Quiet please, eyes on your papers."

    hide shizuma pink surprised at center
    show shizuma pink blushed at center
    "The girl blushed, turning to her front and embarrassingly looking down at her exam book."
    "She put her shoulders up as if to hide between them, with her hands together, arms tucked between her legs."

    "Miyake let out an embarrassed cough and blushed just the same. He closed his eyes and tried to pretend that didn't happen."
    "He thought of those green eyes, like freshly polished emeralds glistening in the sun."

    admin "Two minutes!"
    hide administrator grey neutral

    "Miyake hadn't answered a single question in three minutes, too busy thinking about giving up and looking at the cute girl."

    hide shizuma pink blushed
    hide miyake blue grimaching at left
    show miyake blue focusing at center
    m "This is crunch time!"

    "Miyake trited to get himself amped up."
    "With half the exam remaining, and such little time, there was only one option remaining for success."
    "The thing that got Miyake into Esper studies in the first place, the thing that had gotten him into so much trouble, but oh so much fun... "

label projection:
    scene bg lecturehall
    hide miyake
    show miyake blue projecting at center
    "Miyake sat up straight with a stern look on his face, closed his eyes, and opened his mind's eye."
    "Astral Projection. A world within the mind, able to be summoned by any human being. The basis for Esper abilities."




    scene bg black
    with projectionDissolve
    "In this world, time stands still, as the Astral reality becomes that of the user's design."
    "There is nothing but one's self and blackness, until one's consciousness creates another thing."
    "Miyake had discovered this place by accident when he was young, bored, and lonely. Like many, Miyake had created imaginary friends to keep himself company, but only after an accident did Miyake actually migrate an Astral lifeform to the real world."
    "It was an imperfect being, with it's soul tied to Miyake himself, but it lived, walked and talked for a short time. A taboo, creating life, but he didn't learn that until later."

    scene bg dragon
    with dissolve
    "Right now the situation called for one of Miyake's best projections. HYPER DRAGON EYE! The name was a work in progress, because he couldn't think of any more fitting names."
    "This projection could be likened to an ancient dragon who is terrorizing a populous. The dragon's seeming omnipresence in the people's lives create the sentiment that the dragon is the seer of all secrets."

    scene bg projection
    show miyake blue projecting at center
    with dissolve
    "Miyake began the projection by viewing himself in the Astral world. Standing tall, with arms stretched downward, he created a summoning circle at his feet. Elements of vision, mind, and body were contained within the circle."
    "The circle spun slowly, gradually increasing in size. Silently and motionless in the real world, Miyake opened both eyes in the Astral world, yelling at the top of his lungs, HYPER-DRAGON-EYE!"

    hide miyake
    show miyake blue thirdeye at center
    with dissolve
    "A third eyelid suddenly appeared in Miyake's Astral forehead, opening wide as the summoning circle expanded drastically."
    "Miyake drew on his knowledge of the lecture hall he was sitting in, and superimposed it's geometry into the Astral realm."

    "So far, this process was child's play, an activity kids with wild imaginations do. The next step however, was what separated the men from the boys."
    "The final step was bridging the gap between the Astral Realm and the physical world, a feat which only Espers were capable of."
    "With the image of Hyper Dragon Eye in his mind, Miyake opened his physical eyes, splicing the two realities into one."
    "Obviously, he couldn't reveal a third eye or giant summoning circle to those in his surroundings, so he made sure to bridge those features into a subvisual level of existence."

    show bg lecturehall
    show miyake blue projecting at center
    with pixellate
    "The projection was complete, and there was still one minute and fifty seconds on the clock."

    hide miyake
    show miyake blue neutral at center
    "Miyake flipped to the next page in his exam book, and just like a uneducated peasant's delusions of an ancient dragon's capabilities, he felt the secrets of those in his surroundings."
    "His third eye darted around from left to right, gazing upon the completed papers of his peers."
    "Answer 53, E=mc2."
    "Answer 54, \"Malcom's Theorum solves for the natural fluctuations of space time after becoming cached in the Astral Flow\"."
    "Miyake's hands raced wildly as he wrote in answers gathered from the students around him."
    "Answer 55, \"Effects from personal reality cannot be affected by magic because magic affects the physics of the world, whereas personal reality is outside of that space.\""

    "One minute remained, then thirty seconds, then ten. Miyake scrambled to write in the last stolen answer."

    show administrator grey neutral at right
    admin "Pencils down. The exam is complete."

    hide administrator
    hide miyake

label campus:
    show bg uni
    with fade

    "St. Ezreal's campus was lit up by the sun as students exited the Astral Science Studies building. A.S.S."

    show miyake blue squinting
    m "That test was ASS"

    "Miyake pouted, with one hand holding his book bag slung over his shoulder and the other in his pocket."
    "He had a concerned look on his face as he walked close eyed down the concrete path which separated two sections of grass."

    hide miyake
    show miyake blue projecting
    m "At least I finished, and those answers seemed Okay."

    "The other students who had been taking the entrance exam were walking in the same direction."
    "There were school uniforms of all the nearby highschools, as well as uniforms Miyake had never seen before."

    hide miyake
    show tanaka red mystery at center
    mystery "Hey you!"

    show miyake blue peek at left
    "An unfamiliar voice pitched in, Miyake opening an eye to see."
    "There standing before him, was a long brown haired girl with arms crossed. She was wearing one of the uniforms Miyake hadn’t recognized, and boy did she look pissed off."

    m "Is this some kind of lovers quarrel?"
    "Miyake looked behind him to see who she was talking to."

    hide tanaka
    show tanaka red condescending at center
    mystery "No, you! You right there with that dumb look on your face!"

    "The girl barked, and now Miyake got it."
    "She standing there with a fancy looking, two piece white skirt uniform and a book bag in one hand."

    hide miyake
    show miyake blue confused at left
    m "Um, what do you want?"

    mystery "You said something about Shizuma and made her blush. What was it?!"

    "the girl asked brazenly, as she clenched her free fist. It looked like a vein in her forehead would pop at any second."
    "Miyake didn't want to make a scene, but if this girl kept up, there was about to be one regardless."

    hide miyake
    show miyake blue charming at left
    m "Oh that, that was uhh.."

    "Miyake didn't know what to say. If he came right out and said what he said earlier, she might get the wrong idea, as if he were a stalker or something."

    hide miyake
    show miyake blue nervous sweat at left
    mystery "What's that? I can't hear you over the sound of your stupid mumbling face!"

    "The girl rudely piped. She was serious. People were starting to look. Miyake was even more speechless now, because of the weird crazy girl in front of him."

    show shizuma pink neutral at right
    s "Ummm"

    "A voice quietly spoke. Miyake and the crazy girl turned to see the same platinum blonde girl from before."

    s "Tanaka-chan, you shouldn't yell at strangers."




    return
