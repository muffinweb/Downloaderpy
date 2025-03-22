import urllib.request
from Report import Report
import os

class DownloaderPy():

    # Urls List
    urls = []

    overrideExtension = None

    def setUrl(self, url):
        self.urls.append(url)

        return self
    def setUrls(self, urls):
        self.urls = urls

        return self

    def download(self):

        # Data folder check
        if not os.path.exists("data/"):
            os.makedirs("data/")

        # Successful Attemps Counter
        successfullAttempts = 0
        failedAttempts = 0

        for url in self.urls:

            try:
                # Response
                response = urllib.request.urlopen(url)

                # Statua Code
                status_code = response.getcode()

                # Download if it returns 200 statuscode, skip if its not 200 instead
                if (status_code == 200):
                    print("----------------------------------------")
                    print('Downloading: ' + self.get_file_name(url))
                    with open("data/" + self.get_file_name(url), 'wb') as f:
                        f.write(response.read())
                        f.close()
                    print('Download finished: ' + self.get_file_name(url))
                    print("----------------------------------------\n")

                    successfullAttempts += 1
                else:
                    print("----------------------------------------")
                    print("Skipped: " + self.get_file_name(url) + " Status: " + str(status_code))
                    print("----------------------------------------")

                    failedAttempts += 1
            except Exception as e:
                print("----------------------------------------")
                print("Skipped: " + self.get_file_name(url) + " Error: " + str(e))
                print("----------------------------------------")

                failedAttempts += 1

        return Report(successfullAttempts, failedAttempts)

    def extension(self, extension):
        self.overrideExtension = extension

        return self

    def get_file_name(self, url):
        # Divide string by / symbol
        segments = url.split('/')

        # Get latest item to catch filename with its extension
        last_segment = segments[-1]

        if(self.overrideExtension != None):
            return last_segment + "." + self.overrideExtension

        # Return
        return last_segment