# Azure AI-900 Exam Study Guide: Topic 1

## Topic 1: Describe Artificial Intelligence Workloads and Considerations (15–20%)

This topic focuses on understanding common AI workloads and the principles of responsible AI. It accounts for 15–20% of the exam questions. You'll need to recognize different types of AI applications and emphasize ethical considerations in AI development and deployment. Key to acing this section is differentiating between workload types with real-world examples and grasping how responsible AI principles mitigate risks.

Study Tip: Review real-world AI use cases (e.g., from Microsoft case studies) and memorize the six responsible AI principles. Practice by identifying which principle applies to scenarios like bias in hiring algorithms.

### 1.1 Identify Features of Common AI Workloads

AI workloads refer to tasks or applications where AI technologies process data to generate insights, predictions, or actions. Common workloads include computer vision, natural language processing (NLP), document processing, and generative AI. Features typically involve data input (e.g., images, text), processing via models, and outputs like classifications or generated content.

#### 1.1.1 Identify Computer Vision Workloads
Computer vision enables machines to interpret and understand visual information from the world, similar to human sight.

- **Key Features**:
  - Image analysis: Detecting, classifying, or segmenting objects in images or videos.
  - Real-time processing: Often used for video streams or live feeds.
  - Integration with sensors: Common in IoT devices like cameras.
  
- **Examples**:
  - Autonomous vehicles detecting road signs.
  - Medical imaging identifying tumors in X-rays.
  - Retail systems for inventory management via shelf scanning.

- **Azure Relevance**: Services like Azure AI Vision handle these tasks.

Study Tip: Remember that computer vision deals with pixels and patterns, not text or audio.

#### 1.1.2 Identify Natural Language Processing Workloads
NLP allows machines to understand, interpret, and generate human language.

- **Key Features**:
  - Text analysis: Extracting meaning, sentiment, or entities from text.
  - Language generation: Creating responses or summaries.
  - Multilingual support: Handling translation and dialect variations.
  
- **Examples**:
  - Chatbots answering customer queries.
  - Sentiment analysis on social media posts.
  - Virtual assistants like Cortana processing voice commands.

- **Azure Relevance**: Azure AI Language service supports NLP tasks.

Study Tip: NLP workloads often involve unstructured text data; contrast this with structured data in databases.

#### 1.1.3 Identify Document Processing Workloads
Document processing involves extracting and analyzing information from documents, forms, or unstructured files.

- **Key Features**:
  - Optical Character Recognition (OCR): Converting scanned images to editable text.
  - Form recognition: Identifying fields like names, dates, or signatures.
  - Intelligent extraction: Pulling key data points automatically.
  
- **Examples**:
  - Automating invoice processing in finance.
  - Extracting patient info from medical forms.
  - Legal document review for contract clauses.

- **Azure Relevance**: Azure AI Document Intelligence (formerly Form Recognizer) is key here.

Study Tip: This workload bridges computer vision (for scanning) and NLP (for understanding content).

#### 1.1.4 Identify Features of Generative AI Workloads
Generative AI creates new content, such as text, images, or code, based on patterns learned from data.

- **Key Features**:
  - Content creation: Generating novel outputs from prompts.
  - Creativity and variation: Producing multiple versions or styles.
  - Foundation models: Often based on large pre-trained models like GPT.
  
- **Examples**:
  - Writing articles or code snippets.
  - Creating images from descriptions (e.g., DALL-E).
  - Music composition or video generation.

- **Azure Relevance**: Azure OpenAI Service enables generative tasks.

Study Tip: Focus on the "generative" aspect—it's about creation, not just analysis. Be aware of ethical concerns like misinformation.

### 1.2 Identify Guiding Principles for Responsible AI

Microsoft's responsible AI framework includes six principles to ensure AI is ethical, trustworthy, and beneficial. These guide development to avoid harm and build user trust.

#### 1.2.1 Describe Considerations for Fairness in an AI Solution
Fairness ensures AI treats all individuals and groups equitably, avoiding bias.

- **Key Considerations**:
  - Bias detection: Test for disparities in outcomes across demographics (e.g., gender, race).
  - Diverse datasets: Use inclusive training data to prevent skewed results.
  - Mitigation tools: Apply techniques like reweighting data or using fairness-aware algorithms.
  
- **Example Scenario**: An AI hiring tool that disadvantages certain ethnic groups due to biased historical data—mitigate by auditing and retraining.

Study Tip: Link to real issues like facial recognition biases; exam questions may ask for mitigation strategies.

#### 1.2.2 Describe Considerations for Reliability and Safety in an AI Solution
Reliability ensures AI performs consistently and safely, minimizing errors or failures.

- **Key Considerations**:
  - Robust testing: Validate across edge cases and adversarial inputs.
  - Fail-safes: Implement backups or human oversight for critical systems.
  - Performance metrics: Monitor accuracy, precision, and recall.
  
- **Example Scenario**: Self-driving cars must reliably detect obstacles in bad weather to ensure safety.

Study Tip: Think "dependability"—questions might involve scenarios where AI failure could cause harm.

#### 1.2.3 Describe Considerations for Privacy and Security in an AI Solution
Privacy protects user data, while security safeguards against threats.

- **Key Considerations**:
  - Data minimization: Collect only necessary data.
  - Encryption and access controls: Use Azure features like role-based access.
  - Compliance: Adhere to regulations like GDPR.
  
- **Example Scenario**: An AI health app must anonymize patient data to prevent breaches.

Study Tip: Differentiate privacy (user rights) from security (system protection); cite Azure Key Vault for security.

#### 1.2.4 Describe Considerations for Inclusiveness in an AI Solution
Inclusiveness ensures AI benefits diverse users, including those with disabilities or from underrepresented groups.

- **Key Considerations**:
  - Accessibility features: Support for screen readers or multiple languages.
  - User-centered design: Involve diverse stakeholders in development.
  - Broad testing: Evaluate across abilities and cultures.
  
- **Example Scenario**: Voice AI that recognizes accents from various regions to avoid excluding users.

Study Tip: Connect to fairness but focus on access and empowerment.

#### 1.2.5 Describe Considerations for Transparency in an AI Solution
Transparency explains how AI works, building trust through openness.

- **Key Considerations**:
  - Explainable AI (XAI): Provide interpretable models or decision rationales.
  - Documentation: Share data sources and algorithms.
  - User notifications: Inform when AI is in use.
  
- **Example Scenario**: A loan approval AI that explains rejection reasons to applicants.

Study Tip: Remember "black box" issues—transparency counters opacity.

#### 1.2.6 Describe Considerations for Accountability in an AI Solution
Accountability assigns responsibility for AI outcomes to humans or organizations.

- **Key Considerations**:
  - Governance frameworks: Establish policies and audits.
  - Traceability: Log decisions for review.
  - Ethical reviews: Conduct impact assessments.
  
- **Example Scenario**: Holding a company accountable for AI-generated harmful content.

Study Tip: This principle ties all others together; questions may involve who is responsible in a failure.

## Additional Resources and Practice
- **Practice Questions**:
  - What AI workload would you use to analyze customer reviews for emotions? (Answer: NLP – Sentiment Analysis)
  - Which responsible AI principle addresses bias in datasets? (Answer: Fairness)
- **Exam Tip**: Expect scenario-based questions; apply principles to cases like healthcare or finance.

Let me know if you'd like to expand on examples, add diagrams, or move to the next topic!