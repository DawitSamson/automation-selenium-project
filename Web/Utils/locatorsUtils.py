class Utils_Locators:

    NAV_BAR_LINKS = '//header[1]/div/a'  # all The 4 Links in The NavBar

    SEARCH_FIELD = 'header-search-input'  # Search Field
    CITY_NAME = '//section[1]/h1[1]'  # Searching Correctly
    CITY_ERROR_MESSAGE = "//h2[contains(text(),'no city found')]"  # Searching Incorrectly

    # bugs:
    WHO_ARE_WE_BUTTON = '//footer[1]/button[1]'  # The Button That Open The Who Are We Section
    WHO_ARE_WE_LINKS = '//a'  # all The Links in The Page , But I Take Only The Links in The relevant Section

    ACCESSIBILITY_BUTTON = 'toggle-mode-btn'
    ACCESSIBILITY_SECTION = '//div[2]/div[1]/button'
