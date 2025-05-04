# Professional Experience

## Sathyabama Institute
Research Assistant
Chennai, TN, India
December 2021 - January 2023

As a Research Assistant, I worked under a professor on applied AI projects for various clients, often related to medical or biological data analysis. My role involved designing and implementing machine learning pipelines, automating data processing workflows, and contributing to the full lifecycle of AI-driven solutions from experimentation to deployment considerations.

-   **Built a CNN-based pipeline in Pytorch for larvae identification, achieving an F1-score of 0.92 by fine-tuning pre-trained ResNet-34 models and integrating LLM-generated explanations for misclassification analysis.**
    For this project, I developed a complete image classification pipeline. I chose PyTorch for its flexibility in deep learning research. I fine-tuned a ResNet-34 model, which is a widely used convolutional neural network architecture known for its balance of depth and performance, on a specific dataset of larvae images. To provide more than just a classification label, I integrated a component that used an LLM to generate natural language explanations for *why* a particular image might have been misclassified, aiming to provide helpful insights for domain experts (like biologists) analyzing the results. Achieved a strong F1-score of 0.92, indicating high accuracy and precision for this task.

-   **Automated image preprocessing workflows using OpenCv and Kubernetes, reducing inference latency from 200ms to 140ms for real-time edge deployments.**
    To prepare images for the CNN model efficiently, especially for scenarios where the model would be deployed on edge devices with limited resources and requiring fast responses (real-time inference), I automated the preprocessing steps. This involved using OpenCV, a powerful computer vision library, to handle tasks like resizing, normalization, and basic image enhancements. I containerized these preprocessing steps and orchestrated them using Kubernetes, which allowed for scalable and efficient execution of these workflows. By optimizing the processing steps and leveraging containerization, I successfully reduced the end-to-end inference latency from 200 milliseconds to 140 milliseconds, a critical improvement for real-time applications.

-   **Stored preprocessed data in AWS S3, achieving 99.8% uptime and reducing storage costs by 18% using parquet compression.**
    Handling potentially large datasets of images required a robust and scalable storage solution. I utilized AWS S3, Amazon's cloud object storage service, known for its durability and high availability, to store the preprocessed image data. To ensure data was readily available for the pipeline, I focused on configuring access for high uptime. Furthermore, to manage storage costs effectively and improve data retrieval performance for subsequent processing steps, I implemented data serialization using the Parquet format. Parquet is a columnar storage file format that is highly efficient for compression and querying structured data, which resulted in an 18% reduction in storage costs compared to standard formats.

This role provided invaluable experience in applying deep learning and MLOps principles in a professional research context, working with real-world data and focusing on practical outcomes like performance optimization and cost efficiency.