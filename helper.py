import time
import math
import sqlite3

import numpy
from py_expression_eval import Parser
from word2number import w2n

meth = {"ceil": math.ceil, "comb": math.comb, "copysign": math.copysign, "fabs": math.fabs, "factorial": math.factorial,
        "floor": math.floor, "fmod": math.fmod, "frexp": math.frexp, "fsum": math.fsum, "gcd": math.gcd,
        "isclose": math.isclose, "isfinite": math.isfinite, "isinf": math.isinf, "isnan": math.isnan,
        "isqrt": math.isqrt, "ldexp": math.ldexp, "modf": math.modf, "perm": math.perm, "prod": math.prod,
        "remainder": math.remainder, "exp": math.exp, "expm1": math.expm1, "log": math.log, "log1p": math.log1p,
        "log2": math.log2, "log10": math.log10, "pow": math.pow, "sqrt": math.sqrt, "acos": math.acos,
        "asin": math.asin, "atan": math.atan, "atan2": math.atan2, "cos": math.cos, "dist": math.dist,
        "hypot": math.hypot, "sin": math.sin, "tan": math.tan, "degrees": math.degrees, "radians": math.radians,
        "acosh": math.acosh, "asinh": math.asinh, "atanh": math.atanh, "cosh": math.cosh, "sinh": math.sinh,
        "tanh": math.tanh, "erf": math.erf, "erfc": math.erfc, "gamma": math.gamma, "lgamma": math.lgamma,
        "pi": math.pi, "e": math.e, "tau": math.tau, "inf": math.inf, "nan": math.nan, "numpysin": numpy.sin,
        "numpycos": numpy.cos, "numpytan": numpy.tan, "numpyarcsin": numpy.arcsin, "numpyarccos": numpy.arccos,
        "numpyarctan": numpy.arctan, "numpyhypot": numpy.hypot, "numpyarctan2": numpy.arctan2,
        "numpydegrees": numpy.degrees, "numpyradians": numpy.radians, "numpyunwrap": numpy.unwrap,
        "numpydeg2rad": numpy.deg2rad, "numpyrad2deg": numpy.rad2deg, "numpysinh": numpy.sinh, "numpycosh": numpy.cosh,
        "numpytanh": numpy.tanh, "numpyarcsinh": numpy.arcsinh, "numpyarccosh": numpy.arccosh,
        "numpyarctanh": numpy.arctanh, "numpyaround": numpy.around, "numpyround_": numpy.round_,
        "numpyrint": numpy.rint, "numpyfix": numpy.fix, "numpyfloor": numpy.floor, "numpyceil": numpy.ceil,
        "numpytrunc": numpy.trunc, "numpyprod": numpy.prod, "numpysum": numpy.sum, "numpynanprod": numpy.nanprod,
        "numpynansum": numpy.nansum, "numpycumprod": numpy.cumprod, "numpycumsum": numpy.cumsum,
        "numpynancumprod": numpy.nancumprod, "numpynancumsum": numpy.nancumsum, "numpydiff": numpy.diff,
        "numpy.ediff1d": numpy.ediff1d, "numpygradient": numpy.gradient, "numpycross": numpy.cross,
        "numpytrapz": numpy.trapz, "numpyexp": numpy.exp, "numpyexpm1": numpy.expm1, "numpyexp2": numpy.exp2,
        "numpylog": numpy.log, "numpylog10": numpy.log10, "numpylog2": numpy.log2, "numpylog1p": numpy.log1p,
        "numpylogaddexp": numpy.logaddexp, "numpylogaddexp2": numpy.logaddexp2, "numpyi0": numpy.i0,
        "numpysinc": numpy.sinc, "numpysignbit": numpy.signbit, "numpycopysign": numpy.copysign,
        "numpyfrexp": numpy.frexp, "numpyldexp": numpy.ldexp, "numpynextafter": numpy.nextafter,
        "numpyspacing": numpy.spacing, "numpylcm": numpy.lcm, "numpygcd": numpy.gcd, "numpyadd": numpy.add,
        "numpyreciprocal": numpy.reciprocal, "numpypositive": numpy.positive, "numpynegative": numpy.negative,
        "numpymultiple": numpy.multiply, "numpydivide": numpy.divide, "numpypower": numpy.power,
        "numpy.subtract": numpy.subtract, "numpytrue_divide": numpy.true_divide,
        "numpyfloor_divide": numpy.floor_divide, "numpyfloat_power": numpy.float_power, "numpyfmod": numpy.fmod,
        "numpymod": numpy.mod, "numpymodf": numpy.modf, "numpyremainder": numpy.remainder, "numpydivmod": numpy.divmod,
        "numpyangle": numpy.angle, "numpyreal": numpy.real, "numpyimag": numpy.imag, "numpyconj": numpy.conj,
        "numpyconjugate": numpy.conjugate, "numpymaximum": numpy.maximum, "numpyfmax": numpy.fmax,
        "numpyamax": numpy.amax, "numpynanmax": numpy.nanmax, "numpyfmin": numpy.fmin, "numpyamin": numpy.amin,
        "numpynanmin": numpy.nanmin, "numpyconvolve": numpy.convolve, "numpyclip": numpy.clip, "numpysqrt": numpy.sqrt,
        "numpycbrt": numpy.cbrt, "numpysquare": numpy.square, "numpyabsolute": numpy.absolute, "numpyfabs": numpy.fabs,
        "numpysign": numpy.sign, "numpyheaviside": numpy.heaviside, "numpyreal_if_close": numpy.real_if_close,
        "numpyinterp": numpy.interp}
