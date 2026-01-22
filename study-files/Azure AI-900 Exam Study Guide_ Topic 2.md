# Azure AI-900 Exam Study Guide: Topic 2

## Topic 2: Describe Fundamental Principles of Machine Learning on Azure (15–20%)

This topic dives into the basics of machine learning (ML), including techniques, core concepts, and Azure-specific capabilities. It represents 15–20% of the exam and builds foundational knowledge for understanding how ML works and how Azure supports it. Key to success here is distinguishing between ML types with scenarios, grasping data roles in training, and knowing Azure ML tools for automation and deployment. This section assumes no prior coding experience but emphasizes conceptual understanding.

Study Tip: Use diagrams to visualize ML workflows (e.g., training vs. validation data). Practice by mapping real-world problems to ML techniques, like predicting house prices (regression) vs. spam detection (classification). Review Azure ML Studio interfaces via free trials to familiarize yourself with capabilities.

### 2.1 Identify Common Machine Learning Techniques

Machine learning involves algorithms that learn patterns from data to make predictions or decisions without explicit programming. Common techniques fall into supervised (labeled data), unsupervised (unlabeled data), and advanced categories like deep learning.

#### 2.1.1 Identify Regression Machine Learning Scenarios
Regression predicts continuous numerical values based on input features.

- **Key Features**:
  - Output: Numeric (e.g., price, temperature).
  - Algorithms: Linear regression, decision trees, neural networks.
  - Evaluation: Metrics like Mean Absolute Error (MAE) or R-squared.
  
- **Examples**:
  - Predicting house prices based on size, location, and age.
  - Forecasting sales revenue from historical data and market trends.
  - Estimating fuel efficiency of cars from engine specs.

- **Azure Relevance**: Azure ML supports regression via automated ML for quick model building.

Study Tip: Remember "continuous output"—if the answer is a number on a scale, it's likely regression. Contrast with classification's categorical outputs.

#### 2.1.2 Identify Classification Machine Learning Scenarios
Classification assigns data to discrete categories or labels.

- **Key Features**:
  - Output: Categorical (e.g., yes/no, spam/ham).
  - Types: Binary (two classes) or multi-class (multiple classes).
  - Algorithms: Logistic regression, support vector machines (SVM), random forests.
  - Evaluation: Accuracy, precision, recall, F1-score.
  
- **Examples**:
  - Email spam detection (spam or not spam).
  - Diagnosing diseases from symptoms (e.g., benign or malignant tumor).
  - Customer churn prediction (will leave or stay).

- **Azure Relevance**: Use Azure ML for classification tasks in automated pipelines.

Study Tip: Think "labels or categories"—exam questions often present scenarios; identify if the goal is grouping into buckets.

#### 2.1.3 Identify Clustering Machine Learning Scenarios
Clustering groups similar data points without predefined labels (unsupervised learning).

- **Key Features**:
  - Output: Clusters or groups based on similarity.
  - Algorithms: K-means, hierarchical clustering, DBSCAN.
  - Evaluation: Silhouette score or intra-cluster distance.
  
- **Examples**:
  - Customer segmentation for marketing (e.g., grouping by buying habits).
  - Anomaly detection in fraud (identifying unusual patterns).
  - Organizing documents by topics without prior categories.

- **Azure Relevance**: Azure ML integrates clustering in data exploration workflows.

Study Tip: Key word: "unsupervised"—no labels; focus on discovering hidden patterns. Differentiate from classification by lack of training labels.

#### 2.1.4 Identify Features of Deep Learning Techniques
Deep learning uses neural networks with multiple layers to model complex patterns.

- **Key Features**:
  - Layered architecture: Input, hidden, output layers.
  - Handles large data: Excels with big datasets and high-dimensional inputs like images.
  - Automatic feature extraction: Learns representations without manual engineering.
  - Algorithms: Convolutional Neural Networks (CNNs) for images, Recurrent Neural Networks (RNNs) for sequences.
  
- **Examples**:
  - Image recognition in self-driving cars.
  - Voice assistants processing speech.
  - Predictive text in keyboards.

- **Azure Relevance**: Azure ML supports deep learning via integration with frameworks like TensorFlow or PyTorch.

Study Tip: Deep learning is a subset of ML; emphasize "neural networks" and "big data needs." Note computational intensity—requires GPUs.

#### 2.1.5 Identify Features of the Transformer Architecture
Transformers are a deep learning model architecture for handling sequential data, revolutionary in NLP and beyond.

- **Key Features**:
  - Attention mechanism: Focuses on relevant parts of input (self-attention).
  - Parallel processing: Faster training than RNNs by handling sequences in parallel.
  - Encoder-decoder structure: Encoders process inputs; decoders generate outputs.
  - Scalability: Powers large models like GPT or BERT.
  
