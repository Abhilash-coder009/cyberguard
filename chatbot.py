"""
CyberGuard - Cybersecurity Assistant
Created by Abhilash
ALL knowledge comes from files - NOTHING hardcoded!
"""

import os
import subprocess
from pathlib import Path
import logging
from datetime import datetime
import re

# ==================== CONFIGURATION ====================
DOCS_DIR = "cybersecurity_docs"
OLLAMA_PATH = r"C:\Users\Admin\AppData\Local\Programs\Ollama\ollama.exe"
LLM_MODEL = "llama3.2:1b"

# Bot identity (only basic info, no responses)
BOT_NAME = "CyberGuard"
CREATOR_NAME = "Abhilash"
VERSION = "2.0"

# ==================== LOGGING SETUP ====================
logging.basicConfig(
    filename='bot_logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True
)

# ==================== MAIN BOT CLASS ====================
class CyberBot:
    def __init__(self):
        """Initialize the bot"""
        self.bot_name = BOT_NAME
        self.creator = CREATOR_NAME
        self.version = VERSION
        
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Load ALL documents from knowledge folder
        self.documents = []
        self.load_documents_silent()
        
        # Check Ollama
        self.check_ollama_silent()
        
        # Session tracking
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.question_count = 0
        
        # Log startup
        logging.info(f"🔵 {self.bot_name} SESSION STARTED - ID: {self.session_id}")
        logging.info(f"Bot version {self.version} - Created by {self.creator}")
        logging.info(f"Loaded {len(self.documents)} knowledge files")
        logging.info("-" * 50)
        
        # Show welcome banner
        self.show_welcome()
    
    def show_welcome(self):
        """Show the clean welcome banner"""
        print("╔" + "═"*58 + "╗")
        print("║" + f"🔐 {self.bot_name} - Cybersecurity Assistant".center(58) + "║")
        print("╠" + "═"*58 + "╣")
        print("║" + f"  Version {self.version} • Created by {self.creator}".center(58) + "║")
        print("║" + " " * 58 + "║")
        print("║" + "  I'm here to help with cybersecurity questions.  ".center(58) + "║")
        print("║" + "  Type 'exit' to quit.  ".center(58) + "║")
        print("╚" + "═"*58 + "╝")
        print()
        print("─"*60)
        print("💬 Start chatting! Ask me anything about cybersecurity.")
        print("─"*60)
    
    # ==================== HELPER FUNCTIONS ====================
    def clean_text(self, text):
        """Remove markdown formatting from text"""
        if not text:
            return text
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
        text = re.sub(r'__(.*?)__', r'\1', text)
        text = re.sub(r'\*(?!\s)(.*?)(?<!\s)\*', r'\1', text)
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
        text = re.sub(r'`(.*?)`', r'\1', text)
        return text.strip()
    
    def check_ollama_silent(self):
        """Check if Ollama is running"""
        try:
            result = subprocess.run(
                [OLLAMA_PATH, "list"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode != 0:
                print("\n❌ Error: Ollama is not running.")
                print("   Please start Ollama from Start Menu and try again.")
                exit(1)
        except Exception:
            print("\n❌ Error: Could not connect to Ollama.")
            print("   Please make sure Ollama is installed and running.")
            exit(1)
    
    def load_documents_silent(self):
        """Load ALL knowledge files silently"""
        files = list(Path(DOCS_DIR).glob("*.txt"))
        
        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    content = self.clean_text(content)
                    self.documents.append({
                        'content': content,
                        'source': file_path.name
                    })
            except Exception as e:
                logging.error(f"Error loading {file_path.name}: {e}")
    
    def find_exact_match(self, question):
        """Look for exact question matches in knowledge files"""
        question_lower = question.lower().strip()
        
        # Check each document for exact matches
        for doc in self.documents:
            lines = doc['content'].split('\n')
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    if key.lower().strip() == question_lower:
                        return value.strip()
        
        return None
    
    def find_relevant_docs(self, question):
        """Find relevant information from knowledge base"""
        question_lower = question.lower().strip()
        relevant = []
        
        # Log every question
        self.question_count += 1
        logging.info(f"Q{self.question_count}: {question}")
        
        # Search knowledge base
        for doc in self.documents:
            content_lower = doc['content'].lower()
            score = 0
            
            words = question_lower.split()
            for word in words:
                if len(word) > 3 and word in content_lower:
                    score += 1
            
            if score > 0:
                # Find best paragraph
                paragraphs = doc['content'].split('\n\n')
                best_para = ""
                best_score = 0
                
                for para in paragraphs:
                    para_lower = para.lower()
                    para_score = 0
                    for word in words:
                        if len(word) > 3 and word in para_lower:
                            para_score += 1
                    if para_score > best_score:
                        best_score = para_score
                        best_para = para
                
                content = best_para if best_para else doc['content'][:500]
                
                relevant.append({
                    'content': content,
                    'source': doc['source'],
                    'score': score
                })
        
        relevant.sort(key=lambda x: x['score'], reverse=True)
        
        if relevant:
            logging.info(f"  ↳ Used: {relevant[0]['source']} (score: {relevant[0]['score']})")
        else:
            logging.info(f"  ↳ No relevant documents found")
        
        return relevant[:1]
    
    def ask_ollama(self, prompt):
        """Get answer from Ollama"""
        try:
            if len(prompt) > 1500:
                prompt = prompt[:1500] + "..."
            
            result = subprocess.run(
                [OLLAMA_PATH, "run", LLM_MODEL],
                input=prompt,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=20
            )
            answer = result.stdout.strip()
            answer = self.clean_text(answer)
            return answer
        except Exception as e:
            logging.error(f"Ollama error: {e}")
            return None
    
    def ask(self, question):
        """Process a question and return answer - ALL from files!"""
        
        # First check for exact matches in knowledge files
        exact_match = self.find_exact_match(question)
        if exact_match:
            print(f"\n{self.bot_name}: {exact_match}")
            logging.info(f"  ↳ Used: exact match from knowledge file")
            return
        
        # If no exact match, use LLM with knowledge base
        print(f"\n{self.bot_name}: ", end="", flush=True)
        
        # Find relevant info
        relevant = self.find_relevant_docs(question)
        
        if not relevant:
            answer = "I don't have information about that yet. Try asking about phishing, ransomware, passwords, or other cybersecurity topics."
            print(answer)
            logging.info(f"  ↳ Answer: {answer[:100]}...")
            return
        
        best_match = relevant[0]['content']
        
        prompt = f"""You are {self.bot_name}, a cybersecurity assistant created by {self.creator}.
Answer the question using ONLY the information provided.
Keep answers short and focused on cybersecurity.

Question: {question}

Information: {best_match}

Answer:"""
        
        answer = self.ask_ollama(prompt)
        
        if not answer or len(answer) < 10:
            answer = "I found some information but couldn't generate a good answer. Please try rephrasing your question."
        
        print(answer)
        logging.info(f"  ↳ Answer: {answer[:100]}...")
    
    # ==================== CHAT LOOP ====================
    def chat(self):
        """Main chat loop"""
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['exit', 'quit', '/exit']:
                    # Look for goodbye in knowledge files
                    goodbye = self.find_exact_match('exit')
                    if not goodbye:
                        goodbye = "Goodbye! Stay safe online! 👋"
                    print(f"\n{self.bot_name}: {goodbye}")
                    print(f"   - Created by {self.creator}")
                    logging.info(f"🔴 SESSION ENDED - Total questions: {self.question_count}")
                    logging.info("=" * 50)
                    break
                
                if not user_input:
                    continue
                
                self.ask(user_input)
                
            except KeyboardInterrupt:
                print(f"\n\n{self.bot_name}: Goodbye! Stay safe online! 👋")
                print(f"   - Created by {self.creator}")
                logging.info(f"🔴 SESSION ENDED (interrupt) - Total questions: {self.question_count}")
                logging.info("=" * 50)
                break
            except Exception as e:
                print(f"\n{self.bot_name}: I encountered an issue. Please try again.")
                logging.error(f"Error in chat: {e}")

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    bot = CyberBot()
    bot.chat()