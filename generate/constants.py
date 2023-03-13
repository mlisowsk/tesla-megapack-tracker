GOV_DATA_INFO_DICT = {
    "usa": {
        "id": "us",
        "flag": "🇺🇸",
        "name_short": "U.S. EIA",
        "name_long": "U.S. Energy Information Administration (EIA)",
        "title_extra": "data (>10MW)",
        "output_filename": "us-eia",
        "source_url": "https://www.eia.gov/electricity/monthly/",
    },
    "uk": {
        "id": "uk",
        "flag": "🇬🇧",
        "name_short": "UK REPD",
        "name_long": "UK Renewable Energy Planning Database (REPD)",
        "title_extra": "data (>10MW)",
        "output_filename": "uk-repd",
        "source_url": "https://www.gov.uk/government/publications/renewable-energy-planning-database-monthly-extract",
    },
    "germany": {
        "id": "de",
        "flag": "🇩🇪",
        "name_short": "DE MaStR",
        "name_long": "DE Marktstammdatenregister (MaStR)",
        "title_extra": "data (>10MW)",
        "output_filename": "de-mastr",
        "source_url": "https://www.marktstammdatenregister.de/MaStR/",
    },
}


COUNTRY_EMOJI_DI = {
    "usa": "🇺🇸",
    "australia": "🇦🇺",
    "uk": "🇬🇧",
    "korea": "🇰🇷",
    "philippines": "🇵🇭",
    "germany": "🇩🇪",
    "france": "🇫🇷",
    "italy": "🇮🇹",
    "belgium": "🇧🇪",
    "slovenia": "🇸🇮",
}

US_STATES_LONG_TO_SHORT = {
    "alabama": "AL",
    "alaska": "AK",
    "arizona": "AZ",
    "arkansas": "AR",
    "california": "CA",
    "colorado": "CO",
    "connecticut": "CT",
    "delaware": "DE",
    "florida": "FL",
    "georgia": "GA",
    "hawaii": "HI",
    "idaho": "ID",
    "illinois": "IL",
    "indiana": "IN",
    "iowa": "IA",
    "kansas": "KS",
    "kentucky": "KY",
    "louisiana": "LA",
    "maine": "ME",
    "maryland": "MD",
    "massachusetts": "MA",
    "michigan": "MI",
    "minnesota": "MN",
    "mississippi": "MS",
    "missouri": "MO",
    "montana": "MT",
    "nebraska": "NE",
    "nevada": "NV",
    "new hampshire": "NH",
    "new jersey": "NJ",
    "new mexico": "NM",
    "new york": "NY",
    "north carolina": "NC",
    "north dakota": "ND",
    "ohio": "OH",
    "oklahoma": "OK",
    "oregon": "OR",
    "pennsylvania": "PA",
    "rhode island": "RI",
    "south carolina": "SC",
    "south dakota": "SD",
    "tennessee": "TN",
    "texas": "TX",
    "utah": "UT",
    "vermont": "VT",
    "virginia": "VA",
    "washington": "WA",
    "west virginia": "WV",
    "wisconsin": "WI",
    "wyoming": "WY",
}

US_STATES_SHORT_TO_LONG = {
    "AL": "alabama",
    "AK": "alaska",
    "AZ": "arizona",
    "AR": "arkansas",
    "CA": "california",
    "CO": "colorado",
    "CT": "connecticut",
    "DE": "delaware",
    "FL": "florida",
    "GA": "georgia",
    "HI": "hawaii",
    "ID": "idaho",
    "IL": "illinois",
    "IN": "indiana",
    "IA": "iowa",
    "KS": "kansas",
    "KY": "kentucky",
    "LA": "louisiana",
    "ME": "maine",
    "MD": "maryland",
    "MA": "massachusetts",
    "MI": "michigan",
    "MN": "minnesota",
    "MS": "mississippi",
    "MO": "missouri",
    "MT": "montana",
    "NE": "nebraska",
    "NV": "nevada",
    "NH": "new hampshire",
    "NJ": "new jersey",
    "NM": "new mexico",
    "NY": "new york",
    "NC": "north carolina",
    "ND": "north dakota",
    "OH": "ohio",
    "OK": "oklahoma",
    "OR": "oregon",
    "PA": "pennsylvania",
    "RI": "rhode island",
    "SC": "south carolina",
    "SD": "south dakota",
    "TN": "tennessee",
    "TX": "texas",
    "UT": "utah",
    "VT": "vermont",
    "VA": "virginia",
    "WA": "washington",
    "WV": "west virginia",
    "WI": "wisconsin",
    "WY": "wyoming",
}

# in case we don't have any coordinates, we show them at least in the correct state
# those coordinates are picked randomly (trying to put far from other projects so it becomes more obvious)
US_STATES_TO_EIA_COORDINATES = {
    "alabama": None,
    "alaska": (62.054743, -151.102511),
    "arizona": (36.478429, -109.885254),
    "arkansas": (36.042289, -91.148071),
    "california": (41.122677, -121.300049),
    "colorado": (40.632576, -102.716675),
    "connecticut": (41.904185, -72.03186),
    "delaware": (38.999447, -75.405483),
    "florida": (30.131984, -82.147522),
    "georgia": (32.20459, -81.999207),
    "hawaii": (19.611845, -155.513535),
    "idaho": None,
    "illinois": None,
    "indiana": (41.345135, -85.332338),
    "iowa": None,
    "kansas": None,
    "kentucky": None,
    "louisiana": None,
    "maine": (45.137364, -69.263306),
    "maryland": None,
    "massachusetts": (42.571152, -71.801147),
    "michigan": None,
    "minnesota": None,
    "mississippi": (32.682075, -89.744568),
    "missouri": None,
    "montana": (48.650815, -105.721436),
    "nebraska": None,
    "nevada": (41.543396, -114.906006),
    "new hampshire": None,
    "new jersey": (39.911399, -74.307538),
    "new mexico": (36.449861, -103.677979),
    "new york": (42.652007, -75.50354),
    "north carolina": (36.326042, -76.876831),
    "north dakota": None,
    "ohio": (41.388551, -81.155145),
    "oklahoma": (36.696906, -95.223999),
    "oregon": (45.602253, -118.135986),
    "pennsylvania": None,
    "rhode island": None,
    "south carolina": (34.606760, -79.792266),
    "south dakota": None,
    "tennessee": (36.315642, -83.082733),
    "texas": (33.454054, -95.273438),
    "utah": (40.696903, -109.697891),
    "vermont": None,
    "virginia": (38.160223, -77.808750),
    "washington": None,
    "west virginia": None,
    "wisconsin": (45.217776, -88.206482),
    "wyoming": None,
}
