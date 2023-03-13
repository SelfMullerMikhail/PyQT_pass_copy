def resizeFunc(event, constSize, sizeW = 1, sizeH = 1):
    sizeW = round(sizeW * (event.size().width() / constSize.width()))
    sizeH = round(sizeH * (event.size().height() / constSize.height()))
    return sizeW, sizeH