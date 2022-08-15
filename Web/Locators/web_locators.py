class Web_Locators:
    NAV_BAR_LINKS = '//header[1]/div/a'  # all The 4 Links in The NavBar
    SEARCH_FIELD = 'header-search-input'  # Search Field
    CITY_NAME = '//section[1]/h1[1]'  # Searching Correctly
    CITY_ERROR_MESSAGE = "//h2[contains(text(),'no city found')]"  # Searching Incorrectly
