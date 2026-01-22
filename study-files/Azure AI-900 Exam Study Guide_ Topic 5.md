# Azure AI-900 Exam Study Guide: Topic 5

## Topic 5: Describe Features of Generative AI Workloads on Azure (20–25%)

This topic, the largest section at 20–25% of the exam, focuses on generative AI, which involves creating new content like text, images, or code based on learned patterns. It builds on earlier topics (e.g., NLP from Topic 4 and ML principles from Topic 2) and emphasizes innovation, applications, ethics, and Azure's tools for deployment. Key to acing this is understanding how generative AI differs from analytical AI (creation vs. prediction), common use cases, and responsible practices to mitigate risks like hallucinations. As of May 2025, the exam reflects updates in this fast-evolving area, including Azure's platform for enterprise AI.

Study Tip: Experiment with Azure OpenAI Playground (free tier available) to see generation in action. Link scenarios to responsible AI from Topic 1 (e.g., transparency in outputs). Practice identifying when generative AI is overkill (e.g., vs. simple classification). Review transformer architecture from Topic 2, as it's foundational here.

### 5.1 Identify Features of Generative AI Solutions

Generative AI solutions use models to produce original outputs from inputs like prompts, often leveraging large language models (LLMs) or diffusion models.

#### 5.1.1 Identify Features of Generative AI Models
Generative models learn data distributions to create new instances resembling the training data.

- **Key Features**:
  - Probabilistic generation: Outputs vary based on randomness or temperature settings for creativity.
  - Multimodal: Handles text, images, audio (e.g., text-to-image or code generation).
  - Fine-tuning: Adapt pre-trained models to specific tasks with custom data.
  - Scalability: Requires significant compute; uses techniques like few-shot learning for efficiency.
  
- **Examples**:
  - Large models like GPT for text, DALL-E for images.
  - Features include tokenization (breaking input into units) and attention mechanisms (focusing on relevant parts).

- **Azure Relevance**: Models in Azure OpenAI are based on transformers, supporting features like prompt engineering.

Study Tip: Contrast with discriminative models (e.g., classification from Topic 2)—generative creates, discriminative decides. Remember hallucinations: Models can generate plausible but false info.

#### 5.1.2 Identify Common Scenarios for Generative AI
Generative AI excels in creative, automation, and personalization tasks.

- **Key Scenarios**:
  - Content creation: Writing articles, emails, or marketing copy.
  - Code assistance: Generating or debugging code snippets.
  - Image/video synthesis: Creating visuals from descriptions for design or entertainment.
  - Data augmentation: Generating synthetic data for ML training (e.g., rare medical images).
  - Conversational agents: Advanced chatbots for customer service.
  
- **Examples**:
  - A marketer using AI to brainstorm ad campaigns.
  - Developers auto-completing functions in IDEs.
  - Educators creating personalized learning materials.

- **Azure Relevance**: Integrated in tools like Copilot for everyday scenarios.

Study Tip: Map to workloads—e.g., generative text is an NLP extension; images tie to computer vision. Exam questions may present business problems; select generative if "create new" is the goal.

#### 5.1.3 Identify Responsible AI Considerations for Generative AI
Generative AI amplifies risks, so apply Microsoft's principles with extra focus on outputs.

- **Key Considerations**:
  - Fairness: Avoid biased generations (e.g., stereotypical content); use diverse training data.
  - Reliability/Safety: Mitigate hallucinations or harmful outputs via grounding (fact-checking) and filters.
  - Privacy/Security: Protect input data; prevent leaks in prompts.
  - Inclusiveness: Ensure outputs accessible (e.g., multilingual, disability-friendly).
  - Transparency: Disclose AI-generated content; provide explanations for outputs.
  - Accountability: Log generations for audits; human review for high-stakes uses.
  - Additional: Copyright issues with training data; environmental impact from compute.

- **Examples**:
  - Filtering toxic language in chatbots.
  - Watermarking AI images to prevent misinformation.

- **Azure Relevance**: Azure tools include content safety APIs and monitoring.

Study Tip: Build on Topic 1—generative adds risks like deepfakes. Questions may ask for mitigations, e.g., "How to ensure safety in text generation?" (Answer: Use moderation APIs).

### 5.2 Identify Generative AI Services and Capabilities in Microsoft Azure

Azure provides scalable, secure services for generative AI, from pre-built models to custom development.

#### 5.2.1 Describe Features and Capabilities of Azure AI Foundry
Azure AI Foundry is a unified platform for building, managing, and deploying enterprise AI applications, including agents and models.

- **Key Capabilities**:
  - End-to-end workflow: From data prep to deployment.
  - Agent service: Builds AI agents that connect models, tools, and frameworks.
  - Fine-tuning: Customize models with serverless or managed compute.
  - SDK: Toolchain for app development.
  - Scalability: Handles enterprise operations with governance.

- **Examples**:
  - Creating custom AI agents for business automation.
  - Fine-tuning models for industry-specific jargon.

Study Tip: Think "foundry" as a factory for AI—focus on building/customizing vs. using pre-built.

#### 5.2.2 Describe Features and Capabilities of Azure OpenAI Service
Azure OpenAI Service provides access to OpenAI models like GPT and DALL-E, hosted securely on Azure.

- **Key Capabilities**:
  - Model access: GPT for text, embeddings for search, DALL-E for images.
  - Prompt engineering: Fine-control via system/user messages.
  - Fine-tuning and embeddings: Customize and vectorize data.
  - Security: Enterprise-grade with private networking, content filters.
  - Monitoring: Usage analytics, responsible AI tools.
  - Integration: APIs for apps, Copilot Studio for no-code.

- **Examples**:
  - Building chat apps with GPT-4.
  - Generating images from text prompts.

- **Azure Relevance**: Pay-per-token; Playground for testing.

Study Tip: Core service for generative—emphasize differences from open-source (Azure adds compliance).

#### 5.2.3 Describe Features and Capabilities of Azure AI Foundry Model Catalog
The model catalog in Azure AI Foundry curates and manages models for easy discovery and use.

- **Key Capabilities**:
  - Curated selection: Pre-trained models from Microsoft, partners, open-source.
  - Search/filter: By task, performance, or domain.
  - Deployment: One-click to Azure environments.
  - Governance: Tracks versions, licenses, ethical info.
  - Integration: With fine-tuning and agent services.

- **Examples**:
  - Selecting a vision model for custom apps.
  - Browsing for generative text models.

- **Azure Relevance**: Part of Foundry; accelerates development.

Study Tip: Catalog = "library"—focus on discovery vs. building. May overlap with Hugging Face integration in Azure.

## Additional Resources and Practice
- **Practice Questions**:
  - What feature of generative AI models allows for varied outputs? (Answer: Probabilistic generation or temperature control)
  - Identify a common scenario for generative AI. (Answer: Content creation, like writing emails)
  - Which Azure service provides access to GPT models? (Answer: Azure OpenAI Service)
  - Describe a responsible AI consideration for generative AI. (Answer: Mitigating hallucinations through grounding)
- **Exam Tip**: This section weights heavily—expect scenarios tying to services (e.g., "Use Azure AI Foundry for custom agents"). Review updates from 

This completes the study guide! If you'd like a full compilation, review quizzes, or updates, let me know.