from selenium.webdriver.common.by import By

class RegisterLocators():
    REGISTER_LINK = (By.XPATH,"//a[@class='ico-register']")
    MALE_RADIO_BUTTON = (By.XPATH,"//input[@value='M']")
    FIRST_NAME_INPUT=   (By.XPATH,"//input[@id='FirstName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='LastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='Email']")
    BIRTH_DAY = (By.XPATH, "//select[@name='DateOfBirthDay']")
    BIRTH_MONTH = (By.XPATH, "//select[@name= 'DateOfBirthMonth']")
    BIRTH_YEAR = (By.XPATH, "//select[@name='DateOfBirthYear']")
    COMPANY_NAME = (By.XPATH, "//input[@id='Company']")
    PASSWORD = (By.XPATH, "//*[@id='Password']")
    CONFIRM_PASSWORD = (By.XPATH, "//*[@id='ConfirmPassword']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='register-button']")
    FIRST_NAME_ERROR = (By.XPATH, "//span[@id='FirstName-error']")
    EMAIL_ERROR = (By.XPATH, "//span[@id='Email-error']")
    REGISTRATION_SUCCESSFUL_MESSAGE = (By.XPATH, "//div[@class='result']")


class LoginLocators():
    LOGIN_LINK = (By.XPATH,"//a[@class='ico-login']")
    EMAIL_INPUT = (By.XPATH,"//*[@id='Email']")
    PASSWORD_INPUT = (By.XPATH,"//*[@id='Password']")
    LOGIN_BUTTON = (By.XPATH,'//button[@class="button-1 login-button"]')
    LOGIN_FAIL = (By.XPATH,"//div[@class='message-error validation-summary-errors']")

class LogoutLocators():
    LOGOUT_LINK = (By.XPATH,"//a[@class='ico-logout']")


class MyAccountLocators():
    MYACCOUNT_LINK = (By.XPATH,"//a[@class='ico-account']")
    CUSTOMER_INFO =  (By.XPATH,"//li[@class='customer-info active']//a[@href='/customer/info']")
    CUSTOMER_ADDRESS = (By.XPATH,"//li[@class='customer-addresses inactive']//a[@href='/customer/addresses']")
    NOPCOOMERCE_HOME = (By.XPATH,"//img[@alt='nopCommerce demo store']")
    CUSTOMER_ORDERS = (By.XPATH,"//li[@class='customer-orders inactive']//a[@href='/order/history']")
    DOWNLOADABLE_PRODUCT = (By.XPATH,"//li[@class='downloadable-products inactive']//a[@href='/customer/downloadableproducts']")
    BACK_IN_STOCK_SUBSCRIPTIONS = (By.XPATH,"//li[@class='back-in-stock-subscriptions inactive']//a[@href='/backinstocksubscriptions/manage']")
    REWARD_POINTS = (By.XPATH,"//li[@class='reward-points inactive']//a[@href='/rewardpoints/history']")
    CHANGE_PASSWORD = (By.XPATH,"//li[@class='change-password inactive']//a[@href='/customer/changepassword']")
    PRODUCT_REVIEWS = (By.XPATH,"//li[@class='customer-reviews inactive']//a[@href='/customer/productreviews']")

class CartLocators():
    CART_PAGE_TITLE = (By.XPATH,"//h1[normalize-space()='Shopping cart']")
    PRODUCT = (By.XPATH,"//img[@title='Show details for Apple MacBook Pro 13-inch']")
    PRODUCT_NAME = (By.XPATH,"//h1")
    PRODUCT_PRICE = (By.XPATH, "//span[@id='price-value-4']")
    PRODUCT_QUANTITY = (By.XPATH, "//input[@id='product_enteredQuantity_4']")
    PRODUCT_ADD_TO_CART = (By.XPATH,"//button[@id='add-to-cart-button-4']")
    CART_PAGE = (By.XPATH,"//span[@class='cart-label']")
    # add to cart
    CART_PAGE_PRODUCT_NAME = (By.XPATH,"//a[@class='product-name']")
    CART_PAGE_PRODUCT_PRICE = (By.XPATH,"//span[@class='product-unit-price']")
    CART_PAGE_PRODUCT_QUANTITY = (By.XPATH,"//input[@id='itemquantity11224']")
    GIFT_WRAP_SELECT_FIELD = (By.XPATH,"//select[@id='checkout_attribute_1']")
    DISCOUNT_CODE_FIELD = (By.XPATH,"//input[@id='discountcouponcode']")
    GIFT_CARDS_FIELD = (By.XPATH,"//input[@id='giftcardcouponcode']")
    APPLY_COUPON_BUTTON  = (By.XPATH,"//button[@id='applydiscountcouponcode']")
    ADD_GIFT_CARD_BUTTON = (By.XPATH,"//button[@id='applygiftcardcouponcode']")
    # remove from cart
    REMOVE_PRODUCT_BUTTON = (By.XPATH,"//button[@class='remove-btn']")
    CART_EMPTY_MESSAGE = (By.XPATH,"//div[@class='no-data']")

