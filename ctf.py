import flask
import html
from flask import Flask, request, jsonify
# from js_random import check_from_seed

app = Flask(__name__)

@app.route("/game-1/a")
def homef():
    return """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>ctf</title>
    <script>window.history.pushState(" ", " ", "/game-1/");</script>
  </head>
  <body>
    <center><h1> Find the flag </h1></center>
  </body>
</html>"""



@app.route("/game-1/")
def home():
    # 98849333-1d1f-439b-871c-3ca843097cc3
    resp = flask.Response("CTF: 98849333-1d1f-439b-871c-3ca843097cc3", status=302)
    resp.headers['Location'] = "/game-1/a"
    return resp


@app.route("/game-2/", methods=["GET", "POST"])
def game2():
    # bf3d486c-9877-44eb-b7c1-ccc6f9ffd248
    if request.method == "POST":
        if "admin" == request.form.get("user_type"):
            return "<center><h1>CTF: bf3d486c-9877-44eb-b7c1-ccc6f9ffd248</h1></center>"
        if request.form.get("username") is None:
            return "hmm you found a easter egg"
        else:
            return "<center><h1>Hi " + html.escape(request.form.get("username")) + "</h1></center>"
    return """<!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Register CTF Game</title>
      </head>
      <body>
          <center>
                <form method="post">
                    <label for="uname"><b>Username</b></label>
                    <br>
                    <input type="text" placeholder="Enter Username" name="username" required>
                    <br>
                    <label for="psw"><b>Password</b></label>
                    <br>
                    <input type="password" placeholder="Enter Password" name="psw" required>
                    <br>
                    <button type="submit">Register</button>
                    <input type="hidden" name="user_type" value="user">
                </form>
          </center>
      </body>
    </html>
    """



