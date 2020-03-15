import naver
import time

if __name__ == "__main__":
    naver = naver.Naver('', '')
    try:
        naver.clipboard_login("id", "pwd")
    finally:
        time.sleep(5)
        naver.driver.quit()
