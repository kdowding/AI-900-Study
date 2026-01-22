from flask import Flask, render_template, session, request, redirect, url_for, jsonify
import json
import os
import re
from datetime import datetime, timedelta
import random
import markdown

app = Flask(__name__)
app.secret_key = 'ai900-study-app-secret-key'

# Custom markdown filter
@app.template_filter('markdown')
def markdown_filter(text):
    if text:
        return markdown.markdown(text, extensions=['extra', 'codehilite'])
    return text

class StudyContentParser:
    def __init__(self):
        self.topics = {}
        self.practice_quiz = {}
        self.key_essentials = {}
        self.outline = {}
        self.flashcards = {}

    def parse_all_content(self):
        """Parse all study materials into structured format"""
        try:
            # Parse outline
            self.outline = self.parse_outline()
            
            # Parse each topic
            for i in range(1, 6):
                self.topics[f"topic_{i}"] = self.parse_topic(i)
                
            # Parse key essentials
            self.key_essentials = self.parse_key_essentials()
            
            # Parse practice quiz
            self.practice_quiz = self.parse_practice_quiz()

            # Generate flashcards from content
            self.flashcards = self.generate_flashcards()

            return True
        except Exception as e:
            print(f"Error parsing content: {e}")
            return False
    
    def parse_outline(self):
        """Parse the study guide outline"""
        try:
            with open('study-files/Azure AI-900 Exam Study Guide Outline.md', 'r', encoding='utf-8') as f:
                content = f.read()
            
            outline = {
                'title': 'Azure AI-900 Exam Study Guide Outline',
                'topics': []
            }
            
            # Extract topic sections
            topic_pattern = r'## (\d+)\.\s+(.+?)\((\d+–\d+%)\)(.*?)(?=## \d+\.|$)'
            matches = re.findall(topic_pattern, content, re.DOTALL)
            
            for match in matches:
                topic_num, title, percentage, content_text = match
                outline['topics'].append({
                    'number': int(topic_num),
                    'title': title.strip(),
                    'percentage': percentage,
                    'content': content_text.strip()
                })
            
            return outline
        except Exception as e:
            print(f"Error parsing outline: {e}")
            return {}
    
    def parse_topic(self, topic_num):
        """Parse individual topic file"""
        try:
            filename = f'study-files/Azure AI-900 Exam Study Guide_ Topic {topic_num}.md'
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            topic = {
                'number': topic_num,
                'title': '',
                'sections': []
            }
            
            # Extract title
            title_match = re.search(r'# (.+)', content)
            if title_match:
                topic['title'] = title_match.group(1)
            
            # Split content into sections and subsections
            sections = self.split_into_study_chunks(content)
            topic['sections'] = sections
            
            return topic
        except Exception as e:
            print(f"Error parsing topic {topic_num}: {e}")
            return {}
    
    def split_into_study_chunks(self, content):
        """Split content into bite-sized study chunks"""
        sections = []
        
        # Split by major sections (###)
        section_pattern = r'###\s+(.+?)(?=###|\Z)'
        section_matches = re.findall(section_pattern, content, re.DOTALL)
        
        for i, section_content in enumerate(section_matches):
            lines = section_content.strip().split('\n')
            if not lines:
                continue
                
            section_title = lines[0].strip()
            section_text = '\n'.join(lines[1:]).strip()
            
            # Further split large sections into smaller chunks
            chunks = self.create_study_chunks(section_text)
            
            sections.append({
                'title': section_title,
                'chunks': chunks
            })
        
        return sections
    
    def create_study_chunks(self, text):
        """Create bite-sized chunks from section text"""
        chunks = []
        
        # Split by major paragraphs or bullet points
        paragraphs = re.split(r'\n\s*\n', text)
        
        current_chunk = ""
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue
                
            # If adding this paragraph would make chunk too long, start new chunk
            if len(current_chunk) + len(paragraph) > 800 and current_chunk:
                chunks.append({
                    'content': current_chunk.strip(),
                    'type': 'content'
                })
                current_chunk = paragraph
            else:
                if current_chunk:
                    current_chunk += "\n\n" + paragraph
                else:
                    current_chunk = paragraph
        
        # Add final chunk
        if current_chunk:
            chunks.append({
                'content': current_chunk.strip(),
                'type': 'content'
            })
        
        return chunks
    
    def parse_key_essentials(self):
        """Parse key essentials file"""
        try:
            with open('study-files/Azure AI-900 Exam Study Guide_ Key Essentials.md', 'r', encoding='utf-8') as f:
                content = f.read()
            
            essentials = {
                'title': 'Key Essentials',
                'sections': []
            }
            
            # Split into major sections
            section_pattern = r'##\s+(.+?)(?=##|\Z)'
            sections = re.findall(section_pattern, content, re.DOTALL)
            
            for section in sections:
                lines = section.strip().split('\n')
                if lines:
                    title = lines[0].strip()
                    content_text = '\n'.join(lines[1:]).strip()
                    essentials['sections'].append({
                        'title': title,
                        'content': content_text
                    })
            
            return essentials
        except Exception as e:
            print(f"Error parsing key essentials: {e}")
            return {}
    
    def parse_practice_quiz(self):
        """Parse practice quiz with questions and answers"""
        try:
            with open('study-files/Azure AI-900 Practice Quiz.md', 'r', encoding='utf-8') as f:
                content = f.read()
            
            quiz = {
                'title': 'Azure AI-900 Practice Quiz',
                'questions': [],
                'answers': {}
            }
            
            # Extract all content before answers section
            questions_section = re.search(r'# Azure AI-900 Practice Quiz.*?(?=# Answers)', content, re.DOTALL)
            if questions_section:
                questions_text = questions_section.group(0)
                
                # Parse individual questions - more flexible pattern
                question_pattern = r'(\d+)\.\s+(.+?)(?=(?:\d+\.\s+|\Z))'
                questions = re.findall(question_pattern, questions_text, re.DOTALL)
                
                for q_num, q_content in questions:
                    question_data = self.parse_question(q_num, q_content)
                    if question_data:
                        quiz['questions'].append(question_data)
            
            # Extract answers
            answers_section = re.search(r'# Answers and Explanations\n\n(.+)', content, re.DOTALL)
            if answers_section:
                answers_text = answers_section.group(1)
                quiz['answers'] = self.parse_answers(answers_text)
            
            return quiz
        except Exception as e:
            print(f"Error parsing practice quiz: {e}")
            return {}
    
    def parse_question(self, q_num, q_content):
        """Parse individual question"""
        lines = q_content.strip().split('\n')
        if len(lines) < 2:
            return None
        
        question_text = lines[0].strip()
        options = []
        
        for line in lines[1:]:
            line = line.strip()
            # Handle both formats: "- A) text" and "A) text"
            if re.match(r'^-?\s*[A-D]\)', line):
                # Remove leading "- " if present
                clean_line = re.sub(r'^-\s*', '', line)
                option_letter = clean_line[0]
                option_text = clean_line[3:].strip()
                options.append({
                    'letter': option_letter,
                    'text': option_text
                })
        
        return {
            'number': int(q_num),
            'question': question_text,
            'options': options
        }
    
    def parse_answers(self, answers_text):
        """Parse answer explanations"""
        answers = {}
        
        # Pattern to match answer lines
        answer_pattern = r'(\d+)\.\s+([A-D])\)\s+(.+?)(?=\d+\.\s+|\Z)'
        matches = re.findall(answer_pattern, answers_text, re.DOTALL)
        
        for match in matches:
            q_num, correct_answer, explanation = match
            answers[int(q_num)] = {
                'correct': correct_answer,
                'explanation': explanation.strip()
            }
        
        return answers

    def generate_flashcards(self):
        """Generate flashcards from study content"""
        flashcards = []

        # Extract from key essentials vocabulary section
        if self.key_essentials and 'sections' in self.key_essentials:
            for section in self.key_essentials['sections']:
                if 'vocabulary' in section.get('title', '').lower() or 'key' in section.get('title', '').lower():
                    content = section.get('content', '')
                    # Parse vocabulary table format
                    flashcards.extend(self.extract_vocab_flashcards(content))

        # Extract from topics
        for topic_key, topic_data in self.topics.items():
            if topic_data and 'sections' in topic_data:
                topic_num = topic_data.get('number', 0)
                for section in topic_data['sections']:
                    section_content = section.get('content', '')
                    flashcards.extend(self.extract_topic_flashcards(section_content, topic_num))

        # Add manual flashcards for key concepts
        manual_cards = self.create_manual_flashcards()
        flashcards.extend(manual_cards)

        # Remove duplicates and assign IDs
        seen_terms = set()
        unique_flashcards = []
        for card in flashcards:
            term_key = card['term'].lower().strip()
            if term_key not in seen_terms:
                seen_terms.add(term_key)
                card['id'] = len(unique_flashcards) + 1
                unique_flashcards.append(card)

        return unique_flashcards

    def extract_vocab_flashcards(self, content):
        """Extract flashcards from vocabulary-style content"""
        flashcards = []

        # Look for term: definition patterns
        lines = content.split('\n')
        current_term = None
        current_definition = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check for term pattern (Term: definition)
            if ':' in line and len(line.split(':')[0].strip()) < 50:  # Avoid long lines
                if current_term and current_definition:
                    flashcards.append({
                        'term': current_term,
                        'definition': ' '.join(current_definition),
                        'category': 'vocabulary',
                        'difficulty': self.assess_difficulty(current_definition)
                    })

                parts = line.split(':', 1)
                current_term = parts[0].strip()
                current_definition = [parts[1].strip()]
            elif current_term:
                current_definition.append(line)

        # Add the last card
        if current_term and current_definition:
            flashcards.append({
                'term': current_term,
                'definition': ' '.join(current_definition),
                'category': 'vocabulary',
                'difficulty': self.assess_difficulty(current_definition)
            })

        return flashcards

    def extract_topic_flashcards(self, content, topic_num):
        """Extract flashcards from topic content"""
        flashcards = []

        # Look for key terms and their explanations
        lines = content.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Look for bold/italic terms followed by explanations
            if '**' in line or '*' in line:
                # Extract term and definition from markdown formatting
                term_match = re.search(r'\*\*([^*]+)\*\*', line)
                if term_match:
                    term = term_match.group(1).strip()
                    # Get the next few lines as definition
                    definition_lines = []
                    for j in range(i + 1, min(i + 4, len(lines))):
                        next_line = lines[j].strip()
                        if next_line and not next_line.startswith('###') and not next_line.startswith('**'):
                            definition_lines.append(next_line)
                        else:
                            break

                    if definition_lines:
                        definition = ' '.join(definition_lines)
                        if len(definition) > 20:  # Ensure meaningful definition
                            flashcards.append({
                                'term': term,
                                'definition': definition,
                                'category': f'topic_{topic_num}',
                                'difficulty': 'medium'
                            })

        return flashcards

    def create_manual_flashcards(self):
        """Create manually curated flashcards for key concepts"""
        return [
            {
                'term': 'Machine Learning',
                'definition': 'A subset of AI where systems learn from data without being explicitly programmed. Uses algorithms to identify patterns and make predictions.',
                'category': 'core_concept',
                'difficulty': 'easy'
            },
            {
                'term': 'Deep Learning',
                'definition': 'A subset of machine learning using neural networks with multiple layers. Excels at processing complex data like images and natural language.',
                'category': 'core_concept',
                'difficulty': 'medium'
            },
            {
                'term': 'Computer Vision',
                'definition': 'AI field focused on enabling machines to interpret and understand visual information from the world, similar to human sight.',
                'category': 'workload',
                'difficulty': 'easy'
            },
            {
                'term': 'Natural Language Processing',
                'definition': 'AI field that enables machines to understand, interpret, and generate human language, including text and speech.',
                'category': 'workload',
                'difficulty': 'easy'
            },
            {
                'term': 'Generative AI',
                'definition': 'AI that creates new content such as text, images, or code based on patterns learned from training data.',
                'category': 'workload',
                'difficulty': 'medium'
            },
            {
                'term': 'Azure AI Vision',
                'definition': 'Azure service for computer vision tasks including image classification, object detection, OCR, and face analysis.',
                'category': 'azure_service',
                'difficulty': 'easy'
            },
            {
                'term': 'Azure AI Language',
                'definition': 'Azure service for natural language processing including entity recognition, sentiment analysis, and language understanding.',
                'category': 'azure_service',
                'difficulty': 'easy'
            },
            {
                'term': 'Azure OpenAI Service',
                'definition': 'Azure service providing access to OpenAI models like GPT for generative AI tasks including text generation and code completion.',
                'category': 'azure_service',
                'difficulty': 'medium'
            },
            {
                'term': 'Responsible AI',
                'definition': 'Framework ensuring AI systems are fair, reliable, safe, inclusive, transparent, accountable, and respect privacy.',
                'category': 'responsible_ai',
                'difficulty': 'medium'
            },
            {
                'term': 'Supervised Learning',
                'definition': 'ML approach where models learn from labeled training data to make predictions on new, unseen data.',
                'category': 'ml_concept',
                'difficulty': 'medium'
            },
            {
                'term': 'Unsupervised Learning',
                'definition': 'ML approach where models find patterns in data without labeled examples, such as clustering similar items.',
                'category': 'ml_concept',
                'difficulty': 'hard'
            },
            {
                'term': 'Regression',
                'definition': 'ML technique for predicting continuous numerical values, such as price prediction or temperature forecasting.',
                'category': 'ml_technique',
                'difficulty': 'easy'
            },
            {
                'term': 'Classification',
                'definition': 'ML technique for predicting categorical outcomes, such as spam detection or image recognition.',
                'category': 'ml_technique',
                'difficulty': 'easy'
            },
            {
                'term': 'Clustering',
                'definition': 'Unsupervised ML technique for grouping similar data points together without predefined categories.',
                'category': 'ml_technique',
                'difficulty': 'medium'
            },
            {
                'term': 'Transformer Architecture',
                'definition': 'Neural network architecture that uses attention mechanisms, powering modern language models like GPT and BERT.',
                'category': 'advanced_concept',
                'difficulty': 'hard'
            },
            {
                'term': 'Foundation Model',
                'definition': 'Large, pre-trained AI model that can be fine-tuned for specific tasks, such as GPT or BERT.',
                'category': 'advanced_concept',
                'difficulty': 'hard'
            },
            {
                'term': 'Prompt Engineering',
                'definition': 'The practice of crafting effective prompts to get desired outputs from generative AI models.',
                'category': 'advanced_concept',
                'difficulty': 'medium'
            },
            {
                'term': 'Hallucinations',
                'definition': 'When AI models generate false or misleading information that appears plausible but is not grounded in reality.',
                'category': 'responsible_ai',
                'difficulty': 'medium'
            },
            {
                'term': 'Optical Character Recognition (OCR)',
                'definition': 'Technology that converts images of text into machine-readable text format.',
                'category': 'computer_vision',
                'difficulty': 'easy'
            },
            {
                'term': 'Sentiment Analysis',
                'definition': 'NLP technique that determines whether text expresses positive, negative, or neutral sentiment.',
                'category': 'nlp',
                'difficulty': 'easy'
            },
            {
                'term': 'Embeddings',
                'definition': 'Vector representations of data that capture semantic meaning, used for similarity search and clustering.',
                'category': 'advanced_concept',
                'difficulty': 'hard'
            },
            {
                'term': 'Azure AI Foundry',
                'definition': 'Azure platform for building, deploying, and managing AI applications with model catalogs and development tools.',
                'category': 'azure_service',
                'difficulty': 'medium'
            },
            {
                'term': 'Automated ML (AutoML)',
                'definition': 'Azure Machine Learning feature that automates the process of selecting and training the best ML model for your data.',
                'category': 'azure_service',
                'difficulty': 'medium'
            },
            {
                'term': 'MLOps',
                'definition': 'Practices for deploying, monitoring, and maintaining ML models in production environments.',
                'category': 'ml_concept',
                'difficulty': 'hard'
            },
            {
                'term': 'Features and Labels',
                'definition': 'Features are input variables used to make predictions; Labels are the target outputs that models learn to predict.',
                'category': 'ml_concept',
                'difficulty': 'easy'
            },
            {
                'term': 'Training and Validation Datasets',
                'definition': 'Training data is used to fit the model; Validation data is used to tune hyperparameters and prevent overfitting.',
                'category': 'ml_concept',
                'difficulty': 'medium'
            },
            {
                'term': 'Overfitting',
                'definition': 'When a model learns the training data too well, including noise, leading to poor performance on new data.',
                'category': 'ml_concept',
                'difficulty': 'medium'
            },
            {
                'term': 'Bias in AI',
                'definition': 'Systematic errors in AI systems that lead to unfair outcomes, often due to biased training data or algorithms.',
                'category': 'responsible_ai',
                'difficulty': 'medium'
            }
        ]

    def assess_difficulty(self, definition_lines):
        """Assess difficulty level based on content complexity"""
        definition = ' '.join(definition_lines).lower()

        # Count complex terms
        complex_terms = ['transformer', 'neural network', 'algorithm', 'architecture', 'embeddings', 'unsupervised', 'supervised']
        complex_count = sum(1 for term in complex_terms if term in definition)

        # Length-based assessment
        length = len(definition)

        if complex_count >= 2 or length > 300:
            return 'hard'
        elif complex_count == 1 or length > 150:
            return 'medium'
        else:
            return 'easy'

