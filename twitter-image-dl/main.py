import scraper
import urlparser
import downloader

def main():
    scraper.scrape()
    urlparser.parse()
    downloader.download()

if __name__ == "__main__":
    main()