class Presets(object):
    HELP_TEXT = """
Youtube_Downloader Help:

Send any image to setup a permanent custom thumbnail for the videos. 

To delete the previously saved custom thumbnail select in options. 

If no custom thumbnail are available bot will set the default YouTube thumbnail for the videos.

Search inline facility, or paste the YouTube link to start downloading.

JOIN <a href='https://t.me/BioHazard_Bots'>Updates</a> | Repo <a href='https://github.com/Rexinazor/Youtube_Downloader'>LINK</a>   
    """
    WELCOME_MSG = "Hello... {}\nI can download YouTube Videos.\nSearch Inline- select and download."
    OPTIONS_TXT = "I can download YouTube Videos.\nSearch Inline- select and download."
    RESULTS_TXT = "👀 Results:"
    NO_RESULTS = "❌ No Results:"
    DESCRIPTION = "Duration: {} || {}"
    NOT_AUTH_TXT = "❌ ❌ You are not authorized ❌ ❌"
    DEFAULT_TITLE = "Youtube_Downloader Repository"
    DEFAULT_THUMB_URL = "https://image.flaticon.com/icons/png/512/25/25231.png"
    DEFAULT_LINK = "https://github.com/Rexinaxor"
    DEFAULT_DESCRIPTION = "LINK: Rexinazor | Github"
    DEV_TITLE = "Developer information"
    DEV_THUMB_URL = "https://freepikpsd.com/media/2019/10/software-developer-icon-png-2-Transparent-Images.png"
    SHARE_BUTTON_TEXT = "HI..  👋\nCheckout : @{username}\nFor search and download YouTube videos"
    SAVED_THUMB = "<b>✅ Thumbnail Saved Successfully</b>\n<code>This file will be used in next YouTube " \
                  "downloads until you clear it !</code> "
    WAIT_MESSAGE = "Please wait.. for a second !"
    THUMB_CAPTION = "<code>This image is your current thumbnail, Tap </code><b> DEL THUMB </b><code> if you wish to " \
                    "clear it !</code> "
    NO_THUMB = "THere are no thumbnail in your Local Directory, Please upload an image and save it !"
    DEL_THUMB_CNF = "Thumbnail cleared successfully ✅"
    LINK_ERROR = "𝐒𝐨𝐦𝐞 𝐞𝐫𝐫𝐨𝐫𝐬 𝐨𝐜𝐜𝐮𝐫𝐫𝐞𝐝 𝐰𝐡𝐢𝐥𝐞 𝐭𝐡𝐞 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 !\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫.."
    #
    #
    #
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    FINISHED_PROGRESS_STR = "◼️"
    UN_FINISHED_PROGRESS_STR = "◻️"
    CHECKING_LINK = "⏳ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭... ⏳"
    DOWNLOAD_START = "𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠... 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 !"
    UPLOAD_START = "𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐭𝐨 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦..."
    NOT_DOWNLOADABLE = "𝐔𝐑𝐋 𝐍𝐨𝐭 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐚𝐛𝐥𝐞 !"
    CANCEL_PROCESS = "<b>Process Cancelled Successfully</b>  ✅"
    FORMAT_SELECTION = """
<b>Title -</b> {}
<b>Channel -</b> <a href={}>{}</a>
<b>Uploaded On -</b> {}
<b>Views -</b> {}  |  <b>Rating:</b> {}

<b>Select the desired format:</b>
    """
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @RMProjects"
    RCHD_TG_API_LIMIT = "Detected File Size: {}\nSorry. But, I cannot upload files " \
                        "greater than 1.95GB due to Telegram API limitations."
    AD_STRING_TO_REPLACE = "please report this issue on https://yt-dl.org/bug . Make sure you are using the " \
                           "latest version; see  https://yt-dl.org/update  on how to update. Be sure to call " \
                           "youtube-dl with the --verbose flag and include its complete output."
