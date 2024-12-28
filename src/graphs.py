PERSON_KNOWS_PERSON_GRAPH = {
    "Julia Morrongiello": {
        "nodes": [
            ("Julia Morrongiello", {"label": "Julia Morrongiello (Person)", "size": 25, "color": "lightblue"}),
            ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 25, "color": "lightblue"}),
            ("Luca Bocchio", {"label": "Luca Bocchio (Person)", "size": 35, "color": "lightblue"}),
            ("Stefano Bernardi", {"label": "Stefano Bernardi (Person)", "size": 20, "color": "lightblue"}),
            ("2100 Ventures", {"label": "2100 Ventures (Company)", "size": 20, "color": "green"}),
            ("Accel", {"label": "Accel (Company)", "size": 20, "color": "green"}),
            ("Saber", {"label": "Saber (Startup)", "size": 30, "color": "green"}),
            ("Fintech", {"label": "Fintech (Industry)", "size": 18, "color": "pink"}),
            ("Fintech Guild", {"label": "Fintech Guild (Community)", "size": 18, "color": "red"})   
        ],
        "edges": [
            ("Andrea Gurnari", "2100 Ventures", "Works At"),
            ("Stefano Bernardi", "2100 Ventures", "Works At"),
            ("Luca Bocchio", "Accel", "Works At"),
            ("Julia Morrongiello", "Accel", "Works At"),
            ("Andrea Gurnari", "Luca Bocchio", "Knows"),
            ("Andrea Gurnari", "Stefano Bernardi", "Knows"),
            ("Stefano Bernardi", "Julia Morrongiello", "Knows"),
            ("Luca Bocchio", "Julia Morrongiello", "Knows"),
            ("2100 Ventures", "Saber", "Has Invested In"),
            ("Andrea Gurnari", "Saber", "Has Invested In"),
            ("Andrea Gurnari", "Fintech Guild", "Belongs To"),
            ("Julia Morrongiello", "Fintech Guild", "Belongs To"),
            ("Luca Bocchio", "Fintech Guild", "Belongs To"),
            ("Andrea Gurnari", "Fintech", "Has Invested In"),
            ("Julia Morrongiello", "Fintech", "Has Invested In")
        ]
    },
    "Pietro Bezza": {
        "nodes": [
            ("Pietro Bezza", {"label": "Pietro Bezza (Person)", "size": 25, "color": "lightblue"}),
            ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 25, "color": "lightblue"}),
            ("Connect Ventures", {"label": "Connect Ventures (Company)", "size": 20, "color": "green"}),
        ],
        "edges": [
            ("Andrea Gurnari", "Connect Ventures", "Worked At"),
            ("Pietro Bezza", "Connect Ventures", "Works At"),
            ("Andrea Gurnari", "Pietro Bezza", "Knows"),
        ]
    },
    "Akash Bajwa": {
        "nodes": [
            ("Akash Bajwa", {"label": "Akash Bajwa (Person)", "size": 25, "color": "lightblue"}),
            ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 25, "color": "lightblue"}),
        ],
        "edges": [
            ("Andrea Gurnari", "Akash Bajwa", "Knows"),
        ]
    },
    "Barbod Namini": {
         "nodes": [
            ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 25, "color": "lightblue"}),
            ("Philippe Teixeira da Mota", {"label": "Philippe Teixeira da Mota (Person)", "size": 35, "color": "lightblue"}),
            ("Qonto", {"label": "Qonto (Organization)", "size": 20, "color": "green"}),
            ("Barbod Namini", {"label": "Barbod Namini (Person)", "size": 25, "color": "lightblue"}),
        ],
        "edges": [
            ("Andrea Gurnari", "Philippe Teixeira da Mota", "Knows"),
            ("Philippe Teixeira da Mota", "Qonto", "Worked At"),
            ("Barbod Namini", "Qonto", "Worked At"),
        ]
    }
}

