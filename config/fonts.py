import customtkinter as ctk


def get_fonts():
    return {
        "title": ctk.CTkFont("Meiryo Bold", 12),
        "default": ctk.CTkFont("Meiryo", 12),
        "description": ctk.CTkFont("Meiryo", 10),
    }
