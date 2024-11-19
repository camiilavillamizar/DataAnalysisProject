


OCEAN_COORDINATES = {
    'NORTH PACIFIC OCEAN': [50.0, -145.0], 
    'NORTH ATLANTIC OCEAN': [48.0, -50.0], 
    'ARCTIC OCEAN': [75.0, -95.0], 
    'SOUTH PACIFIC OCEAN': [-10.0, -140.0], 
    'MEDITERRANEAN SEA': [35.0, 18.0], 
    'SOUTH CHINA SEA': [15.0, 115.0], 
    'ANTARCTIC OCEAN': [-68.438, -160.234],
    'SOUTH ATLANTIC OCEAN': [-33.7243, -15.9961],
    'INDIAN OCEAN': [-33.1376, 81.8262]
}

OCEAN_PROVINCES_COORDINATES = {
    'ATLANTIC': {
        'PRINCE EDWARD ISLAND': [46.25, -63.0],
        'NOVA SCOTIA': [44.65, -63.57],
        'NEW BRUNSWICK': [45.95, -64.8],
        'NEWFOUNDLAND AND LABRADOR': [49.25, -53.5],
        'QUEBEC': [50.0, -60.0],
        'ONTARIO': [44.0, -77.5],  # Closest approximation for Atlantic connection.
        'ALBERTA': [53.0, -113.5],  # Alberta has no direct Atlantic connection; internal approximation.
        'MANITOBA': [50.0, -96.0],  # Manitoba has no direct Atlantic connection either; internal approximation.
        'NUNAVUT': [63.5, -68.5],
        'NEW JERSEY': [39.8, -74.4],
        'SASKATCHEWAN': [52.0, -106.0],  # Saskatchewan is not near the Atlantic; internal approximation.
        'NEW HAMPSHIRE': [43.2, -71.5],
        'MASSACHUSETTS': [42.4, -70.9],
        'MAINE': [44.1, -69.0],
        'BRITISH COLUMBIA': [48.4, -123.4]  # Approximation; British Columbia is in the Pacific region.
    },
    'PACIFIC': {
        'BRITISH COLUMBIA': [48.4, -123.4],
        'ONTARIO': [48.0, -123.0],  # Closest point to the Pacific Ocean.
        'ALBERTA': [53.5, -114.0],
        'YUKON': [60.7, -135.05],
        'WASHINGTON': [47.5, -122.3],
        'ARIZONA': [34.0, -112.0],  # Arizona is far from the Pacific; internal approximation.
        'ALASKA': [57.0, -135.0],
        'CALIFORNIA': [36.8, -121.5],
        'MANITOBA': [50.0, -96.8],  # Manitoba has no Pacific connection; internal approximation.
        'NORTHWEST TERRITORIES': [62.0, -114.4]
    },
    'NORTH ATLANTIC': {
        'NEWFOUNDLAND AND LABRADOR': [49.0, -54.0],
        'ALBERTA': [53.5, -113.0],  # Alberta is far from the North Atlantic; internal approximation.
        'NOVA SCOTIA': [44.5, -63.6]
    }
}

