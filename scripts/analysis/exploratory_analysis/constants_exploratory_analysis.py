COLOR_PALETTE = ['#957fec', '#fff071', '#6cc5ff', '#e3a7d5', '#5ecfce',
                 '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', 
                 '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5', 
                 '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', 
                 '#e5c494']

SELECTED_PROVINCES = [
    'ALBERTA', 'BRITISH COLUMBIA', 'MANITOBA', 'NEW BRUNSWICK',
    'NEWFOUNDLAND AND LABRADOR', 'NORTHWEST TERRITORIES',
    'NOVA SCOTIA', 'ONTARIO', 'QUEBEC', 'SASKATCHEWAN', 'YUKON'
]

ORDERED_DAMAGE_LEVELS = ['NONE', 'MINOR', 'SUBSTANTIAL', 'DESTROYED','MISSING AIRCRAFT']
DEFAULT_COLOR = "#80549c"

DAMAGE_MAPPING = {'NONE': 0, 'MINOR': 1, 'SUBSTANTIAL': 2}

CATEGORY_MAPPING = {
    'WeightCategoryID_DisplayEng': {
        '0-2250 KG       (0-4960 LBS)': 1,
        '2251-5700 KG    (4961-12566 LBS)': 2,
        '5701-27000 KG   (12567-59525 LBS)': 3,
        '27001-272000 KG (59526-599650 LBS)': 4
    },
    'WakeTurbulenceCategoryID_DisplayEng': {
        'LIGHT': 1, 'MEDIUM': 2, 'HEAVY': 3
    },
    'DamageLevelID_DisplayEng': {
        'NONE': 0, 'MINOR': 1, 'SUBSTANTIAL': 2, 'DESTROYED': 3
    }
}

COLUMNS_FOR_HEATMAP = [
    'Latitude', 'Longitude', 'YearOfManuf', 'NumberOfEngine', 
    'WeightCategoryID_DisplayEng', 'WakeTurbulenceCategoryID_DisplayEng',
    'DamageLevelID_DisplayEng'
]