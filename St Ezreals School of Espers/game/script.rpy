# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miyake", color="#0b2987")
define s = Character("Shizuma", color="#bdbba6")
define t = Character("Tanaka", color="#775b51")
define a = Character("Aldo", color="#7000ff")
define tsu = Character("Tsubasa", color="#a9b153")
define admin = Character("Administrator", color="#7e7e7e")
define mystery = Character("???", color="#808080")

define projectionDissolve = ImageDissolve("projection.jpg", 1.0, 0)


label start:
    menu:
        "Begin the game":
            jump game
        "Miyake's first projection":
            jump projection
        "After the entrance exam":
            jump campus
        "Aldo's fight with Miyake":
            jump aldo

label game:
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
    "The circle spun slowly, gradually increasing in size. Silently and motionless in the real world, Miyake opened both eyes in the Astral world, yelling at the top of his astral lungs, HYPER-DRAGON-EYE!"

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

    hide tanaka
    show tanaka red demanding at center
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

    hide shizuma
    show shizuma pink blushed at right
    s "Tanaka-chan, you shouldn't yell at strangers."

    "The platinum blonde girl spoke, her words barely escaping from her bright red face as if she were afraid to talk."

    hide tanaka
    show tanaka red concerned

    "Tanaka's expression changed from enraged to surprised, as she turned to see Shizuma's blushing face."
    "Her escapade was over as she rushed over to Shizuma, grasping her on the shoulders."

    t "Are you Okay, Shizuma? I didn't mean to make you blush. Please don't cry!"

    "she pleaded with Shizuma before she turned towards Miyake."

    hide tanaka
    show tanaka red demanding
    t "We're not done here, I'll talk to you later!"

    hide tanaka
    hide shizuma

    hide miyake
    show miyake blue neutral at left
    "The two scurried away and Miyake sighed, relieved."

    mystery "Actually, you {i}are{/i} done."

    hide miyake
    show miyake blue confused at left
    show aldo purple neutral at right
    "A man's voice echoed. Startled, Miyake turned to see a tall slender man in the shadows."
    "He wore dark flared pants, pointy shined shoes, a partially buttoned white long sleeve shirt with rolled up sleeves, and a black choker."
    "His hair was silver, short and combed, with hair covering part of his face."

    m "Who are you?"

    "Miyake questioned."

    mystery "Allow me to introduce myself."

    "The man said as he stood up from his leaned position against a shadowed wall."

    a "I am Aldo. Fifth pillar of St. Ezreal."

    "he pronounced, before dramatically opening one hand and covering half of his face. His other hand opened, stretched out towards Miyake."

    a "You have been found guilty of cheating on the entrance exam using condemned Astral methods. Now you must die!"

    "Aldo-sensei proclained, his expression going from stone faced to hysterical. His arm stretched towards Miyake."
    "The other students nearby stopped in their tracks, watching as the bizarre instructor made his threats."
    "Miyake knew he was guilty, but what was this about condemned methods?"
    "With a dumbfounded look on his face, he took a step back as he processed what Aldo-sensei had just said."

    hide miyake
    show miyake blue nervous sweat at left
    m "Wh.. What are you talking about? All I did was use HYPER DRAGON EYE!"

    "He rebutted, not minding that the name he had given to his remote viewing projection may come across as ambiguous."

    a "Ah, so that's what you call it. A user of a projection such as that cannot be allowed to exist."

    "Aldo began."

    a "It's a shame, really. A talented Esper such as yourself could have been an asset to this Academy."

    "Aldo went on with a pained look."

    a "It's no matter, the law is the law, and this world has no place for a deviant such as yourself."

    "Aldo said with a bent smile."

    "Miyake was in a state of shock, not fully comprehending the situation."
    "In high school whenever he would use HYPER DRAGON EYE to cheat on a test, he'd get a slap on the wrist and an F."
    "Was a teacher here seriously about to kill him? This must be some kind of sick joke!"

    hide miyake
    show miyake blue grimacing at left
    m "I.. I... WHAT!!?"
    m "None of this makes any sense!"

    "Was the only thing the frozen up Miyake could think to say."
    "Miyake had even read about St. Ezreal's Esper operatives who use projections similar to HYPER DRAGON EYE to scope out the terrain and blueprints of the facilities they're about to raid."

    "HYPER DRAGON EYE isn't a condemned spell, it's practiced at this very academy!"

    a "Prepare youself, heretic."

    play sound "sound/zap.ogg"
    "Aldo warned, as a ball of energy began to form at his palm. The other students began to express concern, one letting out a scream of terror."

    a "Where are my manners, please forgive me."

    "Aldo apologized with a crooked grin, as he used his free hand to reach for the sky."