COUNTRY_PROVINCE_COORDINATES = {
    "CANADA": {
        # Largest city in Prince Edward Island is Charlottetown
        "PRINCE EDWARD ISLAND": [46.2382, -63.1311],  
        # Largest city in Manitoba is Winnipeg
        "MANITOBA": [49.8951, -97.1384],  
        # Largest city in Ontario is Toronto
        "ONTARIO": [43.65107, -79.347015],  
        # Largest city in Nunavut is Iqaluit
        "NUNAVUT": [63.7467, -68.5170],  
        # Largest city in British Columbia is Vancouver
        "BRITISH COLUMBIA": [49.2827, -123.1207],  
        # Largest city in Nova Scotia is Halifax
        "NOVA SCOTIA": [44.6488, -63.5752],  
        # Largest city in Quebec is Montreal
        "QUEBEC": [45.5017, -73.5673],  
        # Largest city in Saskatchewan is Saskatoon
        "SASKATCHEWAN": [52.1332, -106.6700],  
        # Largest city in Alberta is Calgary
        "ALBERTA": [51.0447, -114.0719],  
        # Largest settlement in Northwest Territories is Yellowknife
        "NORTHWEST TERRITORIES": [62.4540, -114.3718],  
        # Largest city in New Brunswick is Moncton
        "NEW BRUNSWICK": [46.0878, -64.7782],  
        # Largest city in Newfoundland and Labrador is St. John's
        "NEWFOUNDLAND AND LABRADOR": [47.5615, -52.7126],  
        # Largest city in Yukon is Whitehorse
        "YUKON": [60.7212, -135.0568]  
    },
    "UNITED STATES": {
        # Example with well-known cities or state capitals
        "CALIFORNIA": [34.0522, -118.2437],  # Los Angeles
        "NEW MEXICO": [35.0844, -106.6504],  # Albuquerque
        "INDIANA": [39.7684, -86.1581],  # Indianapolis
        "HAWAII": [21.3069, -157.8583],  # Honolulu
        "NEW JERSEY": [40.7357, -74.1724],  # Newark
        "WASHINGTON": [47.6062, -122.3321],  # Seattle
        "MICHIGAN": [42.3314, -83.0458],  # Detroit
        "NORTH DAKOTA": [46.8772, -96.7898],  # Fargo
        "COLORADO": [39.7392, -104.9903],  # Denver
        "NEW YORK": [40.7128, -74.0060],  # New York City
        "FLORIDA": [25.7617, -80.1918],  # Miami
        "NORTH CAROLINA": [35.2271, -80.8431],  # Charlotte
        "OREGON": [45.5051, -122.6750],  # Portland
        "ARIZONA": [33.4484, -112.0740],  # Phoenix
        "TEXAS": [29.7604, -95.3698],  # Houston
        "UTAH": [40.7608, -111.8910],  # Salt Lake City
        "ALASKA": [61.2181, -149.9003],  # Anchorage
        "VIRGINIA": [37.5407, -77.4360],  # Richmond
        "DISTRICT OF COLUMBIA": [38.9072, -77.0369],  # Washington, D.C.
        "MAINE": [43.6591, -70.2568],  # Portland
        "PENNSYLVANIA": [39.9526, -75.1652],  # Philadelphia
        "KENTUCKY": [38.2527, -85.7585],  # Louisville
        "WISCONSIN": [43.0389, -87.9065],  # Milwaukee
        "WYOMING": [41.1398, -104.8202],  # Cheyenne
        "MISSOURI": [38.6270, -90.1994],  # St. Louis
        "CONNECTICUT": [41.7658, -72.6734],  # Hartford
        "NEVADA": [36.1716, -115.1391],  # Las Vegas
        "GEORGIA": [33.7490, -84.3880],  # Atlanta
        "ARKANSAS": [34.7465, -92.2896],  # Little Rock
        "MASSACHUSETTS": [42.3601, -71.0589],  # Boston
        "ILLINOIS": [41.8781, -87.6298],  # Chicago
        "SOUTH DAKOTA": [44.3668, -100.3538],  # Pierre
        "OHIO": [39.9612, -82.9988],  # Columbus
        "MINNESOTA": [44.9778, -93.2650],  # Minneapolis
        "IOWA": [41.5868, -93.6250],  # Des Moines
        "KANSAS": [39.0997, -94.5786],  # Kansas City
        "MARYLAND": [39.2904, -76.6122],  # Baltimore
        "MONTANA": [46.5891, -112.0391],  # Helena
        "SOUTH CAROLINA": [34.0007, -81.0348],  # Columbia
        "TENNESSEE": [36.1627, -86.7816],  # Nashville
        "NEBRASKA": [41.2565, -95.9345],  # Omaha
        "RHODE ISLAND": [41.8240, -71.4128],  # Providence
        "VERMONT": [44.2624, -72.5800],  # Montpelier
        "LOUISIANA": [29.9511, -90.0715],  # New Orleans
        "IDAHO": [43.6150, -116.2023],  # Boise
        "NEW HAMPSHIRE": [43.2081, -71.5376],  # Concord
        "ALABAMA": [32.3668, -86.3000],  # Montgomery
        "WEST VIRGINIA": [38.3498, -81.6326],  # Charleston
        "DELAWARE": [39.7391, -75.5398],  # Wilmington
        "PUERTO RICO": [18.4655, -66.1057],  # San Juan
        "MISSISSIPPI": [32.2988, -90.1848],  # Jackson
        "OKLAHOMA": [35.4676, -97.5164]  # Oklahoma City
    }
}