# Initialize content parser
content_parser = StudyContentParser()
study_data = {}

def init_study_data():
    """Initialize study data on app startup"""
    global study_data
    if content_parser.parse_all_content():
        study_data = {
            'outline': content_parser.outline,
            'topics': content_parser.topics,
            'key_essentials': content_parser.key_essentials,
            'practice_quiz': content_parser.practice_quiz,
            'flashcards': content_parser.flashcards
        }
        print(f"✅ Generated {len(study_data['flashcards'])} flashcards")
    else:
        print("Failed to parse study content")

def init_user_session():
    """Initialize user session data"""
    if 'progress' not in session:
        session['progress'] = {
            'topics_completed': [],
            'topics_started': [],  # Track which topics have been started
            'current_topic': 1,
            'current_section': 0,
            'current_chunk': 0,
            'quiz_scores': {},
            'study_streak': 0,
            'last_study_date': None,
            'study_notes': {},  # User's personal study notes
            'bookmarks': []  # Bookmarked sections
        }

    # Ensure flashcard_progress exists (for backward compatibility)
    if 'flashcard_progress' not in session['progress']:
        session['progress']['flashcard_progress'] = {
            'cards_studied': [],  # List of card IDs studied
            'cards_mastered': [],  # List of card IDs mastered
            'review_queue': [],  # Cards due for review
            'study_sessions': [],  # Track study sessions
            'last_flashcard_date': None,
            'stats': {
                'total_studied': 0,
                'total_mastered': 0,
                'study_time': 0,  # in minutes
                'current_streak': 0
            }
        }

    # Ensure flashcard_progress.stats exists
    if 'stats' not in session['progress']['flashcard_progress']:
        session['progress']['flashcard_progress']['stats'] = {
            'total_studied': 0,
            'total_mastered': 0,
            'study_time': 0,  # in minutes
            'current_streak': 0
        }
    
    # Ensure study_notes and bookmarks exist
    if 'study_notes' not in session['progress']:
        session['progress']['study_notes'] = {}
    if 'bookmarks' not in session['progress']:
        session['progress']['bookmarks'] = []

