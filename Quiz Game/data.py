import requests

logo = """
 ______  __ __    ___       ___   __ __  ____  _____       ____   ____  ___ ___    ___ 
|      ||  |  |  /  _]     /   \ |  |  ||    ||     |     /    | /    ||   |   |  /  _]
|      ||  |  | /  [_     |     ||  |  | |  | |__/  |    |   __||  o  || _   _ | /  [_ 
|_|  |_||  _  ||    _]    |  Q  ||  |  | |  | |   __|    |  |  ||     ||  \_/  ||    _]
  |  |  |  |  ||   [_     |     ||  :  | |  | |  /  |    |  |_ ||  _  ||   |   ||   [_ 
  |  |  |  |  ||     |    |     ||     | |  | |     |    |     ||  |  ||   |   ||     |
  |__|  |__|__||_____|     \__,_| \__,_||____||_____|    |___,_||__|__||___|___||_____|

"""

# Alternate way of gaining api
# parameters = {
#     "amount": 10,
#     "type": "boolean"
# }
#
# response = requests.get(url="https://opentbd.com/api.php", params=parameters)
# response.raise_for_status()
# data = response.json()
# question_data = data["results"]

question_data = [
    {"question": "A slug's blood is green.", "correct_answer": "True"},
    {"question": "The loudest animal is the African Elephant.", "correct_answer": "False"},
    {"question": "Approximately one quarter of human bones are in the feet.", "correct_answer": "True"},
    {"question": "The total surface area of a human lungs is the size of a football pitch.", "correct_answer": "True"},
    {"question": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it "
                 "home to eat.", "correct_answer": "True"},
    {"question": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "correct_answer": "False"},
    {"question": "It is illegal to pee in the Ocean in Portugal.", "correct_answer": "True"},
    {"question": "You can lead a cow down stairs but not up stairs.", "correct_answer": "False"},
    {"question": "Google was originally called 'Backrub'.", "correct_answer": "True"},
    {"question": "Buzz Aldrin's mother's maiden name was 'Moon'.", "correct_answer": "True"},
    {"question": "No piece of square dry paper can be folded in half more than 7 times.", "correct_answer": "False"},
    {"question": "A few ounces of chocolate can to kill a small dog.", "correct_answer": "True"}
]

science_and_nature = [{"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "The Neanderthals were a direct ancestor of modern humans.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "The Doppler effect applies to light.", "correct_answer": "True",
                       "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Hippopotomonstrosesquippedaliophobia is the irrational fear of long words.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "The planet Mars has two moons orbiting it.", "correct_answer": "True",
                       "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Steel is an alloy of Iron and Carbon.", "correct_answer": "True",
                       "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Like with the Neanderthals, Homo sapiens sapiens also interbred with the Denisovans.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "A defibrillator is used to start up a heartbeat once a heart has stopped beating.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Shrimp can swim backwards.", "correct_answer": "True",
                       "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Type 1 diabetes is a result of the liver working improperly.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                       "question": "Salt is 100% composed of Sodium.", "correct_answer": "False",
                       "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                       "question": "An atom contains a nucleus.", "correct_answer": "True",
                       "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Centripedal force is an apparent force that acts outward on a body moving around a center, arising from the body&#039;s inertia.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "In the periodic table, Potassium&#039;s symbol is the letter K.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                       "question": "An Astronomical Unit is the distance between Earth and the Moon.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "hard",
                       "question": "The chemical element Lithium is named after the country of Lithuania.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "hard",
                       "question": "The value of one Calorie is different than the value of one calorie.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                       "question": "Celiac Disease is a disease that effects the heart, causing those effected to be unable to eat meat.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                       "question": "Psychology is the science of behavior and mind.", "correct_answer": "True",
                       "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Pneumonoultramicroscopicsilicovolcanoconiosis is a synonym for the disease known as silicosis.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                       "question": "Water always boils at 100&deg;C, 212&deg;F, 373.15K, no matter where you are.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "Sound can travel through a vacuum.", "correct_answer": "False",
                       "incorrect_answers": ["True"]},
                      {"category": "Science & Nature", "type": "boolean", "difficulty": "medium",
                       "question": "The most frequent subconscious activity repeated by the human body is blinking.",
                       "correct_answer": "False", "incorrect_answers": ["True"]}
                      ]