# stopped at FPR

parser = Parser()


def top(guild_id: str) -> tuple:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT counts, ID FROM mathematicians ORDER BY counts DESC LIMIT 10")
    tops = cursor.fetchall()
    db.close()
    return tops


def prime_top(guild_id: str) -> tuple:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT primes, ID FROM mathematicians ORDER BY primes DESC LIMIT 10")
    p_tops = cursor.fetchall()
    db.close()
    return p_tops


def top_fail(guild_id: str) -> tuple:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT fails, ID FROM mathematicians ORDER BY fails DESC LIMIT 10")
    f_tops = cursor.fetchall()
    db.close()
    return f_tops


def is_prime(n: float) -> bool:
    n = int(n)
    prime_flag = 0
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False


def next_prime(guild_id: str) -> int:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT count FROM server WHERE serverID={int(guild_id)}")
    no = int(cursor.fetchone()[0])
    db.close()
    while not is_prime(no):
        no += 1
    return no


def init_db(guild_id: str, text_channel_id: int):
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE server (serverID PRIMARY KEY, count_channel INT, count INT NOT NULL, fail_role INT, last_counter TEXT, high_score INT NOT NULL, base TEXT NOT NULL, fails INT NOT NULL, counts INT NOT NULL, primes INT NOT NULL, fail_reset_count INT, fail_reset_time INT)")
    cursor.execute(
        "CREATE TABLE mathematicians (ID PRIMARY KEY, fails INT, counts INT, high_score INT, last_fail INT, last_fail_date TEXT, last_count INT, delta_fail INT, primes INT)")
    cursor.execute(
        "INSERT INTO server (serverID, count_channel, count, high_score, base, fails, counts, primes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (int(guild_id), text_channel_id, 1, 0, "10", 0, 0, 0))
    db.commit()
    db.close()


def user_stats(guild_id: str, mathematician: int) -> tuple:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT last_count, counts, fails, high_score, last_fail, last_fail_date, primes FROM mathematicians WHERE ID={mathematician}")
    stats = cursor.fetchone()
    db.close()
    return stats


def count_channel(guild_id: str) -> int:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT count_channel FROM server WHERE serverID={int(guild_id)}")
    channel = cursor.fetchone()
    db.close()
    if channel is None:
        return None
    else:
        return int(channel[0])


def change_count_channel(guild_id: str, text_channel_id: int):
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE server SET count_channel={int(text_channel_id)}")
    db.commit()
    db.close()


def fail_role(guild_id: str) -> int:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"SELECT fail_role FROM server WHERE serverID={int(guild_id)}")
    role_id = cursor.fetchone()[0]
    db.close()
    return role_id


def change_fail_role(guild_id: str, fail_role_id: int):
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(f"UPDATE server SET fail_role={int(fail_role_id)}")
    db.commit()
    db.close()


