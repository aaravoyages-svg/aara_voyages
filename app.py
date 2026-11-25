from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# ── Brand Info ──────────────────────────────────────────────────────────────
BRAND = {
    "name": "Aara Voyages",
    "tagline": "Journeys Worth Telling",
    "email": "aaravoyages@gmail.com",
    "whatsapp": "9871976001",
    "whatsapp_link": "https://wa.me/919871976001",
    "phone_display": "+91 98719 76001",
}

# ── Destinations ────────────────────────────────────────────────────────────
DESTINATIONS = {
    "dubai": {
        "name": "Dubai",
        "country": "United Arab Emirates",
        "hero_image": "dubai.jpg",
        "duration": "5 Days / 4 Nights",
        "price_from": "₹45,000",
        "tagline": "Where Tradition Meets the Future",
        "overview": (
            "Experience the dazzling city of Dubai — a spectacular fusion of "
            "ancient Arabian heritage and jaw-dropping modernity. From the "
            "world's tallest skyscraper to golden desert safaris, Dubai "
            "promises a holiday of extraordinary contrasts and unforgettable "
            "luxury."
        ),
        "highlights": [
            "Burj Khalifa – At the Top observation deck",
            "Desert Safari with BBQ dinner & belly dance",
            "Dubai Mall & Dubai Fountain show",
            "Palm Jumeirah & Atlantis Aquaventure",
            "Dhow Cruise along Dubai Marina",
            "Old Dubai – Gold & Spice Souks, Abra Ride",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival & Marina Dazzle",
                "description": (
                    "Arrive at Dubai International Airport. Private transfer "
                    "to your hotel. Evening at leisure — stroll along the "
                    "glittering Dubai Marina promenade and enjoy dinner at a "
                    "waterfront restaurant."
                ),
            },
            {
                "day": 2,
                "title": "City Tour & Burj Khalifa",
                "description": (
                    "Full-day city tour covering Jumeirah Mosque, Dubai "
                    "Museum, and the heritage quarter. Afternoon visit to "
                    "Dubai Mall for shopping, followed by sunset tickets to "
                    "the Burj Khalifa 'At the Top' observation deck. Evening "
                    "Dubai Fountain show."
                ),
            },
            {
                "day": 3,
                "title": "Desert Safari Adventure",
                "description": (
                    "Morning at leisure or optional visit to Miracle Garden. "
                    "Afternoon pick-up for an exhilarating 4×4 dune-bashing "
                    "desert safari. Enjoy camel rides, sandboarding, henna "
                    "painting, and a lavish BBQ dinner under the stars with "
                    "live entertainment."
                ),
            },
            {
                "day": 4,
                "title": "Palm Jumeirah & Old Dubai",
                "description": (
                    "Morning visit to Palm Jumeirah and Atlantis "
                    "Aquaventure Waterpark. Afternoon explore Old Dubai — "
                    "cross Dubai Creek on a traditional Abra, wander through "
                    "the Gold Souk and Spice Souk. Evening Dhow Cruise "
                    "dinner along the Marina."
                ),
            },
            {
                "day": 5,
                "title": "Departure",
                "description": (
                    "Enjoy a leisurely breakfast. Free time for last-minute "
                    "shopping at Mall of the Emirates or Ibn Battuta Mall. "
                    "Private transfer to the airport for your departure."
                ),
            },
        ],
        "tips": [
            "Best time to visit: November to March (pleasant weather).",
            "Dress modestly when visiting mosques and heritage sites.",
            "The Dubai Metro is an affordable way to get around.",
            "Haggle politely at the souks — it's expected!",
            "Carry sunscreen and stay hydrated in the desert.",
        ],
    },
    "singapore": {
        "name": "Singapore",
        "country": "Singapore",
        "hero_image": "singapore.jpg",
        "duration": "4 Days / 3 Nights",
        "price_from": "₹55,000",
        "tagline": "The Lion City of Wonders",
        "overview": (
            "Discover Singapore — a vibrant island city-state where "
            "futuristic skyscrapers meet lush tropical gardens, world-class "
            "street food tempts every palate, and cultures blend seamlessly. "
            "Compact yet endlessly exciting, Singapore is the perfect "
            "getaway for every kind of traveller."
        ),
        "highlights": [
            "Marina Bay Sands SkyPark & Light Show",
            "Gardens by the Bay – Supertree Grove & Cloud Forest",
            "Sentosa Island – Universal Studios & S.E.A. Aquarium",
            "Orchard Road shopping spree",
            "Chinatown & Little India heritage walks",
            "Hawker centre food trails",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival & Marina Bay Magic",
                "description": (
                    "Arrive at Changi Airport (voted world's best!). "
                    "Transfer to your hotel. Evening visit to Marina Bay — "
                    "see the iconic Merlion, walk along the Helix Bridge, "
                    "and catch the spectacular Spectra Light & Water Show."
                ),
            },
            {
                "day": 2,
                "title": "Gardens, Culture & Flavours",
                "description": (
                    "Morning at Gardens by the Bay — explore the Cloud "
                    "Forest dome and Flower Dome, walk the OCBC Skyway "
                    "among the Supertrees. Afternoon heritage walk through "
                    "Chinatown (Thian Hock Keng Temple) and Little India "
                    "(Mustafa Centre). Evening hawker food tour at Lau Pa "
                    "Sat or Maxwell Food Centre."
                ),
            },
            {
                "day": 3,
                "title": "Sentosa Island Fun",
                "description": (
                    "Full day at Sentosa Island. Visit Universal Studios "
                    "Singapore for thrilling rides, or explore S.E.A. "
                    "Aquarium and the Madame Tussauds wax museum. Relax at "
                    "Palawan Beach. Evening cable car ride back with "
                    "panoramic harbour views."
                ),
            },
            {
                "day": 4,
                "title": "Shopping & Departure",
                "description": (
                    "Morning shopping on Orchard Road — ION Orchard, "
                    "Takashimaya, and Paragon. Last stop at the futuristic "
                    "Jewel Changi waterfall before your departure flight."
                ),
            },
        ],
        "tips": [
            "Singapore is safe and super clean — fines for littering are real!",
            "Get an EZ-Link card for hassle-free MRT & bus travel.",
            "Hawker centres offer Michelin-star food under ₹500.",
            "The Singapore Flyer offers stunning sunset views.",
            "English is widely spoken — communication is easy.",
        ],
    },
    "malaysia": {
        "name": "Malaysia",
        "country": "Malaysia",
        "hero_image": "malaysia.jpg",
        "duration": "5 Days / 4 Nights",
        "price_from": "₹35,000",
        "tagline": "Truly Asia, Truly Magical",
        "overview": (
            "Malaysia is a kaleidoscope of cultures, flavours, and "
            "landscapes. From the gleaming Petronas Towers of Kuala Lumpur "
            "to the pristine beaches of Langkawi, ancient rainforests to "
            "aromatic street-food stalls, Malaysia offers extraordinary "
            "value and diversity in one stunning package."
        ),
        "highlights": [
            "Petronas Twin Towers & KLCC Park",
            "Batu Caves – Rainbow staircase temple",
            "Langkawi Sky Bridge & Cable Car",
            "Penang street food & George Town art",
            "Genting Highlands theme parks",
            "Taman Negara — world's oldest rainforest",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival in Kuala Lumpur",
                "description": (
                    "Arrive at KLIA. Transfer to hotel in the city centre. "
                    "Evening visit to the Petronas Twin Towers — walk "
                    "across the Skybridge and enjoy the KLCC Park fountain "
                    "show. Dinner at Jalan Alor night market."
                ),
            },
            {
                "day": 2,
                "title": "KL City Tour & Batu Caves",
                "description": (
                    "Morning visit to Batu Caves (iconic 272-step rainbow "
                    "staircase). Continue to the National Mosque, Merdeka "
                    "Square, and the Royal Palace. Afternoon at Central "
                    "Market for handicrafts. Evening at Bukit Bintang "
                    "for shopping and street food."
                ),
            },
            {
                "day": 3,
                "title": "Genting Highlands",
                "description": (
                    "Day trip to Genting Highlands — ride the Awana "
                    "SkyWay cable car through misty mountains. Enjoy the "
                    "indoor theme park, Skytropolis Funland, and the "
                    "SkyAvenue mall. Return to KL in the evening for a "
                    "rooftop dinner with city views."
                ),
            },
            {
                "day": 4,
                "title": "Langkawi Island Escape",
                "description": (
                    "Morning flight to Langkawi. Visit the Langkawi Sky "
                    "Bridge and Cable Car for breathtaking aerial views. "
                    "Afternoon island-hopping tour — Pregnant Maiden Lake, "
                    "Eagle Square, and Wet Rice Museum. Sunset at Cenang "
                    "Beach."
                ),
            },
            {
                "day": 5,
                "title": "Langkawi & Departure",
                "description": (
                    "Morning mangrove boat tour through the Kilim "
                    "Geoforest Park — spot eagles, monkeys, and "
                    "limestone caves. Duty-free shopping at Kuah town. "
                    "Transfer to airport for departure."
                ),
            },
        ],
        "tips": [
            "Best time: March to October (dry season for most regions).",
            "Try nasi lemak for breakfast — the national dish!",
            "Langkawi is a duty-free island — great for chocolate & alcohol.",
            "Grab (ride-hailing app) is the easiest way to get around.",
            "Carry an umbrella — tropical rain showers are brief but heavy.",
        ],
    },
    "bali": {
        "name": "Bali",
        "country": "Indonesia",
        "hero_image": "bali.jpg",
        "duration": "5 Days / 4 Nights",
        "price_from": "₹40,000",
        "tagline": "Island of Gods & Eternal Beauty",
        "overview": (
            "Bali is a paradise that enchants every traveller. Emerald rice "
            "terraces cascade down volcanic hillsides, ancient temples rise "
            "from clifftops above crashing waves, and vibrant nightlife "
            "pulses through beach towns. Whether you seek spiritual peace "
            "in Ubud or adventure in the surf, Bali delivers magic at every "
            "turn."
        ),
        "highlights": [
            "Ubud – Sacred Monkey Forest & art galleries",
            "Tegallalang Rice Terraces",
            "Tanah Lot – Sunset sea temple",
            "Seminyak & Kuta beach clubs",
            "Mount Batur sunrise trek",
            "Uluwatu Temple & Kecak fire dance",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival & Seminyak Vibes",
                "description": (
                    "Arrive at Ngurah Rai International Airport. Transfer "
                    "to your villa in Seminyak. Afternoon relax at a beach "
                    "club — Potato Head or Ku De Ta. Watch the legendary "
                    "Bali sunset with cocktails on the sand."
                ),
            },
            {
                "day": 2,
                "title": "Ubud – Heart of Bali",
                "description": (
                    "Drive to Ubud. Visit the Sacred Monkey Forest "
                    "Sanctuary, stroll through the Ubud Art Market, and "
                    "explore the magnificent Tirta Empul water temple. "
                    "Afternoon walk through the stunning Tegallalang Rice "
                    "Terraces. Evening Balinese cooking class."
                ),
            },
            {
                "day": 3,
                "title": "Temples & Waterfalls",
                "description": (
                    "Morning visit to Tegenungan Waterfall for a refreshing "
                    "swim. Drive to the iconic Tanah Lot sea temple — one "
                    "of Bali's most photographed landmarks. Afternoon at "
                    "the Jatiluwih rice terraces (UNESCO site). Sunset at "
                    "Tanah Lot."
                ),
            },
            {
                "day": 4,
                "title": "Uluwatu & Beach Day",
                "description": (
                    "Morning at leisure or optional Mount Batur sunrise "
                    "trek (early 2 AM start). Afternoon visit to the "
                    "dramatic clifftop Uluwatu Temple. Stay for the "
                    "mesmerising Kecak Fire Dance performance at sunset. "
                    "Seafood dinner at Jimbaran Bay beach."
                ),
            },
            {
                "day": 5,
                "title": "Departure",
                "description": (
                    "Morning spa treatment — traditional Balinese massage. "
                    "Last-minute shopping for silver jewellery, batik, and "
                    "organic products. Transfer to airport for departure."
                ),
            },
        ],
        "tips": [
            "Best time: April to October (dry season).",
            "Respect temple dress codes — sarongs are required.",
            "Rent a scooter for the full Bali experience (₹300/day).",
            "Ubud is cooler than the coast — carry a light jacket.",
            "Always carry small change for temple donations.",
        ],
    },
    "vietnam": {
        "name": "Vietnam",
        "country": "Vietnam",
        "hero_image": "vietnam.jpg",
        "duration": "6 Days / 5 Nights",
        "price_from": "₹38,000",
        "tagline": "Timeless Charm, Boundless Beauty",
        "overview": (
            "Vietnam is a country of staggering natural beauty and deep "
            "cultural richness. Cruise through the emerald waters of Ha "
            "Long Bay, wander the lantern-lit streets of Hoi An, savour "
            "the world's best phở, and discover a nation where ancient "
            "traditions thrive alongside buzzing modernity."
        ),
        "highlights": [
            "Ha Long Bay overnight cruise",
            "Hanoi Old Quarter & street food tour",
            "Hoi An Ancient Town & lantern market",
            "Ho Chi Minh City – War Museum & Cu Chi Tunnels",
            "Mekong Delta floating markets",
            "Sapa rice terraces & hill tribe villages",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival in Hanoi",
                "description": (
                    "Arrive at Noi Bai International Airport. Transfer to "
                    "your hotel in the atmospheric Old Quarter. Evening "
                    "walking tour — Hoan Kiem Lake, Ngoc Son Temple, and "
                    "the vibrant night market. Try egg coffee at a "
                    "traditional café."
                ),
            },
            {
                "day": 2,
                "title": "Hanoi City & Street Food",
                "description": (
                    "Morning visit to Ho Chi Minh Mausoleum, One Pillar "
                    "Pagoda, and the Temple of Literature. Afternoon at "
                    "the Vietnam Museum of Ethnology. Evening street food "
                    "tour — phở, bánh mì, bún chả, and more in the Old "
                    "Quarter's bustling alleys."
                ),
            },
            {
                "day": 3,
                "title": "Ha Long Bay Cruise",
                "description": (
                    "Early morning drive to Ha Long Bay. Board a "
                    "traditional junk boat for an overnight cruise through "
                    "thousands of limestone karsts rising from emerald "
                    "waters. Kayak through hidden caves, swim in secluded "
                    "lagoons, and enjoy a seafood dinner on deck under the "
                    "stars."
                ),
            },
            {
                "day": 4,
                "title": "Ha Long Bay & Fly to Hoi An",
                "description": (
                    "Sunrise tai chi on the boat deck. Continue cruising "
                    "through the bay, visit a floating fishing village. "
                    "Return to Hanoi and fly to Da Nang. Transfer to Hoi "
                    "An — check in and explore the lantern-lit Ancient "
                    "Town on foot."
                ),
            },
            {
                "day": 5,
                "title": "Hoi An – Ancient Charm",
                "description": (
                    "Morning visit to the Japanese Covered Bridge, Chinese "
                    "Assembly Halls, and local tailor shops (custom suits "
                    "in 24 hrs!). Afternoon cooking class — learn to make "
                    "bánh xèo and cao lầu. Evening boat ride on the Thu "
                    "Bon River releasing paper lanterns."
                ),
            },
            {
                "day": 6,
                "title": "Departure",
                "description": (
                    "Morning at An Bang Beach or cycle through rice "
                    "paddies. Pick up your custom tailoring orders. "
                    "Transfer to Da Nang airport for your departure flight. "
                    "Goodbye, Vietnam!"
                ),
            },
        ],
        "tips": [
            "Best time: October to April (cool, dry weather in the north).",
            "E-visa is available for Indian passport holders — apply online.",
            "Hanoi traffic is chaotic — walk steadily and traffic flows around you!",
            "Hoi An tailors can make custom suits/dresses overnight.",
            "Carry cash (Vietnamese Dong) — small shops don't accept cards.",
        ],
    },
    "kerala": {
        "name": "Kerala",
        "country": "India",
        "hero_image": "kerala.jpg",
        "duration": "5 Days / 4 Nights",
        "price_from": "₹22,000",
        "tagline": "God's Own Country",
        "overview": (
            "Kerala is India's most enchanting state — a sliver of paradise "
            "draped in lush backwaters, mist-clad hill stations, and pristine "
            "beaches. Glide through the serene Alleppey backwaters on a "
            "traditional houseboat, wander through Munnar's emerald tea "
            "gardens, and experience the timeless rhythms of Kathakali dance. "
            "Kerala is wellness, nature, and culture in one breathtaking package."
        ),
        "highlights": [
            "Alleppey Backwaters — overnight houseboat stay",
            "Munnar tea estates & Eravikulam National Park",
            "Thekkady — Periyar Tiger Reserve jungle safari",
            "Kovalam beach & Ayurvedic spa therapies",
            "Kathakali & Kalaripayattu cultural performances",
            "Varkala cliff beach & sunset views",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival in Kochi — The Queen of the Arabian Sea",
                "description": (
                    "Arrive at Cochin International Airport. Transfer to hotel. "
                    "Evening explore Fort Kochi — the iconic Chinese Fishing Nets, "
                    "Dutch Palace, Jew Town's antique lanes, and the atmospheric "
                    "Santa Cruz Basilica. Enjoy a seafood dinner by the waterfront."
                ),
            },
            {
                "day": 2,
                "title": "Munnar — Tea Country Escape",
                "description": (
                    "Drive to Munnar (3.5 hrs) through winding mountain roads. "
                    "Visit the Tata Tea Museum to learn about Kerala's famed "
                    "tea culture. Afternoon walk through rolling tea estates at "
                    "Top Station. Evening at leisure in the cool hill air."
                ),
            },
            {
                "day": 3,
                "title": "Thekkady — Wild Encounters",
                "description": (
                    "Morning visit to Eravikulam National Park — spot the "
                    "endangered Nilgiri Tahr. Drive to Thekkady. Afternoon "
                    "spice plantation tour and boat safari on Periyar Lake "
                    "inside the Tiger Reserve. Evening Kathakali performance "
                    "— the mesmerising classical dance of Kerala."
                ),
            },
            {
                "day": 4,
                "title": "Alleppey — Houseboat Paradise",
                "description": (
                    "Drive to Alleppey (Alappuzha). Check in to a traditional "
                    "kettuvallam (rice boat) houseboat. Cruise through the "
                    "legendary backwaters — emerald canals, paddy fields, "
                    "village life, and abundant birdlife. Sunset over the water, "
                    "followed by a chef-prepared Kerala feast on board. Overnight "
                    "on the houseboat."
                ),
            },
            {
                "day": 5,
                "title": "Kovalam Beach & Departure",
                "description": (
                    "Morning disembarkation. Drive to Kovalam Beach. Enjoy a "
                    "traditional Ayurvedic massage before lunch. Afternoon at "
                    "leisure at the crescent beach. Transfer to Trivandrum "
                    "International Airport for departure."
                ),
            },
        ],
        "tips": [
            "Best time: September to March (post-monsoon — lush and green).",
            "Book houseboats well in advance — they fill up quickly in season.",
            "Try the Kerala sadya (banana leaf meal) for an authentic experience.",
            "Carry mosquito repellent for backwater regions.",
            "Respect temple dress codes — cover shoulders and knees.",
        ],
    },
    "rajasthan": {
        "name": "Rajasthan",
        "country": "India",
        "hero_image": "rajasthan.jpg",
        "duration": "6 Days / 5 Nights",
        "price_from": "₹25,000",
        "tagline": "Land of Maharajas & Desert Splendour",
        "overview": (
            "Rajasthan is India's most regal state — a vast canvas of "
            "sun-baked forts, jewel-toned palaces, and golden deserts. "
            "Wander through the blue lanes of Jodhpur, float on a boat "
            "beneath the fairy-tale Lake Palace of Udaipur, and ride a "
            "camel into the dunes of Jaisalmer as the sun melts into the "
            "horizon. Rajasthan is a living, breathing storybook."
        ),
        "highlights": [
            "Amber Fort & Jaipur's Pink City palaces",
            "Udaipur's Lake Pichola & City Palace",
            "Jaisalmer Golden Fort & desert dune safari",
            "Jodhpur's Mehrangarh Fort & blue city lanes",
            "Pushkar camel fair & Brahma Temple",
            "Traditional Rajasthani folk dance & cuisine",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival in Jaipur — The Pink City",
                "description": (
                    "Arrive in Jaipur. Transfer to hotel. Evening visit Hawa "
                    "Mahal (Palace of Winds) for the iconic pink facade. "
                    "Explore the colourful bazaars of Johari Bazaar. Dinner "
                    "featuring Dal Baati Churma, the quintessential Rajasthani meal."
                ),
            },
            {
                "day": 2,
                "title": "Jaipur — Forts, Palaces & Gems",
                "description": (
                    "Morning elephant or jeep ride up to the magnificent "
                    "Amber Fort. Visit the Sheesh Mahal (Mirror Palace) within. "
                    "Afternoon at Jaipur's City Palace Museum and the "
                    "astronomical marvel of Jantar Mantar. Optional shopping "
                    "for gemstones, blue pottery, and block-print textiles."
                ),
            },
            {
                "day": 3,
                "title": "Jaipur to Jodhpur — The Blue City",
                "description": (
                    "Drive to Jodhpur (5 hrs). En route, stop at Ajmer's "
                    "Dargah Sharif. Check in. Afternoon explore the labyrinthine "
                    "blue lanes of the Old City. Sunset at the towering "
                    "Mehrangarh Fort with panoramic desert views. "
                    "Evening rooftop dinner overlooking the blue city."
                ),
            },
            {
                "day": 4,
                "title": "Jodhpur to Jaisalmer — Desert City",
                "description": (
                    "Drive to Jaisalmer (4.5 hrs). Arrive and check in. "
                    "Afternoon explore the golden sandstone Jaisalmer Fort — "
                    "one of the world's largest living forts. Walk through the "
                    "ornate Patwon ki Haveli mansions. Evening at Gadisar Lake."
                ),
            },
            {
                "day": 5,
                "title": "Desert Safari & Camp Under Stars",
                "description": (
                    "Full day Thar Desert experience. Camel safari over golden "
                    "dunes to Sam Sand Dunes. Watch the sunset from atop the "
                    "highest dune. Evening at a luxury desert camp — folk music, "
                    "bonfire, Rajasthani dinner, and stargazing. Optional "
                    "quad biking on the dunes."
                ),
            },
            {
                "day": 6,
                "title": "Udaipur — City of Lakes & Departure",
                "description": (
                    "Drive to Udaipur or fly. Visit the enchanting City Palace "
                    "complex and take a sunset boat ride on Lake Pichola "
                    "to admire the floating Lake Palace. Browse the Hathi Pol "
                    "bazaar for traditional jewellery. Transfer to airport."
                ),
            },
        ],
        "tips": [
            "Best time: October to March (cool desert evenings).",
            "Carry a warm layer — desert nights can be surprisingly cold.",
            "Book desert camp stays in advance during peak season (Nov–Jan).",
            "Bargain at bazaars — vendors expect negotiation.",
            "Try laal maas (fiery mutton curry) — Rajasthan's signature dish.",
        ],
    },
    "goa": {
        "name": "Goa",
        "country": "India",
        "hero_image": "goa.jpg",
        "duration": "4 Days / 3 Nights",
        "price_from": "₹18,000",
        "tagline": "Sun, Sand, Spice & Soul",
        "overview": (
            "Goa is India's most beloved beach destination — a laid-back "
            "paradise where Portuguese colonial charm meets tropical coastline. "
            "From the boisterous nightlife of North Goa to the tranquil, "
            "palm-fringed beaches of the South, Goa offers something for every "
            "soul — surfers, foodies, party-goers, and seekers of pure relaxation."
        ),
        "highlights": [
            "North Goa beaches — Baga, Calangute & Anjuna",
            "South Goa — Palolem & Agonda secluded beaches",
            "Old Goa's UNESCO churches — Se Cathedral & Basilica of Bom Jesus",
            "Dudhsagar Waterfalls jungle trek",
            "Spice plantation tour & traditional Goan lunch",
            "Casino nights & beach shack sundowners",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival & North Goa Beach Vibes",
                "description": (
                    "Arrive at Goa International Airport. Transfer to hotel. "
                    "Afternoon at Baga or Calangute Beach. Rent a scooter and "
                    "cruise along the coastline. Evening at Tito's Lane or the "
                    "Anjuna flea market. Seafood dinner at a beachfront shack."
                ),
            },
            {
                "day": 2,
                "title": "Heritage Goa & Waterfalls",
                "description": (
                    "Morning visit to Old Goa — the magnificent Se Cathedral "
                    "and Basilica of Bom Jesus (housing St. Francis Xavier's "
                    "remains). Afternoon jeep safari to the spectacular "
                    "Dudhsagar Waterfalls — one of India's tallest. Swim in "
                    "the natural pool at the base. Evening spice plantation "
                    "tour with traditional Goan dinner."
                ),
            },
            {
                "day": 3,
                "title": "South Goa Serenity",
                "description": (
                    "Drive to peaceful South Goa. Spend the day at Palolem "
                    "or Agonda Beach — some of India's most pristine sands. "
                    "Optional kayaking through mangroves or dolphin-watching "
                    "boat trip. Sunset yoga session on the beach. "
                    "Candlelit seafood dinner."
                ),
            },
            {
                "day": 4,
                "title": "Morning Dip & Departure",
                "description": (
                    "Last morning swim or sunrise walk on the beach. Browse "
                    "the Saturday Night Market or Mapusa Market for Goan "
                    "cashews, spices, and feni (local spirit). Transfer to "
                    "airport for departure."
                ),
            },
        ],
        "tips": [
            "Best time: November to February (peak season, perfect weather).",
            "Rent a scooter — it's the most fun way to explore Goa (₹350/day).",
            "Try Goan fish curry rice at a local restaurant — not a resort.",
            "Stay in South Goa for peace, North Goa for nightlife.",
            "Keep valuables locked at the hotel when going to the beach.",
        ],
    },
    "kashmir": {
        "name": "Kashmir",
        "country": "India",
        "hero_image": "kashmir.jpg",
        "duration": "5 Days / 4 Nights",
        "price_from": "₹28,000",
        "tagline": "Paradise on Earth",
        "overview": (
            "Kashmir is nothing short of heaven on earth. Emerald lakes "
            "mirror snow-capped Himalayan peaks, saffron fields blaze at "
            "sunrise, and shikaras drift silently across the legendary "
            "Dal Lake. From the flowered gardens of Srinagar to the "
            "snow-dusted valleys of Gulmarg and Pahalgam, Kashmir is a "
            "destination that permanently captures your heart."
        ),
        "highlights": [
            "Dal Lake — shikara ride & houseboat stay",
            "Gulmarg — Gondola cable car & snowfields",
            "Pahalgam — Betaab Valley & Aru Valley",
            "Srinagar's Mughal Gardens — Shalimar Bagh & Nishat Bagh",
            "Shopping for Pashmina shawls & Kashmiri handicrafts",
            "Sonamarg — Thajiwas Glacier snow trek",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival in Srinagar — Dal Lake Welcome",
                "description": (
                    "Arrive at Sheikh ul-Alam International Airport. Transfer "
                    "to your luxury houseboat on Dal Lake. Evening shikara "
                    "ride across the glassy lake — past floating gardens, "
                    "vegetable markets, and the golden Hazratbal Shrine "
                    "reflected in the water."
                ),
            },
            {
                "day": 2,
                "title": "Mughal Gardens & Srinagar Bazaars",
                "description": (
                    "Morning visit to the magnificent Mughal Gardens — "
                    "Shalimar Bagh, Nishat Bagh, and Chashme Shahi (Royal "
                    "Spring). Afternoon explore Srinagar's old bazaars for "
                    "Kashmiri Pashmina shawls, papier-mâché crafts, and "
                    "precious saffron. Evening traditional wazwan dinner."
                ),
            },
            {
                "day": 3,
                "title": "Gulmarg — Snow World",
                "description": (
                    "Drive to Gulmarg (56 km). Ride Asia's highest cable car "
                    "— the Gulmarg Gondola — up to 4,000 metres. Walk on snow, "
                    "sledge, or ski (seasonal). The panoramic Himalayan views "
                    "are simply unmatchable. Return to Srinagar in the evening."
                ),
            },
            {
                "day": 4,
                "title": "Pahalgam — Valley of Shepherds",
                "description": (
                    "Drive to Pahalgam. Visit the stunning Betaab Valley "
                    "(filming location of Bollywood blockbusters) and "
                    "the serene Aru Valley. Horse riding along the Lidder River. "
                    "Walk through pine forests to Baisaran — 'Mini Switzerland' "
                    "of India."
                ),
            },
            {
                "day": 5,
                "title": "Sonamarg & Departure",
                "description": (
                    "Morning excursion to Sonamarg ('Meadow of Gold') — "
                    "pony trek to the Thajiwas Glacier. Enjoy the surreal "
                    "snowfields against a backdrop of pristine alpine meadows. "
                    "Return to Srinagar for last-minute shopping. Transfer "
                    "to airport for departure."
                ),
            },
        ],
        "tips": [
            "Best time: March–June (spring blooms) & Oct (autumn foliage).",
            "Carry warm layers even in summer — temperatures drop at night.",
            "Book houseboats directly to avoid middlemen overcharging.",
            "Check current travel advisories before booking.",
            "Buy authentic Pashmina — look for the Pashmina Craft Mark label.",
        ],
    },
    "andaman": {
        "name": "Andaman",
        "country": "India",
        "hero_image": "andaman.jpg",
        "duration": "5 Days / 4 Nights",
        "price_from": "₹30,000",
        "tagline": "Jewel of the Indian Ocean",
        "overview": (
            "The Andaman Islands are India's best-kept tropical secret — "
            "a remote archipelago where turquoise waters meet white-sand "
            "beaches fringed by primeval rainforest. World-class snorkelling "
            "and scuba diving reveal vibrant coral reefs, while the haunting "
            "Cellular Jail tells India's most powerful story of freedom and "
            "sacrifice. Andaman is raw, wild, and utterly breathtaking."
        ),
        "highlights": [
            "Radhanagar Beach — Asia's finest beach",
            "Scuba diving & snorkelling at Elephant Beach",
            "Cellular Jail & Sound & Light Show",
            "Ross Island — colonial ruins & deer park",
            "Neil Island — tranquil beaches & coral reefs",
            "Sea-walking & glass-bottom boat rides",
        ],
        "itinerary": [
            {
                "day": 1,
                "title": "Arrival in Port Blair — Gateway to Paradise",
                "description": (
                    "Arrive at Veer Savarkar International Airport. Transfer "
                    "to hotel. Afternoon visit the sobering Cellular Jail — "
                    "where India's freedom fighters were imprisoned. Attend "
                    "the moving Sound & Light Show commemorating their sacrifice. "
                    "Dinner at a waterfront restaurant."
                ),
            },
            {
                "day": 2,
                "title": "Ross Island & North Bay — Colonial Charm",
                "description": (
                    "Morning ferry to Ross Island — explore the atmospheric "
                    "ruins of the former British HQ, now inhabited by spotted "
                    "deer and peacocks. Afternoon at North Bay Island for "
                    "sea-walking, snorkelling, and a glass-bottom boat ride "
                    "over colourful coral gardens."
                ),
            },
            {
                "day": 3,
                "title": "Havelock Island — Radhanagar Beach",
                "description": (
                    "Ferry to Havelock Island. Check in to your beach resort. "
                    "Afternoon at the legendary Radhanagar Beach — rated one "
                    "of Asia's finest beaches by TIME magazine. Crystal-clear "
                    "turquoise water, pristine white sand, and a "
                    "breathtaking sunset. Evening bonfire on the beach."
                ),
            },
            {
                "day": 4,
                "title": "Elephant Beach — Marine Paradise",
                "description": (
                    "Morning boat trip to Elephant Beach for world-class "
                    "snorkelling — swim among parrotfish, clownfish, and "
                    "manta rays in crystal waters. Optional beginner scuba "
                    "dive (no experience needed). Afternoon kayaking through "
                    "the mangroves. Evening at leisure."
                ),
            },
            {
                "day": 5,
                "title": "Neil Island Visit & Departure",
                "description": (
                    "Morning ferry to the tranquil Neil Island — visit the "
                    "natural rock formation 'Howrah Bridge' and Laxmanpur "
                    "Beach for a final snorkel. Ferry back to Port Blair. "
                    "Last-minute shopping for black pearls and coral jewellery. "
                    "Transfer to airport for departure."
                ),
            },
        ],
        "tips": [
            "Best time: October to May (seas are calm and visibility is good).",
            "Book inter-island ferries in advance — they sell out in season.",
            "Carry reef-safe sunscreen to protect the coral ecosystem.",
            "Keep some cash — ATMs can be unreliable on remote islands.",
            "The Andaman is alcohol-friendly — unlike most of India's islands.",
        ],
    },
}

