import hashlib
def md5(str):
    md = hashlib.md5(str.encode())
    md5pwd = md.hexdigest()
    return md5pwd
MD5_SUFFIX = "FDSW$t34tregt5tO&$(#RHuyoyiUYE*&OI$HRLuy87odlfh是个风格热腾腾)"