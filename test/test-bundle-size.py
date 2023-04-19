"""
To be run on MicroPython.

Tests RAM usage of (de)-serialization of different payload bundles.
"""
import gc
print("free: {}, used: {}".format(gc.mem_free(), gc.mem_alloc()))  # this should always be over 100000
from py_dtn7 import Bundle
print("free: {}, used: {}".format(gc.mem_free(), gc.mem_alloc()))
gc.collect()
print("free: {}, used: {}".format(gc.mem_free(), gc.mem_alloc()))


raw_bundle = b'\x9f\x88\x07\x1a\x00\x02\x00\x04\x00\x82\x01l//node1/ping\x82\x01h//node1/\x82\x01h//node1/\x82\x1b\x00\x00\x00\xa8\xb0R\x18\xb8\x00\x1a\x006\xee\x80\x85\n\x02\x00\x00D\x82\x18 \x00\x85\x01\x01\x00\x00X@LwL2KMBGNgy11Y8Ofa4EYfDultcE7Ulq7b3veSMSKgzvSjDbO0aRVxQYwMInIR4g\xff'

raw_cat_bundle = b'\x9f\x88\x07\x1a\x00\x02\x00\x04\x00\x82\x01l//node1/ping\x82\x01h//node1/\x82\x01h//node1/\x82\x1b\x00\x00\x00\xa8\xb0R\x18\xb8\x00\x1a\x006\xee\x80\x85\n\x02\x00\x00D\x82\x18 \x00\x85\x01\x01\x00\x00Y\x11\xc8\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00IIIIMIR[[Rr{m{r\xa8\x9a\x8d\x8d\x9a\xa8\xfe\xb6\xc3\xb6\xc3\xb6\xfe\xff\xf1\xff\xf1\xf1\xff\xf1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01IIIIMIR[[Rr{m{r\xa8\x9a\x8d\x8d\x9a\xa8\xfe\xb6\xc3\xb6\xc3\xb6\xfe\xff\xf1\xff\xf1\xf1\xff\xf1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc2\x00\x11\x08\x01\x94\x02d\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x18\x00\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\xff\xda\x00\x08\x01\x01\x00\x00\x00\x00\xf4\x01<\xbee\x88/oW@\x00\x14\x02\x06<8\x00:\xfa\xfa\x00\x00\'/\x14\xb1\x01}^\x9a\x00\x05\x10s\xe6N\x18E\x80\xd7\xa7\xb6\xa8\x00\x04\x9e.@\x81zw\xednqu\xaa\x00L\xe71f9\xcc\x10/~\xb7z\xa0\x00\x13\x8f\x88\x00F\xfa\xef-o[\x8bh\x89$\x0c\xf2\xce$\x82\xde\xfa\xbdv\x00\x00\x93\xcd\xe6X\x00\xde\xfb-\xaa\x14\xa9\x10\x99\xd6y\xb1\x9c\xc1\xadw\xeb\xab@\x00\x0c\xe3\xcf\xc0\x02\xe9\xae\xbbZ\xb2*\xe6\xcd\xe36\xa6e\xcc\xces\x98j\xf7\xec\xe9@\x00\x04\xcf\x1e\x1c\xec"\xea\xea\xf4\xd2\xd4.Z\xc6\xf9\xf5\xc4,\xcd\xb9\xces\x9c\x8dk\xbf{\xa0\x00\x01\x13<\xfc\xd2H7n\xf7m\x92h\xcbY\xd6SL\xa2\xd6s0\xc8\xd7n\xba\xdd\xa0\x00\x06d\xce|\xcc\xe4]\xeb[\xd2\xcc\xe3z\xcck\x1a\x99\x9d/;\x96\xac3q2\xba\xed\xd5w@\x00\t\x12q\xf3\xe6\x17z\xdbUf3\xa8]s\xd4\xcbw\x11m\x94\x96jGn\xb1\xaa\x81@\x04&y\xf9\xb1\x17\xae\xf5Hff\x16\xeb\x9e\x99i%\xabi\xabd\xac\xeb\xad\xb6\x02\x80\t$\xc6y\xf2-\xed\xb8\xcce$\x91\xb9*72\xb6\xb4\xd5hF:n\xda\x82\xa8\x00\x893\x9cbt\xb3l\xcc\xc8\x92$\xdc\x84\xbb\xcc\xb6\xb4kMK9o\xd1\xa4\x96!m\x00\x04g\x965\xab*g9\x88\x92I\xa2%\xb2\xe9m\x95\xb5\xaex\xf5u$ [@\x02N9\xce\xb7Q1\x94\x88\x92E\x95)t\xd5\x85j\xd9\x96z\xf6\xd2B\x16\xd5\x00$\xc3\\8\xf5\xe9\x19\x99\x88\x19\xca,k:\xcbV\xea\xc9ih\x93]\xf5\x11\x0b\xab@\x01\x8b\xcb\xcf\xad\xd4\xccDY\x98\x92h\xe9\x9c\xcbkh\xa2\xad\rt\xa4\x16\xea\x80\x04s\xe0\xd5L\xe4%fd\x93[\xdcs\xcd\xa6\xd4\xa4Z\xab7\xb1\r](\x00\xce9\x153\x98\x11fa&\xfa\xeb\x1d|\xa2]\xa2\xd1V\x94\xde\x81\xab\xa5\x00&8\xa93\x99\x0b\x12\xcc\x89:\xf6\xa7\x9a\t\xaa\xaaCM\x06\xf6\r](\x019\xf2X\xced\x02&A\xdf\xb9\x9e\x1c\xd0\xda\x84\x8bm\xa3\xa6\xa8\xb6\xe9@\t\xcb\x08\x99\xceb\xd1\x13!\xae\xfe\x8d\xe2\xf9y`n\x92\xcb\x82\xdbt\xbb\xda\xc5\xb7J\x00N\\\xd13\x9c\x94\xb6D\x90\xbe\xafV\xa6|\\\xa4\xb4]\xeag\x9c\x1a\xd5\xdd\xd6\xb4\x17V\x80\x0c\xf3\xc4fg27l\x98\xa2E\xf6z\xab\x1e?9f\xfa\xe7[q\xc6j]n\xdb\xadQm\xb4\x00\x93\x9efs\x89\x98\xba\xdd\xea\xc7W.\x0c\xd7\xaf\xd9\\\xbc|eu\xef\xa6s\xcac55\xbbn\xb5t\x8bm\xa0\x04\x98\xc4\xcefs,on\xbd\x13\x97,\xc9\xaf_\xa7S\x1eo65\xbbw\xac\xe6s\x90\xb7v\xebwVE\xb6\xd0\x02fba\x9c3\x15\xae\x85\x89\x9c;z\xb7\xa99\xf9\xb8/EFr\x85\xd6\xf4\xd6\xf4\xa8[h\x011\x139\xceq\x05j\x88\xcez\xfa:\xf439\xf8\xf3kQ\x11\x0bwn\xb5\xab\xa4\x96\xd5\x00&s.s\x9cg-b\xdbe\x88\xbe\xae\xd9\xe9S3\x8f\x91\xa1Q\x99Z\xd5\xb7[\xba\xb2-\xaa\x00e\x98\x98\xces\x996\x827\x1d\xbd5FN\x1ex\x85\xd6Ke\xdd\xba\xdd\xa8[h\x00bFfs\x8c\xc2\xead\xd2\xef\xbf@\x89\x8e\xae\x1c\xf3\x99nm\xde&\xadk\xa5T[U@\x132&q&p\x1a\xb9\xd6\xb7\xd7\xad\xc7\x9e\xba1\xcezw\x9c\xe11I*\xe8\xb6\x81h\xe8\x01"Dc13\x08\xdb}\xf7\xb6x\xf2\xc7G=\xf6\xe8\x9a\x87&nu4\xcem\xaa\x82\xa9\xd0\x04\x11\x19\x9c\xf3&b\xed\xad\xf5\xe9\xa5\x939\xe7:n\xdc4g8\xcdi\x0c\xda\xa4\x15N\x80 \x91.s\x8c\xc4j\xed\xbe\x9a\xd4\xb2I\x8c\xefT\xcd\xcb,\xa4\xb6UR\x02\xa9\xd0\x06f\x89\x913\x94\x91W}\xf4&s\x85\x8d\xe94e.\x18\x16\xa8 \xaa\xe8\x02gZ\x93(g9\xcc.\xee\xfa\xd1\x9c\xe7ZI\x9d[br\x90j\x96\xd0\x90Z\xba\x00\xce.\xad\x92I#8:N\x9d4g\x12\xd2\x91\xba\xb9\xe1.u\xbbB\xd31\x0bj\x80\x98\xa5\xa4\x82H\x9c\xf7\xad\xe8\xcf>\x96\xa5&oD\xe7\x9c5v[A\x96b\xd5\xb4\t\x9c\xea\xe8!\x14\x9c\x8c^\xba\x98\xd6\xb4F\xa33Vc,\xddn\xac\x8dY\x98\xc8\xb5t\t\x9eZ\xde\xaaU \x13\x96u5kJ\x8dD$\x91\xb5TT#\x11Kn\x811\xce\xebZ\xdaE!i\x98\x90Y\xa4\xa0\x1a\n\x88T\x92H\x0bv"q\x97{\xdd\x90[\x93U\x04\xcc\x82\xa5)mR\x19J\x96fdJ\xb5\xd0\x93\x1c\xe5\xd6\xf4h\x14Z\x94\x89 \x94\xb5T\x12Y\x99S53\x0b-^\x84\xc7<\xda\xb7z*\xa2\xa9e\t \xd4i(E\x8b1%\x91q\x92\x8b]L\xe3\x9en\x8d][V\x90\x9a\xa0\x12\xc5\x00#P\x98\x913.EYk\xaaLbJ\xd5\xba-n\xc2M\x014Q,"\xa4j\xc8\xe7\x98\xceT\xa0[\xd13\x89"\xdb\xb3y\x97z\x9a\x85\x88F\xa8\xa8!\x05\xa93\xca\x0c\xd6\x90E]i$k\x91\xab\xab%j75\x9d$\x1b\x84\xd1,\x92Z\xaabs\xc4\x03QD/D\xc0\x92\xb5l\xb4\xa5\x15\x81\xabfn\xcc\x8b\x95\xb5d\xc6q\x86\xb1\xa8\xb5\x9dX\x0e\xf9\xc6\x05\xa3B\xaeuP\xb9h\x95\x99\xba\xcbSIm\x96\xf3c\x19Y,\xba\x99\xd6\xb0\x15\xff\xc4\x00\x16\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\xff\xda\x00\x08\x01\x02\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04P@P\x00\x00@\x00\x94\xa0\x00\x01\x00\x00\x14\x00\x00 \x00\x00\xa0\x00\x08\x00\x00\n\x00\x01\x00\x00\x02\x80\x00@\x00\x00\x14\x00\x08\x00T\x00\x14\x00 \x01D\x00\x05\x00\x80\n\x02\x00\x94\xa0\x10\x14\x8a\x11H\x12\xa8\x02\x01\xa2\x00\xa9\x00P\x04\x00( \x01@\x08\x14\x85\x04\x00\x95@\x10\x01HP P\x02\x00Q\x14\x02\x14\x00 \n\x00\x08P\x00 \x14\x00@\xa0\x00 (\x01\x02\x91@\x8a\x00\x00\x00AB\x14E\x00\x00 \x14\x80\xa0\x00\x01\x00\x15\x00P\x00\x02\x00*\x00\x02\x80\x08\x00X\x00\x01R\x82\x12\x80\xff\xc4\x00\x16\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\xff\xda\x00\x08\x01\x03\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05@P@\x00\x00P\x00\x08\xb0\x00\x00\xa0\x01a\x16\x00\x00(\x00\x00\x80\x00\x05\x00\x00\x08\x00\x01@\x00\x02\x00\x00P\x00\x00\x10\x00\n\x00\x85\x00\x10\x00(\x01\x05\x00\x10\x00\xa0\x08\x02\x81R\x00\x14\x00\x81H\xa2\xa4\x00(\x12(,\x14S \x05\x00 (\n\x90\x00\xa1\x14EE\x01R\x00\x16\xa0\x02\x99\x02\x84\x00(\x04.\x99\x80)\x00\x02\x80\x85\xa8\x80\xa4\x00\x02\x81\x14\x10\xa0\x80\x00(\x00\x00!`\n\x82\xa0\x00P\x02\x02\x90T\x00\x00\xa0 \xa0\x80\x00\x01@A@AH\x00U@"\x80\x00E\x11T@J)\x00\x00\x05\x08\x0f\xff\xc4\x00/\x10\x00\x02\x02\x01\x03\x03\x03\x02\x06\x02\x03\x01\x00\x00\x00\x00\x00\x01\x02\x11\x10\x12 !01A\x03@Qaq\x13"2BR\x81b\x91#P\xa1\xd1\xff\xda\x00\x08\x01\x01\x00\x01?\x00\xe8z\xd1\xe9&\xd1\x1fY\xa2\x13R\xf7\xf3\x9a\x8999>\xa4\x11\x1fi>P\xd5>\x9am\x10\xf5\x84\xd3\xf6\xf6Jt~#\x1c\xd8\xa6\xe8\x94\xd9&\xdfR*\xd9\x15BK\xda4z\xb1\xa7\xd5\x8f\xa8\xe2/Y\x1a\xd0\xa4\x98\xdaF\xb4?PS\x14\x84\xfa\x966X\xd5\x9aJ\x12\xe0Hq$\x86\xb8\xe9zQCbf\xa1{?V6\x86\xab\xac\x9b\xa2\x13cm\x8a\xd9\xa4HB,\xb2\xcb/e\xf4Q\xe4\x90\xc6\x86\xb9\xde\xb0\x8a\x15\x91^\xd1\xa3\xd4\x80\xd5uZ\xe0\x8a\x1a\xe0\xae\x11Et,\xb2\xf3e\x8cye\x8d\x8d\x8f\xbe\x1f}\xe8K\x92(I\n\xbd\xb3\x898t\xe8H\xf8"<\xac\xb2\xf0\xdf\x04Ye\x8c\xd5\xce\x18\xdf%\x97\x8b/\x08c,l{\x91\x08\n"\x13^\xd9\xb2V\xc9G\x15\xb9lB\x18\xb0\x86\xc6\xf6I\x88b|\xe1\xbeK\xe0\xbc\xa6x\x1e>1\xdd\x92c\xe2\x96\x1e\xe4E\xb15\xe7\xdc\xb4J)\x92\x8d\x08kj\xc2\x16#\x84<X\xde\xe7\xd8\xb2\xc9\x17\xc0\x9d\xb1\x0f\x1e\x19xX\xec.YV\xc6\x86\x9b+j\x8c\x99\x195\xe0R\x8b5P\xa4_\xb6vQ(\xd8\xe2\xe2\xc7\xbda\x0bk\x18\x9e,g\xc6\x1fv!\xf9\x13<\x89\x8b\xb9|\x9e1\xe0]\xb3\xdb\x14\xe4\xc7H\xab\x1b\xf0\x8a(\xa16\x88\xbf\x98\x95\x17\xe0R\xc2\xf6\xed,z\x8a\xd0\xc7\x9a\x12\x12\x14D\x8a\xde\xc4\xc7"\xf1\xe5!\x0c\xec\x86\xcf(}\xc8\xf7\x13\xe3\x16x\xc2\xcf\x92\xac\xbf\x08\xd2}\x10\xa0~\x1a\x1cD\xda\x14\x88\xbbgb\x93;p/p\xc9Y-\x89\xb4E_1\x12^\n;\xad\x8cLom\x96#W\x03,\xf2\'\x84X\xcf(]\xc4,\xa1\xf0\x85\xc1BU\x86T\x98\xa3CQ+\x91M\xa1I1\xa1{m_A\xb9\x1f\x9d\x8e\x0f\xe4pc\x8b(\xd0i\x7f\x02^Q\x17{\x9fEe2\xc7\x85\xdb\x0cX\xf0\xb0\xbc\x88\xbe\xc7\x91,-\x8d\x94\xcam\xf7\x14\x11\xa4M\x8b\xdbP\xceGe1\xc6\xc7\x03D\x84\xda\xee\x87\x18\xb3KYx\xbe\xf9X{o)\xe6\xf1xB\xec,.\xf8]\xcf"y\xef\x86\xcd\\\x91NB\x82Yh^\xe5\x92\x9f\x84&\xfc\x96&\x86\x8a\xf8\x10\xf0\xcb\xdc\xf2\xf0\x9eVP\xdf\x02\xc2\xee!a\xec\xf0!\xe6bDd\xbd\xf4\x9d\xf0\x8a;\nG\x1b,\xb1\xbd\xff\x00;\x90\xc4w\xbc\xc8G\x91y\xfb\x0b\xa3e\x96w\x18\x9bD}AI?w!B\x8aH\x9b\x8e"\xd9x\xbe\x8b\x17m\x8f/\x15P\xfb\xb1\x08x}\xc5\xe7\xed\x84\xac|\xe5l\xb1\xbcV(h\x8b\xa1?u\\\xde\'#\x96\xc4\x84\xb2\xd8\xde^>\x83<\x0fk\xc2\xc5\rp5O\xec-\x8b\xb3\xc7d\xb0\xf0\xb7\xde(\xa5\x84\xc4\xfd\xd4\xe4;b+c{\x13_\'\x08\xfe\xca\xb4.\xd4=\x8f+\xbaBB_\x9d\xb1\xf6+\xf53\xb4^\xcf\x02\x1b\xb7e\x1c\x16\xbe\x11k\xe0\xe0\xe0\xaf\xaa\xc5\x8b\x16-\x89\x97\xed\xd8\xe5Cv%\xb5\x8d\x96\xf7.0\xf7\xc0\xa4\x90\xad\xc5\xfc\xb2Q$\xb8\xa2B\xd8\x8b\xaf\xbe/m\x96^8\xdc\x85\xed\xe4;\xdc\xcb\xdbY\xbe\x8f\xa4\xae\xc6\xb8\x97\xd9\x11\xe2\r\xbf\x04#\xf9\xa3\xf4X\x99\xe1m]\x1b,M\xe1R/6/o!\xe2\xd6/u\xef{\xfd#\xff\x00\xa9\t\\\x17\xd6C\xf3/\x96Sm\xc4\xf5Q\xfbv\xa5\xb1\x97\x86_E\x0b\xdb\xcbs\xd9LI\xee\xad\xe9Y\xe9r\xc4\x96\xa7\xf4hJ\xb4\x92\x8d\xb4\x8f,\xf5\x1f\xe6g\x87\xb5Y\xc1E\x97\x86\x8a\x19e\x96Z/\x0b+\xdb1\xe5\x8b\x0fu\x97\x8a\x1f\x19\xa2\xb6\xfa\x02]\xfe\xaf\x15\xdcg\xab\xfa\xd9\xe1o\xd5BV(\x8a$\xd0\xf8\xcdl\xa6S++\xda\xb1\xedl\xbc\xd8\x844i\xb3H\xd3F\xa6s\xf0Z/j=\r\x92\xecz\xabta)\x9f\x80O\xd2\xe3\x820\xa4Q\xca\x1b\xb6<V)\x89\x0b\x0b\x08\xe0^\xd5\x8f/\x17Lv\xb7.H\xba\xe0\xa3J\x1f\xa5r\xb1Dp\x83\xee\x89z+\xc3\x1cZyH\xf3\xc9\xe9J\x85\x99\x93\xbe\x16P\x93=4\x97tYxct96?\xa6\xe4"\xb2\x8a\xf6\xecxxh\xfa1\xa6\xb6\xa6w\x13q#$\xf2\xd8\xe4;c\x1e\x12\x94\x8fN4\xd8\xb3"V5M\xd7\xce,K\xb3\x1f\x02m\nF\xb1\xb6\xcf\xb8\xda\x1e\xfb\xe0BG\x02e{f1\xa1\xacP\xd0\xcb]\x98\xd3[Q\xe0\xa4\x7fe\xcb\xe5\xe3\xc0\xfbf*\xd9\x06!\x16^%\x1b\'\x1a\x93\xb3\xb3\xc7)\x8d\x8b\x16Yc,\xec\xb3\xc6\x10\xb2\x85\xed\xde\xca\x1a\xc3\x1a\x13\xf0\xfb\r5\xf6\xc53\x8c&\xde\xf6\xf8\xc4\x13\xa20\xa1lx\x9clpj\xf0\xf7<w\x1b\xfaf\x8a\x12\xd8\xb2\xbd\xab\xd8\xc7\x87yM\xa3J\x971\xff\x00G%\xbcY\xcdv9\xc3x\x91\\\x1c\xf1\xc1\x04\xd9\xe0\x88\x9e^\x19\xea.\x07\x1c\'\x9b/\x1c\x8e\x92\xa3\x9d\x8a\x1e_\x08\xfa.\x10\x92Y^\xe6\x8a\xc3\x1a\xc3\xdbj\\K\xfd\x8e\r}Q\xc9e\xbb\x1eP\xf9\x12 \xbcP\xad,%\xc6,\xbc\xd8\xd2d\xe05\xb5<q\x1f\xbe\x17\xdb\n\r\x97\x18\xf6\xe5\x96\xdb\xe7<a{\x87\xba\xd0\xc6=\x89\xca/\x86~I\x7f\x8b\x1aq\xee\xb0\x9a\xec\xfb\r4#\x91&%"\nE\xe2\xcb,\xb2\xcb5P\x9d\x8c\x94G\x1f\xa1\xa0pf\x96(6v\xe2&\x96S\x14d\xfc\x15\x18\xff\x00\x93\x1e\xa9w)\x8a,J\xb1BB\xd9e\xe2\xcb-\x16\x8bE\xae\x9d\xedc\x1eZ\x1d\x1clSk\x8f\x1f\x06\x98K\xf4\xff\x00\xa6U:h_\x0f\xb1\xa6\x85\x14\xc8\xc1/"\x82\xf8O\x12C\x9b\x83\x1f\xab\x1e\x05\xea\xc5\xba,L\x9f\xa8\xa2/UY\xcc\xd9\x08\xb4\x86P\xd2(I\xcb\xb1\xa7\xe1X\xf9\x14[\xec\x8aK\xbc\x8bK\xb2\x1bo\xbb\xc53\x8c%\xff\x00CM\x8e\x1fT\x8a\x8f\xcb-x\x81\xa9\xfcG\xfd\x0f\xd4\xf5>O\xc5\x99\xady\x84O\xf8\xbf\xca&\x86\xfbI1\xa6\x8a/\xc4\x95\x94\xbc1\x11DsVN\x1a\x87\xe8\x8f\xd2\xa3\x9a/\x81CT\x98\xbd\x120HH\x92\xa2)6Ti\xbd&\x85J\xd3dc\xa5\xc9x\xa2:\x12\x95&T\\d\xd2\xe5\x12\x8f\x8f\xf1\x1aQQ\xe1\x15\x05=4/\xa4[e~h\xf8\xb4&\x9a\x93\xd2\x8d\x15KE\x9a+W\x16\xc7\xf4U\xef\xa9|\x9c/\x05\x8e\xc6\x86\xb3[4\x8aR\xfb\xa2\xd7\xd5\x14\xc8\xa5\xf5\x14D\xb3ea\xa1\xa2Q#\x1b\x12)\x1cbD;\x8f\xf3y-4\xb9\xa15o\x914\x9c\x95\x9e\x9f\x13hrNSvK\xf6\xfd\x86\xd6\xbb;\xc6\x84\xb9\x8f\x0e\x92+W\x1a\x87\xa6\\\xea*?$\x9au\xc9^\xe6\xfa\r\x0ck\r%\xe4\xd2\xdfh\xb68O\xf83G\xa9\xfc$(z\xbf\xc5\x9ag\xfc\x18\xa35\xfbYMx\x90\x9f\xd1\x89\x8bm\x97\x86\xc8\xb2-\xd7;$+\xbe\x06\xe5\x96\xbe\x86\xbd<\x16\x8b-\xff\x00\x99\xfd1:|#[\xc7?\x07\xf5\xbe\xd7\xb2{Z\xdc\xd2)\x1c\xae\xd2\x8a\x1a\x93\xee\xff\x00\xf4\xd1\xf5F\x95\xfc\xa2T?\x90\xb4\x7f&q\xfblN_,W\xfc\x88\xad\x8f-\x8eBV8\xa2\xd8\xa4Z\xc4\x84&\x97\x91\xb4Z\xf98\xae\xe3\x94II|\xf1\xc8\xed&\xf5\x1a\xd7\xf25\xd2\xfdV\xc6\xed\xf7-\xfc\xb2\xdfJ\xbd\x8b\xcd\x15\xd2w\x8a(\xa1,-\xcd\x8d\x89\x15\x9aE\x15BeY\xa4\xd2i4\x8d\x15}\x8a~\x1a\x7f\xf8\xce<\xa7\x13O\xc4\x934M~\xd6.Je\x14QE\x14i4\x9a\r&\x92\x8a(\xa2\x8a(\xae\x93\xa3Q\xa8\xd4^\xca+\x15\x8d#C,H\xd0\xeb\x96\x928]\xb9"\x9f\x7f\x02\xcd\x8c\xb3\xbfE<\xde8$\xa8s\xf15bo\xc3\xd4\xbe\x19P~\x1cE\t.S52\xd7\xc1H\xa2\xb7Y\xa8\xb2\xcb\xf6\x0c\xa2\x8d%f\x8a\xcdf\x8d\'\xe1\xbf<#Z\x8f\xe8Cm\xbbdb\xbb\xb1\xc9\x89\x9a\xbf\xd1\xce\x1b9\x93\xc5P\x96h\xac1\xaf"x\xab\xc4\x99k\xcf\xe9c\x8e\x97\xc9K\xc1\xaa\xfb\xab\x14|\xa2\xfey)\x14\xd6-\xe3\x8fn\xd9b\xb2\x8a\xcd\x97\x8a\xdbG\xd8j\xc7\x11*\xe5\x8f\xb5\xc8\xb6\xdd\x96vi|\x1a\xb8\xfe\xc6\xf0\x90\xba\x89\xf6\x1b\xa6<v\xfb\x0e"BX\xac\xb5\xb9\x96_\xb0c\x10\xb6Q[\xab\x15\x9a\x1cm\xdb%\x16\xd9\xa4\x8a\xe5\x1d\xdb<D\xf1\x86,\xbc-\xade\xf2\x8am\x14$\xd1E\x14V\xfb,\xbc\xff\x00^\xc2L\xb1\x08\xb3\xb8\x96\xdb\xdc\xb3CF\x92\xb8e\x0f\xc6|\x9e\x0f\x8e\xa5b\x8a+\xaf}v2\xd6R\x11e\x97\xec\x18\xd1]Z+\xa6\xf6&X\xdb\xd9\xfd\xe6\xbam\x8eO)\x88\xb4j9b^\xce\x8a\xd9X\xa2\x8a\x12(\xa1.\x9b\xd9g\x18N\xcb/\xae\xc6\xf6\xf3\x84^\xd4\x87\xec+uu+(y\xb2\xc7\x85C\x1d\xee}\x16\x87\x9a[\x13\xdc\xb1C[/\xa9E\x15\xd6YC\xc5\xe1\x16\x87X\xf0\xc6\xf1]K\x1b\x1e,\xb2\xf6\xd9\xdf\x16\'\x85\xb1\x89m\xbcX\xbd\xb3\xc3\x18\xcb\x13\xe5\x1f\x98xWh\xe5m\xb3\x81\x8b6\xb0\xda\x1bC\xd9X\xb1Y[\x96.\x90\x9e\xc5\xb2\xf6/od\x99\xa9\xf9G%\x96I\xf2\xcb\xc5!\xa5ef\xf6-\x9ax\x1e\x92\xa3\x7f\xd0\x92hj<\xf1\xd9\x95\x1bf\x8e\xfb;a\x1c"\xf1Yb\xcbbe\xe2\xf1x\xef\xb6\xfa6^\xc5\xb1\xbc6]\x17\x86\xe8k\x96V[|\x17\xd2\xa6r\x87&93S\xaa\x1c\x9b53S\xdd{/,[\xaco\x0b\x17E\x9666"\xf1e\x96_Aa\x8f\x12\x1b\xa5\xb2C\xe1\xb2\xcbX\xf8\xcd\xbcYy\xb2\xf0\xc7\xd2\xf1\xb5t\x9b\x11\xe3,Ce\xf3\x85\x8b\x1btG\xa8\xc6_\x0cL{\x12\x1f-\xe1a\xf6C\xee!\x16\xd8\x87\xb2\x8f\xff\xc4\x00\x16\x11\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11P\x90\xff\xda\x00\x08\x01\x02\x01\x01?\x00jn\x0f\xff\xc4\x00\x19\x11\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x11P\x80\x90\xff\xda\x00\x08\x01\x03\x01\x01?\x00\xe2\xdc\xc3\xd1\x0c\xba\xe3\xff\xd9\xff'

