from math import sqrt
import sqlite3
from datetime import datetime
import time
from py_expression_eval import Parser
import math
import numpy

meth = {"ceil":math.ceil, "comb":math.comb, "copysign":math.copysign, "fabs":math.fabs, "factorial":math.factorial, "floor":math.floor, "fmod":math.fmod, "frexp":math.frexp, "fsum":math.fsum, "gcd":math.gcd, "isclose":math.isclose, "isfinite":math.isfinite, "isinf":math.isinf, "isnan":math.isnan, "isqrt":math.isqrt, "ldexp":math.ldexp, "modf":math.modf, "perm":math.perm, "prod":math.prod, "remainder":math.remainder, "exp":math.exp, "expm1":math.expm1, "log":math.log, "log1p":math.log1p, "log2":math.log2, "log10":math.log10, "pow":math.pow, "sqrt":math.sqrt, "acos":math.acos, "asin":math.asin, "atan":math.atan, "atan2":math.atan2, "cos":math.cos, "dist":math.dist, "hypot":math.hypot, "sin":math.sin, "tan":math.tan, "degrees":math.degrees, "radians":math.radians, "acosh":math.acosh, "asinh":math.asinh, "atanh":math.atanh, "cosh":math.cosh, "sinh":math.sinh, "tanh":math.tanh, "erf":math.erf, "erfc":math.erfc, "gamma":math.gamma, "lgamma":math.lgamma, "pi":math.pi, "e":math.e, "tau":math.tau, "inf":math.inf, "nan":math.nan, "numpysin":numpy.sin, "numpycos":numpy.cos, "numpytan":numpy.tan, "numpyarcsin":numpy.arcsin, "numpyarccos":numpy.arccos, "numpyarctan":numpy.arctan, "numpyhypot":numpy.hypot, "numpyarctan2":numpy.arctan2, "numpydegrees":numpy.degrees, "numpyradians":numpy.radians, "numpyunwrap":numpy.unwrap, "numpydeg2rad":numpy.deg2rad, "numpyrad2deg":numpy.rad2deg, "numpysinh":numpy.sinh, "numpycosh":numpy.cosh, "numpytanh":numpy.tanh, "numpyarcsinh":numpy.arcsinh, "numpyarccosh":numpy.arccosh, "numpyarctanh":numpy.arctanh, "numpyaround":numpy.around, "numpyround_":numpy.round_, "numpyrint":numpy.rint, "numpyfix":numpy.fix, "numpyfloor":numpy.floor, "numpyceil":numpy.ceil, "numpytrunc":numpy.trunc, "numpyprod":numpy.prod, "numpysum":numpy.sum, "numpynanprod":numpy.nanprod, "numpynansum":numpy.nansum, "numpycumprod":numpy.cumprod, "numpycumsum":numpy.cumsum, "numpynancumprod":numpy.nancumprod, "numpynancumsum":numpy.nancumsum, "numpydiff":numpy.diff, "numpy.ediff1d":numpy.ediff1d, "numpygradient":numpy.gradient, "numpycross":numpy.cross, "numpytrapz":numpy.trapz, "numpyexp":numpy.exp, "numpyexpm1":numpy.expm1, "numpyexp2":numpy.exp2, "numpylog":numpy.log, "numpylog10":numpy.log10, "numpylog2":numpy.log2, "numpylog1p":numpy.log1p, "numpylogaddexp":numpy.logaddexp, "numpylogaddexp2":numpy.logaddexp2, "numpyi0":numpy.i0, "numpysinc":numpy.sinc,"numpysignbit":numpy.signbit, "numpycopysign":numpy.copysign, "numpyfrexp":numpy.frexp, "numpyldexp":numpy.ldexp, "numpynextafter":numpy.nextafter, "numpyspacing":numpy.spacing, "numpylcm":numpy.lcm, "numpygcd":numpy.gcd, "numpyadd":numpy.add, "numpyreciprocal":numpy.reciprocal, "numpypositive":numpy.positive, "numpynegative":numpy.negative, "numpymultiple":numpy.multiply, "numpydivide":numpy.divide, "numpypower":numpy.power, "numpy.subtract":numpy.subtract, "numpytrue_divide":numpy.true_divide, "numpyfloor_divide":numpy.floor_divide, "numpyfloat_power":numpy.float_power, "numpyfmod":numpy.fmod, "numpymod":numpy.mod, "numpymodf":numpy.modf, "numpyremainder":numpy.remainder, "numpydivmod":numpy.divmod, "numpyangle":numpy.angle, "numpyreal":numpy.real, "numpyimag":numpy.imag, "numpyconj":numpy.conj, "numpyconjugate":numpy.conjugate, "numpymaximum":numpy.maximum, "numpyfmax":numpy.fmax, "numpyamax":numpy.amax, "numpynanmax":numpy.nanmax, "numpyfmin":numpy.fmin, "numpyamin":numpy.amin, "numpynanmin":numpy.nanmin, "numpyconvolve":numpy.convolve, "numpyclip":numpy.clip, "numpysqrt":numpy.sqrt, "numpycbrt":numpy.cbrt, "numpysquare":numpy.square, "numpyabsolute":numpy.absolute, "numpyfabs":numpy.fabs, "numpysign":numpy.sign, "numpyheaviside":numpy.heaviside, "numpyreal_if_close":numpy.real_if_close, "numpyinterp":numpy.interp}
#stoped at FPR

parser = Parser()

