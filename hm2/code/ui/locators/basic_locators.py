from selenium.webdriver.common.by import By


class BasePageLocators(object):
    pass


class LoginPageLocators(BasePageLocators):
    GO_PREV_LOGIN_BUTTON = (By.XPATH, "//*[contains(@class, 'responseHead-module-button')]")
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    GO_LOGIN_BUTTON = (By.XPATH, "//*[contains(@class, 'authForm-module-button')]")
    WRONG_LOGIN_TEXT = (By.XPATH, "//*[contains(@class, 'notify-module-notifyBlock')]")


class LoginErrorPageLocators(BasePageLocators):
    INVALID_LOGIN_TEXTS = (By.XPATH, "//div[contains(@class, 'formMsg_title')]")


class MainPageLocators(BasePageLocators):
    GO_PREV_LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'right-module-rightButton')]")
    HELP_ANIMATING = (By.CSS_SELECTOR, "//*[contains(@class, 'rightMenu-module-visibleRightMenu')]")
    GO_LOGOUT_BUTTON = (By.XPATH, "//*[@href='/logout']")
    GO_CAMPAIGN_BUTTON = (By.XPATH, "//a[contains(@class, 'center-module-campaigns')]")

    GO_SEGMENT_BUTTON = (By.XPATH, "//a[contains(@class, 'center-module-segments')]")


class DashboardPageLocators(MainPageLocators):
    CREATE_CAMPAIGN = (By.XPATH, "//*[contains(@class, 'instruction-module-link')]")
    CREATE_ANOTHER_CAMPAIGN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')

    CAMPAIGN_NAME_CHECK = (By.XPATH, "(//*[contains(@class, 'nameCell-module-campaignNameCell')])[1]/descendant::a[contains(@class,'nameCell-module-campaignName')]")

    FIRST_CAMPAIGN_CHECKBOX = (By.XPATH, "(//input[contains(@class, 'nameCell-module-checkbox')])[1]")
    GO_TABLE_CONTROL_BUTTON = (By.XPATH, "(//*[contains(@class, 'tableControls-module-massActionsSelect')])")
    GO_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'optionsList-module-hasScroll') and @title='Удалить']")


class CreateCampaignPageLocators(MainPageLocators):
    GO_TRAFFIC_BUTTON = (By.XPATH, '//div[contains(text(), "Трафик")]')
    CAMPAIGN_LINK_INPUT_BOX = (By.XPATH, "//input[contains(@class, 'mainUrl-module-searchInput-Su-Rad')]")
    CAMPAIGN_NAME_INPUT_BOX = (By.XPATH, "//*[contains(@class, 'input_campaign-name')]/div[@class='input__wrap']/input")
    GO_BANNER_FORMAT = (By.ID, "patterns_4")

    UPLOAD_IMG_INPUT = (By.XPATH, "//*[contains(@class, 'roles-module-buttonWrap')]/*[contains(@class, 'upload-module-wrapper')]/input")

    LEGAL_INFORMATION_TEXTAREA = (By.XPATH, "//textarea[contains(@class, 'roles-module-roleTextarea')]")

    SLIDER_ICON = (By.XPATH, "//*[contains(@class, 'price-slider-setting__btn')]")
    GRAPH = (By.XPATH, "//*[contains(@class, 'bubble-ts_projection')]")

    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//div[contains(text(),'Создать кампанию')]/..")


class SegmentPageLocators(MainPageLocators):
    CREATE_SEGMENT = (By.XPATH, "//a[contains(@href, '/segments/segments_list/new/')]")
    CREATE_ANOTHER_SEGMENT = (By.XPATH, "//*[contains(@class,'segments-list__btn-wrap')]/button[contains(@class,'button_submit')]")

    ALL_SEGMENTS = (By.XPATH, "//div[contains(@class, 'main-module-CellFirst')]/ancestor::div[contains(@class, 'ReactVirtualized__Grid__innerScrollContainer')]/descendant::a")

    NEW_SEGMENT_NAME_CHECK = (By.XPATH, "//div[contains(@class, 'main-module-CellFirst')]/ancestor::div[contains(@class, 'ReactVirtualized__Grid__innerScrollContainer')]/descendant::a[1]")
    NEXT_SEGMENT_NAME_CHECK = (By.XPATH, "//div[contains(@class, 'main-module-CellFirst')]/ancestor::div[contains(@class, 'ReactVirtualized__Grid__innerScrollContainer')]/descendant::a[2]")

    NEW_SEGMENT_ID_CHECK = (By.XPATH, "(//div[contains(@class, 'main-module-CellFirst')]/ancestor::div[contains(@class, 'ReactVirtualized__Grid__innerScrollContainer')]/descendant::div[contains(@class, 'segmentsTable-module-idCellWrap')]/span)[1]")
    NEXT_SEGMENT_ID_CHECK = (By.XPATH, "(//div[contains(@class, 'main-module-CellFirst')]/ancestor::div[contains(@class, 'ReactVirtualized__Grid__innerScrollContainer')]/descendant::div[contains(@class, 'segmentsTable-module-idCellWrap')]/span)[2]")

    DELETE_NEW_SEGMENT = (By.XPATH, "(//*[contains(@class, 'cells-module-removeCell')])[1]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//*[contains(@class,'button_confirm-remove')]")

    COUNT_OF_SEGMENTS = (By.XPATH, "(//span[contains(@class, 'left-nav__count')])[1]")

    INSTRUCTIONS = (By.XPATH, "//*[contains(@class, 'page_segments__instruction-wrap')]")


class CreateSegmentPageLocators(MainPageLocators):
    SEGMENT_CHECKBOX = (By.XPATH, "//input[contains(@class, 'adding-segments-source__checkbox')]")
    ADD_SEGMENT_BUTTON = (By.XPATH, "//*[contains(@class, 'adding-segments-modal__btn-wrap ')]/button[contains(@class, 'button_submit')]")

    SEGMENT_NAME_INPUT = (By.XPATH, "//*[contains(@class, 'input_create-segment-form')]/descendant::input")
    CREATE_SEGMENT_BUTTON = (By.XPATH, "//*[contains(@class,'create-segment-form__btn-wrap')]/button[contains(@class,'button_submit')]")


