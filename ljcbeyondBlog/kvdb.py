# coding=utf-8
'''
用于存取一些key-value数据，本机用redis(待补全配置)，sae用kvdb
'''
try:
    import sae.kvdb as kv
    kv = sae.kvdb.KVClient()
except ImportError:
    import redis as kv
