import random

R_EATING = "I don't eat anything just roam around my code!"
R_ADVICE = "I have no experience, I could only reflect some predefined junks; Prefer someone elder!"
R_Born = "Ask Sayan and Sanidhya!They know the secret ingredient."
R_Play= "I am not made for playing. I \'m just a Bot. That the sad truth."
def unknown():
    response = ["Could you please re-order that? ",
                "Is that in Bot-lish?I can\'t decipher that",
                "This is not in my Dictionary. Please Retry",
                "What does that mean?"][
        random.randrange(4)]
    return response

def joke():
    response = ["Why did the robot fall in love with the magnet?\nHe couldn’t resist the magnetic attraction!",
                "Why do robots make bad teachers? They just drone on and on!",
                "How do doggy robots do? They byte!",
                "What do you call a robot who always runs into the wall? Wall-E!",
                'Where do Cauliflowers hangout?....The Gobi Desert!'
                ][
        random.randrange(5)]
    return response

def fact():
    response = ["The world’s oldest wooden wheel has been around for more than 5,000 years",
                "There are over 6,500 languages spoken in the world.",
                "Dead skin cells are a main ingredient in household dust",
                "The bumblebee bat is the world’s smallest mammal",
                "You are a Human.Gotcha!"
                ][
        random.randrange(5)]
    return response