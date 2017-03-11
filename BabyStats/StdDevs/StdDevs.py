
import math

def phi(sigma):
    # sigma is your standard deviation
    # sigma = 3.0
    # 4.891639 sigma is (basically) 1 in a million
    sampleSize = (1./ (math.erfc(sigma/sqrt(2))))
    # "80 billion 'events' in an day at Intel..."
    msg = '1 in a', sampleSize, 'or ', 80e9/sampleSize, ' for an IntelDay'
    return (print(msg))