@app.route('/')
def index():
    """Main dashboard"""
    init_user_session()
    
    # Calculate study stats
    progress = session['progress']
    total_topics = 5
    completed_topics = len(progress['topics_completed'])
    completion_percentage = (completed_topics / total_topics) * 100
    
    # Calculate exam readiness
    readiness = calculate_exam_readiness(progress)
    
    return render_template('index.html', 
                         study_data=study_data,
                         progress=progress,
                         completion_percentage=completion_percentage,
                         readiness=readiness)

@app.route('/study/<int:topic_num>')
def study_topic(topic_num):
    """Study specific topic"""
    init_user_session()
    
    if f'topic_{topic_num}' not in study_data['topics']:
        return redirect(url_for('index'))
    
    topic = study_data['topics'][f'topic_{topic_num}']
    progress = session['progress']
    
    # Mark topic as started when user visits it
    if topic_num not in progress.get('topics_started', []):
        if 'topics_started' not in progress:
            progress['topics_started'] = []
        progress['topics_started'].append(topic_num)
        session['progress'] = progress
    
    # Set current topic if user is actually studying
    if progress['current_topic'] != topic_num:
        progress['current_topic'] = topic_num
        progress['current_section'] = 0
        progress['current_chunk'] = 0
        session['progress'] = progress
    
    current_section = progress.get('current_section', 0)
    current_chunk = progress.get('current_chunk', 0)
    
    return render_template('study.html', 
                         topic=topic,
                         current_section=current_section,
                         current_chunk=current_chunk,
                         progress=progress)

