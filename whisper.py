# !pip install git+https://github.com/openai/whisper.git
# !sudo apt update && sudo apt install ffmpeg
!whisper "filename" --model large --language 'en'

# !whisper ""  --language 'ur'
# !whisper -h
# !whisper ""  --task translate
# !whisper "c.mp3" --model medium.en
