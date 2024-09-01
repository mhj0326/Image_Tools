###########################################################
#1. DICOM(Digital Imaging and Communication in Medicine)
###########################################################
#in format 'body-003.dcm'

#read image
im = imageio.v2.imread('name_of file.dcm')

#image shape
im.shape

#image datatype
im.dtype

#slicing
im[x:y, z:w]

#image meta
im.meta

#function for reading metadata
def beautify_metadata(metadata):
    print("\nDICOM Metadata:")
    print("-" * 40)
    for key, value in metadata.items():
        print(f"{key}:")
        if isinstance(value, (bytes, bytearray)):
            print("Data ByteArray")
        else:
            print(f"  {value}")
    print("-" * 40)
  
'''
1. TransferSyntaxUID: A unique identifier (UID) that defines the encoding (compression, uncompressed, etc.) used for the DICOM file. 
2. SOPClassUID:A UID that identifies the type of object stored. 
3. SOPInstanceUID: A unique identifier for the specific DICOM object, which uniquely identifies this particular image or dataset.
4. Modality: Indicates the type of equipment that generated the image. 
5. PatientName
6. PatientID
7. StudyInstanceUID: A unique identifier for a specific study.
8. SeriesInstanceUID: A unique identifier for a series within a study. 
9. AcquisitionNumber: The acquisition number represents the order or sequence of the image acquisition. 
10. SamplesPerPixel: Indicates the number of color samples per pixel. A value of 1 suggests that the image is grayscale.
11. Rows: The number of rows (height) in the image. Here, it’s 512 pixels.
12. Columns: The number of columns (width) in the image. Here, it’s 512 pixels.
13. BitsAllocated: The number of bits allocated for each pixel in the image. Here, 8 bits per pixel are allocated.
14. BitsStored: The number of bits actually used to store the pixel data. Here, 8 bits are used.
15. HighBit: Indicates which bit is the most significant bit in the pixel data. Here, 7 means that the most significant bit is the 8th bit (index 7 in 0-based numbering).
16. PixelRepresentation: Indicates whether the pixel data is signed or unsigned. A value of 0 means the pixel data is unsigned.
17. PixelData: Represents the actual image data in the DICOM file. Since it's binary data, it’s often labeled as "Data ByteArray" to indicate it’s not directly human-readable.
18. Shape
19. Sampling: Refers to the physical sampling interval or the pixel spacing, often given in units of millimeters or pixels per millimeter. Here, (1.0, 1.0) suggests that the image has equal sampling in both dimensions.
'''

#plot
import matplotlib.pyplot as plt
plt.imshow(im, cmap = 'gray')
plt.title('DICOM Image')
plt.axis('off')
plt.show()


















