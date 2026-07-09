"""
Question bank for the Quiz App.
Each question has: id, category, difficulty, question (EN), question_hi (HI),
options (EN), options_hi (HI), correct_index, explanation.
"""

QUESTIONS = [
    # ── SCIENCE ──────────────────────────────────────────────────────────
    {
        "id": 1, "category": "Science", "difficulty": "easy",
        "question": "What is the chemical symbol for water?",
        "question_hi": "पानी का रासायनिक प्रतीक क्या है?",
        "options": ["H2O", "CO2", "NaCl", "O2"],
        "options_hi": ["H2O", "CO2", "NaCl", "O2"],
        "correct_index": 0,
        "explanation": "Water is H₂O — two hydrogen atoms bonded to one oxygen atom."
    },
    {
        "id": 2, "category": "Science", "difficulty": "easy",
        "question": "How many planets are in our Solar System?",
        "question_hi": "हमारे सौर मंडल में कितने ग्रह हैं?",
        "options": ["7", "8", "9", "10"],
        "options_hi": ["7", "8", "9", "10"],
        "correct_index": 1,
        "explanation": "There are 8 planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune."
    },
    {
        "id": 3, "category": "Science", "difficulty": "medium",
        "question": "What is the speed of light in a vacuum?",
        "question_hi": "निर्वात में प्रकाश की गति क्या है?",
        "options": ["3×10⁸ m/s", "3×10⁶ m/s", "3×10¹⁰ m/s", "3×10⁴ m/s"],
        "options_hi": ["3×10⁸ m/s", "3×10⁶ m/s", "3×10¹⁰ m/s", "3×10⁴ m/s"],
        "correct_index": 0,
        "explanation": "The speed of light is approximately 299,792,458 m/s ≈ 3×10⁸ m/s."
    },
    {
        "id": 4, "category": "Science", "difficulty": "medium",
        "question": "Which element has the atomic number 79?",
        "question_hi": "किस तत्व की परमाणु संख्या 79 है?",
        "options": ["Silver", "Platinum", "Gold", "Copper"],
        "options_hi": ["चाँदी", "प्लेटिनम", "सोना", "तांबा"],
        "correct_index": 2,
        "explanation": "Gold (Au) has atomic number 79."
    },
    {
        "id": 5, "category": "Science", "difficulty": "hard",
        "question": "What is the Heisenberg Uncertainty Principle about?",
        "question_hi": "हाइजेनबर्ग अनिश्चितता सिद्धांत किसके बारे में है?",
        "options": [
            "Energy and mass", "Position and momentum",
            "Charge and spin", "Temperature and pressure"
        ],
        "options_hi": [
            "ऊर्जा और द्रव्यमान", "स्थिति और संवेग",
            "आवेश और चक्रण", "तापमान और दबाव"
        ],
        "correct_index": 1,
        "explanation": "It states that position and momentum of a particle cannot both be known precisely simultaneously."
    },
    {
        "id": 6, "category": "Science", "difficulty": "hard",
        "question": "Which subatomic particle has no electric charge?",
        "question_hi": "कौन सा उप-परमाणु कण विद्युत आवेश रहित है?",
        "options": ["Proton", "Electron", "Neutron", "Positron"],
        "options_hi": ["प्रोटॉन", "इलेक्ट्रॉन", "न्यूट्रॉन", "पॉज़िट्रॉन"],
        "correct_index": 2,
        "explanation": "Neutrons carry no electric charge; they reside in the atomic nucleus alongside protons."
    },

    # ── HISTORY ──────────────────────────────────────────────────────────
    {
        "id": 7, "category": "History", "difficulty": "easy",
        "question": "In which year did World War II end?",
        "question_hi": "द्वितीय विश्व युद्ध किस वर्ष समाप्त हुआ?",
        "options": ["1943", "1944", "1945", "1946"],
        "options_hi": ["1943", "1944", "1945", "1946"],
        "correct_index": 2,
        "explanation": "World War II ended in 1945 with the surrender of Germany (May) and Japan (September)."
    },
    {
        "id": 8, "category": "History", "difficulty": "easy",
        "question": "Who was the first President of the United States?",
        "question_hi": "संयुक्त राज्य अमेरिका के पहले राष्ट्रपति कौन थे?",
        "options": ["John Adams", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
        "options_hi": ["जॉन एडम्स", "थॉमस जेफरसन", "जॉर्ज वाशिंगटन", "बेंजामिन फ्रैंकलिन"],
        "correct_index": 2,
        "explanation": "George Washington was inaugurated as the first US President on April 30, 1789."
    },
    {
        "id": 9, "category": "History", "difficulty": "medium",
        "question": "The Great Wall of China was primarily built to protect against which group?",
        "question_hi": "चीन की महान दीवार मुख्य रूप से किस समूह से सुरक्षा के लिए बनाई गई थी?",
        "options": ["Mongols", "Romans", "Persians", "Vikings"],
        "options_hi": ["मंगोल", "रोमन", "फारसी", "वाइकिंग"],
        "correct_index": 0,
        "explanation": "The Great Wall was built to defend against raids by Mongol and other nomadic tribes."
    },
    {
        "id": 10, "category": "History", "difficulty": "medium",
        "question": "Who wrote the Declaration of Independence?",
        "question_hi": "स्वतंत्रता की घोषणा किसने लिखी?",
        "options": ["George Washington", "Thomas Jefferson", "John Adams", "James Madison"],
        "options_hi": ["जॉर्ज वाशिंगटन", "थॉमस जेफरसन", "जॉन एडम्स", "जेम्स मैडिसन"],
        "correct_index": 1,
        "explanation": "Thomas Jefferson was the principal author of the Declaration of Independence in 1776."
    },
    {
        "id": 11, "category": "History", "difficulty": "hard",
        "question": "Which ancient wonder was located in Alexandria, Egypt?",
        "question_hi": "अलेक्जेंड्रिया, मिस्र में कौन सा प्राचीन आश्चर्य स्थित था?",
        "options": [
            "Colossus of Rhodes", "Lighthouse of Alexandria",
            "Hanging Gardens", "Temple of Artemis"
        ],
        "options_hi": [
            "रोड्स का कोलोसस", "अलेक्जेंड्रिया का प्रकाशस्तंभ",
            "बेबीलोन के झूलते बाग", "आर्टेमिस का मंदिर"
        ],
        "correct_index": 1,
        "explanation": "The Lighthouse of Alexandria (Pharos) stood on the island of Pharos in Alexandria."
    },

    # ── GEOGRAPHY ────────────────────────────────────────────────────────
    {
        "id": 12, "category": "Geography", "difficulty": "easy",
        "question": "What is the capital of France?",
        "question_hi": "फ्रांस की राजधानी क्या है?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "options_hi": ["बर्लिन", "मैड्रिड", "पेरिस", "रोम"],
        "correct_index": 2,
        "explanation": "Paris has been the capital of France since the late 10th century."
    },
    {
        "id": 13, "category": "Geography", "difficulty": "easy",
        "question": "Which is the longest river in the world?",
        "question_hi": "विश्व की सबसे लंबी नदी कौन सी है?",
        "options": ["Amazon", "Yangtze", "Nile", "Mississippi"],
        "options_hi": ["अमेज़न", "यांग्त्ज़ी", "नील", "मिसिसिपी"],
        "correct_index": 2,
        "explanation": "The Nile River (~6,650 km) is generally considered the world's longest river."
    },
    {
        "id": 14, "category": "Geography", "difficulty": "medium",
        "question": "Which country has the most natural lakes?",
        "question_hi": "किस देश में सबसे अधिक प्राकृतिक झीलें हैं?",
        "options": ["USA", "Russia", "Canada", "Brazil"],
        "options_hi": ["USA", "रूस", "कनाडा", "ब्राज़ील"],
        "correct_index": 2,
        "explanation": "Canada has over 2 million lakes, more than any other country."
    },
    {
        "id": 15, "category": "Geography", "difficulty": "medium",
        "question": "What is the smallest country in the world by area?",
        "question_hi": "क्षेत्रफल की दृष्टि से विश्व का सबसे छोटा देश कौन सा है?",
        "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"],
        "options_hi": ["मोनाको", "सैन मैरिनो", "वेटिकन सिटी", "लिकटेंस्टाइन"],
        "correct_index": 2,
        "explanation": "Vatican City (0.44 km²) is the world's smallest country."
    },
    {
        "id": 16, "category": "Geography", "difficulty": "hard",
        "question": "Which African country has the most pyramids?",
        "question_hi": "किस अफ्रीकी देश में सबसे अधिक पिरामिड हैं?",
        "options": ["Egypt", "Sudan", "Libya", "Ethiopia"],
        "options_hi": ["मिस्र", "सूडान", "लीबिया", "इथियोपिया"],
        "correct_index": 1,
        "explanation": "Sudan (ancient Nubia) has over 200–255 pyramids, more than Egypt's ~130."
    },

    # ── TECHNOLOGY ───────────────────────────────────────────────────────
    {
        "id": 17, "category": "Technology", "difficulty": "easy",
        "question": "What does 'HTML' stand for?",
        "question_hi": "'HTML' का पूर्ण रूप क्या है?",
        "options": [
            "HyperText Markup Language",
            "HighText Machine Language",
            "Hyperlink and Text Markup Language",
            "HyperText Modeling Language"
        ],
        "options_hi": [
            "हाइपरटेक्स्ट मार्कअप लैंग्वेज",
            "हाई टेक्स्ट मशीन लैंग्वेज",
            "हाइपरलिंक टेक्स्ट मार्कअप लैंग्वेज",
            "हाइपरटेक्स्ट मॉडलिंग लैंग्वेज"
        ],
        "correct_index": 0,
        "explanation": "HTML stands for HyperText Markup Language, the standard for web pages."
    },
    {
        "id": 18, "category": "Technology", "difficulty": "easy",
        "question": "Who is the co-founder of Apple Inc.?",
        "question_hi": "Apple Inc. के सह-संस्थापक कौन हैं?",
        "options": ["Bill Gates", "Steve Jobs", "Elon Musk", "Mark Zuckerberg"],
        "options_hi": ["बिल गेट्स", "स्टीव जॉब्स", "एलन मस्क", "मार्क जुकरबर्ग"],
        "correct_index": 1,
        "explanation": "Steve Jobs, Steve Wozniak, and Ronald Wayne co-founded Apple on April 1, 1976."
    },
    {
        "id": 19, "category": "Technology", "difficulty": "medium",
        "question": "What does CPU stand for?",
        "question_hi": "CPU का पूर्ण रूप क्या है?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Core Processing Unit"
        ],
        "options_hi": [
            "सेंट्रल प्रोसेसिंग यूनिट",
            "कंप्यूटर पर्सनल यूनिट",
            "सेंट्रल प्रोग्राम यूटिलिटी",
            "कोर प्रोसेसिंग यूनिट"
        ],
        "correct_index": 0,
        "explanation": "CPU — Central Processing Unit — is the primary component of a computer that executes instructions."
    },
    {
        "id": 20, "category": "Technology", "difficulty": "medium",
        "question": "Which programming language is known as the 'language of the web'?",
        "question_hi": "कौन सी प्रोग्रामिंग भाषा 'वेब की भाषा' के रूप में जानी जाती है?",
        "options": ["Python", "Java", "JavaScript", "Ruby"],
        "options_hi": ["पायथन", "जावा", "जावास्क्रिप्ट", "रूबी"],
        "correct_index": 2,
        "explanation": "JavaScript runs natively in every web browser and is the backbone of interactive web pages."
    },
    {
        "id": 21, "category": "Technology", "difficulty": "hard",
        "question": "What is the time complexity of binary search?",
        "question_hi": "बाइनरी सर्च की समय जटिलता क्या है?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
        "options_hi": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
        "correct_index": 2,
        "explanation": "Binary search halves the search space each step, giving O(log n) time complexity."
    },
    {
        "id": 22, "category": "Technology", "difficulty": "hard",
        "question": "In networking, what does 'DNS' stand for?",
        "question_hi": "नेटवर्किंग में 'DNS' का अर्थ क्या है?",
        "options": [
            "Dynamic Network Service",
            "Domain Name System",
            "Data Node Server",
            "Distributed Network Storage"
        ],
        "options_hi": [
            "डायनामिक नेटवर्क सर्विस",
            "डोमेन नेम सिस्टम",
            "डेटा नोड सर्वर",
            "डिस्ट्रीब्यूटेड नेटवर्क स्टोरेज"
        ],
        "correct_index": 1,
        "explanation": "DNS (Domain Name System) translates human-readable domain names into IP addresses."
    },

    # ── MATHEMATICS ──────────────────────────────────────────────────────
    {
        "id": 23, "category": "Mathematics", "difficulty": "easy",
        "question": "What is the value of π (pi) to two decimal places?",
        "question_hi": "π (पाई) का दो दशमलव स्थानों तक मान क्या है?",
        "options": ["3.12", "3.14", "3.16", "3.18"],
        "options_hi": ["3.12", "3.14", "3.16", "3.18"],
        "correct_index": 1,
        "explanation": "π ≈ 3.14159… so to two decimal places it is 3.14."
    },
    {
        "id": 24, "category": "Mathematics", "difficulty": "easy",
        "question": "What is the square root of 144?",
        "question_hi": "144 का वर्गमूल क्या है?",
        "options": ["11", "12", "13", "14"],
        "options_hi": ["11", "12", "13", "14"],
        "correct_index": 1,
        "explanation": "12 × 12 = 144, so √144 = 12."
    },
    {
        "id": 25, "category": "Mathematics", "difficulty": "medium",
        "question": "What is the sum of interior angles of a triangle?",
        "question_hi": "त्रिभुज के आंतरिक कोणों का योग क्या है?",
        "options": ["90°", "180°", "270°", "360°"],
        "options_hi": ["90°", "180°", "270°", "360°"],
        "correct_index": 1,
        "explanation": "The sum of interior angles of any triangle is always 180°."
    },
    {
        "id": 26, "category": "Mathematics", "difficulty": "medium",
        "question": "If a rectangle has length 8 and width 5, what is its area?",
        "question_hi": "यदि एक आयत की लंबाई 8 और चौड़ाई 5 है, तो उसका क्षेत्रफल क्या है?",
        "options": ["26", "40", "13", "45"],
        "options_hi": ["26", "40", "13", "45"],
        "correct_index": 1,
        "explanation": "Area = length × width = 8 × 5 = 40."
    },
    {
        "id": 27, "category": "Mathematics", "difficulty": "hard",
        "question": "What is the derivative of sin(x)?",
        "question_hi": "sin(x) का अवकलज क्या है?",
        "options": ["-cos(x)", "cos(x)", "-sin(x)", "tan(x)"],
        "options_hi": ["-cos(x)", "cos(x)", "-sin(x)", "tan(x)"],
        "correct_index": 1,
        "explanation": "d/dx [sin(x)] = cos(x). This is a fundamental calculus identity."
    },
    {
        "id": 28, "category": "Mathematics", "difficulty": "hard",
        "question": "What is the value of 0! (zero factorial)?",
        "question_hi": "0! (शून्य का क्रमगुणित) का मान क्या है?",
        "options": ["0", "1", "Undefined", "Infinity"],
        "options_hi": ["0", "1", "अपरिभाषित", "अनंत"],
        "correct_index": 1,
        "explanation": "By convention, 0! = 1. This is consistent with the recurrence n! = n×(n-1)!."
    },

    # ── GENERAL KNOWLEDGE ────────────────────────────────────────────────
    {
        "id": 29, "category": "General Knowledge", "difficulty": "easy",
        "question": "How many colors are there in a rainbow?",
        "question_hi": "इंद्रधनुष में कितने रंग होते हैं?",
        "options": ["5", "6", "7", "8"],
        "options_hi": ["5", "6", "7", "8"],
        "correct_index": 2,
        "explanation": "VIBGYOR — Violet, Indigo, Blue, Green, Yellow, Orange, Red — 7 colors."
    },
    {
        "id": 30, "category": "General Knowledge", "difficulty": "easy",
        "question": "Which is the largest ocean on Earth?",
        "question_hi": "पृथ्वी पर सबसे बड़ा महासागर कौन सा है?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "options_hi": ["अटलांटिक", "हिंद", "आर्कटिक", "प्रशांत"],
        "correct_index": 3,
        "explanation": "The Pacific Ocean covers more than 165 million km², about one-third of Earth's surface."
    },
    {
        "id": 31, "category": "General Knowledge", "difficulty": "medium",
        "question": "What is the hardest natural substance on Earth?",
        "question_hi": "पृथ्वी पर सबसे कठोर प्राकृतिक पदार्थ कौन सा है?",
        "options": ["Iron", "Quartz", "Diamond", "Titanium"],
        "options_hi": ["लोहा", "क्वार्ट्ज़", "हीरा", "टाइटेनियम"],
        "correct_index": 2,
        "explanation": "Diamond rates 10 on the Mohs hardness scale — the highest possible."
    },
    {
        "id": 32, "category": "General Knowledge", "difficulty": "medium",
        "question": "Which country invented the printing press?",
        "question_hi": "प्रिंटिंग प्रेस का आविष्कार किस देश ने किया?",
        "options": ["China", "Germany", "England", "France"],
        "options_hi": ["चीन", "जर्मनी", "इंग्लैंड", "फ्रांस"],
        "correct_index": 1,
        "explanation": "Johannes Gutenberg invented the movable-type printing press in Germany around 1440."
    },
    {
        "id": 33, "category": "General Knowledge", "difficulty": "hard",
        "question": "What is the rarest blood type?",
        "question_hi": "सबसे दुर्लभ रक्त प्रकार कौन सा है?",
        "options": ["AB-", "O-", "B-", "A-"],
        "options_hi": ["AB-", "O-", "B-", "A-"],
        "correct_index": 0,
        "explanation": "AB- is the rarest blood type, found in less than 1% of the world's population."
    },

    # ── SPORTS ───────────────────────────────────────────────────────────
    {
        "id": 34, "category": "Sports", "difficulty": "easy",
        "question": "How many players are on a standard soccer team on the field?",
        "question_hi": "मैदान पर एक मानक फुटबॉल टीम में कितने खिलाड़ी होते हैं?",
        "options": ["9", "10", "11", "12"],
        "options_hi": ["9", "10", "11", "12"],
        "correct_index": 2,
        "explanation": "Each soccer team fields 11 players, including the goalkeeper."
    },
    {
        "id": 35, "category": "Sports", "difficulty": "easy",
        "question": "In which sport would you perform a 'slam dunk'?",
        "question_hi": "किस खेल में 'स्लैम डंक' किया जाता है?",
        "options": ["Volleyball", "Basketball", "Tennis", "Baseball"],
        "options_hi": ["वॉलीबॉल", "बास्केटबॉल", "टेनिस", "बेसबॉल"],
        "correct_index": 1,
        "explanation": "A slam dunk is a basketball shot where the player jumps and forces the ball through the hoop."
    },
    {
        "id": 36, "category": "Sports", "difficulty": "medium",
        "question": "How often are the Summer Olympics held?",
        "question_hi": "ग्रीष्मकालीन ओलंपिक कितने वर्षों में एक बार होते हैं?",
        "options": ["2 years", "3 years", "4 years", "5 years"],
        "options_hi": ["2 वर्ष", "3 वर्ष", "4 वर्ष", "5 वर्ष"],
        "correct_index": 2,
        "explanation": "The Summer Olympics are held every 4 years."
    },
    {
        "id": 37, "category": "Sports", "difficulty": "hard",
        "question": "Who holds the record for the most Grand Slam tennis titles (men's)?",
        "question_hi": "पुरुष टेनिस में सर्वाधिक ग्रैंड स्लैम खिताब किसके नाम है?",
        "options": ["Pete Sampras", "Roger Federer", "Rafael Nadal", "Novak Djokovic"],
        "options_hi": ["पीट सैम्प्रास", "रोजर फेडरर", "राफेल नडाल", "नोवाक जोकोविच"],
        "correct_index": 3,
        "explanation": "Novak Djokovic holds the men's record with 24 Grand Slam singles titles (as of 2024)."
    },
]

CATEGORIES = sorted(set(q["category"] for q in QUESTIONS))
DIFFICULTIES = ["easy", "medium", "hard"]

CATEGORY_ICONS = {
    "Science": "🔬",
    "History": "🏛️",
    "Geography": "🌍",
    "Technology": "💻",
    "Mathematics": "📐",
    "General Knowledge": "🧠",
    "Sports": "🏆",
}

DIFFICULTY_INFO = {
    "easy":   {"label": "Easy",   "label_hi": "आसान",     "color": "success", "time": 20},
    "medium": {"label": "Medium", "label_hi": "मध्यम",    "color": "warning", "time": 25},
    "hard":   {"label": "Hard",   "label_hi": "कठिन",     "color": "danger",  "time": 30},
}