actual_bundle_size = len(bytearray(raw_cat_bundle))
print("\nactual bytearray length (actual size of bundle): {}".format(actual_bundle_size))

gc.collect()
before = gc.mem_free()
bundle = Bundle.from_cbor(raw_cat_bundle)
after = gc.mem_free()
gc.collect()
after_collect = gc.mem_free()

deserialized_bundle_size = before-after_collect
print("\ndeserialized bundle:")
print("free before: {}, object size without collect: {}, object size with collect: {}, garbage collected: {}".format(before, before-after, deserialized_bundle_size, after_collect-after))

gc.collect()
before = gc.mem_free()
bundle_bytes = bundle.to_cbor()
after = gc.mem_free()
gc.collect()
after_collect = gc.mem_free()

serialized_bundle_size = before-after_collect
print("\nbundle bytes:")
print("free before: {}, object size without collect: {}, object size with collect: {}, garbage collected: {}".format(before, before-after, serialized_bundle_size, after_collect-after))


print("\nbundle_bytes length (actual size of again serialized bundle): {}".format(len(bytearray(bundle_bytes))))


print("\nthis show (garbage collected) that compared to the actual size that factors are: serialized bundle -> {}, deserialized bundle -> {}\n".format(serialized_bundle_size/actual_bundle_size, deserialized_bundle_size/actual_bundle_size))

