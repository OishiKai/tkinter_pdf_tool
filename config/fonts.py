import customtkinter as ctk


def get_fonts():
    return {
        "title": ctk.CTkFont("Meiryo UI", 12, "bold"),
        "default": ctk.CTkFont("Meiryo UI", 12),
        "description": ctk.CTkFont("Meiryo UI", 10),
    }
