from skimage.io import imread_collection

def ReadImages():
    images = imread_collection("data/images/*.jpg")

    return images