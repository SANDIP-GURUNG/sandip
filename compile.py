from os import system as c
import marshal
import base64
import zlib

try:
    from Cython.Build.BuildExecutable import build as execute
except:
    c('pip install cython >/dev/null')
    
try:
    import os,cython
    from Cython.Build.BuildExecutable import build
except:
    os.system('pip install cython > /dev/null')
os.system('xdg-open https://github.com/SANDIP-GURUNG')

def line():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#---------------- LOGO -----------#
logo=(f"""            
                 {A}╔═╗╔═╗╔╗╔╦╔═╗
                 {G}╚═╗╠═╣║║║║╠═╝
                 {A}╚═╝╩ ╩╝╚╝╩╩  
{A}┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{B}┃ {G}   ┏┓┏┓┳┓┳┏┓     {B}┃ {G} OWNER  : SANDIP GURUNG     {B}┃
{B}┃ {G}   ┗┓┣┫┃┃┃┃┃     {B}┃ {G} TOOL   : COMPILE           {B}┃
{B}┃ {G}   ┗┛┛┗┛┗┻┣┛     {B}┃ {G} GITHUB : SANDIP-GURUNG     {B}┃
{B}┃ {G}                 {B}┃ {G} STATUS : FREE              {B}┃
{A}┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")



 

#--------------- CLEAR FUNCTION -------------#
def clear():
    c('clear')
    print(logo)
#----------- MAIN FUNCTION ------------#


def main():
    clear()
    print(' \x1b[38;5;46m[1] Marshal ')
    print(' [2] Base64  ')
    print(' [3] Zlib    ')
    print(' [4] Cython  ')
    print(' [5] Cython1  ')
    print(' [0] Exit ')
    line()
    option=input('\x1b[38;5;46m [?] CHOICE MENU : ')
    if option in ['a','1']:
        marshal_enc()
    elif option in ['b','2']:
        base64_enc()
    elif option in ['c','3']:
        zlib_enc()
    elif option in ['d','4']:
        cython_executable()
    elif option in ['5','e']:
        cython1()
    else:
        exit(' TOOL EXITED :/')
#----------- MARSHAL ENCRYPTION --------------#
def marshal_enc():
    clear()
    file=input(' ENTER SOURCE FILE NAME : ')
    filex=input(' ENTER OUTPUT FILE NAME : ')
    try:
        file_open=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : SANDIP GURUNG\n# GITHUB : https://github.com/SANDIP-GURUNG\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    line()
    print(' [✓✓] ENCRYPTION COMPLETE :/ ')
    print(' [✓✓] OUTPUT FILE SAVE AS : '+filex)
#---------- BASE64 ENCRYPTION ------------#
def base64_enc():
    clear()
    input_file=input(' ENTER SOURCE FILE PATH : ')
    output_file=input(' ENTER OUTPUT FILE PATH : ')
    try:
        file_open=open(input_file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compile=base64.b64encode(file_open.encode())
    run_code=f'import base64\nexec(base64.b64decode({compile}))'
    out_put=open(output_file,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : ABDUL HAKIM\n# GITHUB : https://github.com/MASTER-404\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+output_file)
#---------------- ZLIB ENCRYPTION -----------------#
def zlib_enc():
    clear()
    src=input(' ENTER SOURCE FILE PATH : ')
    save_file=input(' ENTER OUTPUT FILE PATH : ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(' FILE NOT FOUND !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'import zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : SANDIP GURUNG\n# GITHUB : https://github.com/SANDIP-GURUNG\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+save_file)
#--------------- CYTHON EXECUTABLE -----------------#
def cython_executable():
        clear()
        os.system('xdg-open https://facebook.com/sandipghotaneygurung ')       
        file = input(' Put File: ')
        try:
            open(file,'r').read()
        except:
            exit(' File Location Not Found ')
        os.system('cythonize -b '+file+'> /dev/null')
        input(' Your File Compile Done Enjoy ');main() 

#----------------- END --------------#

def cython1():
    clear()
    file=input(' ENTER SOURCE FILE PATH : ')
    try:
        filex=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR :/')
    error=filex.replace('	','    ')
    solve=open(file,'w').write(error)
    execute(file)
    clear()
    print(' [✓✓] CYTHON EXECUTABLE COMPLETE :")')
    save=file[:-3]
    print(' [✓✓] EXECUTABLE FILE SAVE AS : '+save)
#----------------- END --------------#
main()