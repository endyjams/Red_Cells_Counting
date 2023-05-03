from skimage.io import imread_collection

def ReadImages():
    images = imread_collection("archive/images/*.png")

    return images