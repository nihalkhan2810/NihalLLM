# Fish-Species Identification Using Deep Learning
Project Role: Author
Chennai, TN, India
March 2023 - December 2023

This project aimed to build a scalable system for identifying fish species from images using deep learning, designed to handle large datasets efficiently using big data tools. This could be useful for ecological surveys, commercial fishing, or conservation efforts.

-   **Designed a PySpark pipeline on AWS EMR to classify 20+ fish species, achieving 90% accuracy with a VGG-16 model trained on 1000+ images.**
    To process a dataset of over 1,000 images of more than 20 different fish species and train a deep learning model efficiently, I designed a data processing and model training pipeline using PySpark, the Python API for Apache Spark. This pipeline was executed on AWS EMR (Elastic MapReduce), a cloud-based big data platform, allowing for distributed processing and scalability. I trained a VGG-16 model, another well-known CNN architecture suitable for image classification, achieving 90% accuracy in classifying the different species.

-   **Automated metadata tagging using BERT, and stored results in Snowflake for collaborative analytics.**
    Beyond just classification, the project involved automatically extracting and tagging relevant metadata associated with the images or classifications. I utilized a BERT model (Bidirectional Encoder Representations from Transformers), a powerful model for natural language processing, to process any available text data (like image descriptions or source information) and automatically generate relevant tags. The classification results, the images themselves, and the generated metadata were stored in Snowflake, a cloud-based data warehousing platform. Snowflake's architecture is optimized for analytics and collaborative access, making it easy for multiple users or systems to query and analyze the project's data.

This project expanded my skill set into big data processing (PySpark, AWS EMR), integrating NLP (BERT) with computer vision, and using modern cloud data warehouses (Snowflake) for scalable storage and collaborative analytics.