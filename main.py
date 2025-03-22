# Simple File Downloader script for python syntax exercise purpose
# Ugur Cengiz <muffinweb>
# ugurcengiz.mail@icloudd.com
import pprint

from Downloaderpy import DownloaderPy

logos = [
    "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
    "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg",
    "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg",
    "https://upload.wikimedia.org/wikipedia/commons/4/44/Facebook_Logo.png",
    "https://upload.wikimedia.org/wikipedia/commons/0/09/YouTube_full-color_icon_%282017%29.svg",
    "https://upload.wikimedia.org/wikipedia/commons/8/83/Telegram_2019_Logo.svg"
]

# Use docs array with extension method in chain to ovveride file extension that you're saving
# docs = [
#    "https://www.kap.org.tr/tr/api/file/download/4028328c950ba8c801956bd352eb267e"
# ]

# Basic Usage of SimpleDownloader

report = (DownloaderPy()
              .setUrls(logos)
              #.extension("pdf")
              .download())

print("success: " + str(report.success))
print("fail: " + str(report.fail))