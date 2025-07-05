# !/usr/bin/python3(venv)
# THIS CODE IS MADE FOR LEARNING PURPOSES
# I'm not even an university/college student, still 17 Years old and have yet to learn about programming.
# There may be a few errors or typo mistakes i've made, i don't even suggest you to use this code in the first place. But if you feel like it, be my guest.
# UTF-8 - All english

__author__ = "Mert KM"                                                

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import simpledialog
import subprocess
import threading
import os
import sys
import time



class UpdateManagement:
    def __init__(self, root, update):
        self.root = root
        self.update_flag = update
        self.text_output = None

        
    def run_sudo_command(self, command, password):
        try:
            process = subprocess.Popen(['sudo', '-S'] + command.split(),
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT,
                                       text=True)
            stdout, _ = process.communicate(password + '\n')
            self.text_output.insert(tk.END, stdout)
            self.text_output.see(tk.END)
        except Exception as e:
            self.text_output.insert(tk.END, f"Error: {e}\n")


    
    def update(self):
        self.text_output.insert(tk.END, "[$] Starting update process...\n")

        password = simpledialog.askstring("Authentication Required",
                                          "Enter your sudo password if you have one. Leave it blank otherly:",
                                          show='*')

        if not password:
            self.text_output.insert(tk.END, "[!] Update canceled. No password entered.\n")
            return

        self.run_sudo_command("apt update", password)
        self.run_sudo_command("apt upgrade -y", password)
        time.sleep(0.15) # brief time cut to avoid possible errors
        self.text_output.insert(tk.END, "[+] Update process completed.\n")

        
    def start_update_thread(self):
        # show what's going on
        threading.Thread(target=self.update, daemon=True).start()
 
    def automation(self):   
        # i used automatic root privillege here, you can adjust this part a little. It uses sudo/root 
        self.text_output.insert(tk.END, "[*] Enable button clicked. Trying to run script...\n")

        self.script_path = os.path.abspath("./startpy.sh")
        if os.path.exists(self.script_path):
            try:
                process = subprocess.Popen(['bash', self.script_path],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT,
                                           text=True)
                for line in process.stdout:
                    self.text_output.insert(tk.END, line)
                    self.text_output.see(tk.END)
            except Exception as a:
                self.text_output.insert(tk.END, f"[!] Can't run the script, check it perhaps? {a}\n")
        else:
            self.text_output.insert(tk.END, "[?] Script not found.\n")



        

## ------MAIN------

    def main(self):
        self.root.geometry("700x400")
        self.root.resizable(False, False)
        self.root.title("automation update")

        # Label for update management and INFOS/DETAILS.
        self.min = tk.StringVar(self.root)
        self.min.set("automation")
        self.sec = tk.StringVar(self.root)
        self.sec.set("for updates")

        self.min_label = tk.Label(self.root,
                                  textvariable=self.min, font=(
                                      "arial", 18, "bold"), bg="red", fg='black')
        self.min_label.pack()

        self.sec_label = tk.Label(self.root,
                                  textvariable=self.sec, font=(
                                      "arial", 18, "bold"), bg="black", fg="white")
        self.sec_label.pack()

    ## -------------FUNCTIONS AND GUI'S-------------   
        


        # terminal output
        self.text_output = scrolledtext.ScrolledText(self.root, height=10, width=80)
        self.text_output.pack(pady=10)

        # buttons
        ttk.Button(self.root, text="Run Update", command=self.start_update_thread).pack(pady=5)


        ##
        ttk.Button(self.root, text="Settings", command=self.new_window).pack(pady=20)

    def new_window(self):
        top = tk.Toplevel(self.root)
        top.geometry("300x300")
        top.resizable(False, False)
        top.title("Enabling / Automation / Updating")
        tk.Label(top, text='''
            This is where you automate the program.
            even when the computer is shut off or rebooted.    
            (UNIX ONLY) 
                 ''').pack(pady=20)
        ttk.Button(top, text="Close", command=top.destroy).pack()
        ttk.Button(top, text="Enable", command=self.automation).pack()


        





if __name__ == "__main__":
    root = tk.Tk()
    manage = UpdateManagement(root, update=False)
    manage.main()
    root.mainloop()
 

