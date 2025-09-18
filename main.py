// Instalador
// Preguntar caracteristicas pc --> Script con API de Nvidia
// Qtile, picom, kitty, nvim

import os

user = os.getlogin()
os.chdir(f"/home/{user}")

def main():
    # Qtile
    os.system("sudo pacman -S qtile pacman-contrib")
    os.system("yay -S nerd-fonts-ubuntu-mono")
    os.system("pip install psutil")
    os.system("sudo pacman -S picom")

    # Neovim
    os.system("curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz")
    os.system("sudo rm -rf /opt/nvim-linux-x86_64")
    os.system("sudo tar -C /opt -xzf nvim-linux-x86_64.tar.gz")

if __name__ == "__main__":
    main()