@app.route("/game-3/", methods=["GET", "POST"])
def game3():
    if request.method == "POST":
        if request.form.get("username") is None:
            return "hmm you found a easter egg"
        else:
            # 8684c0f7-d4e5-4cc8-9949-64b1193ab8b2
            # raw js | if (document.getElementById("username").children.length > 0) {document.getElementById("username").innerHTML = "CTF: 8684c0f7-d4e5-4cc8-9949-64b1193ab8b2"}
            keyjs = """
            (function(_0x5b8a2d,_0x130e47){function _0x5d3256(_0x541c17,_0x3737de,_0x4f1089,_0x4d35dc,_0x210e61){return _0x3497(_0x541c17-0x86,_0x210e61);}function _0x425205(_0x501ac2,_0x2bbf2c,_0x4e557a,_0x706fde,_0x1a4d6d){return _0x3497(_0x706fde-'0x6e',_0x4e557a);}function _0x1a9379(_0x352cd7,_0x334599,_0x327279,_0x5e6b67,_0x2dce77){return _0x234b(_0x2dce77-'0x2b3',_0x334599);}function _0x2815c9(_0x359d1f,_0x5326b8,_0x4f20b4,_0x3c04f5,_0x297ca9){return _0x234b(_0x359d1f-0x2f6,_0x3c04f5);}function _0x3884a6(_0x45cb15,_0xb5fe79,_0x4ae8ee,_0x315c06,_0x1db5ed){return _0x3497(_0xb5fe79-0x2f1,_0x45cb15);}function _0x51227a(_0x44c234,_0x1dc175,_0x59db1a,_0x28fb5a,_0xad2b5a){return _0x3497(_0x28fb5a- -0x4b,_0x59db1a);}function _0x405ece(_0x5501d3,_0x4c39e2,_0x3bdd3e,_0x59863f,_0x5231ca){return _0x3497(_0x59863f- -0x342,_0x5231ca);}function _0x463a2b(_0x269869,_0x5543b0,_0x52a3e4,_0x339244,_0x2803db){return _0x234b(_0x52a3e4-0x1fd,_0x339244);}var _0x25933c=_0x5b8a2d();function _0x386e79(_0x4a5316,_0x5f1d63,_0x14a7ef,_0x39e6c0,_0x76da04){return _0x234b(_0x4a5316-0x2c8,_0x14a7ef);}while(!![]){try{var _0x16aaa3=-parseInt(_0x1a9379(0x3d5,'0x3d1',0x426,'0x3fd','0x3f9'))/(-0x1cb4+-0x5*-0x6e7+-0x5ce)*(-parseInt(_0x3884a6('WB%T',0x448,0x3ff,'0x441','0x493'))/(-0x56*-0x34+0x1c80+-0x2df6))+-parseInt(_0x3884a6('Vp83','0x453','0x46f',0x489,0x435))/(0x22f9+-0x19*0xb3+-0x117b*0x1)+parseInt(_0x3884a6('lFpT',0x488,0x4a7,'0x489',0x49d))/(0x2435+0x11d+-0x2*0x12a7)*(-parseInt(_0x1a9379(0x416,0x3fb,0x455,'0x440',0x440))/(0x6*0x37c+-0x1bca+-0x1f*-0x39))+-parseInt(_0x3884a6('mJk^',0x421,0x446,0x461,0x409))/(0x123a*-0x1+-0xb2b+-0x11*-0x1bb)*(-parseInt(_0x425205('0x1db','0x1c7','jtjB','0x1ed','0x242'))/(0x1039+0x1*-0x2207+0x11d5))+-parseInt(_0x5d3256('0x20c',0x24f,'0x1d7','0x1f4','3S##'))/(0x1161+0x11*-0x2+0x1*-0x1137)*(parseInt(_0x2815c9('0x498',0x48f,'0x4c4','0x461','0x4d2'))/(0x18fe+-0x1456+-0xa9*0x7))+-parseInt(_0x425205('0x16c',0x12d,'1z6a',0x16a,0x12e))/(0x1aec+-0x1e26+0x344)+parseInt(_0x1a9379(0x3de,0x456,0x3e1,0x42d,0x41d))/(-0x9f9*0x2+0x1a2f+-0x1a*0x3d);if(_0x16aaa3===_0x130e47)break;else _0x25933c['push'](_0x25933c['shift']());}catch(_0x5c8ae6){_0x25933c['push'](_0x25933c['shift']());}}}(_0x4ba3,-0x4393f+0x5a5ae+-0x3*-0x18316));function _0x574d0e(_0x4a3eeb,_0x41f3ae,_0x29dc4e,_0xbb0d72,_0x3e5ba9){return _0x3497(_0x29dc4e-0x30d,_0xbb0d72);}function _0x51b425(_0x217ba6,_0x39f0bf,_0x4c3390,_0x47b32d,_0x47ddbf){return _0x3497(_0x47ddbf- -0x1de,_0x47b32d);}var _0x2d3bac=(function(){function _0xb00c16(_0x493186,_0x5b358c,_0x5be40b,_0x43e777,_0x23b1af){return _0x3497(_0x5be40b-'0x232',_0x23b1af);}var _0x1da102={};function _0x24d644(_0xbff465,_0x16680d,_0x2db9ea,_0x1dd7ea,_0x237da1){return _0x3497(_0x237da1-0x271,_0x2db9ea);}function _0x1d7cf9(_0x243310,_0x1d5219,_0x527f26,_0xf6617d,_0x159faa){return _0x3497(_0x159faa- -'0x2c0',_0x243310);}function _0x1bdb5d(_0x4fb7cf,_0x2eab61,_0x2a69f7,_0x2e00de,_0x4841b6){return _0x3497(_0x2a69f7- -'0x35b',_0x2e00de);}_0x1da102[_0x1d7cf9('YNH4',-0x1bd,-'0x200',-'0x1c0',-0x1a9)]=_0x1d7cf9('Wdn$',-0xf6,-0xee,-0xed,-0x146)+_0x2d9d62('0x49b',0x4a4,0x4d8,'0x52b',0x4b5),_0x1da102[_0x1d7cf9('S)8J',-0x1f5,-0x199,-0x1ad,-'0x19c')]=_0x24d644('0x414',0x3d2,'M3Fo',0x37f,'0x3cc')+_0x1d7cf9('1z6a',-0x187,-0x1f0,-0x1d9,-0x1c5)+_0xb00c16(0x3bd,'0x3b3','0x371',0x361,'lFpT')+_0x2d9d62(0x4e4,0x48a,'0x4d9','0x4c0',0x52c)+_0x4c4fe2(-'0x1ab',-'0x1cb',-'0x1bc','kOO*',-'0x17c')+_0x25ffb9(-'0x278',-0x280,-'0x1d0',-'0x22e',-'0x228')+_0x25ffb9(-'0x30e',-'0x312',-0x327,-'0x27d',-'0x2d5')+_0x547c63('0x511','0x4e7','0x4e0','0x533','0x515')+'2',_0x1da102[_0xb00c16('0x378',0x36c,'0x386',0x358,'YNH4')]=function(_0x5ace11,_0x2be152){return _0x5ace11===_0x2be152;};function _0x13ddbd(_0x59a075,_0x55a2a6,_0x3a6561,_0x48620c,_0x24528e){return _0x234b(_0x59a075-'0x39b',_0x55a2a6);}_0x1da102[_0x547c63(0x4dc,'0x4e0',0x4b3,0x52a,0x535)]=_0x547c63(0x53d,0x4e4,'0x570','0x57e','0x4e3'),_0x1da102[_0x25ffb9(-'0x23d',-0x1dd,-'0x243',-'0x26c',-'0x238')]=_0x1d7cf9('W)pE',-'0x1ec',-0x138,-'0x15f',-'0x191'),_0x1da102[_0x2d9d62(0x4e9,'0x4cd',0x4ac,'0x4eb','0x4fb')]=function(_0x9ce27e,_0x4dda1b){return _0x9ce27e!==_0x4dda1b;};function _0x25ffb9(_0x1c0749,_0x4662e1,_0x4247a7,_0xb43a8f,_0x3b99a2){return _0x234b(_0x3b99a2- -'0x3d5',_0x1c0749);}_0x1da102[_0x2d9d62(0x4d5,'0x4a4','0x4cd',0x475,0x4d9)]=_0x13ddbd(0x4d3,'0x522',0x4cd,0x499,'0x4a4');function _0x547c63(_0x244910,_0x261d8f,_0x32e14b,_0x3bc91d,_0x41e61a){return _0x234b(_0x244910-0x3dd,_0x32e14b);}function _0x4c4fe2(_0x300d25,_0x12e312,_0x4766a4,_0x1cca24,_0x20182){return _0x3497(_0x4766a4- -'0x312',_0x1cca24);}_0x1da102[_0x2d9d62('0x466','0x418',0x461,'0x411',0x429)]=_0x547c63('0x4e6','0x510','0x4e1','0x4e6','0x49e');function _0xc513d(_0x338d59,_0x566575,_0x478119,_0x317823,_0xd71876){return _0x234b(_0xd71876-0x21b,_0x338d59);}_0x1da102[_0x25ffb9(-0x2c7,-'0x291',-0x28c,-0x244,-0x271)]=function(_0x2a95f6,_0x22deb9){return _0x2a95f6!==_0x22deb9;},_0x1da102[_0x1d7cf9('jtjB',-0x155,-'0x15a',-0x1b0,-'0x161')]=_0x24d644('0x3f7','0x3fe','upn%',0x400,'0x3ad');function _0x2d9d62(_0xbfcca7,_0x3e480c,_0x3602ab,_0x362da6,_0x4413b2){return _0x234b(_0x3602ab-'0x33e',_0x3e480c);}var _0x4ca1da=_0x1da102,_0x3d7341=!![];return function(_0x10a7c8,_0x1df4e4){function _0x408b0d(_0x165e9b,_0x1d1b9c,_0x2dff7e,_0x337be1,_0x458db5){return _0x4c4fe2(_0x165e9b-'0x152',_0x1d1b9c-'0x153',_0x2dff7e-'0x1c3',_0x1d1b9c,_0x458db5-'0x122');}function _0x46e1dd(_0x9e5e51,_0x5997e3,_0x4b92a5,_0x3f5bb8,_0x383fad){return _0x13ddbd(_0x9e5e51- -0x6e8,_0x383fad,_0x4b92a5-0xd,_0x3f5bb8-'0x1e8',_0x383fad-0x28);}var _0x2d85bc={'HLiyi':_0x4ca1da[_0x408b0d(-0x5f,'kOO*',-0x56,-'0x27',-0x70)],'bANBt':_0x4ca1da[_0x5af3c0('0x345',0x34c,0x33c,'NZ7J','0x39d')],'dzQmG':function(_0x101216,_0x49f33b){function _0x546962(_0xeecaca,_0x37e76b,_0x51affc,_0x5594d0,_0x424c5a){return _0x408b0d(_0xeecaca-'0x8e',_0x424c5a,_0x51affc- -'0x104',_0x5594d0-0x1ed,_0x424c5a-'0x1f0');}return _0x4ca1da[_0x546962(-0xdd,-'0xa4',-0xcf,-'0x7b','7n9Q')](_0x101216,_0x49f33b);},'AMHKE':_0x4ca1da[_0x1e0c6e(-'0x11b',-'0x119','7n9Q',-'0x135',-0x185)],'XKwxD':_0x4ca1da[_0x2bb900('lFpT','0x40a',0x47a,0x443,0x446)],'hnKWX':function(_0x40b9a2,_0x55d15f){function _0x590c9e(_0x410546,_0x328ad7,_0x3208f4,_0x197eba,_0x1cf5b1){return _0x234b(_0x1cf5b1-0x29,_0x410546);}return _0x4ca1da[_0x590c9e(0x15f,0x1c7,'0x18c',0x18d,0x197)](_0x40b9a2,_0x55d15f);},'KrUfI':_0x4ca1da[_0x1e0c6e(-'0x18a',-0x1e2,'hL3V',-0x1d4,-0x1e7)],'dnCFo':_0x4ca1da[_0x408b0d(-'0x12','B1mS',-'0x3d',-0x57,-0x72)]};function _0x1e0c6e(_0x401a88,_0x6a468,_0x32d0fd,_0x592049,_0x128b15){return _0x24d644(_0x401a88-'0x38',_0x6a468-0x14a,_0x32d0fd,_0x592049-'0x11',_0x592049- -0x54a);}function _0x4463f1(_0x2a4b78,_0x65c4ec,_0x468b51,_0x49ddaf,_0x2b18b5){return _0x1bdb5d(_0x2a4b78-0xbe,_0x65c4ec-0x75,_0x468b51-'0x154',_0x2b18b5,_0x2b18b5-'0x76');}function _0x2bb900(_0x55aa25,_0x4e9bf5,_0x50c09b,_0x1d9af5,_0x31564d){return _0x4c4fe2(_0x55aa25-'0x18c',_0x4e9bf5-'0xd',_0x1d9af5-'0x5d3',_0x55aa25,_0x31564d-'0x17b');}function _0x5af3c0(_0x1f6fe5,_0x2a7772,_0x224ffa,_0xd82afc,_0x44b928){return _0xb00c16(_0x1f6fe5-'0x28',_0x2a7772-'0x10b',_0x2a7772- -'0x26',_0xd82afc-'0x95',_0xd82afc);}function _0x177063(_0x1baa8f,_0x533c01,_0x44d19a,_0x2bac90,_0x9030b6){return _0x13ddbd(_0x533c01- -0x56a,_0x9030b6,_0x44d19a-'0x15a',_0x2bac90-0xeb,_0x9030b6-'0x1a0');}if(_0x4ca1da[_0x2bb900('1z6a','0x461','0x474',0x442,0x46f)](_0x4ca1da[_0x408b0d(-'0x54','B1mS',-'0x3a',-0x4b,-0x66)],_0x4ca1da[_0x177063(-0xe8,-0xb4,-0xb4,-'0xf1',-0x58)])){if(_0x48dd1b){var _0x440765=_0x3d668c[_0x46e1dd(-'0x20a',-0x217,-'0x227',-'0x21c',-'0x23a')](_0x1c2b44,arguments);return _0x83c96d=null,_0x440765;}}else{var _0x340fee=_0x3d7341?function(){var _0x2b190a={};function _0x43e576(_0x473fa6,_0x50ba54,_0x3db4dc,_0x5f52e5,_0x106ab2){return _0x2bb900(_0x50ba54,_0x50ba54-0xa1,_0x3db4dc-0x13c,_0x106ab2- -0x379,_0x106ab2-'0x149');}function _0x39dc3a(_0x37f117,_0x16c791,_0x44819f,_0x36763a,_0x164c15){return _0x5af3c0(_0x37f117-0xa8,_0x44819f- -0x143,_0x44819f-'0xe7',_0x16c791,_0x164c15-0xf1);}_0x2b190a[_0x510f69('0x28c','0x23b',0x2b2,0x274,'0x2a8')]=_0x2d85bc[_0x510f69(0x21d,'0x204',0x248,0x23b,0x22f)];function _0x3e9e8f(_0xa9335f,_0x1d4bff,_0x4cc8b6,_0x259b90,_0x37d08b){return _0x4463f1(_0xa9335f-'0x11',_0x1d4bff-'0x18f',_0xa9335f-0x1f,_0x259b90-0x4f,_0x4cc8b6);}function _0x5a3609(_0x43dd5c,_0x5e16dc,_0x5e7038,_0x2fa08f,_0x2ceb8b){return _0x4463f1(_0x43dd5c-'0x127',_0x5e16dc-0xee,_0x43dd5c- -'0x15',_0x2fa08f-0x37,_0x2fa08f);}function _0x1db869(_0x531bf4,_0x3b9f57,_0x35a502,_0x5b3edf,_0x56a71a){return _0x46e1dd(_0x35a502- -0x69,_0x3b9f57-0x39,_0x35a502-'0xc4',_0x5b3edf-0x14f,_0x56a71a);}function _0x139238(_0x33b058,_0x105a38,_0x516cd4,_0x6f7bac,_0x1edbdf){return _0x177063(_0x33b058-'0x1b3',_0x105a38-'0x527',_0x516cd4-'0x7c',_0x6f7bac-'0x1cd',_0x33b058);}_0x2b190a[_0x3e9e8f(-'0x6a',-0x93,'7g%t',-'0x17',-'0xa9')]=_0x2d85bc[_0x39bb4b(-'0xc9',-0xd5,-'0x7c',-0xc3,-'0x3c')];function _0x96bf85(_0x39d93d,_0x130b42,_0x272021,_0x46fbbc,_0x26518b){return _0x408b0d(_0x39d93d-'0xff',_0x272021,_0x130b42-0x27,_0x46fbbc-'0x99',_0x26518b-'0xdd');}function _0x39bb4b(_0x4804a2,_0x18b54d,_0x5509ab,_0x42587f,_0x42a350){return _0x46e1dd(_0x5509ab-'0x18a',_0x18b54d-0x14b,_0x5509ab-0xfb,_0x42587f-0xee,_0x42587f);}function _0x4157cd(_0x30f6dc,_0x2cd657,_0x42138c,_0x2f9429,_0x4512c9){return _0x46e1dd(_0x42138c-'0x16c',_0x2cd657-'0x1ec',_0x42138c-0x1c5,_0x2f9429-'0x1f4',_0x2f9429);}var _0x1f668a=_0x2b190a;function _0x510f69(_0x4661d1,_0x3cc007,_0x1bf69d,_0x559c58,_0x51dc4a){return _0x177063(_0x4661d1-0xfd,_0x559c58-'0x2e9',_0x1bf69d-0x24,_0x559c58-'0x17',_0x4661d1);}if(_0x2d85bc[_0x39bb4b(-'0xdd',-'0xdc',-0xa1,-'0xd7',-0xb4)](_0x2d85bc[_0x96bf85(0x13,0x34,'7n9Q',-0x20,-'0xf')],_0x2d85bc[_0x43e576('0xb6','nFbT',0xb8,0x96,'0xc4')])){var _0x14f70c=_0x1d2950?function(){function _0x540b78(_0x4150ce,_0x1b8f44,_0x59df3b,_0x500e10,_0x5451b0){return _0x43e576(_0x4150ce-'0x3b',_0x59df3b,_0x59df3b-'0x1c0',_0x500e10-0x1ae,_0x500e10- -0x2e1);}if(_0x45c011){var _0x907605=_0x5ee993[_0x540b78(-'0x297',-0x249,'hW61',-0x24e,-'0x269')](_0x4cd83c,arguments);return _0x3df542=null,_0x907605;}}:function(){};return _0x135b6a=![],_0x14f70c;}else{if(_0x1df4e4){if(_0x2d85bc[_0x139238('0x449','0x456','0x48c',0x477,'0x417')](_0x2d85bc[_0x5a3609(-0x110,-0x10d,-0xf5,'YNH4',-0x148)],_0x2d85bc[_0x139238(0x462,0x493,'0x4bc',0x43c,'0x461')])){var _0x240083=_0x1df4e4[_0x96bf85(0x41,-0x1b,'WpSm',-'0x6b',0x3c)](_0x10a7c8,arguments);return _0x1df4e4=null,_0x240083;}else _0x2179d6[_0x1db869(-'0x1bb',-'0x1ed',-0x217,-0x250,-0x1d0)+_0x139238('0x479',0x4b1,0x4d2,'0x50a','0x470')+_0x39bb4b(-'0x8d',-'0xa9',-'0x77',-0x53,-'0xa7')](_0x1f668a[_0x96bf85(-'0xe',0x29,'WB%T',-'0x8',0x76)])[_0x96bf85('0x78','0x21','C(KE','0x43',0x49)+_0x510f69('0x21e','0x22b',0x28c,0x23f,0x25d)]=_0x1f668a[_0x39bb4b(-'0xc9',-0x87,-'0x9a',-'0xa1',-0x80)];}}}:function(){};return _0x3d7341=![],_0x340fee;}};}()),_0x5103f3=_0x2d3bac(this,function(){function _0x47727f(_0xfee639,_0x2e75df,_0x328ad1,_0x4dcad3,_0x587131){return _0x3497(_0x587131- -'0x7',_0x2e75df);}var _0x2fd63b={'LeURK':function(_0x36829c,_0x2e9ece){return _0x36829c(_0x2e9ece);},'jbUcr':function(_0x321dbd,_0x11b4fa){return _0x321dbd+_0x11b4fa;},'RZcka':_0x1bd92c('0x37f','0x3a9','0x392','0x3c2',0x36c)+_0x5d67a7(-'0x261','SO%G',-'0x214',-0x297,-0x247)+_0x1bd92c(0x3f0,'0x3f9','0x3e6',0x402,'0x3f0')+_0x1bd92c('0x44b','0x429','0x41f','0x425','0x409'),'jkreY':_0x5d67a7(-'0x20a','YNH4',-'0x1d9',-0x1e7,-'0x243')+_0x139b11(-'0x145',-0x111,-'0x142',-0x115,'YNH4')+_0x4ae880('pLI8','0x3e0','0x3a9','0x3e1','0x39b')+_0x4ae880('LI9n','0x312',0x312,0x383,0x36a)+_0x5d67a7(-0x280,'mJk^',-'0x23f',-'0x229',-0x244)+_0x378fd2('0x2b2','0x2b1','0x29c','0x2fd','0x264')+'\x20)','Expji':_0x8cfa67(0x356,0x2ef,0x307,'0x2bb','0x352')+_0x8cfa67('0x37a',0x39a,0x34a,'0x31e','0x301')+'1','ioZuL':function(_0x3d474a,_0x4d5966){return _0x3d474a===_0x4d5966;},'BSqUu':_0x5d67a7(-'0x233','Wdn$',-'0x26f',-'0x22b',-0x1f8),'eQnuK':_0x1bd92c(0x3ff,'0x3b4',0x397,'0x3b9','0x412'),'Chyav':function(_0x4f802c,_0x2dcdfe){return _0x4f802c!==_0x2dcdfe;},'haiCO':_0x1bd92c('0x3f7','0x386','0x381','0x3ae','0x3d0'),'FRLlh':_0x3e09c1(-'0x8e',-'0x9a',-'0x1f','LI9n',-'0x49'),'mJAOR':function(_0x4e65c1,_0x49a439){return _0x4e65c1(_0x49a439);},'MDvcg':function(_0x57fd41,_0x6f6f8b){return _0x57fd41+_0x6f6f8b;},'oBhBX':function(_0x40ec9e,_0x42e983){return _0x40ec9e+_0x42e983;},'tEZWC':_0x139b11(-0x16d,-0x1ab,-0x1a0,-'0x178','i)uy'),'flXac':_0x47727f('0xc9','3S##',0x16c,0xf1,'0x124'),'rqgEL':function(_0x362253){return _0x362253();},'UYsTA':_0x5d67a7(-0x1f5,'upn%',-'0x20a',-0x1cc,-'0x246'),'vUsZM':_0x8cfa67('0x38e','0x2ea',0x33f,'0x2e8',0x2eb),'SeQhj':_0x1c26fb('0x25e','0x1eb','0x23a','0x1e4',0x276),'lZOTk':_0x139b11(-'0x11b',-'0x10a',-'0x10d',-0x13d,'sQ7^'),'KjaxR':_0x47727f('0xf7','%[^N',0xf6,0x123,0x107)+_0x139b11(-'0x174',-0xfc,-'0x128',-0x16a,'WB%T'),'KJEoy':_0x378fd2('0x30e',0x2c0,0x2b5,'0x33e','0x31a'),'hjZWL':_0x1bd92c(0x3f6,'0x3c4',0x36a,'0x3b4','0x396'),'bdQiN':function(_0x9fa31d,_0x2e63d0){return _0x9fa31d<_0x2e63d0;},'TDkIN':function(_0x46e874,_0x59d51f){return _0x46e874===_0x59d51f;},'NBMOv':_0x139b11(-0x1d7,-'0x206',-0x1c2,-'0x1ac','kOO*'),'QCUpU':_0x3e09c1(-0xf9,-0x5d,-'0xf7','sQ7^',-'0xb7'),'swjbI':_0x8cfa67(0x33e,'0x2a2','0x2e9',0x2a5,0x325)+_0x1bd92c(0x48c,0x430,0x455,0x445,'0x43e')+'0'};function _0x3e09c1(_0x45117f,_0x1f9a8d,_0x1a906c,_0x43b2dc,_0x30a35c){return _0x3497(_0x30a35c- -'0x1ee',_0x43b2dc);}var _0x202c8f=function(){function _0x314642(_0x511cdb,_0x51fdf1,_0x15727a,_0x51c95e,_0xa4a2ef){return _0x4ae880(_0x51fdf1,_0x51fdf1-'0xdb',_0x15727a-'0xd9',_0x51c95e-0x7c,_0x511cdb- -0x4e1);}function _0x50e406(_0x23fdbc,_0x4bdff5,_0x4fc17b,_0x51046f,_0x4114fb){return _0x5d67a7(_0x51046f-0x104,_0x4114fb,_0x4fc17b-'0x1ea',_0x51046f-'0x74',_0x4114fb-0x169);}function _0x380360(_0x5e0148,_0x70e014,_0x3de082,_0xed832,_0x1f19ca){return _0x139b11(_0x5e0148-'0x4d',_0x70e014-'0xa6',_0xed832- -'0x49',_0xed832-0xa8,_0x5e0148);}function _0x112c19(_0x41eeea,_0x5de9f0,_0x391085,_0x1cb56b,_0x2c37c7){return _0x378fd2(_0x5de9f0- -'0x570',_0x2c37c7,_0x391085-0x1cd,_0x1cb56b-0x19a,_0x2c37c7-0xfe);}function _0x38dddc(_0x516236,_0xcdea05,_0x54897d,_0x86bea1,_0xc96705){return _0x378fd2(_0xcdea05-'0x169',_0x54897d,_0x54897d-0xda,_0x86bea1-0x17f,_0xc96705-'0x120');}var _0x323f2b={'dGTft':function(_0x43b50e,_0x2fd012){function _0x2907f8(_0x17e04a,_0x4f9aad,_0x458233,_0x4ed2ac,_0x274ed2){return _0x3497(_0x4ed2ac-0x2d1,_0x274ed2);}return _0x2fd63b[_0x2907f8(0x463,0x447,'0x46c','0x474','YNH4')](_0x43b50e,_0x2fd012);},'lHcCO':function(_0x3da520,_0x50601c){function _0x2cd8e7(_0x7ec167,_0x17da74,_0x2aab19,_0x452b35,_0x2493a1){return _0x234b(_0x2aab19- -0x18,_0x452b35);}return _0x2fd63b[_0x2cd8e7('0x118','0x155',0x129,'0x123',0x160)](_0x3da520,_0x50601c);},'fiXXu':_0x2fd63b[_0x33e337(0xa3,0x1e,0x64,'wDW@','0xb')],'cGxPD':_0x2fd63b[_0x55c9cf(0x481,0x4b5,'0x4ca',0x471,'0x4f6')],'nyLuV':_0x2fd63b[_0x55c9cf('0x53d',0x51c,'0x4dc','0x4fa','0x4d8')]};function _0x17abdf(_0x2f2265,_0x3a3cfc,_0x1e53c3,_0xc2cda0,_0x5e8e49){return _0x8cfa67(_0x2f2265-0x10d,_0x3a3cfc-0x12d,_0x5e8e49- -0x493,_0xc2cda0-'0x1db',_0x3a3cfc);}function _0x33e337(_0x151f40,_0x3567e0,_0xfbd325,_0x4eebb4,_0x1d1265){return _0x4ae880(_0x4eebb4,_0x3567e0-0x72,_0xfbd325-0x15,_0x4eebb4-'0xd8',_0xfbd325- -'0x301');}function _0x391136(_0x251e60,_0x94fbe2,_0x2c672a,_0x7ec62a,_0x13b117){return _0x139b11(_0x251e60-0x84,_0x94fbe2-'0xf4',_0x7ec62a- -0x82,_0x7ec62a-'0x6',_0x94fbe2);}function _0x55c9cf(_0x53369c,_0x57aaa9,_0x43f6bb,_0x292b13,_0x50a9a3){return _0x1bd92c(_0x43f6bb,_0x57aaa9-0x24,_0x43f6bb-'0x11',_0x57aaa9-'0x110',_0x50a9a3-'0xdb');}function _0x4dc898(_0x1e03e3,_0x2e1ed3,_0x5ef6c0,_0xc0f8de,_0x5671fb){return _0x1c26fb(_0x1e03e3-0x1e9,_0x5671fb,_0x5ef6c0- -'0x23f',_0xc0f8de-0x19c,_0x5671fb-'0x1b0');}if(_0x2fd63b[_0x55c9cf('0x521','0x52d','0x54e',0x4d4,'0x544')](_0x2fd63b[_0x4dc898(-'0x42',-0x1,0x9,0x4f,'0x34')],_0x2fd63b[_0x112c19(-0x250,-'0x2a1',-'0x267',-'0x2ee',-'0x24c')])){var _0x38a582=_0x6f239c[_0x112c19(-0x272,-0x298,-'0x29d',-0x28a,-0x2ef)](_0x59c475,arguments);return _0x3eb1c0=null,_0x38a582;}else{var _0x34f922;try{if(_0x2fd63b[_0x391136(-'0x248','xzV8',-0x1a5,-'0x1ed',-0x1fd)](_0x2fd63b[_0x4dc898(-0x81,-0xb6,-0x96,-'0x42',-0xa6)],_0x2fd63b[_0x380360('nFbT',-'0x233',-0x237,-0x1fe,-'0x1a5')]))_0x34f922=_0x2fd63b[_0x17abdf(-'0x1a9',-0x1ac,-0x1d2,-0x1ca,-0x1a6)](Function,_0x2fd63b[_0x38dddc('0x425','0x40d',0x3c3,0x402,0x430)](_0x2fd63b[_0x391136(-0x1aa,'S)8J',-'0x229',-'0x1e3',-0x1e2)](_0x2fd63b[_0x112c19(-'0x266',-0x270,-0x233,-0x2a7,-'0x238')],_0x2fd63b[_0x314642(-0x15f,'!E[D',-'0x19f',-'0x19f',-'0x111')]),');'))();else{var _0x4780e2;try{_0x4780e2=_0x323f2b[_0x17abdf(-'0x1f5',-'0x20f',-0x1b6,-'0x1b1',-'0x1c3')](_0x112e6c,_0x323f2b[_0x33e337(0x26,0x56,'0x67','LI9n',0xa6)](_0x323f2b[_0x50e406(-0x123,-0x109,-0xde,-'0xe4','NZ7J')](_0x323f2b[_0x33e337('0xf7',0xbf,0xf7,'lFpT',0xaa)],_0x323f2b[_0x55c9cf('0x52d',0x4fa,0x553,'0x52c',0x4d6)]),');'))();}catch(_0x9f4d05){_0x4780e2=_0x33b94e;}return _0x4780e2;}}catch(_0x15fbe0){if(_0x2fd63b[_0x55c9cf(0x570,'0x52d','0x4da','0x4ee','0x586')](_0x2fd63b[_0x38dddc('0x458',0x492,0x4bd,'0x4ed','0x43a')],_0x2fd63b[_0x50e406(-0x1bd,-0x136,-'0x193',-0x181,'hkYa')])){var _0x30604d=_0x323f2b[_0x391136(-'0x1a5','7g%t',-0x200,-0x1f9,-0x1f1)][_0x50e406(-'0x12b',-0x159,-0x115,-'0x104',')ouu')]('|'),_0x181e99=0xe4b+-0x2333*-0x1+-0x317e;while(!![]){switch(_0x30604d[_0x181e99++]){case'0':var _0x4bad5a=_0x3d32ef[_0x2607a1]||_0x386d38;continue;case'1':_0xe3625e[_0x2607a1]=_0x386d38;continue;case'2':var _0x2607a1=_0x55e54b[_0x33707f];continue;case'3':_0x386d38[_0x38dddc('0x431','0x431','0x3f5','0x420','0x41d')+_0x112c19(-0x28f,-'0x27d',-'0x25e',-0x242,-'0x26b')]=_0x45638c[_0x33e337(0x6f,'0xc3',0x77,')ouu','0x4d')](_0xa15627);continue;case'4':_0x386d38[_0x314642(-0x189,'WB%T',-0x1a4,-0x163,-'0x175')+_0x4dc898(-0xb4,-'0x93',-0x7a,-'0x4a',-'0x90')]=_0x4bad5a[_0x33e337(0x74,0x1f,'0x72','Vp83',0x7d)+_0x380360('G61p',-'0x13d',-'0x10a',-'0x166',-0x1bb)][_0x391136(-0x1d2,'%[^N',-0x22c,-0x1fd,-0x1cd)](_0x4bad5a);continue;case'5':var _0x386d38=_0x4d3368[_0x33e337(0xa7,0x9,0x62,'jtjB','0x10')+_0x33e337('0x55',0x102,0xae,'jtjB','0x97')+'r'][_0x55c9cf('0x4b5','0x4a4',0x45b,'0x49f','0x4db')+_0x17abdf(-0x17f,-'0xf2',-0x163,-0xe3,-0x134)][_0x380360('9vHf',-'0x188',-0x153,-'0x18c',-0x1e0)](_0x1613a);continue;}break;}}else _0x34f922=window;}return _0x34f922;}};function _0x8cfa67(_0x364376,_0x1453aa,_0x48b666,_0x15471a,_0x2c2a1f){return _0x234b(_0x48b666-'0x1b8',_0x2c2a1f);}function _0x1bd92c(_0x3bb563,_0xa1f513,_0x518938,_0x35f929,_0x3f2202){return _0x234b(_0x35f929-'0x29a',_0x3bb563);}function _0x1c26fb(_0x10044c,_0x12f105,_0x5a54d7,_0x292e15,_0x4b2b98){return _0x234b(_0x5a54d7-'0xa7',_0x12f105);}var _0xdcbd63=_0x2fd63b[_0x378fd2('0x33f','0x36b',0x38c,'0x31b',0x2f6)](_0x202c8f),_0x2781eb=_0xdcbd63[_0x5408a9(-0x154,-0xc1,-0xff,-'0xcc',-'0x108')+'le']=_0xdcbd63[_0x1c26fb('0x26e','0x263',0x250,0x25e,'0x212')+'le']||{};function _0x4ae880(_0x1c13b7,_0x5ea094,_0x4b51a8,_0x35b533,_0x4dafdc){return _0x3497(_0x4dafdc-0x262,_0x1c13b7);}function _0x378fd2(_0x5cc999,_0x1636e2,_0x3d6f2f,_0x2e120b,_0xde3577){return _0x234b(_0x5cc999-0x195,_0x1636e2);}function _0x5408a9(_0x547fce,_0x1140f1,_0x3f3055,_0x3fe4a6,_0x327a50){return _0x234b(_0x327a50- -0x2b1,_0x3fe4a6);}function _0x139b11(_0x2917d6,_0x530330,_0x30347e,_0x32692f,_0x56cf10){return _0x3497(_0x30347e- -'0x2b9',_0x56cf10);}var _0x43e335=[_0x2fd63b[_0x5408a9(-'0xfa',-0x17f,-0x159,-'0xf5',-'0x139')],_0x2fd63b[_0x8cfa67('0x37c','0x2ec',0x338,'0x366',0x387)],_0x2fd63b[_0x47727f('0x109','xzV8','0x15d','0x17e','0x15f')],_0x2fd63b[_0x1bd92c('0x42f','0x46a',0x478,'0x41f',0x432)],_0x2fd63b[_0x139b11(-'0x20b',-0x1a3,-0x1af,-0x1f7,')ouu')],_0x2fd63b[_0x3e09c1(-'0x106',-'0x79',-0xd1,'NZ7J',-'0xc2')],_0x2fd63b[_0x5d67a7(-'0x22a','SO%G',-0x267,-0x284,-0x21e)]];function _0x5d67a7(_0x3e3dc4,_0x531dc7,_0x32440d,_0x597132,_0x3ebb23){return _0x3497(_0x3e3dc4- -0x37d,_0x531dc7);}for(var _0x5081e3=0x14d9+-0x47*0x73+0x2*0x586;_0x2fd63b[_0x5d67a7(-0x21a,'n#iz',-0x218,-'0x1f7',-0x229)](_0x5081e3,_0x43e335[_0x1c26fb(0x202,0x1a6,0x1eb,'0x1f4','0x1e9')+'h']);_0x5081e3++){if(_0x2fd63b[_0x5d67a7(-0x210,'fKU1',-0x261,-0x256,-0x1ea)](_0x2fd63b[_0x1c26fb('0x245',0x24a,'0x237',0x25a,0x28b)],_0x2fd63b[_0x47727f(0xd3,'M3Fo','0xb6',0x116,'0x109')]))_0x38a068=_0x5b0bb8;else{var _0x44218a=_0x2fd63b[_0x47727f('0x100','M3Fo','0x111',0x137,0x14e)][_0x3e09c1(0x2,-'0x21',-'0x26','G61p',-'0x48')]('|'),_0x31fc22=0x10a5+-0x1*0x11dd+0x138;while(!![]){switch(_0x44218a[_0x31fc22++]){case'0':_0x2781eb[_0x6209e3]=_0x3ce876;continue;case'1':var _0x1dc8c4=_0x2781eb[_0x6209e3]||_0x3ce876;continue;case'2':var _0x3ce876=_0x2d3bac[_0x4ae880('NZ7J','0x450',0x417,'0x400',0x402)+_0x4ae880('sWnZ','0x3f9','0x3cf',0x3f9,'0x3f0')+'r'][_0x8cfa67(0x2c5,'0x2f3',0x2b2,0x25f,'0x2b8')+_0x3e09c1(-'0x7c',-0x45,-'0x96','W)pE',-0x89)][_0x3e09c1(-0xd7,-'0x12f',-'0x12a','NZ7J',-'0xdb')](_0x2d3bac);continue;case'3':_0x3ce876[_0x5d67a7(-0x20d,'hkYa',-'0x1c0',-'0x1b2',-0x1da)+_0x8cfa67('0x324',0x2cd,0x2d6,0x2ce,0x32a)]=_0x1dc8c4[_0x378fd2(0x2e7,'0x2bf',0x335,'0x2c4',0x314)+_0x378fd2(0x2b3,'0x279','0x26c','0x293',0x2ed)][_0x5d67a7(-'0x1d5','G61p',-'0x1df',-'0x1eb',-'0x1c1')](_0x1dc8c4);continue;case'4':_0x3ce876[_0x5d67a7(-'0x235','pLI8',-'0x1f2',-0x1f5,-'0x276')+_0x378fd2(0x2f3,0x30e,0x2cd,0x2d0,0x2b8)]=_0x2d3bac[_0x3e09c1(-'0xb7',-0x9c,-'0x88','i)uy',-'0xc0')](_0x2d3bac);continue;case'5':var _0x6209e3=_0x43e335[_0x5081e3];continue;}break;}}}});_0x5103f3();function _0x232beb(_0x2cebe2,_0x5e89cf,_0x2a3d1e,_0x3b6e58,_0x94b10f){return _0x234b(_0x2a3d1e- -0x138,_0x5e89cf);}function _0x44222e(_0x277c48,_0x314385,_0x408a34,_0x3eda6c,_0x2ac574){return _0x3497(_0x3eda6c-0x1f5,_0x2ac574);}function _0x234b(_0x5e4133,_0x3bde30){var _0x10d78f=_0x4ba3();return _0x234b=function(_0x6dc0a5,_0x2179d6){_0x6dc0a5=_0x6dc0a5-(0x90b*0x3+0x3*-0x66a+0x1*-0x6ed);var _0x602474=_0x10d78f[_0x6dc0a5];if(_0x234b['APTIIF']===undefined){var _0x5a7b6f=function(_0x406005){var _0x2f5d55='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';var _0x3f329d='',_0x47b849='';for(var _0xc18922=0x583*-0x7+-0x2221*-0x1+0x474,_0x3560a0,_0x551b60,_0x1f13b0=0x1921*-0x1+-0x1b08+-0x1163*-0x3;_0x551b60=_0x406005['charAt'](_0x1f13b0++);~_0x551b60&&(_0x3560a0=_0xc18922%(-0xa*-0x355+0x12a+-0x2278)?_0x3560a0*(0x27*-0xdc+0x205a+0x16a*0x1)+_0x551b60:_0x551b60,_0xc18922++%(0x2441*0x1+0x1*-0x197c+0x1*-0xac1))?_0x3f329d+=String['fromCharCode'](0x14b*-0xc+0x2*-0xcbb+0x29f9&_0x3560a0>>(-(0xb3c+-0xffe+0x131*0x4)*_0xc18922&0x1*-0x1fbb+-0x2162+0x4123)):-0x1c81+-0x17f5+0x3476){_0x551b60=_0x2f5d55['indexOf'](_0x551b60);}for(var _0x1e8d05=0x1a7*0x2+-0x1eeb+-0x1*-0x1b9d,_0x115bf0=_0x3f329d['length'];_0x1e8d05<_0x115bf0;_0x1e8d05++){_0x47b849+='%'+('00'+_0x3f329d['charCodeAt'](_0x1e8d05)['toString'](0x2277*-0x1+-0x1546+0x37cd))['slice'](-(0x2*-0x8e1+0xcf0+-0x26a*-0x2));}return decodeURIComponent(_0x47b849);};_0x234b['RVAwuf']=_0x5a7b6f,_0x5e4133=arguments,_0x234b['APTIIF']=!![];}var _0xab3251=_0x10d78f[0x1a*-0x180+-0x1f4e*-0x1+0x7b2],_0x260361=_0x6dc0a5+_0xab3251,_0x12b215=_0x5e4133[_0x260361];return!_0x12b215?(_0x602474=_0x234b['RVAwuf'](_0x602474),_0x5e4133[_0x260361]=_0x602474):_0x602474=_0x12b215,_0x602474;},_0x234b(_0x5e4133,_0x3bde30);}function _0x3856d9(_0x2df121,_0x385162,_0x498468,_0x2e26cd,_0x1baec8){return _0x234b(_0x2e26cd-0x1d3,_0x2df121);}function _0x274498(_0x51f498,_0x5b18a7,_0x5950c8,_0xd192ee,_0x5709dc){return _0x234b(_0x5709dc-0x389,_0x5950c8);}function _0x41e28c(_0x243c14,_0x545fde,_0x1f525d,_0x216bf0,_0x12f26a){return _0x3497(_0x1f525d- -'0x19c',_0x243c14);}function _0x5c1c1c(_0x4106f6,_0x559c68,_0x3fab27,_0x3b0a6,_0x3319e2){return _0x234b(_0x3fab27- -0x1b0,_0x4106f6);}function _0x4ea25c(_0x56d3a3,_0x4d39a6,_0x1e1d92,_0x50004a,_0x2e4018){return _0x3497(_0x2e4018- -0x1ae,_0x56d3a3);}function _0x3497(_0x3253c2,_0x86d138){var _0x4bd20f=_0x4ba3();return _0x3497=function(_0x415ff2,_0x55d440){_0x415ff2=_0x415ff2-(0x90b*0x3+0x3*-0x66a+0x1*-0x6ed);var _0x19b36d=_0x4bd20f[_0x415ff2];if(_0x3497['YfpAlU']===undefined){var _0x4f93c0=function(_0x45ee91){var _0x353d26='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';var _0x5c734c='',_0x38ee1e='';for(var _0x40708d=0x583*-0x7+-0x2221*-0x1+0x474,_0x68c435,_0x54a7e3,_0x815188=0x1921*-0x1+-0x1b08+-0x1163*-0x3;_0x54a7e3=_0x45ee91['charAt'](_0x815188++);~_0x54a7e3&&(_0x68c435=_0x40708d%(-0xa*-0x355+0x12a+-0x2278)?_0x68c435*(0x27*-0xdc+0x205a+0x16a*0x1)+_0x54a7e3:_0x54a7e3,_0x40708d++%(0x2441*0x1+0x1*-0x197c+0x1*-0xac1))?_0x5c734c+=String['fromCharCode'](0x14b*-0xc+0x2*-0xcbb+0x29f9&_0x68c435>>(-(0xb3c+-0xffe+0x131*0x4)*_0x40708d&0x1*-0x1fbb+-0x2162+0x4123)):-0x1c81+-0x17f5+0x3476){_0x54a7e3=_0x353d26['indexOf'](_0x54a7e3);}for(var _0x1bc05b=0x1a7*0x2+-0x1eeb+-0x1*-0x1b9d,_0x1183ee=_0x5c734c['length'];_0x1bc05b<_0x1183ee;_0x1bc05b++){_0x38ee1e+='%'+('00'+_0x5c734c['charCodeAt'](_0x1bc05b)['toString'](0x2277*-0x1+-0x1546+0x37cd))['slice'](-(0x2*-0x8e1+0xcf0+-0x26a*-0x2));}return decodeURIComponent(_0x38ee1e);};var _0x1ec972=function(_0x3bce62,_0x29424b){var _0xa55866=[],_0x1c7638=0x1a*-0x180+-0x1f4e*-0x1+0x7b2,_0xeaa4e4,_0x2c12f0='';_0x3bce62=_0x4f93c0(_0x3bce62);var _0x57ccad;for(_0x57ccad=0x2627+0x9fb+-0x3022;_0x57ccad<-0x2226+0x2310+0x16;_0x57ccad++){_0xa55866[_0x57ccad]=_0x57ccad;}for(_0x57ccad=0x46*0x32+-0x44+0x138*-0xb;_0x57ccad<-0xd9c+-0xe0b+-0x1e9*-0xf;_0x57ccad++){_0x1c7638=(_0x1c7638+_0xa55866[_0x57ccad]+_0x29424b['charCodeAt'](_0x57ccad%_0x29424b['length']))%(0x7a+-0x20e0+0x13*0x1c2),_0xeaa4e4=_0xa55866[_0x57ccad],_0xa55866[_0x57ccad]=_0xa55866[_0x1c7638],_0xa55866[_0x1c7638]=_0xeaa4e4;}_0x57ccad=-0x9d*0x23+0xb29*0x2+-0xdb,_0x1c7638=0x26cf*-0x1+0x1f3c+0x793;for(var _0x103553=0x1345+0x8ed+-0x1c32;_0x103553<_0x3bce62['length'];_0x103553++){_0x57ccad=(_0x57ccad+(0x164*-0x17+-0x22*-0xa8+0x9ad))%(0x1f*-0x80+-0x2364+0xc*0x453),_0x1c7638=(_0x1c7638+_0xa55866[_0x57ccad])%(-0x14bd+-0x319*0x1+-0x16*-0x121),_0xeaa4e4=_0xa55866[_0x57ccad],_0xa55866[_0x57ccad]=_0xa55866[_0x1c7638],_0xa55866[_0x1c7638]=_0xeaa4e4,_0x2c12f0+=String['fromCharCode'](_0x3bce62['charCodeAt'](_0x103553)^_0xa55866[(_0xa55866[_0x57ccad]+_0xa55866[_0x1c7638])%(0xb47+0x21f7+-0x2c3e*0x1)]);}return _0x2c12f0;};_0x3497['jRTBAW']=_0x1ec972,_0x3253c2=arguments,_0x3497['YfpAlU']=!![];}var _0x430839=_0x4bd20f[0x1dad+0x9a9*-0x1+0x54*-0x3d],_0x78ee90=_0x415ff2+_0x430839,_0x1a59c8=_0x3253c2[_0x78ee90];return!_0x1a59c8?(_0x3497['HzJLQT']===undefined&&(_0x3497['HzJLQT']=!![]),_0x19b36d=_0x3497['jRTBAW'](_0x19b36d,_0x55d440),_0x3253c2[_0x78ee90]=_0x19b36d):_0x19b36d=_0x1a59c8,_0x19b36d;},_0x3497(_0x3253c2,_0x86d138);}function _0x4524f3(_0x163f8e,_0x5f2267,_0x1e8492,_0x3afdfa,_0x37a68e){return _0x234b(_0x5f2267-0x148,_0x37a68e);}function _0x4ba3(){var _0x51e3ca=['jmkiqmk8WPK','DhjHy2u','rwLVsvq','hCozW5ZdQcW','AxmIksG','Aw5N','qMvqsLu','W5RcH2Cqza','seXPEwK','zhPrBuC','AwXWBg8','pSkZDfCn','sfrnta','oWdcImozdCo9WOG','FCkBwmk0W78','CMv0Dxi','D0f1AM0','FCkRtbRdKq','W53dKexcV8os','z0RcRdHR','vCoYWOBcIq','pSkvECk+','EdpcVMFcUa','W64iW4WXcCoiWQCC','mNW1Fde','BSobr8k1W61bWP1/','x19WCM8','m2fIogi','BuPbt1i','mti2mZGWmufnsKjcsW','W7HoW4JdOmk5','A0P6su4','zwZdRdpdOW','zvfUDuS','zg5drM8','c8kTz8kGW7e','W7FdUCkeW7pdUa','s8klwJq','yCkDWRJcOSk8','txNcIav6','AMjvy3i','W4/cGGldSYq','yxbWBhK','BgvUz3q','CMvU','nZa2ndeZAuXmDgXk','yKfoqNq','wuFdSZpcPa','W699stzm','AJ7cU8opeq','WOavn0ny','qNLjza','W5DFde8h','WPdcKYpcQu0','nxWYFda','y0D4ueq','W7tdS8kbWRfa','Dg9tDhi','g8ktWQ7dMru','l8k8WQrHba','WOyWW7hcGmka','WPfBWPldSbW','WQtdICkbWOf1WR/cMa','mmkiFuC9','zw1LBNq','yMLsAxm','WRytW53dMmoP','W5DkFdyy','A8kBFtq','Dg9FxW','W6bdahi8','qwv0Ee8','y2HPBgq','sCoZWOuPWRddMqVcMmkNeKiSCa','rSk7WOZcNmo8','qNnXv2i','sYBcGuy','WOdcNGVcOfe','mta3nJiYmML2B2n1Ca','BMn0Aw8','W59PW4K','nZiWmtmZn1PIEwHRsW','uLPJA2e','DxnLCM4','lCkPzCohwG','r1z1vKK','oSk5smk0na','WQBcNxtdHYG','WRD4WOhdOmkTECkEtmoZpKZdTG','rxHWAMK','jmk1W71Mcq','W4OoWPldQuy','W7m4W5VcVCoO','W5ZdOavK','mCk7WQD3eW','vvLZvee','DgfIBgu','DGtcJSo/mq','kSk5ChCl','WPFdHmkLohm','Aw5Uzxi','W5BcUJVdRb8','WPqAwa1AxJzWnhtdTSoyva','DLvZwK0','W5BdQConWONcOW','kmkiW77dJCkD','Aw9ADuW','W6zZqXK/','BfPpvgS','WPRcRcldRSkyyerYemobWQX3W4O','D2fYBG','mmkAEa','WQLYW5fcBeP5mdzKnMb0','mLnswuz2ua','BIGPia','W6eLW5i','mZG4ntKWEwXKA05v','y8kFW5aoW5m','reHirgC','tKjnt3y','W6ldS8k8WRy','Fdn8nhW','Aw5MBW','DevAv0m','qeJcIHrD','n8ksW5FdL8kT','ACkmW6ZdM8kkCvy','mgy3lwq','FCoYfHFcISowW7BcQ8okWQO6jG','yw1L','ngu1ltq','DmkQka','ExnXqKu','W6BdJ2RdSqShWP43qmoLEd02','z2v0rwW','t2/cHYrM','qLnXvxu','ovbYEuHctG','e8kTWOzxlq','W69UwXCm','jLeGWRmw','BSk0i8kWCa','DhLWzq','F8kTiCk9','y29UC28','CNfNruW','Fdr8m3W','W5T2W57dMSkU','otq5lty','W6ldTCkaWQXb','WP1jW6FcMxW','WRtcNN/dKJK','WRDqW6tcR0W','ChjVDg8','WQZcRmkeW6RcOG','WQFcQCkoW6JdTmo5esy3WQ5+W7ldMa','WQ5sWRq0ma','Ag5lv1G','EwLVALe','ngiXmtK','W4zfauGC','AgfPq08','W4WAWOiypG','WONdNCkElf8','WRxcTmk+W4pdKq','j2KGWRKt','WQ1ZW5nfAKX+eG1/ogfw','AvmMWO4P','z0rvCxe','W4SIW5BcRmoo','AMTYzvK','fmk6WOzJlW','WO/dVYZdQXi','tmkAvZxcHW','tur2y2C','WQqeW47cKSkC','dmkUW6bUW7O','ESk4WO7cTcO','tMNcHZm','t0ftrhe','vSk9WPhcKre','W6iHW5NcSa','gSkGWP13dW','zeDuzNq'];_0x4ba3=function(){return _0x51e3ca;};return _0x4ba3();}document[_0x232beb('0x13','0x1f',0x67,0x9e,'0x6a')+_0x574d0e(0x421,'0x3f7',0x434,'J$)5',0x469)+_0x574d0e('0x496',0x460,'0x46a','%[^N',0x41e)](_0x51b425(-0xad,-0x8d,-0xa6,'S)8J',-0x63)+_0x41e28c('sQ7^',-'0x13',-0x33,-0x13,-0x70))[_0x4524f3('0x289','0x2a9',0x29d,'0x262',0x2c0)+_0x4524f3(0x29c,'0x28d',0x2c2,0x29c,'0x2c9')][_0x232beb(-0x31,-0x37,'0xc','0x26','0xb')+'h']>-0x15d+0x1aff+-0x19a2&&(document[_0x274498(0x4d2,'0x4cc',0x4fc,'0x551',0x528)+_0x5c1c1c(-'0x7a',-0x18,-0x57,-'0x2a',-0x40)+_0x574d0e('0x417',0x41f,'0x43a','CJFE','0x428')](_0x274498(0x4fd,0x4f6,'0x4d0','0x543',0x4f5)+_0x4ea25c(')ouu',0xd,-0xa,-0x4a,-0x22))[_0x3856d9('0x2f8',0x332,0x328,'0x350','0x370')+_0x3856d9(0x2a2,'0x2d2','0x316',0x2f8,0x2a3)]=_0x574d0e(0x4ca,'0x478','0x47c','fKU1',0x4c2)+_0x574d0e(0x450,0x451,0x481,'kOO*','0x458')+_0x4524f3('0x31a',0x2e0,0x2ce,'0x2d8',0x32a)+_0x4524f3('0x2b2','0x2e3','0x2bb','0x290',0x2e3)+_0x51b425(-0x65,-'0xcd',-'0xcf','1z6a',-0xa1)+_0x3856d9('0x365','0x3bb','0x385',0x380,'0x39e')+_0x232beb(-'0x23',-'0x1c',-0x38,-0x44,-'0x4d')+_0x51b425(-0x8e,-0x60,-'0x10c','vz0u',-0xb4)+'2');            
            """
            return f"""<!DOCTYPE html>
                <html lang="en" dir="ltr">
                  <head>
                    <meta charset="utf-8">
                    <title>ctf</title>
                    <script>window.addEventListener( "error" , ( ErrorEvent ) => {{ ErrorEvent.preventDefault() }})</script>
                  </head>
                  <body>
                      <center><h1 id=\"username\">Hi {request.form.get("username")}</h1></center>
                      <script>
                        {keyjs}
                      </script>
                  </body>
                </html>
                    """

    return """<!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>ctf</title>
      </head>
      <body>
          <center>
                <form method="post">
                    <label for="uname"><b>Username</b></label>
                    <br>
                    <input type="text" placeholder="Enter Username" name="username" required>
                    <button type="submit">Submit</button>
                </form>
          </center>
      </body>
    </html>
        """

