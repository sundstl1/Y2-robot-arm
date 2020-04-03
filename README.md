# Y2 robot arm simulator

432021 robot arm simulation project for the course CS-A1121 Ohjelmointi Y2

1. Mitä ominaisuuksia olet jo toteuttanut projektiisi?
    * The project currently conforms to "Iteration 2".
    * A specification for what that means can be found on page 3 in the project plan.

2. Käyttöohje

  - Voiko ohjelmaa jo ajaa? (kyllä/ei)
    * yes

  - Kuinka ohjelma käynnistetään?
    * The program can be run by executing main.py in the src/ folder
    * On my system that means running the command "python main.py"

  - Mitä sillä voi tässä vaiheessa tehdä?
    * The program shows a robot arm with an arbitrary number of joints.
    * Joint angles may be manipulated using sliders.
    * Manipulations to individual joints are handled in separate threads, allowing multiple joints to rotate at once.
    * A joint will always choose the shortest rotation direction to its set angle.
    * There is no physics simulation. movement speed is simply limited as a max change in angle / timeunit.
    * The coordinates of the arm endpoint is shown at the top of the window (origo is a the root of the arm).
    * The amount of joints and arm lengths may be easily edited in main.py (lines 13-23)



3. Aikataulu

  - Kuinka paljon olet jo käyttänyt aikaa projektiin?
    * I have currently invested around 15-20 hours in the project.

  - Onko ilmennyt muutoksia suunnitelman aikatauluun?
    * I ended up skipping Iteration 1 and going straight to Iteration 2 (see project plan page 3).
    * This is because it ended up being just as simple to implement Iteration 2 straight away compared to doing iteration 1 first.
 
4. Muuta

  - Onko ilmaantunut erityisiä ongelmia?
    * I planned to complete theproject using test driven development.
    * Unfortunately I haven't found a compelling way to test the UI though.
    * I also ended up not doing test cases for thread handling beforehand due to just wanting to get the features done.
    * I should implement some tests for this.

  - Oletko joutunut tekemään muutoksia suunnitelmaasi?
    * Nothing noticeable. Some small changes to file structure but I would have been very surprised if that didn't happen.
    * The project is currently heavily derived from robots and linked_list excercises earlier this course.
    * I expect more deviation now that the basic functionality is implemented.