STARTUP_RECOMMENDATION_GRAPH = {
    ("Swap", "Julia Morrongiello"): {
       "nodes": [
            ("Julia Morrongiello", {"label": "Julia Morrongiello (Person)", "size": 20, "color": "lightblue"}),
            ("Sam Atkinson", {"label": "Sam Atkinson (Person)", "size": 20, "color": "lightblue"}),
            ("English", {"label": "English (Nationality)", "size": 20, "color": "red"}),
            ("ZeroHash", {"label": "ZeroHash (Company)", "size": 20, "color": "green"}),
            ("Point Nine Capital", {"label": "Point Nine Capital (Company)", "size": 20, "color": "green"}),
            ("Accel", {"label": "Accel (Company)", "size": 20, "color": "green"}),
            ("Juni", {"label": "Juni (Company)", "size": 20, "color": "green"}),
            ("Swap", {"label": "Swap (Startup)", "size": 20, "color": "green"}),
            ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
            ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ],
        "edges": [
            ("Sam Atkinson", "Juni", "Worked At"),
            ("Julia Morrongiello", "ZeroHash", "Worked At"),
            ("Swap", "Sam Atkinson", "Founded By"),
            ("Juni", "Fintech", "Belongs To Vertical"),
            ("ZeroHash", "Fintech", "Belongs To Vertical"),
            ("Sam Atkinson", "English", "Is Nationality"),
            ("Julia Morrongiello", "English", "Is Nationality"),
            ("Sam Atkinson", "Fintech", "Is Expert In"),
            ("Julia Morrongiello", "Fintech", "Is Expert In"),
            ("Sam Atkinson", "London", "Is Based In"),
            ("Julia Morrongiello", "London", "Is Based In"),
            ("Julia Morrongiello", "Point Nine Capital", "Worked At"),
            ("Julia Morrongiello", "Accel", "Works At")
        ]
    },
    ("Flanks", "Akash Bajwa"): {
    "nodes": [
        ("Akash Bajwa", {"label": "Akash Bajwa (Person)", "size": 37, "color": "lightblue"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("Earlybird Venture Capital", {"label": "Earlybird Venture Capital (Company)", "size": 20, "color": "green"}),
        ("Augmentum Fintech", {"label": "Augmentum Fintech (Company)", "size": 20, "color": "green"}),
        ("Barclays Ventures", {"label": "Barclays Ventures (Company)", "size": 20, "color": "green"}),
        ("Payable", {"label": "Payable (Company)", "size": 20, "color": "green"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"})
    ],
    "edges": [
        ("Akash Bajwa", "London", "Is Based In"),
        ("Akash Bajwa", "Earlybird Venture Capital", "Works At"),
        ("Akash Bajwa", "Fintech", "Is Expert In"),
        ("Akash Bajwa", "Wealth Management", "Is Expert In"),
        ("Akash Bajwa", "Augmentum Fintech", "Worked At"),
        ("Akash Bajwa", "Barclays Ventures", "Worked At"),
        ("Akash Bajwa", "Payable", "Worked At"),
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Akash Bajwa", "Angel Investor", "Is"),
        ("Flanks", "Akash Bajwa", "Suggested Angel For"),
        ("Andrea Gurnari", "Akash Bajwa", "Has Shortest Path To")
    ]
},("Flanks", "Marko Bradic"): {
    "nodes": [
        ("Marko Bradic", {"label": "Marko Bradic (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Marko Bradic", "Suggested Angel For"),
        ("Andrea Gurnari", "Marko Bradic", "Has Shortest Path To")
    ]
},
("Flanks", "Valentin Vincendon"): {
    "nodes": [
        ("Valentin Vincendon", {"label": "Valentin Vincendon (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Valentin Vincendon", "Suggested Angel For"),
        ("Andrea Gurnari", "Valentin Vincendon", "Has Shortest Path To")
    ]
},
("Flanks", "Til Rochow"): {
    "nodes": [
        ("Til Rochow", {"label": "Til Rochow (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Til Rochow", "Suggested Angel For"),
        ("Andrea Gurnari", "Til Rochow", "Has Shortest Path To")
    ]
},("Flanks", "Andrew Shapiro"): {
    "nodes": [
        ("Andrew Shapiro", {"label": "Andrew Shapiro (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Andrew Shapiro", "Suggested Angel For"),
        ("Andrea Gurnari", "Andrew Shapiro", "Has Shortest Path To")
    ]
},
("Flanks", "Faith Forster"): {
    "nodes": [
        ("Faith Forster", {"label": "Faith Forster (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Faith Forster", "Suggested Angel For"),
        ("Andrea Gurnari", "Faith Forster", "Has Shortest Path To")
    ]
},
("Flanks", "Michael Keskerides"): {
    "nodes": [
        ("Michael Keskerides", {"label": "Michael Keskerides (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Michael Keskerides", "Suggested Angel For"),
        ("Andrea Gurnari", "Michael Keskerides", "Has Shortest Path To")
    ]
}, ("Flanks", "Will Sorby"): {
    "nodes": [
        ("Will Sorby", {"label": "Will Sorby (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Will Sorby", "Suggested Angel For"),
        ("Andrea Gurnari", "Will Sorby", "Has Shortest Path To")
    ]
},
("Flanks", "Jas Shah"): {
    "nodes": [
        ("Jas Shah", {"label": "Jas Shah (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Jas Shah", "Suggested Angel For"),
        ("Andrea Gurnari", "Jas Shah", "Has Shortest Path To")
    ]
},
("Flanks", "Kaushik Subramanian"): {
    "nodes": [
        ("Kaushik Subramanian", {"label": "Kaushik Subramanian (Person)", "size": 20, "color": "lightblue"}),
        ("Flanks", {"label": "Flanks (Startup)", "size": 20, "color": "green"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Developer APIs", {"label": "Developer APIs (Industry)", "size": 20, "color": "pink"}),
        ("Software", {"label": "Software (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Barcelona", {"label": "Barcelona (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Flanks", "Developer APIs", "Belongs To Vertical"),
        ("Flanks", "Fintech", "Belongs To Vertical"),
        ("Flanks", "Software", "Belongs To Vertical"),
        ("Flanks", "Wealth Management", "Belongs To Vertical"),
        ("Flanks", "Barcelona", "Is Based In"),
        ("Flanks", "Kaushik Subramanian", "Suggested Angel For"),
        ("Andrea Gurnari", "Kaushik Subramanian", "Has Shortest Path To")
    ]
},
("Arke", "Daniele Simoneschi"): {
    "nodes": [
        ("Daniele Simoneschi", {"label": "Daniele Simoneschi (Person)", "size": 20, "color": "lightblue"}),
        ("Arke", {"label": "Arke (Startup)", "size": 20, "color": "green"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Arke", "Daniele Simoneschi", "Suggested Angel For"),
        ("Andrea Gurnari", "Daniele Simoneschi", "Has Shortest Path To")
    ]
},
("Arke", "Francesco Simoneschi"): {
    "nodes": [
        ("Francesco Simoneschi", {"label": "Francesco Simoneschi (Person)", "size": 20, "color": "lightblue"}),
        ("Arke", {"label": "Arke (Startup)", "size": 20, "color": "green"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Arke", "Francesco Simoneschi", "Suggested Angel For"),
        ("Andrea Gurnari", "Francesco Simoneschi", "Has Shortest Path To")
    ]
},
("Arke", "Sam Pratt"): {
    "nodes": [
        ("Sam Pratt", {"label": "Sam Pratt (Person)", "size": 20, "color": "lightblue"}),
        ("Arke", {"label": "Arke (Startup)", "size": 20, "color": "green"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Arke", "Sam Pratt", "Suggested Angel For"),
        ("Andrea Gurnari", "Sam Pratt", "Has Shortest Path To")
    ]
},
("Arke", "Alexandre Dewez"): {
    "nodes": [
        ("Alexandre Dewez", {"label": "Alexandre Dewez (Person)", "size": 20, "color": "lightblue"}),
        ("Arke", {"label": "Arke (Startup)", "size": 20, "color": "green"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Arke", "Alexandre Dewez", "Suggested Angel For"),
        ("Andrea Gurnari", "Alexandre Dewez", "Has Shortest Path To")
    ]
},("Arke", "Max Bacon"): {
    "nodes": [
        ("Max Bacon", {"label": "Max Bacon (Person)", "size": 20, "color": "lightblue"}),
        ("Arke", {"label": "Arke (Startup)", "size": 20, "color": "green"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Arke", "Max Bacon", "Suggested Angel For"),
        ("Andrea Gurnari", "Max Bacon", "Has Shortest Path To")
    ]
}, ("Prometheux", "Akash Bajwa"): {
    "nodes": [
        ("Akash Bajwa", {"label": "Akash Bajwa (Person)", "size": 37, "color": "lightblue"}),
        ("Prometheux", {"label": "Prometheux (Startup)", "size": 20, "color": "green"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("Earlybird Venture Capital", {"label": "Earlybird Venture Capital (Company)", "size": 20, "color": "green"}),
        ("Augmentum Fintech", {"label": "Augmentum Fintech (Company)", "size": 20, "color": "green"}),
        ("Barclays Ventures", {"label": "Barclays Ventures (Company)", "size": 20, "color": "green"}),
        ("Payable", {"label": "Payable (Company)", "size": 20, "color": "green"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Fintech", {"label": "Fintech (Industry)", "size": 20, "color": "pink"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Akash Bajwa", "London", "Is Based In"),
        ("Prometheux", "United Kingdom", "Is Based In"),
        ("Akash Bajwa", "Earlybird Venture Capital", "Works At"),
        ("Akash Bajwa", "Wealth Management", "Is Expert In"),
        ("Akash Bajwa", "Fintech", "Is Expert In"),
        ("Akash Bajwa", "Augmentum Fintech", "Worked At"),
        ("Akash Bajwa", "Barclays Ventures", "Worked At"),
        ("Akash Bajwa", "Payable", "Worked At"),
        ("Prometheux", "Akash Bajwa", "Suggested Angel For"),
        ("Andrea Gurnari", "Akash Bajwa", "Has Shortest Path To"),
        ("Prometheux", "Fintech", "Belongs To Vertical"),
        ("Prometheux", "Wealth Management", "Belongs To Vertical")
    ]
},("Prometheux", "Michael Jenkins"): {
    "nodes": [
        ("Michael Jenkins", {"label": "Michael Jenkins (Person)", "size": 20, "color": "lightblue"}),
        ("Prometheux", {"label": "Prometheux (Startup)", "size": 20, "color": "green"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Prometheux", "United Kingdom", "Is Based In"),
        ("Prometheux", "Michael Jenkins", "Suggested Angel For"),
        ("Andrea Gurnari", "Michael Jenkins", "Has Shortest Path To")
    ]
},("Revolut", "Tanya Agarwal"): {
    "nodes": [
        ("Tanya Agarwal", {"label": "Tanya Agarwal (Person)", "size": 34, "color": "lightblue"}),
        ("Revolut", {"label": "Revolut (Startup)", "size": 20, "color": "green"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("England", {"label": "England (Geo)", "size": 20, "color": "blue"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("Banking", {"label": "Banking (Industry)", "size": 20, "color": "pink"}),
        ("Financial Services", {"label": "Financial Services (Industry)", "size": 20, "color": "pink"}),
        ("FinTech", {"label": "FinTech (Industry)", "size": 20, "color": "pink"}),
        ("Mobile Payments", {"label": "Mobile Payments (Industry)", "size": 20, "color": "pink"}),
        ("Lending", {"label": "Lending (Industry)", "size": 20, "color": "pink"}),
        ("Insurance", {"label": "Insurance (Industry)", "size": 20, "color": "pink"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Revolut", "London", "Is Based In"),
        ("Revolut", "United Kingdom", "Is Based In"),
        ("Revolut", "Banking", "Belongs To Vertical"),
        ("Revolut", "Financial Services", "Belongs To Vertical"),
        ("Revolut", "FinTech", "Belongs To Vertical"),
        ("Revolut", "Mobile Payments", "Belongs To Vertical"),
        ("Tanya Agarwal", "London", "Is Based In"),
        ("Tanya Agarwal", "United Kingdom", "Is Nationality"),
        ("Tanya Agarwal", "Lending", "Is Expert In"),
        ("Tanya Agarwal", "Insurance", "Is Expert In"),
        ("Revolut", "Tanya Agarwal", "Suggested Angel For"),
        ("Andrea Gurnari", "Tanya Agarwal", "Has Shortest Path To")
    ]
},
("Revolut", "Will Sorby"): {
    "nodes": [
        ("Will Sorby", {"label": "Will Sorby (Person)", "size": 20, "color": "lightblue"}),
        ("Revolut", {"label": "Revolut (Startup)", "size": 20, "color": "green"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("Banking", {"label": "Banking (Industry)", "size": 20, "color": "pink"}),
        ("Financial Services", {"label": "Financial Services (Industry)", "size": 20, "color": "pink"}),
        ("FinTech", {"label": "FinTech (Industry)", "size": 20, "color": "pink"}),
        ("Mobile Payments", {"label": "Mobile Payments (Industry)", "size": 20, "color": "pink"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Revolut", "London", "Is Based In"),
        ("Revolut", "United Kingdom", "Is Based In"),
        ("Revolut", "Banking", "Belongs To Vertical"),
        ("Revolut", "Financial Services", "Belongs To Vertical"),
        ("Revolut", "FinTech", "Belongs To Vertical"),
        ("Revolut", "Mobile Payments", "Belongs To Vertical"),
        ("Will Sorby", "United Kingdom", "Is Nationality"),
        ("Revolut", "Will Sorby", "Suggested Angel For"),
        ("Andrea Gurnari", "Will Sorby", "Has Shortest Path To")
    ]
},
("Revolut", "Kartik Dabbiru"): {
    "nodes": [
        ("Kartik Dabbiru", {"label": "Kartik Dabbiru (Person)", "size": 20, "color": "lightblue"}),
        ("Revolut", {"label": "Revolut (Startup)", "size": 20, "color": "green"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("Banking", {"label": "Banking (Industry)", "size": 20, "color": "pink"}),
        ("Financial Services", {"label": "Financial Services (Industry)", "size": 20, "color": "pink"}),
        ("FinTech", {"label": "FinTech (Industry)", "size": 20, "color": "pink"}),
        ("Mobile Payments", {"label": "Mobile Payments (Industry)", "size": 20, "color": "pink"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Revolut", "London", "Is Based In"),
        ("Revolut", "United Kingdom", "Is Based In"),
        ("Revolut", "Banking", "Belongs To Vertical"),
        ("Revolut", "Financial Services", "Belongs To Vertical"),
        ("Revolut", "FinTech", "Belongs To Vertical"),
        ("Revolut", "Mobile Payments", "Belongs To Vertical"),
        ("Kartik Dabbiru", "United Kingdom", "Is Nationality"),
        ("Revolut", "Kartik Dabbiru", "Suggested Angel For"),
        ("Andrea Gurnari", "Kartik Dabbiru", "Has Shortest Path To")
    ]
},("Revolut", "Julia Morrongiello"): {
    "nodes": [
        ("Julia Morrongiello", {"label": "Julia Morrongiello (Person)", "size": 20, "color": "lightblue"}),
        ("Revolut", {"label": "Revolut (Startup)", "size": 20, "color": "green"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("Banking", {"label": "Banking (Industry)", "size": 20, "color": "pink"}),
        ("Financial Services", {"label": "Financial Services (Industry)", "size": 20, "color": "pink"}),
        ("FinTech", {"label": "FinTech (Industry)", "size": 20, "color": "pink"}),
        ("Mobile Payments", {"label": "Mobile Payments (Industry)", "size": 20, "color": "pink"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Revolut", "London", "Is Based In"),
        ("Revolut", "United Kingdom", "Is Based In"),
        ("Revolut", "Banking", "Belongs To Vertical"),
        ("Revolut", "Financial Services", "Belongs To Vertical"),
        ("Revolut", "FinTech", "Belongs To Vertical"),
        ("Revolut", "Mobile Payments", "Belongs To Vertical"),
        ("Julia Morrongiello", "United Kingdom", "Is Nationality"),
        ("Revolut", "Julia Morrongiello", "Suggested Angel For"),
        ("Andrea Gurnari", "Julia Morrongiello", "Has Shortest Path To")
    ]
},
("Swap", "Tanya Agarwal"): {
    "nodes": [
        ("Tanya Agarwal", {"label": "Tanya Agarwal (Person)", "size": 34, "color": "lightblue"}),
        ("Swap", {"label": "Swap (Startup)", "size": 20, "color": "green"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("England", {"label": "England (Geo)", "size": 20, "color": "blue"}),
        ("Payments", {"label": "Payments (Industry)", "size": 20, "color": "pink"}),
        ("Lending", {"label": "Lending (Industry)", "size": 20, "color": "pink"}),
        ("Insurance", {"label": "Insurance (Industry)", "size": 20, "color": "pink"}),
        ("FinTech", {"label": "FinTech (Industry)", "size": 20, "color": "pink"}),
        ("WISE", {"label": "Wise (Company)", "size": 20, "color": "green"}),
        ("Paddle", {"label": "Paddle (Company)", "size": 20, "color": "green"}),
        ("SME Stories", {"label": "SME Stories (Company)", "size": 20, "color": "green"}),
        ("Asto UK", {"label": "Asto UK (Company)", "size": 20, "color": "green"}),
        ("Basement Crowd", {"label": "Basement Crowd (Company)", "size": 20, "color": "green"}),
        ("Sparqa Legal", {"label": "Sparqa Legal (Company)", "size": 20, "color": "green"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Swap", "United Kingdom", "Is Based In"),
        ("Swap", "FinTech", "Belongs To Vertical"),
        ("Swap", "Payments", "Belongs To Vertical"),
        ("Tanya Agarwal", "London", "Is Based In"),
        ("Tanya Agarwal", "England", "Is Based In"),
        ("Tanya Agarwal", "United Kingdom", "Is Nationality"),
        ("Tanya Agarwal", "Payments", "Is Close To Vertical"),
        ("Tanya Agarwal", "Lending", "Is Expert In"),
        ("Tanya Agarwal", "Insurance", "Is Expert In"),
        ("Tanya Agarwal", "WISE", "Worked At"),
        ("Tanya Agarwal", "Paddle", "Worked At"),
        ("Tanya Agarwal", "SME Stories", "Worked At"),
        ("Tanya Agarwal", "Asto UK", "Worked At"),
        ("Tanya Agarwal", "Basement Crowd", "Worked At"),
        ("Tanya Agarwal", "Sparqa Legal", "Worked At"),
        ("Swap", "Tanya Agarwal", "Suggested Angel For"),
        ("Andrea Gurnari", "Tanya Agarwal", "Has Shortest Path To"),
        ("Tanya Agarwal", "Swap", "Supernode Connection (Weight: 0.5)")
    ]
}
,
("Swap", "Akash Bajwa"): {
    "nodes": [
        ("Akash Bajwa", {"label": "Akash Bajwa (Person)", "size": 37, "color": "lightblue"}),
        ("Swap", {"label": "Swap (Startup)", "size": 20, "color": "green"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("London", {"label": "London (Geo)", "size": 20, "color": "blue"}),
        ("Earlybird Venture Capital", {"label": "Earlybird Venture Capital (Company)", "size": 20, "color": "green"}),
        ("Augmentum Fintech", {"label": "Augmentum Fintech (Company)", "size": 20, "color": "green"}),
        ("Barclays Ventures", {"label": "Barclays Ventures (Company)", "size": 20, "color": "green"}),
        ("Payable", {"label": "Payable (Company)", "size": 20, "color": "green"}),
        ("FinTech", {"label": "FinTech (Industry)", "size": 20, "color": "pink"}),
        ("Wealth Management", {"label": "Wealth Management (Industry)", "size": 20, "color": "pink"}),
        ("Financial Services", {"label": "Financial Services (Industry)", "size": 20, "color": "pink"}),
        ("Venture Capital", {"label": "Venture Capital (Industry)", "size": 20, "color": "pink"}),
        ("Private Equity", {"label": "Private Equity (Industry)", "size": 20, "color": "pink"}),
        ("Management Consulting", {"label": "Management Consulting (Industry)", "size": 20, "color": "pink"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Swap", "United Kingdom", "Is Based In"),
        ("Swap", "FinTech", "Belongs To Vertical"),
        ("Swap", "Financial Services", "Belongs To Vertical"),
        ("Swap", "Venture Capital", "Belongs To Vertical"),
        ("Swap", "Private Equity", "Belongs To Vertical"),
        ("Akash Bajwa", "London", "Is Based In"),
        ("Akash Bajwa", "United Kingdom", "Is Nationality"),
        ("Akash Bajwa", "FinTech", "Is Expert In"),
        ("Akash Bajwa", "Wealth Management", "Is Expert In"),
        ("Akash Bajwa", "Financial Services", "Is Expert In"),
        ("Akash Bajwa", "Earlybird Venture Capital", "Works At"),
        ("Akash Bajwa", "Augmentum Fintech", "Worked At"),
        ("Akash Bajwa", "Barclays Ventures", "Worked At"),
        ("Akash Bajwa", "Payable", "Worked At"),
        ("Akash Bajwa", "Management Consulting", "Is Expert In"),
        ("Swap", "Akash Bajwa", "Suggested Angel For"),
        ("Andrea Gurnari", "Akash Bajwa", "Has Shortest Path To"),
        ("Akash Bajwa", "Swap", "Supernode Connection (Weight: 0.5)")
    ]
}, ("Swap", "Kartik Dabbiru"): {
    "nodes": [
        ("Kartik Dabbiru", {"label": "Kartik Dabbiru (Person)", "size": 20, "color": "lightblue"}),
        ("Swap", {"label": "Swap (Startup)", "size": 20, "color": "green"}),
        ("United Kingdom", {"label": "United Kingdom (Geo)", "size": 20, "color": "blue"}),
        ("FinTech", {"label": "FinTech (Industry)", "size": 20, "color": "pink"}),
        ("Financial Services", {"label": "Financial Services (Industry)", "size": 20, "color": "pink"}),
        ("Venture Capital", {"label": "Venture Capital (Industry)", "size": 20, "color": "pink"}),
        ("Private Equity", {"label": "Private Equity (Industry)", "size": 20, "color": "pink"}),
        ("Andrea Gurnari", {"label": "Andrea Gurnari (Person)", "size": 20, "color": "lightblue"})
    ],
    "edges": [
        ("Swap", "United Kingdom", "Is Based In"),
        ("Swap", "FinTech", "Belongs To Vertical"),
        ("Swap", "Financial Services", "Belongs To Vertical"),
        ("Swap", "Venture Capital", "Belongs To Vertical"),
        ("Swap", "Private Equity", "Belongs To Vertical"),
        ("Kartik Dabbiru", "United Kingdom", "Is Nationality"),
        ("Swap", "Kartik Dabbiru", "Suggested Angel For"),
        ("Andrea Gurnari", "Kartik Dabbiru", "Has Shortest Path To")
    ]
}
}

HARDCODED_SHORTEST_PATHS = {
    ("Pietro Bezza", "Andrea Gurnari"): """Since there is an edge from Andrea Gurnari to Pietro Bezza of type person_knows_person, then there is a path from Andrea Gurnari to Pietro Bezza of length 1.. 
Since there is a path from Andrea Gurnari to Pietro Bezza of length 1., then The shortest path from source Andrea Gurnari to target Pietro Bezza is of length 1..
""",
    ("Akash Bajwa", "Andrea Gurnari"): """Since there is an edge from Andrea Gurnari to Akash Bajwa of type person_knows_person, then there is a path from Andrea Gurnari to Akash Bajwa of length 1.. 
Since there is a path from Andrea Gurnari to Akash Bajwa of length 1., then The shortest path from source Andrea Gurnari to target Akash Bajwa is of length 1..
""",
    ("Barbod Namini", "Andrea Gurnari"): """Since there is an edge from Andrea Gurnari to Philippe Teixeira da Mota of type person_knows_person, then there is a path from Andrea Gurnari to Philippe Teixeira da Mota of length 1.. 
Since there is an edge from Philippe Teixeira da Mota to Qonto of type person_worked_in_organization, and there is a path from Andrea Gurnari to Philippe Teixeira da Mota of length 1., then there is a path from Andrea Gurnari to Qonto of length 2.. 
Since there is a path from Andrea Gurnari to Qonto of length 2., and there is an edge from Qonto to Barbod Namini of type organization_had_employee_person, then there is a path from Andrea Gurnari to Barbod Namini of length 3.. 
Since there is a path from Andrea Gurnari to Barbod Namini of length 3., then The shortest path from source Andrea Gurnari to target Barbod Namini is of length 3..
"""
}

JULIA_SHORTEST_PATH = """
    The shortest path between Julia Morrongiello and you is of length 2.

In order to get to Julia Morrongiello, the strongest identified link is through Luca Bocchio, Partner at Accel.

In fact:
- Both Julia and Luca work at Accel. Julia is a Starter at Accel while Luca is a Partner
- You have invested in Saber where Accel has also invested
- You and Luca have been in touch recently.

You and Julia follow the following properties:
- You are both in the Fintech Guild community
- You share the same focus for vertical Fintech
- Julia was also in VC before, having worked at Point Nine Capital
"""

JULIA_STARTUP_ANGEL_RECOMMENDATIONS = """
    I would recommend Julia Morrongiello, Corporate Development and Strategy at BVNK as an angel for Swap, Fintech B2B SaaS for e-commerce stores, because: 

- Julia has been identified as an angel investor
- Julia is an expert in startup investing, currently working at Accel in its angel program and having worked at Point Nine Capital.
- Julia has worked at Zero Hash, so she is an expert in fintech, just like Sam Atkinson, founder of Swap. Sam is also an expert, having worked as Head of Strategy at Juni, a fintech company.
- Julia and Sam also share that they are both English and based in London, adding a criteria of proximity.

You share with Julia the participation in the fintech guild, the expertise in fintech and in startup investing. She is not a direct contact, but I can help you identify the shortest path to her.
"""
