from PIL import Image, ExifTags, ImageFont, ImageDraw


def get_exif(im):
    im_exif = im._getexif().items()
    exif = {}
    
    for (tag, value) in im_exif:
        if tag in ExifTags.TAGS:
            exif[ExifTags.TAGS[tag]] = value

    return exif


def get_img_date(im):
    exif = get_exif(im)
    date = exif['DateTime'].split(' ')[0]
    year = str(date[2:4])
    month = str(date[5:7])
    day = str(date[8:10])
    return {'day': day, 'month': month, 'year': year}


def write_on_img(im, text, font, size, position, color):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font, size)
    draw.text(position, text, color, font=font)
    return im


def blank_img(size, color):
    im = Image.new('RGB', size, color)
    return im


def black_img(size):
    color = (0, 0, 0)
    im = blank_img(size, color)
    return im


def brazilian_date_format(date):
    text = date['day'] + ' ' + date['month'] + " '" + date['year']
    return text

def write_date_img_black(im):
    size = im.size
    black_im = black_img(size)
    date = get_img_date(im)
    text = brazilian_date_format(date)
    font_color = (255, 255, 255)
    position = (0, 0)
    write_on_img(black_im, text, 'digital-7.ttf', 50, position, font_color)
    return black_im

