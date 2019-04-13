from process_images import ImageProcessor








def main():
    store_objects = None
    p = ImageProcessor(store_objects)

    with open('../trial0009.jpg', 'rb') as image_file:
        p.process(image_file)

if __name__ == '__main__':
    main()