mythology = [
    {"category": "Mythology", "type": "boolean", "difficulty": "easy",
     "question": "In Norse mythology, Thor once dressed as a woman.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "easy",
     "question": "According to Greek Mythology, Zeus can control lightning.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "medium",
     "question": "According to Norse mythology, Loki is a mother.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "medium",
     "question": "The Japanese god Izanagi successfully returned his wife Izanami from the Underworld.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "hard",
     "question": "Rannamaari was a sea demon that haunted the people of the Maldives and had to be appeased monthly with the sacrifice of a virgin girl.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "medium",
     "question": "In Greek mythology, Hera is the goddess of harvest.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "easy",
     "question": "According to Greek Mythology, Atlas was an Olympian God.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "medium",
     "question": "The Roman god 'Jupiter' was first known as 'Zeus' to the Greeks.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "easy",
     "question": "A wyvern is the same as a dragon.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Mythology", "type": "boolean", "difficulty": "hard",
     "question": "Janus was the Roman god of doorways and passageways.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]

animal = [
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "The Axolotl is an amphibian that can spend its whole life in a larval state.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "The Ceratosaurus, a dinosaur known for having a horn on the top of its nose, is also known to be a decendent of the Tyrannosaurus Rex.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "An octopus can fit through any hole larger than its beak.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "A slug&rsquo;s blood is green.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "Kangaroos keep food in their pouches next to their children.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "'Kamea' the Gilbertese Islander word for dog, is derived from the English phrase 'Come here!'",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "A bear does NOT defecate during hibernation. ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "In 2016, the IUCN reclassified the status of Giant Pandas from endangered to vulnerable.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "The average lifespan of a wildcat is only around 5-6 years. ",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "Rabbits are rodents.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "A flock of crows is known as a homicide.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "The Platypus is a mammal.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "A caterpillar has more muscles than humans do.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "Cats have whiskers under their legs.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "The Killer Whale is considered a type of dolphin.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "Finnish Lapphund dogs were used for herding reindeer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "Tigers have one colour of skin despite the stripey fur.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "Rabbits can see what&#039;s behind themselves without turning their heads.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "You can tell the age of a ladybird by counting the spots on his back.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "Rabbits are carnivores.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "The internet browser Firefox is named after the Red Panda.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "The freshwater amphibian, the Axolotl, can regrow it&#039;s limbs.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]

mathematics = [
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "The Pythagorean theorem states that the square of the hypotenuse is equal to the product of the squares of the other two sides.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "The proof for the Chinese Remainder Theorem used in Number Theory was NOT developed by its first publisher, Sun Tzu.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
     "question": "A universal set, or a set that contains all sets, exists.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "111,111,111 x 111,111,111 = 12,345,678,987,654,321",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
     "question": "The &#039;Squaring the Circle&#039; problem is solvable.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
     "question": "The binary number '101001101' is equivalent to the Decimal number &quot;334&quot;",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
     "question": "If you could fold a piece of paper in half 50 times, it's; thickness will be 3\/4th the distance from the Earth to the Sun.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "E = MC3", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "A 'Millinillion' is a real number.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
     "question": "In Topology, the complement of an open set is a closed set.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "hard",
     "question": "L'Hôpital was the mathematician who created the homonymous rule that uses derivatives to evaluate limits with indeterminations.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "You can square root a negative number with an imaginary number &quot;i&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
     "question": "An isosceles triangle has two sides of equal length as opposed to three.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
     "question": "A scalene triangle has two sides of equal length.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
     "question": "An equilateral triangle always has every angle measuring 60&deg;.",
     "correct_answer": "True", "incorrect_answers": ["False"]}
]

sports = [
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "Peyton Manning retired after winning Super Bowl XLIX.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Skateboarding will be included in the 2020 Summer Olympics in Tokyo.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "The Olympics tennis court is a giant green screen.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "Roger Federer is a famous soccer player.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Formula E is an auto racing series that uses hybrid electric race cars.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "In association football, or soccer, a corner kick is when the game restarts after someone scores a goal.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "In Rugby League, performing a &quot;40-20&quot; is punished by a free kick for the opposing team.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Wilt Chamberlain scored his infamous 100-point-game against the New York Knicks in 1962.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "In 2008, Usain Bolt set the world record for the 100 meters with one shoelace untied.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "ATP tennis hosted several tournaments on carpet court before being replaced to reduce injuries.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "There are a total of 20 races in Formula One 2016 season.",
     "correct_answer": "False", "incorrect_answers": ["True"]}
]

geography = [
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Seoul is the capital of North Korea.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The flag of South Africa features 7 colours.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Greenland is almost as big as Africa.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "A group of islands is called an &#039;archipelago&#039;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The surface area of Russia is slightly larger than that of the dwarf planet Pluto.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "The Republic of Malta is the smallest microstate worldwide.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "There are no roads in\/out of Juneau, Alaska.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "San Marino is the only country completely surrounded by another country.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Israel is 7 hours ahead of New York.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "There is a city called Rome in every continent on Earth.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Alaska is the largest state in the United States.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Vietnam is the only country in the world that starts with V. ",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Gothenburg is the capital of Sweden.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "Ottawa is the capital of Canada.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "There exists an island named &quot;Java&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The capital of the US State Ohio is the city of Chillicothe.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Japan has left-hand side traffic.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "New Haven is the capital city of the state of Connecticut in the United States.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "hard",
     "question": "The two largest ethnic groups of Belgium are Flemish and Walloon. ",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The title of the 1969 film &quot;Krakatoa, East_of Java&quot; is incorrect, as Krakatoa is in fact west of Java.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "Is Tartu the capital of Estonia?", "correct_answer": "False",
     "incorrect_answers": ["True"]}
]