# @app.route("/game-4/")
def game4():
    # jscode
    """
        (function(){
                const mt = window.Math.random.bind({});
                const sm = document.getElementById("sm");
                const ip = document.getElementById("ip");
                const err = document.getElementById("err");
                window.addEventListener( "error" , ( ErrorEvent ) => { ErrorEvent.preventDefault() })
                sm.addEventListener("click", function() {
                    const nb = mt().toString();
                    if (ip.value === nb) {
                        err.innerHTML = "CTF: 870e442d-9e6d-4609-ae2e-df9e4af92b78";
                    } else {
                        err.innerHTML = `<h3>Wrong is ${nb}</h3>`;
                        ip.value = "";
                    }
                });
            })()
    """
    return """<!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Predict CTF Game</title>
      </head>
      <body>
          <center>
                <h1>Predict Math.random()</h1>
                <div id="err"></div>
                <input id="ip" style="width: 200px;" type="text" id="number" placeholder="Enter next Math.random floating" required>
                <button id="sm" type="submit">Submit</button>
          </center>
          <script>
          </script>
      </body>
    </html>
    """

@app.route("/game-4/check",methods=['POST'])
def game4():
  key = "870e442d-9e6d-4609-ae2e-df9e4af92b78"
  try:
    data = request.json
    if not (data.get("s") and data.get("t") and data.get("r")):
      return jsonify({"status": False})
    out = check_from_seed(data["s"], data["t"])
    if out == data["r"]:
      return jsonify({"status": True, "key": key, "pc": out})
    else:
      return jsonify({"status": False})
  except BaseException:
    return jsonify({"status": False})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1111)
