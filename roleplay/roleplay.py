import discord
from redbot.core import commands, Config
from random import randint
import aiohttp
import logging
import re

log = logging.getLogger("Roleplay")  # Thanks to Sinbad for the example code for logging
log.setLevel(logging.DEBUG)

console = logging.StreamHandler()

if logging.getLogger("red").isEnabledFor(logging.DEBUG):
    console.setLevel(logging.DEBUG)
else:
    console.setLevel(logging.INFO)
log.addHandler(console)

BaseCog = getattr(commands, "Cog", object)


class Roleplay(BaseCog):
    """Interact with people!"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=842364413)
        default_global = {
            "hugs": [
                "https://safebooru.org//images/1174/5ebeacd87b22a0c5949ecb875667ae75702c2fed.gif",
                "https://safebooru.org//images/848/4828fc43e39f52abd5bac6b299e822ae02786974.gif",
                "https://safebooru.org//images/160/ba09bc95bc05b4f47af22671950e66f085c7ea9e.gif",
                "https://cdn.weeb.sh/images/rJaog0FtZ.gif",
                "https://cdn.weeb.sh/images/Hyv6uOQPZ.gif",
                "https://cdn.weeb.sh/images/BJx2l0ttW.gif",
                "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif",
                "https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
                "https://media.giphy.com/media/3ZnBrkqoaI2hq/giphy.gif",
                "https://media.giphy.com/media/3o6ZsTopjMRVkJXAWI/giphy.gif",
                "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
                "https://media.giphy.com/media/vVA8U5NnXpMXK/giphy.gif",
                "https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif",
                "https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif",
                "https://media.giphy.com/media/C4gbG94zAjyYE/giphy.gif",
                "https://i.imgur.com/hM1LcZf.gif",
                "https://i.imgur.com/cRfX87T.gif",
                "https://cdn.weeb.sh/images/HyNJIaVCb.gif",
                "https://cdn.weeb.sh/images/ryMqdOXvZ.gif",
                "https://cdn.weeb.sh/images/ByuHsvu8z.gif",
                "https://cdn.weeb.sh/images/Hy4hxRKtW.gif",
                "https://cdn.weeb.sh/images/Sk2gmRZZG.gif",
                "https://cdn.weeb.sh/images/HkfgF_QvW.gif",
                "https://cdn.weeb.sh/images/HJTWcTNCZ.gif",
                "https://cdn.weeb.sh/images/rko9O_mwW.gif",
                "https://cdn.weeb.sh/images/rkx1dJ25z.gif",
                "https://cdn.weeb.sh/images/BkZngAYtb.gif",
                "https://tenor.com/view/anime-happy-girl-hug-shocked-gif-15788552",
                "https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif",
                "https://cdn-live.warthunder.com/uploads/5f/8f903f513e363b978150babb9297f4be9c90d8_mq/tumblr_n8wr8siAyx1qa94xto2_500.gif",
                "https://c.tenor.com/FTgiqwBBvr8AAAAC/anime-kirito.gif",
                "https://c.tenor.com/xURq6gggo18AAAAC/anime-are-you-lost.gif",
            ],
            "cuddle": [
                "https://cdn.weeb.sh/images/BkTe8U7v-.gif",
                "https://cdn.weeb.sh/images/SykzL87D-.gif",
                "https://cdn.weeb.sh/images/BywGX8caZ.gif",
                "https://cdn.weeb.sh/images/SJceIU7wZ.gif",
                "https://cdn.weeb.sh/images/SJn18IXP-.gif",
                "https://cdn.weeb.sh/images/B1Qb88XvW.gif",
                "https://cdn.weeb.sh/images/SJLkLImPb.gif",
                "https://cdn.weeb.sh/images/SyUYOJ7iZ.gif",
                "https://cdn.weeb.sh/images/rkBl8LmDZ.gif",
                "https://cdn.weeb.sh/images/B1S1I87vZ.gif",
                "https://cdn.weeb.sh/images/r1s9RqB7G.gif",
                "https://cdn.weeb.sh/images/Hy5y88mPb.gif",
                "https://cdn.weeb.sh/images/rkA6SU7w-.gif",
                "https://cdn.weeb.sh/images/r1A77CZbz.gif",
                "https://cdn.weeb.sh/images/SJYxIUmD-.gif",
                "https://cdn.weeb.sh/images/H1SfI8XwW.gif",
                "https://cdn.weeb.sh/images/rJCAH8XPb.gif",
                "https://cdn.weeb.sh/images/By03IkXsZ.gif",
                "https://cdn.weeb.sh/images/ryfyLL7D-.gif",
                "https://cdn.weeb.sh/images/BJwpw_XLM.gif",
                "https://cdn.weeb.sh/images/r1VzDkmjW.gif",
                "https://cdn.weeb.sh/images/HkzArUmvZ.gif",
                "https://cdn.weeb.sh/images/r1A77CZbz.gif",
                "https://gfycat.com/chubbydrearyfirefly",
            ],
            "kiss": [
                "https://cdn.weeb.sh/images/r1cB3aOwW.gif",
                "https://cdn.weeb.sh/images/Hy-oQl91z.gif",
                "https://cdn.weeb.sh/images/rJ6PWohA-.gif",
                "https://cdn.weeb.sh/images/rJrCj6_w-.gif",
                "https://78.media.tumblr.com/7255f36b2c31fac77542e8fe6837b408/tumblr_mokq94dAXR1s05qslo1_500.gif",
                "https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif",
                "https://c.tenor.com/dJU8aKmPKAgAAAAC/anime-kiss.gif",
                "https://c.tenor.com/g9HjxRZM2C8AAAAC/anime-love.gif",
                "https://c.tenor.com/tJEMsDqIYaAAAAAd/sao-kirito.gif",
                "https://c.tenor.com/olQHQvJ_sZUAAAAC/sword-art-online-kirito.gif",
                "https://c.tenor.com/sJ3YEq7sQ0AAAAAC/anime-kiss.gif",

            ],
            "slap": [
                "https://cdn.weeb.sh/images/H16aQJFvb.gif",
                "https://safebooru.org//images/192/fb1c45872a172ab384a22b9d9089b861d366564c.gif",
                "https://safebooru.org//images/118/968c5b9f042a5262c8c8628cd52a7a6a557e525d.gif",
                "https://media1.tenor.com/images/d14969a21a96ec46f61770c50fccf24f/tenor.gif?itemid=5509136",
                "https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956",
                "https://media1.tenor.com/images/4a6b15b8d111255c77da57c735c79b44/tenor.gif?itemid=10937039",
                "https://media1.tenor.com/images/153b2f1bfd3c595c920ce60f1553c5f7/tenor.gif?itemid=10936993",
                "https://media1.tenor.com/images/4fa82be21ffd18c99a9708ba209d56ad/tenor.gif?itemid=5318916",
                "https://media1.tenor.com/images/1ba1ea1786f0b03912b1c9138dac707c/tenor.gif?itemid=5738394",
                "https://i.imgur.com/EO8udG1.gif",
                "https://i.imgur.com/lMmn1wy.gif",
                "https://i.imgur.com/TuSUTg5.gif",
                "https://i.imgur.com/9Ql97mO.gif",
                "https://i.imgur.com/VBGqeIU.gif",
                "https://i.imgur.com/uPZwGFQ.gif",
                "https://i.imgur.com/eNiOIMB.gif",
                "https://i.imgur.com/gsAGyoI.gif",
                "https://cdn.weeb.sh/images/HyPjmytDW.gif",
                "https://cdn.weeb.sh/images/BJ8o71tD-.gif",
                "https://cdn.weeb.sh/images/BJLCX1Kw-.gif",
                "https://cdn.weeb.sh/images/rJvR71KPb.gif",
                "https://cdn.weeb.sh/images/SkZTQkKPZ.gif",
                "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
                "https://cdn.weeb.sh/images/BkxEo7ytDb.gif",
                "https://cdn.weeb.sh/images/B1fnQyKDW.gif",
                "https://cdn.weeb.sh/images/Bkj-oaV0Z.gif",
                "https://cdn.weeb.sh/images/r1siXJKw-.gif",
                "https://cdn.weeb.sh/images/r1VF-lcyz.gif",
                "https://cdn.weeb.sh/images/BJgsX1Kv-.gif",
                "https://cdn.weeb.sh/images/SkKn-xc1f.gif",
                "https://cdn.weeb.sh/images/Sk9mfCtY-.gif",
                "https://cdn.weeb.sh/images/ry_RQkYDb.gif",
                "https://cdn.weeb.sh/images/HkK2mkYPZ.gif",
                "https://cdn.weeb.sh/images/S1ylxxc1M.gif",
                "https://cdn.weeb.sh/images/SJdXoVguf.gif",
                "https://cdn.weeb.sh/images/ByHUMRNR-.gif",
                "https://cdn.weeb.sh/images/SkdyfWCSf.gif",
                "https://cdn.weeb.sh/images/rknn7Jtv-.gif",
                "https://cdn.weeb.sh/images/rJgTQ1tvb.gif",
                "https://cdn.weeb.sh/images/rkaqm1twZ.gif",
                "https://cdn.weeb.sh/images/ryn_Zg5JG.gif",
                "https://cdn.weeb.sh/images/SJ-CQytvW.gif",
                "https://i.gifer.com/9OQv.gif",
            ],
            "pat": [
                "https://cdn.weeb.sh/images/r180y1Yvb.gif",
                "http://i.imgur.com/10VrpFZ.gif",
                "http://i.imgur.com/x0u35IU.gif",
                "http://i.imgur.com/0gTbTNR.gif",
                "http://i.imgur.com/hlLCiAt.gif",
                "http://i.imgur.com/sAANBDj.gif",
                "https://i.imgur.com/10VrpFZ.gif",
                "https://i.imgur.com/x0u35IU.gif",
                "https://i.imgur.com/sAANBDj.gif",
                "https://i.imgur.com/wtxwpm1.gif",
                "https://i.imgur.com/3eR7weH.gif",
                "https://i.imgur.com/cK8Ro3x.gif",
                "https://i.imgur.com/qtHlt3n.gif",
                "https://i.imgur.com/bzzodCZ.gif",
                "https://cdn.weeb.sh/images/r180y1Yvb.gif",
                "https://cdn.weeb.sh/images/Sky1x1YwW.gif",
                "https://cdn.weeb.sh/images/r1Y5L6NCZ.gif",
                "https://cdn.weeb.sh/images/HJGQlJYwb.gif",
                "https://cdn.weeb.sh/images/rkBZkRttW.gif",
                "https://cdn.weeb.sh/images/rJavp1KVM.gif",
                "https://cdn.weeb.sh/images/r1AsJ1twZ.gif",
                "https://cdn.weeb.sh/images/ry1tlj2AW.gif",
                "https://cdn.weeb.sh/images/HyqTkyFvb.gif",
                "https://cdn.weeb.sh/images/ryLKqTVCW.gif",
                "https://cdn.weeb.sh/images/rJJXgJFDW.gif",
                "https://i.imgur.com/grAHcaB.gif",
                "https://cdn.weeb.sh/images/SJS1lyYwW.gif",
                "https://cdn.weeb.sh/images/rkbblkYvb.gif",
                "https://cdn.weeb.sh/images/H1s5hx0Bf.gif",
                "https://cdn.weeb.sh/images/rkSN7g91M.gif",
                "https://cdn.weeb.sh/images/rktsca40-.gif",
                "https://cdn.weeb.sh/images/ryh6x04Rb.gif",
                "https://cdn.weeb.sh/images/rkTC896_f.gif",
                "https://cdn.weeb.sh/images/r1lVQgcyG.gif",
            ],
            "lick": [
                "https://media1.tenor.com/images/c4f68fbbec3c96193386e5fcc5429b89/tenor.gif?itemid=13451325",
                "https://media1.tenor.com/images/ec2ca0bf12d7b1a30fea702b59e5a7fa/tenor.gif?itemid=13417195",
                "https://cdn.weeb.sh/images/HkEqiExdf.gif",
                "https://media1.tenor.com/images/5f73f2a7b302a3800b3613095f8a5c40/tenor.gif?itemid=10005495",
                "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727",
                "https://media1.tenor.com/images/069076cc8054bb8b114c5a37eec70a1f/tenor.gif?itemid=13248504",
                "https://media1.tenor.com/images/fc0ef2ba03d82af0cbd6c5815c3c83d5/tenor.gif?itemid=12141725",
                "https://media1.tenor.com/images/d702fa41028207c6523b831ec2db9467/tenor.gif?itemid=5990650",
                "https://media1.tenor.com/images/81769ee6622b5396d1489fb4667fd20a/tenor.gif?itemid=14376074",
                "https://media1.tenor.com/images/feeef4685f9307b76c78a22ba0a69f48/tenor.gif?itemid=8413059",
                "https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773",
            ],
            "highfive": [
                "https://media1.tenor.com/images/0ae4995e4eb27e427454526c05b2e3dd/tenor.gif?itemid=12376992",
                "https://media1.tenor.com/images/7b1f06eac73c36721912edcaacddf666/tenor.gif?itemid=10559431",
                "https://media1.tenor.com/images/c3263b8196afc25ddc1d53a4224347cd/tenor.gif?itemid=9443275",
                "https://media1.tenor.com/images/56d6725009312574e4798c732cebc5fe/tenor.gif?itemid=12312526",
                "https://media1.tenor.com/images/e96d2396570a2fadd9c83e284a1ca675/tenor.gif?itemid=5390726",
                "https://media1.tenor.com/images/106c8e64e864230341b59cc892b5a980/tenor.gif?itemid=5682921",
                "https://media1.tenor.com/images/b714d7680f8b49d69b07bc2f1e052e72/tenor.gif?itemid=13400356",
                "https://media1.tenor.com/images/0c23b320822afd5b1ce3faf01c2b9b69/tenor.gif?itemid=14137078",
                "https://media1.tenor.com/images/e2f299d05a7b1832314ec7a331440d4e/tenor.gif?itemid=5374033",
                "https://media1.tenor.com/images/16267f3a34efb42598bd822effaccd11/tenor.gif?itemid=14137081",
                "https://media1.tenor.com/images/9730876547cb3939388cf79b8a641da9/tenor.gif?itemid=8073516",
                "https://media1.tenor.com/images/ce85a2843f52309b85515f56a0a49d06/tenor.gif?itemid=14137077",
                "https://c.tenor.com/JBBZ9mQntx8AAAAC/anime-high-five.gif",
                "https://c.tenor.com/YCub_pFV2uAAAAAd/anime-high.gif",
                "https://c.tenor.com/Ajl4l3PWf8sAAAAC/high-five-anime.gif",
                "https://c.tenor.com/H2x6-sF50jUAAAAC/anime-kirito.gif",
                "https://c.tenor.com/5N0TrhayLwIAAAAC/polnareff-handshake.gif",
            ],
            "feed": [
                "https://media1.tenor.com/images/93c4833dbcfd5be9401afbda220066ee/tenor.gif?itemid=11223742",
                "https://media1.tenor.com/images/33cfd292d4ef5e2dc533ff73a102c2e6/tenor.gif?itemid=12165913",
                "https://media1.tenor.com/images/72268391ffde3cd976a456ee2a033f46/tenor.gif?itemid=7589062",
                "https://media1.tenor.com/images/4b48975ec500f8326c5db6b178a91a3a/tenor.gif?itemid=12593977",
                "https://media1.tenor.com/images/187ff5bc3a5628b6906935232898c200/tenor.gif?itemid=9340097",
                "https://media1.tenor.com/images/15e7d9e1eb0aad2852fabda1210aee95/tenor.gif?itemid=12005286",
                "https://media1.tenor.com/images/d08d0825019c321f21293c35df8ed6a9/tenor.gif?itemid=9032297",
                "https://media1.tenor.com/images/571da4da1ad526afe744423f7581a452/tenor.gif?itemid=11658244",
                "https://media1.tenor.com/images/6bde17caa5743a22686e5f7b6e3e23b4/tenor.gif?itemid=13726430",
                "https://media1.tenor.com/images/fd3616d34ade61e1ac5cd0975c25a917/tenor.gif?itemid=13653906",
                "https://imgur.com/v7jsPrv",
                "https://c.tenor.com/Aflxvrwa0woAAAAC/kawaii-wholesome.gif",
            ],
            "tickle": [
                "https://media1.tenor.com/images/02f62186ccb7fa8a2667f3216cfd7e13/tenor.gif?itemid=13269751",
                "https://media1.tenor.com/images/d38554c6e23b86c81f8d4a3764b38912/tenor.gif?itemid=11379131",
                "https://media1.tenor.com/images/05a64a05e5501be2b1a5a734998ad2b2/tenor.gif?itemid=11379130",
                "https://c.tenor.com/WBwonvADeCoAAAAC/mareva-tickle.gif",
                "https://c.tenor.com/9KCaFFBc_lkAAAAC/anime-tickle.gif",
                "https://c.tenor.com/PXL1ONAO9CEAAAAC/tickle-laugh.gif",
                "https://imgur.com/bt2ZRjJ",
                "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7bbbe46f-5285-46b1-804e-337939538ae7/dbmlvcf-8dcf9ae8-65bc-48f0-9d95-d982fd1be597.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzdiYmJlNDZmLTUyODUtNDZiMS04MDRlLTMzNzkzOTUzOGFlN1wvZGJtbHZjZi04ZGNmOWFlOC02NWJjLTQ4ZjAtOWQ5NS1kOTgyZmQxYmU1OTcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.lv0IH_Ak5xfjRa8xbPbKRZmfGpRPuZw3aO52CHoVwKk",
            ],
            "poke": [
                "https://media1.tenor.com/images/3b2bfd09965bd77f2a8cb9ba59cedbe4/tenor.gif?itemid=5607667",
                "https://media1.tenor.com/images/514efe749cb611eb382713596e3427d8/tenor.gif?itemid=13054528",
                "https://media1.tenor.com/images/8795ff617de989265907eed8029a99a3/tenor.gif?itemid=14629871",
                "https://media1.tenor.com/images/1e0ea8b241a7db2b9c03775133138733/tenor.gif?itemid=10064326",
                "https://media1.tenor.com/images/90f68d48795c51222c60afc7239c930c/tenor.gif?itemid=8701034",
                "https://media1.tenor.com/images/01b264dc057eff2d0ee6869e9ed514c1/tenor.gif?itemid=14346763",
                "https://media1.tenor.com/images/f8a48a25f47d5d12342705c7c87368bb/tenor.gif?itemid=14134415",
                "https://media.tenor.com/images/6b5c1554a6ee9d48ab0392603bab8a8e/tenor.gif",
            ],
            "smug": [
                "https://cdn.nekos.life/v3/sfw/gif/smug/smug_027.gif",
                "https://cdn.nekos.life/v3/sfw/gif/smug/smug_057.gif",
                "https://i.kym-cdn.com/photos/images/original/001/087/562/93c.gif",
                "https://i.kym-cdn.com/photos/images/newsfeed/001/161/167/eda.gif",
                "https://media1.tenor.com/images/d9b3127da3f9419cbb28f9f7c00860d8/tenor.gif?itemid=9588226",
                "https://c.tenor.com/p2dWs1LsL_wAAAAC/vampire-anime-girl.gif",
                "https://c.tenor.com/MQ610z61FU4AAAAC/chika-love-is-war.gif",
                "https://c.tenor.com/rcDotvVDRK4AAAAC/smug-kurumi-ebisuzawa.gif",
                "https://c.tenor.com/Zv9fBbsIWjAAAAAC/fanning-smug.gif",
                "https://c.tenor.com/ZaxUeXcUtDkAAAAC/shrug-smug.gif",
                "https://c.tenor.com/SGMyv6dZ2XMAAAAC/you-got-it-thumbs-up-anime.gif",
                "https://c.tenor.com/8M4T11FxGI0AAAAC/anime-smug.gif",
                "https://c.tenor.com/3VC5WFlytlUAAAAC/anime-anime-smug-face.gif",
                "https://c.tenor.com/HqSfHfC6fUsAAAAC/ram-re-zero.gif",
                "https://c.tenor.com/Thm-jFJZJ-4AAAAC/rossweisse-dxd.gif",
                "https://c.tenor.com/nC-6JLX1EsIAAAAC/anime-smug.gif",
            ],
            "kill": [
                "https://c.tenor.com/A4w9SaoFaVUAAAAC/akame.gif",
                "https://c.tenor.com/AGTqt-wXyiEAAAAC/nichijou-minigun.gif",
                "https://c.tenor.com/Ssauo2VG5qYAAAAC/akame-akame-of-demon-sword-murasame.gif",
                "https://c.tenor.com/SX5B_1kKYYcAAAAC/akame-akamegakill.gif",
                "https://c.tenor.com/bznBkYdhexcAAAAC/fire-arm-fire.gif",
            ],
            "murder":[
                "https://c.tenor.com/pwPMerSJ-6gAAAAC/happy-sugar-life-%E3%83%8F%E3%83%83%E3%83%94%E3%83%BC%E3%82%B7%E3%83%A5%E3%82%AC%E3%83%BC%E3%83%A9%E3%82%A4%E3%83%95.gif",
                "https://c.tenor.com/Nn6cRTGDcrIAAAAC/danganronpa-nanami.gif",
                "https://data.whicdn.com/images/37008393/original.gif",
                "https://c.tenor.com/Ze50E1rW44UAAAAC/akudama-drive.gif",
                "https://c.tenor.com/NbBCakbfZnkAAAAC/die-kill.gif",
                "https://c.tenor.com/G4SGjQE8wCEAAAAC/mikey-tokyo.gif",
            ],
            "spank": [
                "https://c.tenor.com/gScnebhgJn4AAAAC/taritari-anime-spank.gif",
                "https://c.tenor.com/5SPNhg5O38oAAAAC/anime-rikka-takanashi.gif",
                "https://c.tenor.com/uER90n0laEEAAAAC/anime-spanking.gif",
                "https://c.tenor.com/jq-PoRYhLYwAAAAC/anime-waifu.gif",
                "https://c.tenor.com/4RIbgFCLRrUAAAAd/rikka-takanashi-bad-girl.gif",
                "https://c.tenor.com/jwSXb8QcklwAAAAM/anime-waifu.gif",
                "https://i.makeagif.com/media/7-21-2017/IgmqSc.gif",
                "https://c.tenor.com/Ep5dFoM0h5gAAAAC/bad-spank.gif",
                "https://c.tenor.com/zpK3DZkGjtYAAAAC/ueno-anime.gif",
                "https://24.media.tumblr.com/38094ad70dcf7722b7aceb6bbd82507f/tumblr_mqqu76NpRP1srsfpho1_400.gif",
                "https://i.makeagif.com/media/11-20-2013/WveGOX.gif",
            ],
            "punch": [
                "https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif",
                "https://c.tenor.com/aEX1wE-WrEMAAAAC/anime-right-in-the-stomach.gif",
                "https://c.tenor.com/EvBn8m3xR1cAAAAC/toradora-punch.gif",
                "https://c.tenor.com/o8RbiF5-9dYAAAAC/killua-hxh.gif",
                "https://c.tenor.com/UH8Jnl1W3CYAAAAC/anime-punch-anime.gif",
                "https://c.tenor.com/s0bU-NO1QIQAAAAC/anime-punch.gif",
                "https://c.tenor.com/wYyB8BBA8fIAAAAM/some-guy-getting-punch-anime-punching-some-guy-anime.gif",
                "https://c.tenor.com/F_PdE5FZAjEAAAAC/asuna-punch.gif",
                "https://c.tenor.com/H04N4qqJhZ0AAAAC/golden-boy-anime.gif",
                "https://c.tenor.com/qrNB6eZr3HQAAAAC/jojo-bizarre-jojos-adventure.gif",
                "https://c.tenor.com/Hf9MuA4oUrQAAAAC/star-platinum-ora.gif",
                "https://c.tenor.com/mOYMcLekRWQAAAAC/hamon-punch-jojo.gif",
                "https://c.tenor.com/_zZe_wgU1dcAAAAC/ora-jojo.gif",
                "https://c.tenor.com/zQJvL4bppdsAAAAC/punch-diavolo.gif",
                "https://c.tenor.com/Q2A-CA2vGpwAAAAC/jojos-bizarre-adventure-jojo.gif",
            ],
            "grope": [
                "https://c.tenor.com/Lp0DoHwREjAAAAAC/sao-sword-art-online.gif",
                "https://c.tenor.com/Jb_F2aFPQEkAAAAC/grip-death-grip.gif",
                "https://c.tenor.com/EvQp572ilIEAAAAC/nogamenolife-shiro.gif",
                "https://c.tenor.com/hi_bhCiKFYgAAAAC/grope-anime.gif",
                "https://c.tenor.com/8werfp2g6sUAAAAC/oppai-anime.gif",
                "https://c.tenor.com/19rq6zteNnQAAAAC/anime-touch.gif",
                "https://c.tenor.com/JC4LjDJ8ZuwAAAAC/grab-meat.gif",
                "https://c.tenor.com/O36Sl6bYnggAAAAC/anime-touch.gif",
                "https://c.tenor.com/FtNQmchw_IwAAAAC/anime-touch.gif",
                "https://c.tenor.com/hRCafFw1KZwAAAAC/anime-seras-victoria.gif",
                "https://c.tenor.com/0E-ttG8cHA8AAAAC/boob-grab-anime.gif",
                "https://c.tenor.com/5CRy73KdjjoAAAAC/tohru-dragon-maid.gif",
            ],
            "sleep": [
                "https://c.tenor.com/qlxdd9DVMHUAAAAC/willcore-kon.gif",
                "https://c.tenor.com/EES7ZFe56w0AAAAC/anime-sleep.gif",
                "https://c.tenor.com/IXA8luG-tccAAAAC/anime-sleep.gif",
                "https://c.tenor.com/HItBOocy6ikAAAAC/umaru-sleeping.gif",
                "https://c.tenor.com/nlARLJ6M_t8AAAAC/mashiro-drool.gif",
                "https://c.tenor.com/0i6HB03LuE4AAAAC/anime-sleeping.gif",
                "https://c.tenor.com/hz6VBkoTLJIAAAAC/sleep-resting.gif",
                "https://c.tenor.com/jrBQmuo2elMAAAAC/anime-sleep.gif",
                "https://c.tenor.com/e_d1mTN6kHUAAAAC/yamaguchi-tadashi-haikyuu.gif",
                "https://c.tenor.com/paUFtJtPwcAAAAAC/sleep-anime.gif",
                "https://c.tenor.com/EO_k8kxEyTgAAAAC/noela-anime.gif",
            ],
            "kick": [
                "https://c.tenor.com/Lyqfq7_vJnsAAAAC/kick-funny.gif",
                "https://c.tenor.com/EcdG5oq7MHYAAAAC/shut-up-hit.gif",
                "https://c.tenor.com/4zwRLrLMGm8AAAAC/chifuyu-chifuyu-kick.gif",
                "https://c.tenor.com/4F6aGlGwyrwAAAAC/sdf-avatar.gif",
                "https://c.tenor.com/kvxt9X-gXqQAAAAC/anime-clannad.gif",
                "https://c.tenor.com/mEgexCY-65QAAAAC/toradora-taiga.gif",
                "https://c.tenor.com/7te6q4wtcYoAAAAC/mad-angry.gif",
                "https://c.tenor.com/2l13s2uQ6GkAAAAC/kick.gif",
                "https://c.tenor.com/QxoBMmf2bRwAAAAC/jormungand-anime.gif",
                "https://c.tenor.com/aAvEGbU2WK0AAAAC/maria-osawa-canaan.gif",
                "https://c.tenor.com/bpgPEPfFlnIAAAAC/yeet-anime.gif",
                "https://c.tenor.com/R2t36ofOQ9gAAAAC/anime.gif",
                "https://c.tenor.com/LEgnGzli8VMAAAAC/anime-fight.gif",
                "https://c.tenor.com/KlvWYCEumXAAAAAC/kick-anime.gif",
                "https://c.tenor.com/b5GclJfU4e0AAAAC/anime-tough.gif",
                "https://c.tenor.com/tuOSy0KcR6EAAAAC/kick-jotaro-kujo.gif",
                "https://c.tenor.com/VFo0I0Po0zoAAAAC/jojos-bizarre-adventure-golden-experience.gif",
            ],
            "bow": [
                "https://c.tenor.com/eDZrsiuxSDQAAAAC/ban-bowing.gif",
                "https://c.tenor.com/w4SX4j1CdZkAAAAC/bow-anime.gif",
                "https://c.tenor.com/lpxKv7slwfgAAAAC/mashu-kyrielight-fate-grand-order.gif",
                "https://c.tenor.com/lSwVx09EvFkAAAAC/jasorry-jaanime.gif",
                "https://c.tenor.com/2uPTZEqzFzoAAAAC/edgeworth-anime.gif",
                "https://c.tenor.com/APIsjPJxtAUAAAAC/anime-sorry.gif",
                "https://c.tenor.com/6NMWhoAJrQMAAAAC/anime-bow-down.gif",
                "https://c.tenor.com/iP6_Nm7Mj7UAAAAC/boku-no-hero-academia-gomen.gif",
                "https://c.tenor.com/TZ0cJkL8_j8AAAAC/inazuma-eleven-go-inago.gif",
                "https://c.tenor.com/q2yqXbpuII8AAAAC/thank-you-deku-bow.gif",
                "https://c.tenor.com/Fe0OQTDDN38AAAAC/anime-bow.gif",
                "https://c.tenor.com/fljs-c50YBgAAAAC/black-lagoon.gif",
                "https://c.tenor.com/47GM87fDYNYAAAAC/shouko-nishimiya-bow.gif",
                "https://c.tenor.com/IBK2-Nd9MaUAAAAC/anime-maid.gif",
            ]
        }
        self.config.register_global(**default_global)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def hugs(self, ctx, *, user: discord.Member):
        """Hugs a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self hugging!")
        images = await self.config.hugs()

        nekos = await self.fetch_nekos_life(ctx, "hug")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddles a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self cuddling!")
        images = await self.config.cuddle()

        nekos = await self.fetch_nekos_life(ctx, "cuddle")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} cuddles {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self kissing!")
        images = await self.config.kiss()

        nekos = await self.fetch_nekos_life(ctx, "kiss")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} kisses {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx, *, user: discord.Member):
        """Slaps a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self slapping!")
        images = await self.config.slap()

        nekos = await self.fetch_nekos_life(ctx, "slap")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} slaps {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, *, user: discord.Member):
        """Pats a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self patting!")
        images = await self.config.pat()

        nekos = await self.fetch_nekos_life(ctx, "pat")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} pats {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def lick(self, ctx, *, user: discord.Member):
        """Licks a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self licking!")
        images = await self.config.lick()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} licks {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def highfive(self, ctx, *, user: discord.Member):
        """Highfives a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self highfiving!")
        images = await self.config.highfive()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} highfives {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def feed(self, ctx, *, user: discord.Member):
        """Feeds a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self feeding!")
        images = await self.config.feed()

        nekos = await self.fetch_nekos_life(ctx, "feed")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} feeds {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickles a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self tickling!")
        images = await self.config.tickle()

        nekos = await self.fetch_nekos_life(ctx, "tickle")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} tickles {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, *, user: discord.Member):
        """Pokes a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("No self poking!")
        images = await self.config.poke()

        nekos = await self.fetch_nekos_life(ctx, "poke")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} pokes {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        """Be smug towards someone!"""

        author = ctx.message.author
        images = await self.config.smug()

        smug = await self.fetch_nekos_life(ctx, "smug")
        images.extend(smug)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} is smug**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kill(self, ctx, *, user: discord.Member):
        """Kills a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("Don't suicide man!")
        images = await self.config.kill()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} just killed {user.mention}**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def murder(self, ctx, *, user: discord.Member):
        """Murders a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("Don't suicide man!")
        images = await self.config.murder()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} just murdered {user.mention}**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def spank(self, ctx, *, user: discord.Member):
        """Spanks a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("Don't spank yourself!")
        images = await self.config.spank()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} spanks {user.mention}**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def punch(self, ctx, *, user: discord.Member):
        """Punches a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("Why are you hitting yourself?!?")
        images = await self.config.punch()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} punched {user.mention}**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def grope(self, ctx, *, user: discord.Member):
        """Gropes a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("Go to horny jail **bonk**")
        images = await self.config.grope()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} groped {user.mention}**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def sleep(self, ctx):
        """Sleep"""

        author = ctx.message.author
        images = await self.config.sleep()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} is sleeping.**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def bow(self, ctx, *, user: discord.Member):
        """Bows down to a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("You're not your own King, **I AM**")
        images = await self.config.bow()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} bowed down to {user.mention}**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kicks(self, ctx, *, user: discord.Member):
        """Kicks a user!"""

        author = ctx.message.author
        if author == user:
            return await ctx.send("Don't kick yourself!")
        images = await self.config.kick()

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} kicked {user.mention}**"
        embed.set_footer(text="Made by Yuuki")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    async def fetch_nekos_life(self, ctx, rp_action):

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nekos.dev/api/v3/images/sfw/gif/{rp_action}/?count=20") as resp:
                try:
                    content = await resp.json(content_type=None)
                except (ValueError, aiohttp.ContentTypeError) as ex:
                    log.debug("Pruned by exception, error below:")
                    log.debug(ex)
                    return []

        if content["data"]["status"]["code"] == 200:
            return content["data"]["response"]["urls"]

