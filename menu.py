#Encrypt by Ikz
#Queue206Ikz
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
