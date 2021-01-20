from bs4 import BeautifulSoup
import requests
import webbrowser


def main():
    
    
    while True:
        URL = 'https://en.wikipedia.org/wiki/Special:Random'
        page = requests.get(URL)
        content = page.content
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find(id='firstHeading').text
        print('Would you like to view the article: ' + title)
        choice = input()
        
        if choice.lower() == 'yes':
                webbrowser.open(page.url)
                break

        elif choice.lower() == "no":
            choice2 = input("Would you like to pick a different random article?")
            if choice2 == "yes":
                continue
            elif choice2 == "no":
                print('Ending program.')
                return False
        else:
            print("Wrong input entered please try again.")
            continue
        
        

   
   





if __name__ == "__main__":
    main()