label aldo:
    scene bg black
    show miyake blue grimacing at left
    show aldo purple neutral at right
    with dissolve
    "As he did so, the blue sky Miyake saw seemed to go black, as well as all the surroundings."
    "Miyake and Aldo were alone in a void."
    "Miyake had read about this projection as well, but never seen it used. Cryptic Isolation."
    "This was Aldo's personal Astral realm, and Miyake had been dragged into it."
    "Much like Miyake's own Astral realm, nothing existed unless Aldo created it within his mind. Aldo was good."
    "This projection isn't simple, and it's something Miyake had never accomplished."

    "The steps to project Cryptic Isolation are in reverse order of HYPER DRAGON EYE. An injection if you will."
    "The process begins with a reality bridge, splicing another person's reality into one's own Astral realm."
    "Injections are the most advanced class of projections because the creator must be aware of the other person's personal reality, seizing it and making it part of their own."
    "Using Cryptic Isolation on a stranger would be impossible, because the creator cannot know the stranger's mindset."
    "The better a creator knows the target, the more effective the injection."
    "Aldo did his research; Any teacher would have what they needed with access to Miyake's educational history."

    a "The other students are innocent, they need not see your death."

    scene bg projection
    show miyake blue grimacing at left
    show aldo purple neutral at right
    with projectionDissolve

    play sound "sound/electricity.ogg"
    "Aldo spoke as the ball of energy before his hand grew larger."
    "Miyake recognized that projection as well-- Ionic Shock."
    "Using the body's natural electricity as a reference, the creator projects a concentrated clone into the world."
    "The process is repeated until an energy ball of the desired size is formed."
    "At small sizes, the ball of electricity is harmless and feels like a static shock."
    "At large sizes, it turns deadly as it's high voltage would devastate a person's nervous system."
    "In the past, Miyake had used this projection to start fires and play pranks, but never maintained concentration for long enough to create a ball as large as the one Aldo was creating."
    "This one was already the size of a watermelon, and it's size was still increasing!"

    a "Any last words?"

    "The instructor asked with a crazed look in his eyes."

    "Miyake wanted to believe that this was a joke, but all signs indicated that Aldo-sensei was serious."
    "Except for one, Aldo's accusation that Miyake had projected a condemned Astral method."
    "HYPER DRAGON EYE, or Remote Viewing is not a condemned method in this Academy or even this region."
    "Miyake concluded that Aldo must be bluffing, and this is his twisted way of punishing a misbehaving student."

    hide miyake
    show miyake blue neutral at left
    "No, this wasn't a punishment at all, it is a test!"
    "Someone finally saw through his apathetic exterior, and recognized his brilliance as an Esper!"
    "This had to be the beginning of the course for the advanced students."

    hide miyake
    show miyake blue neutral at left
    m "Ok then, I'll play along."

    "Miyake said with a mischievous smile. He assumed his fighting stance, a pose he had seen in a Kung-Fu movie."
    "One leg crouched, with the other stretched out and planted on the ground in front. One fist near his face, and the other pointed at his opponent."

    "Aldo looked confused as the size of his Ionic Shock grew larger."

    a "Are you mocking me? This is not a game, this is your execution!"

    "Aldo said as he became increasingly upset."

    a "Now, show me your afraid face!"

    "he yelled, again looking crazed."

    hide miyake
    show miyake blue charming at left
    m "You're pretty good, but I'm on to you."

    "Miyake laughed."

    m "You almost had me thinking you were some kind of psychopath. Anyway, come at me, bro!"

    "Miyake yelled, clenching his fists. Miyake had already figured out his defense against the incoming blast."

    "Aldo's expression revealed his ticked off state. He let out an uncomfortable laugh on the verge of hyperventilation."

    a "You annoying braaaat!"

    "As he let Ionic Shock fly, now the size of an open umbrella."

    hide miyake
    show miyake blue projecting at left
    "Miyake closed his eyes as Aldo's Ionic Shock rapidly moved towards him. His face brought on a look of contentment and he smiled."
    "The ball of energy sped closer, and the black void suddenly returned to sky."

    scene bg uni
    show miyake blue projecting at left
    show aldo purple neutral at right
    with projectionDissolve

    a "What's this!?"

    "Aldo cried as the two were returned to the campus. Students still standing there, looking on as the Ionic Shock almost reached Miyake."

    "Miyake's forward fist became engulfed in the light of Ionic Shock."
    "The energy engulfed his entire arm, then shrunk rapidly as his body seemed to absorb the voltage."

    scene bg uni
    show miyake blue projecting at left
    show aldo purple neutral at right
    with hpunch
    play sound "sound/zap.ogg"
    "A loud \"TZZAP\" sound permeated the air, echoing off the surrounding buildings."

    "Miyake stood there motionless, smoke raising from his charred sleeve. Aldo became overjoyed."

    a "Ahahaha! Take that you little brat, there's nothing left but an empty shell!"

    "Aldo boasted as he flicked his hair, looking up at the sunlight."

    a "Sunlight?"

    "Aldo quickly realized what had just happened. Cryptic Isolation had broken down mid flight of Ionic Shock. Looking back at Miyake, from his drooped head, Aldo could see that Miyake was still smiling."

    hide miyake
    show miyake blue neutral at left
    m "Is that all you've got?"

    "Miyake spoke up, staring straight at Aldo."

    a "What!? You should be dead!"

    "Aldo replied, shocked that his opponent had not been."

    "Opening his fist and clenching it again, Miyake revealed how he had survived the attack. On his hand hit by the blast, he wore a thick metal gauntlet."

    a "A metal glove? But that's just a conductor, you still should have been electrocuted!"

    m "Yes, if it was just a metal glove."

    "Miyake ripped off the sleeve of his charred school uniform, revealing an entire metal shirt below. Then he pulled up his pant leg, exposing metal trousers and a metal boot."

    a "You grounded yourself!"

    "Aldo caught on."

    a "But you were in my Cryptic Isolation, you shouldn't have been able to project at all!"

    m "That's right. A normal Cryptic Isolation compartmentalizes the target's personal reality into the projector's astral realm."

    "Miyake explained."

    m "It wasn't possible for me to project from inside your realm because you created the restriction that I could not project."
    m "It was a perfect situation, really. Leave me completely without defense so you can take me down."
    m "But you forgot one thing."
    m "Because Cryptic Isolation is an injection, a projection which pulls my reality into your own, you first have to have a firm grasp on my personal reality."
    m "You must have done that by researching my past and hypothesizing my personality, but there's only so much school records can tell you about me."

    a "I can tell enough from your school history. I can tell that you suck at sports, you're incompetent at all school subjects, and girls ignore you! That's all I need!"

    "Aldo replied, ticked off."

    "Miyake smiled again."

    m "Yes, you got that right. I'm not good at school or sports. I'm a loser and girls ignore me. But that's just what you can see on the surface level."

    a "Surface level? Anything deeper is nonsense. You're empty inside!"

    m "That's where you're wrong."

    a "Get to the point! How did you escape from my Cryptic Isolation!?"

    hide miyake
    show miyake blue perverted at left

    "Miyake smilled his biggest smile yet."

    m "Shizuma Mizu, 153cm, 90-65-89. Tanaka Aoi, 159cm, 83-59-84. Those two, naked with cat ears pinning you down and nibbling at your chest seemed good enough."

    a "Wha.. "

    "Aldo-sensei was speechless, as he instinctively covered his chest between his partially buttoned shirt."

    m "Easy enough, I just had to imagine something you wouldn't have guessed I'd imagine."

    "Miyake casually explained."

    a "You.. You're so perverted you broke my projection?! That's impossible!"

    hide miyake
    show miyake neutral at left

    "The confrontation had caused quite the stir on campus."
    "Students had gathered around in shock and awe and the fight they had just witnessed."
    "From their point of view, a teacher had approached a student with death threats, the two disappearing for an instant before returning half a second later with a giant ball of electricity striking the student."

    "Miyake prepared to follow up with a punch with a metal gauntlet to Aldo-sensei's face. Before that could happen, another teacher arrived on the scene, breaking up the fight."

    hide aldo
    show aldo purple neutral at center
    show tsubasa yellow angry at right
    mystery "Aldo-sensei"

    "the woman's voice interjected as she spread her arms to block Miyake's view."
    mystery "This is not how we do things at St. Ezreal's."
    mystery "You more than anyone should know we are different than {i}that{/i} place."

    "Gritting his teeth, Aldo took a step back, relaxing his stance and closing his eyes."

    a "Tsubasa-sama, this one used Nemesis of Time. {b}YOU{/b} more than anyone should know he must be dealt with."

    tsu "And he will. But using that transgression as an excuse to go off killing a new student is unacceptable."

    "The teacher barked back."
    "Aldo looked away."

    a "{i}Tsk{/i}"

    "Marth looked up at the woman in front of him."

    "{b}[TO BE CONTINUED...]{/b}"

    return