- **Examples**:
  - Machine translation (e.g., Google Translate).
  - Text generation in chatbots.
  - Image processing in vision transformers (ViT).

- **Azure Relevance**: Used in Azure OpenAI Service for generative models.

Study Tip: Remember "attention is all you need" paper; transformers excel in sequences. Exam may ask to identify vs. traditional RNNs (no recurrence).

### 2.2 Describe Core Machine Learning Concepts

These are foundational ideas in ML workflows, focusing on data preparation and model training.

#### 2.2.1 Identify Features and Labels in a Dataset for Machine Learning
Datasets consist of features (inputs) and labels (outputs) in supervised learning.

- **Key Concepts**:
  - Features: Independent variables (e.g., age, income in a salary prediction dataset).
  - Labels: Dependent variable or target (e.g., salary).
  - Data types: Numerical, categorical, text; preprocessing like normalization is key.
  
- **Examples**:
  - In iris flower classification: Features = petal length, width; Label = species.
  - Unsupervised: Only features, no labels (e.g., customer data for clustering).

- **Azure Relevance**: Azure ML datasets allow uploading and labeling data easily.

Study Tip: Features are "what you know," labels are "what you predict." Practice spotting them in sample datasets.

#### 2.2.2 Describe How Training and Validation Datasets Are Used in Machine Learning
Training data teaches the model; validation assesses performance to avoid overfitting.

- **Key Concepts**:
  - Training set: Used to fit the model (e.g., 70-80% of data).
  - Validation set: Evaluates during training to tune hyperparameters.
  - Test set: Final unbiased evaluation (held out).
  - Overfitting: Model memorizes training data but fails on new data; validation helps detect.
  
- **Examples**:
  - Split a 10,000-row dataset: 7,000 training, 1,500 validation, 1,500 test.
  - Cross-validation: Rotate subsets for robust evaluation.

- **Azure Relevance**: Azure ML automates data splitting in experiments.

Study Tip: Workflow: Train → Validate (tune) → Test (final check). Diagram this process for memory.

### 2.3 Describe Azure Machine Learning Capabilities

Azure ML is a cloud-based platform for building, training, and deploying ML models.

#### 2.3.1 Describe Capabilities of Automated Machine Learning
AutoML automates model selection, hyperparameter tuning, and feature engineering.

- **Key Capabilities**:
  - No-code/low-code: Ideal for beginners.
  - Supports classification, regression, forecasting.
  - Leaderboards: Ranks models by performance.
  - Explanations: Provides model interpretability.
  
- **Examples**:
  - Quickly building a churn prediction model without manual coding.

- **Azure Relevance**: Azure ML's AutoML UI runs experiments automatically.

Study Tip: AutoML democratizes ML—focus on "automation" for non-experts.

#### 2.3.2 Describe Data and Compute Services for Data Science and Machine Learning
These services handle storage, processing, and computation.

- **Key Capabilities**:
  - Data: Azure Blob Storage, Data Lake, SQL Database for datasets.
  - Compute: Azure ML Compute Instances (VMs), Compute Clusters (scalable), Inference Clusters.
  - Integration: With Azure Synapse for big data analytics.
  
- **Examples**:
  - Storing large datasets in Blob Storage for ML training.
  - Using GPU clusters for deep learning.

- **Azure Relevance**: Pay-as-you-go; scales for big jobs.

Study Tip: Data = storage/ingestion; Compute = processing power. Know when to use clusters vs. instances (interactive vs. batch).

#### 2.3.3 Describe Model Management and Deployment Capabilities in Azure Machine Learning
Manage models post-training for production.

- **Key Capabilities**:
  - Registry: Store and version models.
  - Endpoints: Deploy as web services (real-time or batch).
  - Monitoring: Track performance with Azure Monitor.
  - Pipelines: Automate workflows from data to deployment.
  
- **Examples**:
  - Deploying a model as an API for app integration.
  - A/B testing models in production.

- **Azure Relevance**: Integrates with Azure Kubernetes Service (AKS) for scaling.

Study Tip: Lifecycle: Train → Register → Deploy → Monitor. Emphasize MLOps for continuous integration.

## Additional Resources and Practice
- **Practice Questions**:
  - Which ML technique predicts a continuous value like temperature? (Answer: Regression)
  - What is the role of validation data? (Answer: To tune the model and prevent overfitting during training)
  - Name an Azure service for scalable ML training. (Answer: Azure ML Compute Clusters)
- **Exam Tip**: Scenarios dominate—apply concepts to business problems. Use free Azure credits to experiment with ML Studio.