@app.route('/quiz/<quiz_type>')
def quiz(quiz_type):
    """Quiz interface"""
    init_user_session()
    
    # Get custom quiz parameters from query string
    num_questions = request.args.get('num_questions', type=int, default=10)
    topics_filter = request.args.getlist('topics')  # Can select multiple topics
    
    all_questions = study_data['practice_quiz']['questions']

    if quiz_type == 'practice':
        questions = all_questions
        # Randomly select specified number of questions
        selected_questions = random.sample(questions, min(num_questions, len(questions)))
        # Shuffle answer options for each question
        for question in selected_questions:
            if 'options' in question:
                random.shuffle(question['options'])
    elif quiz_type == 'custom':
        # Custom quiz with filters
        questions = all_questions
        
        # Filter by topics if specified
        if topics_filter:
            filtered_questions = []
            for topic in topics_filter:
                topic_num = int(topic.replace('topic_', ''))
                # Questions 1-10 for topic 1, 11-20 for topic 2, etc.
                start_q = (topic_num - 1) * 10 + 1
                end_q = topic_num * 10
                filtered_questions.extend([q for q in questions if start_q <= q['number'] <= end_q])
            questions = filtered_questions if filtered_questions else questions
        
        # Select random questions
        selected_questions = random.sample(questions, min(num_questions, len(questions)))
        for question in selected_questions:
            if 'options' in question:
                random.shuffle(question['options'])
    elif quiz_type.startswith('topic_'):
        # Topic-specific mini quiz
        topic_num = int(quiz_type.split('_')[1])
        if f'topic_{topic_num}' in study_data['topics']:
            # Get questions related to this topic
            start_q = (topic_num - 1) * 10 + 1
            end_q = topic_num * 10
            topic_questions = [q for q in all_questions if start_q <= q['number'] <= end_q]
            selected_questions = random.sample(topic_questions, min(num_questions, len(topic_questions)))
            for question in selected_questions:
                if 'options' in question:
                    random.shuffle(question['options'])
        else:
            selected_questions = []
    else:
        selected_questions = []

    return render_template('quiz.html',
                         questions=selected_questions,
                         quiz_type=quiz_type)

@app.route('/quiz-builder')
def quiz_builder():
    """Custom quiz builder interface"""
    init_user_session()
    return render_template('quiz_builder.html', study_data=study_data)

@app.route('/practice-exam')
def practice_exam():
    """Full practice exam mode - simulates real AI-900 exam"""
    init_user_session()
    
    # Get all 50 questions
    all_questions = study_data['practice_quiz']['questions']
    
    # Shuffle questions for exam randomization
    import random
    exam_questions = random.sample(all_questions, min(50, len(all_questions)))
    
    # Shuffle answer options for each question
    for question in exam_questions:
        if 'options' in question:
            random.shuffle(question['options'])
    
    return render_template('practice_exam.html',
                         questions=exam_questions,
                         exam_duration=60)  # 60 minutes