# ── Travel Tips Data ────────────────────────────────────────────────────────
TRAVEL_TIPS = [
    {
        "icon": "🧳",
        "category": "Packing Smart",
        "tips": [
            "Roll your clothes to save space and prevent wrinkles.",
            "Always pack a universal adapter and portable charger.",
            "Carry a lightweight rain jacket — weather can be unpredictable.",
            "Keep a photocopy of your passport and visa separately.",
            "Pack a small first-aid kit with basics: band-aids, painkillers, anti-allergy.",
        ],
    },
    {
        "icon": "📄",
        "category": "Visa & Documents",
        "tips": [
            "Check visa requirements at least 2 months before travel.",
            "Keep digital copies of all documents in cloud storage.",
            "Ensure your passport is valid for at least 6 months beyond travel dates.",
            "Print hotel booking confirmations — some immigration counters ask for them.",
            "Register with your embassy if travelling to remote areas.",
        ],
    },
    {
        "icon": "💰",
        "category": "Budget & Money",
        "tips": [
            "Use a forex card instead of carrying large amounts of cash.",
            "Notify your bank before international travel to avoid card blocks.",
            "Set a daily budget — track expenses with a simple app.",
            "Eat where locals eat — the food is better and cheaper!",
            "Book flights and hotels in advance for the best deals.",
        ],
    },
    {
        "icon": "🛡️",
        "category": "Safety & Health",
        "tips": [
            "Purchase comprehensive travel insurance — it's non-negotiable.",
            "Share your itinerary with a trusted family member.",
            "Stay hydrated, especially in tropical destinations.",
            "Avoid displaying expensive jewellery or electronics openly.",
            "Research local emergency numbers before you arrive.",
        ],
    },
    {
        "icon": "📸",
        "category": "Photography & Memories",
        "tips": [
            "Wake up early — golden hour light makes everything magical.",
            "Respect local customs — always ask before photographing people.",
            "Back up your photos to the cloud every night.",
            "Put the camera down sometimes and just soak in the moment.",
            "Capture the small details — food, signs, textures tell a story.",
        ],
    },
    {
        "icon": "✈️",
        "category": "Flight & Airport",
        "tips": [
            "Download your airline's app for mobile boarding passes.",
            "Arrive at least 3 hours before international flights.",
            "Carry an empty water bottle — fill it after security.",
            "Wear comfortable shoes — you'll walk a lot at airports.",
            "Noise-cancelling headphones are a game-changer on long flights.",
        ],
    },
    {
        "icon": "🌍",
        "category": "Visa & Entry Requirements",
        "tips": [
            "Apply for your visa at least 6–8 weeks before departure.",
            "Many countries offer e-Visa or visa-on-arrival for Indian passport holders — check official embassy sites.",
            "Always carry printed copies of your visa approval along with digital backups.",
            "Ensure your passport has at least two blank pages for stamps.",
            "Some countries require proof of onward travel — have your return flight booking ready.",
        ],
    },
    {
        "icon": "💱",
        "category": "Currency & Forex",
        "tips": [
            "Buy foreign currency from authorised RBI-licensed money changers for the best rates.",
            "A multi-currency forex card is safer and more cost-effective than carrying cash.",
            "Inform your bank about your travel dates to prevent card blocks at ATMs abroad.",
            "Avoid exchanging currency at airports — rates are significantly worse.",
            "Always keep a small amount of local currency for tips, taxis, and emergencies.",
        ],
    },
    {
        "icon": "🍜",
        "category": "Food & Local Culture",
        "tips": [
            "Eat where the locals eat — the best food is never at the tourist-facing restaurants.",
            "Learn 5–10 basic words in the local language — it opens doors and wins smiles.",
            "Always ask before photographing people, religious sites, or private property.",
            "Try street food cautiously — go for stalls with high turnover and fresh cooking.",
            "Respect local dress codes, especially at temples, mosques, and sacred sites.",
        ],
    },
    {
        "icon": "🚫",
        "category": "Things to Avoid",
        "tips": [
            "Never leave your luggage unattended at airports or train stations.",
            "Avoid accepting food or drinks from strangers on overnight trains or buses.",
            "Don't flash expensive cameras, jewellery, or large amounts of cash in public.",
            "Avoid booking tours through random touts — always use your hotel or trusted operators.",
            "Don't post real-time updates of your location on social media while travelling.",
        ],
    },
]


