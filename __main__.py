'''
Goals for tonight:
#1 get photo from folder
#2 get data from photo (smile or not, eye contact or not)
#3

'''
from photo import analyzePhoto, deleteFile, getFiles, analyzeAllPhotos
from audio import analyzeAudio, analyzeAllAudio

#make class having folder name ? triv
#deleteFile('new-hack-valley', 'bad_example.jpg')

photoBucket = 'hack-the-valley-photo'
audioBucket = 'hack-the-valley-audio'

analyzeAllPhotos(photoBucket)
#analyzeAllAudio(audioBucket)