@app.route('/weak-areas')
def weak_areas():
    """Analyze quiz performance and create targeted study plan"""
    init_user_session()
    
    progress = session['progress']
    quiz_scores = progress.get('quiz_scores', {})
    
    # Analyze weak topics
    weak_topics = analyze_weak_areas(progress)
    
    # Generate study plan
    study_plan = generate_study_plan(weak_topics, progress)
    
    return render_template('weak_areas.html',
                         weak_topics=weak_topics,
                         study_plan=study_plan,
                         progress=progress,
                         study_data=study_data)

@app.route('/service-comparison')
def service_comparison():
    """Azure AI Service Comparison Tool"""
    init_user_session()
    
    # Service comparison data
    comparisons = {
        'vision': {
            'title': 'Computer Vision Services',
            'services': [
                {
                    'name': 'Azure AI Vision',
                    'use_case': 'General-purpose image analysis',
                    'key_features': ['Image classification', 'Object detection', 'OCR', 'Face detection', 'Spatial analysis'],
                    'when_to_use': 'Pre-built models for common vision tasks'
                },
                {
                    'name': 'Custom Vision',
                    'use_case': 'Custom image classification/object detection',
                    'key_features': ['Train custom models', 'Image classification', 'Object detection', 'Export models'],
                    'when_to_use': 'Need domain-specific image recognition'
                },
                {
                    'name': 'Face API',
                    'use_case': 'Face detection and recognition',
                    'key_features': ['Face detection', 'Face verification', 'Face identification', 'Similar face finding'],
                    'when_to_use': 'Face-specific scenarios only'
                }
            ]
        },
        'language': {
            'title': 'Natural Language Processing Services',
            'services': [
                {
                    'name': 'Azure AI Language',
                    'use_case': 'Text analysis and NLP',
                    'key_features': ['Sentiment analysis', 'Key phrase extraction', 'Entity recognition', 'Language detection', 'PII detection'],
                    'when_to_use': 'Pre-built NLP capabilities'
                },
                {
                    'name': 'Azure AI Translator',
                    'use_case': 'Text and document translation',
                    'key_features': ['90+ languages', 'Document translation', 'Custom translation', 'Transliteration'],
                    'when_to_use': 'Multi-language support needed'
                },
                {
                    'name': 'Azure AI Speech',
                    'use_case': 'Speech-to-text and text-to-speech',
                    'key_features': ['Speech recognition', 'Speech synthesis', 'Speech translation', 'Speaker recognition'],
                    'when_to_use': 'Audio/voice interactions'
                }
            ]
        },
        'conversational': {
            'title': 'Conversational AI Services',
            'services': [
                {
                    'name': 'Azure Bot Service',
                    'use_case': 'Build and deploy chatbots',
                    'key_features': ['Multi-channel deployment', 'Bot Framework SDK', 'Integration with AI services'],
                    'when_to_use': 'Deploy bots across channels'
                },
                {
                    'name': 'Azure AI Language (CLU)',
                    'use_case': 'Conversational language understanding',
                    'key_features': ['Intent recognition', 'Entity extraction', 'Multi-turn conversations'],
                    'when_to_use': 'Custom conversational models'
                },
                {
                    'name': 'QnA Maker',
                    'use_case': 'Question & Answer from documents',
                    'key_features': ['FAQ automation', 'Knowledge base', 'Active learning'],
                    'when_to_use': 'FAQ/knowledge base scenarios'
                }
            ]
        },
        'ml': {
            'title': 'Machine Learning Services',
            'services': [
                {
                    'name': 'Azure Machine Learning',
                    'use_case': 'Enterprise ML platform',
                    'key_features': ['AutoML', 'Designer', 'MLOps', 'Model deployment', 'Responsible AI dashboard'],
                    'when_to_use': 'Custom ML models and pipelines'
                },
                {
                    'name': 'Azure AI Services',
                    'use_case': 'Pre-built AI APIs',
                    'key_features': ['Vision', 'Language', 'Speech', 'Decision', 'OpenAI'],
                    'when_to_use': 'Use pre-built models quickly'
                },
                {
                    'name': 'Azure OpenAI Service',
                    'use_case': 'Generative AI models',
                    'key_features': ['GPT-4', 'GPT-3.5', 'DALL-E', 'Embeddings', 'Enterprise-ready'],
                    'when_to_use': 'Generative AI scenarios'
                }
            ]
        }
    }
    
    # ML Techniques Comparison
    ml_techniques = [
        {
            'name': 'Regression',
            'type': 'Supervised Learning',
            'output': 'Continuous numerical value',
            'examples': ['Price prediction', 'Temperature forecasting', 'Sales forecasting'],
            'key_point': 'Predicts numbers'
        },
        {
            'name': 'Classification',
            'type': 'Supervised Learning',
            'output': 'Category/class label',
            'examples': ['Spam detection', 'Image recognition', 'Sentiment analysis'],
            'key_point': 'Predicts categories'
        },
        {
            'name': 'Clustering',
            'type': 'Unsupervised Learning',
            'output': 'Groups/clusters',
            'examples': ['Customer segmentation', 'Anomaly detection', 'Document grouping'],
            'key_point': 'Finds patterns without labels'
        }
    ]
    
    return render_template('service_comparison.html',
                         comparisons=comparisons,
                         ml_techniques=ml_techniques)