def top(guild_id:str) -> tuple :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT counts, ID FROM mathematicians ORDER BY counts DESC LIMIT 10")
    tops = cursor.fetchall()
    db.close()
    return tops

def prime_top(guild_id:str) -> tuple :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT primes, ID FROM mathematicians ORDER BY counts DESC LIMIT 10")
    p_tops = cursor.fetchall()
    db.close()
    return p_tops

def top_fail(guild_id:str) -> tuple :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT fails, ID FROM mathematicians ORDER BY counts DESC LIMIT 10")
    f_tops = cursor.fetchall()
    db.close()
    return f_tops

def is_prime(n:float) -> bool: 
    n = int(n)
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False
        
def next_prime(guild_id:str) -> int :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT count from server WHERE serverID={int(guild_id)}")
    no = int(cursor.fetchone()[0])
    db.close()
    while not is_prime(no):
        no += 1
    return no
        
def init_db(guild_id:str, text_channel_id:int):
    db = sqlite3.connect(guild_id+".db")
    db.execute("CREATE TABLE server (serverID PRIMARY KEY, count_channel INT, count INT NOT NULL, fail_role INT, last_counter TEXT, high_score INT NOT NULL, base TEXT NOT NULL, fails INT NOT NULL, counts INT NOT NULL) ")
    db.execute("CREATE TABLE mathematicians (ID PRIMARY KEY, fails INT, counts INT, high_score INT, last_fail INT, last_fail_date TEXT, last_count INT, delta_fail INT, primes INT)")
    db.close()
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO server (serverID, count_channel, count, high_score, base, fails, counts) VALUES (?, ?, ?, ?, ?, ?, ?)", (int(guild_id), text_channel_id, 1, 0, "10", 0, 0))
    db.commit()
    db.close()

def user_stats(guild_id:str, mathematician:int) -> tuple :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT last_count, counts, fails, high_score, last_fail, last_fail_date, primes FROM mathematicians WHERE ID={mathematician}")
    stats = cursor.fetchone()
    db.close()
    return stats

def count_channel(guild_id:str) -> int :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT count_channel FROM server WHERE serverID={int(guild_id)}")
    channel = cursor.fetchone()
    db.close()
    return int(channel[0])

def change_count_channel(guild_id:str, text_channel_id:int):
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE server SET count_channel={int(text_channel_id)}")
    db.commit()
    db.close()

def fail_role(guild_id:str) -> int :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT fail_role FROM server WHERE serverID={int(guild_id)}")
    role_id = cursor.fetchone()[0]
    db.close()
    return role_id
    

def change_fail_role(guild_id:str, fail_role_id:int):
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE server SET fail_role={int(fail_role_id)}")
    db.commit()
    db.close()
    
def count(expression:str, guild_id:str, mathematician:int) -> tuple :
    db = sqlite3.connect(guild_id+".db")
    cursor = db.cursor()
    lzs = cursor.execute(f"SELECT ID FROM mathematicians").fetchall()
    eep = []
    for i in lzs:
        eep.append(i[0])
    if mathematician not in eep:
        cursor.execute(f"INSERT INTO mathematicians (ID, fails, counts, high_score, last_fail, last_fail_date, last_count, delta_fail, primes) VALUES ({mathematician}, 0, 0, 0, 0, 'None', 0, 0, 0)")
        db.commit()
    try:
        number = parser.parse(expression).evaluate({})
    except:
        number = 0
    try:
        number2 = eval(expression,{},meth)
    except:
        number2 = 0
    
    cursor.execute(f"SELECT count from server WHERE serverID={int(guild_id)}")
    no = int(cursor.fetchone()[0])
    cursor.execute(f"SELECT last_counter from server WHERE serverID={int(guild_id)}")
    last_math = cursor.fetchone()[0]
    last_math = int(last_math if last_math != None else 0)
    if (number == 0 and number2 == 0) :
        return (69, None)
    elif (no == number or no == number2) and not (mathematician == last_math):
        new_c = cursor.execute(f"SELECT counts from mathematicians WHERE ID={mathematician}").fetchone()[0] + 1
        new_d = cursor.execute(f"SELECT delta_fail from mathematicians WHERE ID={mathematician}").fetchone()[0] + 1
        high = cursor.execute(f"SELECT high_score from mathematicians WHERE ID={mathematician}").fetchone()[0]
        cursor.execute(f"UPDATE mathematicians SET counts={new_c}, high_score={no if no>high else high}, last_count={no}, delta_fail={new_d} WHERE ID={mathematician}")   
        cursor.execute(f"UPDATE server SET count={no+1}, last_counter={mathematician} WHERE serverID={int(guild_id)}")
        if (is_prime(number or is_prime(number2))):
            new_p = cursor.execute(f"SELECT primes from mathematicians WHERE ID={mathematician}").fetchone()[0] + 1
            cursor.execute(f"UPDATE mathematicians SET primes={new_p} WHERE ID={mathematician}")
        db.commit()
        db.close()
        return (True, (is_prime(number or is_prime(number2))))
    else:
        new_f = cursor.execute(f"SELECT fails from mathematicians WHERE ID={mathematician}").fetchone()[0] + 1
        cursor.execute(f"UPDATE mathematicians SET fails={new_f}, last_fail={no}, last_fail_date={time.time()} WHERE ID={mathematician}")
        cursor.execute(f"UPDATE server SET count=1, last_counter={mathematician} WHERE serverID={int(guild_id)}")
        db.commit()
        db.close()
        return (False, None)