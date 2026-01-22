# Azure AI-900 Exam Study Guide: Topic 4

## Topic 4: Describe Features of Natural Language Processing (NLP) Workloads on Azure (15–20%)

This topic covers how Azure supports NLP, which enables machines to understand, interpret, and generate human language in text or speech form. It accounts for 15–20% of the exam and emphasizes recognizing NLP scenarios and the corresponding Azure services. To excel, focus on mapping real-world problems to NLP features (e.g., analyzing customer feedback) and understanding service capabilities without needing implementation details. Build on Topic 1's NLP workload overview.

Study Tip: Practice with text examples—e.g., extract entities from a sentence. Use Azure's free tiers for Language and Speech services to test features. Differentiate text-based (Language service) from audio-based (Speech service) tasks. Link to responsible AI, like bias in sentiment analysis.

### 4.1 Identify Features of Common NLP Workload Scenarios

NLP workloads process unstructured language data for insights or actions. Common scenarios include extracting information, analyzing opinions, modeling language, handling speech, and translating.

#### 4.1.1 Identify Features and Uses for Key Phrase Extraction
Key phrase extraction identifies main ideas or topics from text by pulling out significant phrases.

- **Key Features**:
  - Unsupervised: Doesn't require labeled data; uses algorithms to find salient terms.
  - Ranking: Scores phrases by importance.
  - Multi-language support: Works across languages.
  
- **Uses**:
  - Summarizing articles or documents.
  - SEO optimization by identifying keywords in content.
  - Tagging customer support tickets for routing.

- **Azure Relevance**: Part of Azure AI Language for quick text analysis.

Study Tip: Think "summarization in phrases"—e.g., from "The quick brown fox jumps over the lazy dog," extracts "quick brown fox," "lazy dog."

#### 4.1.2 Identify Features and Uses for Entity Recognition
Entity recognition (Named Entity Recognition - NER) detects and categorizes entities like people, places, or organizations in text.

- **Key Features**:
  - Categorization: Labels as person, location, date, etc.
  - Contextual: Considers surrounding words for accuracy.
  - Custom entities: Train for domain-specific ones (e.g., medical terms).
  
- **Uses**:
  - Extracting patient names and conditions from medical notes.
  - Analyzing news for mentioned companies or events.
  - Personalizing responses in chatbots by recognizing user mentions.

- **Azure Relevance**: Azure AI Language supports pre-built and custom NER.

Study Tip: Focus on "who, what, where"—exam may provide text snippets; identify entities.

#### 4.1.3 Identify Features and Uses for Sentiment Analysis
Sentiment analysis determines the emotional tone of text, such as positive, negative, or neutral.

- **Key Features**:
  - Polarity scoring: Rates from -1 (negative) to +1 (positive).
  - Aspect-based: Analyzes sentiment per topic (e.g., food vs. service in reviews).
  - Confidence scores: Indicates analysis certainty.
  
- **Uses**:
  - Monitoring brand reputation on social media.
  - Gauging customer satisfaction from surveys.
  - Prioritizing negative feedback in support systems.

- **Azure Relevance**: Azure AI Language provides sentiment with opinion mining.

Study Tip: Remember cultural nuances can affect accuracy; tie to fairness in responsible AI.

#### 4.1.4 Identify Features and Uses for Language Modeling
Language modeling predicts or generates text based on patterns, often using probabilistic models.

- **Key Features**:
  - Predictive: Suggests next words or completes sentences.
  - Generative: Creates coherent text (links to Topic 5).
  - Fine-tuning: Adapts to specific domains.
  
- **Uses**:
  - Autocomplete in search engines or emails.
  - Chatbots generating responses.
  - Summarizing long texts.

- **Azure Relevance**: Integrated in Azure AI Language; advanced via Azure OpenAI.

Study Tip: Basic models count word probabilities; modern use transformers (from Topic 2).

#### 4.1.5 Identify Features and Uses for Speech Recognition and Synthesis
Speech recognition converts audio to text; synthesis (TTS) turns text to speech.

- **Key Features**:
  - Recognition: Handles accents, noise; real-time or batch.
  - Synthesis: Natural voices, prosody (intonation), custom voices.
  - Multilingual: Supports many languages/dialects.
  
- **Uses**:
  - Transcription of meetings or calls.
  - Voice assistants like dictation tools.
  - Accessibility for reading text aloud.

- **Azure Relevance**: Azure AI Speech handles both.

Study Tip: Recognition = audio to text; Synthesis = text to audio. Note privacy for voice data.

#### 4.1.6 Identify Features and Uses for Translation
Translation converts text or speech from one language to another.

- **Key Features**:
  - Neural machine translation: Context-aware for natural results.
  - Custom models: Train for industry jargon.
  - Real-time: For live conversations.
  
- **Uses**:
  - Globalizing websites or apps.
  - Subtitling videos in multiple languages.
  - Multilingual customer support.

- **Azure Relevance**: Azure AI Translator (part of Language/Speech services).

Study Tip: Emphasize accuracy improvements with neural nets; potential for cultural mistranslations.

### 4.2 Identify Azure Tools and Services for NLP Workloads

Azure offers integrated, scalable services for NLP, often no-code via studios.

#### 4.2.1 Describe Capabilities of the Azure AI Language Service
Azure AI Language provides text analysis tools in one service.

- **Key Capabilities**:
  - Unified API: For entity recognition, sentiment, key phrases, summarization.
  - Custom features: Train models for NER or classification.
  - Conversation analysis: For dialogs (e.g., intent recognition).
  - Integration: With Azure Bot Service or Power Virtual Agents.
  - Responsible AI: Built-in content filters.

- **Examples**:
  - Analyzing emails for urgency via sentiment and entities.
  - Building Q&A systems with language understanding.

- **Azure Relevance**: Pay-per-use; Language Studio for no-code testing.

Study Tip: It's the core for text NLP—contrast with Vision for images.

#### 4.2.2 Describe Capabilities of the Azure AI Speech Service
Azure AI Speech handles audio-language tasks.

- **Key Capabilities**:
  - Speech-to-text: Custom acoustic/language models.
  - Text-to-speech: Neural voices, SSML for customization.
  - Translation: Real-time speech translation.
  - Speaker recognition: Identifies voices.
  - SDKs: For apps on devices or cloud.

- **Examples**:
  - Live captioning in meetings.
  - Creating audiobooks from text.

- **Azure Relevance**: Integrates with Language for hybrid tasks; supports 100+ languages.

Study Tip: Focus on audio; exam may ask for scenarios like call center transcription.

## Additional Resources and Practice
- **Practice Questions**:
  - Which NLP feature identifies opinions in reviews? (Answer: Sentiment Analysis)
  - What Azure service transcribes audio meetings? (Answer: Azure AI Speech – Speech-to-Text)
  - Describe a use for entity recognition. (Answer: Extracting names and locations from news articles)
- **Exam Tip**: Scenarios often combine features (e.g., sentiment + translation). Relate to ML concepts from Topic 2, like classification in sentiment.

Let me know if you'd like more details, examples, or to proceed to Topic 5!