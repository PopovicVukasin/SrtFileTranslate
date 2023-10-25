import os
from translate import Translator
import srt

translator = Translator(to_lang="sr", from_lang="en")

try:
    original_filename = 'test1.srt'  
    
    with open(original_filename, 'r', encoding='utf-8') as file:
        original_subtitles = list(srt.parse(file))

    translated_subtitles = []
    
    total_subtitles = len(original_subtitles)
    
    for idx, subtitle in enumerate(original_subtitles):
        translated_text = translator.translate(subtitle.content)
        translated_subtitle = srt.Subtitle(subtitle.index, subtitle.start, subtitle.end, translated_text)
        translated_subtitles.append(translated_subtitle)
        
        # Calculate progress
        progress = (idx + 1) / total_subtitles * 100
        print(f"Progress: {progress:.2f}%")

    base_filename = os.path.splitext(original_filename)[0]
    translated_filename = f"{base_filename}_translated.srt"

    with open(translated_filename, 'w', encoding='utf-8') as file:
        file.write(srt.compose(translated_subtitles))

    print(f"Translation completed. Subtitles saved to '{translated_filename}'.")

except Exception as e:
    print("An error occurred:", str(e))