def analyze_weak_areas(progress):
    """Analyze quiz performance to identify weak topics"""
    weak_topics = []
    quiz_scores = progress.get('quiz_scores', {})
    
    if not quiz_scores:
        return []
    
    # Aggregate performance by topic
    topic_performance = {}
    for i in range(1, 6):
        topic_performance[i] = {'correct': 0, 'total': 0, 'percentage': 0}
    
    # Collect data from all quizzes
    for quiz_type, score_data in quiz_scores.items():
        topic_perf = score_data.get('topic_performance', {})
        for topic_key, perf in topic_perf.items():
            topic_num = int(topic_key.replace('topic_', ''))
            topic_performance[topic_num]['correct'] += perf.get('correct', 0)
            topic_performance[topic_num]['total'] += perf.get('total', 0)
    
    # Calculate percentages and identify weak topics
    for topic_num, perf in topic_performance.items():
        if perf['total'] > 0:
            perf['percentage'] = round((perf['correct'] / perf['total']) * 100, 1)
            
            # Consider weak if < 70% or if not studied at all
            if perf['percentage'] < 70:
                # Get topic info
                topic_key = f'topic_{topic_num}'
                topic_data = study_data['topics'].get(topic_key, {})
                
                weak_topics.append({
                    'number': topic_num,
                    'title': topic_data.get('title', f'Topic {topic_num}'),
                    'percentage': perf['percentage'],
                    'correct': perf['correct'],
                    'total': perf['total'],
                    'priority': 'High' if perf['percentage'] < 50 else 'Medium'
                })
        elif topic_num not in progress.get('topics_completed', []):
            # Topic not studied yet
            topic_key = f'topic_{topic_num}'
            topic_data = study_data['topics'].get(topic_key, {})
            weak_topics.append({
                'number': topic_num,
                'title': topic_data.get('title', f'Topic {topic_num}'),
                'percentage': 0,
                'correct': 0,
                'total': 0,
                'priority': 'High'
            })
    
    # Sort by percentage (weakest first)
    weak_topics.sort(key=lambda x: x['percentage'])
    
    return weak_topics

def generate_study_plan(weak_topics, progress):
    """Generate personalized study plan based on weak areas"""
    plan = {
        'steps': [],
        'estimated_time': 0,
        'focus_areas': []
    }
    
    if not weak_topics:
        plan['steps'].append({
            'type': 'success',
            'title': 'Great Job!',
            'description': 'You don\'t have any weak areas. Keep practicing with full exams!',
            'action': 'Take a practice exam',
            'action_url': '/practice-exam'
        })
        return plan
    
    # Add study steps for each weak topic
    for idx, topic in enumerate(weak_topics[:3], 1):  # Focus on top 3 weakest
        topic_num = topic['number']
        
        # Study the topic
        plan['steps'].append({
            'type': 'study',
            'step_num': len(plan['steps']) + 1,
            'title': f'Study {topic["title"]}',
            'description': f'Current score: {topic["percentage"]}%. Review all sections carefully.',
            'action': 'Start studying',
            'action_url': f'/study/{topic_num}',
            'priority': topic['priority'],
            'estimated_time': 30
        })
        
        # Quiz on that topic
        plan['steps'].append({
            'type': 'quiz',
            'step_num': len(plan['steps']) + 1,
            'title': f'Quiz on {topic["title"]}',
            'description': 'Test your understanding with targeted questions.',
            'action': 'Take quiz',
            'action_url': f'/quiz/topic_{topic_num}',
            'priority': topic['priority'],
            'estimated_time': 10
        })
        
        plan['estimated_time'] += 40
        plan['focus_areas'].append(topic['title'])
    
    # Review flashcards
    plan['steps'].append({
        'type': 'flashcards',
        'step_num': len(plan['steps']) + 1,
        'title': 'Review Key Concepts',
        'description': 'Use flashcards to memorize important terms and services.',
        'action': 'Study flashcards',
        'action_url': '/flashcards',
        'priority': 'Medium',
        'estimated_time': 15
    })
    
    # Final practice
    plan['steps'].append({
        'type': 'practice',
        'step_num': len(plan['steps']) + 1,
        'title': 'Take Custom Quiz',
        'description': 'Create a quiz focusing on your weak topics.',
        'action': 'Build custom quiz',
        'action_url': '/quiz-builder',
        'priority': 'High',
        'estimated_time': 20
    })
    
    plan['estimated_time'] += 35
    
    return plan

@app.route('/api/update_progress', methods=['POST'])
def update_progress():
    """Update user progress"""
    data = request.json
    progress = session.get('progress', {})
    
    # Ensure topics_started exists
    if 'topics_started' not in progress:
        progress['topics_started'] = []
    
    if 'topic' in data:
        progress['current_topic'] = data['topic']
    if 'section' in data:
        progress['current_section'] = data['section']
    if 'chunk' in data:
        progress['current_chunk'] = data['chunk']
    if 'completed_topic' in data:
        topic_num = data['completed_topic']
        if topic_num not in progress['topics_completed']:
            progress['topics_completed'].append(topic_num)
        # Move to next topic if available
        if topic_num < 5:
            progress['current_topic'] = topic_num + 1
            progress['current_section'] = 0
            progress['current_chunk'] = 0
    if 'last_study_date' in data:
        progress['last_study_date'] = data['last_study_date']
    
    session['progress'] = progress
    return jsonify({'status': 'success'})

