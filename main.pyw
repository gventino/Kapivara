import docling
from docling.document_converter import DocumentConverter

import customtkinter as ctk
from customtkinter import filedialog

def Popup(title, text):
    popup = ctk.CTkToplevel()
    popup.title(title)
    
    label = ctk.CTkLabel(popup, text=text)
    label.pack(pady=20, padx=10)
    
    button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    button.pack(pady=10, padx=10)

def browse_files():
    file = filedialog.askopenfilename(filetypes=[('PDFs','.pdf')])
    if file:
        convert_n_save(file)
        Popup(':D', 'MARKDOWN SALVO')
               
def convert_n_save(file):
    filename = file.split('.')
    try:
        converter = DocumentConverter()
        result = converter.convert(file)
        md = result.document.export_to_markdown()
        with open(filename[0]+'.md','w') as f:
            f.write(md)
    except:
        Popup('ERRO!','Cuidado, acho que você fez algo errado...')

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    window = ctk.CTk()
    window.title('Kapivara')
    window.geometry()

    label_file_explorer = ctk.CTkLabel(window,
                                            text='Kapivara',
                                            width=30, height=2,
                                        )

    button_explore = ctk.CTkButton(window, 
                                        text="Buscar Arquivos",
                                        command=browse_files, 
                                    )

    label_file_explorer.grid(column=1, row=1, padx=10, pady=10)
    button_explore.grid(column=1, row=2, padx=10, pady=5)

    window.mainloop()

if __name__=='__main__':
    main()
