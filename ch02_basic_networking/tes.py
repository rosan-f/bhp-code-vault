import subprocess
import shlex

def execute(cmd):
    if not cmd:
        return

    perintah_terpisah = shlex.split(cmd)
    print(f"[DEBUG] Bentuk List setelah diPecah shlex:\n{perintah_terpisah}")


    try:
        output = subprocess.check_output(
            perintah_terpisah, 
            stderr=subprocess.STDOUT
            )
        
        return output.decode()
    
    except subprocess.CalledProcessError as e:
        return e.output.decode()

if __name__ == '__main__':
    # Tes 1: Perintah sederhana melihat user
    print("--- HASIL TES 1 (whoami) ---")
    hasil1 = execute("whoami")
    print(f"Output:\n{hasil1}")

    # Tes 2: Perintah dengan argumen dan tanda petik
    print("--- HASIL TES 2 (echo dengan spasi) ---")
    hasil2 = execute('echo "Halo dari subprocess Python!"')
    print(f"Output:\n{hasil2}")

    # Tes 3: Perintah melihat isi folder saat ini
    print("--- HASIL TES 3 (ls -l) ---")
    hasil3 = execute("ls -l")
    print(f"Output:\n{hasil3}")