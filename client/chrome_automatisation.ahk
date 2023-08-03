
LaunchNightly()
{
    Run "C:\Program Files\Google\Chrome\Application\chrome.exe"
	WinWaitActive("ahk_exe chrome.exe")
	Send "^+c"
	Sleep 1000
	
	Send "https://bg-sillgasse.tsn.at/"
	Send "{Enter}"
	Sleep 10000
	WinWaitActive("ahk_exe chrome.exe")
    Send "^w"
	return
}

Loop 4
{
    LaunchNightly()
    Sleep 100
}