# ── Testimonials ────────────────────────────────────────────────────────────
TESTIMONIALS = [
    {
        "name": "Priya Sharma",
        "location": "Delhi",
        "rating": 5,
        "destination": "Dubai",
        "review": (
            "Aara Voyages made our Dubai trip absolutely magical! Every detail "
            "was taken care of — from the airport pickup to the desert safari. "
            "Our relationship manager was just a call away at all times. Highly recommended!"
        ),
        "initials": "PS",
    },
    {
        "name": "Rahul & Meena Gupta",
        "location": "Mumbai",
        "rating": 5,
        "destination": "Bali",
        "review": (
            "We celebrated our honeymoon in Bali with Aara Voyages and it was "
            "beyond our dreams. The villa, the temple tours, the Kecak dance at "
            "Uluwatu — every single moment was curated with love. Thank you!"
        ),
        "initials": "RG",
    },
    {
        "name": "Ankit Verma",
        "location": "Bangalore",
        "rating": 5,
        "destination": "Kerala",
        "review": (
            "The Kerala backwater houseboat experience organised by Aara Voyages "
            "was worth every rupee. Seamless planning, lovely accommodations, and "
            "the most delicious food I've ever had on a trip. Will book again!"
        ),
        "initials": "AV",
    },
    {
        "name": "Sunita Kapoor",
        "location": "Pune",
        "rating": 5,
        "destination": "Singapore",
        "review": (
            "First international trip for our family and Aara Voyages made it "
            "stress-free! The kids loved Universal Studios, I loved the food trail, "
            "and my husband loved the value for money. 10/10 experience."
        ),
        "initials": "SK",
    },
    {
        "name": "Vikram Singh",
        "location": "Jaipur",
        "rating": 5,
        "destination": "Vietnam",
        "review": (
            "Vietnam was on my bucket list for years. Aara Voyages turned that "
            "dream into a flawless 6-day adventure. The Ha Long Bay cruise was "
            "the highlight — absolutely stunning. Professional, reliable, and warm."
        ),
        "initials": "VS",
    },
    {
        "name": "Deepa Nair",
        "location": "Chennai",
        "rating": 5,
        "destination": "Kashmir",
        "review": (
            "Kashmir in spring with the tulip gardens in bloom — I cannot find "
            "words for how beautiful it was. Aara Voyages planned everything "
            "perfectly. The houseboat on Dal Lake was an experience of a lifetime!"
        ),
        "initials": "DN",
    },
]

# ── Routes ──────────────────────────────────────────────────────────────────
@app.context_processor
def inject_brand():
    """Make brand info available in every template."""
    return {"brand": BRAND, "destinations_data": DESTINATIONS}


