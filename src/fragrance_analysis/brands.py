DESIGNER_HOUSES = {
    "Giorgio Armani", "Dior", "Hermès", "Yves Saint Laurent", "Tom Ford", "Chanel", "Zara",
    "Calvin Klein", "Bvlgari", "Prada", "Paco Rabanne", "Hugo Boss", "Mugler", "Dolce & Gabbana",
    "Gucci", "Givenchy", "Jean Paul Gaultier", "Jil Sander", "Comme des Garçons", "Louis Vuitton",
    "Cartier", "Joop!", "Burberry", "Versace", "Issey Miyake", "Kenzo", "Van Cleef & Arpels",
    "Valentino", "Narciso Rodriguez", "Maison Margiela", "Etro", "Montblanc", "Chloé",
    "Carolina Herrera", "Marc Jacobs", "Lacoste", "Bottega Veneta", "Rochas", "Cacharel",
    "Salvatore Ferragamo", "Trussardi", "Boucheron", "Loewe", "Diesel", "Lolita Lempicka",
    "Ralph Lauren", "DKNY / Donna Karan", "Laura Biagiotti", "John Varvatos", "Roberto Cavalli",
    "Dsquared²", "Zadig & Voltaire", "Karl Lagerfeld", "Azzaro", "Lanvin", "Viktor & Rolf",
    "Moschino", "Balmain", "Dunhill", "Aigner", "Abercrombie & Fitch", "Juicy Couture", "Cerruti",
    "Nina Ricci", "Tommy Hilfiger", "Celine", "Jimmy Choo", "Ermenegildo Zegna", "Fendi",
    "Oscar de la Renta", "Balenciaga", "Michael Kors", "Guess", "Benetton", "Coach", "Vera Wang",
    "Gianfranco Ferré", "Bogner", "Puma", "Iceberg", "Mauboussin", "Toni Gard", "Jacomo",
    "Courrèges", "Kenneth Cole", "Hollister", "Anna Sui", "Krizia", "Elie Saab", "Escada",
    "Ted Lapidus", "Victoria's Secret", "Mexx", "s.Oliver", "bugatti Fashion", "Grès",
    "Guy Laroche", "Costume National", "Otto Kern", "Jesus del Pozo", "Masakï Matsushïma", "Adidas",
    "Alexander McQueen", "Stella McCartney", "Vivienne Westwood", "Christian Louboutin",
    "Yohji Yamamoto", "Missoni", "Emanuel Ungaro", "Tiffany & Co.",
    "Chopard", "Agent Provocateur", "Banana Republic", "Bruno Banani", "Jean Patou",
    "Jean-Louis Scherrer", "La Perla", "Michalsky", "Tom Tailor",
    "Perry Ellis", "Paul Smith", "Ghost", "Halston", "Adolfo Dominguez", "Angel Schlesser",
    "Roccobarocco", "Fiorucci", "Baldessarini", "Worth", "Jacques Fath", "Jean-Charles Brosseau",
    "Georges Rech", "Léonard", "Bijan", "Alfred Sung", "Curve / Liz Claiborne", "Vince Camuto",
    "Ellen Tracy", "Gloria Vanderbilt", "Mila Schön", "Lancetti", "Blumarine", "Tory Burch",
    "Sonia Rykiel", "Byblos", "Molyneux", "Sean John", "Gian Marco Venturi", "Luciano Soprani",
    "Weil", "Montana", "Carven", "John Galliano", "Geoffrey Beene", "Kiton", "Enrico Coveri",
    "La Martina", "Liu•Jo", "Sergio Tacchini", "Springfield", "Massimo Dutti", "River Island",
    "American Eagle", "Urban Outfitters", "Aéropostale", "Old Navy", "GAP", "H&M", "Express",
    "Superdry", "MCM", "Ed Hardy", "Koton", "moussy / マウジー", "Victorinox", "Nike", "Fila",
    "Francesca's", "Claire's", "Ocean Pacific", "Mango", "Bershka", "Primark", "Police",
    "Betty Barclay", "Tous", "Replay", "French Connection / FCUK", "Tommy Bahama", "Nautica",
    "Mandarina Duck", "Korloff", "Elizabeth and James",
}

# Unclassified brands that clearly aren't a perfumery whose entire business is fragrance only
EXCLUDE_FROM_NICHE = {
    "Ariana Grande", "Avon", "Axe / Lynx", "Aēsop", "Bath & Body Works", "Britney Spears",
    "By Terry", "Christina Aguilera", "Clinique", "Coty", "David Beckham", "Davidoff",
    "Elizabeth Arden", "Elizabeth Taylor", "Estēe Lauder", "Frapin", "Jaguar", "Judith Williams",
    "Katy Perry", "Korres", "L'Erbolario", "L'Occitane en Provence", "Lalique", "Lancaster",
    "Lancôme", "Laura Mercier", "Lush / Cosmetics To Go", "Marbert", "Mercedes-Benz",
    "Molton Brown", "Naomi Campbell", "Oriflame", "Rammstein", "Rituals", "Salvador Dali",
    "Shiseido / 資生堂", "Sisley", "The Body Shop", "Yves Rocher",
    "Puig", "Helena Rubinstein", "Philosophy", "Paris Hilton", "Jennifer Lopez", "Banderas",
    "M. Asam", "Jafra", "Milton-Lloyd / Jean Yves Cosmetics", "California Perfume Company",
    "O Boticário", "Violette Market",
    "Ferrari", "Tonino Lamborghini", "Playboy", "James Bond 007", "Beyoncé", "Rihanna",
    "Shakira", "Cristiano Ronaldo", "Sarah Jessica Parker", "Jessica Simpson",
    "KKW Fragrance / Kim Kardashian", "Harajuku Lovers / Gwen Stefani", "Paloma Picasso",
    "Procter & Gamble", "Revlon / Charles Revson", "Clarins", "Biotherm", "Kiehl's", "Nuxe",
    "Juvena", "Missha", "Kosé / コーセー", "Pola / ポーラ", "Kanebo", "Decorté",
    "Orlane / Jean d'Albret", "Dermacol", "Perlier", "Gosh Cosmetics", "essence", "KIKO",
    "M∙A∙C", "General Cosmetics", "Dina Cosmetics", "Constance Carroll", "Alcina", "Farmasi",
    "Yanbal", "ésika", "Nutrimetics", "Vanda / Beauty Counselor", "Viviane Woodard",
    "Dorothy Gray", "Richard Hudnut", "Prince Matchabelli", "Jōvan", "Shulton",
    "Body Fantasies", "bodycology",
    "Sephora", "Boots", "Douglas", "Aldi / Hofer", "Lidl", "Mercadona",
}


def classify_brand(brand: str) -> str:
    if brand in DESIGNER_HOUSES:
        return "Designer"
    if brand in EXCLUDE_FROM_NICHE:
        return "Unclassified"
    return "Niche"