COUNTRIES_COORDINATES = {
    "GUATEMALA": [14.6349, -90.5069],  # Guatemala City
    "AUSTRIA": [48.2082, 16.3738],  # Vienna
    "CHILE": [-33.4489, -70.6693],  # Santiago
    "ICELAND": [64.1355, -21.8954],  # Reykjavik
    "MEXICO": [19.4326, -99.1332],  # Mexico City
    "AZERBAIJAN": [40.4093, 49.8671],  # Baku
    "PERU": [-12.0464, -77.0428],  # Lima
    "RUSSIA": [55.7558, 37.6173],  # Moscow
    "FRANCE": [48.8566, 2.3522],  # Paris
    "GRENADA": [12.0561, -61.7488],  # St. George's
    "UNITED KINGDOM": [51.5074, -0.1278],  # London
    "FIJI": [-18.1248, 178.4501],  # Suva
    "EGYPT ARAB REP. OF": [30.0444, 31.2357],  # Cairo
    "TAIWAN": [25.0330, 121.5654],  # Taipei
    "THAILAND": [13.7563, 100.5018],  # Bangkok
    "GERMANY": [52.5200, 13.4050],  # Berlin
    "DEM PEOPLE'S REP KOREA": [39.0392, 125.7625],  # Pyongyang
    "JAPAN": [35.6895, 139.6917],  # Tokyo
    "PUERTO RICO": [18.4655, -66.1057],  # San Juan
    "IRELAND": [53.3498, -6.2603],  # Dublin
    "TURKEY": [39.9208, 32.8541],  # Ankara
    "GREENLAND": [64.1835, -51.7216],  # Nuuk
    "SPAIN": [40.4168, -3.7038],  # Madrid
    "CHINA": [39.9042, 116.4074],  # Beijing
    "EL SALVADOR": [13.6929, -89.2182],  # San Salvador
    "ARGENTINA": [-34.6037, -58.3816],  # Buenos Aires
    "HONG KONG": [22.3193, 114.1694],  # Hong Kong
    "ALBANIA": [41.3275, 19.8189],  # Tirana
    "VENEZUELA": [10.4806, -66.9036],  # Caracas
    "KENYA": [-1.2864, 36.8172],  # Nairobi
    "DOMINICAN REPUBLIC": [18.4861, -69.9312],  # Santo Domingo
    "TRINIDAD AND TOBAGO": [10.6918, -61.2225],  # Port of Spain
    "IVORY COAST": [5.3453, -4.0244],  # Abidjan
    "BAHAMAS": [25.0343, -77.3963],  # Nassau
    "JAMAICA": [18.1096, -77.2975],  # Kingston
    "BRAZIL": [-23.5505, -46.6333],  # São Paulo
    "COLOMBIA": [4.7110, -74.0721],  # Bogotá
    "NEW ZEALAND": [-36.8485, 174.7633],  # Auckland
    "KUWAIT": [29.3759, 47.9774],  # Kuwait City
    "GERMAN DEM. REP.": [52.5200, 13.4050],  # Berlin (historical)
    "BARBADOS": [13.0978, -59.6171],  # Bridgetown
    "BELGIUM": [50.8503, 4.3517],  # Brussels
    "SINGAPORE": [1.3521, 103.8198],  # Singapore
    "NETHERLANDS": [52.3676, 4.9041],  # Amsterdam
    "YEMEN": [15.3694, 44.1910],  # Sana'a
    "HAITI": [18.5944, -72.3074],  # Port-au-Prince
    "AUSTRALIA": [-33.8688, 151.2093],  # Sydney
    "MARTINIQUE": [14.6415, -61.0242],  # Fort-de-France
    "INDIA": [28.6139, 77.2090],  # New Delhi
    "INDONESIA": [-6.2088, 106.8456],  # Jakarta
    "CUBA": [23.1136, -82.3666],  # Havana
    "ITALY": [41.9028, 12.4964],  # Rome
    "NORWAY": [59.9139, 10.7522],  # Oslo
    "ALGERIA": [36.7529, 3.0420],  # Algiers
    "SUDAN": [15.5007, 32.5599],  # Khartoum
    "ETHIOPIA": [9.1450, 40.4897]  # Addis Ababa
}

COUNTRIES_CARDINAL_DIRECTIONS = {
    'GERMANY': ['N', 'E'],          # Northern Hemisphere, Eastern Hemisphere
    'UNITED KINGDOM': ['N', 'W'],   # Northern Hemisphere, Western Hemisphere
    'DENMARK': ['N', 'E'],          # Northern Hemisphere, Eastern Hemisphere
    'CANADA': ['N', 'W'],           # Northern Hemisphere, Western Hemisphere
    'UNITED STATES': ['N', 'W'],    # Northern Hemisphere, Western Hemisphere
    'IRELAND': ['N', 'W'],          # Northern Hemisphere, Western Hemisphere
    'FRANCE': ['N', 'E'],           # Northern Hemisphere, Eastern Hemisphere
    'SPAIN': ['N', 'W'],            # Northern Hemisphere, Western Hemisphere
    'AZORES': ['N', 'W'],           # Northern Hemisphere, Western Hemisphere
    'GREENLAND': ['N', 'W'],        # Northern Hemisphere, Western Hemisphere
    'ICELAND': ['N', 'W'],          # Northern Hemisphere, Western Hemisphere
}

OCEAN_CARDINAL_DIRECTIONS = {
    'NORTH ATLANTIC OCEAN': ['N', 'W']
}