def count(expression: str, guild_id: str, mathematician: int) -> tuple:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    lzs = cursor.execute(f"SELECT ID FROM mathematicians").fetchall()
    if (mathematician,) not in lzs:
        cursor.execute(
            f"INSERT INTO mathematicians (ID, fails, counts, high_score, last_fail, last_fail_date, last_count, delta_fail, primes) VALUES ({mathematician}, 0, 0, 0, 0, 'None', 0, 0, 0)")
        db.commit()
    try:
        number = parser.parse(expression).evaluate({})
    except:
        number = 0
    try:
        number2 = eval(expression, {}, meth)
    except:
        number2 = 0

    if len(expression.split()) == 1:
        try:
            number4 = w2n.word_to_num(expression)
        except:
            number4 = 0
    else:
        number4 = 0

    cursor.execute(f"SELECT count from server WHERE serverID={int(guild_id)}")
    no = int(cursor.fetchone()[0])
    cursor.execute(f"SELECT last_counter from server WHERE serverID={int(guild_id)}")
    last_math = cursor.fetchone()[0]
    last_math = int(last_math if last_math is not None else 0)

    if number == 0 and number2 == 0 and number4 == 0:
        return 69, None, None
    elif (no in (number, number2, number4)) and not (mathematician == last_math):
        m_count, m_delta, m_fail_date, m_high = cursor.execute(
            f"SELECT counts, delta_fail, last_fail_date, high_score from mathematicians WHERE ID={mathematician}").fetchone()
        s_delta_count, s_delta_time, s_count, s_high = cursor.execute(
            f"SELECT fail_reset_count, fail_reset_time, counts, high_score from server WHERE serverID={int(guild_id)}").fetchone()
        cursor.execute(
            f"UPDATE mathematicians SET counts={m_count + 1}, high_score={no if no > m_high else m_high}, last_count={no}, delta_fail={m_delta + 1} WHERE ID={mathematician}")
        cursor.execute(
            f"UPDATE server SET count={no + 1}, counts={s_count + 1}, last_counter={mathematician}, high_score={no + 1 if no + 1 > s_high else s_high} WHERE serverID={int(guild_id)}")
        if is_prime(number) or is_prime(number2) or is_prime(number4):
            s_prime = cursor.execute(f"SELECT primes from server WHERE serverID={int(guild_id)}").fetchone()[0]
            m_prime = cursor.execute(f"SELECT primes from mathematicians WHERE ID={mathematician}").fetchone()[0]
            cursor.execute(f"UPDATE mathematicians SET primes={m_prime + 1} WHERE ID={mathematician}")
            cursor.execute(f"UPDATE server SET primes={s_prime + 1} WHERE serverID={int(guild_id)}")
        if m_fail_date == "None" or s_delta_count is None or s_delta_time is None:
            reset = False
        elif m_delta > s_delta_count and (time.time() - float(m_fail_date)) > float(s_delta_time):
            reset = True
        else:
            reset = False
        db.commit()
        db.close()
        return True, (is_prime(number) or is_prime(number2) or is_prime(number4)), reset
    else:
        s_fail = cursor.execute(f"SELECT fails from server WHERE serverID={int(guild_id)}").fetchone()[0]
        m_fail = cursor.execute(f"SELECT fails from mathematicians WHERE ID={mathematician}").fetchone()[0]
        cursor.execute(
            f"UPDATE mathematicians SET fails={m_fail + 1}, last_fail={no}, last_fail_date={time.time()}, delta_fail=0 WHERE ID={mathematician}")
        cursor.execute(
            f"UPDATE server SET count=1, fails={s_fail + 1}, last_counter={mathematician} WHERE serverID={int(guild_id)}")
        db.commit()
        db.close()
        return False, None, None


def next(guild_id: str) -> int:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    curr = cursor.execute(f"SELECT count from server WHERE serverID={int(guild_id)}").fetchone()[0]
    db.close()
    return curr


def set_frrc(guild_id: int, counts: int, time: int):
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE server SET fail_reset_count={counts}, fail_reset_time={time} WHERE serverID={int(guild_id)}")
    db.commit()
    db.close()


def server_stats(guild_id: str) -> tuple:
    db = sqlite3.connect(guild_id + ".db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT counts, primes, fails, high_score, fail_role, fail_reset_count, fail_reset_time FROM server")
    stats = cursor.fetchone()
    db.close()
    return stats
