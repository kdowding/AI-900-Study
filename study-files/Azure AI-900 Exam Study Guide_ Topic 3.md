# Azure AI-900 Exam Study Guide: Topic 3

## Topic 3: Describe Features of Computer Vision Workloads on Azure (15–20%)

This topic explores how Azure handles computer vision tasks, which involve AI interpreting visual data like images and videos. It makes up 15–20% of the exam and focuses on recognizing solution types and Azure services. Success here requires understanding how vision AI extracts insights from visuals (e.g., identifying objects) and mapping scenarios to Azure tools. No deep technical knowledge is needed, but familiarize yourself with service capabilities and limitations.

Study Tip: Visualize use cases—think of everyday apps like photo tagging or security cameras. Use Azure's free tier to test services like AI Vision. Practice distinguishing between classification (labeling whole images) and detection (locating specific objects). Review demos on Microsoft Learn for hands-on feel without coding.

### 3.1 Identify Common Types of Computer Vision Solution

Computer vision solutions process visual data to derive meaning, mimicking human vision. Common types include classification, detection, OCR, and facial analysis, each suited to different scenarios.

#### 3.1.1 Identify Features of Image Classification Solutions
Image classification assigns labels or categories to an entire image based on its content.

- **Key Features**:
  - Multi-class or multi-label: Can assign one or multiple tags (e.g., "dog" and "outdoors").
  - Probability scores: Outputs confidence levels for each label.
  - Pre-trained models: Often use transfer learning for efficiency.
  
- **Examples**:
  - Tagging photos in social media (e.g., classifying as "beach" or "cityscape").
  - Quality control in manufacturing (e.g., identifying defective products).
  - Wildlife monitoring (e.g., classifying animal species from camera traps).

- **Azure Relevance**: Azure AI Vision supports custom or pre-built classification models.

Study Tip: Focus on "whole image" labeling—contrast with object detection, which pinpoints locations.

#### 3.1.2 Identify Features of Object Detection Solutions
Object detection identifies and locates multiple objects within an image or video, drawing bounding boxes around them.

- **Key Features**:
  - Localization: Provides coordinates (e.g., bounding boxes or polygons).
  - Multi-object support: Detects several instances in one frame.
  - Real-time capability: Suitable for video streams.
  
- **Examples**:
  - Autonomous vehicles spotting pedestrians or vehicles.
  - Retail shelf analysis counting stock items.
  - Security systems detecting unauthorized intrusions.

- **Azure Relevance**: Azure AI Vision's object detection analyzes images/videos for common or custom objects.

Study Tip: Remember "where and what"—includes position data. Exam questions may ask for scenarios needing bounding boxes.

#### 3.1.3 Identify Features of Optical Character Recognition Solutions
OCR extracts text from images, converting it to machine-readable format.

- **Key Features**:
  - Text detection and recognition: Locates and reads text in various fonts/languages.
  - Handwriting support: Handles printed or cursive text.
  - Layout preservation: Maintains structure like tables or paragraphs.
  
- **Examples**:
  - Digitizing scanned documents or books.
  - License plate recognition in parking systems.
  - Extracting text from product labels in inventory.

- **Azure Relevance**: Integrated in Azure AI Vision for reading text in images.

Study Tip: OCR bridges vision and NLP—focus on "text from visuals." Note limitations like poor image quality affecting accuracy.

#### 3.1.4 Identify Features of Facial Detection and Facial Analysis Solutions
Facial solutions detect faces and analyze attributes like emotions or demographics.

- **Key Features**:
  - Detection: Locates faces in images/videos.
  - Analysis: Infers age, gender, emotions, or landmarks (e.g., eyes, nose).
  - Recognition: Matches faces to known identities (with consent).
  
- **Examples**:
  - Attendance systems using face recognition.
  - Sentiment analysis from customer reactions in videos.
  - Accessibility tools describing faces for visually impaired users.

- **Azure Relevance**: Azure AI Face service handles detection and analysis ethically.

Study Tip: Emphasize responsible AI—privacy concerns are key; questions may link to fairness/privacy principles from Topic 1.

### 3.2 Identify Azure Tools and Services for Computer Vision Tasks

Azure provides no-code/low-code services for vision workloads, scalable via cloud.

#### 3.2.1 Describe Capabilities of the Azure AI Vision Service
Azure AI Vision (formerly Computer Vision) analyzes images/videos for insights.

- **Key Capabilities**:
  - Image analysis: Describes content, tags, detects objects/brands.
  - OCR: Reads text in 100+ languages.
  - Spatial analysis: Tracks people/objects in videos (e.g., for retail analytics).
  - Custom models: Train with your data via Vision Studio.
  - Integration: APIs for apps, supports batch processing.

- **Examples**:
  - Generating image captions for accessibility.
  - Moderating content by detecting inappropriate visuals.

- **Azure Relevance**: Part of Azure AI services; pay-per-transaction, integrates with Power Apps or Logic Apps.

Study Tip: It's the go-to for general vision—remember features like "smart cropping" for thumbnails. Free tier available for practice.

#### 3.2.2 Describe Capabilities of the Azure AI Face Detection Service
Azure AI Face focuses on face-related tasks with built-in responsibility.

- **Key Capabilities**:
  - Detection: Finds faces and returns attributes (e.g., pose, occlusion).
  - Verification/Identification: Compares faces (1:1 or 1:many matching).
  - Grouping: Clusters similar faces.
  - Limited use policy: Requires approval for sensitive scenarios to ensure ethics.
  - Liveness detection: Prevents spoofing with photos.

- **Examples**:
  - Secure access control in buildings.
  - Personalizing experiences in apps (e.g., age-appropriate content).

- **Azure Relevance**: Standalone service; emphasizes privacy with data not stored by default.

Study Tip: Differentiate from Vision service—Face is specialized. Note deprecation risks or policy changes; link to responsible AI.

## Additional Resources and Practice
- **Practice Questions**:
  - Which computer vision type would locate and box cars in a traffic photo? (Answer: Object Detection)
  - What Azure service extracts text from receipts? (Answer: Azure AI Vision – OCR)
  - Describe a feature of Azure AI Face for security. (Answer: Liveness detection to verify real users)
- **Exam Tip**: Expect diagrams or scenarios—identify the right service. Tie back to workloads from Topic 1 (e.g., computer vision as an AI workload).

Let me know if you'd like deeper examples, code snippets (though not required for AI-900), or to move to Topic 4!