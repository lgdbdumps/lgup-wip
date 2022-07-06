DOMAIN_NAME_UPLOAD='library.bz'
PROTO='https://'
USER='genesis'
PSWD='upload'
PATH='main/upload/'
UPLOAD_URL=PROTO + USER + ':' + PSWD + '@' + DOMAIN_NAME_UPLOAD + '/' + PATH
BATCH_SEARCH_PAGE='https://libgen.rs/batchsearchindex.php'

READ_BUFFER_SIZE=65536
ISBN_REGEX=r'isbn(-)?(13|10)?(:)?(\s)(.*)'

XPATH_SELECTOR_INPUT_FILE='//input[@type="file"]'
XPATH_SELECTOR_FILE_SUBMIT='//input[@type="submit"]'
XPATH_SELECTOR_ISBN_FIELD='//input[@name="isbn"]'
XPATH_SELECTOR_META_QUERY_FIELD='//input[@name="metadata_query"]'
XPATH_SELECTOR_META_QUERY_SUBMIT='//input[@name="fetch_metadata"]'
XPATH_SELECTOR_FINAL_SUBMIT='//input[@value="SUBMIT!"]'
XPATH_SELECTOR_OPTION='//select[@name="metadata_source"]'
XPATH_SELECTOR_STATUS_RESULT='//body//div[3]'

XPATH_SELECTOR_DUP_SEARCH_CHECKBOX_MD5='//input[@name="md5hash"]'
XPATH_SELECTOR_DUP_SEARCH_CHECKBOX_ISBN='//input[@name="isbn"]'
XPATH_SELECTOR_INPUT_FIELD='//textarea[@name="dsk"]'
XPATH_SELECTOR_DUP_SEARCH_SUBMIT='//input[@name="submit"]'
XPATH_SELECTOR_DUP_IS_PRESENT='//td[@width="40"]'

OK_STATUS='The record has been successfully saved.'

ALLOWED_EXT=['PDF', 'DJVU', 'EPUB', 'MOBI', 'AZW', 'AZW3', 'AZW4', 'FB2', 'CHM', 'RTF', 'DOC', 'DOCX', 'ZIP', 'RAR', '7Z', 'CBZ', 'CBR', 'CB7']
ALLOWED_FILE_HEADERS=['PDF', 'EPUB', 'Mobipocket', 'Zip', 'RAR', 'DjVu', 'HtmlHelp', 'Rich Text', 'XML', 'Microsoft Word']
KiB=1024
MiB=1048576
MIN_SIZE=30 * KiB
MAX_SIZE=1024 * MiB

CHROMEDRIVER_PATH=r"C:\app\chromedriver_win32\chromedriver.exe"

START_BANNER='''
                                                                                 
                                                                                 
LLLLLLLLLLL                    GGGGGGGGGGGGG                                     
L:::::::::L                 GGG::::::::::::G                                     
L:::::::::L               GG:::::::::::::::G                                     
LL:::::::LL              G:::::GGGGGGGG::::G                                     
  L:::::L               G:::::G       GGGGGGuuuuuu    uuuuuu ppppp   ppppppppp   
  L:::::L              G:::::G              u::::u    u::::u p::::ppp:::::::::p  
  L:::::L              G:::::G              u::::u    u::::u p:::::::::::::::::p 
  L:::::L              G:::::G    GGGGGGGGGGu::::u    u::::u pp::::::ppppp::::::p
  L:::::L              G:::::G    G::::::::Gu::::u    u::::u  p:::::p     p:::::p
  L:::::L              G:::::G    GGGGG::::Gu::::u    u::::u  p:::::p     p:::::p
  L:::::L              G:::::G        G::::Gu::::u    u::::u  p:::::p     p:::::p
  L:::::L         LLLLLLG:::::G       G::::Gu:::::uuuu:::::u  p:::::p    p::::::p
LL:::::::LLLLLLLLL:::::L G:::::GGGGGGGG::::Gu:::::::::::::::uup:::::ppppp:::::::p
L::::::::::::::::::::::L  GG:::::::::::::::G u:::::::::::::::up::::::::::::::::p 
L::::::::::::::::::::::L    GGG::::::GGG:::G  uu::::::::uu:::up::::::::::::::pp  
LLLLLLLLLLLLLLLLLLLLLLLL       GGGGGG   GGGG    uuuuuuuu  uuuup::::::pppppppp    
                                                              p:::::p            
                                                              p:::::p            
                                                             p:::::::p           
                                                             p:::::::p           
                                                             p:::::::p           
                                                             ppppppppp           
                                                                                 
'''