@app.route("/")
def home():
    return render_template(
        "home.html",
        destinations=DESTINATIONS,
        testimonials=TESTIMONIALS,
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/destinations")
def destinations():
    return render_template("destinations.html", destinations=DESTINATIONS)


@app.route("/destination/<slug>")
def destination_detail(slug):
    dest = DESTINATIONS.get(slug)
    if not dest:
        return render_template("404.html"), 404
    return render_template("destination_detail.html", dest=dest, slug=slug)


@app.route("/tips")
def tips():
    return render_template("tips.html", tips=TRAVEL_TIPS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ── Hotels Data ──────────────────────────────────────────────────────────────
HOTELS = [
    # =========== INTERNATIONAL ===========
    # Dubai
    {"id":"h-dubai-budget","destination":"dubai","dest_label":"Dubai, UAE","category":"international","name":"Rove City Centre Hotel","stars":3,"location":"Deira, Dubai","price_per_night":4800,"price_display":"₹4,800/night","image":"dubai.jpg","amenities":["Free WiFi","Breakfast Included","Swimming Pool","Gym","City View"],"highlights":"Located in the heart of Deira, walking distance to Dubai Metro, Gold Souk and Dubai Mall. Modern rooms with Arabian touches."},
    {"id":"h-dubai-standard","destination":"dubai","dest_label":"Dubai, UAE","category":"international","name":"Radisson Blu Hotel Dubai Waterfront","stars":4,"location":"Business Bay, Dubai","price_per_night":8500,"price_display":"₹8,500/night","image":"dubai.jpg","amenities":["Free WiFi","Breakfast + Dinner","Rooftop Pool","Spa","Burj Khalifa View","Airport Transfer"],"highlights":"Stunning Burj Khalifa views from the rooftop pool. Steps from the Dubai Canal and Business Bay. Ideal for couples and families."},
    {"id":"h-dubai-luxury","destination":"dubai","dest_label":"Dubai, UAE","category":"international","name":"Atlantis The Palm","stars":5,"location":"Palm Jumeirah, Dubai","price_per_night":22000,"price_display":"₹22,000/night","image":"dubai.jpg","amenities":["All Meals","Aquaventure Waterpark Access","Private Beach","Dolphin Bay","Butler Service","Helicopter Transfers"],"highlights":"Iconic ultra-luxury resort on Palm Jumeirah. Home to the Aquaventure Waterpark, Dolphin Bay & 23 world-class restaurants. Pure indulgence."},

    # Singapore
    {"id":"h-singapore-budget","destination":"singapore","dest_label":"Singapore","category":"international","name":"Hotel Boss Singapore","stars":3,"location":"Lavender, Singapore","price_per_night":5500,"price_display":"₹5,500/night","image":"singapore.jpg","amenities":["Free WiFi","Rooftop Pool","City View","Near MRT","Air Conditioning"],"highlights":"Modern budget hotel with rooftop pool, a short MRT ride from Marina Bay Sands and Gardens by the Bay."},
    {"id":"h-singapore-standard","destination":"singapore","dest_label":"Singapore","category":"international","name":"Marriott Tangs Plaza Hotel","stars":4,"location":"Orchard Road, Singapore","price_per_night":11000,"price_display":"₹11,000/night","image":"singapore.jpg","amenities":["Free WiFi","Breakfast Included","Pool","Gym","Orchard Road Shopping","Concierge"],"highlights":"Prime location on the iconic Orchard Road shopping belt. Elegant rooms with Singapore skyline views."},
    {"id":"h-singapore-luxury","destination":"singapore","dest_label":"Singapore","category":"international","name":"Marina Bay Sands","stars":5,"location":"Marina Bay, Singapore","price_per_night":28000,"price_display":"₹28,000/night","image":"singapore.jpg","amenities":["Infinity Rooftop Pool","All Meals","Casino Access","Shoppes at MBS","Sands SkyPark","Butler Service"],"highlights":"World-famous infinity pool on the 57th floor. Unmatched views of Singapore's skyline. The ultimate luxury experience in Southeast Asia."},

    # Bali
    {"id":"h-bali-budget","destination":"bali","dest_label":"Bali, Indonesia","category":"international","name":"Alam Kul Kul Resort","stars":3,"location":"Kuta Beach, Bali","price_per_night":3200,"price_display":"₹3,200/night","image":"bali.jpg","amenities":["Free WiFi","Breakfast Included","Pool","Steps from Beach","Garden View"],"highlights":"Tropical garden resort steps from Kuta Beach. Ideal base to explore Bali's temples, markets and nightlife."},
    {"id":"h-bali-standard","destination":"bali","dest_label":"Bali, Indonesia","category":"international","name":"The Layar Private Villas","stars":4,"location":"Seminyak, Bali","price_per_night":7800,"price_display":"₹7,800/night","image":"bali.jpg","amenities":["Private Pool Villa","Breakfast Included","Butler Service","Spa","Airport Transfer","Beach Club Access"],"highlights":"Stunning private pool villas in the heart of Seminyak. Perfect for couples and honeymooners seeking a romantic tropical escape."},
    {"id":"h-bali-luxury","destination":"bali","dest_label":"Bali, Indonesia","category":"international","name":"COMO Uma Ubud","stars":5,"location":"Ubud, Bali","price_per_night":18500,"price_display":"₹18,500/night","image":"bali.jpg","amenities":["All Meals","Infinity Valley Pool","Spa & Wellness","Yoga Studio","Jungle View","Private Butler"],"highlights":"Nestled in the lush jungles of Ubud. Breathtaking valley views, world-renowned COMO Shambhala spa and organic farm-to-table dining."},

    # Malaysia
    {"id":"h-malaysia-budget","destination":"malaysia","dest_label":"Kuala Lumpur, Malaysia","category":"international","name":"Aloft Kuala Lumpur Sentral","stars":3,"location":"KL Sentral, Kuala Lumpur","price_per_night":4200,"price_display":"₹4,200/night","image":"malaysia.jpg","amenities":["Free WiFi","Rooftop Pool","Gym","Connected to KL Sentral Station","Air Conditioning"],"highlights":"Vibrant hotel connected directly to KL Sentral, the hub of KL's transport network. Easy access to all major attractions."},
    {"id":"h-malaysia-standard","destination":"malaysia","dest_label":"Kuala Lumpur, Malaysia","category":"international","name":"Traders Hotel Kuala Lumpur","stars":4,"location":"KLCC, Kuala Lumpur","price_per_night":8800,"price_display":"₹8,800/night","image":"malaysia.jpg","amenities":["Free WiFi","Breakfast Included","Pool","Petronas Towers View","Gym","Sky Bar"],"highlights":"Directly connected to Suria KLCC mall with unparalleled Petronas Twin Towers views from the rooftop Sky Bar."},
    {"id":"h-malaysia-luxury","destination":"malaysia","dest_label":"Kuala Lumpur, Malaysia","category":"international","name":"Mandarin Oriental Kuala Lumpur","stars":5,"location":"KLCC, Kuala Lumpur","price_per_night":19000,"price_display":"₹19,000/night","image":"malaysia.jpg","amenities":["All Meals","Petronas Towers View","Spa","Butler Service","Infinity Pool","Fine Dining"],"highlights":"Exquisite luxury at the foot of the Petronas Twin Towers. Mandarin Oriental's legendary service paired with KL's most iconic views."},

    # Vietnam
    {"id":"h-vietnam-budget","destination":"vietnam","dest_label":"Vietnam","category":"international","name":"Hanoi La Siesta Hotel","stars":3,"location":"Old Quarter, Hanoi","price_per_night":2800,"price_display":"₹2,800/night","image":"vietnam.jpg","amenities":["Free WiFi","Breakfast Included","Rooftop Bar","Old Quarter Location","Air Conditioning"],"highlights":"Charming boutique hotel in the heart of Hanoi's Old Quarter. Walk to Hoan Kiem Lake and street food stalls."},
    {"id":"h-vietnam-standard","destination":"vietnam","dest_label":"Vietnam","category":"international","name":"Anantara Hoi An Resort","stars":4,"location":"Hoi An Ancient Town","price_per_night":7200,"price_display":"₹7,200/night","image":"vietnam.jpg","amenities":["Free WiFi","Breakfast + Dinner","Pool","River View","Cooking Class","Spa"],"highlights":"Elegant resort on the banks of the Thu Bon River, minutes from Hoi An Ancient Town. Authentic Vietnamese hospitality."},
    {"id":"h-vietnam-luxury","destination":"vietnam","dest_label":"Vietnam","category":"international","name":"InterContinental Sun Peninsula Danang","stars":5,"location":"Monkey Mountain, Danang","price_per_night":21000,"price_display":"₹21,000/night","image":"vietnam.jpg","amenities":["All Meals","Private Beach","Infinity Pool","Funicular","Spa","Butler Service"],"highlights":"Dramatic cliffside resort on Monkey Mountain with private beach. Reached by private funicular. Vietnam's most spectacular luxury escape."},

    # =========== DOMESTIC ===========
    # Kerala
    {"id":"h-kerala-budget","destination":"kerala","dest_label":"Kerala, India","category":"domestic","name":"Fragrant Nature Kochi","stars":3,"location":"Kochi, Kerala","price_per_night":3500,"price_display":"₹3,500/night","image":"kerala.jpg","amenities":["Free WiFi","Breakfast Included","Pool","Near Fort Kochi","Air Conditioning"],"highlights":"Eco-friendly hotel near Fort Kochi's famous fishing nets, Chinese fishing nets, and colonial heritage."},
    {"id":"h-kerala-standard","destination":"kerala","dest_label":"Kerala, India","category":"domestic","name":"Zuri Kumarakom Kerala Resort","stars":4,"location":"Kumarakom, Kerala","price_per_night":9500,"price_display":"₹9,500/night","image":"kerala.jpg","amenities":["Breakfast Included","Pool","Backwater View","Ayurvedic Spa","Shikara Ride","Airport Transfer"],"highlights":"Serene backwater resort on Vembanad Lake. Stunning views of the Kerala backwaters from every room and the infinity pool."},
    {"id":"h-kerala-luxury","destination":"kerala","dest_label":"Kerala, India","category":"domestic","name":"Taj Kumarakom Resort & Spa","stars":5,"location":"Kumarakom, Kerala","price_per_night":22000,"price_display":"₹22,000/night","image":"kerala.jpg","amenities":["All Meals","Private Houseboat","Ayurvedic Spa","Infinity Pool","Butler Service","Cooking Classes"],"highlights":"Kerala's finest luxury resort with villas that open onto the backwaters. The Taj Ayurvedic spa offers transformative wellness experiences."},

    # Rajasthan
    {"id":"h-rajasthan-budget","destination":"rajasthan","dest_label":"Rajasthan, India","category":"domestic","name":"Hotel Bissau Palace Jaipur","stars":3,"location":"Jaipur, Rajasthan","price_per_night":3800,"price_display":"₹3,800/night","image":"rajasthan.jpg","amenities":["Free WiFi","Breakfast Included","Pool","Heritage Property","Near Pink City"],"highlights":"A 250-year-old heritage haveli in the heart of Jaipur. Experience royal Rajputana hospitality at budget prices."},
    {"id":"h-rajasthan-standard","destination":"rajasthan","dest_label":"Rajasthan, India","category":"domestic","name":"Raas Jodhpur","stars":4,"location":"Jodhpur, Rajasthan","price_per_night":12500,"price_display":"₹12,500/night","image":"rajasthan.jpg","amenities":["Breakfast + Dinner","Mehrangarh Fort View","Pool","Heritage Tours","Spa","Airport Transfer"],"highlights":"Boutique heritage hotel at the base of Mehrangarh Fort. Dramatic blue city views and award-winning architecture."},
    {"id":"h-rajasthan-luxury","destination":"rajasthan","dest_label":"Rajasthan, India","category":"domestic","name":"Umaid Bhawan Palace Jodhpur","stars":5,"location":"Jodhpur, Rajasthan","price_per_night":45000,"price_display":"₹45,000/night","image":"rajasthan.jpg","amenities":["All Meals","Museum Access","Heritage Gardens","Spa","Vintage Car Tours","Billiard Room","Butler Service"],"highlights":"Live like a Maharaja at one of the world's finest palace hotels. Part of the Taj Hotels family, Umaid Bhawan is pure regal grandeur."},

    # Goa
    {"id":"h-goa-budget","destination":"goa","dest_label":"Goa, India","category":"domestic","name":"Mango Tree Goa","stars":3,"location":"Calangute Beach, Goa","price_per_night":2800,"price_display":"₹2,800/night","image":"goa.jpg","amenities":["Free WiFi","Breakfast Included","Pool","Near Beach","Air Conditioning"],"highlights":"Bright and airy hotel minutes from Calangute Beach. Perfect base for exploring North Goa's beaches, markets and nightlife."},
    {"id":"h-goa-standard","destination":"goa","dest_label":"Goa, India","category":"domestic","name":"Alila Diwa Goa","stars":4,"location":"Majorda Beach, South Goa","price_per_night":8200,"price_display":"₹8,200/night","image":"goa.jpg","amenities":["Breakfast + Dinner","Pool","Private Beach","Spa","Water Sports","Airport Transfer"],"highlights":"South Goa's crown jewel. Breathtaking paddy field views, pristine private beach, and the award-winning Spa Alila."},
    {"id":"h-goa-luxury","destination":"goa","dest_label":"Goa, India","category":"domestic","name":"Taj Exotica Resort & Spa Goa","stars":5,"location":"Benaulim Beach, South Goa","price_per_night":18000,"price_display":"₹18,000/night","image":"goa.jpg","amenities":["All Meals","Private Beach","Infinity Pool","Jiva Spa","Butler Service","Water Sports","Fine Dining"],"highlights":"Sprawling beachfront luxury resort in South Goa. The Jiva Spa, multiple dining venues, and private beach make it Goa's finest retreat."},

    # Kashmir
    {"id":"h-kashmir-budget","destination":"kashmir","dest_label":"Kashmir, India","category":"domestic","name":"Houseboat Heritage Palace","stars":3,"location":"Dal Lake, Srinagar","price_per_night":4200,"price_display":"₹4,200/night","image":"kashmir.jpg","amenities":["Breakfast + Dinner","Dal Lake View","Shikara Ride Included","Carved Wood Interiors","Bonfire Evening"],"highlights":"Authentic cedar wood houseboat on Dal Lake. Wake up to misty Himalayan views and morning shikara rides."},
    {"id":"h-kashmir-standard","destination":"kashmir","dest_label":"Kashmir, India","category":"domestic","name":"The Lalit Grand Palace Srinagar","stars":4,"location":"Dal Lake, Srinagar","price_per_night":11000,"price_display":"₹11,000/night","image":"kashmir.jpg","amenities":["Breakfast Included","Dal Lake Garden","Pool","Heritage Building","Mountain View","Spa"],"highlights":"A 19th century royal palace turned luxury hotel with sweeping Dal Lake and Zabarwan mountain views. Historic grandeur meets modern comfort."},
    {"id":"h-kashmir-luxury","destination":"kashmir","dest_label":"Kashmir, India","category":"domestic","name":"Vivanta Dal View Srinagar","stars":5,"location":"Dal Lake, Srinagar","price_per_night":19500,"price_display":"₹19,500/night","image":"kashmir.jpg","amenities":["All Meals","Private Shikara","Dal Lake Suite","Spa","Heli-Excursion Available","Butler Service"],"highlights":"The ultimate Kashmir luxury experience. Private shikara at your doorstep, floating flower markets, and incomparable Dal Lake panoramas."},

    # Andaman
    {"id":"h-andaman-budget","destination":"andaman","dest_label":"Andaman, India","category":"domestic","name":"Sea Shell Port Blair","stars":3,"location":"Port Blair, Andaman","price_per_night":3600,"price_display":"₹3,600/night","image":"andaman.jpg","amenities":["Free WiFi","Breakfast Included","Pool","Near Cellular Jail","Ferry Bookings Help"],"highlights":"Well-located hotel in Port Blair city centre near Cellular Jail and the ferry terminal for island hops."},
    {"id":"h-andaman-standard","destination":"andaman","dest_label":"Andaman, India","category":"domestic","name":"Barefoot at Havelock","stars":4,"location":"Havelock Island, Andaman","price_per_night":9800,"price_display":"₹9,800/night","image":"andaman.jpg","amenities":["Breakfast Included","Beach Access","Scuba Diving Packages","Eco Cottages","Snorkelling","Airport Boat Transfer"],"highlights":"Eco-luxury resort on Havelock Island adjacent to Radhanagar Beach (Asia's best beach). Award-winning sustainable design."},
    {"id":"h-andaman-luxury","destination":"andaman","dest_label":"Andaman, India","category":"domestic","name":"Taj Exotica Resort & Spa Andaman","stars":5,"location":"Havelock Island, Andaman","price_per_night":28000,"price_display":"₹28,000/night","image":"andaman.jpg","amenities":["All Meals","Private Beach","Overwater Villas","Diving Centre","Spa","Helicopter Transfer"],"highlights":"Andaman's most luxurious address. Overwater villas, coral-fringed private beach, and the Jiva Spa set among pristine tropical forest."},
]

# ── Flights Data ──────────────────────────────────────────────────────────────
FLIGHTS = [
    # =========== TO DUBAI ===========
    {"id":"f-del-dubai-eco","destination":"dubai","dest_label":"Dubai, UAE","category":"international","from_city":"Delhi (DEL)","to_city":"Dubai (DXB)","airline":"IndiGo","airline_code":"6E","duration":"3h 30m","departure":"06:15","arrival":"08:45","stops":"Non-Stop","class":"Economy","price_per_person":14500,"price_display":"₹14,500/person","features":["30kg Checked Baggage","Meal Included","Free Seat Selection"]},
    {"id":"f-del-dubai-biz","destination":"dubai","dest_label":"Dubai, UAE","category":"international","from_city":"Delhi (DEL)","to_city":"Dubai (DXB)","airline":"Emirates","airline_code":"EK","duration":"3h 20m","departure":"14:00","arrival":"17:20","stops":"Non-Stop","class":"Business","price_per_person":52000,"price_display":"₹52,000/person","features":["Lie-Flat Seat","Gourmet Dining","Chauffeur Drive","Priority Boarding","40kg Baggage"]},
    {"id":"f-mum-dubai-eco","destination":"dubai","dest_label":"Dubai, UAE","category":"international","from_city":"Mumbai (BOM)","to_city":"Dubai (DXB)","airline":"Air Arabia","airline_code":"G9","duration":"3h 05m","departure":"08:30","arrival":"10:35","stops":"Non-Stop","class":"Economy","price_per_person":11800,"price_display":"₹11,800/person","features":["25kg Checked Baggage","Snacks Included","Web Check-in"]},
    {"id":"f-mum-dubai-biz","destination":"dubai","dest_label":"Dubai, UAE","category":"international","from_city":"Mumbai (BOM)","to_city":"Dubai (DXB)","airline":"Emirates","airline_code":"EK","duration":"3h 00m","departure":"22:00","arrival":"01:00+1","stops":"Non-Stop","class":"Business","price_per_person":48000,"price_display":"₹48,000/person","features":["Lie-Flat Seat","Fine Dining","Lounge Access","Chauffeur Drive","40kg Baggage"]},
    {"id":"f-blr-dubai-eco","destination":"dubai","dest_label":"Dubai, UAE","category":"international","from_city":"Bengaluru (BLR)","to_city":"Dubai (DXB)","airline":"IndiGo","airline_code":"6E","duration":"4h 00m","departure":"10:45","arrival":"13:45","stops":"Non-Stop","class":"Economy","price_per_person":13200,"price_display":"₹13,200/person","features":["30kg Checked Baggage","Meal Included","Free Seat Selection"]},

    # =========== TO SINGAPORE ===========
    {"id":"f-del-sin-eco","destination":"singapore","dest_label":"Singapore","category":"international","from_city":"Delhi (DEL)","to_city":"Singapore (SIN)","airline":"Singapore Airlines","airline_code":"SQ","duration":"5h 45m","departure":"03:15","arrival":"12:00","stops":"Non-Stop","class":"Economy","price_per_person":18500,"price_display":"₹18,500/person","features":["30kg Baggage","World's Best Airline","In-flight Entertainment","Meal Included"]},
    {"id":"f-del-sin-biz","destination":"singapore","dest_label":"Singapore","category":"international","from_city":"Delhi (DEL)","to_city":"Singapore (SIN)","airline":"Singapore Airlines","airline_code":"SQ","duration":"5h 45m","departure":"03:15","arrival":"12:00","stops":"Non-Stop","class":"Business","price_per_person":72000,"price_display":"₹72,000/person","features":["Lie-Flat Bed","KrisFlyer Lounge","Michelin-Star Dining","Priority Boarding","40kg Baggage"]},
    {"id":"f-mum-sin-eco","destination":"singapore","dest_label":"Singapore","category":"international","from_city":"Mumbai (BOM)","to_city":"Singapore (SIN)","airline":"IndiGo","airline_code":"6E","duration":"5h 20m","departure":"00:30","arrival":"09:50","stops":"Non-Stop","class":"Economy","price_per_person":16800,"price_display":"₹16,800/person","features":["30kg Baggage","Meal Included","Web Check-in"]},
    {"id":"f-blr-sin-eco","destination":"singapore","dest_label":"Singapore","category":"international","from_city":"Bengaluru (BLR)","to_city":"Singapore (SIN)","airline":"Scoot","airline_code":"TR","duration":"5h 15m","departure":"07:00","arrival":"14:15","stops":"Non-Stop","class":"Economy","price_per_person":12500,"price_display":"₹12,500/person","features":["20kg Baggage","Budget Carrier","Fast Boarding"]},

    # =========== TO BALI ===========
    {"id":"f-del-bali-eco","destination":"bali","dest_label":"Bali, Indonesia","category":"international","from_city":"Delhi (DEL)","to_city":"Bali (DPS)","airline":"Air Asia","airline_code":"AK","duration":"8h 30m","departure":"09:00","arrival":"17:30","stops":"1 Stop (KUL)","class":"Economy","price_per_person":19500,"price_display":"₹19,500/person","features":["20kg Baggage","Meal Available","1 Stop Kuala Lumpur"]},
    {"id":"f-mum-bali-eco","destination":"bali","dest_label":"Bali, Indonesia","category":"international","from_city":"Mumbai (BOM)","to_city":"Bali (DPS)","airline":"Garuda Indonesia","airline_code":"GA","duration":"7h 50m","departure":"00:35","arrival":"10:25","stops":"1 Stop (CGK)","class":"Economy","price_per_person":21000,"price_display":"₹21,000/person","features":["30kg Baggage","Meal Included","Flag Carrier Service"]},
    {"id":"f-blr-bali-eco","destination":"bali","dest_label":"Bali, Indonesia","category":"international","from_city":"Bengaluru (BLR)","to_city":"Bali (DPS)","airline":"IndiGo","airline_code":"6E","duration":"9h 15m","departure":"22:15","arrival":"09:30+1","stops":"1 Stop (SIN)","class":"Economy","price_per_person":18200,"price_display":"₹18,200/person","features":["25kg Baggage","Meal Included","1 Stop Singapore"]},

    # =========== TO MALAYSIA ===========
    {"id":"f-del-kul-eco","destination":"malaysia","dest_label":"Kuala Lumpur, Malaysia","category":"international","from_city":"Delhi (DEL)","to_city":"Kuala Lumpur (KUL)","airline":"Malaysia Airlines","airline_code":"MH","duration":"5h 50m","departure":"01:05","arrival":"10:55","stops":"Non-Stop","class":"Economy","price_per_person":16500,"price_display":"₹16,500/person","features":["30kg Baggage","Meal Included","In-flight Entertainment"]},
    {"id":"f-mum-kul-eco","destination":"malaysia","dest_label":"Kuala Lumpur, Malaysia","category":"international","from_city":"Mumbai (BOM)","to_city":"Kuala Lumpur (KUL)","airline":"Air Asia","airline_code":"AK","duration":"5h 30m","departure":"06:15","arrival":"14:45","stops":"Non-Stop","class":"Economy","price_per_person":12000,"price_display":"₹12,000/person","features":["20kg Baggage","Budget Carrier","Low Cost Fares"]},
    {"id":"f-blr-kul-eco","destination":"malaysia","dest_label":"Kuala Lumpur, Malaysia","category":"international","from_city":"Bengaluru (BLR)","to_city":"Kuala Lumpur (KUL)","airline":"Air Asia","airline_code":"AK","duration":"5h 10m","departure":"11:30","arrival":"19:40","stops":"Non-Stop","class":"Economy","price_per_person":11500,"price_display":"₹11,500/person","features":["20kg Baggage","Budget Carrier","Online Check-in"]},

    # =========== TO VIETNAM ===========
    {"id":"f-del-han-eco","destination":"vietnam","dest_label":"Vietnam","category":"international","from_city":"Delhi (DEL)","to_city":"Hanoi (HAN)","airline":"Vietnam Airlines","airline_code":"VN","duration":"6h 30m","departure":"11:20","arrival":"19:50","stops":"Non-Stop","class":"Economy","price_per_person":17800,"price_display":"₹17,800/person","features":["30kg Baggage","Meal Included","Flag Carrier Service"]},
    {"id":"f-mum-sgn-eco","destination":"vietnam","dest_label":"Vietnam","category":"international","from_city":"Mumbai (BOM)","to_city":"Ho Chi Minh City (SGN)","airline":"Air Asia","airline_code":"AK","duration":"7h 45m","departure":"23:30","arrival":"08:15+1","stops":"1 Stop (KUL)","class":"Economy","price_per_person":15200,"price_display":"₹15,200/person","features":["20kg Baggage","Budget Carrier","1 Stop Kuala Lumpur"]},
    {"id":"f-blr-han-eco","destination":"vietnam","dest_label":"Vietnam","category":"international","from_city":"Bengaluru (BLR)","to_city":"Hanoi (HAN)","airline":"IndiGo","airline_code":"6E","duration":"8h 20m","departure":"09:00","arrival":"19:20","stops":"1 Stop (SIN)","class":"Economy","price_per_person":16500,"price_display":"₹16,500/person","features":["25kg Baggage","Meal Included","1 Stop Singapore"]},

    # =========== DOMESTIC ===========
    # To Kerala (Kochi - COK)
    {"id":"f-del-cok-eco","destination":"kerala","dest_label":"Kerala, India","category":"domestic","from_city":"Delhi (DEL)","to_city":"Kochi (COK)","airline":"IndiGo","airline_code":"6E","duration":"3h 10m","departure":"06:00","arrival":"09:10","stops":"Non-Stop","class":"Economy","price_per_person":4800,"price_display":"₹4,800/person","features":["15kg Baggage","Meal Available","Web Check-in"]},
    {"id":"f-del-cok-biz","destination":"kerala","dest_label":"Kerala, India","category":"domestic","from_city":"Delhi (DEL)","to_city":"Kochi (COK)","airline":"Air India","airline_code":"AI","duration":"3h 15m","departure":"07:30","arrival":"10:45","stops":"Non-Stop","class":"Business","price_per_person":14500,"price_display":"₹14,500/person","features":["25kg Baggage","Priority Boarding","Meal Included","Lounge Access"]},
    {"id":"f-mum-cok-eco","destination":"kerala","dest_label":"Kerala, India","category":"domestic","from_city":"Mumbai (BOM)","to_city":"Kochi (COK)","airline":"SpiceJet","airline_code":"SG","duration":"2h 00m","departure":"08:15","arrival":"10:15","stops":"Non-Stop","class":"Economy","price_per_person":3500,"price_display":"₹3,500/person","features":["15kg Baggage","Snacks Included","Online Check-in"]},
    {"id":"f-blr-cok-eco","destination":"kerala","dest_label":"Kerala, India","category":"domestic","from_city":"Bengaluru (BLR)","to_city":"Kochi (COK)","airline":"IndiGo","airline_code":"6E","duration":"1h 10m","departure":"07:30","arrival":"08:40","stops":"Non-Stop","class":"Economy","price_per_person":2800,"price_display":"₹2,800/person","features":["15kg Baggage","Quick Hop","Web Check-in"]},

    # To Rajasthan (Jaipur - JAI)
    {"id":"f-mum-jai-eco","destination":"rajasthan","dest_label":"Rajasthan, India","category":"domestic","from_city":"Mumbai (BOM)","to_city":"Jaipur (JAI)","airline":"IndiGo","airline_code":"6E","duration":"1h 45m","departure":"07:00","arrival":"08:45","stops":"Non-Stop","class":"Economy","price_per_person":4200,"price_display":"₹4,200/person","features":["15kg Baggage","Snack Included","Online Check-in"]},
    {"id":"f-del-jai-eco","destination":"rajasthan","dest_label":"Rajasthan, India","category":"domestic","from_city":"Delhi (DEL)","to_city":"Jaipur (JAI)","airline":"SpiceJet","airline_code":"SG","duration":"0h 55m","departure":"06:30","arrival":"07:25","stops":"Non-Stop","class":"Economy","price_per_person":2200,"price_display":"₹2,200/person","features":["15kg Baggage","Budget Carrier","Fast Boarding"]},
    {"id":"f-blr-jai-eco","destination":"rajasthan","dest_label":"Rajasthan, India","category":"domestic","from_city":"Bengaluru (BLR)","to_city":"Jaipur (JAI)","airline":"Air India","airline_code":"AI","duration":"2h 20m","departure":"10:15","arrival":"12:35","stops":"Non-Stop","class":"Economy","price_per_person":5500,"price_display":"₹5,500/person","features":["15kg Baggage","Meal Included","Flag Carrier"]},

    # To Goa (GOI)
    {"id":"f-del-goi-eco","destination":"goa","dest_label":"Goa, India","category":"domestic","from_city":"Delhi (DEL)","to_city":"Goa (GOI)","airline":"IndiGo","airline_code":"6E","duration":"2h 15m","departure":"06:15","arrival":"08:30","stops":"Non-Stop","class":"Economy","price_per_person":4500,"price_display":"₹4,500/person","features":["15kg Baggage","Snack Included","Web Check-in"]},
    {"id":"f-mum-goi-eco","destination":"goa","dest_label":"Goa, India","category":"domestic","from_city":"Mumbai (BOM)","to_city":"Goa (GOI)","airline":"SpiceJet","airline_code":"SG","duration":"1h 05m","departure":"08:00","arrival":"09:05","stops":"Non-Stop","class":"Economy","price_per_person":2800,"price_display":"₹2,800/person","features":["15kg Baggage","Budget Carrier","Fast Boarding"]},
    {"id":"f-chn-goi-eco","destination":"goa","dest_label":"Goa, India","category":"domestic","from_city":"Chennai (MAA)","to_city":"Goa (GOI)","airline":"Air India","airline_code":"AI","duration":"1h 25m","departure":"12:00","arrival":"13:25","stops":"Non-Stop","class":"Economy","price_per_person":3800,"price_display":"₹3,800/person","features":["15kg Baggage","Meal Included","Web Check-in"]},

    # To Kashmir (Srinagar - SXR)
    {"id":"f-del-sxr-eco","destination":"kashmir","dest_label":"Kashmir, India","category":"domestic","from_city":"Delhi (DEL)","to_city":"Srinagar (SXR)","airline":"IndiGo","airline_code":"6E","duration":"1h 20m","departure":"06:00","arrival":"07:20","stops":"Non-Stop","class":"Economy","price_per_person":4800,"price_display":"₹4,800/person","features":["15kg Baggage","Snack Included","Web Check-in"]},
    {"id":"f-del-sxr-biz","destination":"kashmir","dest_label":"Kashmir, India","category":"domestic","from_city":"Delhi (DEL)","to_city":"Srinagar (SXR)","airline":"Air India","airline_code":"AI","duration":"1h 25m","departure":"07:45","arrival":"09:10","stops":"Non-Stop","class":"Business","price_per_person":12000,"price_display":"₹12,000/person","features":["25kg Baggage","Meal Included","Priority Boarding","Lounge Access"]},
    {"id":"f-mum-sxr-eco","destination":"kashmir","dest_label":"Kashmir, India","category":"domestic","from_city":"Mumbai (BOM)","to_city":"Srinagar (SXR)","airline":"SpiceJet","airline_code":"SG","duration":"2h 30m","departure":"05:30","arrival":"08:00","stops":"Non-Stop","class":"Economy","price_per_person":6500,"price_display":"₹6,500/person","features":["15kg Baggage","Budget Carrier","Online Check-in"]},

    # To Andaman (Port Blair - IXZ)
    {"id":"f-del-ixz-eco","destination":"andaman","dest_label":"Andaman, India","category":"domestic","from_city":"Delhi (DEL)","to_city":"Port Blair (IXZ)","airline":"IndiGo","airline_code":"6E","duration":"2h 55m","departure":"07:30","arrival":"10:25","stops":"Non-Stop","class":"Economy","price_per_person":7200,"price_display":"₹7,200/person","features":["15kg Baggage","Meal Included","Web Check-in"]},
    {"id":"f-mum-ixz-eco","destination":"andaman","dest_label":"Andaman, India","category":"domestic","from_city":"Mumbai (BOM)","to_city":"Port Blair (IXZ)","airline":"Air India","airline_code":"AI","duration":"2h 45m","departure":"08:00","arrival":"10:45","stops":"Non-Stop","class":"Economy","price_per_person":8500,"price_display":"₹8,500/person","features":["20kg Baggage","Meal Included","Flag Carrier"]},
    {"id":"f-chn-ixz-eco","destination":"andaman","dest_label":"Andaman, India","category":"domestic","from_city":"Chennai (MAA)","to_city":"Port Blair (IXZ)","airline":"IndiGo","airline_code":"6E","duration":"2h 10m","departure":"06:00","arrival":"08:10","stops":"Non-Stop","class":"Economy","price_per_person":5500,"price_display":"₹5,500/person","features":["15kg Baggage","Snack Included","Web Check-in"]},
    {"id":"f-blr-ixz-eco","destination":"andaman","dest_label":"Andaman, India","category":"domestic","from_city":"Bengaluru (BLR)","to_city":"Port Blair (IXZ)","airline":"SpiceJet","airline_code":"SG","duration":"2h 25m","departure":"09:15","arrival":"11:40","stops":"Non-Stop","class":"Economy","price_per_person":6200,"price_display":"₹6,200/person","features":["15kg Baggage","Budget Carrier","Online Check-in"]},
]


@app.route("/hotels-flights")
@app.route("/hotels-flights/<destination>")
def hotels_flights(destination=None):
    all_destinations = [
        {"slug": "dubai", "label": "Dubai", "flag": "🇦🇪", "category": "international"},
        {"slug": "singapore", "label": "Singapore", "flag": "🇸🇬", "category": "international"},
        {"slug": "bali", "label": "Bali", "flag": "🇮🇩", "category": "international"},
        {"slug": "malaysia", "label": "Malaysia", "flag": "🇲🇾", "category": "international"},
        {"slug": "vietnam", "label": "Vietnam", "flag": "🇻🇳", "category": "international"},
        {"slug": "kerala", "label": "Kerala", "flag": "🇮🇳", "category": "domestic"},
        {"slug": "rajasthan", "label": "Rajasthan", "flag": "🇮🇳", "category": "domestic"},
        {"slug": "goa", "label": "Goa", "flag": "🇮🇳", "category": "domestic"},
        {"slug": "kashmir", "label": "Kashmir", "flag": "🇮🇳", "category": "domestic"},
        {"slug": "andaman", "label": "Andaman", "flag": "🇮🇳", "category": "domestic"},
    ]
    filtered_hotels = HOTELS if not destination else [h for h in HOTELS if h["destination"] == destination]
    filtered_flights = FLIGHTS if not destination else [f for f in FLIGHTS if f["destination"] == destination]
    filtered_packages = PACKAGES if not destination else [p for p in PACKAGES if p["destination"] == destination]
    return render_template(
        "hotels_flights.html",
        hotels=filtered_hotels,
        flights=filtered_flights,
        packages=filtered_packages,
        destinations=all_destinations,
        active_destination=destination,
        brand=BRAND,
    )


# ── Packages Data ────────────────────────────────────────────────────────────
PACKAGES = [
    # =================== INTERNATIONAL ===================
    # Dubai
    {"id":"dubai-3n4d-budget","destination":"dubai","category":"international","country":"United Arab Emirates","flag":"UAE","name":"Dubai Budget Getaway","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.42,000","price_numeric":42000,"hotel_category":"3 Star","theme":["city"],"badge":"Budget Pick","badge_color":"#2e7d32","image":"dubai.jpg","top_highlights":["Burj Khalifa At-The-Top","Dubai Mall & Fountain Show","Old Dubai Souk Walk"],"inclusions":["3-Star Hotel (3N)","Daily Breakfast","Airport Transfers","City Tour","Travel Insurance"]},
    {"id":"dubai-4n5d-standard","destination":"dubai","category":"international","country":"United Arab Emirates","flag":"UAE","name":"Dubai Classic Explorer","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.52,000","price_numeric":52000,"hotel_category":"4 Star","theme":["city","adventure"],"badge":"Best Seller","badge_color":"#e94560","image":"dubai.jpg","top_highlights":["Burj Khalifa At-The-Top","Desert Safari with BBQ Dinner","Dhow Cruise Marina","Palm Jumeirah"],"inclusions":["4-Star Hotel (4N)","Daily Breakfast","Airport Transfers","Desert Safari","City Tour","Travel Insurance"]},
    {"id":"dubai-5n6d-deluxe","destination":"dubai","category":"international","country":"United Arab Emirates","flag":"UAE","name":"Dubai Deluxe Experience","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.68,000","price_numeric":68000,"hotel_category":"5 Star","theme":["city","luxury"],"badge":"Top Rated","badge_color":"#f57c00","image":"dubai.jpg","top_highlights":["5-Star Luxury Stay","Desert Safari & Camel Ride","Atlantis Aquaventure Waterpark","Burj Al Arab View Tour"],"inclusions":["5-Star Hotel (5N)","Breakfast & Dinner","Private Transfers","Desert Safari","Aquaventure Entry","Travel Insurance"]},
    {"id":"dubai-6n7d-luxury","destination":"dubai","category":"international","country":"United Arab Emirates","flag":"UAE","name":"Dubai Royal Luxury Escape","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.95,000","price_numeric":95000,"hotel_category":"5 Star Deluxe","theme":["city","luxury","honeymoon"],"badge":"Honeymoon Pick","badge_color":"#7b1fa2","image":"dubai.jpg","top_highlights":["Luxury 5-Star Deluxe Hotel","Private Desert Safari","Helicopter City Tour","Burj Khalifa Premium Level","Yacht Cruise"],"inclusions":["5-Star Deluxe Hotel (6N)","All Meals","Private Transfers","Helicopter Tour","Yacht Cruise","Travel Insurance"]},
    # Singapore
    {"id":"singapore-3n4d-budget","destination":"singapore","category":"international","country":"Singapore","flag":"SG","name":"Singapore Quick Break","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.48,000","price_numeric":48000,"hotel_category":"3 Star","theme":["city"],"badge":None,"badge_color":None,"image":"singapore.jpg","top_highlights":["Gardens by the Bay","Merlion Park & Marina Bay","Sentosa Island"],"inclusions":["3-Star Hotel (3N)","Daily Breakfast","Airport Transfers","City Tour","Travel Insurance"]},
    {"id":"singapore-4n5d-standard","destination":"singapore","category":"international","country":"Singapore","flag":"SG","name":"Singapore Explorer","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.62,000","price_numeric":62000,"hotel_category":"4 Star","theme":["city","family"],"badge":"Best Seller","badge_color":"#e94560","image":"singapore.jpg","top_highlights":["Universal Studios Singapore","Gardens by the Bay Light Show","Singapore Zoo","Marina Bay Sands Skypark"],"inclusions":["4-Star Hotel (4N)","Daily Breakfast","Airport Transfers","Universal Studios Tickets","City Tour","Travel Insurance"]},
    {"id":"singapore-5n6d-family","destination":"singapore","category":"international","country":"Singapore","flag":"SG","name":"Singapore Family Fiesta","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.72,000","price_numeric":72000,"hotel_category":"4 Star","theme":["city","family"],"badge":"Family Favourite","badge_color":"#1565c0","image":"singapore.jpg","top_highlights":["Universal Studios","Singapore Zoo & Night Safari","S.E.A. Aquarium","Sentosa Beach","Jurong Bird Park"],"inclusions":["4-Star Hotel (5N)","Daily Breakfast","Airport Transfers","4 Attraction Tickets","City Tour","Travel Insurance"]},
    # Bali
    {"id":"bali-4n5d-honeymoon","destination":"bali","category":"international","country":"Indonesia","flag":"ID","name":"Bali Honeymoon Bliss","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.38,000","price_numeric":38000,"hotel_category":"4 Star Villa","theme":["beach","honeymoon"],"badge":"Honeymoon Pick","badge_color":"#7b1fa2","image":"bali.jpg","top_highlights":["Romantic Villa with Pool","Tegallalang Rice Terrace Sunrise","Uluwatu Sunset Temple & Kecak Dance","Seminyak Beach Dinner"],"inclusions":["4-Star Pool Villa (4N)","Daily Breakfast","Airport Transfers","Sunset Dinner","Couple Spa Session","Travel Insurance"]},
    {"id":"bali-5n6d-standard","destination":"bali","category":"international","country":"Indonesia","flag":"ID","name":"Bali Classic Adventure","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.45,000","price_numeric":45000,"hotel_category":"4 Star","theme":["beach","adventure","culture"],"badge":"Best Seller","badge_color":"#e94560","image":"bali.jpg","top_highlights":["Tegallalang Rice Terrace","Ubud Monkey Forest & Art Market","White Water Rafting","Tanah Lot Sunset Temple"],"inclusions":["4-Star Hotel (5N)","Daily Breakfast","Airport Transfers","Rafting","Full Day Ubud Tour","Travel Insurance"]},
    {"id":"bali-6n7d-luxury","destination":"bali","category":"international","country":"Indonesia","flag":"ID","name":"Bali Luxury Escape","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.65,000","price_numeric":65000,"hotel_category":"5 Star Villa","theme":["beach","honeymoon","luxury"],"badge":"Top Rated","badge_color":"#f57c00","image":"bali.jpg","top_highlights":["5-Star Infinity Pool Villa","Private Cooking Class","Mount Batur Sunrise Trek","Nusa Penida Island Hopping","Romantic Candle Dinner"],"inclusions":["5-Star Pool Villa (6N)","All Meals","Private Transfers","Nusa Penida Trip","Sunrise Trek","Couple Spa","Travel Insurance"]},
    # Malaysia
    {"id":"malaysia-3n4d-budget","destination":"malaysia","category":"international","country":"Malaysia","flag":"MY","name":"Malaysia Express Escape","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.32,000","price_numeric":32000,"hotel_category":"3 Star","theme":["city"],"badge":"Budget Pick","badge_color":"#2e7d32","image":"malaysia.jpg","top_highlights":["Petronas Twin Towers","Batu Caves","KL City Tour"],"inclusions":["3-Star Hotel (3N)","Daily Breakfast","Airport Transfers","City Tour","Travel Insurance"]},
    {"id":"malaysia-4n5d-standard","destination":"malaysia","category":"international","country":"Malaysia","flag":"MY","name":"Malaysia & Genting Combo","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.42,000","price_numeric":42000,"hotel_category":"4 Star","theme":["city","adventure","family"],"badge":"Best Seller","badge_color":"#e94560","image":"malaysia.jpg","top_highlights":["Petronas Towers Observation Deck","Genting Highlands Cable Car","Batu Caves","Sunway Lagoon Water Park"],"inclusions":["4-Star Hotel (4N)","Daily Breakfast","Airport Transfers","Genting Day Trip","City Tour","Travel Insurance"]},
    {"id":"malaysia-5n6d-deluxe","destination":"malaysia","category":"international","country":"Malaysia","flag":"MY","name":"Malaysia Penang & KL Delight","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.55,000","price_numeric":55000,"hotel_category":"4 Star","theme":["city","culture","beach"],"badge":None,"badge_color":None,"image":"malaysia.jpg","top_highlights":["Penang Street Art & Heritage Town","Petronas Towers Night View","Langkawi Cable Car","Genting Highlands"],"inclusions":["4-Star Hotels (5N)","Daily Breakfast","Airport Transfers","Penang Tour","Langkawi Day Trip","Travel Insurance"]},
    # Vietnam
    {"id":"vietnam-5n6d-standard","destination":"vietnam","category":"international","country":"Vietnam","flag":"VN","name":"Vietnam Classic Discovery","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.38,000","price_numeric":38000,"hotel_category":"3 Star","theme":["culture","adventure"],"badge":None,"badge_color":None,"image":"vietnam.jpg","top_highlights":["Ha Long Bay Cruise","Hoi An Ancient Town","Ho Chi Minh City Tour"],"inclusions":["3-Star Hotels (5N)","Daily Breakfast","Airport Transfers","Ha Long Bay Cruise","City Tours","Travel Insurance"]},
    {"id":"vietnam-6n7d-adventure","destination":"vietnam","category":"international","country":"Vietnam","flag":"VN","name":"Vietnam Adventure Trail","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.48,000","price_numeric":48000,"hotel_category":"4 Star","theme":["adventure","culture"],"badge":"Best Seller","badge_color":"#e94560","image":"vietnam.jpg","top_highlights":["Ha Long Bay 2-Day Cruise","Phong Nha Cave Trekking","Hoi An Cooking Class","Sapa Rice Terrace Hike"],"inclusions":["4-Star Hotels (6N)","Daily Breakfast","Airport Transfers","Ha Long 2D Cruise","Sapa Hike","Travel Insurance"]},
    {"id":"vietnam-7n8d-deluxe","destination":"vietnam","category":"international","country":"Vietnam","flag":"VN","name":"Vietnam Grand Tour","duration_nights":7,"duration_label":"7 Nights / 8 Days","price_per_person":"Rs.62,000","price_numeric":62000,"hotel_category":"4 Star","theme":["culture","adventure","luxury"],"badge":"Top Rated","badge_color":"#f57c00","image":"vietnam.jpg","top_highlights":["Ha Long Bay Overnight Junk Cruise","Hoi An Ancient Town Night Market","Hue Imperial Citadel","Mekong Delta Boat Tour","Ninh Binh Cycling Tour"],"inclusions":["4-Star Hotels (7N)","Breakfast & Select Dinners","All Internal Transfers","Ha Long Cruise","All City Tours","Travel Insurance"]},
    # =================== DOMESTIC ===================
    # Kerala
    {"id":"kerala-3n4d-houseboat","destination":"kerala","category":"domestic","country":"Kerala, India","flag":"IN","name":"Kerala Houseboat Retreat","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.18,000","price_numeric":18000,"hotel_category":"3 Star + Houseboat","theme":["beach","nature","honeymoon"],"badge":"Honeymoon Pick","badge_color":"#7b1fa2","image":"kerala.jpg","top_highlights":["Alleppey Houseboat (1 Night)","Kumarakom Backwaters","Vembanad Lake Sunset"],"inclusions":["Hotel (2N) + Houseboat (1N)","All Meals on Houseboat","Airport Transfers","Backwater Tour","Travel Insurance"]},
    {"id":"kerala-4n5d-standard","destination":"kerala","category":"domestic","country":"Kerala, India","flag":"IN","name":"Kerala Classic Holiday","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.22,000","price_numeric":22000,"hotel_category":"3 Star","theme":["nature","culture"],"badge":"Best Seller","badge_color":"#e94560","image":"kerala.jpg","top_highlights":["Alleppey Houseboat","Munnar Tea Plantations","Periyar Wildlife Sanctuary","Kovalam Beach"],"inclusions":["3-Star Hotels (4N)","Daily Breakfast","Airport Transfers","Houseboat (1N)","Jeep Safari","Travel Insurance"]},
    {"id":"kerala-5n6d-deluxe","destination":"kerala","category":"domestic","country":"Kerala, India","flag":"IN","name":"Kerala Grand Expedition","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.30,000","price_numeric":30000,"hotel_category":"4 Star","theme":["nature","adventure","culture"],"badge":"Top Rated","badge_color":"#f57c00","image":"kerala.jpg","top_highlights":["Munnar Top Station Trek","Wayanad Bamboo Rafting","Alleppey Houseboat (2N)","Thekkady Spice Garden","Thrissur Cultural Evening"],"inclusions":["4-Star Hotels (3N) + Houseboat (2N)","Daily Breakfast","Airport Transfers","Bamboo Rafting","All Tours","Travel Insurance"]},
    {"id":"kerala-6n7d-luxury","destination":"kerala","category":"domestic","country":"Kerala, India","flag":"IN","name":"Kerala Luxury Retreat","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.45,000","price_numeric":45000,"hotel_category":"5 Star","theme":["luxury","nature","honeymoon"],"badge":None,"badge_color":None,"image":"kerala.jpg","top_highlights":["5-Star Treehouse Stay in Munnar","Luxury Houseboat (2N)","Ayurvedic Spa & Wellness","Private Beach at Kovalam","Kathakali Cultural Night"],"inclusions":["5-Star Resort (4N) + Luxury Houseboat (2N)","All Meals","Private Transfers","Spa Session","All Tours","Travel Insurance"]},
    # Rajasthan
    {"id":"rajasthan-4n5d-heritage","destination":"rajasthan","category":"domestic","country":"Rajasthan, India","flag":"IN","name":"Rajasthan Heritage Circuit","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.20,000","price_numeric":20000,"hotel_category":"Heritage Hotel","theme":["heritage","culture"],"badge":"Budget Pick","badge_color":"#2e7d32","image":"rajasthan.jpg","top_highlights":["Jaipur City Palace & Amber Fort","Pushkar Holy Lake","Jodhpur Blue City Walk"],"inclusions":["Heritage Hotels (4N)","Daily Breakfast","Airport Transfers","City Tours","Travel Insurance"]},
    {"id":"rajasthan-5n6d-standard","destination":"rajasthan","category":"domestic","country":"Rajasthan, India","flag":"IN","name":"Rajasthan Royal Explorer","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.27,000","price_numeric":27000,"hotel_category":"4 Star Heritage","theme":["heritage","culture","adventure"],"badge":"Best Seller","badge_color":"#e94560","image":"rajasthan.jpg","top_highlights":["Jaisalmer Desert Camp (1N)","Camel Safari on Sand Dunes","Amber Fort Jaipur","Udaipur Lake Pichola Boat Ride","Mehrangarh Fort Jodhpur"],"inclusions":["4-Star Hotels (4N) + Desert Camp (1N)","Daily Breakfast","Airport Transfers","Camel Safari","City Tours","Travel Insurance"]},
    {"id":"rajasthan-7n8d-grand","destination":"rajasthan","category":"domestic","country":"Rajasthan, India","flag":"IN","name":"Rajasthan Grand Royal Tour","duration_nights":7,"duration_label":"7 Nights / 8 Days","price_per_person":"Rs.40,000","price_numeric":40000,"hotel_category":"5 Star Palace","theme":["heritage","luxury","culture"],"badge":"Top Rated","badge_color":"#f57c00","image":"rajasthan.jpg","top_highlights":["Stay in Maharaja Palace Hotel","Ranthambore Tiger Safari","Jaipur-Jodhpur-Jaisalmer-Udaipur Circuit","Desert Stargazing Camp","Folk Dance Evening"],"inclusions":["5-Star Palace Hotels (6N) + Desert Camp (1N)","Breakfast & Dinner","All Transfers","Tiger Safari","All City Tours","Travel Insurance"]},
    # Goa
    {"id":"goa-3n4d-budget","destination":"goa","category":"domestic","country":"Goa, India","flag":"IN","name":"Goa Weekend Escape","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.14,000","price_numeric":14000,"hotel_category":"3 Star","theme":["beach"],"badge":"Budget Pick","badge_color":"#2e7d32","image":"goa.jpg","top_highlights":["Baga & Calangute Beaches","Old Goa Church Walk","Dudhsagar Waterfall Day Trip"],"inclusions":["3-Star Hotel (3N)","Daily Breakfast","Airport Transfers","Waterfall Tour","Travel Insurance"]},
    {"id":"goa-4n5d-standard","destination":"goa","category":"domestic","country":"Goa, India","flag":"IN","name":"Goa Beach & Party Getaway","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.18,000","price_numeric":18000,"hotel_category":"4 Star","theme":["beach","adventure"],"badge":"Best Seller","badge_color":"#e94560","image":"goa.jpg","top_highlights":["North & South Goa Beaches","Water Sports Package","Cruise on Mandovi River","Old Goa Heritage Walk","Spice Plantation Tour"],"inclusions":["4-Star Beach Resort (4N)","Daily Breakfast","Airport Transfers","Water Sports","River Cruise","Travel Insurance"]},
    {"id":"goa-5n6d-premium","destination":"goa","category":"domestic","country":"Goa, India","flag":"IN","name":"Goa Premium Beach Retreat","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.28,000","price_numeric":28000,"hotel_category":"5 Star","theme":["beach","luxury","honeymoon"],"badge":"Honeymoon Pick","badge_color":"#7b1fa2","image":"goa.jpg","top_highlights":["5-Star Beach Resort with Private Pool","Sunset Dinner Cruise on Arabian Sea","Scuba Diving at Grand Island","Palolem Beach Kayaking"],"inclusions":["5-Star Beach Resort (5N)","Breakfast & Dinner","Airport Transfers","Scuba Diving","Dinner Cruise","Travel Insurance"]},
    # Kashmir
    {"id":"kashmir-4n5d-standard","destination":"kashmir","category":"domestic","country":"Kashmir, India","flag":"IN","name":"Kashmir Valley Delight","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.24,000","price_numeric":24000,"hotel_category":"Houseboat + Hotel","theme":["nature","honeymoon"],"badge":"Best Seller","badge_color":"#e94560","image":"kashmir.jpg","top_highlights":["Dal Lake Shikara Ride","Houseboat Stay (1N)","Gulmarg Gondola Cable Car","Pahalgam River Walk"],"inclusions":["Houseboat (1N) + Hotel (3N)","Daily Breakfast","Airport Transfers","Shikara Ride","Gondola Tickets","Travel Insurance"]},
    {"id":"kashmir-6n7d-deluxe","destination":"kashmir","category":"domestic","country":"Kashmir, India","flag":"IN","name":"Kashmir Grand Splendour","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.34,000","price_numeric":34000,"hotel_category":"4 Star","theme":["nature","adventure","honeymoon"],"badge":"Top Rated","badge_color":"#f57c00","image":"kashmir.jpg","top_highlights":["Luxury Dal Lake Houseboat (2N)","Gulmarg Ski / Snow Activities","Sonamarg Glacier Trek","Pahalgam Betaab Valley","Mughal Gardens Tour"],"inclusions":["4-Star Hotels (4N) + Luxury Houseboat (2N)","Daily Breakfast","Airport Transfers","Snow Activities","All Tours","Travel Insurance"]},
    {"id":"kashmir-7n8d-family","destination":"kashmir","category":"domestic","country":"Kashmir, India","flag":"IN","name":"Kashmir Family Adventure","duration_nights":7,"duration_label":"7 Nights / 8 Days","price_per_person":"Rs.42,000","price_numeric":42000,"hotel_category":"4 Star","theme":["family","adventure","nature"],"badge":"Family Favourite","badge_color":"#1565c0","image":"kashmir.jpg","top_highlights":["Houseboat (2N) on Dal Lake","Gulmarg Gondola Phase II","Sonamarg Glacier Day Trip","Doodhpathri Valley","White Water Rafting Lidder River"],"inclusions":["4-Star Hotels (5N) + Houseboat (2N)","Daily Breakfast","Airport Transfers","All Activities","All Tours","Travel Insurance"]},
    # Andaman
    {"id":"andaman-4n5d-standard","destination":"andaman","category":"domestic","country":"Andaman & Nicobar, India","flag":"IN","name":"Andaman Island Escape","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.26,000","price_numeric":26000,"hotel_category":"3 Star","theme":["beach","nature"],"badge":None,"badge_color":None,"image":"andaman.jpg","top_highlights":["Radhanagar Beach (Asia Best Beach)","Cellular Jail Light & Sound Show","Havelock Island Day Trip","Scuba Diving"],"inclusions":["3-Star Hotel (4N)","Daily Breakfast","Airport Transfers","Ferry Tickets","Scuba Intro Dive","Travel Insurance"]},
    {"id":"andaman-5n6d-deluxe","destination":"andaman","category":"domestic","country":"Andaman & Nicobar, India","flag":"IN","name":"Andaman Coral Paradise","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.34,000","price_numeric":34000,"hotel_category":"4 Star","theme":["beach","adventure","honeymoon"],"badge":"Best Seller","badge_color":"#e94560","image":"andaman.jpg","top_highlights":["Havelock Island (2N)","Scuba Diving & Snorkelling at Elephant Beach","Neil Island Day Trip","Glass Bottom Boat Ride","Radhanagar Beach Sunset"],"inclusions":["4-Star Hotels (5N)","Daily Breakfast","Airport Transfers","Ferry Tickets","Scuba Diving","Glass Boat Ride","Travel Insurance"]},
    {"id":"andaman-6n7d-adventure","destination":"andaman","category":"domestic","country":"Andaman & Nicobar, India","flag":"IN","name":"Andaman Deep Sea Adventure","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.46,000","price_numeric":46000,"hotel_category":"4 Star","theme":["beach","adventure"],"badge":"Top Rated","badge_color":"#f57c00","image":"andaman.jpg","top_highlights":["Havelock (3N) + Neil Island (1N)","PADI Open Water Scuba Certification","Sea Walk Underwater","Deep Sea Fishing","Jolly Buoy Snorkelling"],"inclusions":["4-Star Resorts (6N)","Daily Breakfast","All Ferry Tickets","PADI Dive Course","Sea Walk","All Tours","Travel Insurance"]},
    # Maharashtra
    {"id":"maharashtra-3n4d-mumbai","destination":"maharashtra","category":"domestic","country":"Maharashtra, India","flag":"IN","name":"Mumbai & Lonavala Getaway","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.15,500","price_numeric":15500,"hotel_category":"4 Star","theme":["city","nature"],"badge":"Best Seller","badge_color":"#e94560","image":"hero_bg.jpg","top_highlights":["Gateway of India & Marine Drive","Elephanta Caves Ferry Tour","Lonavala & Khandala Hills","Pune Heritage Walk"],"inclusions":["4-Star Hotel (3N)","Daily Breakfast","Airport Transfers","Sightseeing Cab","Travel Insurance"]},
    {"id":"maharashtra-4n5d-hill","destination":"maharashtra","category":"domestic","country":"Maharashtra, India","flag":"IN","name":"Mahabaleshwar & Shirdi Explorer","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.19,000","price_numeric":19000,"hotel_category":"4 Star","theme":["nature","culture"],"badge":"Family Favourite","badge_color":"#1565c0","image":"about_bg.jpg","top_highlights":["Mahabaleshwar Strawberry Farms","Venna Lake Boating","Shirdi Sai Baba Darshan","Ajanta & Ellora Caves Option"],"inclusions":["4-Star Resorts (4N)","Daily Breakfast","Private AC Cab","All Sightseeing","Travel Insurance"]},
    # Delhi & Golden Triangle
    {"id":"delhi-3n4d-triangle","destination":"delhi","category":"domestic","country":"Delhi & Agra, India","flag":"IN","name":"Delhi Agra Golden Triangle","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.16,000","price_numeric":16000,"hotel_category":"4 Star","theme":["heritage","culture"],"badge":"Best Seller","badge_color":"#e94560","image":"rajasthan.jpg","top_highlights":["Taj Mahal Sunrise Tour","Red Fort & Qutub Minar","India Gate & Humayun Tomb","Agra Fort Visit"],"inclusions":["4-Star Hotels (3N)","Daily Breakfast","Airport Transfers","Private AC Car","Monument Guide","Travel Insurance"]},
    # Himachal Pradesh
    {"id":"himachal-5n6d-manali","destination":"himachal","category":"domestic","country":"Himachal Pradesh, India","flag":"IN","name":"Shimla & Manali Himalayan Escape","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.21,000","price_numeric":21000,"hotel_category":"4 Star","theme":["nature","adventure","honeymoon"],"badge":"Best Seller","badge_color":"#e94560","image":"kashmir.jpg","top_highlights":["Solang Valley Snow Activities","Atal Tunnel & Rohtang Pass","Shimla Mall Road & Kufri","Hadimba Devi Temple"],"inclusions":["4-Star Hotels (5N)","Breakfast & Dinner","Volvo / Private Cab Transfers","Local Sightseeing","Travel Insurance"]},
    # Uttarakhand
    {"id":"uttarakhand-4n5d-hills","destination":"uttarakhand","category":"domestic","country":"Uttarakhand, India","flag":"IN","name":"Rishikesh, Mussoorie & Nainital Tour","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.18,500","price_numeric":18500,"hotel_category":"4 Star","theme":["nature","adventure"],"badge":"Top Rated","badge_color":"#f57c00","image":"kashmir.jpg","top_highlights":["Ganga Aarti at Rishikesh","Kempty Falls Mussoorie","Naini Lake Boating","River Rafting & Adventure"],"inclusions":["4-Star Hotels (4N)","Daily Breakfast","Airport Transfers (Dehradun)","All Hill Transfers","Travel Insurance"]},
    # Ladakh
    {"id":"ladakh-5n6d-pangong","destination":"ladakh","category":"domestic","country":"Ladakh, India","flag":"IN","name":"Leh Ladakh & Pangong Expedition","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.29,500","price_numeric":29500,"hotel_category":"4 Star + Camp","theme":["adventure","nature"],"badge":"Adventure Pick","badge_color":"#e94560","image":"kashmir.jpg","top_highlights":["Pangong Tso Lake Overnight Camp","Nubra Valley Camel Safari","Khardung La Pass Drive","Shanti Stupa & Magnetic Hill"],"inclusions":["Hotels (4N) + Lake Camp (1N)","Breakfast & Dinner","Airport Transfers","Inner Line Permits","Oxygen Cylinder Backup"]},
    # Karnataka
    {"id":"karnataka-4n5d-coorg","destination":"karnataka","category":"domestic","country":"Karnataka, India","flag":"IN","name":"Bengaluru, Mysuru & Coorg Retreat","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.19,500","price_numeric":19500,"hotel_category":"4 Star","theme":["nature","culture"],"badge":"Nature Pick","badge_color":"#2e7d32","image":"kerala.jpg","top_highlights":["Mysore Palace Illumination","Coorg Coffee Estate Stay","Abbey Falls & Raja Seat","Bengaluru Botanical Gardens"],"inclusions":["4-Star Hotels & Estate Stay (4N)","Daily Breakfast","Airport Transfers","Private Cab","Travel Insurance"]},
    # Tamil Nadu
    {"id":"tamilnadu-4n5d-ooty","destination":"tamilnadu","category":"domestic","country":"Tamil Nadu, India","flag":"IN","name":"Chennai, Pondicherry & Ooty Tour","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.18,000","price_numeric":18000,"hotel_category":"4 Star","theme":["culture","nature"],"badge":None,"badge_color":None,"image":"kerala.jpg","top_highlights":["Ooty Nilgiri Mountain Railway","Pondicherry French Quarter","Mahabalipuram Shore Temple","Botanical Gardens"],"inclusions":["4-Star Hotels (4N)","Daily Breakfast","Airport Transfers","Sightseeing Cab","Travel Insurance"]},
    # West Bengal & Sikkim
    {"id":"westbengal-5n6d-darjeeling","destination":"westbengal","category":"domestic","country":"West Bengal & Sikkim, India","flag":"IN","name":"Darjeeling & Gangtok Himalayan Tour","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.24,500","price_numeric":24500,"hotel_category":"4 Star","theme":["nature","culture"],"badge":"Best Seller","badge_color":"#e94560","image":"kashmir.jpg","top_highlights":["Tiger Hill Kanchenjunga Sunrise","Tsomgo Lake & Baba Mandir","Darjeeling Toy Train Ride","Tea Garden Visit"],"inclusions":["4-Star Hotels (5N)","Daily Breakfast","Bagdogra Airport Transfers","All Permits & Tours","Travel Insurance"]},
    # Uttar Pradesh
    {"id":"up-3n4d-spiritual","destination":"uttarpradesh","category":"domestic","country":"Uttar Pradesh, India","flag":"IN","name":"Varanasi & Ayodhya Spiritual Circuit","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.16,500","price_numeric":16500,"hotel_category":"4 Star","theme":["culture","heritage"],"badge":"Popular","badge_color":"#f57c00","image":"rajasthan.jpg","top_highlights":["Kashi Vishwanath & Ganga Aarti","Morning Boat Ride on Ganga","Ayodhya Ram Mandir Darshan","Sarnath Buddhist Stupa"],"inclusions":["4-Star Hotels (3N)","Daily Breakfast","Airport Transfers","Private AC Cab","Boat Ride","Travel Insurance"]},
    # Telangana
    {"id":"telangana-3n4d-hyd","destination":"telangana","category":"domestic","country":"Telangana, India","flag":"IN","name":"Hyderabad Royal & Ramoji Tour","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.14,500","price_numeric":14500,"hotel_category":"4 Star","theme":["city","heritage"],"badge":"Budget Pick","badge_color":"#2e7d32","image":"rajasthan.jpg","top_highlights":["Ramoji Film City Full Day","Charminar & Golconda Fort","Hussain Sagar Lake Cruise","Authentic Hyderabadi Cuisine"],"inclusions":["4-Star Hotel (3N)","Daily Breakfast","Airport Transfers","Ramoji Entry Tickets","Travel Insurance"]},
    # Gujarat
    {"id":"gujarat-4n5d-gir","destination":"gujarat","category":"domestic","country":"Gujarat, India","flag":"IN","name":"Gujarat Gir, Somnath & Dwarka Tour","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.21,500","price_numeric":21500,"hotel_category":"4 Star","theme":["culture","nature"],"badge":"Family Favourite","badge_color":"#1565c0","image":"rajasthan.jpg","top_highlights":["Gir National Park Lion Safari","Somnath Temple Sunset Aarti","Dwarkadhish Temple","Sabarmati Riverfront Ahmedabad"],"inclusions":["4-Star Hotels (4N)","Daily Breakfast","Airport Transfers","Gir Safari Permit","Travel Insurance"]},
    # Northeast / Assam & Meghalaya
    {"id":"assam-5n6d-meghalaya","destination":"assam","category":"domestic","country":"Assam & Meghalaya, India","flag":"IN","name":"Guwahati, Shillong & Cherrapunji","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.26,500","price_numeric":26500,"hotel_category":"4 Star","theme":["nature","adventure"],"badge":"Top Rated","badge_color":"#f57c00","image":"kerala.jpg","top_highlights":["Living Root Bridges Cherrapunji","Dawki Crystal Clear River Boating","Kaziranga Rhino Safari","Umiam Lake Shillong"],"inclusions":["4-Star Hotels (5N)","Daily Breakfast","Guwahati Airport Transfers","Jeep Safari","Travel Insurance"]},
    # =================== MORE INTERNATIONAL ===================
    # Thailand
    {"id":"thailand-4n5d-bangkok","destination":"thailand","category":"international","country":"Thailand","flag":"TH","name":"Bangkok & Pattaya Coral Island","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.34,000","price_numeric":34000,"hotel_category":"4 Star","theme":["beach","city"],"badge":"Best Seller","badge_color":"#e94560","image":"bali.jpg","top_highlights":["Coral Island Speedboat & Lunch","Alcazar Cabaret Show","Bangkok Temple & City Tour","Chao Phraya Dinner Cruise"],"inclusions":["4-Star Hotels (4N)","Daily Breakfast","Airport Transfers","Island Tour","Travel Insurance"]},
    {"id":"thailand-5n6d-phuket","destination":"thailand","category":"international","country":"Thailand","flag":"TH","name":"Phuket & Krabi Phi Phi Island","duration_nights":5,"duration_label":"5 Nights / 6 Days","price_per_person":"Rs.46,000","price_numeric":46000,"hotel_category":"4 Star","theme":["beach","honeymoon"],"badge":"Honeymoon Pick","badge_color":"#7b1fa2","image":"bali.jpg","top_highlights":["Phi Phi Island Speedboat Tour","James Bond Island Cruise","Krabi 4-Island Hopping","Patong Beach Sunset"],"inclusions":["4-Star Resorts (5N)","Daily Breakfast","Airport Transfers","Island Speedboat Tours","Travel Insurance"]},
    # Maldives
    {"id":"maldives-4n5d-villa","destination":"maldives","category":"international","country":"Maldives","flag":"MV","name":"Maldives Overwater Villa Escape","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.78,000","price_numeric":78000,"hotel_category":"5 Star Water Villa","theme":["beach","honeymoon","luxury"],"badge":"Honeymoon Pick","badge_color":"#7b1fa2","image":"andaman.jpg","top_highlights":["Overwater Villa with Lagoon Access","Speedboat Resort Transfers","Snorkelling & Dolphin Cruise","Candlelight Beach Dinner"],"inclusions":["5-Star Water Villa (4N)","All Meals Included","Speedboat Transfers","Water Sports","Travel Insurance"]},
    # Europe & UK
    {"id":"europe-6n7d-classic","destination":"europe","category":"international","country":"UK & Europe","flag":"EU","name":"London, Paris & Swiss Highlights","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.1,35,000","price_numeric":135000,"hotel_category":"4 Star","theme":["city","luxury","culture"],"badge":"Top Rated","badge_color":"#f57c00","image":"singapore.jpg","top_highlights":["London Eye & Thames Cruise","Eiffel Tower & Seine River Cruise","Mt. Titlis Swiss Alps Cable Car","Eurostar High-Speed Rail"],"inclusions":["4-Star Hotels (6N)","Daily Breakfast","Airport & Rail Transfers","Sightseeing Passes","Travel Insurance"]},
    # Japan
    {"id":"japan-6n7d-tokyo","destination":"japan","category":"international","country":"Japan","flag":"JP","name":"Tokyo, Mt. Fuji & Kyoto Discovery","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.1,42,000","price_numeric":142000,"hotel_category":"4 Star","theme":["city","culture"],"badge":"Trending","badge_color":"#1565c0","image":"vietnam.jpg","top_highlights":["Shinkansen Bullet Train Ride","Mt. Fuji 5th Station & Lake Ashi","Kyoto Fushimi Inari & Bamboo Grove","Tokyo Shibuya & Senso-ji"],"inclusions":["4-Star Hotels (6N)","Daily Breakfast","JR Rail Pass","Airport Transfers","Travel Insurance"]},
    # Sri Lanka
    {"id":"srilanka-4n5d-island","destination":"srilanka","category":"international","country":"Sri Lanka","flag":"LK","name":"Sri Lanka Cultural & Beach Trail","duration_nights":4,"duration_label":"4 Nights / 5 Days","price_per_person":"Rs.32,000","price_numeric":32000,"hotel_category":"4 Star","theme":["culture","beach"],"badge":"Budget Pick","badge_color":"#2e7d32","image":"kerala.jpg","top_highlights":["Kandy Temple of the Tooth","Nuwara Eliya Tea Plantations","Bentota Beach & Turtle Hatchery","Colombo City Tour"],"inclusions":["4-Star Hotels (4N)","Daily Breakfast","Airport Transfers","Private AC Vehicle","Travel Insurance"]},
    # Turkey
    {"id":"turkey-6n7d-istanbul","destination":"turkey","category":"international","country":"Turkey","flag":"TR","name":"Istanbul & Cappadocia Hot Air Balloon","duration_nights":6,"duration_label":"6 Nights / 7 Days","price_per_person":"Rs.88,000","price_numeric":88000,"hotel_category":"4 Star Cave Hotel","theme":["culture","adventure","honeymoon"],"badge":"Best Seller","badge_color":"#e94560","image":"dubai.jpg","top_highlights":["Cappadocia Hot Air Balloon Sunrise","Bosphorus Dinner Cruise Istanbul","Hagia Sophia & Grand Bazaar","Goreme Cave Hotel Stay"],"inclusions":["4-Star Hotels & Cave Stay (6N)","Daily Breakfast","Domestic Flight & Transfers","City Tours","Travel Insurance"]},
    # Qatar
    {"id":"qatar-3n4d-doha","destination":"qatar","category":"international","country":"Qatar","flag":"QA","name":"Doha Luxury Stopover & Desert","duration_nights":3,"duration_label":"3 Nights / 4 Days","price_per_person":"Rs.44,000","price_numeric":44000,"hotel_category":"5 Star","theme":["city","luxury"],"badge":"Stopover Pick","badge_color":"#7b1fa2","image":"dubai.jpg","top_highlights":["Souq Waqif & Museum of Islamic Art","Inland Sea Desert Safari","The Pearl-Qatar Marina","Katara Cultural Village"],"inclusions":["5-Star Hotel (3N)","Daily Breakfast","Airport Transfers","Desert Safari","Travel Insurance"]},
]


@app.route("/packages/international")
def packages_international():
    intl_pkgs = [p for p in PACKAGES if p["category"] == "international"]
    dest_slugs = sorted(set(p["destination"] for p in intl_pkgs))
    return render_template(
        "packages_listing.html",
        packages=intl_pkgs,
        category="international",
        page_title="International Tour Packages",
        page_subtitle="Explore 5 countries / 18 handcrafted packages / Complimentary Travel Insurance",
        dest_slugs=dest_slugs,
        DESTINATIONS=DESTINATIONS,
    )


@app.route("/packages/domestic")
def packages_domestic():
    dom_pkgs = [p for p in PACKAGES if p["category"] == "domestic"]
    dest_slugs = sorted(set(p["destination"] for p in dom_pkgs))
    return render_template(
        "packages_listing.html",
        packages=dom_pkgs,
        category="domestic",
        page_title="Domestic Tour Packages",
        page_subtitle="Explore 5 Indian states / 17 handcrafted packages / Complimentary Travel Insurance",
        dest_slugs=dest_slugs,
        DESTINATIONS=DESTINATIONS,
    )


# ── Error handlers ──────────────────────────────────────────────────────────
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

# ── Live API Integration (SerpApi) ──────────────────────────────────────────
# Using Google Flights API via SerpApi
SERPAPI_KEY = '46c9a9dd7ab268b224f9b08814f903b48ddfe57f36feea36c59d46a36050a5ed'

# IATA_MAP removed - we now accept dynamic IATA|City format from the frontend

@app.route("/api/search_live")
def search_live():
    departure = request.args.get('departure', 'any').lower()
    destination = request.args.get('destination', 'any').lower()
    trip_type = request.args.get('trip_type', 'one_way').lower()
    return_date = request.args.get('return_date', '').strip()
    try:
        adults = max(1, min(9, int(request.args.get('adults', request.args.get('persons', 1)))))
    except (TypeError, ValueError):
        adults = 1
    try:
        children = max(0, min(8, int(request.args.get('children', 0))))
    except (TypeError, ValueError):
        children = 0
    try:
        infants = max(0, min(adults, int(request.args.get('infants', 0))))
    except (TypeError, ValueError):
        infants = 0
    persons = adults + children + infants
    
    # Use selected date, fallback to 7 days from today if empty or in the past
    today_str = datetime.now().strftime("%Y-%m-%d")
    default_future = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    date_val = request.args.get('date', '').strip()
    if not date_val:
        date_val = default_future
    # SerpApi Google Flights requires YYYY-MM-DD
    if len(date_val) == 7:
        date_val += "-01"
    if date_val < today_str:
        date_val = default_future
    # Parse IATA|CityName
    dep_parts = departure.split('|')
    dest_parts = destination.split('|')
    
    dep_iata = dep_parts[0].upper() if len(dep_parts) > 0 and dep_parts[0] != 'any' else 'DEL'
    dep_name = dep_parts[1].title() if len(dep_parts) > 1 else 'Delhi'
    
    dest_iata = dest_parts[0].upper() if len(dest_parts) > 0 and dest_parts[0] != 'any' else 'DXB'
    dest_name = dest_parts[1].title() if len(dest_parts) > 1 else 'Dubai'

    # Compute nights for round trip
    nights = 1
    checkin_dt = datetime.strptime(date_val, "%Y-%m-%d")
    is_valid_round_trip = False
    if trip_type == 'round_trip' and return_date:
        try:
            ret_dt = datetime.strptime(return_date, "%Y-%m-%d")
            if ret_dt > checkin_dt:
                nights = (ret_dt - checkin_dt).days
                checkout_date = return_date
                is_valid_round_trip = True
            else:
                checkout_date = (checkin_dt + timedelta(days=1)).strftime("%Y-%m-%d")
        except ValueError:
            checkout_date = (checkin_dt + timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        checkout_date = (checkin_dt + timedelta(days=1)).strftime("%Y-%m-%d")
    
    try:
        traveller_qs = f"&adults={adults}" + (f"&children={children}" if children > 0 else "") + (f"&infants_on_lap={infants}" if infants > 0 else "")
        hotel_traveller_qs = f"&adults={adults}" + (f"&children={children}" if children > 0 else "")
        if is_valid_round_trip:
            url_flights = f"https://serpapi.com/search.json?engine=google_flights&departure_id={dep_iata}&arrival_id={dest_iata}&outbound_date={date_val}&return_date={return_date}{traveller_qs}&currency=INR&hl=en&type=1&api_key={SERPAPI_KEY}"
            url_return = f"https://serpapi.com/search.json?engine=google_flights&departure_id={dest_iata}&arrival_id={dep_iata}&outbound_date={return_date}{traveller_qs}&currency=INR&hl=en&type=2&api_key={SERPAPI_KEY}"
        else:
            url_flights = f"https://serpapi.com/search.json?engine=google_flights&departure_id={dep_iata}&arrival_id={dest_iata}&outbound_date={date_val}{traveller_qs}&currency=INR&hl=en&type=2&api_key={SERPAPI_KEY}"
            url_return = None

        url_hotels = f"https://serpapi.com/search.json?engine=google_hotels&q={requests.utils.quote(dest_name)}&check_in_date={date_val}&check_out_date={checkout_date}{hotel_traveller_qs}&currency=INR&hl=en&api_key={SERPAPI_KEY}"

        def fetch_json(u):
            return requests.get(u, timeout=15).json() if u else {}

        with ThreadPoolExecutor(max_workers=3) as pool:
            fut_f = pool.submit(fetch_json, url_flights)
            fut_r = pool.submit(fetch_json, url_return)
            fut_h = pool.submit(fetch_json, url_hotels)
            data = fut_f.result()
            data_ret = fut_r.result()
            data_h = fut_h.result()
        
        if "error" in data:
            return jsonify({"status": "error", "message": data["error"]})

        # Parse return flight timings if round trip
        return_options = []
        if is_valid_round_trip:
            ret_list = data_ret.get("best_flights", []) + data_ret.get("other_flights", [])
            for rf in ret_list[:10]:
                r_legs = rf.get("flights", [])
                if not r_legs:
                    continue
                r_first = r_legs[0]
                r_last = r_legs[-1]
                r_dep_raw = r_first.get("departure_airport", {}).get("time", "16:00")
                r_arr_raw = r_last.get("arrival_airport", {}).get("time", "19:00")
                r_mins = rf.get("total_duration", 180)
                return_options.append({
                    "airline": r_first.get("airline", "Multiple Airlines"),
                    "departure": r_dep_raw[-5:] if " " in r_dep_raw else r_dep_raw,
                    "arrival": r_arr_raw[-5:] if " " in r_arr_raw else r_arr_raw,
                    "duration": f"{r_mins // 60}h {r_mins % 60}m",
                    "stops": "Non-Stop" if len(r_legs) == 1 else f"{len(r_legs)-1} Stop(s)"
                })
            
        # Parse the 'best_flights' from SerpApi to match our mock FLIGHTS structure
        parsed_flights = []
        flights_list = data.get("best_flights", []) + data.get("other_flights", [])
        
        # Take up to 10 flights
        for idx, f in enumerate(flights_list[:10]):
            flight_legs = f.get("flights", [])
            if not flight_legs: continue
            
            first_leg = flight_legs[0]
            last_leg = flight_legs[-1]
            
            # Extract times (SerpApi format is usually "2026-11-01 10:00")
            dep_time_raw = first_leg.get("departure_airport", {}).get("time", "10:00")
            arr_time_raw = last_leg.get("arrival_airport", {}).get("time", "13:00")
            dep_time = dep_time_raw[-5:] if " " in dep_time_raw else dep_time_raw
            arr_time = arr_time_raw[-5:] if " " in arr_time_raw else arr_time_raw
            
            total_duration_mins = f.get("total_duration", 180)
            dur_hours = total_duration_mins // 60
            dur_mins = total_duration_mins % 60
            duration_str = f"{dur_hours}h {dur_mins}m"
            
            stops = "Non-Stop" if len(flight_legs) == 1 else f"{len(flight_legs)-1} Stop(s)"
            
            airline = first_leg.get("airline", "Multiple Airlines")
            airline_code = airline[:2].upper()
            
            raw_price = f.get("price", 0)
            paying_pax = max(1, adults + children)
            price_per_person = round(raw_price / paying_pax) if raw_price else 0
            trip_label = f"Round Trip ({nights}N)" if is_valid_round_trip else "One Way"
            pax_parts = [f"{adults} Adult{'s' if adults > 1 else ''}"]
            if children > 0:
                pax_parts.append(f"{children} Child{'ren' if children > 1 else ''}")
            if infants > 0:
                pax_parts.append(f"{infants} Infant{'s' if infants > 1 else ''}")
            pax_summary = ", ".join(pax_parts)

            # Match return flight timing for round trip
            ret_match = None
            if is_valid_round_trip and return_options:
                same_airline = next((ro for ro in return_options if ro["airline"].lower() == airline.lower()), None)
                ret_match = same_airline or return_options[idx % len(return_options)]

            flight_entry = {
                "id": f"f-live-{dep_iata.lower()}-{dest_iata.lower()}-{date_val}-{trip_type}-{adults}a{children}c{infants}i-{idx}",
                "from_city": f"{dep_name} ({dep_iata})",
                "to_city": f"{dest_name} ({dest_iata})",
                "airline": airline,
                "airline_code": airline_code,
                "duration": duration_str,
                "departure": dep_time,
                "arrival": arr_time,
                "stops": stops,
                "class": f.get("type", "Economy"),
                "trip_type": trip_label,
                "adults": adults,
                "children": children,
                "infants": infants,
                "persons": persons,
                "pax_summary": pax_summary,
                "nights": nights,
                "checkin": date_val,
                "checkout": checkout_date,
                "price_per_person": price_per_person,
                "total_price_all": raw_price,
                "price_display": f"₹{raw_price:,}" if raw_price else "Price unavailable",
                "features": [trip_label, pax_summary, "Google Flights"],
                "dest_label": dest_name
            }
            if ret_match:
                flight_entry["return_date"] = return_date
                flight_entry["return_departure"] = ret_match["departure"]
                flight_entry["return_arrival"] = ret_match["arrival"]
                flight_entry["return_duration"] = ret_match["duration"]
                flight_entry["return_stops"] = ret_match["stops"]
                flight_entry["return_airline"] = ret_match["airline"]
            parsed_flights.append(flight_entry)
            
        parsed_hotels = []
        hotels_list = data_h.get("properties", [])
        
        for idx, h in enumerate(hotels_list[:10]):
            price = h.get("rate_per_night", {}).get("extracted_lowest", 0)
            rating = h.get("overall_rating", 0.0)
            stars = min(5, max(1, int(round(rating)))) if rating else 4
            
            images = h.get("images", [])
            # Fallback to local image if missing
            img_url = images[0].get("original_image") if images else "/static/images/dubai.jpg"
            total_price = price * nights if price else 0
            
            parsed_hotels.append({
                "id": f"h-live-{dest_iata.lower()}-{date_val}-{checkout_date}-{idx}",
                "name": h.get("name", "Premium Hotel"),
                "location": h.get("description", "City Center")[:40] + "...",
                "stars": stars,
                "dest_label": dest_name,
                "price_per_night": price,
                "price_display": f"₹{price:,}/night" if price else "Price unavailable",
                "nights": nights,
                "total_price": total_price,
                "total_display": f"₹{total_price:,}" if total_price else "Price unavailable",
                "checkin": date_val,
                "checkout": checkout_date,
                "highlights": "Live Booking via Google Hotels",
                "amenities": ["Free WiFi", f"{nights} Night{'s' if nights > 1 else ''} Stay", "Google Hotels"],
                "image": img_url,
                "is_external_image": True
            })
            
        return jsonify({
            "status": "success",
            "trip_type": trip_type,
            "persons": persons,
            "nights": nights,
            "checkin": date_val,
            "checkout": checkout_date,
            "flights": parsed_flights,
            "hotels": parsed_hotels,
            "message": "Live data successfully fetched from SerpApi!"
        })
    except Exception as error:
        return jsonify({
            "status": "error",
            "message": f"Live API Error: {str(error)}"
        })


@app.route("/api/search_multicity", methods=["POST"])
def search_multicity():
    payload = request.get_json(silent=True) or {}
    legs = payload.get("legs", [])
    if not legs:
        return jsonify({"status": "error", "message": "Please provide at least one flight leg."})
    try:
        adults = max(1, min(9, int(payload.get("adults", payload.get("persons", 1)))))
    except (TypeError, ValueError):
        adults = 1
    try:
        children = max(0, min(8, int(payload.get("children", 0))))
    except (TypeError, ValueError):
        children = 0
    try:
        infants = max(0, min(adults, int(payload.get("infants", 0))))
    except (TypeError, ValueError):
        infants = 0
    persons = adults + children + infants
    mc_traveller_qs = f"&adults={adults}" + (f"&children={children}" if children > 0 else "") + (f"&infants_on_lap={infants}" if infants > 0 else "")
    mc_hotel_qs = f"&adults={adults}" + (f"&children={children}" if children > 0 else "")
    pax_parts = [f"{adults} Adult{'s' if adults > 1 else ''}"]
    if children > 0:
        pax_parts.append(f"{children} Child{'ren' if children > 1 else ''}")
    if infants > 0:
        pax_parts.append(f"{infants} Infant{'s' if infants > 1 else ''}")
    pax_summary = ", ".join(pax_parts)

    today_str = datetime.now().strftime("%Y-%m-%d")
    normalized_legs = []
    for i, leg in enumerate(legs):
        dep_parts = (leg.get("departure") or "DEL|Delhi").split("|")
        dest_parts = (leg.get("destination") or "DXB|Dubai").split("|")
        dep_iata = dep_parts[0].upper() if dep_parts[0] != "any" else "DEL"
        dep_name = dep_parts[1].title() if len(dep_parts) > 1 else dep_iata
        dest_iata = dest_parts[0].upper() if dest_parts[0] != "any" else "DXB"
        dest_name = dest_parts[1].title() if len(dest_parts) > 1 else dest_iata

        date_val = (leg.get("date") or "").strip()
        if not date_val or date_val < today_str:
            date_val = (datetime.now() + timedelta(days=7 + i * 3)).strftime("%Y-%m-%d")

        normalized_legs.append({
            "leg_index": i + 1,
            "dep_iata": dep_iata,
            "dep_name": dep_name,
            "dest_iata": dest_iata,
            "dest_name": dest_name,
            "date": date_val,
        })

    # Determine stay cities & durations between consecutive legs
    stays = []
    for i in range(len(normalized_legs)):
        curr = normalized_legs[i]
        if i < len(normalized_legs) - 1:
            nxt = normalized_legs[i + 1]
            c_dt = datetime.strptime(curr["date"], "%Y-%m-%d")
            n_dt = datetime.strptime(nxt["date"], "%Y-%m-%d")
            nights = max(1, (n_dt - c_dt).days)
            checkout = nxt["date"] if n_dt > c_dt else (c_dt + timedelta(days=1)).strftime("%Y-%m-%d")
            stays.append({
                "city": curr["dest_name"],
                "iata": curr["dest_iata"],
                "checkin": curr["date"],
                "checkout": checkout,
                "nights": nights,
            })
        else:
            # If final destination is not the origin of leg 1, suggest a 2-night stay there too
            if curr["dest_iata"] != normalized_legs[0]["dep_iata"]:
                c_dt = datetime.strptime(curr["date"], "%Y-%m-%d")
                checkout = (c_dt + timedelta(days=2)).strftime("%Y-%m-%d")
                stays.append({
                    "city": curr["dest_name"],
                    "iata": curr["dest_iata"],
                    "checkin": curr["date"],
                    "checkout": checkout,
                    "nights": 2,
                })

    def fetch_leg_flights(leg):
        url_f = (
            f"https://serpapi.com/search.json?engine=google_flights"
            f"&departure_id={leg['dep_iata']}&arrival_id={leg['dest_iata']}"
            f"&outbound_date={leg['date']}{mc_traveller_qs}&currency=INR&hl=en&type=2&api_key={SERPAPI_KEY}"
        )
        try:
            res = requests.get(url_f, timeout=15).json()
            flights_list = res.get("best_flights", []) + res.get("other_flights", [])
            out = []
            for idx, f in enumerate(flights_list[:4]):
                flight_legs = f.get("flights", [])
                if not flight_legs:
                    continue
                first_leg = flight_legs[0]
                last_leg = flight_legs[-1]
                dep_time_raw = first_leg.get("departure_airport", {}).get("time", "10:00")
                arr_time_raw = last_leg.get("arrival_airport", {}).get("time", "13:00")
                dep_time = dep_time_raw[-5:] if " " in dep_time_raw else dep_time_raw
                arr_time = arr_time_raw[-5:] if " " in arr_time_raw else arr_time_raw
                mins = f.get("total_duration", 180)
                dur_str = f"{mins // 60}h {mins % 60}m"
                stops = "Non-Stop" if len(flight_legs) == 1 else f"{len(flight_legs)-1} Stop(s)"
                airline = first_leg.get("airline", "Multiple Airlines")
                raw_price = f.get("price", 0)
                paying_pax = max(1, adults + children)
                price_pp = round(raw_price / paying_pax) if raw_price else 0
                out.append({
                    "id": f"f-mc-{leg['dep_iata'].lower()}-{leg['dest_iata'].lower()}-{leg['date']}-{adults}a{children}c{infants}i-{idx}",
                    "leg_index": leg["leg_index"],
                    "from_city": f"{leg['dep_name']} ({leg['dep_iata']})",
                    "to_city": f"{leg['dest_name']} ({leg['dest_iata']})",
                    "airline": airline,
                    "airline_code": airline[:2].upper(),
                    "duration": dur_str,
                    "departure": dep_time,
                    "arrival": arr_time,
                    "stops": stops,
                    "class": f.get("type", "Economy"),
                    "trip_type": f"Multi-City Leg {leg['leg_index']}",
                    "date": leg["date"],
                    "adults": adults,
                    "children": children,
                    "infants": infants,
                    "persons": persons,
                    "pax_summary": pax_summary,
                    "price_per_person": price_pp,
                    "total_price_all": raw_price,
                    "price_display": f"₹{raw_price:,}" if raw_price else "Price unavailable",
                    "features": [f"Leg {leg['leg_index']} ({leg['date']})", pax_summary, "Google Flights"],
                    "dest_label": leg["dest_name"],
                })
            return out
        except Exception:
            return []

    def fetch_stay_hotels(stay):
        url_h = (
            f"https://serpapi.com/search.json?engine=google_hotels"
            f"&q={requests.utils.quote(stay['city'])}"
            f"&check_in_date={stay['checkin']}&check_out_date={stay['checkout']}"
            f"{mc_hotel_qs}&currency=INR&hl=en&api_key={SERPAPI_KEY}"
        )
        try:
            res = requests.get(url_h, timeout=15).json()
            hotels_list = res.get("properties", [])
            parsed = []
            for idx, h in enumerate(hotels_list[:6]):
                price = h.get("rate_per_night", {}).get("extracted_lowest", 0)
                rating = h.get("overall_rating", 0.0)
                stars = min(5, max(1, int(round(rating)))) if rating else 4
                images = h.get("images", [])
                img_url = images[0].get("original_image") if images else "/static/images/dubai.jpg"
                total_price = price * stay["nights"] if price else 0
                parsed.append({
                    "id": f"h-mc-{stay['iata'].lower()}-{stay['checkin']}-{stay['checkout']}-{idx}",
                    "name": h.get("name", "Premium Hotel"),
                    "location": (h.get("description") or "City Center")[:40] + "...",
                    "stars": stars,
                    "dest_label": stay["city"],
                    "price_per_night": price,
                    "price_display": f"₹{price:,}/night" if price else "Price unavailable",
                    "nights": stay["nights"],
                    "total_price": total_price,
                    "total_display": f"₹{total_price:,}" if total_price else "Price unavailable",
                    "checkin": stay["checkin"],
                    "checkout": stay["checkout"],
                    "highlights": "Live Booking via Google Hotels",
                    "amenities": ["Free WiFi", f"{stay['nights']} Night{'s' if stay['nights'] > 1 else ''} Stay", "Google Hotels"],
                    "image": img_url,
                    "is_external_image": True,
                })
            return {
                "city": stay["city"],
                "iata": stay["iata"],
                "checkin": stay["checkin"],
                "checkout": stay["checkout"],
                "nights": stay["nights"],
                "hotels": parsed,
            }
        except Exception:
            return {
                "city": stay["city"],
                "iata": stay["iata"],
                "checkin": stay["checkin"],
                "checkout": stay["checkout"],
                "nights": stay["nights"],
                "hotels": [],
            }

    try:
        with ThreadPoolExecutor(max_workers=6) as pool:
            flight_lists = list(pool.map(fetch_leg_flights, normalized_legs))
            hotel_groups = list(pool.map(fetch_stay_hotels, stays))

        all_flights = [f for sub in flight_lists for f in sub]
        return jsonify({
            "status": "success",
            "trip_type": "multi_city",
            "stays": stays,
            "flights": all_flights,
            "hotel_groups": hotel_groups,
            "message": "Multi-city flights and hotels fetched!"
        })
    except Exception as error:
        return jsonify({"status": "error", "message": f"Multi-City API Error: {str(error)}"})


@app.route("/api/hotels_live")
def hotels_live():
    query = request.args.get('q', '').strip() or 'Dubai'
    today_str = datetime.now().strftime("%Y-%m-%d")
    default_future = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    date_val = request.args.get('date', '').strip()
    if not date_val:
        date_val = default_future
    if len(date_val) == 7:
        date_val += "-01"
    if date_val < today_str:
        date_val = default_future

    try:
        checkin_dt = datetime.strptime(date_val, "%Y-%m-%d")
        checkout_date = (checkin_dt + timedelta(days=1)).strftime("%Y-%m-%d")
        encoded_q = requests.utils.quote(query)
        url_hotels = (
            f"https://serpapi.com/search.json?engine=google_hotels"
            f"&q={encoded_q}&check_in_date={date_val}&check_out_date={checkout_date}"
            f"&currency=INR&hl=en&api_key={SERPAPI_KEY}"
        )
        resp_h = requests.get(url_hotels, timeout=15)
        data_h = resp_h.json()

        if "error" in data_h:
            return jsonify({"status": "error", "message": data_h["error"], "hotels": []})

        parsed_hotels = []
        hotels_list = data_h.get("properties", [])
        for idx, h in enumerate(hotels_list[:15]):
            price = h.get("rate_per_night", {}).get("extracted_lowest", 0)
            rating = h.get("overall_rating", 0.0)
            stars = min(5, max(1, int(round(rating)))) if rating else 4
            images = h.get("images", [])
            img_url = images[0].get("original_image") if images else "/static/images/dubai.jpg"
            desc = h.get("description") or h.get("neighborhood") or query
            parsed_hotels.append({
                "id": f"h-live-{idx}-{abs(hash(h.get('name', ''))) % 10000}",
                "name": h.get("name", "Premium Hotel"),
                "location": (desc[:55] + "...") if len(desc) > 55 else desc,
                "stars": stars,
                "dest_label": query,
                "price_per_night": price,
                "price_display": f"₹{price:,}/night" if price else "Price on request",
                "highlights": "Live Booking via Google Hotels",
                "amenities": ["Free WiFi", "Live Pricing", "Google Hotels"],
                "image": img_url,
                "is_external_image": True,
                "source": "live"
            })

        return jsonify({
            "status": "success",
            "hotels": parsed_hotels,
            "query": query
        })
    except Exception as error:
        return jsonify({
            "status": "error",
            "message": f"Live Hotel API Error: {str(error)}",
            "hotels": []
        })


if __name__ == "__main__":
    app.run(debug=True)