@app.route('/api/submit_quiz', methods=['POST'])
def submit_quiz():
    """Submit quiz answers"""
    data = request.json
    answers = data.get('answers', {})
    quiz_type = data.get('quiz_type', 'practice')
    time_taken = data.get('time_taken', 0)  # Time in seconds

    # Validate that all questions have been answered
    if len(answers) == 0:
        return jsonify({'error': 'No answers provided'}), 400

    # Calculate score
    correct_answers = study_data['practice_quiz']['answers']
    score = 0
    total = len(answers)
    results = {}

    # Track performance by topic (basic implementation)
    topic_performance = {f'topic_{i}': {'correct': 0, 'total': 0} for i in range(1, 6)}

    for q_num, user_answer in answers.items():
        q_num = int(q_num)
        if q_num in correct_answers:
            is_correct = correct_answers[q_num]['correct'] == user_answer
            if is_correct:
                score += 1

            # Basic topic mapping for performance tracking
            topic_num = min(5, max(1, (q_num - 1) // 10 + 1))
            topic_performance[f'topic_{topic_num}']['total'] += 1
            if is_correct:
                topic_performance[f'topic_{topic_num}']['correct'] += 1

            results[q_num] = {
                'correct': is_correct,
                'user_answer': user_answer,
                'correct_answer': correct_answers[q_num]['correct'],
                'explanation': correct_answers[q_num]['explanation']
            }

    # Update session with enhanced tracking
    progress = session.get('progress', {})
    if 'quiz_scores' not in progress:
        progress['quiz_scores'] = {}

    progress['quiz_scores'][quiz_type] = {
        'score': score,
        'total': total,
        'percentage': round((score / total * 100), 1) if total > 0 else 0,
        'date': datetime.now().isoformat(),
        'time_taken': time_taken,
        'topic_performance': topic_performance
    }

    # Update study streak if quiz score >= 70%
    if score / total >= 0.7:
        today = datetime.now().date()
        if progress.get('last_quiz_date'):
            last_quiz = datetime.fromisoformat(progress['last_quiz_date']).date()
            if (today - last_quiz).days == 1:
                progress['study_streak'] = progress.get('study_streak', 0) + 1
            elif (today - last_quiz).days > 1:
                progress['study_streak'] = 1
        else:
            progress['study_streak'] = 1

        progress['last_quiz_date'] = today.isoformat()

    session['progress'] = progress

    return jsonify({
        'score': score,
        'total': total,
        'percentage': round((score / total * 100), 1) if total > 0 else 0,
        'results': results,
        'topic_performance': topic_performance,
        'time_taken': time_taken
    })

@app.route('/review')
def review():
    """Review mode for key concepts"""
    init_user_session()
    search_query = request.args.get('q', '').strip()
    filtered_essentials = study_data['key_essentials']

    if search_query:
        # Filter sections based on search query
        filtered_sections = []
        for section in study_data['key_essentials'].get('sections', []):
            # Search in title and content
            if (search_query.lower() in section.get('title', '').lower() or
                search_query.lower() in section.get('content', '').lower()):
                filtered_sections.append(section)
        filtered_essentials = {
            'title': study_data['key_essentials']['title'],
            'sections': filtered_sections
        }

    return render_template('review.html',
                         key_essentials=filtered_essentials,
                         search_query=search_query)

@app.route('/analytics')
def analytics():
    """Analytics dashboard showing quiz performance and exam readiness"""
    init_user_session()
    
    progress = session['progress']
    quiz_scores = progress.get('quiz_scores', {})
    
    # Calculate exam readiness
    readiness_score = calculate_exam_readiness(progress)
    
    # Get quiz history
    quiz_history = []
    for quiz_type, score_data in quiz_scores.items():
        quiz_history.append({
            'quiz_type': quiz_type,
            'score': score_data.get('score', 0),
            'total': score_data.get('total', 0),
            'percentage': score_data.get('percentage', 0),
            'date': score_data.get('date', ''),
            'time_taken': score_data.get('time_taken', 0)
        })
    
    # Sort by date (newest first)
    quiz_history.sort(key=lambda x: x['date'], reverse=True)
    
    return render_template('analytics.html',
                         progress=progress,
                         quiz_history=quiz_history,
                         readiness=readiness_score,
                         study_data=study_data)

def calculate_exam_readiness(progress):
    """Calculate exam readiness percentage based on multiple factors"""
    readiness = {
        'overall': 0,
        'topics_score': 0,
        'quiz_score': 0,
        'flashcard_score': 0,
        'ready': False,
        'recommendations': []
    }
    
    # Topics completed (30% weight)
    topics_completed = len(progress.get('topics_completed', []))
    topics_score = (topics_completed / 5) * 30
    readiness['topics_score'] = topics_score
    
    # Quiz performance (50% weight)
    quiz_score = 0  # Initialize to 0
    quiz_scores = progress.get('quiz_scores', {})
    if quiz_scores:
        avg_percentage = sum(q.get('percentage', 0) for q in quiz_scores.values()) / len(quiz_scores)
        quiz_score = (avg_percentage / 100) * 50
        readiness['quiz_score'] = quiz_score
    else:
        readiness['recommendations'].append('Take practice quizzes to assess your knowledge')
        readiness['quiz_score'] = 0
    
    # Flashcards mastered (20% weight)
    flashcard_progress = progress.get('flashcard_progress', {})
    stats = flashcard_progress.get('stats', {})
    total_mastered = stats.get('total_mastered', 0)
    # Assuming 50+ cards as good target
    flashcard_score = min((total_mastered / 50) * 20, 20)
    readiness['flashcard_score'] = flashcard_score
    
    # Calculate overall
    readiness['overall'] = round(topics_score + quiz_score + flashcard_score, 1)
    
    # Determine if ready
    readiness['ready'] = (
        readiness['overall'] >= 80 and
        topics_completed >= 5 and
        quiz_scores and
        all(q.get('percentage', 0) >= 80 for q in quiz_scores.values())
    )
    
    # Generate recommendations
    if topics_completed < 5:
        readiness['recommendations'].append(f'Complete {5 - topics_completed} more topic(s)')
    
    if quiz_scores:
        low_scores = [q for q in quiz_scores.values() if q.get('percentage', 0) < 80]
        if low_scores:
            readiness['recommendations'].append(f'Improve quiz scores (currently {len(low_scores)} below 80%)')
    
    if total_mastered < 30:
        readiness['recommendations'].append(f'Master more flashcards (current: {total_mastered}, target: 30+)')
    
    if readiness['ready']:
        readiness['recommendations'] = ['You\'re ready for the exam! 🎉']
    
    return readiness

@app.route('/debug/quiz')
def debug_quiz():
    """Debug route to see parsed quiz data"""
    quiz_data = study_data.get('practice_quiz', {})
    return jsonify({
        'total_questions': len(quiz_data.get('questions', [])),
        'sample_questions': quiz_data.get('questions', [])[:3],  # First 3 questions
        'total_answers': len(quiz_data.get('answers', {}))
    })

@app.route('/flashcards')
def flashcards():
    """Flashcard study interface"""
    init_user_session()

    # Get filter parameters
    category = request.args.get('category', 'all')
    difficulty = request.args.get('difficulty', 'all')
    mode = request.args.get('mode', 'study')  # study, review, or new

    # Filter flashcards based on parameters
    all_flashcards = study_data.get('flashcards', [])
    filtered_cards = []

    for card in all_flashcards:
        # Apply category filter
        if category != 'all' and card.get('category') != category:
            continue

        # Apply difficulty filter
        if difficulty != 'all' and card.get('difficulty') != difficulty:
            continue

        # Apply mode filter
        if mode == 'new':
            # Only show cards not studied yet
            progress = session['progress']['flashcard_progress']
            if card['id'] in progress['cards_studied']:
                continue
        elif mode == 'review':
            # Only show cards due for review
            progress = session['progress']['flashcard_progress']
            if card['id'] not in progress['review_queue']:
                continue

        filtered_cards.append(card)

    # If no cards match filters, show all cards
    if not filtered_cards:
        filtered_cards = all_flashcards[:20]  # Show first 20 cards

    # Shuffle for study mode
    if mode == 'study':
        random.shuffle(filtered_cards)

    # Get progress stats
    progress = session['progress']['flashcard_progress']
    stats = progress['stats']

    return render_template('flashcards.html',
                         flashcards=filtered_cards,
                         category=category,
                         difficulty=difficulty,
                         mode=mode,
                         stats=stats)

@app.route('/api/flashcard_response', methods=['POST'])
def flashcard_response():
    """Handle flashcard response (correct/incorrect)"""
    data = request.json
    card_id = data.get('card_id')
    response = data.get('response')  # 'correct' or 'incorrect'
    study_time = data.get('study_time', 0)  # Time spent on this card in seconds

    if not card_id or response not in ['correct', 'incorrect']:
        return jsonify({'error': 'Invalid data'}), 400

    init_user_session()
    progress = session['progress']['flashcard_progress']
    stats = progress['stats']

    # Update cards studied
    if card_id not in progress['cards_studied']:
        progress['cards_studied'].append(card_id)
        stats['total_studied'] += 1

    # Handle response
    if response == 'correct':
        # Add to mastered if not already there
        if card_id not in progress['cards_mastered']:
            progress['cards_mastered'].append(card_id)
            stats['total_mastered'] += 1

        # Remove from review queue if present
        if card_id in progress['review_queue']:
            progress['review_queue'].remove(card_id)

    else:  # incorrect
        # Add to review queue for later review
        if card_id not in progress['review_queue']:
            progress['review_queue'].append(card_id)

        # Remove from mastered if it was there
        if card_id in progress['cards_mastered']:
            progress['cards_mastered'].remove(card_id)
            stats['total_mastered'] -= 1

    # Update study time
    stats['study_time'] += study_time / 60  # Convert to minutes

    # Update last flashcard date
    today = datetime.now().date().isoformat()
    progress['last_flashcard_date'] = today

    # Update study streak
    if progress.get('last_flashcard_date'):
        last_date = datetime.fromisoformat(progress['last_flashcard_date']).date()
        today_date = datetime.now().date()
        if (today_date - last_date).days == 1:
            stats['current_streak'] += 1
        elif (today_date - last_date).days > 1:
            stats['current_streak'] = 1
    else:
        stats['current_streak'] = 1

    # Record study session
    progress['study_sessions'].append({
        'date': datetime.now().isoformat(),
        'cards_studied': 1,
        'time_spent': study_time,
        'response': response
    })

    session['progress'] = session['progress']  # Save changes

    return jsonify({
        'success': True,
        'stats': stats,
        'review_queue_count': len(progress['review_queue'])
    })

@app.route('/api/flashcard_stats')
def flashcard_stats():
    """Get flashcard statistics"""
    init_user_session()
    progress = session['progress']['flashcard_progress']
    stats = progress['stats']

    # Calculate additional stats
    total_cards = len(study_data.get('flashcards', []))
    mastered_percentage = (stats['total_mastered'] / total_cards * 100) if total_cards > 0 else 0

    # Category breakdown
    category_stats = {}
    for card in study_data.get('flashcards', []):
        category = card.get('category', 'unknown')
        if category not in category_stats:
            category_stats[category] = {'total': 0, 'mastered': 0}
        category_stats[category]['total'] += 1
        if card['id'] in progress['cards_mastered']:
            category_stats[category]['mastered'] += 1

    return jsonify({
        'total_cards': total_cards,
        'studied_cards': stats['total_studied'],
        'mastered_cards': stats['total_mastered'],
        'mastered_percentage': round(mastered_percentage, 1),
        'review_queue': len(progress['review_queue']),
        'study_time': round(stats['study_time'], 1),
        'current_streak': stats['current_streak'],
        'category_stats': category_stats
    })

@app.route('/api/save_note', methods=['POST'])
def save_note():
    """Save a study note"""
    data = request.json
    note_id = data.get('note_id')  # Format: "topic_X_section_Y"
    note_text = data.get('note_text', '')
    
    if not note_id:
        return jsonify({'error': 'Note ID required'}), 400
    
    init_user_session()
    progress = session.get('progress', {})
    
    if not progress.get('study_notes'):
        progress['study_notes'] = {}
    
    progress['study_notes'][note_id] = {
        'text': note_text,
        'updated': datetime.now().isoformat()
    }
    
    session['progress'] = progress
    
    return jsonify({'success': True})

@app.route('/api/get_notes')
def get_notes():
    """Get all study notes"""
    init_user_session()
    progress = session.get('progress', {})
    notes = progress.get('study_notes', {})
    return jsonify({'notes': notes})

@app.route('/api/toggle_bookmark', methods=['POST'])
def toggle_bookmark():
    """Toggle bookmark for a section"""
    data = request.json
    bookmark_id = data.get('bookmark_id')  # Format: "topic_X_section_Y"
    
    if not bookmark_id:
        return jsonify({'error': 'Bookmark ID required'}), 400
    
    init_user_session()
    progress = session.get('progress', {})
    
    if 'bookmarks' not in progress:
        progress['bookmarks'] = []
    
    if bookmark_id in progress['bookmarks']:
        progress['bookmarks'].remove(bookmark_id)
        bookmarked = False
    else:
        progress['bookmarks'].append(bookmark_id)
        bookmarked = True
    
    session['progress'] = progress
    
    return jsonify({'success': True, 'bookmarked': bookmarked})

if __name__ == '__main__':
    init_study_data()
    app.run(debug=True) 