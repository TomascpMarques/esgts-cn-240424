# THE CODE ! ! !
import sys

def factorial_recurssive(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial_recurssive(n - 1)


def factorial_iterative(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        mult = 1
        for factor in range(1, n + 1):
            mult *= factor
        return mult


# ==============================================================================
# Run as a script 

if __name__ == "__main__":
    # Sys args
    
    receive_num_from_cli = int (sys.argv[1])
    r = receive_num_from_cli
    
    fr = factorial_recurssive(receive_num_from_cli)
    fi = factorial_iterative(receive_num_from_cli)
    
    msg = f"Received {r}\n | FI = {fi}\n | FR = {fr}"
    print(msg)
    
# ==============================================================================