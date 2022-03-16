from keras.preprocessing.image import ImageDataGenerator

def orthogonal_rot(image):
    return np.rot90(image, np.random.choice([-1, 0, 1]))

datagen = ImageDataGenerator(
        featurewise_center=False, 
        samplewise_center=False,  
        featurewise_std_normalization=False,  
        samplewise_std_normalization=False,  
        zca_whitening=False,  
        preprocessing_function= orthogonal_rot,  
        width_shift_range= 0.1,  
        height_shift_range= 0.1,  
        horizontal_flip = True,  
        vertical_flip=True)  


datagen.fit(x_train)
