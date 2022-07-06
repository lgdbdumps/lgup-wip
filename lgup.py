#!/usr/bin/env python3

import os
import sys
import hashlib
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import magic

from constants import *
import globals_data

def start_selenium(headless=False):
    options = Options()
    options.add_argument("--start-maximized")
    if headless:
        options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("user-agent=Chrome/53.0.2704.79 Safari/537.36 Edge/14.14393")
    globals_data.browser = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_PATH)

def init():
    start_selenium()
    globals_data.browser.get(BATCH_SEARCH_PAGE)

def upload_file(filename, isbn=None):
    try:
        globals_data.browser.get(UPLOAD_URL)

        input_file_elem = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_INPUT_FILE)
        input_file_elem.send_keys(filename)
        
        submit_button = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_FILE_SUBMIT)
        submit_button.click()
        
        time.sleep(5)
        
        
        metadata_source = Select(globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_OPTION))
        metadata_source.select_by_value('google_books')
        
        isbn = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_ISBN_FIELD)
        isbn_text = isbn.get_attribute('value').split(',')

        isbn_field_input = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_META_QUERY_FIELD)
        isbn_field_input.send_keys(isbn_text[0])
        
        submit_button = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_META_QUERY_SUBMIT)
        submit_button.click()
        
        time.sleep(5)
        
        final_button = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_FINAL_SUBMIT)
        final_button.click()

        status = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_STATUS_RESULT)
    except Exception:
        return False
    if status.text == OK_STATUS:
        return True
    else:
        return False

def check_duplicates(book_list, type_of_id):
    init()
    if type_of_id.upper() == 'MD5':
        checkbox = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_DUP_SEARCH_CHECKBOX_MD5)
    else:
        checkbox = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_DUP_SEARCH_CHECKBOX_ISBN)
    checkbox.click()
    text_field = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_INPUT_FIELD)
    for i, book in enumerate(book_list):
        if type_of_id.upper() == 'MD5':
            text_field.send_keys(book.md5)
        else:
            text_field.send_keys(book.isbn)
        if i < len(book_list) - 1: # do not insert one more newline
            text_field.send_keys(Keys.RETURN)
    submit_button = globals_data.browser.find_element_by_xpath(XPATH_SELECTOR_DUP_SEARCH_SUBMIT)
    submit_button.click()
    rows = globals_data.browser.find_elements_by_xpath(XPATH_SELECTOR_DUP_IS_PRESENT)
    i = 0
    for row in rows[1:]:
        if row.text != '0': # > 0 duplicate(s) are found
            book_list[i].is_duplicate = True
        else:
            book_list[i].is_duplicate = False
        i += 1

def remove_hyphens(isbn):
    return isbn.replace('-', '')            
    
def compute_md5(book_list):
    for book in book_list:
        f = open(book.filename, 'rb')
        h = hashlib.md5(f.read())
        #for data in f.read(READ_BUFFER_SIZE):
        #    h.update(data)
        book.md5 = h.hexdigest()

def check_filesize(book_list):
    for book in book_list:
        if MIN_SIZE < book.size < MAX_SIZE :
            book.is_size_ok = True
        else:
            book.is_size_ok = False

def check_file_ext(book_list):
    for book in book_list:
        name, dot_ext = os.path.splitext(book.filename)
        ext = dot_ext.replace('.', '').upper()
        if ext not in ALLOWED_EXT:
            book.is_ext_ok = False
        else:
            book.is_ext_ok = True

def check_file_header(book_list):
    for book in book_list:
        filetype_header_str=magic.from_file(book.filename)
        for allowed_ftype in ALLOWED_FILE_HEADERS:
            if allowed_ftype in filetype_header_str:
                book.is_file_header_ok = True
                break
        else:
            book.is_file_header_ok = False

def check_is_well_formed(book_list):
    for book in book_list:
        try:
            pdf = pikepdf.Pdf.open(book.filename)
            pdf.check()
            pdf.close()
        except Exception:
            book.is_well_formed = False
        else:
            book.is_well_formed = True          
        
def file_check(book_list):
    check_file_ext(book_list)
    check_file_header(book_list)
    check_filesize(book_list)
    compute_md5(book_list)
    check_duplicates(book_list, 'MD5')
    #check_file_is_clean(book_list)
    #check_is_well_formed(book_list)

def get_full_filenames(path):
    for dir, _, filenames in os.walk(path):
        for filename in filenames:
            fullpath = os.path.join(dir, filename)
            size=os.stat(fullpath)[6]
            globals_data.list_of_books.append(globals_data.book_data(fullpath, size))

def find_string(filename, string):
    pass

def do_ocr(filename):
    pass

def signal_handler():
    pass

def arg_parser():
    pass

def test(args):
    get_full_filenames(args[1])
    file_check(globals_data.list_of_books)
    dupl_num = 0
    nodupl_num = 0
    for book in globals_data.list_of_books:
        if not book.is_duplicate :
            print("%s : %s\n%s : %s\n%s : %s\n%s : %s\n%s : %s\n%s : %s\n%s : %s\n%s : %s\n\n" % ("filename", book.filename, "md5", book.md5, "size", book.size, "well formed?", book.is_well_formed, "size ok?", book.is_size_ok, "ext ok ?", book.is_ext_ok, "file header ok ?", book.is_file_header_ok, 'duplicato ?', book.is_duplicate))
            nodupl_num += 1
        else:
            dupl_num += 1
    print("%s duplicates" % dupl_num)
    print("%s not duplicates" % nodupl_num)
    uploaded = 0
    book_list = [b for b in globals_data.list_of_books if not b.is_duplicate]
    for book in book_list[::-1]:
        if upload_file(book.filename):
            uploaded += 1
    print("%s uploaded" % uploaded)
            

if __name__ == '__main__':
    test(sys.argv)

