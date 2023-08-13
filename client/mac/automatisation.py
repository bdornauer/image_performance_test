import automate_chrome
import automate_opera
import automate_firefox
import automate_edge
import automate_safari
import requests
import time

def mix_images_backend():
    url = "http://192.168.1.145:8080/mix"
    response = requests.get(url)
    print(response.text)

def change_format_background(format):
    url =  "http://192.168.1.145:8080/change_image_format"
    response = requests.post(url, data={'image_format': format})
    print(response.text)


if __name__ == '__main__':
    chrome_controller = automate_chrome.ChromeAutomation()
    opera_controller = automate_opera.OperaAutomation()
    firefox_controller = automate_firefox.FirefoxAutomation()
    edge_controller = automate_edge.EdgeAutomation()
    safari_controller = automate_safari.SafariAutomation()

    image_formats = ["png", "jpeg",  "avif", "webp"]

    for i in  range(0, 200):
        for image_format in image_formats:
            change_format_background(image_format)
            time.sleep(5)
            chrome_controller.complet_run()
            opera_controller.complet_run()
            firefox_controller.complet_run()
            edge_controller.complet_run()
            safari_controller.complet_run()
        mix_images_backend()
        time.sleep(5)