class WishListLocators():
    PRODUCT_ADD_TO_WISHLIST = (By.XPATH,"//button[@id='add-to-wishlist-button-4']")
    WISHLIST_PAGE = (By.XPATH,"//span[@class='wishlist-label']")
    WISHLIST_PAGE_TITLE = (By.XPATH,"//h1[normalize-space()='Wishlist']")
    UPDATE_WISHLIST = (By.XPATH,"//button[@id='updatecart']")
    EMAIL_FRIEND = (By.XPATH,"//button[normalize-space()='Email a friend']")
    ADD_TO_CART_CHECKBOX = (By.XPATH,"//input[@name='addtocart']")
    ADD_TO_CART_WISHLISTBUTTON = (By.XPATH,"//button[@name='addtocartbutton']")

class HomePageLocators:
        CURRENCY_SELECTOR = (By.XPATH,"//select[@id='customerCurrency']")
        PRICE = (By.XPATH,"//span[contains(text(), '€1032.00')]")
        SEARCH_BAR = (By.XPATH,"//input[@id='small-searchterms']")
        SEARCH_BUTTON = (By.XPATH,"//button[@class='button-1 search-box-button']")
        SEARCH_RESULT_PRODUCT = (By.XPATH,"//h2[@class='product-title']//a[normalize-space()='Build your own computer']")
        RETURN_HOME = (By.XPATH,"//img[@alt='nopCommerce demo store']")
        COMPUTER_CATEGORY = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']")
        ELECTRONICS_CATEGORY = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']")
        APPAREL_CATEGORY = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Apparel']")
        DIGITAL_DOWNLOADS_CATEGORY = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Digital downloads']")
        BOOKS_CATEGORY = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Books']")
        JEWELRY_CATEGORY = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Jewelry']")
        GIFTCARD_CATEGORY = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Gift Cards']")
        ADD_TO_CART_HOME = (By.XPATH,"//div[@class='page-body']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]")
        WISHLIST_HOME = (By.XPATH,"//div[@class='page-body']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]")
        COMPARELIST_HOME = (By.XPATH,"//div[@class='page-body']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]")
        NEWS_DETAIL = (By.XPATH,"//a[@href='/new-online-store-is-open'][normalize-space()='details']")
        VIEW_NEWS_ARCHIVE = (By.XPATH,"//a[normalize-space()='View News Archive']")
        RATING_RADIO_BUTTON = (By.XPATH,"//input[@id='pollanswers-1']")
        VOTE_BUTTON = (By.XPATH,"//button[@id='vote-poll-1']")
        FACEBOOK_PAGE = (By.XPATH,"//a[@href='http://www.facebook.com/nopCommerce']")
        TWITTER_PAGE = (By.XPATH,"//a[@href='https://twitter.com/nopCommerce']")
        YOUTUBE_PAGE = (By.XPATH,"//a[@href='http://www.youtube.com/user/nopCommerce']")
        NEWS_PAGE = (By.XPATH,"//a[@href='/news/rss/1']")
        NEWS_LETTER_EMAIL = (By.XPATH,"//input[@id='newsletter-email']")
        NEWS_LETTER_SUBSCRIBE= (By.XPATH,"//button[@id='newsletter-subscribe-button']")




