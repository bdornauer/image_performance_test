import automate_chrome
import automate_opera
import automate_firefox
import automate_edge
import automate_brave

if __name__ == '__main__':
    chrome_controller = automate_chrome.ChromeAutomation()
    opera_controller = automate_opera.OperaAutomation()
    firefox_controller = automate_firefox.FirefoxAutomation()
    edge_controller = automate_edge.EdgeAutomation()
    brave_controller = automate_brave.BraveAutomation()


    for i in range(0, 1):
        print("iteration: ", i)
        #opera_controller.complet_run()
        chrome_controller.complet_run()
        #firefox_conrchrome.exe ßßincognito
        # troller.complet_run()
        #edge_controller.complet_run()
        #brave_controller.complet_run()