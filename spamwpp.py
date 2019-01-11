from selenium import webdriver

# Se de erro... instale o geckodriver, se persistir o erro instale
# o Chrome Driver e mude de Firefox() para Chrome()

driver = webdriver.Firefox() 
driver.get('https://web.whatsapp.com/') 

msg = str(input('ENTER MESSAGE: '))
count = int(input('ENTER TURNS: '))

msg_box = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    btn = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]/button')
    btn.click()
