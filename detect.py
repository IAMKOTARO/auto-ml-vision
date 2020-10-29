import os
import io
import sys

from google.cloud import vision

def detect_document(path):
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


if __name__ == "__main__":
    if len(sys.argv) is not 2:
        print('Error:コマンドライン引数を正しく指定してください。')
        print('フォーマット：python detect.py [path/to/key.json]')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = sys.argv[1] # キーファイルのパス
    path = 'sample.png'
    detect_document(os.path.abspath(path))