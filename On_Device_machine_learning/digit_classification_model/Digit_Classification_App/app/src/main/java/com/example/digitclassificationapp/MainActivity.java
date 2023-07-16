package com.example.digitclassificationapp;

import android.content.Intent;
import android.content.res.AssetFileDescriptor;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import org.tensorflow.lite.Interpreter;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;

public class MainActivity extends AppCompatActivity {
    private Interpreter tflite;
    private ImageView imageView;
    private TextView predictionTextView;
    private TextView accuracyTextView;
    private Button chooseImageButton;
    private Button classifyButton;
    private Bitmap image;

    private static final int PICK_IMAGE = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize TensorFlow Lite model
        try {
            tflite = new Interpreter(loadModelFile());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Get references to views
        imageView = findViewById(R.id.image_view);
        predictionTextView = findViewById(R.id.prediction_text_view);
        accuracyTextView = findViewById(R.id.accuracy_text_view);
        chooseImageButton = findViewById(R.id.choose_image_button);
        classifyButton = findViewById(R.id.classify_button);



        // Set up choose image button
        chooseImageButton.setOnClickListener(v -> {
            // Open image picker
            // ...
            Intent intent = new Intent();
            intent.setType("image/*");
            intent.setAction(Intent.ACTION_GET_CONTENT);
            startActivityForResult(Intent.createChooser(intent, "Select Picture"), PICK_IMAGE);
        });

        // Set up classify button
        classifyButton.setOnClickListener(v -> {
            if (image != null) {
                // Preprocess the image
                float[] input = getPreprocessedImage(image);

                // Classify the image
                float[][] output = new float[1][10];
                tflite.run(input, output);

                // Find the class with the highest confidence
                int classIndex = 0;
                float maxConfidence = output[0][0];
                for (int i = 1; i < 10; i++) {
                    if (output[0][i] > maxConfidence) {
                        classIndex = i;
                        maxConfidence = output[0][i];
                    }
                }

                // Display the prediction
                predictionTextView.setText(String.valueOf(classIndex));
                accuracyTextView.setText(String.valueOf(maxConfidence));
            }
        });
    }





    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == PICK_IMAGE && resultCode == RESULT_OK && data != null && data.getData() != null) {
            // Get the image URI
            Uri imageUri = data.getData();

            try {
                // Convert the image URI to a Bitmap
                image = MediaStore.Images.Media.getBitmap(getContentResolver(), imageUri);

                // Display the image
                imageView.setImageBitmap(image);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }



    private float[] getPreprocessedImage(Bitmap image) {
        // Resize the image
        Bitmap resizedImage = Bitmap.createScaledBitmap(image, 28, 28, true);

        // Convert the image to a float array
        int width = resizedImage.getWidth();
        int height = resizedImage.getHeight();
        int[] pixels = new int[width * height];
        resizedImage.getPixels(pixels, 0, width, 0, 0, width, height);

        float[] imageData = new float[pixels.length];
        for (int i = 0; i < pixels.length; i++) {
            imageData[i] = (pixels[i] & 0xff) / 255.0f;
        }

        return imageData;
    }



    private MappedByteBuffer loadModelFile() throws IOException {
        // Open the model file from the assets folder
        AssetFileDescriptor fileDescriptor = getAssets().openFd("digit_classification_model.tflite");
        FileInputStream inputStream = new FileInputStream(fileDescriptor.getFileDescriptor());
        FileChannel fileChannel = inputStream.getChannel();
        return fileChannel.map(FileChannel.MapMode.READ_ONLY, fileDescriptor.getStartOffset(), fileDescriptor.getDeclaredLength());
    }

}
