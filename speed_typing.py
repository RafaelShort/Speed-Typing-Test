import tkinter as tk
from tkinter import messagebox
import time
import random

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Velocidade de Digitação")
        
        # Título do aplicativo
        self.title_label = tk.Label(root, text="Teste de Velocidade de Digitação", font=("Helvetica", 16))
        self.title_label.pack(pady=10)
        
        # Lista de frases para digitar
        self.phrases = [
            "Que a força esteja com você.",
            "Eu sou seu pai.",
            "Aqui está olhando para você, garoto.",
            "A vida é como uma caixa de chocolates.",
            "Você não pode lidar com a verdade!",
            "Vou fazer uma oferta que você não poderá recusar.",
            "Desculpe, não posso fazer isso.",
            "E.T. telefone para casa.",
            "O nome é Bond, James Bond.",
            "Houston, temos um problema.",
            "Eu vejo pessoas mortas.",
            "Lembre-se de quem você é.",
            "Viva, e deixe viver.",
            "Eu sou o rei do mundo!",
            "Apenas faça.",
            "A vida encontra um jeito.",
            "Com grandes poderes vêm grandes responsabilidades.",
            "Eu vou precisar de um barco maior.",
            "Cuidado com o lado negro.",
            "Você fala comigo?",
            "Nós sempre teremos Paris.",
            "O que temos aqui é um fracasso de comunicação.",
            "Um dia, esse sonho se tornará realidade.",
            "Aqui vamos nós de novo.",
            "A vida é um presente.",
            "Você não pode ganhar.",
            "Se você a construir, eles virão.",
            "Ninguém é perfeito.",
            "Eu sou Groot.",
            "Isso é tudo, pessoal!",
            "O verdadeiro amor nunca morre.",
            "Você é um bicho do mato!",
            "Estou aqui para ajudar.",
            "A escolha é sua.",
            "A vida é uma aventura.",
            "Coragem é saber o que não temer.",
            "Às vezes, você só precisa dar um passo para trás.",
            "A felicidade é um estado de espírito.",
            "Sonhos podem se tornar realidade.",
            "Nada é impossível.",
            "A vida é curta, então viva-a.",
            "A mente é tudo.",
            "O futuro pertence àqueles que acreditam.",
            "Você faz o que tem que fazer.",
            "Um dia de cada vez.",
            "A vida é um mistério a ser resolvido.",
            "A sabedoria é um presente.",
            "O amor é a resposta.",
            "Seja a mudança que você deseja ver.",
            "A verdadeira beleza vem de dentro.",
            "Cada dia é uma nova oportunidade.",
            "A vida é cheia de surpresas."
        ]
        self.start_time = None
        
        self.prompt_label = tk.Label(root, text="Digite o seguinte texto:")
        self.prompt_label.pack(pady=10)
        
        self.phrase_display = tk.Label(root, wraplength=400, justify="center")
        self.phrase_display.pack(pady=10)

        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack(pady=10)
        self.input_text.bind("<KeyRelease>", self.check_input)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Iniciar Teste", command=self.start_test)
        self.start_button.pack(pady=10)

    def start_test(self):
        self.input_text.delete(1.0, tk.END)
        self.result_label.config(text="")
        self.selected_phrase = random.choice(self.phrases)
        self.phrase_display.config(text=self.selected_phrase)
        self.start_time = time.time()
        self.input_text.focus()

    def check_input(self, event):
        user_input = self.input_text.get(1.0, tk.END).strip()
        if user_input == self.selected_phrase:
            time_taken  = time.time() - self.start_time
            typing_speed = (len(user_input.split()) / time_taken) * 60
            self.result_label.config(text=f"Parabéns, você conseguiu! Velocidade: {typing_speed:.2f} palavras por minuto")
            messagebox.showinfo("Teste Concluído", f"Velocidade: {typing_speed:.2f} palavras por minuto")
            self.start_time = None  # Reset the start time

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
