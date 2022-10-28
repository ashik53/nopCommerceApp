pytest -s -v -m "sanity" --html=./Reports/report_chrome.html  "D:\Python_Selenium\nopCommerceApp\testCases" --browser chrome
rem pytest -s -v -m "sanity or regression" --browser chrome
rem pytest -s -v -m "sanity and regression"  --browser chrome
rem  pytest -s -v -m "regression"  --browser chrome

pytest -s -v -m "sanity" --html=./Reports/report_firefox.html  "D:\Python_Selenium\nopCommerceApp\testCases" --browser firefox
rem pytest -s -v -m "sanity or regression" --browser firefox
rem pytest -s -v -m "sanity and regression"  --browser firefox
rem  pytest -s -v -m "regression"  --browser firefox